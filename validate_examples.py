import json,pathlib
from jsonschema import Draft202012Validator
p=pathlib.Path(__file__).parent
s=json.loads((p/'CMER_registry_schema.json').read_text());g=json.loads((p/'CMER_guard_dictionary.json').read_text());guards={x['code']:x for x in g['legal_transitions']}
for fn in sorted(p.glob('CMER_illustrative_record_*.json')):
 r=json.loads(fn.read_text());Draft202012Validator(s).validate(r)
 for t in r['transitions']:
  rule=guards[t['guard']];assert rule['source'] in ('ANY_EXCEPT_WITHDRAWN',t['from']) and rule['target']==t['to']
 print('PASS',fn.name)
