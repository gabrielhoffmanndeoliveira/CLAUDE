import re,glob,csv,os,html.parser
D='/home/user/CLAUDE/ths-seo/guides/'
def rep(t,a,b):
    assert t.count(a)==1,(t.count(a),a[:70]); return t.replace(a,b)
E={}
E['atmospheric-vs-direct-vent-vs-power-vent-water-heaters']=[
 (' It is also the standard type for manufactured housing.',''),
 (' and lists PVC, ABS or CPVC vent and air inlet pipe with vent lengths up to 100 feet on its Professional Classic PDV models.',' and lists PVC, ABS or CPVC vent and air inlet pipe on its Professional Classic PDV models.'),
 ('<a href="/products/rheem-40-gallon-40-000-btu-h-professional-classic-power-vent-natural-gas-water-heater">Rheem 40 gallon power vent</a>','<a href="/products/rheem-50-gallon-42-000-btu-h-professional-classic-power-vent-natural-gas-water-heater">Rheem 50 gallon power vent</a>'),
]
E['condensing-appliance-vent-pipe-pvc-cpvc-polypropylene']=[
 ('Polypropylene handles the most of the three plastics and is the only one manufactured and listed specifically as a flue gas vent system.','Polypropylene handles the most of the three plastics and is sold as a listed flue gas vent system.'),
 ('PVC and CPVC pipe are made to plumbing pressure-pipe standards. Pipe manufacturers generally do not rate them as flue gas vents; their use rests on the appliance manufacturer\'s instructions.','Standard PVC and CPVC pipe is made to plumbing pipe standards. Pipe manufacturers generally do not rate it as a flue gas vent; its use rests on the appliance manufacturer\'s instructions.'),
 ('Canada has required S636-listed venting for years, and US codes and manufacturers have been moving toward listed vent systems as well. ','Canada requires S636-listed venting. '),
]
E['hot-water-recirculation-pump-buying-guide']=[
 (' Grundfos limits its ALPHA COMFORT SYSTEM to a maximum of 1.2 gpm for this reason.',' Grundfos sets a default flow limit of 1.2 gpm on its ALPHA COMFORT SYSTEM, which it gives as the recommended limit for 1/2 inch pipe.'),
 ('A pump on a timer that makes a tankless heater fire for hours every day shortens the life of the unit and can affect the warranty.','A timer-only loop can make a tankless heater fire for hours every day, so check the manual and the warranty terms before setting one up.'),
 ('(control modes, 95-102°F temperature band, 1.2 gpm limit, dedicated return versus comfort valve)','(control modes, 95-102°F temperature band, 1.2 gpm flow limit, dedicated return versus comfort valve)'),
]
E['indirect-water-heater-sizing-and-piping']=[
 ('increases the usable hot water from a given tank by roughly a third.','increases the usable hot water from a given tank by roughly a quarter to a third, depending on the cold water temperature.'),
 ('Most residential indirect coils have 1 inch connections. Reducing to 3/4 inch cuts flow and recovery.','Many residential indirect coils have 1 inch connections. Use the pipe size the tank manual specifies; reducing it cuts flow and recovery.'),
]
E['oxygen-barrier-vs-non-barrier-pex']=[
 ('and it quickly loses its dissolved oxygen, which is what keeps iron and steel parts from rusting.','and it quickly uses up its dissolved oxygen. With no fresh oxygen arriving, iron and steel parts stop rusting.'),
 ('gas work requires a licensed professional in every jurisdiction.','gas work requires a licensed professional in most jurisdictions.'),
]
E['pex-fitting-compatibility-f1960-f1807-f2159']=[
 ('<td>Only if the tubing is marked F1960</td><td>No</td>','<td>Only if the tubing is marked F1960</td><td>Only if the tubing is marked F1960</td>'),
]
E['replacing-a-discontinued-honeywell-thermostat']=[
 ('<td>PRO 2000 and 4000 programmable, FocusPRO 6000, T4 Pro</td>','<td>PRO 2000 and 4000 programmable, FocusPRO 6000</td>'),
 (' For example, the FocusPRO N100 TH1210U4001 (2 heat/1 cool heat pump, 1 heat/1 cool conventional) lists earlier non-programmable models, and the P200 TH2110U4004 lists the FocusPRO 6000 models TH6110D1005 and TH6110D1021.',''),
 ('Wi-Fi and Z-Wave models generally need a C wire or an adapter.','Wi-Fi models generally need a C wire or an adapter.'),
 ('The newer lines mount on Resideo\'s UWP wall plate, which is different from the FocusPRO 5000 and 6000 sub-base. Plan to move the wires to the new plate.','The T6 Pro mounts on Resideo\'s UWP wall plate, which is different from the FocusPRO 5000 and 6000 sub-base. Whichever model you choose, plan to move the wires to the new plate.'),
]
E['viega-propress-vs-megapress-vs-pureflow']=[]
SKIP={'combi-boiler-sizing-guide':"Skipped: the live article what-is-a-combi-boiler already has a full 'How to size a combi boiler' section (heating load, GPM formula, Navien model fit, gas line). Also: draft gives NCB-250/150H 210,000 BTU/h DHW input while the store title says 199,900; Navien flow and minimum-input figures were not verified."}
NOTES={
'atmospheric-vs-direct-vent-vs-power-vent-water-heaters':"Removed unverified '100 feet' PDV vent length and the manufactured-housing sentence; power vent example link moved from the 40 gal (out of stock) to the 50 gal model. Partial overlap with one section of best-gas-water-heaters-how-to-compare.",
'condensing-appliance-vent-pipe-pvc-cpvc-polypropylene':"Corrected the claim that polypropylene is the only listed plastic vent (UL 1738 listed PVC/CPVC systems exist); removed unsupported statement about US codes. Navien NPE-2 figures (2 in. 75 ft, 3 in. 150 ft, 8 ft / 5 ft per 90 elbow) checked against Navien spec sheet and quick installation guide by search; an older Navien guide shows 60 ft for 2 in., the article already tells readers to use the manual for their model. Partial overlap with the venting section of what-is-a-combi-boiler.",
'hot-water-recirculation-pump-buying-guide':"Grundfos 95-102 F band and 1.2 gpm limit checked on Grundfos training pages; 1.2 gpm reworded (it is an adjustable default for 1/2 in. pipe, not an erosion limit). Reworded unsupported claim that timer loops shorten tankless life. Taco SmartPlus-e product is ACTIVE but has 0 inventory.",
'indirect-water-heater-sizing-and-piping':"Recovery table recalculated and correct. Softened 'roughly a third' and '1 inch connections'. Tank-size table is a rule of thumb with no manufacturer source; labelled as a starting point in the text.",
'oxygen-barrier-vs-non-barrier-pex':"Fixed an ambiguous sentence on dissolved oxygen; 'every jurisdiction' changed to 'most jurisdictions'. Loop-length table is industry rule of thumb (PPI/RPA cited), labelled as such.",
'pex-fitting-compatibility-f1960-f1807-f2159':"PEX-C / F1960 cell changed from 'No' to 'Only if the tubing is marked F1960' to agree with the print-line rule. Partial overlap with the fittings section of pex-a-vs-pex-b.",
'replacing-a-discontinued-honeywell-thermostat':"Removed unverified 'replaces' examples (TH2110U4004 / TH6110D), the T4 Pro mention, the Z-Wave C-wire claim and the claim that N100/P200 use the UWP plate. N100 and P200 example products are ACTIVE with 0 inventory. Stage options for N100/P200 come from the cited Resideo sell sheets, not re-verified.",
'viega-propress-vs-megapress-vs-pureflow':"No text changes. Figures match Viega literature as cited (not re-fetched). Links to the new oxygen-barrier guide, so that guide is published first.",
}
class V(html.parser.HTMLParser):
    void={'br','img','hr'}
    def __init__(s): super().__init__(); s.st=[]; s.bad=[]
    def handle_starttag(s,t,a):
        if t in('script','style'): s.bad.append(t)
        if any(k.startswith('on') for k,_ in a): s.bad.append('handler')
        if t not in s.void: s.st.append(t)
    def handle_endtag(s,t):
        if not s.st or s.st[-1]!=t: s.bad.append('unbalanced '+t)
        else: s.st.pop()
rows=[]
for f in sorted(glob.glob(D+'NEW_*.html')):
    if f.endswith('_REVIEWED.html'): continue
    h=os.path.basename(f)[4:-5]
    t=open(f,encoding='utf-8').read()
    m=re.match(r'<!--\n(.*?)-->\n',t,flags=re.S); hd=dict(l.split(': ',1) for l in m.group(1).strip().split('\n'))
    body=t[m.end():]
    title,seo,meta=hd['Title'],hd['SEO title'],hd['Meta description']
    assert len(seo)<=60 and len(meta)<=155,(h,len(seo),len(meta))
    assert hd['Suggested handle']==h
    if h in SKIP:
        rows.append([os.path.basename(f),h,title,seo,meta,'skipped',SKIP[h]]); continue
    for a,b in E[h]: body=rep(body,a,b)
    v=V(); v.feed(body); assert not v.bad and not v.st,(h,v.bad,v.st)
    assert '<!--' not in body
    open(D+f'NEW_{h}_REVIEWED.html','w',encoding='utf-8').write(body.strip()+'\n')
    rows.append([os.path.basename(f),h,title,seo,meta,'publish',NOTES[h]])
    print(h,len(body),len(seo),len(meta))
with open(D+'GUIDES_new_index.csv','w',encoding='utf-8',newline='') as o:
    w=csv.writer(o,quoting=csv.QUOTE_ALL); w.writerow(['File','Handle','Title','SEO title 60 max','Meta description 155 max','Decision','Notes']); w.writerows(rows)
