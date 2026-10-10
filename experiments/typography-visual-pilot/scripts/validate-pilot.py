#!/usr/bin/env python3
"""Check specimen integrity and technical evidence; never score beauty."""
from pathlib import Path
from PIL import Image
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]
CASES=[f'{s}-{m}' for s in ('product','editorial','native') for m in ('new','refine')]
ROLES={'brand','eyebrow','title','deck','body','meta','section','item','value'}
for arm in ('baseline','impeccable','original'):
 data=json.loads((ROOT/'treatments'/f'{arm}.json').read_text())
 assert set(data)==set(CASES),(arm,'case mismatch')
 for case,c in data.items():
  assert set(c['roles'])==ROLES
  allowed={'system','serif','rounded','Georgia'} if case.startswith('native') else {'Inter','Source Serif 4','IBM Plex Sans'}
  for role,r in c['roles'].items():
   assert r['font'] in allowed,(arm,case,role)
   assert 8<=r['size']<=100 and 100<=r['weight']<=900 and .8<=r['leading']<=2
  image=ROOT/'renders'/(f'{case}-{arm}'+('.png' if case.startswith('native') else '.jpg'))
  expected=(860,1700) if case.startswith('native') else (1100,760 if case.startswith('product') else 900)
  with Image.open(image) as im: assert im.size==expected,(image,im.size)
for row in json.loads((ROOT/'fonts/provenance.json').read_text()):
 p=ROOT/'fonts'/row['file'];assert hashlib.sha256(p.read_bytes()).hexdigest()==row['sha256'],p
for family in ('inter','sourceserif4','ibmplexsans'):
 assert 'SIL OPEN FONT LICENSE' in (ROOT/'fonts'/f'{family}-OFL.txt').read_text()
proof=json.loads((ROOT/'renders/web-font-proof.json').read_text());assert len(proof)==14
for row in proof:
 assert row['used'] and all(any(f['family']==name and f['status']=='loaded' for f in row['fonts']) for name in row['used']),row['name']
for surface in ('product','editorial'):
 rows=json.loads((ROOT/'renders'/f'web-{surface}-report.json').read_text());assert len(rows)==7
 for row in rows:
  assert row['viewport']==row['size'],row['name']
  assert row['contentBottom']<row['footerTop'],row['name']
details=json.loads((ROOT/'renders/web-detail-report.json').read_text())
for row in details: assert not any(r['overflow'] for r in row['roles']),row['name']
# Compare whitespace-normalized visible text by role across all arms, independent of styling.
for case in [c for c in CASES if not c.startswith('native')]:
 rows=[d for d in details if d['name'].startswith(case+'-')]
 def copy(r):return [(t['role'],''.join(t['text'].split())) for t in r['roles']]
 assert len(rows)==3 and all(copy(r)==copy(rows[0]) for r in rows),case
native=json.loads((ROOT/'renders/native-render-report.json').read_text())
# Report schema is rendered by Swift; walk it to catch any geometry issues.
def check(value):
 if isinstance(value,dict):
  if 'issues' in value: assert value['issues']==[],value['issues']
  for v in value.values():check(v)
 elif isinstance(value,list):
  for v in value:check(v)
check(native)
assert (ROOT/'renders/native-new-before.png').read_bytes()==(ROOT/'renders/native-refine-before.png').read_bytes()
for case in CASES:
 assert (ROOT/'review'/f'{case}-board.png').is_file()
print('PASS: 18 treatments, font hashes/licenses/loading, normalized web copy, dimensions, overflow and native geometry; aesthetics require visual judgment.')
