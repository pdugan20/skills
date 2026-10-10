#!/usr/bin/env python3
"""Assemble inspected render bytes into comparison boards (no image edits)."""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import json,random
ROOT=Path(__file__).resolve().parents[1]
renders=ROOT/'renders'; review=ROOT/'review'; review.mkdir(exist_ok=True)
font=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',24)
small=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',18)
rng=random.Random(101026)
key={}
for task in ['product-new','product-refine','editorial-new','editorial-refine','native-new','native-refine']:
 arms=['baseline','impeccable','original'];rng.shuffle(arms)
 key[task]=dict(zip('ABC',arms))
 labels=list('ABC'); paths=[]
 for arm in arms:
  name=f'{task}-{arm}'+('.png' if task.startswith('native') else '.jpg')
  paths.append(renders/name)
 if task.endswith('refine'):
  labels=['BEFORE']+labels
  paths=[renders/(task+'-before.png' if task.startswith('native') else task.split('-')[0]+'-before.jpg')]+paths
 native=task.startswith('native'); cols=len(paths) if native or task.endswith('new') else 2
 w,h=(430,850) if native else (1100,760 if task.startswith('product') else 900)
 rows=(len(paths)+cols-1)//cols
 board=Image.new('RGB',(cols*(w+24)+24,rows*(h+70)+70),'#e7e7e2');d=ImageDraw.Draw(board)
 d.text((24,18),task.replace('-',' / ').upper()+' · matched typography comparison',font=font,fill='#262a27')
 for i,(label,path) in enumerate(zip(labels,paths)):
  im=Image.open(path).convert('RGB');im.thumbnail((w,h),Image.Resampling.LANCZOS)
  x=24+(i%cols)*(w+24);y=62+(i//cols)*(h+70)
  d.text((x,y),label,font=small,fill='#262a27');board.paste(im,(x,y+30))
  # Blind full resolution copies: reviewer need not read identity key.
  imfull=Image.open(path).convert('RGB');imfull.save(review/f'{task}-{label}.png')
 board.save(review/f'{task}-board.png')
(review/'identity-key.json').write_text(json.dumps(key,indent=2)+'\n')
print(json.dumps(key,indent=2))
