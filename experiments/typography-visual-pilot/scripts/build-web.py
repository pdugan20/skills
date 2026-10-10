#!/usr/bin/env python3
"""Build inert matched HTML specimens; no candidate runtime is executed."""
import json, pathlib, html
ROOT=pathlib.Path(__file__).resolve().parents[1]
FONTS={'Inter':'inter-Inter[opsz,wght].ttf','Source Serif 4':'sourceserif4-SourceSerif4[opsz,wght].ttf','IBM Plex Sans':'ibmplexsans-IBMPlexSans[wdth,wght].ttf'}
p1='We had walked this street a hundred times. That morning, with no appointment ahead of us, it seemed to contain an entirely different city.'
p2='There was a seam of light beneath the bookshop door, a pear tree leaning over a wall, the sound of someone practising a difficult piece of music. Nothing had changed. We had simply begun to notice.'
def t(role,text,tag='div',cl=''):
 return f'<{tag} class="{role} {cl}" data-role="{role}">{text}</{tag}>'
def page(task,c):
 product=task.startswith('product')
 styles='\n'.join(f'@font-face{{font-family:"{name}";src:url("../fonts/{file}");font-weight:100 900;font-style:normal;font-display:block;}}' for name,file in FONTS.items())
 styles+='\n'.join('.'+role+'{'+f'font-family:"{s["font"]}";font-size:{s["size"]}px;font-weight:{s["weight"]};line-height:{s["leading"]};letter-spacing:{s["tracking"]}em;'+'}' for role,s in c['roles'].items())
 styles+=':root{'+''.join(f'--{k}:{v}px;' for k,v in c['space'].items())+'}'
 base='''*{box-sizing:border-box}html,body{margin:0;background:#F6F3EB;color:#262A27}body{width:1100px;font-optical-sizing:auto;-webkit-font-smoothing:auto}p,h1,h2{margin:0}main{position:relative;width:1100px;min-height:HEIGHTpx;padding:38px 48px 76px}header{display:flex;align-items:baseline;justify-content:space-between;border-bottom:1px solid #CFCFC3;padding-bottom:22px}.muted,.meta,.eyebrow{color:#626960}.header-left{display:flex;align-items:baseline;gap:22px}.hero{margin-top:54px}.eyebrow{margin-bottom:20px}.title{margin-bottom:var(--titleAfter)}.deck{margin-bottom:var(--deckAfter)}.section{margin-top:var(--sectionBefore);margin-bottom:16px}footer{position:absolute;bottom:28px;left:48px;right:48px;border-top:1px solid #CFCFC3;padding-top:18px;display:flex;justify-content:space-between;align-items:baseline}.product-hero{display:grid;grid-template-columns:1fr 390px;gap:36px;align-items:center}.stats{display:grid;grid-template-columns:1fr 1fr 1.3fr;gap:20px;border-left:1px solid #CFCFC3;padding-left:26px}.stat .meta{margin-top:9px}.table{margin-top:var(--sectionBefore)}.tr{display:grid;grid-template-columns:4fr 1.65fr 1.25fr 1fr;gap:20px;align-items:baseline;border-bottom:1px solid #CFCFC3;padding:var(--rowGap) 0}.th{padding:0 0 14px}.tr>:last-child{text-align:right}.status{color:#52604E}.editorial .hero{max-width:920px}.editorial .title{max-width:910px}.editorial .deck{max-width:650px}.byline{display:flex;gap:28px}.article-grid{display:grid;grid-template-columns:644px 236px;gap:76px;margin-top:var(--sectionBefore)}.article-grid .section{margin-top:0}.body p{margin-bottom:var(--paragraphAfter)}aside{padding-top:36px;border-top:1px solid #CFCFC3;margin-top:34px}.editorial .hero>.eyebrow{display:flex;justify-content:space-between}.editorial footer{font-variant-numeric:tabular-nums}'''.replace('HEIGHT','760' if product else '900')
 if product:
  header='<div class="header-left">'+t('brand','Index')+t('meta','Editorial workspace')+'</div>'+t('meta','Autumn 2026')
  stats=''.join('<div class="stat">'+t('value',v)+t('meta',l)+'</div>' for v,l in [('12','Stories'),('04','In review'),('Oct 28','Publish date')])
  hero='<div class="product-hero hero"><div>'+t('eyebrow','AUTUMN 2026')+t('title','Issue 08','h1')+t('deck','A place for things worth keeping.')+'</div><div class="stats">'+stats+'</div></div>'
  rows=[('The quiet work of restoration','Nora Ellis','In review','Today'),('An ordinary kind of wonder','Theo Park','Draft','Yesterday'),("A room of one's own",'June Hara','Ready','Oct 08'),('Objects that stay','Luca Reed','In review','Oct 07')]
  content='<div class="table"><div class="tr th">'+''.join(t('section',x) for x in ['Story','Author','Status','Updated'])+'</div>'+''.join('<div class="tr">'+t('item',r[0])+t('body',r[1])+t('meta',r[2],cl='status')+t('meta',r[3])+'</div>' for r in rows)+'</div>'
  footer=t('meta','Every story starts with a good question.')+t('meta','View archive →')
 else:
  header='<div class="header-left">'+t('brand','FIELD NOTES')+t('meta','A journal of everyday life')+'</div>'+t('meta','Vol. 08 · Autumn 2026')
  title='The art of<br>paying attention' if c['titleBreak']=='after-art' else 'The art of paying attention'
  hero='<div class="hero">'+t('eyebrow','<span>ESSAY</span><span>01</span>')+t('title',title,'h1')+t('deck','A walk without a destination can change the shape of a day.')+'<div class="byline">'+''.join(t('meta',x) for x in ['Nora Ellis','October 10, 2026','8 min read'])+'</div></div>'
  content='<div class="article-grid"><article>'+t('section','Opening note','h2')+t('body','<p>'+p1+'</p><p>'+p2+'</p>')+'</article><aside>'+t('item','“Attention is a way of making room.”')+'</aside></div>'
  footer=t('meta','FIELD NOTES')+t('meta','01—08')
 return '<!doctype html><html lang="en"><meta charset="utf-8"><title>Typography specimen</title><style>'+styles+base+'</style><main class="'+('product' if product else 'editorial')+'"><header>'+header+'</header>'+hero+content+'<footer>'+footer+'</footer></main><script>document.fonts.ready.then(()=>{document.documentElement.dataset.fontProof=JSON.stringify(Array.from(document.fonts).map(f=>({family:f.family,status:f.status})));});</script></html>'
for path in sorted((ROOT/'treatments').glob('*.json')):
 for task,c in json.loads(path.read_text()).items():
  if not task.startswith('native'): (ROOT/'renders'/f'{task}-{path.stem}.html').write_text(page(task,c))
before=json.loads((ROOT/'briefs/before.json').read_text())
for task,c in before.items():
 if not task.startswith('native'): (ROOT/'renders'/f'{task}-before.html').write_text(page(task,c))
print('Built HTML specimens')
