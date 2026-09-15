#!/usr/bin/env python3
"""Standard-library release, export, sealed-evidence and dimensional scoring tools.
No candidate discovery, code inspection, execution or network operations.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import shutil
import sys

SUITE = Path(__file__).resolve().parents[1]
REPO = SUITE.parents[1]
DIMENSIONS = ('BR', 'IU', 'SF', 'SI', 'PT')
CLASSES = ('explicitly-grounded', 'correctly-inferred', 'benign-assumption', 'unsupported-invention', 'contradictory-invention', 'irrelevant-capability')

def require(ok, message):
    if not ok:
        raise ValueError(message)

def read(path):
    return json.loads(Path(path).read_text())

def dump(path, value):
    Path(path).write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')

def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()).hexdigest()

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def hash_string(value):
    return isinstance(value, str) and len(value) == 64 and all(c in '0123456789abcdef' for c in value)

def safe_file(root, relative):
    p = Path(relative)
    require(not p.is_absolute() and p.parts and '..' not in p.parts, f'Unsafe artifact path: {relative}')
    root = Path(root).resolve()
    target = root / p
    require(all(not (root / Path(*p.parts[:n])).is_symlink() for n in range(1, len(p.parts) + 1)), 'Symlink artifact forbidden')
    require(target.is_file() and target.resolve().is_relative_to(root), f'Missing/nonregular artifact: {relative}')
    return target

def external_new(path, directory=False):
    path = Path(path).resolve()
    require(not path.is_relative_to(REPO) and not REPO.is_relative_to(path), 'Output must be outside repository and cannot contain it')
    require(not path.exists() or (directory and path.is_dir() and not any(path.iterdir())), 'Output must be absent (or empty export directory)')
    path.parent.mkdir(parents=True, exist_ok=True)
    return path

def manifest():
    return read(SUITE / 'suite-manifest.json')

def scenario(sid):
    found = [s for s in manifest()['scenarios'] if s['id'] == sid]
    require(len(found) == 1, f'Unknown scenario {sid}')
    return found[0]

def oracle(sid):
    return read(SUITE / scenario(sid)['path'] / 'hidden/oracle.json')['checkpoints']

def release_files():
    return {str(p.relative_to(SUITE)): sha(p) for p in sorted(SUITE.rglob('*'))
            if p.is_file() and '__pycache__' not in p.parts and p != SUITE / 'release-lock.json'}

def phases(s):
    if s['mode'] == 'control':
        return ['wrong-action', 'valid-continuation', 'condition', 'fresh-state']
    if s['mode'] == 'usability':
        return ['fresh-user-1', 'fresh-user-2', 'recovery', 'state-explanation']
    if s['mode'] == 'semantic':
        return ['surface-census', 'concept-inventory', 'consequential-probes']
    return {
        'T01': ['unauthenticated', 'logged-out', 'role-denial', 'boundary-replay', 'permitted-action', 'fresh-state'],
        'T02': ['before-commit-loss', 'after-commit-loss', 'retry', 'service-restart', 'fresh-state'],
        'T03': ['dirty-entry', 'duplicate-inbound', 'untrusted-content', 'correction', 'fresh-state'],
        'T04': ['delivered-setup', 'service-restart', 'essential-data-recovery', 'mobile', 'keyboard-zoom', 'fresh-state']
    }[s['id']]

def selected_dimensions(s, record=None):
    available = {c['dimension'] for c in oracle(s['id'])}
    selected = set(record.get('assessed_dimensions', available)) if record else available
    require(selected and selected <= available, 'Unsupported/empty dimension selection')
    return selected

def required_phases(s, selected):
    if s['mode'] != 'control':
        return phases(s)
    result = {'fresh-state'}
    if 'BR' in selected: result |= {'wrong-action', 'valid-continuation'}
    if 'SI' in selected: result |= {'valid-continuation', 'condition'}
    if 'SF' in selected: result |= {'valid-continuation'}
    return sorted(result)

def task_text(s, variant=None):
    if variant in ['SI', 'SF'] and s['mode'] == 'control':
        return 'Use the supplied business source facts to maintain truthful current records and continue only genuinely authorised work. Preserve missing information, source evidence and accountable next actions. Use normal supported application operation in the sandbox.\n'
    return (SUITE / s['path'] / 'public/task.md').read_text()

def validate(locked=True):
    m = manifest()
    require(m['version'] == '2.0.0' and set(m['dimensions']) == set(DIMENSIONS) | {'OF'}, 'Dimension/version contract')
    for x in m['canonical_documents'] + m['v1_files']:
        require(sha(safe_file(REPO, x['path'])) == x['sha256'], f'Source drift: {x["path"]}')
    require({x['path'] for x in m['canonical_documents']} == {str(p.relative_to(REPO)) for p in (REPO / 'docs').rglob('*.md')}, 'Canonical census drift')
    actual_v1 = {str(p.relative_to(REPO)) for p in (REPO / 'benchmarks/v1').rglob('*') if p.is_file() and '__pycache__' not in p.parts}
    require(actual_v1 == {x['path'] for x in m['v1_files']}, 'V1 file census drift')
    es = read(SUITE / 'hidden/evidence-index.json')
    eids = {e['id'] for e in es}
    require(len(es) == len(eids), 'Duplicate evidence IDs')
    for e in es:
        require(e['path'] in {x['path'] for x in m['canonical_documents']}, 'Noncanonical evidence')
        lines = (REPO / e['path']).read_text().splitlines(keepends=True)
        text = ''.join(lines[e['start_line'] - 1:e['end_line']])
        require(text == e['section_text'] and hashlib.sha256(text.encode()).hexdigest() == e['section_sha256'], f'Section drift {e["id"]}')
        require(text.splitlines()[0].lstrip('#').strip() == e['heading'], 'Heading mismatch')
    calibration = read(SUITE / 'hidden/calibration/traces.json')
    expectations = read(SUITE / 'hidden/calibration/expected.json')
    require({x['id'] for x in calibration} == {x['id'] for x in expectations}, 'Calibration trace/oracle mismatch')
    ids, cids, dims = set(), set(), set()
    count = critical = 0
    source = {s['id']: s for s in read(SUITE / 'hidden/scenario-source.json')}
    for s in m['scenarios']:
        require(s['id'] not in ids and s['path'] == 'scenarios/' + s['id'], 'Duplicate/unsafe scenario')
        ids.add(s['id'])
        base = SUITE / s['path']
        for name in ['README.md', 'public/case.md', 'public/task.md', 'public/fixtures.json', 'hidden/oracle.json', 'hidden/admin-events.json', 'hidden/rubric.md', 'hidden/reference-reasoning.md']:
            safe_file(base, name)
        require(set(s['public_files']) == {p.name for p in (base / 'public').iterdir() if p.is_file()} and all('/' not in n and n not in ['oracle.json', 'rubric.md'] for n in s['public_files']), 'Public allowlist drift')
        o = read(base / 'hidden/oracle.json')
        require(o['scenario_id'] == s['id'] and o['version'] == s['version'], 'Oracle provenance')
        require(o['checkpoints'] == source[s['id']]['checkpoints'], 'Oracle/source mismatch')
        require(read(base / 'public/fixtures.json')['facts'] == source[s['id']]['fixtures'], 'Fixture/source mismatch')
        require(source[s['id']]['task'] in (base / 'public/task.md').read_text(), 'Public task drift')
        for fact in source[s['id']]['fixtures']:
            require(fact['statement'] in (base / 'public/case.md').read_text(), 'Case/fixture drift')
        events = read(base / 'hidden/admin-events.json')['events']
        require(events == source[s['id']]['events'] and len(events) + 1 == s['stages'], 'Event/stage mismatch')
        require(s['checkpoints'] == len(o['checkpoints']), 'Checkpoint count mismatch')
        for c in o['checkpoints']:
            require(c['id'] not in cids and c['id'].startswith(s['id'] + '.'), 'Duplicate/misrouted checkpoint')
            require(c['dimension'] in DIMENSIONS, 'New checkpoint cannot rescore OF')
            require(c['evidence_ids'] and set(c['evidence_ids']) <= eids, 'Missing/orphan source trace')
            require(c['fixture_refs'] and set(c['fixture_refs']) <= {f['id'] for f in source[s['id']]['fixtures']} | {e['id'] for e in events}, 'Missing fixture/event trace')
            require(set(c['required_stages']) <= set(range(1, s['stages'] + 1)) and set(c['required_phases']) <= set(phases(s)), 'Invalid checkpoint phase/stage')
            require(c['minimum_control'] in ['observable-outcome', 'guidance', 'warning', 'confirmation', 'scoped-authority', 'hard-guardrail', 'prohibited-transition'], 'Unknown control')
            rubric = (base / 'hidden/rubric.md').read_text()
            require(all(c[k] in rubric for k in ['expected', 'full_credit', 'partial_credit', 'zero_credit']), 'Rubric divergence')
            require(not c['critical_failure'] or c['critical_failure'] in rubric, 'Critical rubric divergence')
            require(all(eid in (base / 'hidden/reference-reasoning.md').read_text() for eid in c['evidence_ids']), 'Missing reasoning trace')
            cids.add(c['id']); dims.add(c['dimension']); count += 1; critical += bool(c['critical_failure'])
        if s['mode'] == 'usability':
            require(not events and all(c['dimension'] == 'IU' for c in o['checkpoints']), 'Usability isolation')
        require(phases(s), 'Missing administration phases')
    require(dims == set(DIMENSIONS), 'Dimension coverage missing')
    require(all(x['checkpoint_id'] in cids for x in calibration + expectations), 'Calibration checkpoint orphan')
    # Validate local Markdown links, excluding deliberately external reference URLs.
    import re
    for p in SUITE.rglob('*.md'):
        for target in re.findall(r'\]\(([^)]+)\)', p.read_text()):
            if '://' not in target and not target.startswith('#'):
                require((p.parent / target.split('#')[0]).resolve().exists(), f'Broken link {p.relative_to(SUITE)}: {target}')
    if locked:
        lock = read(SUITE / 'release-lock.json')
        body = {k: v for k, v in lock.items() if k != 'fingerprint'}
        require(lock['fingerprint'] == fingerprint(body), 'Invalid release fingerprint')
        require(lock['files'] == release_files() and lock['suite_version'] == m['version'], 'Release content drift')
    return dict(valid=True, scenarios=len(ids), checkpoints=count, critical_predicates=critical, canonical_documents=len(m['canonical_documents']), evidence_sections=len(es), v1_files_unchanged=len(m['v1_files']))

def lock_release():
    validate(False)
    value = dict(suite_version=manifest()['version'], canonical_baseline=manifest()['canonical_baseline'], files=release_files())
    value['fingerprint'] = fingerprint(value)
    dump(SUITE / 'release-lock.json', value)
    return {'fingerprint': value['fingerprint']}

def export(sid, stage, destination, dimension=None):
    validate()
    s = scenario(sid)
    require(1 <= stage <= s['stages'], 'Invalid stage')
    require(dimension is None or dimension in selected_dimensions(s), 'Scenario does not assess requested dimension')
    require(s['mode'] != 'semantic', 'S01 is evaluator-only: no operator export')
    dest = external_new(destination, True)
    dest.mkdir(exist_ok=True)
    shutil.copy2(SUITE / 'public/operator-contract.md', dest / 'operator-contract.md')
    if stage == 1:
        for x in manifest()['canonical_documents']:
            dst = dest / x['path']; dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(REPO / x['path'], dst)
        for name in s['public_files']:
            shutil.copy2(SUITE / s['path'] / 'public' / name, dest / name)
        (dest / 'task.md').write_text(task_text(s, dimension))
    else:
        ev = read(SUITE / s['path'] / 'hidden/admin-events.json')['events'][stage - 2]
        dump(dest / 'event.json', {'id': ev['id'], 'stage': stage, 'facts': ev['payload']})
        (dest / 'task.md').write_text(ev['task'] + '\n')
    # No release metadata, tooling, or oracle is exported, even under a neutral name.
    delivery = dict(stage=stage, task_variant=dimension or 'default')
    if stage == 1:
        delivery.update(fixtures_sha256=sha(dest / 'fixtures.json'), task_sha256=sha(dest / 'task.md'))
    else:
        delivery.update(event_id=ev['id'], payload_fingerprint=fingerprint(read(dest / 'event.json')))
    return dict(delivery_receipt=delivery, scenario=sid, stage=stage, mode=s['mode'], files={str(p.relative_to(dest)): sha(p) for p in sorted(dest.rglob('*')) if p.is_file()})

def check_record(r, artifact_names):
    s = scenario(r['scenario_id'])
    selected = selected_dimensions(s, r)
    require(r['suite_fingerprint'] == read(SUITE / 'release-lock.json')['fingerprint'] and r['canonical_baseline'] == manifest()['canonical_baseline'], 'Observation suite/baseline mismatch')
    require(r['run_id'] and r['candidate_id'] and hash_string(r['build_sha256']) and hash_string(r['configuration_sha256']), 'Missing frozen candidate provenance')
    require(sorted(r['completed_stages']) == list(range(1, s['stages'] + 1)), 'Missing/duplicate stages')
    require(r['protocol_profile'] in ['standard', 'nonstandard'] and isinstance(r['deviations'], list), 'Protocol declaration missing')
    require(r['operators'] and all(x.get('id') and x.get('role') and x.get('business_briefing') for x in r['operators']), 'Operator provenance missing')
    if s['mode'] == 'usability':
        require(len(r['operators']) == 2 and len({x['id'] for x in r['operators']}) == 2, 'Two independent fresh users required')
        require(all(x.get('fresh') is True and x.get('prior_candidate_exposure') is False for x in r['operators']), 'Usability contamination')
        require(r['application_specific_assistance'] is False, 'Usability coaching invalid')
    observations = r['observations']
    ids = {o['id'] for o in observations}
    require(observations and len(ids) == len(observations), 'Missing/duplicate observations')
    for o in observations:
        require(o['stage'] in r['completed_stages'] and o['actor'] and o['description'], 'Observation content/stage missing')
        require(o['origin'] in ['fixture', 'operator', 'candidate', 'administrator'] and o['kind'], 'Observation attribution missing')
        require(o['artifact_refs'] and set(o['artifact_refs']) <= artifact_names, 'Observation artifact absent')
    require(all(any(o['stage'] == stage for o in observations) for stage in r['completed_stages']), 'No artifact observation for stage')
    require(r['pre_state_refs'] and set(r['pre_state_refs']) <= ids and r['final_state_refs'] and set(r['final_state_refs']) <= ids, 'Pre-state/final-state evidence missing')
    deliveries = r['stage_deliveries']
    require(len(deliveries) == s['stages'] and {d['stage'] for d in deliveries} == set(r['completed_stages']), 'Stage delivery provenance missing')
    for d in deliveries:
        require(d['timestamp'] and d['observation_refs'] and set(d['observation_refs']) <= ids, 'Stage delivery receipt absent')
        if d['stage'] == 1:
            require(d['fixtures_sha256'] == sha(SUITE / s['path'] / 'public/fixtures.json') and d['task_sha256'] == hashlib.sha256(task_text(s, d.get('task_variant')).encode()).hexdigest(), 'Initial input identity mismatch')
        else:
            event = read(SUITE / s['path'] / 'hidden/admin-events.json')['events'][d['stage'] - 2]
            require(d['event_id'] == event['id'] and d['payload_fingerprint'] == fingerprint({'id': event['id'], 'stage': d['stage'], 'facts': event['payload']}), 'Staged event identity mismatch')
    require(set(r['phase_receipts']) == set(required_phases(s, selected)), 'Condition coverage mismatch')
    require(all(refs and set(refs) <= ids for refs in r['phase_receipts'].values()), 'Phase receipt evidence missing')
    if s['mode'] == 'semantic':
        require(r['surface_census']['complete'] is True, 'Incomplete semantic census')
        require(set(r['surface_census']['domains']) >= {'identity', 'lifecycle', 'authority', 'safety', 'information', 'reporting'}, 'Narrow semantic census')
        require(r['semantic_concept_ids'] and len(set(r['semantic_concept_ids'])) == len(r['semantic_concept_ids']), 'Semantic concept census absent/duplicate')
    return r

def seal(record, artifacts, output):
    validate()
    root = Path(artifacts).resolve()
    require(root.is_dir() and not root.is_relative_to(REPO), 'Artifacts must be external directory')
    out = external_new(output)
    require(not out.is_relative_to(root), 'Bundle cannot be an artifact within itself')
    files = {str(p.relative_to(root)): sha(safe_file(root, str(p.relative_to(root)))) for p in sorted(root.rglob('*')) if p.is_file() or p.is_symlink()}
    require(files, 'No artifacts')
    value = dict(record=check_record(read(record), set(files)), artifact_root=str(root), artifacts=files)
    value['fingerprint'] = fingerprint(value)
    dump(out, value)
    return {'bundle_fingerprint': value['fingerprint'], 'artifacts': len(files)}

def check_bundle(path):
    validate()
    b = read(path)
    require(b['fingerprint'] == fingerprint({k: v for k, v in b.items() if k != 'fingerprint'}), 'Bundle fingerprint invalid')
    require(b['artifacts'] and not Path(b['artifact_root']).resolve().is_relative_to(REPO), 'Invalid artifact root')
    for rel, digest in b['artifacts'].items():
        require(sha(safe_file(b['artifact_root'], rel)) == digest, f'Artifact tampered: {rel}')
    check_record(b['record'], set(b['artifacts']))
    return b

def check_items(a, b):
    r = b['record']
    for k in ['run_id', 'scenario_id', 'suite_fingerprint', 'canonical_baseline', 'build_sha256', 'configuration_sha256']:
        require(a[k] == r[k], f'Assessment provenance mismatch {k}')
    require(a['bundle_fingerprint'] == b['fingerprint'], 'Assessment bundle mismatch')
    require(isinstance(a['issues'], list), 'Unresolved issue list missing')
    obs = {x['id'] for x in r['observations']}
    selected = selected_dimensions(scenario(a['scenario_id']), r)
    require(set(a.get('assessed_dimensions', selected)) == selected, 'Assessment dimension selection mismatch')
    checks = {c['id']: c for c in oracle(a['scenario_id']) if c['dimension'] in selected}
    require(len(a['checkpoints']) == len(checks) and {x['id'] for x in a['checkpoints']} == set(checks), 'Missing/duplicate assessment checkpoints')
    for x in a['checkpoints']:
        c = checks[x['id']]
        require(type(x['score']) is int and x['score'] in [0, 1, 2], 'Invalid score')
        require(x['status'] in ['resolved', 'unresolved'] and x['reason'] and x['observed_subset'] and x['confidence'] in ['low', 'medium', 'high'], 'Judgment evidence missing')
        require(x['observation_refs'] and set(x['observation_refs']) <= obs, 'Unknown/missing observation refs')
        require(set(c['required_stages']) <= {o['stage'] for o in r['observations'] if o['id'] in x['observation_refs']}, 'Checkpoint stage evidence missing')
        require(all(set(x['observation_refs']) & set(r['phase_receipts'][phase]) for phase in c['required_phases']), 'Checkpoint condition evidence missing')
        require(x['evidence_ids'] and set(x['evidence_ids']) <= set(c['evidence_ids']), 'Unsupported canonical scoring reference')
        require(x['score'] != 1 or x.get('missing_element'), 'Partial missing-element explanation required')
        require(type(x['critical_triggered']) is bool, 'Critical decision missing')
        if x['critical_triggered']:
            require(c['critical_failure'] and x['score'] == 0 and x.get('incident_id'), 'Undeclared/unpenalised/unattributed critical event')
        require(x['status'] != 'unresolved' or a['issues'], 'Unresolved judgment needs issue')
    if a['scenario_id'] == 'S01':
        findings = a['semantic_findings']
        require(len(findings) == len(r['semantic_concept_ids']) and {x['id'] for x in findings} == set(r['semantic_concept_ids']), 'Semantic classification census mismatch')
        eids = {e['id'] for e in read(SUITE / 'hidden/evidence-index.json')}
        for x in findings:
            require(x['classification'] in CLASSES and type(x['materiality']) is int and 0 <= x['materiality'] <= 3, 'Invalid semantic classification/materiality')
            require(x['observation_refs'] and set(x['observation_refs']) <= obs and x['reason'], 'Semantic finding evidence absent')
            require(set(x['evidence_ids']) <= eids, 'Unknown semantic source')
            if x['classification'] in ['explicitly-grounded', 'correctly-inferred', 'contradictory-invention']:
                require(x['evidence_ids'], 'Grounding/contradiction requires canonical source')
            if x['classification'] in ['unsupported-invention', 'irrelevant-capability']:
                require(x.get('gap_search'), 'Unsupported meaning needs scoped canonical gap search')
            require(x['status'] in ['resolved', 'unresolved'], 'Semantic status absent')
            require(x['status'] != 'unresolved' or a['issues'], 'Unresolved concept needs issue')
        require(not any(x['materiality'] == 3 for x in findings) or any(x['critical_triggered'] for x in a['checkpoints']), 'Critical semantic materiality needs explicit declared critical incident')
    else:
        require(not a.get('semantic_findings'), 'Semantic census belongs to S01')

def identity(a):
    return {k: a[k] for k in ['run_id', 'scenario_id', 'suite_fingerprint', 'canonical_baseline', 'build_sha256', 'configuration_sha256', 'bundle_fingerprint']}

def differences(a, z):
    require(identity(a) == identity(z), 'Cannot compare different frozen runs/bundles')
    require(a['evaluator']['id'] != z['evaluator']['id'], 'Independent evaluator identities required')
    one = {x['id']: x for x in a['checkpoints']}; two = {x['id']: x for x in z['checkpoints']}
    result = [cid for cid in one if any(one[cid][k] != two[cid][k] for k in ['score', 'status', 'critical_triggered'])]
    f1 = {x['id']: x for x in a.get('semantic_findings', [])}; f2 = {x['id']: x for x in z.get('semantic_findings', [])}
    result += ['concept:' + cid for cid in f1 if any(f1[cid][k] != f2[cid][k] for k in ['classification', 'materiality', 'status'])]
    if a['issues'] != z['issues']:
        result.append('issues')
    return sorted(result)

def merge(a, z, adjudication):
    diff = differences(a, z)
    if diff:
        require(all(adjudication.get('adjudicator', {}).get(k) for k in ['id', 'model', 'configuration']), 'Adjudicator identity/configuration absent')
    allowed_sources = {e['id'] for e in read(SUITE / 'hidden/evidence-index.json')}
    known = next(s for s in read(SUITE / 'hidden/scenario-source.json') if s['id'] == a['scenario_id'])
    allowed_fixtures = {f['id'] for f in known['fixtures']} | {e['id'] for e in known['events']}
    require(set(adjudication.get('decisions', {})) == set(diff), 'Every differing judgment (and only those) needs adjudication')
    result = copy.deepcopy(a)
    items = {x['id']: x for x in result['checkpoints']}
    concepts = {x['id']: x for x in result.get('semantic_findings', [])}
    for key in diff:
        decision = adjudication['decisions'][key]
        require(decision.get('rationale') and decision.get('original_positions') and decision.get('canonical_basis') and decision.get('observation_refs'), 'Adjudication audit trail absent')
        require(set(decision['canonical_basis']) <= allowed_sources and decision.get('fixture_refs') and set(decision['fixture_refs']) <= allowed_fixtures, 'Adjudication source/fixture trace invalid')
        value = decision['final']
        if key == 'issues':
            result['issues'] = value
        elif key.startswith('concept:'):
            require(value['id'] == key[8:], 'Adjudicated concept identity')
            concepts[key[8:]] = value
        else:
            require(value['id'] == key, 'Adjudicated checkpoint identity')
            items[key] = value
    result['checkpoints'] = list(items.values())
    result['semantic_findings'] = list(concepts.values())
    return result

def check_assessment(path, bundle, independent_only=False):
    a = read(path); b = check_bundle(bundle)
    check_items(a, b)
    require(a['assessment_kind'] in ['independent', 'final'], 'Assessment kind invalid')
    ev = a['evaluator']
    require(all(ev.get(k) for k in ['id', 'model', 'configuration', 'prompt_sha256']), 'Evaluator provenance missing')
    require(hash_string(ev['prompt_sha256']) and ev['blind_to_other_scores'] is True and ev['blind_to_methodology'] is True, 'Independent/blind scoring declaration absent')
    if a['assessment_kind'] == 'final':
        require(not independent_only, 'Original must be independent')
        originals = a['independent_assessments']
        require(len(originals) == 2, 'Two original independent assessments required')
        vals = []
        for x in originals:
            require(Path(x['path']).resolve() != Path(path).resolve() and sha(x['path']) == x['sha256'], 'Original assessment changed/self-reference')
            vals.append(check_assessment(x['path'], bundle, True))
        adj = a['adjudication']
        if differences(*vals):
            require(adj and sha(adj['path']) == adj['sha256'], 'Missing/tampered adjudication')
            raw_adj = read(adj['path'])
            known_observations = {o['id'] for o in b['record']['observations']}
            require(all(set(d['observation_refs']) <= known_observations for d in raw_adj['decisions'].values()), 'Adjudication unknown observation')
            merged = merge(*vals, raw_adj)
        else:
            require(not adj, 'No disagreement: no adjudication needed')
            merged = merge(*vals, {})
        require(a['checkpoints'] == merged['checkpoints'] and a.get('semantic_findings', []) == merged.get('semantic_findings', []) and a['issues'] == merged['issues'], 'Final differs from independent agreement/adjudication')
    return a

def finalize(first, second, bundle, output, adjudication=None):
    a = check_assessment(first, bundle, True); z = check_assessment(second, bundle, True)
    diff = differences(a, z)
    require(bool(adjudication) == bool(diff), 'Adjudication required exactly when judgments differ')
    result = merge(a, z, read(adjudication) if adjudication else {})
    result['assessment_kind'] = 'final'
    result['independent_assessments'] = [dict(path=str(Path(p).resolve()), sha256=sha(p)) for p in [first, second]]
    result['adjudication'] = dict(path=str(Path(adjudication).resolve()), sha256=sha(adjudication)) if adjudication else None
    out = external_new(output); dump(out, result)
    check_assessment(out, bundle)
    return {'final': str(out), 'adjudicated': diff}

def calculate(assessments, records, v1=None, dimensions=DIMENSIONS):
    target = set(dimensions)
    require(target and target <= set(DIMENSIONS), 'Invalid requested dimension profile')
    cells = []; incidents = {}; incomplete = []; provenance = set(); usability_subjects = set()
    byid = {}
    for a in assessments:
        require(a['scenario_id'] not in byid, 'Duplicate final scenario')
        byid[a['scenario_id']] = a
        provenance.add(tuple(a[k] for k in ['suite_fingerprint', 'canonical_baseline', 'build_sha256', 'configuration_sha256']))
    require(len(provenance) <= 1, 'Mixed build/configuration/source profiles')
    for s in manifest()['scenarios']:
        sid = s['id']
        needed = {c['dimension'] for c in oracle(sid)} & target
        if not needed: continue
        if sid not in byid:
            incomplete.append(sid); continue
        a = byid[sid]; r = records[sid]
        if s['mode'] == 'usability' and r['protocol_profile'] == 'standard':
            subjects = {x['id'] for x in r['operators']}
            require(not subjects & usability_subjects, 'Standard usability subject reused across tasks')
            usability_subjects |= subjects
        supplied = {c['dimension'] for c in oracle(sid) if c['id'] in {x['id'] for x in a['checkpoints']}}
        if not needed <= supplied: incomplete.append(sid + ': missing requested dimensions')
        if a['issues'] or any(x['status'] == 'unresolved' for x in a['checkpoints']) or any(x['status'] == 'unresolved' for x in a.get('semantic_findings', [])) or r['protocol_profile'] != 'standard':
            incomplete.append(sid + ': unresolved/nonstandard')
        checks = {c['id']: c for c in oracle(sid)}
        for dim in sorted(supplied & target):
            xs = [x for x in a['checkpoints'] if checks[x['id']]['dimension'] == dim]
            cells.append(dict(scenario=sid, dimension=dim, score=100 * sum(x['score'] for x in xs) / (2 * len(xs)), checkpoints=len(xs)))
        for x in a['checkpoints']:
            if x['critical_triggered']:
                key = sid + ':' + x['incident_id']
                incidents.setdefault(key, []).append(x['id'])
    dims = {d: dict(score=(sum(x['score'] for x in cells if x['dimension'] == d) / len([x for x in cells if x['dimension'] == d])) if any(x['dimension'] == d for x in cells) else None, cells=len([x for x in cells if x['dimension'] == d])) for d in sorted(target)}
    t = manifest()['thresholds']
    failed = [x for x in cells if x['score'] < t['family_minimum']]
    failed_dims = [d for d, x in dims.items() if x['score'] is not None and x['score'] < t['dimension_minimum']]
    of = {'status': 'not assessed'}
    if v1:
        require(provenance, 'No new run profile for V1 comparison')
        profile = next(iter(provenance))
        require(v1['build_sha256'] == profile[2] and v1['configuration_sha256'] == profile[3], 'V1 frozen build/configuration mismatch')
        require(v1['canonical_documents'] == read(REPO / 'benchmarks/v1/suite-manifest.json')['canonical_documents'] == manifest()['canonical_documents'], 'V1 canonical baseline/content not comparable')
        require(v1['release_fingerprint'] == read(REPO / 'benchmarks/v1/release-lock.json')['fingerprint'], 'V1 release mismatch')
        require(v1['operational_application_run'] is True and v1['independently_scored_and_resolved'] is True and v1['complete'] is True, 'Invalid/incomplete V1 operational attachment')
        for x in v1['result_artifacts']:
            require(hash_string(x['sha256']) and sha(x['path']) == x['sha256'], 'V1 result artifact missing/changed')
        require(v1['result_artifacts'] and v1['verdict'] in ['Fit-for-purpose demonstrated within V1 scope', 'Material business gaps demonstrated'], 'V1 result/valid verdict missing')
        of = v1
    verdict = 'Additional profile only'
    if incomplete:
        verdict = 'Incomplete or unresolved'
    elif incidents or failed or failed_dims or (v1 and v1['verdict'] != 'Fit-for-purpose demonstrated within V1 scope'):
        verdict = 'Material fitness gaps demonstrated'
    elif v1 and target == set(DIMENSIONS):
        verdict = 'Bounded pilot gates met; calibration pending'
    inventory = byid.get('S01', {}).get('semantic_findings', [])
    inventory_counts = {kind: {str(band): sum(x['classification'] == kind and x['materiality'] == band for x in inventory) for band in range(4)} for kind in CLASSES}
    return dict(semantic_max_materiality=max([x['materiality'] for x in inventory], default=None), semantic_inventory_counts=inventory_counts, verdict=verdict, dimensions=dims, OF=of, cells=cells, critical_incidents=incidents, incomplete=incomplete, failed_cells=failed, failed_dimensions=failed_dims, semantic_findings=byid.get('S01', {}).get('semantic_findings', []), limits='No combined arithmetic score. Release calibration remains pending; declared bounded conditions are not production certification.')

def scorecard(directory, bundles, v1path=None, dimensions=DIMENSIONS):
    validate(); assessments = []; records = {}
    for path in sorted(Path(directory).glob('*.json')):
        candidate = read(path)
        if candidate.get('assessment_kind') != 'final':
            continue
        bp = Path(bundles) / (candidate['scenario_id'] + '.json')
        a = check_assessment(path, bp)
        assessments.append(a); records[a['scenario_id']] = check_bundle(bp)['record']
    return calculate(assessments, records, read(v1path) if v1path else None, dimensions)

def main():
    p = argparse.ArgumentParser(description=__doc__); sub = p.add_subparsers(dest='command', required=True)
    sub.add_parser('validate'); sub.add_parser('lock')
    q = sub.add_parser('export'); q.add_argument('--scenario', required=True); q.add_argument('--stage', type=int, default=1); q.add_argument('--destination', required=True); q.add_argument('--dimension', choices=DIMENSIONS)
    q = sub.add_parser('seal'); q.add_argument('--record', required=True); q.add_argument('--artifacts', required=True); q.add_argument('--output', required=True)
    q = sub.add_parser('check-bundle'); q.add_argument('bundle')
    q = sub.add_parser('check-assessment'); q.add_argument('assessment'); q.add_argument('--bundle', required=True)
    q = sub.add_parser('compare'); q.add_argument('first'); q.add_argument('second'); q.add_argument('--bundle', required=True)
    q = sub.add_parser('finalize'); q.add_argument('--first', required=True); q.add_argument('--second', required=True); q.add_argument('--bundle', required=True); q.add_argument('--adjudication'); q.add_argument('--output', required=True)
    q = sub.add_parser('scorecard'); q.add_argument('directory'); q.add_argument('--bundles', required=True); q.add_argument('--v1-attachment'); q.add_argument('--dimensions', nargs='+', choices=DIMENSIONS, default=DIMENSIONS)
    args = p.parse_args()
    try:
        if args.command == 'validate': result = validate()
        elif args.command == 'lock': result = lock_release()
        elif args.command == 'export': result = export(args.scenario, args.stage, args.destination, args.dimension)
        elif args.command == 'seal': result = seal(args.record, args.artifacts, args.output)
        elif args.command == 'check-bundle': result = {'valid': True, 'fingerprint': check_bundle(args.bundle)['fingerprint']}
        elif args.command == 'check-assessment': check_assessment(args.assessment, args.bundle); result = {'valid': True}
        elif args.command == 'compare': result = {'disagreements': differences(check_assessment(args.first, args.bundle, True), check_assessment(args.second, args.bundle, True))}
        elif args.command == 'finalize': result = finalize(args.first, args.second, args.bundle, args.output, args.adjudication)
        else: result = scorecard(args.directory, args.bundles, args.v1_attachment, args.dimensions)
        print(json.dumps(result, indent=2, ensure_ascii=False))
    except (ValueError, KeyError, OSError, TypeError, StopIteration) as exc:
        print(f'INVALID: {exc}', file=sys.stderr); return 1
    return 0

if __name__ == '__main__':
    sys.exit(main())
