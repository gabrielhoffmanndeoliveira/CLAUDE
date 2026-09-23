<!-- Registro de casos do projeto TFAS. Movido VERBATIM de CLAUDE.md em 23 Sep 2026; nada foi reescrito. Nao e carregado automaticamente: leia sob demanda. E cronologico: entradas posteriores corrigem anteriores; em caso de conflito vale a mais recente e o nucleo em CLAUDE.md. -->

# simplex-autocall-ansul

- **The JCI hub carries Ansul too, under `specialhazards` &mdash; and the segment is
  the business unit, not the brand.** `https://docs.johnsoncontrols.com/specialhazards/api/khub/documents?search=<term>`
  returns a **1,449-document index** in the same shape as the Simplex hub
  (`id`/`filename`/`title`/`metadata`, `ft:locale`, `ft:lastEdition`, non-English
  duplicates), and `search` is ignored there too, so grep the JSON. Download via
  `/specialhazards/api/khub/documents/<id>/content`. The segments `ansul`,
  `ansul-us`, `tycofs`, `chemguard`, `tyco`, `fire`, `johnsoncontrols`, `jci` and
  `ansulfire` **all 404**. So **when a JCI brand seems missing, guess the business
  unit, not the brand name** &mdash; Chemguard, Skum, Pyro-Chem and Williams should
  sit here too. This unlocks Ansul, 27 products and 14,768 impressions of the v2
  queue, and settled a part in two fetches that would otherwise have gone to
  resellers.
- **Simplex documents: use the Johnson Controls document hub.** A GET on
  `https://docs.johnsoncontrols.com/simplex/api/khub/documents?search=<term>`
  returns a JSON index of ~961 Simplex documents with `title` and
  `documentApiEndpoint`. `search` and `limit` are effectively ignored, so it
  returns the whole index &mdash; grep the JSON rather than trusting ranking.
  Download with `https://docs.johnsoncontrols.com/simplex/api/khub/documents/<id>/content`
  (note the `/simplex/` segment; the bare `/api/` path 404s). This reaches
  current datasheets that are not otherwise linkable, and it settled the 4081
  end-of-line range in one call after four other documents had left a gap.
- **The merged-cell trap.** A vertically merged table cell emits its text at a
  position in the stream that implies the **wrong** grouping, and `find_tables()`
  can fail on the same table without erroring. On Simplex `S4906-0001` plain
  extraction put six SKUs under Ceiling and two under Wall in an order that invited
  exactly the wrong assignment. **Only `page.get_text("words")` with y-coordinates
  settles a merged cell.** Re-check any mounting, candela or variant column read out
  of a selection table by plain text.
- **The JCI hub has an `autocall` segment too.**
  `https://docs.johnsoncontrols.com/autocall/api/khub/documents/<id>/content` serves
  Autocall documents directly, alongside the known `/simplex/` and `/specialhazards/`
  segments &mdash; more confirmation that the segment is the business unit. Autocall
  part numbers are Simplex numbers with an `A` prefix. Meanwhile
  **`autocall.com/uploads/resources/Datasheets/*.pdf` is blocked and returns 103 bytes
  of `text/plain`** for every request &mdash; a new failure fingerprint alongside EDAM's
  8,047-byte JavaScript and steelfire's 48,687 bytes.
- **On the JCI hub, grep the `filename` field, not the title.** The document that
  settled `4906-9101` is titled "Visible Notification Appliances with Synchronized
  Flash" &mdash; containing neither "4906" nor "TrueAlert". Its filename,
  `S4906-0001.pdf`, is the reliable key.
- **Two current parts in parallel document lines look exactly like a supersession
  pair from outside.** `4099-9005` carried "(Replaces 4099-9002)". `4099-9002` is a
  real, current Simplex part &mdash; listed in `S14099-0001` Rev 7 (02/2021) &mdash;
  and `4099-9005` sits in `S4099-0005` Rev 4, **the same revision month**. Two
  concurrent document lines (one IDNet-only/ULC-oriented, one IDNet-or-MAPNET II),
  neither stating a replacement in either direction. So "the other part still exists
  and is documented" does **not** disprove a supersession claim, and it does not
  support one either; only a manufacturer statement settles it.
- **Word coordinates are necessary but were not sufficient, for the first time.** On
  Simplex `S49AVC-0001` Table 1, plain text put `579-1242` after &quot;Blue&quot; and
  word coordinates put it at y=250.6 next to &quot;Clear&quot; &mdash; but neither
  settled the *merged* Installation-Instructions cell. A 200 dpi render did
  (`579-1242` spans rows 1&ndash;6, `579-1279` the last two). So the escalation is three
  steps, not two: plain text, then `get_text(&quot;words&quot;)` with coordinates, then
  **render and read**. Also from that sheet: **`-BA` on a Simplex appliance code means
  &quot;assembled in the USA&quot;**, not a functional variant.
- **The appliance-only trap: a part that is merchandised as a finished product but
  ships as bare electronics.** Autocall `A49CMT-APPLW` was titled &quot;Conventional
  Mount Appliance&quot;, which contains no class noun at all and names a mounting style
  that does not exist. `AC49CMT-0001` Rev. 7 heads Table 2 *&quot;Separate mounting
  plate, **required** when ordering model A49CMT-APPLW&quot;* and Table 3 the same for
  covers; the finished horns `49CMT-WRF` and `49CMT-WWF` *&quot;include cover and
  matching mounting plate&quot;*. So the buyer receives a horn with no cover, no plate
  and no lettering. This is the `4099-9015` shape one step worse, and it is the second
  time in three batches. **Check the ordering table for the word &quot;required&quot;
  before assuming a catalogue number is a complete product.**
  **A trap avoided inside it:** the trailing `W` does **not** mean white. Word
  coordinates show that row's Cover-colour and Wording cells are **empty**, with
  &quot;Select cover and mounting plate separately&quot; spanning both, while the rows
  above do carry Red and White. Colour is set by the cover ordered separately, so
  titling it white would assert what the manufacturer deliberately leaves open.
- **A part can be merchandised as its general family when it is the special case, and
  that is worse than a wrong class noun.** Simplex `4099-9015` was titled *&quot;Double
  Action Addressable Manual Pull Station&quot;* &mdash; not false, but it is documented
  in its own datasheet, `S4099-0006`, as a station **for releasing applications**, and
  it **ships with a blank front panel**: the buyer must separately order label kit
  `4099-9802` to mark it clean agent, CO&#8322;, foam, sprinkler or manual release.
  Someone shopping for an ordinary Simplex double-action station received an unmarked
  agent-release station and a part number they did not know to order. Corrected.
  **The agent found it only by continuing past three negative results** &mdash; the part
  is in none of `S4099-0005`, `S14099-0001` or `S4099-0008`, the three obvious
  manual-station datasheets. **Wrong document family, for the third time.**
- **On the JCI hub an accessory may appear in NO index entry at all.** `2975-9206` is in
  no filename and no title across the 961-entry Simplex index; grepping `2975` returns
  one unrelated Canadian bells-and-chimes sheet from 11/00 that does not contain the part.
  It was found by grepping the **downloaded text of the parent annunciator data sheets**.
  **So the rule &quot;grep the `filename` field, not the title&quot; has a boundary: it
  works for documents, and an accessory is usually not a document.** For an accessory,
  identify the parent product and grep its PDF text. Two smaller notes from the same work:
  the index `metadata` is a **list of `{key,label,values}` dicts, not a dict**, so
  `.get()` on it raises; and filtering `ft:locale` to `en-US` collapsed one family's hits
  from 11 to 7.
- **Two more index and path facts.** The JCI Simplex hub has a **`product_code` metadata
  field**, and grepping `filename` alone missed `4100-5451` entirely &mdash; the four
  documents carrying it expose it only there, so grep `filename`, `prodname` **and**
  `product_code`. And on EDAM, **prefix and case are independent axes**:
  `BA-Fire-AVDS-62173-A.pdf` works while `ba-fire-DN-60240.pdf` 404s and
  **`hon-ba-fire-dn-60240.pdf`** serves the PDF. Try the `hon-ba-fire-` prefix lowercased.
- **A Simplex title lost a slash in the same import that truncated the others, and only
  the title.** `4100-5113` read `220240V` while its own description `<h2>` still read
  `220/240V`. **The defect was in the Shopify title field alone**, which is the Merchant
  Center attribute, so it cost the feed channel and not the page. Same shape as
  `3-ZA40A`, whose 150-character title ends mid-sentence at *&quot;Has Built in
  Class&quot;* while the description carries the full text. **When a defect appears in one
  field and not the other, say which** &mdash; it decides whether it costs one channel or
  two.
- **A ULC suffix can shift every figure in a table, which is the sibling trap across
  listings rather than across parts.** Simplex `S4902-0003` Rev 11: `4902-9716` is
  **80/83/85/88 dBA at 25 VRMS** and **79/82/85/88 at 70.7 VRMS**, while `4902-9716CA`,
  the **ULC** variant, is **77/80/83/86** &mdash; two to three dBA lower at every tap.
  **`CA` is the only suffix on this series; `-BA` appears nowhere in it**, so the
  assembled-in-the-USA reading recorded from `S49AVC-0001` does not transfer here.
  Two further points from the same table. **The merged-cell trap fired as briefed and
  needed the render**: the Model cell holding `4902-9716` and `4902-9717` is merged
  across two Input-voltage rows, so y-coordinates alone assign 25 VRMS to one and 70.7 to
  the other &mdash; wrong, both are dual-voltage and carry both rows, confirmed at
  300 dpi. And **the two voltage rows are not identical**: 25 V is 1 dBA louder at the
  two lower taps and converges at 1 W and 2 W, so **quoting one set of four figures
  quotes one voltage only.**
  Also a document defect published from: Table 3's general-signalling frequency response
  reads **&quot;125 kHz to 12 kHz&quot;**, not a coherent range. Nothing quoted from it.
- **Eighteenth product-class error, and it is a fire extinguisher sold as the wrong
  AGENT.** Ansul `429022` was titled *&quot;FE13 Cleanguard 13 lb **ABC** Fire
  Extinguisher&quot;*. It is a **clean agent** extinguisher &mdash; Ansul's own class noun
  in `F-96111-17` is *Clean Agent Hand Portable Extinguishers*, the agent is **HFC-236fa**,
  and the UL rating is **2-A:10-B:C**. So the rating genuinely covers A, B and C, which is
  presumably how &quot;ABC&quot; got written &mdash; but **&quot;ABC&quot; in the trade
  means ABC dry chemical**, the corrosive-residue agent that is the exact opposite of what
  a clean-agent buyer is paying $1,750 to avoid. A data room or a switchgear cabinet
  specified for clean agent and given dry chemical is a real mis-sale in both directions.
  **The `type` field said Fire Extinguishers, agreed with the wrong title, and raised
  nothing &mdash; the signature for the sixth time.** Airgas repeats the same
  &quot;ABC&quot; wording, which is correlated distributor copy and not a second source.
  Two more from that sheet. **`FE13` is Ansul's own model designation**, not a mangled
  &quot;FE-36&quot;: the part-number row runs FE02VB / FE05S / FE09 / **FE13** against
  429107 / 442255 / 429021 / **429022**. And **&quot;DuPont FE-36&quot; is not Ansul's
  wording at all** &mdash; `FE-36`, `FE36`, `DuPont` and `Chemours` appear **zero times**
  in both revisions, which Ansul writes as HFC-236fa throughout.
  **The incomplete-product trap fired on the bracket, and only a render found it.** The
  bracket row reads `24610 (Included) | 429146 | 422737 | 30937`, and word coordinates
  plus a 250 dpi render put the **`(Included)` marker in the FE02VB column alone**. The
  FE13's bracket `30937` carries no included marker in either revision, while the live
  copy asserted *&quot;with bracket&quot;*. Claim removed, flagged to the owner &mdash;
  if TFAS assembles the bracket itself that is a stock fact and belongs in the copy said
  that way.
- **Three more first-party hosts, and a new failure fingerprint.**
  `honeywellanalytics.com/~/media/honeywell-analytics/products/<line>/documents/` serves
  Honeywell gas and flame PDFs directly with no bot protection &mdash; the FSL100 needed
  no EDAM probing at all. `docs.johnsoncontrols.com/specialhazards` reaches **Ansul hand
  portable extinguishers** cleanly (`F-96111` is the CLEANGUARD family sheet). And
  `altronix.com/library/pdf/data_sheets/DS_<MODEL>.pdf` is **fully derivable inside the
  library**, so pulling five siblings to find a separator costs five fetches &mdash; its
  404 is a stable **13,828-byte `text/html`**, confirmed against a control.
  Also: `macurco.com` links a first-party `docs.macurco.com`, a bubble.io app whose
  `/file/<id>` route returns a **~15,548-byte `text/html` JS shell**, while the underlying
  `*.cdn.bubble.io/<fileid>/<name>.pdf` serves real PDFs on **searched** paths.
- **The briefing carried the wrong AGENT across a sibling boundary, and the bracket answer
  inverted with it.** `443475` was briefed from `429022`'s chemistry: it is **FK-5-1-12**,
  not HFC-236fa. **HFC-236fa is the legacy CLEANGUARD FE line** (FE02VB/FE05S/FE09/FE13)
  and **CLEANGUARD+ CA03/CA07/CA13/CA25 is a different chemistry in a different document**
  (`F-2022057-06` against `F-96111-17`). Publishing the sibling's agent on a $252
  extinguisher would have been the exact error the `429022` &quot;ABC&quot; defect already
  is, one layer in.
  **And the bracket is INCLUDED here, which explains the sibling case rather than
  contradicting it.** Submittal `F-2004117` Rev. 07 footnote reads **&quot;VB: Includes
  Vehicle Bracket&quot;**, and word coordinates put `24610` and `Included` both inside the
  CA03VB column. So on `429022` the `(Included)` marker sat in the smallest model's column
  **because that model is the VB one** &mdash; same rule, opposite outcome, and the suffix
  was the thing nobody had decoded.
- **Twenty-first product-class case, and it is the private-mode shape rather than a wrong
  noun: an MRI-room extinguisher sold as an ordinary one.** `443479` ($1,033) was titled a
  CLEANGUARD+ clean agent extinguisher, which is true. Ansul's own document is titled
  *&quot;Clean Agent **MR Conditional** Portable Extinguisher&quot;* (`F-2022058-01`): a
  **stainless steel shell with MR Conditional valve, hose and nozzle, tested to 7.0 tesla**,
  which Ansul says *&quot;can be mounted within the MRI room&quot;*. That is what explains
  the price against the ordinary CA13, and it is the `SPSWLED-ALERT` shape &mdash; a
  materially different purchase behind a correct class noun. **Manufacturer-stated, so it
  went into the title** rather than only the body.
  **The briefing pointed at the wrong document family again and the agent caught it:**
  `F-96111-17` is the **older HFC-236fa** CLEANGUARD sheet, where `FK-5-1-12` appears **zero
  times** and `CA14` appears **zero times**. Ninth instance.
- **The borrowed-copy signature threw its second false positive, on the same shape as the
  first.** `4098-9788`'s live body was briefed as self-contradictory (two-wire-with-remote-
  LED against heat detectors needing `4098-9684`). It is neither contradictory nor borrowed:
  `S4098-0043 Rev. 2` states **all three scopes in one entry** &mdash; smoke detectors get
  the remote-LED connections, **heat detectors and QuickConnect2 get a plain two-wire base
  with no options** &mdash; and the live sentence is near-verbatim Simplex `574-709 Rev. AP`
  §3.3. **One part, three scopes by head type.** After `4100-9706` this is the second time
  what read as a sibling's text was the manufacturer's own text about the right part; the
  discriminator remains *whose row it is*, which only the ordering table answers.
  A method note from it worth more than the part: `S4098-0014-10` says *&quot;2-Wire Base,
  no options&quot;* and `S4098-0017-4` says *&quot;with connections for Remote Alarm
  LED&quot;* &mdash; **two Simplex sheets three months apart that appear to contradict**,
  and only a third, the 2023 dust-boot sheet, reconciles them. Reading either alone gives a
  false negative or a false positive.
- **A brand word in a store title that the manufacturer has never written.**
  A Simplex page carried &quot;Digitalflex&quot;. The manufacturer's name for that
  line is **Flex-50**; &quot;Digitalflex&quot; appears in no Simplex document. This is
  a different failure from a wrong class noun &mdash; the noun was right and the
  *proper name* was invented &mdash; and it is invisible to every scan this project
  runs, because a made-up brand word has no shape and no sibling to disagree with. The
  only thing that catches it is an agent reading the live title against the ordering
  block.
- **`53080`'s ABC claim checked out, which completes a three-case set on extinguishing
  agents.** `F-7547-09` (2024) states FORAY is **monoammonium phosphate based**, covers
  Class A, B and C, and is **yellow to distinguish it from the other ANSUL agents**;
  FORAY is Ansul's own registered mark, not distributor wording. So: `429022` had
  &quot;ABC&quot; on a **clean agent** and was wrong; `PRO5` had it on monoammonium
  phosphate and was right; `53080` likewise. **The trap here is the siblings** &mdash;
  `415788` (Industrial FORAY) and `434906` (Modified Industrial FORAY) are **also 45 lb
  yellow pails**, so weight and colour together do not identify the standard agent.
- **Three more JCI hub segments, and the business-unit rule firing again.**
  **`fireclass`, `zettler` and `tycofire`** all serve (5.1, 16.5 and 7.5 MB indexes);
  `firedetection`, `minerva`, `emea`, `jcifire`, `fire`, `firealarm` and `tycoemea` all
  404 at **236 bytes**, and a bogus document id returns **404, 190 bytes,
  `application/json`**. **And the guess mattered: `517.050.023` is in `zettler`, not
  `fireclass`** &mdash; the FireClass index of 1,176 documents contains the string zero
  times, though 81 other dotted codes from the same block are in it. The part is the
  **5BEx intrinsically safe detector base**, an Ex/hazardous-area part, which is a
  materially different purchase from an ordinary base.
- **Nineteenth product-class error, and the mechanism is an ABSENT LISTING rather than an
  absent word.** `49VO-WWF` was titled a **Horn Strobe** and typed **Horn Strobes**, the
  type agreeing with the wrong title and raising nothing &mdash; ninth instance of that
  signature. Simplex `S49VO-0001` Rev. 7 classes the series as **V/O, visible only**, and
  lists it to **UL 1971 and ULC S526 only, with no UL 464 anywhere in the document.**
  **That absence is the proof**: UL 464 is the audible-appliance standard, so a device
  listed without it has no horn, and that is stronger than noting the word
  &quot;horn&quot; is missing. Where an audible device is wanted the wall horn strobe is
  the separate 49AV series.
  **Exception carried rather than flattened:** the candela ladder is 15/30/75/110/135/185
  on **IDNAC** circuits but **only 15/30/75/110 on legacy TrueAlert addressable SLCs**,
  at 17 VDC minimum. Both are in the copy.
- **Two more wrong-document-family instances, and one of them carried a CORRECT warning
  attached to the wrong number.** `4906-9153` is **not** in `S4906-0001` &mdash; that is
  the strobe-only sheet &mdash; but in **`S4906-0003`**, the speaker-and-strobe one.
  **The merged-cell warning that travelled with the wrong document number was right
  anyway and paid twice**: Table 1 merges Listings, Description and Housing dimensions
  across `4906-9151` and `4906-9153` with no row rule, and Table 9 names `4906-9153` by
  model in the **anechoic ULC-S541** row (77/80/83/86 dBA) while the **UL 1480
  reverberant** row (76/79/82/85) is labelled only *&quot;UL listed models&quot;*, with
  the ceiling model two rows below at 81.6&ndash;90.2. **A warning can be transferable
  even when the routing attached to it is not.**
  Second instance: the `125 kHz to 12 kHz` frequency-response defect this file records in
  Simplex `S4902-0003` **reproduces verbatim in `S4906-0003`**. Two documents makes it a
  **house template defect**, not a typo &mdash; and the rule that reproduction across
  documents rules out extraction error and rules in a document defect holds. Nothing
  published from it.
- **Three contradictions inside ONE Simplex datasheet, and publishing nothing from any of them was
  the whole job.** `S49SVW-0001` Rev. 16, 06/2024 &mdash; fetched and read by the coordinator directly
  because the batch's title rested on it. **Table 13 is headed &quot;Weatherproof wall mount
  addressable speaker S/V appliances, NEMA 3R&quot; and lists `49SV-APPLW-O` with &quot;S/V appliance
  only. Select cover, mounting plate and surface or WP back box separately&quot;**, which settles both
  halves of the title: `-O` is the outdoor marker (not a colour or lettering code) and the part is the
  appliance alone. Table 14 independently marks covers *&quot;required when ordering APPLW-O
  models&quot;*. Fourth Simplex `APPL` incomplete-product instance.
  The three defects, none published from: (a) **Table 8 and Table 19 both claim to cover S/V models
  and disagree at every tap** &mdash; 79/83/86/89 dBA reverberant against 78/81/84/87 at 25 V and
  76/80/84/87 at 70.7 V &mdash; so **no dBA figure was published at all**; (b) **Table 12's
  &quot;outdoor private mode&quot; row prints CANDELA under a milliamp heading** (69/240/300/445 are
  exactly the typical candela of WP15/WP75/WP110/WP185 in Table 21, where Table 22 gives the real
  maximum RMS currents as 81/187/230/298 mA) &mdash; the Table 22 currents were published and Table
  12's row was not; (c) Tables 5 and 6 give `7 3/8 in. x 5 in. x 1 3/4 in. or 139 mm x 128 mm x
  42 mm`, and 7 3/8 in. is 187 mm, not 139 &mdash; **no dimension published**. A document that
  contradicts itself three ways on one part is now ordinary rather than remarkable; budget for it.

- **A recommended sweep run, and it closed as a NEGATIVE &mdash; which is the useful outcome,
  because it stops a mass edit.** An agent removed *&quot;Logo Only&quot;* from `4901-9820` as
  contradicted by its datasheet and recommended checking other Simplex appliance titles for the
  phrase, since it looked import-derived. **It is not.** Of **nine** live titles containing
  &quot;logo&quot;, seven are plainly legitimate (VESDA blank plates *with* and *without* the VESDA
  logo, Hochiki glass elements with the Hochiki logo, a Rath acrylic piece) &mdash; and the two
  Simplex covers are **manufacturer-stated**: the coordinator fetched `S49VO-0001` Rev. 7 (3/2018)
  and `S49VOC-0001` Rev. 17 (01/2026) and both print **&quot;Simplex logo only&quot;** as a cover
  option, with `49VOC-WWS` and `49VOC-CWS` against it. Only `49VO-WRSO` is unresolved &mdash; it
  appears zero times in either sheet and its suffix has a different shape &mdash; and it was left
  untouched.
  **So the `4901-9820` defect is a single page, not an import class.** Worth recording precisely
  because the opposite conclusion was the plausible one: this file's own history is full of defects
  that *did* cluster in one import (the 80 non-ASCII titles, the ~300&ndash;400 truncations, the 75
  duplicated brand tokens), and the reflex after finding one is to assume a family. **A
  recommendation to sweep is a hypothesis; run it before believing it, and record the negative so
  nobody runs it again.**
- **`742-351` and `742-590` are adjacent rows in one service parts list, and a distributor
  collapsed them.** `579-1006 Rev. A` page 14, coordinate-verified: `742-351` Power Distribution
  Interface, `742-394` Master Controller PC Assembly, `742-590` 2X40 Master Operator Interface.
  A search result describes `742-351` as a *&quot;4100 Master Controller upgrade board for ES 2X40
  systems&quot;* &mdash; **three rows of that table welded into one sentence.** The store title was
  right all along. Note also `742-396` is the Power Distribution **MODULE**, a different item from
  the **INTERFACE**, and that **the JCI hub carries data sheets, not service parts lists**, so a
  `742-` number appearing zero times in its 961-record index is a bounded negative about the index.
- **Three model-attributed signals against one series-wide row, and the series-wide row lost.**
  Simplex `S4906-0010 Rev. 7` gives `4906-9131` a candela ladder of **15/60/75 cd** in page-1
  prose, in Table 1 (its own model-attributed row) and in Table 8 (whose middle current column
  is *headed* &quot;60 cd&quot;) &mdash; and **15/30/75 cd** in Table 6, the generic
  Specifications block. Both render-confirmed. 60 was published because the dissenter is the
  unattributed family row, which is the `SD365T-IV` rule applied to a ladder rather than a
  temperature. **Flagged to the owner anyway**, because candela in a title is a feed attribute
  and the manufacturer's own general table disagrees.
- **Plain text, word coordinates and the render each gave a DIFFERENT answer, and only the
  render was right. Second instance, and this one would have split a part's harnesses.** In
  Simplex `579-1006`'s Operator Interfaces table, plain text reads the `742-590` row as a flat
  list; **word coordinates put `734-033` in the 742-590 row and `734-026` in the 742-740 row**,
  which would have given the US and Canadian-French assemblies different harnesses; a **250 dpi
  render** shows the cell holding **both** numbers is vertically merged across all three rows.
  Both harnesses belong to this part. The three-step ladder earning its third step outright,
  after the Potter `8900097` case.
- **Two bare service-part numbers, two `null`-shaped answers, and the second one is the
  stronger.** `565-831` is a 4098 Series duct PCB assembly whose **housing Simplex never names
  in any document read**; what the copy could do was give the buyer the discriminator &mdash;
  **Simplex splits Duct SENSOR (`4098-9755`/`-9756`, addressable on MAPNET II or IDNet) from
  Duct DETECTOR (`4098-9685`/`-9688`, conventional two-wire IDC)**, so the label on the housing
  decides the board. `650-440` went further: **the live title &quot;CPU Board LCD&quot; was left
  exactly as it was and the body says plainly that no Simplex publication names the number.**
  The prefix proves nothing &mdash; in the 4017ES list `650-2702` is a frame assembly and
  `650-1192` a wire-entry cover, while board assemblies carry `566-` numbers, and in the 4100ES
  list `650-450` is a box hinge. Every source calling it a CPU board is a distributor.
  **Not called invented, not corrected, and the page now tells the buyer to read the panel's
  service parts list** &mdash; which is the `THM04R3000` rule applied to a title rather than a
  part number: removing a live claim is itself a claim.
- **The coordinator's scepticism was the error for the FIFTH time, and this one had a plausible
  adjacent row to blame.** The `4100-9600` briefing flagged the live body's &quot;2,500 ft&quot;
  as a probable adjacent-row import, because `S4100-1035` p5 carries an IDNet SLC row reading
  exactly `2500 ft (762 m); 35 ohms`. **It is not an import**: three documents state it of the
  RUI link in prose, and the live page's four-item component list is **verbatim Simplex**
  &mdash; *&quot;includes a bay assembly, a power distribution interface module (PDI), a Basic
  Transponder Interface Module, and an interconnect harness&quot;*, with &quot;bay assembly&quot;
  and &quot;interconnect harness&quot; being Simplex's own words in the current Rev. 7. **And
  &quot;Basic Transponder&quot; is Simplex's own term**, not a hiding word, so there was no
  product-class error and the `type` of Transponders is right.
  **The incomplete-product instinct paid anyway, which is the pattern this file has now recorded
  four times.** The current sheet states that **NEMA 1/IP30 boxes and solid doors are ordered
  separately** and that a Power Distribution Module (`4100-0634` at 120 VAC, `4100-0635` at
  220/230/240 VAC) is *&quot;one required per box&quot;*. The buyer receives bay equipment with
  no box, no door and no PDM. Also found and published: `4100-1291` RUI Module is listed
  *&quot;for use with 4100-9600 only&quot;*, an explicit host-side compatibility statement.
  Two live body defects on that same page, both **description-only** so one channel not two:
  *&quot;the status of each **wireless** device&quot;* &mdash; `wireless` occurs **zero times**
  in all three transponder sheets and MINIPLEX devices are wired IDNet/IDNAC/IDC &mdash; and a
  malformed `<ul>` whose first `<li>` is the lead-in *&quot;The transponder can:&quot;*.

- **Twenty-fourth product-class error, and the type field named a COMPONENT of a complete
  $4,159 panel.** `4010-9521` was typed **Loop Modules** and its title was the raw ERP string
  *&quot;4010ES 2 Idnet 2 BAY Red 240V&quot;* &mdash; no class noun at all. Simplex's own Table
  14 files it under **Control Units**, and its Basic control unit description lists Main System
  Supply 2, operator interface, master controller with Compact Flash, an 8 A supply, four 3 A
  NACs, an aux relay, an RUI port and **cabinet and door**, with *&quot;Box and door or retainer
  assemblies are included with basic control unit assemblies&quot;*. A buyer filtering for
  control panels never sees it and one filtering for loop modules gets a two-bay panel. That is
  the `CPU2-3030D` / `4100-9701` signature for the fourth time. Defect field: **Shopify
  `title`**, so two channels.
  **Three sub-findings on that one part, each a recorded trap firing.** (a) **&quot;2 IDNet&quot;
  is neither a loop count nor a 250-point channel, and both readings offered in the briefing
  were half right**: Table 4 gives it *&quot;one two-loop isolated IDNet2 Communications Channel
  and one four-loop Isolated IDNet 2+2 Communications Channel Module &hellip; up to **500**
  addressable IDNet points&quot;* &mdash; two channels, six loops, 250 points each. Page 1's
  *&quot;up to 1000&quot;* is the series figure. (b) **The live title's bare &quot;240V&quot;
  understates a range**: Simplex writes **&quot;English 220 VAC to 240 VAC&quot;**. (c) **The
  invisible-dimension trap, with a number that invites exactly the wrong read** &mdash; Figure
  12 is vector linework with no text layer, and at 200 dpi the prominent **16 in. (406 mm)** is
  the **mounting-hole spacing**, its leaders pointing at two hole circles labelled *&quot;Use 4
  holes to Secure box to wall&quot;*. The box is **24 in.** wide. Publishing 16 in. as the width
  was the obvious error and only the render prevents it.

- **Three documents in one batch splitting a headline figure by STANDARD, which the headline hides.**
  Simplex `S4098-0053` Rev. 6 page 1 summarises the 520 Hz sounder as **85 dBA** unqualified;
  its Table 8, coordinate-verified, gives **79.5 dBA per UL 464** at x=259.8 and **85.5 dBA per
  UL 268 and CSA 6.19-01** at x=382.2. Both published with their conditions. That is the
  conditional-headline rule for the fifth or sixth time, and note the shape here is neither the
  reverberant/anechoic split (Eaton) nor a settings-dependent value (E2S) &mdash; **it is one
  device measured under two standards, and the page-1 number is neither of them exactly.**

- **`4903-9148` is in `S4903-0016-5` (5/2014, index filename `4903-0016.pdf`), zero times in `4903-0015` (v2b51).** Found through the JCI index `prodname`/`product_code`. Its candela cells hold **glyph-less vector check marks**: the only reading is x-position against the column edges (120.4 / 163.9 / 207.4 / 250.9), render-confirmed at 250 dpi &mdash; 30 cd. &quot;TrueAlert&quot; appears in the index `prodname` and zero times in the served sheet. **The borrowed-dimension warning recorded for `S4903-0019-5` did not apply here**: 7-1/4 &times; 5 in. is this wall appliance's genuine housing row. A warning is about a document, not a series.

- **2975-9463/-9464 are semi-flush box adapters, not annunciators (audit t02).** S4606-0003 Rev. 3 7/2026 Table 1 (coordinator-verified): `2975-9463 Red / 2975-9464 Platinum Semi-flush mount metal box adapter for Remote Color Touchscreen LCD annunciators`, 1-3/4 in. deep; 4606-9205 is the platinum annunciator itself &mdash; the live title carried the annunciator's number on the adapter. Found via the index `product_code` field. The handle still contains 4606-9205 (flagged, low).

- **Correction to the t02 2975-9464 title, by the coordinator (audit t03):** S4606-0003's description cell is merged across 2975-9463 (red) and -9464 (platinum) and names no annunciator model, so pairing platinum with 4606-9205 was a colour inference. Both titles now say &quot;for 4606 Series&quot; &mdash; a weakening, not a new claim.

- **650-2493 bounded negative and a citation correction (enrichment e01):** 650-2493 occurs in none of the 961 JCI index records, 258 downloaded Simplex PDFs or the 4017ES/Foundation/4100ES service parts lists (controls 650-2702, 650-450 found; 650-9999 not); only resellers repeat the ERP &quot;Main System Slave II with IDNET2&quot;. **Description not published** (a page about an absence does nothing for Shopping). The mirror file named `733-621.pdf` is really **4100ES Service Parts List 579-1006 Rev. A (2011)**; the JCI hub does carry two service parts lists (`S4017ESSPL`, `S2XXXFSSPL`).

- **4190-9010 is multimode, pairs with media modules, and the current sheet dropped it (enrichment e02).** In no JCI index field; S4100-0056 Rev 11 (all locales) contains it zero times (controls ok) and also drops media modules 4100-6057/4010-9819/4190-6037. Documented only in Rev 4 (2/2013) via an imprint-verified mirror (cdn.thefirepanel.com; coordinator-verified: *&quot;62.5/125 or 50/125 Multi-mode, graded index single fiber optic cable, requires Bi-Directional coupler&quot;*). 850 nm, ST, two couplers per link. Lifecycle flagged. Briefing premise (&quot;pairs with a modem&quot;) wrong.

### e03 (23 Sep 2026): 4100-9211, an earlier-generation 4100ES controller, not 4100/4100U

- The briefing guessed an older 4100 or 4100U part; that was wrong. **4100-9211 is the 4100ES master controller assembly with LCD and operator interface, 220–240 VAC**, from the SPS power-supply generation. Source: S4100-0031 Rev. 42 (11/2019), Table 6, render-checked because a merged description cell spans 4100-9111/9112/9113/9211. S4100-0031 carries a "Discontinued document" watermark on every page. The current S4100-1031 Rev. 22 (06/2026) lists only ES-PS controllers (4100-9701 …). No replacement statement was found in either direction, so lifecycle was flagged to the owner and taken out of the title and body.
- The box and door/retainer are ordered separately (S4100-0031 p3): an incomplete-product warning in the body.
- On the JCI hub (961 simplex records), S4100-0031 was a text hit and S4100-1031 a metadata-only hit. This is the "metadata hit ≠ text hit" rule again.

### e04 (23 Sep 2026): 4090-5250, 566-1424, A4901-9859

- **4090-5250 is an MX loop device** (ESMX), not MAPNET II or IDNet. Sources: `S4090-0016-1` (3/2015) and `S4100-0059` Rev. 11 (02/2023), Table 6. It needs an MX Loop Module in the 4100ES/4010ES. The programming tool differs by imprint: Simplex says 850EMT, Autocall `AC4090-0016` (2020) says 801AP. That is a revision disagreement, so the tool was left out of the copy. The D800 IP55 housing 557.201.401 is a separate model.
- **566-1424 is a 4017ES IDNAC power supply board**, not a 4100ES or 4010ES part. It appears only in the **text** of `S4017ESSPL` Rev. 1 (09/2025), page 4, Figure 3, and in no index field, not even `product_code`. This is the reverse of "metadata hit ≠ text hit": a text hit with no metadata hit. So for service parts, grep the text of the hub's service-parts lists; the index can miss them. It is absent from `S2XXXFSSPL`. The 4100ES list (579-1006) is not on the hub. The board's rating is attributed to the panel sheet `S4017-WIDNAC` Rev. 6.
- **A4901-9859** is settled by `AC4901-0013` Rev. 3 (2/2020), Table 1, checked on a render (Autocall hub). `4905-0003` puts mini-horns under "SmartSync operation only": not a general-purpose 24 V horn. Price gap (not flagged): the Simplex 4901-9859 sells at $42.75 against $20.95 for the Autocall version.

### e05 (23 Sep 2026): 2081-9271 battery

- `S2081-0006` Rev. 27 12/2024 (JCI hub `u0LZH15cA0euIY9_6z5EQw`; Rev. 24 = `XsmfBNc3vldJ~sgeziy8gw`) is the authority for 2081-92xx. It gives model-attributed 20-hour capacity, dimensions, weight and a cabinet-fit table (Table 1). There are **two 33 Ah Simplex parts**: rectangular 2081-9271 ("typically for service"), which is external on 4100/4120, and square 2081-9276 ("use for new"). The live "780 L x 520 D x 622 H" matched no Simplex figure and was removed, not converted.
