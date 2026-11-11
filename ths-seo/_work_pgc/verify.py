import json,re,html,csv,difflib
T='/root/.claude/projects/-home-user-CLAUDE/0f3e2c18-f81e-5ab6-aaac-9938e971fa96/tool-results/mcp-Shopify-graphql_query-1794439681725.txt'
d=json.load(open(T))['data']
def norm(s):
    s=html.unescape(s).replace(' ',' ')
    s=re.sub(r'>\s+<','><',s); s=re.sub(r'\s+',' ',s).strip()
    s=s.replace('<tbody>','').replace('</tbody>','').replace('<thead>','').replace('</thead>','')
    return s
def cmp(live,f):
    a=norm(live); b=norm(open(f,encoding='utf-8').read())
    if a==b: return 'match'
    sm=difflib.SequenceMatcher(None,a,b,autojunk=False)
    out=[(t,a[i1:i2][:80],b[j1:j2][:80]) for t,i1,i2,j1,j2 in sm.get_opcodes() if t!='equal']
    return f'DIFF {len(out)}: {out[:6]}'
res={}
pmap={'navien-model-comparison':'navien-npe-comparison','rheem-proterra-comparison':'rheem-proterra-comparison','rheem-gas-water-heater-comparison':'rheem-gas-tank-comparison','rheem-ruud-equivalent-models':'rheem-ruud-equivalents'}
for p in d['pages']:
    r=cmp(p['body'],f"pages/{pmap[p['handle']]}_REVIEWED.html"); res[p['handle']]=(p,r)
    print(p['id'],p['handle'],p['isPublished'],len(p['body']),r,[(m['key'],len(m['value'])) for m in p['metafields']['nodes']])
idx={r['Handle']:r for r in csv.DictReader(open('guides/GUIDES_new_index.csv',encoding='utf-8'))}
arts={a['handle']:a for a in d['articles']['nodes']}
for h,r in idx.items():
    a=arts.get(h)
    if not a: print('NOT LIVE',h,r['Decision']); continue
    mf={m['key']:m['value'] for m in a['metafields']['nodes']}
    print(a['id'],h,a['isPublished'],a['blog']['handle'],a['author']['name'],cmp(a['body'],f'guides/NEW_{h}_REVIEWED.html'),a['title']==r['Title'],mf.get('title_tag')==r['SEO title 60 max'],mf.get('description_tag')==r['Meta description 155 max'])
plan={x['id']:x for x in json.load(open('_work_pgc/crossref_plan.json'))}
for p in d['prods']:
    want=plan[p['id']]['keep']; got=json.loads(p['replaces']['value']) if p['replaces'] else []
    print(p['id'].split('/')[-1],'OK' if want==got else 'MISMATCH',got,p['replaces']['id'] if p['replaces'] else '')
json.dump({'pages':[{k:p[k] for k in('id','handle','title','metafields')} for p in d['pages']],'arts':{h:a['id'] for h,a in arts.items()},'prods':{p['id']:(p['replaces'] or {}).get('id') for p in d['prods']}},open('_work_pgc/live_ids.json','w'))
