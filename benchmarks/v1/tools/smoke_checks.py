#!/usr/bin/env python3
"""Local administration checks, not independent evaluator or candidate validation."""
import sys
sys.dont_write_bytecode = True
from pathlib import Path
import copy
import hashlib
import json
import runpy
import shutil
import subprocess
import tempfile

API = runpy.run_path(str(Path(__file__).with_name('benchmark.py')))
SUITE = API['SUITE']
PASS_COUNT = 0

def check(label, condition):
    global PASS_COUNT
    if not condition:
        raise AssertionError(label)
    PASS_COUNT += 1
    print('PASS: '+label)

def rejected(label, fn):
    try:
        fn()
    except (ValueError, KeyError, TypeError, OSError):
        check(label, True)
        return
    raise AssertionError('Expected rejection: '+label)

def assessment(sid, scores=None, failure=None):
    oracle = API['oracle'](sid)
    checkpoints = [x for c in oracle['criteria'] for x in c['checkpoints']]
    scores = scores or [10]*10
    result = dict(run_id='synthetic-local-tool-check',scenario_id=sid,scenario_version=oracle['version'],
        suite_version=API['manifest']()['version'],canonical_baseline=API['manifest']()['canonical_baseline'],
        release_fingerprint=API['read'](SUITE/'release-lock.json')['fingerprint'],
        observation_bundle_sha256=hashlib.sha256(('synthetic observations '+sid).encode()).hexdigest(),
        evaluator=dict(id='synthetic-author-anchor-A',model='none; local tool fixture',configuration='no model run',date='2026-09-15'),
        completed_stages=list(range(1,API['scenario'](sid)['stages']+1)),judgement_status='resolved',
        checkpoints=[dict(id=x['id'],score=score,observation_refs=['SYNTHETIC-O001'],evidence_ids=x['evidence_ids'],reason='Synthetic scoring-tool input only; not a candidate or independent model judgement.') for x,score in zip(checkpoints,scores)],
        critical_failures=[],uncertain_judgements=[],secondary_findings=[],confidence='tool fixture only',raw_assessment_reference='synthetic-no-evaluator-output',
        adjudication=dict(status='final',original_assessment_refs=['synthetic-A','synthetic-B'],decisions=[]))
    if failure:
        cf = next(f for f in oracle['critical_failures'] if f['id']==failure)
        result['critical_failures']=[dict(id=failure,observation_refs=['SYNTHETIC-O002'],evidence_ids=cf['evidence_ids'],reason='Synthetic declared-event fixture to test cap arithmetic.')]
    return result

def save(directory, name, value):
    path=directory/name
    path.write_text(json.dumps(value))
    return path

def main(repo):
    check('canonical/rendered/semantic/release validation', API['validate'](repo)['checkpoints']==270)
    with tempfile.TemporaryDirectory(prefix='frostline-benchmark-check-') as tmp:
        tmp=Path(tmp)
        for s in API['manifest']()['scenarios']:
            for stage in range(1,s['stages']+1):
                destination=tmp/f'{s["id"]}-stage{stage}'
                API['export'](repo,s['id'],stage,destination)
                files={str(p.relative_to(destination)) for p in destination.rglob('*') if p.is_file()}
                expected={'submission-contract.md','case.md','task.md','fixtures.json'}|{x['path'] for x in API['manifest']()['canonical_documents']} if stage==1 else {'submission-contract.md','event.json','event.md'}
                check(f'{s["id"]} stage {stage} exact candidate allowlist',files==expected)
                check(f'{s["id"]} stage {stage} no hidden oracle/metadata/later inputs',not any('/hidden/' in '/'+f or f.endswith('oracle.json') or f.endswith('suite-manifest.json') for f in files))
        stale=tmp/'stale';stale.mkdir();(stale/'rubric.md').write_text('hidden old content')
        rejected('reject stale contaminated export directory',lambda:API['export'](repo,'B001',1,stale))
        rejected('reject repository export destination',lambda:API['export'](repo,'B001',1,Path(repo)/'candidate-input'))
        rejected('reject undeclared stage',lambda:API['export'](repo,'B001',2,tmp/'bad-stage'))
        symlink=tmp/'linked';symlink.symlink_to(stale,target_is_directory=True)
        rejected('reject symlink export destination',lambda:API['export'](repo,'B001',1,symlink))
        drift=tmp/'drift';(drift/'docs').mkdir(parents=True)
        for x in API['manifest']()['canonical_documents']:
            p=drift/x['path'];p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes((Path(repo)/x['path']).read_bytes())
        (drift/'docs/operations/work-lifecycle.md').write_text('changed business policy')
        rejected('reject canonical dependency drift before export',lambda:API['export'](drift,'B001',1,tmp/'drift-export'))
        check('drift creates no candidate output',not (tmp/'drift-export').exists())
        tampered=tmp/'tampered-release';shutil.copytree(SUITE,tampered)
        tampered_readme=tampered/'README.md'
        tampered_readme.write_text(tampered_readme.read_text()+'\nUnreviewed frozen-release alteration.\n')
        tamper_run=subprocess.run([sys.executable,str(tampered/'tools/benchmark.py'),'validate','--repo',str(repo)],capture_output=True,text=True)
        check('reject changed frozen release even with unchanged canonical docs',tamper_run.returncode!=0 and 'Frozen release changed' in tamper_run.stderr)
        a=assessment('B002');pa=save(tmp,'a.json',a)
        check('full evidenced synthetic score arithmetic',API['check_assessment'](pa)['effective_score']==100)
        early=assessment('B019',[10,0,0,0,10,10,10,10,0,10],'B019-CF1');pe=save(tmp,'early.json',early)
        score=API['check_assessment'](pe)
        check('stage-history critical failure preserves raw60/caps59/fails',score['raw_score']==60 and score['effective_score']==59 and not score['passed'])
        b=copy.deepcopy(a);b['evaluator']['id']='synthetic-B';b['checkpoints'][0]['score']=5;pb=save(tmp,'b.json',b)
        check('checkpoint disagreement auditable',API['compare'](pa,pb)['adjudication_required'])
        bf=copy.deepcopy(early);bf['evaluator']['id']='synthetic-B';bf['critical_failures']=[];pbf=save(tmp,'bf.json',bf)
        check('critical failure disagreement detected even with same raw scores',API['compare'](pe,pbf)['critical_failure_disagreement'])
        wrong=copy.deepcopy(b);wrong['observation_bundle_sha256']='f'*64
        rejected('reject comparison of different observation bundles',lambda:API['compare'](pa,save(tmp,'wrong-bundle.json',wrong)))
        for label, mutate in [
            ('undeclared critical failure',lambda x:x['critical_failures'].append(dict(id='B002-CF999',observation_refs=['O1'],evidence_ids=['E001'],reason='invented'))),
            ('duplicate/missing checkpoint',lambda x:x['checkpoints'].__setitem__(1,x['checkpoints'][0])),
            ('unevidenced score',lambda x:x['checkpoints'][0].__setitem__('observation_refs',[])),
            ('unsupported policy reference',lambda x:x['checkpoints'][0].__setitem__('evidence_ids',['E999'])),
            ('non-contract score',lambda x:x['checkpoints'][0].__setitem__('score',9)),
            ('unresolved judgement labelled resolved',lambda x:x['uncertain_judgements'].append('unknown observed state')),
        ]:
            bad=copy.deepcopy(a);mutate(bad)
            rejected('reject '+label,lambda bad=bad:API['check_assessment'](save(tmp,'invalid.json',bad)))
        incomplete=copy.deepcopy(a);incomplete['completed_stages']=[1]
        check('incomplete later stage withholds pass',not API['check_assessment'](save(tmp,'incomplete.json',incomplete))['passed'])
        final=tmp/'final';final.mkdir()
        for s in API['manifest']()['scenarios']:save(final,s['id']+'.json',assessment(s['id']))
        check('complete synthetic final records produce scoped verdict',API['aggregate'](final)['verdict']=='fit-for-purpose demonstrated within V1 scope')
        save(final,'B019.json',early)
        aggregate=API['aggregate'](final)
        check('high aggregate cannot erase critical business failure',aggregate['effective_mean']>95 and aggregate['verdict']=='material business gaps demonstrated')
        (final/'B027.json').unlink()  # Only a synthetic temporary fixture, never repository content.
        check('missing scenario withholds whole-suite verdict',API['aggregate'](final)['verdict']=='assessment incomplete or unresolved')
        save(final,'B027.json',assessment('B027'));independent=assessment('B002');independent['adjudication']['status']='independent';save(final,'B002.json',independent)
        check('pending independent adjudication withholds verdict',API['aggregate'](final)['verdict']=='assessment incomplete or unresolved')
        save(final,'duplicate.json',assessment('B002'))
        rejected('reject duplicated scenario aggregate',lambda:API['aggregate'](final))
    print(f'{PASS_COUNT} local checks passed; no independent model/candidate evaluation performed.')

if __name__=='__main__':
    main(Path(sys.argv[1]).resolve())
