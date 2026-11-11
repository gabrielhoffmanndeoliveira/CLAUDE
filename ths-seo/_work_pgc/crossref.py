import json,csv
T='/root/.claude/projects/-home-user-CLAUDE/0f3e2c18-f81e-5ab6-aaac-9938e971fa96/tool-results/mcp-Shopify-graphql_query-1794410472186.txt'
live={n['id'].split('/')[-1]:n for n in json.load(open(T))['data']['nodes']}
imp=list(csv.DictReader(open('Products_replaces_crossref_matrixify.csv',encoding='utf-8')))
COL='Metafield: custom.replaces [list.single_line_text_field]'
assert len(live)==15 and all(r['ID'] in live for r in imp)
with open('Products_replaces_crossref_matrixify_ROLLBACK_live.csv','w',encoding='utf-8',newline='') as o:
    w=csv.writer(o,quoting=csv.QUOTE_ALL); w.writerow(['ID','Handle','Command',COL])
    for r in imp:
        n=live[r['ID']]; assert n['handle']==r['Handle'],(n['handle'],r['Handle'])
        w.writerow([r['ID'],n['handle'],'UPDATE',n['replaces']['value'] if n['replaces'] else ''])
rev=list(csv.DictReader(open('REVIEW_replaces_crossref_notes.csv',encoding='utf-8')))
EXCL=['VR8215S1503','L8148E1265','T87N1000','SV9501M8129']
out=[];log=[]
for r in imp:
    n=live[r['ID']]; vals=json.loads(r[COL]); keep=[];why=[]
    rr={x['Old part number']:x for x in rev if x['Handle']==r['Handle']}
    assert set(rr)==set(vals),(r['Handle'],set(rr)^set(vals))
    for v in vals:
        x=rr[v]; c=x['Confidence']; notes=x['Notes']; two=' | ' in x['Source URL']
        if any(e in x['Title'] for e in EXCL): why.append(f'{v}: excluded by task'); continue
        if c=='high': keep.append(v); continue
        if 'PRIORITY' in notes: why.append(f'{v}: PRIORITY'); continue
        if not two or 'single document' in notes or 'Same crossover sheet' in notes: why.append(f'{v}: one source only'); continue
        if 'best match' in notes: why.append(f'{v}: second source was a guess'); continue
        if 'misaligned' in notes: why.append(f'{v}: source extraction misaligned'); continue
        keep.append(v)
    print(n['status'],n['totalInventory'],r['Handle'][:50],'| live:',n['replaces'],'| keep',keep,'| drop',why)
    out.append((r,n,keep,why))
json.dump([{'id':n['id'],'handle':n['handle'],'keep':k,'why':w} for r,n,k,w in out],open('_work_pgc/crossref_plan.json','w'),indent=1)
with open('Products_replaces_crossref_matrixify_REVIEWED.csv','w',encoding='utf-8',newline='') as o:
    w=csv.writer(o,quoting=csv.QUOTE_ALL); w.writerow(['ID','Handle','Command',COL])
    for r,n,k,_ in out:
        if k: w.writerow([r['ID'],r['Handle'],'UPDATE',json.dumps(k)])
