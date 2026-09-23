<!-- Registro de casos do projeto TFAS. Movido VERBATIM de CLAUDE.md em 23 Sep 2026; nada foi reescrito. Nao e carregado automaticamente: leia sob demanda. E cronologico: entradas posteriores corrigem anteriores; em caso de conflito vale a mais recente e o nucleo em CLAUDE.md. -->

# honeywell-notifier

- **Accessory specs often live in the parent panel's data sheet.** There is no BB-100
  data sheet; Notifier `DN-7070` (the NFS2-3030 sheet) carries dimensions and capacity
  for BB-100, BB-200, NFS-LBB and BB-UZC together. Check the parent panel before
  concluding an accessory is undocumented.
- [CORRIGIDO — `DN-7045` resolve em `notifier-us/hon-ba-fire-dn-7045.pdf`; ver honeywell-system-sensor.md] **EDAM has dropped some Notifier documents entirely.** `DN-7045` 404s under both
  `notifier-us/` and the flat datasheets directory. `honeywellbuildings.in` is a
  Honeywell-operated regional site that still serves them &mdash; first-party, but
  older revisions, so cross-check against a current datasheet before using it.
- **The invisible-dimension trap.** Older Notifier "Document NNNNN" drawings carry
  their dimensions as **vector linework, not text**. For `ABS-2D` (doc 52032)
  `get_text()` returned prose only, `find_tables()` returned garbage, and
  `get_images()` showed nothing but a logo &mdash; **nothing signalled that data was
  missing.** Rendering at 200 dpi and reading the image was the only route. Treat any
  enclosure document whose text carries no inch figures as a render-and-read job.
- **`prod-edam` holds separate `notifier-us/` and `notifier-aus/` trees with
  different documents for the same part number.** Prefer `-us`; a regional variant
  may genuinely differ. Also, an old revision on EDAM is not necessarily superseded
  &mdash; `DN-6643:A1` is from 2008 and is still the newest Notifier publishes for
  the NBG-12 Series.
- **The same mechanism on the `vendor` field fires almost not at all, which is itself
  the result.** 42 families, **2** split across brands. `B501` has four members under
  System Sensor and one, `B501-BL`, under Fire-Lite &mdash; and Honeywell genuinely
  sells that base under several brands (Notifier `DN-62046:C` lists it too), so no
  brand is *wrong*; the defect is the store disagreeing with itself inside one family.
  `E3-TRIMKIT` has the `-A` under Gamewell-FCI and the `-B` and `-C` under Honeywell,
  and **here the minority is the correct one**: the E3 series is Gamewell-FCI's panel
  line and &quot;Honeywell&quot; is the generic umbrella. Second outing, second time the
  outlier-is-not-the-defect caveat fired.
- **The product-class error is the most common real defect in this catalogue's
  titles &mdash; six cases now, and the last two both came from the manufacturer's own
  wording.** A relay sold as a
  resistor (`EOLR-1`), a riser monitor as a plain monitor (`SIGA-RM1`), a controller
  as a detector (`TSD-CJ-C01`), a horn strobe as a horn (`MTH-MC-R`), and a panel CPU
  as a display (`CPU2-3030D`). **The last one came from the manufacturer's own
  wording:** "NFS2-3030 Primary Display" is Notifier's verbatim heading in DN-7070,
  but it names the part's *role* and reads as an add-on annunciator, when the part is
  the CPU that the panel cannot run without. It is also the first where the Shopify
  `type` field gave no warning &mdash; it said "Annunciators", leaning the same wrong
  way. **So the type field is a useful signal when it disagrees and no signal at all
  when it agrees; verify the class from the document either way.** The sixth is
  Simplex `4100-9701`, typed **Annunciators**: `S4100-1031` Rev. 22 Table 8 lists it
  as the 4100ES **master controller** &mdash; 32-bit controller board, CPU card holding
  the site program, IDNet 2 loop card and the ES-PS supply. The panel does not run
  without it. That is the CPU2-3030D shape exactly, one generation of panel later, so
  **treat any &quot;display&quot;, &quot;annunciator&quot; or &quot;interface&quot;
  wording on a panel-family part as a class question until the ordering table settles
  it.**
- [CORRIGIDO — baterias também; ver neste arquivo &quot;BATTERIES are a third category&quot;] **The boundary is now proved on a single page, which is as clean as this gets.**
  Notifier `DN-62046:C` lists the 951 self-test detectors in its Product Line
  Information block with **no `-BP` variant of any kind**, and immediately beneath, in
  the Intelligent Bases sub-block on the same page, states
  **&quot;B300-6-BP: Bulk pack of B300-6, package contains 10&quot;** and
  &quot;B501-WHITE-BP: Bulk pack of B501-WHITE contains 10&quot;. Not two documents
  disagreeing, not two revisions, not two brands &mdash; **one page, one author, one
  date, stating the carton quantity for the base and declining to for the detector
  sitting above it.** So the rule is: **Honeywell states a carton quantity for bases,
  and for the low-frequency sounders via the `9021-62013:C` footnote, and for nothing
  else.** Detectors and notification appliances both fall outside it.
- **CORRECTION, 22 Sep 2026: that boundary was wrong. BATTERIES are a third category,
  and the quantities are not 10.** An agent found it and the coordinator verified it
  directly rather than taking the report on trust, because the claim overturned a rule
  this file states twice. Fire-Lite **`DF-52397:C1`** and its Notifier twin
  **`DN-6933:D`** each state five carton quantities verbatim in Ordering Information:
  `BAT-1250-BP: 10-unit bulk pack`, `BAT-1270-BP: 5-unit`, `BAT-12120-BP: 4-unit`,
  `BAT-12180-BP: 2-unit`, `BAT-12260-BP: 2-unit`. **So the rule becomes: Honeywell
  states carton quantities for bases, low-frequency sounders and batteries, and not for
  detectors or notification appliances.**
  **The sharper half of the finding is the one the agent did not draw: the quantity
  varies inversely with capacity &mdash; 10, 5, 4, 2, 2.** This catalogue's whole
  working assumption has been that `-BP` means ten, which is why the census phrase was
  *&quot;Bulk Pack with 10 Units&quot;*. On batteries that assumption is wrong four
  times out of five. **Checked against the live catalogue immediately: 18 `BAT-*` SKUs,
  two of them `-BP`, and neither asserts any quantity in its title** &mdash; so there is
  no live error, only an unclaimed documentary basis. Nothing was changed; both went to
  the owner's file.
  **The method lesson is the transferable one.** The rule was built from a genuinely
  strong proof &mdash; `DN-62046:C` stating a base's carton quantity and declining to
  state a detector's **on one page** &mdash; and it was still too broad, because the
  evidence covered bases against detectors and the conclusion said *&quot;and nothing
  else&quot;*. **A mechanism confirmed on two categories does not license a claim about
  every category.** The same over-reach the Protectowire spacing rule made when it
  broke at 220 &deg;F.
- **`NCM-F` is MULTIMODE, and there is no single-mode NCM at all.** `DN-6861:D` (3/5/19):
  62.5/125 or 50/125 &micro;m multimode, **ST connectors**, 820 nm, 8 dB budget on 62.5 and
  4.2 dB on 50. That is the **opposite** of `FSL-E3` (single-mode, 9/125, LC), so the
  fibre-mode field cannot be guessed from the brand or the letter.
  **And the 3,000 ft figure on that same data sheet belongs to the NCM-W twisted-pair
  board** &mdash; the adjacent-row trap, avoided. `DN-6861` publishes an optical loss
  budget and no distance for the fibre part, so no distance was published.
  The live page also said the NCM-F *&quot;connects FACPs to Network Control
  Annunciators&quot;*. It does not: the NCM is **each node's own interface to a peer
  network**, and panels and NCA annunciators alike carry one.
- **Sixteenth product-class error, and it is the releasing-gear shape for the THIRD time
  in six batches.** `RP-2002` was titled *&quot;Fire Alarm Control Panel&quot;*. Notifier's
  own title is **&quot;Agent Release Control Panel&quot;**. That follows `4099-9015` (a
  releasing station sold as an ordinary double-action pull station) and `2099-9149` (a
  manual release station typed Pull Stations). **Releasing equipment is consistently
  merchandised in this catalogue as ordinary fire equipment**, which is now a pattern
  rather than three coincidences, and it is the kind that costs a buyer the most: someone
  specifying a fire alarm panel receives a panel that discharges an agent.
  Everything else on that page verified, six zones included, and the panel **is** complete
  &mdash; but the IBC seismic claim it makes is only realisable with `SEISKIT-COMMENC`,
  *&quot;required for seismic-certified installations&quot;*, which is not supplied.
- **The `-IV` protocol convention is now documented outright on a THIRD brand, in the
  manufacturer's own words.** Notifier `DN-62004:B` (7/15/2019) Ordering block:
  ***&quot;'-IV' suffix indicates support of FlashScan and CLIP.&quot;*** That follows
  Gamewell-FCI (`9020-0620 Rev G`, Velociti-or-CLIP) and Fire-Lite (`DF-61011:C` and
  `DF-61010:C`, LiteSpeed-or-CLIP). **Three brands, five documents, one convention:
  ivory is legacy service stock carrying the dual-protocol build.** The `FPTI-951-IV`
  live title already said &quot;(FlashScan and CLIP)&quot; and was right. Also
  manufacturer-stated on the same sheet, and unusually: the FPTI-951 Series **replaces
  the FAPT-851 Series** &mdash; a sourced supersession, which is rare enough to note.
- **The micro-sign trap: a cousin of the Omega trap, and the first one found.**
  Notifier `DN-2243:B` prints the ISO-X standby current as **&quot;450 A&quot;** &mdash;
  the `&micro;` is dropped in extraction exactly as `&#937;` becomes `W`. 450 amperes on
  an SLC isolator module is absurd, which is the tell, and two independent documents
  settle it: installation sheet `I56-3624-001` prints **450 &micro;A** and `DN-60844:A`
  prints **&quot;450 &micro;A per circuit&quot;**. **So the Omega rule generalises to any
  prefix symbol** &mdash; &micro;, &#937;, &deg; &mdash; and the check is the same one:
  ask whether the bare number is physically possible for that quantity before writing it.
- **`DP-DISP` and `DP-DISP2` are different parts for different panels, and the store
  carries both correctly.** `DN-7111:O`: *&quot;DP-DISP2: Dress panel for top row in
  cabinet with CPU2-640/640E installed&quot;*; `DP-DISP` (no 2) serves a CPU2-3030D top
  row (`DN-7070:S`) and an NCA-2 on a CHS-M3 chassis (`DN-7047:H`), and **`DP-DISP2`
  appears zero times in `DN-7047:H`**. A one-character sibling pair separated by which
  CPU sits in the cabinet, both real. Both also require **two BMP-1 blanks** alongside
  them, which is the useful thing on a sheet-metal page.
- **A colour claim with no positive source, handled by naming the sibling instead of
  asserting or denying.** The live `BB-55F` copy said **Red**. Fire-Lite `DF-52220:A1`
  reads *&quot;**BB-55FR**: Same as BB-55F above but painted red&quot;*, and Notifier runs
  the identical convention cross-brand in `DN-7111:O` (*&quot;NFS-LBB &hellip; NFS-LBBR:
  Same as above but red&quot;*) &mdash; so the `R` is the red marker and the plain part is
  something else. **But no document states what the plain part's finish is**, and every
  distributor says red, which is correlated consensus for the fifth time. **Nothing was
  asserted either way**: the closing paragraph names `BB-55FR` and tells the buyer to
  confirm the finish. Note the defect is in the **description**, not the Shopify title,
  so it costs one channel.
- **Wide aspect is about FRAMING, not about shape, and a blanket ratio filter gets it
  wrong.** 28 Westell rows are 2.5:1 or wider and all 28 are correct &mdash; 1RU breaker,
  fuse and transition panels, which genuinely are that shape, with the subject filling the
  frame. The Notifier strips rejected earlier were the opposite: a small subject adrift in a
  2048 &times; 280 canvas. **Same ratio, opposite meaning.** So the third outcome recorded
  last batch needs restating: it is *&quot;subject too small in the frame&quot;*, which a
  ratio only hints at, and the resolution is to look.
- **A prefix documented on one panel family is not documented on another, and the agent
  declined the import.** `DR-APF100` was left as a bare `Brand PartNumber` title.
  Notifier's `DN-6857:C2` does settle the `DR-` prefix &mdash; DR-AA4/A4/B4/C4/D4 are each
  &quot;Door assembly&quot; &mdash; but **that is the CAB-4 cabinet family**, and no
  document names `DR-APF100` or `DR-AFP100`: the 142-page AFP-100 manual `51010:A`
  contains `DR-` **zero times** and calls its only trim part the DP-1-R dress panel, while
  `DN-6857` contains `AFP-100` zero times. Titling it &quot;door assembly&quot; would
  carry a convention across a panel-line boundary, which is the `PC2WKLED` case exactly.
  **Recorded as a bounded negative, not as a claim the part number is invented** &mdash;
  and note the store spells it `APF` where Notifier's panel is `AFP`, which a purchase
  order or a carton settles and a search does not.
- **The Notifier photo zero is 299 SKUs to 2, and only one of its three causes is a
  routing failure.** **21 are software licences** &mdash; Honeywell attaches
  `hbt-icon-licenses-and-agreements` to all of them and **no photograph can exist**, the
  same category as the FireWorks licences already on record. **49 are European numeric
  parts** (`020-xxx`, `002-xxx`), of which only 7 have any asset at all and **every one of
  those 7 is under 600 px at `?scl=1`** &mdash; a native-master size ceiling, not a
  matching problem. The rest sit in family records of 6 to 32 SKUs under one shot.
  **And a generic icon is doing most of the apparent coverage:** of 44 single-SKU records
  with no filename evidence, **30 resolve only to
  `hbt-icon-parts-and-accessories-primaryimage`, one icon attached to 1,677 records and
  1,916 SKUs.** That is the shared-identifier signature again, and without counting
  products per asset those 30 would have looked like hits.
- **Fifteenth incomplete-product case, and the housing proves it from the other side.**
  `FSP-851R` was typed Duct Detectors and titled a sensor. Notifier `DN-6935:E` calls it
  *&quot;a remote test capable detector for use with DNR(A)/DNRW duct detector
  housings&quot;*, **and the housing sheet `DN-60429:C2` closes the loop**: the DNR and
  DNRW housings *&quot;Require photoelectric smoke detector (sold separately)&quot;*, with
  a features bullet reading *&quot;code wheels on sensor head (sold separately)&quot;*.
  **Neither half is a duct detector**, and each document says so about the other &mdash;
  which is a stronger proof than the `PAD200-DD` and `D4S` cases, where only the complete
  unit's sheet named the head. **When a part looks like half a product, read the other
  half's data sheet.**
  A real purchasing trap came with it: a DNR or DNRW with **date code 0012 or earlier
  needs a DCOIL and auxiliary 24 VDC** before the remote-test feature the `R` buys works
  at all.
  Note the `type` field was judged **defensible rather than a defect** here: the `-R`
  variant exists only for duct service, so &quot;Duct Detectors&quot; is arguable even
  though the buyer receives a bare head. Flagged as a categorisation question, not
  counted as the ninth type-agrees-with-wrong-title case &mdash; **a judgement this file
  should make more often than it does.**
- **An unsourced claim in a title, and the only document naming the part is a REGIONAL
  one.** `SW-OW-CON`'s title asserted *&quot;Includes 5 Year&quot;* maintenance. The part
  number appears in **zero US Notifier documents** &mdash; not `DN-7048:Q`, not rev N, not
  the UK sheet &mdash; and turns up only in the **New Zealand/Australia** sheet
  `DOC-02-080 Rev E`, whose entire entry is *&quot;SW-OW-CON &mdash; ONYXWorks Software,
  View + Control&quot;*. **No term, no maintenance period, nothing.** Every source
  asserting five years is a distributor repeating one string. Dropped from the title and
  flagged, on the Trilogy &quot;Reel&quot; precedent: a price list settles it, another
  search will not.
  **And the coordinator misfiled the defect before the agent corrected it.** The briefing
  said that title *&quot;ends mid-phrase&quot;*, treating it as one of the ~300&ndash;400
  truncated titles. It is **103 characters**, well under the 150 cap, and ends on a
  complete word. What is wrong with it is an unsourced claim and a duplicated word, which
  is a different defect with a different fix. **Saying which defect a title has matters
  as much as saying which field it is in.**
  Route fact from it: **`prod-edam` carries a `notifier-nz/` tree** (and a
  `notifier-nz-2026/`), alongside the recorded `notifier-us/`, `-aus/`, `-uk/` and
  `farenhyt/`.
- **A supersession proved by ONE DOCUMENT NUMBER CARRYING TWO PRODUCT HEADINGS, and it
  is the cleanest proof of this kind the project has had.** `PSE-10`'s title asserted
  *&quot;(Replaced by HPF-PS10)&quot;* &mdash; a part number, a parenthetical and no class
  noun, the `ZH-MC-W` shape. This time the claim is **manufacturer-stated**, and the
  coordinator verified it directly because a supersession going *into* a feed title is
  rare here.
  **`DN-61092:C` (3/10/2021) is headed &quot;PSE-6/PSE-10 Series&quot;; `DN-61092:D`
  (8/15/2023) is headed &quot;HPF-PS6/HPF-PS10 Series&quot;** and its General paragraph
  reads verbatim: *&quot;The HPF-PS Series is a remote power supply line from Honeywell
  and is a **direct replacement for the PSE and FCPS Series**.&quot;* Its agency block
  then says it four more times &mdash; `S635, S674 (PSE Series, discontinued)`,
  `S635 (PSE-6C/PSE-10C discontinued)`, `7315-0028:0513 (PSE Series, discontinued)`,
  `2021-TMCOAP-001761-CERT (PSE Series, discontinued)`. **The document did not get a new
  number when the product line was replaced; it got a new revision.** No bulletin needed,
  and the claim stays in the title.
  **But the live title named the wrong successor, and that is the real defect.** Notifier
  states the replacement at **series** level only and publishes no part-for-part map, and
  the colour convention inverts across the generations: rev C has `PSE-10` plain with
  `PSE-10R` red, while rev D has **`HPF-PS10` RED and `HPF-PS10B` BLACK**. A buyer sent
  from PSE-10 to HPF-PS10 may receive a red cabinet where the outgoing part was not.
  Title now says **&quot;Replaced by HPF-PS Series&quot;**, which is exactly what Notifier
  says, with the colour trap in the body.
  **And two revisions are live at once under different slugs**, which is the sharp
  operational point: `hon-ba-fire-dn-61092.pdf` serves **rev C** while
  **`DN-61092-D.pdf`** &mdash; bare, uppercase, revision letter appended, under the
  `honeywell-edam` root &mdash; serves rev D. This file records that appending a revision
  letter *fails* (`9021-62013-E.pdf` returns the fingerprint). Both are true: it is
  per-document. **So a successful EDAM fetch is not evidence that you have the current
  revision** &mdash; check the header line, because the recorded route may hand you the
  superseded one.
- **Three more self-contradicting documents, nothing published from any.** `DN-62112:L`'s
  replacement-parts block calls the SLM-318 *&quot;a Signaling Line Circuit of 159
  addressable points&quot;* while a feature bullet on the same sheet says *&quot;Up to
  159 detectors and 159 modules per SLC; 318 devices per loop&quot;* &mdash; and its own
  N16x total of 3,180 is ten times 318, so the attributed bullet wins and 159 is the
  detector half. `E85010-0057`'s Engineering Specification asks for an *&quot;integral
  backup **1000 KHz** temporal tone generator&quot;* where page 1, page 2 and the specs
  table all give 1 kHz. And `HON-62115:A` writes the board version as `CLP-2PCB` in its
  column headers and `CLP2-PCB` in its own footnote. **Five documents in two batches:
  budget for it.**

- **`HOP-501-240` and `-480` are WATTS, not volts, and the warning was right to give.**
  Notifier's ordering table reads `HOP-501-240 | PSU 240W`, corroborated independently by
  its CONTROL PANELS block (the E10 ships with a 240 W supply, the E15 with a 480 W).
  **240 V is a real European mains voltage on a European Notifier prefix**, which is
  exactly what made the wrong reading plausible &mdash; the same shape as `AS-75-R-WP`,
  where the `75` looked like candela and the manufacturer's own note denies a 75 cd
  setting exists.
- **The `-IV` dual-protocol convention does NOT reach the FSP-851 series.** `DN-6935:E`
  says the plain series is *&quot;Compatible with FlashScan and CLIP protocol
  systems&quot;* with **no `-IV` variant in the sheet at all**. That convention was built
  on the 951 self-test line across three brands and **must not be imported here** &mdash;
  the fourth preventive refusal of a cross-family import, after two on the System Sensor
  `K` suffix and one on Notifier's `DN-7048` view-only sentence.
- **A byte and MD5 difference across two EDAM slugs is NOT evidence of two revisions.**
  `DN-6935` served at **88,456 and 88,321 bytes with different MD5s** from
  `notifier-us/hon-ba-fire-dn-6935.pdf` and the flat form &mdash; **identical text, same
  revision `DN-6935:E`.** This file recorded yesterday that `DN-61092` serves rev C and
  rev D from different slugs, which is real; this is the same observation with the
  opposite cause. **Check the header line, not the hash.**
- **A fourth document confirming the Honeywell pack-count boundary, on one page.**
  `DN-6935:E` numbers **bases** (`B210LPBP` 10, `B501BP` 10) and a **flange** (`F110BP`
  15) and numbers **no detector**, on the same page. That is the `DN-62046:C` proof
  reproduced on a different sheet of a different family &mdash; bases and accessories
  numbered, the detector above them not.
- **A recorded negative decayed for the second time on the same document, and a new EDAM
  prefix came with it.** This file states that &quot;EDAM has dropped some Notifier
  documents entirely&quot;, naming `DN-7045`. **`notifier-us/hon-ba-fire-dn-7045.pdf`
  returns a 416,302-byte real PDF.** And a shape not previously recorded:
  **`hon-ba-<docnum>.pdf`, the `hon-ba-` prefix WITHOUT `-fire-`**, resolved
  (`hon-ba-dn-60726.pdf`) where the `-fire-` form did not. Add it to the per-document path
  list beside bare, lowercased, underscore-for-hyphen, `<Model>_<DocNum>`, `<DocNum>_<Model>`
  and `hon-ba-fire-`. **Re-test a host-level negative before building a batch around the
  workaround** &mdash; that instruction is already in this file and this is its second
  confirmation in a week.
- **Twelfth incomplete-product case, manufacturer-stated in a single sentence, and the
  consequence is that the product cannot do the thing it is named for.** `DVC-RPU` is
  Notifier's Digital Voice Command **remote paging unit** &mdash; and at $2,300.75 the
  carton holds the keypad and display module only. Notifier orders the `CMIC-RP`
  microphone and well and the `CAB-RP`/`CAB-RPR` cabinet separately. **A paging station
  with no microphone cannot page.** The `type` said Annunciators and agreed with a title
  that named no missing part, raising nothing.
- **A search summary attributed a sentence to the wrong sibling and the agent caught it.**
  A summary claimed `DPA-1` is used when the `CMIC-1` is *not* used. That is `DN-7045`'s row
  for the **`DPA-1A4`**; the live sentence was verbatim Notifier for the correct part. The
  live copy was **incomplete, not wrong** &mdash; the `4100-9706` shape for the third time,
  where what reads as borrowed text is the manufacturer's own text about the right part.
- **A suffix documented ONLY by pairing, and the agent said so instead of papering over
  it.** `NFW-50XR` appears **exactly once** in each revision of `DN-60955` &mdash; in
  *&quot;DP-ES-R: Optional dress panel for the NFW-50XR (red)&quot;* against
  *&quot;DP-ES-B: &hellip; for NFW-50X (black)&quot;* &mdash; and has **no Product Line
  entry of its own**. What licenses &quot;Red&quot; is the predecessor sheet `DN-7102:E`
  using the identical two-line construction and defining it outright:
  *&quot;NFW-50R: Same as NFW-50, with red backbox and door.&quot;* Kept, because it was
  already live and is now supported; the communicator was deliberately left out of the
  title and described as an NFW-50X Series feature.
- **`DN-60955` serves two revisions under two DESCRIPTIVE slugs, which is the `DN-61092`
  trap on a different document.** `...intelligent-addressable-facp-with-communicator-datasheet.pdf`
  is rev C and `...fire-alarm-control-panel-data-sheet.pdf` is rev E. **A successful EDAM
  fetch is not evidence you have the current revision** &mdash; check the header line. Two
  independent instances in two days makes this a property of the host, not a one-off.
- **A listing claim wrong two ways, and the newer revision is what shows it.** The live
  Kidde copy said *&quot;UL Listed, ULC Listed and FM Approved for the Kidde ECS, ADS,
  ECS-500 and FE-13 systems&quot;*. In the compatibility table **the two FE-13 rows carry UL
  only**, and **Rev AF adds a row Rev AE does not have** &mdash; *Natura Inert Gas System
  (N2 pilot cylinders), FM only*. **Three distinct approval patterns on one part**, and
  reading Rev AE alone &mdash; the first search hit &mdash; would have missed both. This is
  the two-live-revisions problem for the third time this week, after `DN-61092` and
  `DN-60955`, and here the revisions differ in *content* rather than only in slug.
  An unsourced claim removed alongside it: *&quot;wire pairs about 30 inches long&quot;*
  appears in **no revision**, and a 260 dpi render of Figure 2 dimensions only the body and
  carries no wire length.
- **Two revisions of one sheet carry DIFFERENT AGENCY FILE NUMBERS, which is a new reason to
  publish none.** Fire-Lite `DF-51410` (2005) gives UL **R11746** and CSFM **3550-0075:173**;
  its Notifier issue `DN-5286:A1` (2010) gives UL/ULC **R4869** and CSFM **3550-0028:210**.
  Only the MEA number agrees. They also disagree on punctuation (`FM-900-100` against
  `FM900-100`). No file number was published. **A listing file number is exactly the kind of
  figure that looks safe to copy because it is not a spec.**
- **CORRECTION, AND THIS FILE WAS OVERCONFIDENT: `-IV` IS BOTH A PROTOCOL AND A COLOUR, AND
  NOTIFIER SAYS SO ON ONE PAGE.** This file states that *&quot;the `-IV` suffix encodes a
  PROTOCOL, not a colour&quot;* and, more strongly, that **&quot;any collection logic or copy
  treating `-IV` as a colour variant is wrong.&quot;** An agent contradicted it and the
  coordinator fetched `DN-60979:B` directly, because it overturns a rule this file asserts
  across three brands and five documents. **Both halves are printed on the same sheet:**
  the note reads verbatim ***&quot;&lsquo;-IV&rsquo; suffix indicates CLIP and FlashScan
  device&quot;***, and **every one of the fourteen `-IV` Product Line entries opens with the
  word Ivory** &mdash; `NP-200-IV: Ivory, low-profile intelligent photoelectric sensor`,
  `B300-6-IV: Ivory, 6&quot; base`, `B501-IV: Ivory color`, against `NP-200R` listed as
  **White, FlashScan only**.
  **What settles it beyond doubt is the members that have no protocol at all.**
  `TR300-IV` is a **replacement flange** and `CK300-IV` is a **colour kit**, and both carry
  the suffix. A flange has no communication protocol, so on those parts `-IV` can only be the
  finish. **So the suffix names the finish, and on devices that speak a protocol the ivory
  stock is also the dual-protocol build** &mdash; which is exactly what the original Gamewell
  finding said (*&quot;ivory is a service-stock designation that carries a dual-protocol
  build&quot;*) before this file compressed it into &quot;not a colour&quot;.
  **That compression is this project's own recurring error:** the `2099-` case is recorded
  here as a nuanced finding flattened into a false general rule, and this is the same failure
  on a suffix instead of a product line. The live `NP-200R-IV` title said *&quot;in Ivory
  Color&quot;* and **was correct**; the file's framing would have pushed an agent to delete a
  true claim. What the title actually lacked was the functionally important half. **Carry the
  exception, and when a rule says &quot;X, not Y&quot;, check whether the manufacturer says
  both.**
- **A live claim that is CONTRADICTED rather than merely unsourced, which is a stronger finding
  and a rarer one.** The `NP-200R-IV` page said the detector *&quot;is only compatible with
  Notifier's FireWarden **and ONYX** Series panels&quot;*. Verified by the coordinator in the
  same fetch: **`ONYX` appears 0 times and `NFS` 0 times in `DN-60979:B`**, whose own text reads
  ***&quot;Exclusively for use with NOTIFIER's FireWarden Series addressable fire alarm control
  panels&quot;***. So this is not the usual unsourced-claim case where the document is silent
  &mdash; **the document says the opposite word, &quot;exclusively&quot;.** A buyer with an
  ONYX panel could have ordered it. Removed, and the exclusivity promoted into the title.
  **Defect field: the description body, not the Shopify `title`** &mdash; one channel, not two.
- **An EDAM document unreachable by every recorded shape built from a GUESSED document
  number.** Seven probes for `DH-60541` across both roots all returned the 8,047-byte
  fingerprint; the working slug is `notifier-us/hon-ba-fire-dn-60229.pdf` under the
  `honeywell-edam` root, **found by search**, identical 365,567 bytes with and without
  `?download=false`. *Find the number, then build the slug* &mdash; the path shapes are a way
  of trying a **known** number, not a way of finding one.
  From that document, the `EQBB-D4` answer and a trap larger than the one asked about:
  Notifier states *&quot;a complete cabinet assembly consists of a door, a backbox, and an
  optional semi-flush trim ring&quot;*, so the matching door is `EQDR-D4` &mdash; **and the EQ
  door is a vented blank taking no dress plate, so Notifier states these cabinets are &quot;not
  appropriate for control equipment, annunciators, or remote microphones.&quot;** A buyer
  sizing a cabinet by tier count could put a panel in one. Its dimensions are printed twice and
  **pages 2 and 4 disagree** (2-5/8 in. against 2-9/16 in.); only the figures both pages agree
  on were published.

- **A SUPERSESSION THE MANUFACTURER STATES AND A SUCCESSOR THAT LOSES A FEATURE, ON ONE PAIR
  IN ONE BATCH &mdash; and the feature loss is the thing nobody would have checked.** Notifier
  bulletin **M22.1 discontinues `MODBUS-GW` on 28 Feb 2022** and points at the CLSS Gateway
  Modbus feature `MODBUS-CGW`. The store carries both, the discontinued one live at
  **$1,982.30**. The successor is *better* on the obvious axis &mdash; ten monitored nodes
  against four, two Modbus masters against one &mdash; **and it does NOT read 4 to 20 mA analog
  values, which the legacy gateway does.** So a migration that looks like an upgrade silently
  drops analog reporting, and the register map and device codes differ, so it is not a
  drop-in either.
  **The rule this sharpens: when a supersession IS manufacturer-stated, the work is not
  finished.** This file's existing test asks for a spec that would have to be equal if the
  claim were true, and uses it to *disprove* unsourced claims (`SIGA-HRS`, 70 ft to 50 ft).
  Run the same test on a **sourced** claim and it stops being a disproof and becomes a
  migration warning. Both products' copy now names the split; the lifecycle question went to
  the owner, because discontinuation is a feed decision.
- **The `-IV` finding held on its first use after the correction, which is what a corrected rule
  should do.** `FSV-951R-IV` was titled with **Ivory** in it and that is right: Notifier's
  ordering table has an ivory column, `FSV-951R` being the white model. This is the batch after
  `DN-60979:B` forced this file to stop saying *&quot;`-IV` is a protocol, not a colour&quot;*,
  and the copy now states the finish from the ordering table and the protocol support from the
  device's own row, with neither standing in for the other.

- **ONE DOCUMENT NUMBER, FOUR BRAND ISSUES, THREE DIFFERENT SUPERSESSION STATEMENTS, ALL
  DATED THE SAME DAY &mdash; and this file's own note recorded one of them as the answer.**
  This file records `DN-61092:D` (8/15/2023) stating that the HPF-PS Series *&quot;is a direct
  replacement for the PSE and FCPS Series&quot;*, and the v2b47 briefing carried that as the
  fact to correct a live page by. The live page said **&quot;direct replacement for the
  5495/5499&quot;** and **it is also manufacturer-stated**:

  | issue | document | names as replaced |
  |---|---|---|
  | Notifier | `DN-61092:D` 8/15/2023 | PSE and FCPS Series |
  | Silent Knight | `SK-61095:D` 8/15/2023 | **5495/5499** |
  | Farenhyt | `FH-62003:D` 8/15/2023 | **5495/5499** |
  | Gamewell-FCI | `9021-61096:B` 1/25/2021 | **nothing at all** |

  **Verified directly by the coordinator**, because it corrects a recorded note: `SK-61095-D.pdf`
  under the `honeywell-edam` root opens *&quot;The HPF-PS Series is a remote power supply line
  from Honeywell and is a direct replacement for the 5495/5499&quot;* &mdash; and **`PSE` and
  `FCPS` appear ZERO times in it**, the exact inverse of the Notifier issue.
  **So a &quot;direct replacement for X&quot; sentence on a Honeywell multi-brand product is a
  statement about the READER'S INSTALLED BASE, not about the product.** Grepping only the
  Notifier issue would have called a correct live claim unsourced and removed it &mdash; the
  wrong-document-family failure where the *family* is the brand imprint rather than the product
  line. Both claims are in the body, attributed by brand issue, and **neither went into the
  title**: a single predecessor in a Merchant Center attribute is wrong for three quarters of
  the audience.
  Note the sibling slugs are derivable once the document number is known &mdash; `SK-61095`,
  `FH-62003`, `9021-61096` all resolved first try &mdash; which is the rare case where building
  a path works, because the *number* came from a search.
- **A suffix in no manufacturer source, and the reason a title was still written rather than a
  `null`.** `PSL-BT-122000-G4D`: `G4D` occurs **zero times** across all eleven datasheets, the
  117-page application guide and both lithium product pages, and the REST search returns `[]`
  for it and for the full SKU. The ordering authority lists **only `PSL-BT-122000 M8`**, and the
  terminal drawing &mdash; itself a superset of the ordering list &mdash; also shows only M8.
  **The sitemap discloses the likely pattern and simultaneously the reason not to assert it:**
  siblings are `psl-bt-121000-g24` and `psl-bt-48320-gc2`, which are BCI **group sizes** &mdash;
  but `PSL-BT-121000-G24` prints its group code in **four places at once** (page `<title>`, JSON
  `name`, `<h1>` and its datasheet heading) while `PSL-BT-122000` prints **none** in all four.
  That is the `DN-62046` inverted proof on a suffix: the manufacturer names the group when it
  means to, on a sibling in the same series, and declines to here.
  **The judgement that made a title possible: both readings leave the ELECTRICAL identity
  intact**, because the capacity is in the base number and it matches exactly. So the title
  carries voltage, capacity, energy, cycle life and Bluetooth &mdash; **and no dimensions, no
  group-size claim and no terminal.** **A title can be written around an unsourced suffix when
  the suffix cannot change the facts the title asserts**, which is a narrower and more useful
  rule than holding the whole product.
- **`DR-`/`SBB-` is shared across two Notifier cabinet families and the TRAILING DIGIT is the
  family marker.** The briefing called them CAB-4 numbers. `DN-62113` lists `DR-A5`, `SBB-A5`,
  `DR-B5B`, `SBB-E5` as **CAB-5**, while `DN-6857:C2` (CAB-4) uses `DR-A4`/`SBB-A4` and contains
  `ABP-1` and `ACM-30` **zero times each**. So a prefix that looks like a family marker is not
  one, and the one-character difference decides which cabinet a part fits.
  Two negatives recorded rather than guessed on that part: **no package quantity is stated**
  (&quot;pack&quot; and &quot;package&quot; are zero across `DN-62113` revisions **C and E** and
  `DN-62114:B`), and **no listing was claimed**, because both documents scope their agency
  blocks to the cabinet and modules and hedge that *&quot;certain modules or applications may
  not be listed&quot;* &mdash; a blank plate has no function to list, the `3-LDSM` precedent.

- **A fourth instance of two EDAM revisions under two slugs, and this one differs in
  substance.** `datasheets/notifier-us/hon-ba-fire-dn-62113.pdf` serves **rev C (7/11/2022)**
  and `datasheets/hon-ba-fire-notifier-cab5-datasheet-english.pdf` serves **rev E
  (03/17/2025)**, and rev E adds a ULC listing, an FM number, an IBC 2024 seismic certification
  and a 26 Ah battery note that rev C does not carry. After `DN-61092`, `DN-60955` and
  `DN-6935` this is settled: **a successful EDAM fetch is not evidence you have the current
  revision &mdash; read the header line.** And `DN-62114` is reachable by **no** constructed
  shape (five slug forms &times; both roots &times; `?download=false`, all the 8,047-byte
  fingerprint); it was taken from a mirror, mime-checked and **imprint-verified** against its
  own revision line and the manufacturer's address.

- **A mirror filename can carry a DOWNLOAD ID rather than the document number, so two mirrors of
  one document look like two documents.** `cortesielettronica.it/...2700120843.pdf` is Bosch
  document **2700030219** inside. Add it beside the recorded `DN-6857` case, where two slugs
  serve **413,140 and 412,612 bytes with different MD5s and the same revision `:C2`** &mdash;
  the `DN-6935` shape, not the `DN-61092` two-revision shape. **Check the header line, never the
  hash or the filename.**

- **`FHS` is listed with FPJ and RPJ-1 in `DN-60332:A1` (Canadian FT-300/ONYX sheet), while `DN-60779:C` (NFC-FFT) names only FHS-F (v2b51).** Honeywell's product page carries `&quot;sku&quot;: &quot;FHS,FHS-F&quot;` as one product naming NFC-FFT and ECC-FFT, so that claim is kept and attributed to Honeywell. The two sheets disagree on handset cabinet capacity (five against six), none published. `DN-60332` sits on EDAM as `hbt-fire-473kcn-brg-datasheet.pdf` &mdash; no document number in the slug, found only by search. `securityandfire.honeywell.com/notifier/...` 301s to the brand home page (a path-dropping redirect). The store sells FPJ under vendor Gamewell-FCI; flagged, not researched.
- **`DCOIL` refined (v2b51):** the D2 needs the coil **unconditionally** for RTS151/RTS151KEY remote test (`A05-0421-002`, `I56-0469`), while DNR/DNRW need it (plus auxiliary 24 VDC) only on housings dated **0012 or earlier** (`350085` Rev J, `DN-60429:C2`). DH400/DH500 take a different part, `COIL`.

- **`AA-100` is a Notifier amplifier filed under vendor &quot;Honeywell&quot; (v2b52).** `DN-3224:B` (8/8/07), fetched via `notifier-us/hon-ba-fire-dn-3224.pdf?download=false`, coordinator-verified: *&quot;the AA-30 (30 watts @ 25 Vrms), the AA-120 (120 watts @ 25 Vrms) and the AA-100 (100 watts @ 70.7 Vrms)&quot;*, dual outputs combined not over 100 W, with power supply, battery switch-over and backup tone generator &mdash; a complete amplifier. The live h2's &quot;707 VRMS&quot; is 70.7 with the decimal stripped (description only). **Document defect:** DN-3224:B's kilogram conversions are wrong (16 lb printed as 35.27 kg) &mdash; pounds only. Honeywell's product page tags it Gamewell-FCI and files it under discontinued-products while the badge is hidden &mdash; page-chrome lifecycle trap, nothing published. Vendor flagged for AA-100 and AA-120/AA-120E.

- **`BP-5` is a battery PLATE typed Batteries (v2b52).** DN-62113 revs C and E, identical wording (coordinator-verified): *&quot;BP-5: Battery plate. Used to cover battery and power supply when lower position is used in backbox&quot;*, required per cabinet mounting batteries/supply low; DN-62112:B marks it required for the N16 CPU chassis. Live title said &quot;Battery Dress Panel&quot; (dress panels are the DP- series) with a word-join &quot;Batteriespower&quot;. Also found: the store's `SEISKIT-CAB` title says CAB4 where DN-62113:E lists it under CAB-5 as CAB-4/5.

### e03 (23 Sep 2026): ISO-XA, the A suffix, and the micro-sign trap

- DN-2243:B Product Line Information: "NOTE: 'A' suffix indicates ULC Listed model … ISO-XA: Isolator Module. Canadian (ULC) version." The A marks a listing variant, not a generation. Per the listing-class rule it went into the title ("Canadian ULC Listed Version"). It was also flagged to the owner in case "regulatory approvals in titles" is read as covering ULC.
- The text layer reads **"450 A"** standby; a 300 dpi render shows **450 µA**. This is the symbol trap, settled by the render. The same text is served byte-different at `buildings.honeywell.com/content/dam/hbtbt/en/documents/downloads/hon-ba-iso-x-sa.pdf`. A 2005 edition on `techcommft.blob.core.windows.net` has different panel and CSFM lists; only rev B was used.

### e07 (23 Sep 2026): DR-AA4

- DN-6857:C2 (6/19/2012) p1: "DR-AA4: Door assembly, window, one tier (no battery compartment), BLACK, 9.8 lbs." **The live title omitted "with Window"**, which is what separates it from DR-AA4B (solid door). It is served at `datasheets/notifier-us/hon-ba-fire-dn-6857.pdf` and at `datasheets/hbt-fire-DN-6857.pdf`: same revision, different bytes. The DR-AA page's schema carries a `discontinued-products` tag and `data-discontinued-countries="id"` (Indonesia): page chrome, flagged low.
- t07 (23 Sep): the "A suffix = ULC Listed model" convention is confirmed again in DN-6934:B1 (FSI-851/FSI-851A) and DN-6886:C (FSL-751/FSL-751A). The live FSI-851 copy named "FSI851A", so the SKU was flagged to confirm the stocked unit is the UL version. DN-6934:B1 is served under both `notifier-us/` and the root (different bytes, same revision); DN-6886 is only under `notifier-us/`.
