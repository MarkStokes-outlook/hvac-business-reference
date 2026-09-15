#!/usr/bin/env python3
"""Synthetic administration/tool regression checks; never candidate results."""
import copy
import json
from pathlib import Path
import tempfile
import unittest
import benchmark as b

class AdministrationChecks(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='frostline-v2-self-check-')
        self.root = Path(self.tmp.name)
        self.artifacts = self.root / 'artifacts'; self.artifacts.mkdir()
        (self.artifacts / 'trace.txt').write_text('Synthetic tool fixture only; no application execution.\n')

    def tearDown(self):
        self.tmp.cleanup()

    def record(self, sid='R01'):
        s = b.scenario(sid)
        r = dict(run_id='synthetic-1', scenario_id=sid, suite_fingerprint=b.read(b.SUITE/'release-lock.json')['fingerprint'], canonical_baseline=b.manifest()['canonical_baseline'], candidate_id='synthetic-harness-only', build_sha256='1'*64, configuration_sha256='2'*64, protocol_profile='standard', deviations=[], application_specific_assistance=False, operators=[dict(id=sid+'-subject',role='fixture role',business_briefing='synthetic role facts',fresh=True,prior_candidate_exposure=False)], completed_stages=list(range(1,s['stages']+1)), pre_state_refs=['O1'], final_state_refs=['O1'], observations=[dict(id='O1',stage=stage,actor='synthetic observer',origin='administrator',kind='synthetic trace',description='Test record: this is not evidence of candidate behavior',artifact_refs=['trace.txt']) for stage in [1]], phase_receipts={p:['O1'] for p in b.phases(s)}, stage_deliveries=[])
        for stage in r['completed_stages']:
            oid=f'O{stage}'
            if stage != 1: r['observations'].append(dict(id=oid,stage=stage,actor='synthetic observer',origin='administrator',kind='synthetic trace',description='Synthetic staged trace',artifact_refs=['trace.txt']))
            d=dict(stage=stage,timestamp='2026-10-05T09:00:00+01:00',observation_refs=[oid])
            if stage == 1:
                d.update(fixtures_sha256=b.sha(b.SUITE/s['path']/'public/fixtures.json'),task_sha256=b.sha(b.SUITE/s['path']/'public/task.md'))
            else:
                e=b.read(b.SUITE/s['path']/'hidden/admin-events.json')['events'][stage-2]
                d.update(event_id=e['id'],payload_fingerprint=b.fingerprint({'id':e['id'],'stage':stage,'facts':e['payload']}))
            r['stage_deliveries'].append(d)
        if s['mode']=='control':
            r['phase_receipts']['valid-continuation']=['O2']
            r['final_state_refs']=['O2']
        if s['mode']=='usability':
            r['operators'].append(dict(r['operators'][0], id=sid+'-subject2'))
        if sid=='S01':
            r['surface_census']={'complete':True,'domains':['identity','lifecycle','authority','safety','information','reporting']}
            r['semantic_concept_ids']=['C1']
        return r

    def bundle(self,sid='R01'):
        record=self.root/'record.json'; b.dump(record,self.record(sid))
        bundle=self.root/'bundle.json'
        b.seal(record,self.artifacts,bundle)
        return bundle

    def assessment(self,bundle,judge='A'):
        bundle_value=b.check_bundle(bundle); r=bundle_value['record']
        a={k:r[k] for k in ['run_id','scenario_id','suite_fingerprint','canonical_baseline','build_sha256','configuration_sha256']}
        a.update(assessed_dimensions=sorted(b.selected_dimensions(b.scenario(r['scenario_id']),r)),bundle_fingerprint=bundle_value['fingerprint'],assessment_kind='independent',evaluator=dict(id=judge,model='synthetic-validator',configuration='fixture only',prompt_sha256='3'*64,blind_to_other_scores=True,blind_to_methodology=True),issues=[],checkpoints=[dict(id=c['id'],score=2,status='resolved',reason='Synthetic judgment for tooling only',observed_subset='Synthetic complete subset',missing_element='',observation_refs=['O'+str(stage) for stage in c['required_stages']],evidence_ids=c['evidence_ids'],confidence='high',critical_triggered=False,incident_id='') for c in b.oracle(r['scenario_id']) if c['dimension'] in b.selected_dimensions(b.scenario(r['scenario_id']),r)],semantic_findings=[])
        if r['scenario_id']=='S01':
            a['semantic_findings']=[dict(id='C1',classification='benign-assumption',materiality=0,reason='Synthetic ID convention',observation_refs=['O1'],evidence_ids=[],status='resolved')]
        path=self.root/(judge+'.json'); b.dump(path,a)
        return path

    def test_release_and_canonical_v1_integrity(self):
        result=b.validate(); self.assertEqual(result['scenarios'],30); self.assertEqual(result['checkpoints'],102)

    def test_all_exports_and_stage_separation(self):
        for s in b.manifest()['scenarios']:
            if s['mode']=='semantic':continue
            for stage in range(1,s['stages']+1):
                dest=self.root/(s['id']+f'-stage{stage}')
                output=b.export(s['id'],stage,dest)
                names=set(output['files'])
                self.assertFalse(any('hidden' in n or 'oracle' in n or 'rubric' in n for n in names))
                if stage==1:
                    self.assertTrue({'case.md','task.md','fixtures.json'}<=names)
                    self.assertEqual(sum(n.startswith('docs/') for n in names),len(b.manifest()['canonical_documents']))
                else:self.assertEqual(names,{'operator-contract.md','task.md','event.json'})
        with self.assertRaises(ValueError):b.export('S01',1,self.root/'s01')

    def test_dimensions_independently_administrable(self):
        r=self.record();r['assessed_dimensions']=['BR']
        r['phase_receipts']={p:r['phase_receipts'][p] for p in b.required_phases(b.scenario('R01'),{'BR'})}
        record=self.root/'record.json';b.dump(record,r);bundle=self.root/'bundle.json';b.seal(record,self.artifacts,bundle)
        a=self.assessment(bundle);judged=b.check_assessment(a,bundle)
        self.assertEqual(len(judged['checkpoints']),2)
        result=b.calculate([judged],{'R01':r},dimensions=['BR'])
        self.assertEqual(set(result['dimensions']),{'BR'})
        self.assertEqual(len(result['incomplete']),16)
        dest=self.root/'si-export';receipt=b.export('R01',1,dest,'SI')['delivery_receipt']
        self.assertNotIn('Try making',(dest/'task.md').read_text())
        r=self.record();r['assessed_dimensions']=['SI'];r['phase_receipts']={p:r['phase_receipts'][p] for p in b.required_phases(b.scenario('R01'),{'SI'})}
        r['stage_deliveries'][0].update(receipt)
        b.check_record(r,{'trace.txt'})

    def test_release_drift_rejected(self):
        from unittest.mock import patch
        with patch.object(b, 'release_files', return_value={}):
            with self.assertRaises(ValueError): b.validate()

    def test_scorecard_checks_final_originals_and_bundle(self):
        bundle=self.bundle();a=self.assessment(bundle,'A');z=self.assessment(bundle,'B')
        final_dir=self.root/'finals';final_dir.mkdir();bundle_dir=self.root/'bundles';bundle_dir.mkdir()
        import shutil
        shutil.copy2(bundle,bundle_dir/'R01.json')
        b.finalize(a,z,bundle,final_dir/'R01.json')
        self.assertEqual(b.scorecard(final_dir,bundle_dir)['verdict'],'Incomplete or unresolved')
        (self.artifacts/'trace.txt').write_text('tamper')
        with self.assertRaises(ValueError):b.scorecard(final_dir,bundle_dir)

    def test_export_refuses_unsafe_destinations_and_stage(self):
        with self.assertRaises(ValueError):b.export('R01',1,b.SUITE/'leak')
        with self.assertRaises(ValueError):b.export('U01',2,self.root/'invalid')
        occupied=self.root/'occupied';occupied.mkdir();(occupied/'file').write_text('x')
        with self.assertRaises(ValueError):b.export('R01',1,occupied)

    def test_seal_tamper_and_path_boundaries(self):
        bundle=self.bundle(); b.check_bundle(bundle)
        (self.artifacts/'trace.txt').write_text('tampered')
        with self.assertRaises(ValueError):b.check_bundle(bundle)
        with self.assertRaises(ValueError):b.safe_file(self.artifacts,'../record.json')
        (self.artifacts/'link').symlink_to(self.root/'record.json')
        with self.assertRaises(ValueError):b.safe_file(self.artifacts,'link')

    def test_missing_phases_stages_and_coaching(self):
        r=self.record();del r['phase_receipts']['condition']
        with self.assertRaises(ValueError):b.check_record(r,{'trace.txt'})
        r=self.record();r['completed_stages']=[1]
        with self.assertRaises(ValueError):b.check_record(r,{'trace.txt'})
        r=self.record('U01');r['application_specific_assistance']=True
        with self.assertRaises(ValueError):b.check_record(r,{'trace.txt'})
        r=self.record('S01');r['surface_census']['complete']=False
        with self.assertRaises(ValueError):b.check_record(r,{'trace.txt'})

    def test_assessment_reference_partial_and_critical_checks(self):
        bundle=self.bundle();path=self.assessment(bundle);a=b.read(path)
        for mutation in ['missing','unknown','partial','critical']:
            changed=copy.deepcopy(a)
            if mutation=='missing':changed['checkpoints'].pop()
            if mutation=='unknown':changed['checkpoints'][0]['observation_refs']=['ghost']
            if mutation=='partial':changed['checkpoints'][0]['score']=1
            if mutation=='critical':changed['checkpoints'][0]['critical_triggered']=True
            b.dump(path,changed)
            with self.assertRaises(ValueError):b.check_assessment(path,bundle)

    def test_independent_comparison_and_finalization(self):
        bundle=self.bundle();a=self.assessment(bundle,'A');z=self.assessment(bundle,'B')
        self.assertEqual(b.differences(b.read(a),b.read(z)),[])
        out=self.root/'final.json';b.finalize(a,z,bundle,out);b.check_assessment(out,bundle)
        edited=b.read(out);edited['checkpoints'][0]['score']=0;b.dump(out,edited)
        with self.assertRaises(ValueError):b.check_assessment(out,bundle)
        with self.assertRaises(ValueError):b.differences(b.read(a),b.read(a))
        changed=b.read(z);changed['build_sha256']='4'*64
        with self.assertRaises(ValueError):b.differences(b.read(a),changed)

    def test_disagreement_requires_audited_adjudication(self):
        bundle=self.bundle();a=self.assessment(bundle,'A');z=self.assessment(bundle,'B')
        changed=b.read(z);changed['checkpoints'][0]['score']=0;b.dump(z,changed)
        with self.assertRaises(ValueError):b.finalize(a,z,bundle,self.root/'unresolved-final.json')
        cp=changed['checkpoints'][0];adj=self.root/'adjudication.json'
        b.dump(adj,{'adjudicator':{'id':'synthetic-adjudicator','model':'fixture','configuration':'synthetic-only'},'decisions':{cp['id']:{'original_positions':['A2','B0'],'canonical_basis':b.oracle('R01')[0]['evidence_ids'],'fixture_refs':['R01-F01'],'observation_refs':['O1'],'rationale':'Synthetic audit only','final':cp}}})
        b.finalize(a,z,bundle,self.root/'resolved-final.json',adj)

    def test_semantic_disagreement_and_gap_search(self):
        bundle=self.bundle('S01');a=self.assessment(bundle,'A');z=self.assessment(bundle,'B')
        changed=b.read(z);changed['semantic_findings'][0].update(classification='unsupported-invention',materiality=2)
        b.dump(z,changed)
        with self.assertRaises(ValueError):b.check_assessment(z,bundle)
        changed['semantic_findings'][0]['gap_search']='Synthetic scoped silence search';b.dump(z,changed)
        b.check_assessment(z,bundle)
        self.assertEqual(b.differences(b.read(a),changed),['concept:C1'])

    def profile(self):
        assessments=[];records={}
        for s in b.manifest()['scenarios']:
            r=self.record(s['id']);records[s['id']]=r
            a={k:r[k] for k in ['run_id','scenario_id','suite_fingerprint','canonical_baseline','build_sha256','configuration_sha256']}
            a.update(issues=[],checkpoints=[dict(id=c['id'],score=2,status='resolved',critical_triggered=False) for c in b.oracle(s['id'])],semantic_findings=[])
            assessments.append(a)
        return assessments,records

    def test_dimensional_gates_and_incompleteness(self):
        aa,rr=self.profile();result=b.calculate(aa,rr)
        self.assertEqual(result['verdict'],'Additional profile only')
        self.assertTrue(all(x['score']==100 for x in result['dimensions'].values()))
        self.assertNotIn('overall_score',result)
        aa[0]['checkpoints'][0].update(score=0,critical_triggered=True,incident_id='synthetic-incident')
        self.assertEqual(b.calculate(aa,rr)['verdict'],'Material fitness gaps demonstrated')
        self.assertEqual(b.calculate(aa[:-1],rr)['verdict'],'Incomplete or unresolved')
        aa,rr=self.profile();aa[0]['checkpoints'][-1]['score']=0
        self.assertTrue(b.calculate(aa,rr)['failed_cells'])
        rr['U02']['operators'][0]['id']=rr['U01']['operators'][0]['id']
        with self.assertRaises(ValueError):b.calculate(aa,rr)

if __name__=='__main__':
    unittest.main(verbosity=2)
