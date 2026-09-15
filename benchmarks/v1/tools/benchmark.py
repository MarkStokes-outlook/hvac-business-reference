#!/usr/bin/env python3
"""Implementation-neutral benchmark administration. Python standard library only."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import shutil
import sys

SUITE = Path(__file__).resolve().parents[1]

def read(path):
    return json.loads(Path(path).read_text())

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def fail(message):
    raise ValueError(message)

def require(condition, message):
    if not condition:
        fail(message)

def manifest():
    return read(SUITE / 'suite-manifest.json')

def scenario(sid):
    entries = [s for s in manifest()['scenarios'] if s['id'] == sid]
    require(len(entries) == 1, f'Unknown/nonunique scenario: {sid}')
    return entries[0]

def oracle(sid):
    return read(SUITE / scenario(sid)['path'] / 'hidden/oracle.json')

def release_files():
    result = {}
    for p in sorted(SUITE.rglob('*')):
        require(not p.is_symlink(), f'Symlink not allowed in frozen release: {p}')
        if p.is_file() and p != SUITE / 'release-lock.json':
            result[str(p.relative_to(SUITE))] = sha(p)
    return result

def lock():
    files = release_files()
    fingerprint = hashlib.sha256(json.dumps(files, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    result = dict(suite_version=manifest()['version'], canonical_baseline=manifest()['canonical_baseline'],
                  files=files, fingerprint=fingerprint)
    (SUITE / 'release-lock.json').write_text(json.dumps(result, indent=2) + '\n')
    return dict(files=len(files), fingerprint=fingerprint)

def validate(repo, require_lock=True):
    repo = Path(repo).resolve()
    m = manifest()
    require(20 <= len(m['scenarios']) <= 30, 'V1 scenario count outside intended range')
    ids = [s['id'] for s in m['scenarios']]
    require(len(ids) == len(set(ids)), 'Duplicate scenario IDs')
    require(ids == [f'B{i:03}' for i in range(1, len(ids)+1)], 'Unexpected V1 ID sequence')
    docs = {x['path']: x['sha256'] for x in m['canonical_documents']}
    actual = {}
    for p in (repo / 'docs').rglob('*'):
        require(not p.is_symlink(), f'Canonical symlink not allowed: {p}')
        if p.is_file() and p.name != '.DS_Store':
            actual[str(p.relative_to(repo))] = sha(p)
    require(actual == docs, 'Canonical docs drift/missing/additional file: review and version dependencies before administration')
    evidence = read(SUITE / 'hidden/evidence-index.json')
    eids = {e['id']: e for e in evidence}
    require(len(eids) == len(evidence), 'Duplicate evidence IDs')
    for e in evidence:
        require(e['path'] in docs, f'Noncanonical evidence: {e["id"]}')
        lines = (repo / e['path']).read_text().splitlines(keepends=True)
        text = ''.join(lines[e['start_line']-1:e['end_line']])
        require(text == e['section_text'], f'Evidence section text mismatch: {e["id"]}')
        require(hashlib.sha256(text.encode()).hexdigest() == e['section_sha256'], f'Evidence section hash mismatch: {e["id"]}')
        require(text.splitlines()[0].lstrip('#').strip() == e['heading'], f'Evidence heading mismatch: {e["id"]}')
    checkpoints = 0
    for s in m['scenarios']:
        d = SUITE / s['path']
        require(d.is_dir() and d.is_relative_to(SUITE / 'scenarios'), f'Invalid scenario path: {s["id"]}')
        for name in ['README.md', 'public/case.md', 'public/task.md', 'public/fixtures.json', 'hidden/rubric.md',
                     'hidden/reference-reasoning.md', 'hidden/oracle.json', 'hidden/admin-events.json']:
            require((d / name).is_file(), f'Missing scenario file: {s["id"]}/{name}')
        o = read(d / 'hidden/oracle.json')
        require(o['scenario_id'] == s['id'] and o['version'] == s['version'], f'Oracle identity/version: {s["id"]}')
        require(len(o['criteria']) == 5 and sum(c['points'] for c in o['criteria']) == 100, 'Criterion weights do not total 100')
        seen = set()
        rubric = (d / 'hidden/rubric.md').read_text()
        reasoning = (d / 'hidden/reference-reasoning.md').read_text()
        for c in o['criteria']:
            require(len(c['checkpoints']) == 2 and sum(x['points'] for x in c['checkpoints']) == c['points'], 'Checkpoint weights mismatch')
            require(c['expected_outcome'] in rubric and c['expected_outcome'] in reasoning, 'Rendered outcome differs from oracle')
            for ck in c['checkpoints']:
                require(ck['id'] not in seen and ck['id'].startswith(s['id']+'-C'), 'Duplicate/foreign checkpoint')
                seen.add(ck['id'])
                require(ck['stage'] in range(1, s['stages']+1), 'Checkpoint stage invalid')
                require(ck['outcome'] in rubric and ck['outcome'] in reasoning, 'Rendered checkpoint differs from oracle')
                require(ck['evidence_ids'] and set(ck['evidence_ids']) <= set(eids), 'Checkpoint evidence missing/unknown')
                checkpoints += 1
        require(o['acceptable_alternatives'] and o['critical_failures'] and o['uncertainty'], 'Missing semantic controls')
        for item in o['acceptable_alternatives'] + o['uncertainty'] + o['prohibited_outcomes']:
            require(item['evidence_ids'] and set(item['evidence_ids']) <= set(s['evidence_ids']), 'Semantic alternative/uncertainty/prohibition evidence missing')
        for f in o['critical_failures']:
            require(f['outcome'] in rubric and f['outcome'] in reasoning, 'Rendered critical failure differs from oracle')
            require(f['evidence_ids'] and set(f['evidence_ids']) <= set(eids), 'Failure evidence missing/unknown')
        require(set(s['evidence_ids']) == set(o['evidence_ids']), 'Manifest/oracle dependencies differ')
        for eid in s['evidence_ids']:
            require(eid in reasoning and eids[eid]['path'] in reasoning, 'Missing canonical evidence map')
        fixtures = read(d / 'public/fixtures.json')
        case = (d / 'public/case.md').read_text()
        require(fixtures['scenario_id'] == s['id'] and fixtures['stage'] == 1, 'Fixture identity/stage mismatch')
        for record in fixtures['records']:
            require(record['id'] in case and record['statement'] in case, 'Fixture JSON/Markdown differs')
        require(fixtures['request'] in case and all(x in case for x in fixtures['unknowns']), 'Fixture request/unknowns differ')
        events = read(d / 'hidden/admin-events.json')['events']
        require([e['stage'] for e in events] == list(range(2, s['stages']+1)), 'Events do not cover required later stages')
        for event in events:
            require(set(event) == {'stage', 'time', 'facts', 'request'}, 'Non-neutral/unknown event field')
            require(event['facts'] and event['request'], 'Empty event input')
    release = SUITE / 'release-lock.json'
    if require_lock:
        require(release.exists(), 'Release lock missing; author/reviewer must intentionally freeze first')
    if release.exists():
        pinned = read(release)
        files = release_files()
        require(files == pinned['files'], 'Frozen release changed: review, version and relock before administration')
        fingerprint = hashlib.sha256(json.dumps(files, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
        require(fingerprint == pinned['fingerprint'], 'Release fingerprint mismatch')
        require(pinned['canonical_baseline'] == m['canonical_baseline'] and pinned['suite_version'] == m['version'], 'Lock provenance mismatch')
    return dict(valid=True, scenarios=len(ids), checkpoints=checkpoints, canonical_files=len(docs), evidence_sections=len(eids),
                release_locked=release.exists())

def export(repo, sid, stage, destination):
    validate(repo)
    s = scenario(sid)
    require(stage in range(1, s['stages']+1), f'No stage {stage} for {sid}')
    repo = Path(repo).resolve()
    target = Path(destination)
    require(not target.is_symlink(), 'Export destination cannot be symlink')
    target = target.resolve()
    require(not target.is_relative_to(repo) and not target.is_relative_to(SUITE), 'Export destination must be outside repository/suite')
    require(not target.exists() or (target.is_dir() and not any(target.iterdir())), 'Export destination must be absent or empty; do not mix hidden/stale input')
    target.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SUITE / 'submission-contract.md', target / 'submission-contract.md')
    if stage == 1:
        for document in manifest()['canonical_documents']:
            source = repo / document['path']
            copied = target / document['path']
            copied.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, copied)
        # Exact allowlist: never copy a scenario directory or suite metadata.
        for name in ['case.md', 'task.md', 'fixtures.json']:
            shutil.copyfile(SUITE / s['path'] / 'public' / name, target / name)
    else:
        event = next(e for e in read(SUITE / s['path'] / 'hidden/admin-events.json')['events'] if e['stage'] == stage)
        neutral = dict(scenario_id=sid, **event)
        (target / 'event.json').write_text(json.dumps(neutral, indent=2, ensure_ascii=False)+'\n')
        (target / 'event.md').write_text(f'# {sid} stage {stage}\n\n{event["time"]}\n\n'+'\n\n'.join(event['facts'])+'\n\n## Request\n\n'+event['request']+'\n')
    return dict(scenario=sid, stage=stage, exported_files=len([p for p in target.rglob('*') if p.is_file()]), destination=str(target))

def check_assessment(path):
    a = read(path)
    s = scenario(a['scenario_id'])
    o = oracle(s['id'])
    m = manifest()
    for key in ['run_id', 'observation_bundle_sha256', 'evaluator', 'raw_assessment_reference', 'confidence', 'adjudication']:
        require(a.get(key), f'Missing assessment provenance: {key}')
    require(re.fullmatch('[0-9a-f]{64}', a['observation_bundle_sha256']), 'Invalid observation bundle hash')
    require(a['scenario_version'] == s['version'] and a['suite_version'] == m['version'] and a['canonical_baseline'] == m['canonical_baseline'], 'Assessment version/baseline mismatch')
    require(a['release_fingerprint'] == read(SUITE / 'release-lock.json')['fingerprint'], 'Assessment release fingerprint mismatch')
    require(all(a['evaluator'].get(k) for k in ['id', 'model', 'configuration', 'date']), 'Evaluator identity/configuration/date missing')
    expected = {ck['id']: ck for c in o['criteria'] for ck in c['checkpoints']}
    found = a['checkpoints']
    require(len(found) == len(expected) and {ck['id'] for ck in found} == set(expected), 'Assessment must score all ten unique checkpoints')
    raw = 0
    for ck in found:
        require(type(ck['score']) is int and ck['score'] in [0, 5, 10], f'Invalid score: {ck["id"]}')
        require(ck['reason'].strip() and ck['observation_refs'], f'Missing observation/reason for score or absence: {ck["id"]}')
        require(ck['evidence_ids'] and set(ck['evidence_ids']) <= set(expected[ck['id']]['evidence_ids']), f'Unknown/unsupported policy IDs: {ck["id"]}')
        raw += ck['score']
    cfs = {f['id']: f for f in o['critical_failures']}
    invoked = a['critical_failures']
    require(len({f['id'] for f in invoked}) == len(invoked), 'Duplicate invoked critical failure')
    for f in invoked:
        require(f['id'] in cfs, 'Undeclared critical failure')
        require(f.get('observation_refs') and f.get('reason', '').strip(), 'Critical failure needs actual trace and reason')
        require(f.get('evidence_ids') and set(f['evidence_ids']) <= set(cfs[f['id']]['evidence_ids']), 'Critical failure policy evidence invalid')
    stages = a['completed_stages']
    require(stages == sorted(set(stages)) and all(type(x) is int and x in range(1,s['stages']+1) for x in stages), 'Invalid/duplicate completed stages')
    require(a['judgement_status'] in ['resolved', 'unresolved'], 'Unknown judgement status')
    require(not a.get('uncertain_judgements') or a['judgement_status'] == 'unresolved', 'Uncertain judgements cannot be reported as resolved')
    complete = stages == list(range(1,s['stages']+1)) and a['judgement_status'] == 'resolved'
    effective = min(raw,59) if invoked else raw
    adjudication = a['adjudication']
    require(adjudication.get('status') in ['independent', 'final', 'unresolved'], 'Adjudication status invalid')
    if adjudication['status'] == 'final':
        require(len(set(adjudication.get('original_assessment_refs', []))) >= 2, 'Final record needs at least two independent originals')
        require(isinstance(adjudication.get('decisions'), list), 'Final record requires explicit adjudication decisions (empty only if originals agree)')
    return dict(scenario_id=s['id'],raw_score=raw,effective_score=effective,critical_failures=[f['id'] for f in invoked],
                complete=complete,passed=complete and effective>=75 and not invoked,adjudication_status=adjudication['status'])

def compare(first, second):
    check_assessment(first)
    check_assessment(second)
    a, b = read(first), read(second)
    for key in ['run_id','scenario_id','scenario_version','suite_version','canonical_baseline','release_fingerprint','observation_bundle_sha256','completed_stages']:
        require(a[key] == b[key], f'Non-comparable assessments: {key}')
    require(a['evaluator']['id'] != b['evaluator']['id'], 'Independent assessments need distinct evaluator IDs')
    aa, bb = ({x['id']:x for x in d['checkpoints']} for d in [a,b])
    differences = [dict(id=k,first=aa[k]['score'],second=bb[k]['score'],first_reason=aa[k]['reason'],second_reason=bb[k]['reason']) for k in aa if aa[k]['score']!=bb[k]['score']]
    cf_a = sorted(f['id'] for f in a['critical_failures'])
    cf_b = sorted(f['id'] for f in b['critical_failures'])
    return dict(scenario_id=a['scenario_id'],checkpoint_disagreements=differences,critical_failure_disagreement=cf_a!=cf_b,
                first_failures=cf_a,second_failures=cf_b,judgement_status_disagreement=a['judgement_status']!=b['judgement_status'],
                adjudication_required=bool(differences or cf_a!=cf_b or a['judgement_status']!=b['judgement_status']),
                note='Equal scores do not establish independent conduct or validate evidence; preserve originals and review alternative rationales.')

def aggregate(directory):
    directory = Path(directory)
    require(directory.is_dir(), 'Assessment directory missing')
    results = []
    records = []
    for p in sorted(directory.glob('*.json')):
        records.append(read(p))
        results.append(check_assessment(p))
    require(results, 'No assessments')
    require(len({r['scenario_id'] for r in results}) == len(results), 'Duplicate scenarios; aggregate final records, not independent originals')
    require(len({a['run_id'] for a in records}) == 1, 'Mixed run IDs cannot create a suite verdict')
    expected = {s['id'] for s in manifest()['scenarios']}
    missing = sorted(expected-{r['scenario_id'] for r in results})
    pending = [r['scenario_id'] for r in results if not r['complete'] or r['adjudication_status']!='final']
    complete = not missing and not pending
    passed = complete and all(r['passed'] for r in results)
    verdict = ('fit-for-purpose demonstrated within V1 scope' if passed else 'material business gaps demonstrated') if complete else 'assessment incomplete or unresolved'
    return dict(suite_version=manifest()['version'],release_status=manifest()['status'],result_label='pilot until freeze-checklist approvals recorded',
                assessed=len(results),expected=len(expected),missing=missing,pending=pending,
                raw_mean=sum(r['raw_score'] for r in results)/len(results),effective_mean=sum(r['effective_score'] for r in results)/len(results),
                failed_scenarios=[r['scenario_id'] for r in results if r['complete'] and not r['passed']],verdict=verdict,results=results)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    p = sub.add_parser('validate'); p.add_argument('--repo', required=True); p.add_argument('--authoring', action='store_true')
    sub.add_parser('lock', help='Intentional author/reviewer freeze; status approval is recorded separately')
    p = sub.add_parser('export'); p.add_argument('--repo', required=True); p.add_argument('--scenario', required=True); p.add_argument('--stage', type=int, default=1); p.add_argument('--destination', required=True)
    p = sub.add_parser('check-assessment'); p.add_argument('assessment')
    p = sub.add_parser('compare'); p.add_argument('first'); p.add_argument('second')
    p = sub.add_parser('aggregate'); p.add_argument('directory')
    args = parser.parse_args()
    try:
        if args.command == 'validate': result = validate(args.repo, not args.authoring)
        elif args.command == 'lock': result = lock()
        elif args.command == 'export': result = export(args.repo,args.scenario,args.stage,args.destination)
        elif args.command == 'check-assessment': result = check_assessment(args.assessment)
        elif args.command == 'compare': result = compare(args.first,args.second)
        else: result = aggregate(args.directory)
        print(json.dumps(result,indent=2,ensure_ascii=False))
    except (ValueError, KeyError, TypeError, OSError, json.JSONDecodeError, StopIteration) as error:
        print(f'ERROR: {error}',file=sys.stderr)
        return 1
    return 0

if __name__ == '__main__':
    sys.exit(main())
