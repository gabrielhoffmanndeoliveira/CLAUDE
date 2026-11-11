import re,io
D='/home/user/CLAUDE/ths-seo/pages/'
def rd(n): return open(D+n,encoding='utf-8').read()
def rep(t,a,b,count=1):
    assert t.count(a)>=1, ('missing',a[:80])
    if count: assert t.count(a)==count, (t.count(a),a[:80])
    return t.replace(a,b)
def droprow(t,needle):
    rows=[m for m in re.finditer(r'<tr>.*?</tr>\n?',t,flags=re.S) if needle in m.group(0)]
    assert len(rows)==1,(needle,len(rows))
    return t.replace(rows[0].group(0),'')
PRO=' Gas piping, venting and combustion air work must follow the installation manual and local code and, in most jurisdictions, must be done by a licensed installer.'

# ---------- Navien
t=rd('navien-npe-comparison.html')
# NCB-240/110H product is DRAFT / out of stock: drop its row (RAL row stays)
m=re.search(r'<tr>\n<td><a href="[^"]+">NCB-240/110H</a></td>.*?</tr>\n',t,flags=re.S); assert m; t=t.replace(m.group(0),'')
# NPN-180E-LP is in stock again (1): restore row from live page data
u='<tr><td><a href="/products/navien-mid-efficiency-tankless-water-heater-max-dhw-input-180-000-btu-h-indoor-or-outdoor-wall-hung-residential-commercial-npn-180u-lp">NPN-180U-LP</a></td><td>180,000 BTU/h</td><td>Propane</td><td>0.81</td><td>8.5 GPM</td><td>6.6 GPM</td><td>4.6 GPM</td><td>0.5 GPM</td><td>No</td><td>14.0" W x 23.0" H x 9.3" D</td><td>60 lbs</td></tr>\n'
e=u.replace('indoor-or-outdoor-wall-hung-residential-commercial-npn-180u-lp','exterior-only-wall-hung-residential-commercial-npn-180e-lp').replace('NPN-180U-LP','NPN-180E-LP')
t=rep(t,u,u+e)
t=rep(t,'<p>The NPN-U is a universal indoor or outdoor unit. Navien now lists the NPN series as a legacy line, with the NHW series as its current non-condensing range.</p>','<p>NPN-U models install indoors or outdoors. NPN-E models are for exterior installation only. These are ordered by fuel: check the NG or LP suffix.</p>')
t=rep(t,'<p>* On models with built-in recirculation, the lower minimum flow applies when the recirculation mode is active. See the specification sheet for conditions.</p>','<p>* See the specification sheet for the conditions that apply to the lower minimum flow option.</p>')
t=rep(t,' Navien notes that energy use increases when a unit is set up for recirculation.','')
t=rep(t,'<li><strong>Gas line and vent.</strong> Navien states the NPE-2 series can run on 1/2" gas pipe up to 24 feet and can vent in 2" pipe up to 75 feet with a maximum of six elbows, deducting 8 feet per 90° elbow. Longer runs need larger pipe; confirm against the installation manual and the fuel gas code tables.</li>',
 '<li><strong>Gas line and vent.</strong> The gas pipe size and the vent diameter depend on the length of the run and the number of elbows. Size both from the tables in the installation manual and the fuel gas code.'+PRO+'</li>')
m=re.search(r'<h3>Can a Navien NPE-2 use an existing 1/2" gas line\?</h3>\n<p>.*?</p>\n',t,flags=re.S); assert m; t=t.replace(m.group(0),'')
t=rep(t,'so read the 67°F column and allow a small margin.','so read the 67°F column and expect slightly less flow than it shows.')
open(D+'navien-npe-comparison_REVIEWED.html','w',encoding='utf-8').write(t)

# ---------- ProTerra
t=rd('rheem-proterra-comparison.html')
t=rep(t,'PROPH50-T2-RH400-30</a></td><td>50 gal</td><td>208/240 V, 30 A breaker</td><td>3.88</td>','PROPH50-T2-RH400-30</a></td><td>50 gal</td><td>208/240 V, 30 A breaker</td><td>see spec sheet</td>')
t=rep(t,'<td>see spec sheet</td><td>45 gal</td>','<td>see spec sheet</td><td>see spec sheet</td>')
t=rep(t,'Models ending in 30 have the same tank and heat pump without the shut-off valve.','Models ending in 30 are the 30 amp models without the shut-off valve.')
t=rep(t,'<li><strong>Match the electrical supply.</strong>','<li><strong>Match the electrical supply.</strong> A new or altered circuit is work for a licensed electrician.')
open(D+'rheem-proterra-comparison_REVIEWED.html','w',encoding='utf-8').write(t)

# ---------- Rheem gas
t=rd('rheem-gas-tank-comparison.html')
t=droprow(t,'>PROG40-40N-RH67-PV<')
# drop UEF column (index: PRIORITY, store UEF values disagree with Rheem sheets)
assert t.count('<th>UEF</th>')==5
t=t.replace('<th>UEF</th>','')
n=0
def cut(m):
    global n
    cells=re.findall(r'<td>.*?</td>',m.group(0),flags=re.S)
    if len(cells)!=10: return m.group(0)
    assert re.fullmatch(r'<td>0\.\d+</td>',cells[6]),cells[6]
    del cells[6]; n+=1
    return '<tr>'+''.join(cells)+'</tr>'
t=re.sub(r'<tr><td>.*?</tr>',cut,t,flags=re.S); assert n==30,n
assert t.count('<td>3" or 4" PVC, ABS or CPVC</td>')==7
t=t.replace('<td>3" or 4" PVC, ABS or CPVC</td>','<td>PVC, ABS or CPVC; size: see spec sheet</td>')
t=rep(t,'T&P valve','T&amp;P valve',count=0)
t=rep(t,'with gas input, first-hour rating, UEF, tank height and vent requirements for each.','with gas input, first-hour rating, tank height and vent type for each.')
t=rep(t,'<p>Yes, but it is not a like-for-like swap. A power vent model needs a new plastic vent run to the outdoors, a 120 V outlet and a way to deal with the old B-vent opening. Vent length limits are in the installation manual for each model.</p>',
 '<p>Yes, but it is not a like-for-like swap. A power vent model needs a new plastic vent run to the outdoors, a 120 V outlet and a way to deal with the old B-vent opening. If other appliances share the old vent or chimney, it has to be re-evaluated for what remains connected. Vent sizes and length limits are in the installation manual for each model.'+PRO+'</p>')
open(D+'rheem-gas-tank-comparison_REVIEWED.html','w',encoding='utf-8').write(t)

# ---------- Ruud
t=rd('rheem-ruud-equivalents.html')
t=droprow(t,'>PRO+G40S-40N-RU62<'); t=droprow(t,'>PRO+E40-M2-RU-CG<')
t=rep(t,'<p>Where the Rheem model name is a link, we list that model too. Tank height and diameter are the same for both brands in each row.</p>','<p>Tank height and diameter are the same for both brands in each row.</p>')
t=rep(t,'This page lists the Ruud tank water heaters we carry and the Rheem model each one corresponds to, limited to pairs where published specifications for both brands show the same capacity, input and dimensions.','This page lists Ruud tank water heaters we carry and the Rheem model each one corresponds to, limited to pairs where the manufacturer specification sheets for both brands show the same capacity, input and dimensions.')
t=rep(t,'have the same published capacity, gas input or wattage and dimensions.','have the same published capacity, gas input and dimensions.')
t=rep(t,'<p>We have not matched these two Ruud models','<p>We have not matched these Ruud models')
open(D+'rheem-ruud-equivalents_REVIEWED.html','w',encoding='utf-8').write(t)
