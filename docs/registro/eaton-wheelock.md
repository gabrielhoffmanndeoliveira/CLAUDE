<!-- Registro de casos do projeto TFAS. Movido VERBATIM de CLAUDE.md em 23 Sep 2026; nada foi reescrito. Nao e carregado automaticamente: leia sob demanda. E cronologico: entradas posteriores corrigem anteriores; em caso de conflito vale a mais recente e o nucleo em CLAUDE.md. -->

# eaton-wheelock

- **Manufacturer ordering-syntax blocks beat every other decoder.** Page 5 of the
  Edwards catalogue sheets carries a Model Number Syntax block that decodes any
  G1/G4/GC part letter by letter; Eaton `TD450158EN` Table 3 does the same for Eluxa.
  Reading the syntax block is how `G1VRF` was settled, and it also showed that the
  coordinator's guessed siblings `G1RF` and `G1VF` **do not exist** in the current
  series &mdash; `G1RF...` numbers are the legacy xenon generation.
- **A manufacturer document can contradict itself; prefer the table over the prose.**
  Eaton TD450158EN's A/E Specifications paragraph lists the Eluxa ceiling candela set
  as "15, 20, 110, 150 and 177" &mdash; five values, with 30 and 75 mangled &mdash;
  while Table 4 and page 1 both give the correct six. Anyone quoting the prose
  paragraph publishes a wrong number.
- [CORRIGIDO — `urllib` voltou a funcionar; a falha é por conexão/rota; ver neste arquivo &quot;is alive again&quot;] **Eaton and Wheelock block `curl`, and the `urllib` workaround has now failed
  too.** Both HTTP/2 and HTTP/1.1 with browser headers fail against eaton.com
  (INTERNAL_ERROR or empty reply) and WebFetch gets 503. Python `urllib` through
  `HTTPS_PROXY` with a Safari user-agent worked on 21 Sep and **failed later the
  same day** on three Eluxa PDFs ("Remote end closed connection without response").
  Treat it as worth one attempt, not as the answer.
  **`www.alarmax.com/customer/docs/skudocs/` is the fallback to try first** &mdash; it
  served `TD450188EN` at its **July 2024** revision, so unlike the Anixter mirror it
  is current. `objects.eanixter.com` still works but **carries superseded revisions**:
  it had the 2016 MT4 datasheet describing xenon flashtubes where the current one
  specifies LED.
  **Eaton document numbers are close together and easy to swap:** `TD450158EN` is the
  Eluxa **high-fidelity speaker** sheet (the one whose A/E prose mangles the ceiling
  candela set), while `TD450188EN` is the Eluxa **outdoor horn/strobe** sheet &mdash;
  and in the latter the A/E prose and the table *agree*. The mangled-prose warning is
  about one document, not about Eaton generally.
- **Correction: the Eaton `urllib` workaround is alive again.** This file records it as
  having worked on 21 Sep and failed later the same day. On 22 Sep `curl` still failed
  with an empty reply on both HTTP versions, and **Python `urllib` through
  `HTTPS_PROXY` with a Safari user-agent pulled both Eaton PDFs first try.** So it is
  intermittent rather than dead: **still worth one attempt, and now worth it before
  falling back to alarmax.**
- **A cross-BRAND adjacent-row trap: a live page asserted a candela value its
  manufacturer does not make.** `ELSTWC-ALA` claimed **15/30/75/95/150/177 cd**. Eaton's
  ceiling set is 15/30/75/**110**/150/177, consistent in five places in `TD450157EN`.
  **95 cd is not an Eluxa setting at all, wall or ceiling &mdash; it is a System Sensor
  L-Series ceiling setting.** Every previous instance of this trap in this file is a row
  copied from a *sibling* or an *adjacent row in the same table*; this one crossed a
  vendor boundary, which no amount of reading Eaton documents would have caught. It was
  found by checking the one number that looked out of pattern.
  **A precision worth keeping about where such errors live.** Both this and the
  &quot;S3000&quot; on `4-24L24S` (**which turned out NOT to be bogus &mdash; see the
  resolution below**) sat in the description `<h2>`, **not** in the Shopify
  `title` field, which was clean in both cases. Titles are Merchant Center feed
  attributes and descriptions are not, so an error in the body costs one channel and an
  error in the title costs two. **Say which field a defect is in before sizing it** &mdash;
  the coordinator briefed both as title defects and both were not.
- **Amber lens is a listing class, not a colour option, and it is now proven on two
  brands.** Note 5 of Eaton ceiling installation sheet `P85756F`, word for word in the
  wall sheet `P85750D`: *&quot;Amber strobes are not to be used as a Visual Public Mode
  alarm notification appliance.&quot;* Last batch System Sensor documented its amber
  ALERT models as **private mode**, UL 1638 rather than UL 1971. Two manufacturers, same
  idea, so treat an amber lens as a class question every time.
  **Three things about how that one was handled are the reusable part.** (1) The note is
  item 5 of a **sheet-level `NOTES:` list**, not a footnote on a table row &mdash;
  confirmed by render &mdash; so it is a class statement; but the class it names is
  &quot;amber strobes&quot;, and `TD450157EN` Table 4 assigns **Strobe Color: Amber** to
  this part by name. That is what distinguishes it from the `SD365T-IV` series-block trap,
  where the family statement named no property that could be assigned to the member.
  (2) **The complement is not documented.** &quot;Private&quot; appears **zero times** in
  all three Eaton documents. The agent's first draft wrote *&quot;so this is private mode
  signalling&quot;* and, challenged, traced it to a **web-search snippet about the ELSA
  speaker-strobe line** &mdash; a different product family. Wrong document family for the
  eighth time, and the first caused by an agent inside its own copy. The published
  sentence now states the prohibition and adds that neither document says what amber may
  be used for instead. (3) **The sheet grants the amber model the same UL 1638/1971/ULC
  listing line as the clear one and then forbids the public-mode use**, which is odd and
  unresolved; the copy reports the listing as a family line and the prohibition as the
  part-level fact.
  **The general rule this sharpens: when a restriction is found, look for its complement
  before writing the sentence.** A prohibition without a permitted use is hard to phrase
  without inventing one.
- **The Eaton route's intermittency is PER CONNECTION, not per host per day, and the
  evidence is two processes disagreeing within the same hour.** On 22 Sep a v2b23 agent
  pulled `TD450157EN` **first try**, 519,514 bytes, mime-clean, from
  `www.eaton.com/content/dam/eaton/products/safety-security-emergency-communications/lsmns/eluxa/eaton-eluxa-horn-strobe-and-strobe-clear-and-amber-data-sheet-td450157en-us.pdf`
  &mdash; while the coordinator, using **that same URL** in the same hour, got
  `RemoteDisconnected` **50 times in a row** across two files, and `curl` failed to
  connect at all. Same host, same path, same proxy, opposite outcomes.
  **Two consequences.** First, this file's advice to &quot;keep hammering&quot; is right
  but has a limit: 25 attempts per file is enough to establish that *this* process is not
  getting through, and the next move is to have a different one fetch it, not to keep
  going. Second, **distinguish the failure modes before diagnosing** &mdash; the agent
  separately burned 25 attempts on clean **HTTP 404s** from a wrong slug, which is a
  *connected* failure and reads nothing like `RemoteDisconnected`. A 404 means find the
  slug; a disconnect means try another route or another process.
  Also recorded from that success: **the working slug puts the document number lowercase
  and at the end**, so it cannot be built from `TD450157EN`.
  **And one verification is still owed.** The `ELSTWC-ALA` copy published in v2b22 cites
  Note 5 of installation sheet `P85756F`. It rests on one agent reading it, quoting it
  verbatim, confirming its placement on a 170 dpi render, and re-checking the surrounding
  word counts when challenged &mdash; but **the coordinator has not read it directly**, and
  the attempt failed on the route above. The published sentence is deliberately weaker
  than the finding (it states the prohibition and that no document states the complement),
  so the exposure is small. **Re-check `P85756F` when the Eaton route next answers.**
- **Amber is encoded by POSITION on the Eluxa line, and that is why `-A` does not mean
  amber.** `ELHSR-A` is **AGENT lettering**, confirmed in `TD450157EN` Table 4 by word
  coordinates and a 200 dpi render. On this line amber is a **trailing** A *after* the
  lettering code: `-N` unlettered, `-NA` unlettered amber, `-AL` ALERT, `-ALA` ALERT
  amber. So `ELHSR-A` and `ELHSR-NA` are one character apart and are AGENT-clear against
  unlettered-amber. **A suffix letter means nothing without its position in the syntax.**
  **A new document defect on that sheet, and it is the conditional-headline rule a fourth
  time on this brand.** `TD450157EN` p2 Features prints *&quot;Sound pressure (Anechoic)
  dBA &mdash; Low 78, High 91&quot;*, **pairing a reverberant low with an anechoic high**:
  installation sheet `P85750D` Table 2A, model-attributed and coordinate-verified, gives
  **reverberant 80 H / 78 L per UL 464** and **anechoic 91 H / 86 L per ULC S525**. The
  anechoic low is 86, not 78. Anyone quoting the datasheet bullet publishes a wrong
  number. Also on that sheet, Table 3's second body is labelled **ELHNC**, a ceiling
  *horn*, while carrying ceiling *strobe* candela and currents &mdash; nothing published
  from it.
- **An agent reported a document defect as a &quot;typo&quot;, and it is really two
  separate facts.** `TD450157EN` Table 3's second body is labelled **ELHNC** while
  carrying ceiling *strobe* candela and currents. The agent called the label a typo for
  ELHSC, which is right about the datasheet &mdash; but **`ELHNC` is a real and distinct
  product**, and `P85756F` says so in its own General paragraph: *&quot;The Wheelock Eluxa
  **ELHNC horn**, ELSTC multi-candela strobe, and ELHSC horn/strobe appliances&hellip;&quot;*,
  with **ELHNC also for 12 V operation** and **ELHNC the only one of the three that may be
  wall or ceiling mounted**, and its own **Table 5: ELHNC Horn, Current Ratings**. So the
  datasheet mislabelled an ELHSC row; it did not invent a part. Two things that read as
  one, and worth separating before anyone concludes a catalogue number does not exist.
  **The dB pairing is now confirmed by the coordinator with word coordinates**, on
  `P85756F` Table 2: row (H) reads 80 | 80 | 85 | **91** and row (L) reads 78 | 78 | 79 |
  **86**, across the columns ELHNC@12V and ELHNC/ELHSC@24V for reverberant then anechoic.
  **Reverberant 80 H / 78 L per UL 464; anechoic 91 H / 86 L per ULC-S525.** The
  datasheet's Features bullet *&quot;Sound pressure (Anechoic) dBA &mdash; Low 78, High
  91&quot;* really does pair a reverberant low with an anechoic high.
  **And a supersession sat underneath it that would have poisoned the page.** `P85756E`
  (2022) gives the same model **0.037 / 0.046 / 0.077 / 0.109 / 0.146 / 0.208 A** DC where
  `P85756F` (2025) gives **0.035 / 0.042 / 0.069 / 0.096 / 0.124 / 0.177** &mdash; Eaton
  lowered every DC current in the newer revision. Reading the 2022 install sheet against
  the 2025 datasheet produces a two-document contradiction and the correct response of
  publishing nothing; **only the 2025 install sheet resolves it.** Pull the current
  revision of the *installation* sheet before concluding a datasheet contradicts itself.
- **Coloured lens is a listing class on a FOURTH brand, and Siemens treats amber the
  opposite way to Eaton.** Siemens Data Sheet 2625 states the blue, green and red lens
  strobes are *&quot;solely used for visual **Private Mode** alarm notification&quot;*,
  each with its own candela ladder (blue 15/30/75/95/135/150, green 15/30/60/75/115/125,
  red 10/20/40/50/75/80), while **amber is 15/30/75/95/150/177 and is &quot;certified as
  an Emergency Warning Visual Signal&quot;**. Eaton forbids amber as a public-mode fire
  appliance; Siemens certifies amber for emergency warning and puts blue, green and red
  in private mode. **Same underlying Wheelock hardware** &mdash; the Siemens installation
  sheet is `P85827-001A`, a Wheelock P-number. So after Eaton, System Sensor, Gentex and
  now Siemens: **a non-clear lens is a listing question on every brand, and the answer is
  not the same on every brand.**
  Eaton's own document pair shows it internally too: the coloured-lens ceiling sheet
  `P85756-002F` lists the strobe agency as **UL1638 and ULC526 only**, where the
  clear/amber `P85756F` lists **UL1638, UL1971 and ULC526**.
- **`EL4XBB-R`: the wall-versus-ceiling question was the wrong question, and the live title
  was right.** `TD450188EN` (July 2025) lists it as *&quot;NEMA 4X SURFACE BACKBOX,
  RED&quot;* with **no orientation in the row**, and the install sheets say all Eluxa 4X/3R
  models are listed for wall *or* ceiling. **The real distinction on this line is surface
  against flush** &mdash; `EL4XBB` gives Type 4X/IP66, `EL3RMP` gives Type 3R/IP54 &mdash;
  so **the accessory sets the NEMA rating, not the appliance.** Nothing like the
  `ELSPKBB-R` case. And the incomplete-product trap ran **backwards**: Eaton states the
  outdoor appliances *include* a mounting accessory from the factory, so a separately
  bought back box is a spare or a pre-wire box, not a missing piece.
- **A caption defect where BOTH HALVES OF ONE TABLE CARRY THE IDENTICAL CAPTION.** Eaton
  `TD450181EN` (April 2025) Table 3 prints as two side-by-side blocks under one caption
  reading *&quot;Wall / UL Reverberant dBA at 10 Feet &hellip; Ceiling&quot;* &mdash; and
  the left gives Horn 24V high **91 dBA** while the right gives **99**. Installation sheet
  `P85862C` settles it: **91 is reverberant per UL 464 and 99 is anechoic per ULC S525.**
  Anyone quoting the right-hand block publishes an anechoic figure labelled reverberant.
  **Table 2 on the same page does the same layout correctly**, captioning its halves VDC and
  FWR &mdash; so this is an omission, not a house convention, which is what makes it
  catchable. Fourth shape on the caption ladder, after caption-below-table, tables-emitted-
  swapped and header-contradicts-caption.
  Two more from that sheet: **Table 4's amber rows invert the C-means-ceiling convention**
  (`ELMTSWC-NA` listed Wall, `ELMTSW-NA` listed Ceiling) &mdash; recorded, not this part,
  nothing published; and **`ELSPKBB-R` is confirmed a wall/surface backbox for the third
  time**.
- **The Potter PE series is Wheelock-derived, which imports a whole set of known traps
  across a brand boundary.** Its wall installation sheet is **`P85750-005C`** against
  Eaton Eluxa's `P85750D`, the dBA figures match Eluxa's recorded 80/78 reverberant and
  91/86 anechoic, and **Note 5 is the same amber sentence** this file records from Eaton.
  `PE-HSW` is clear-lens and unaffected, but this catalogue carries `PE-HSW-NA` and
  `PE-STW-NA`, which are amber &mdash; **so the amber listing question applies to Potter
  too**, on a brand nobody had connected to it.
  **And the installation sheet again carried what the datasheet did not**: agency split,
  anechoic dBA, FWR currents, the 105-strobe NAC cap, the 35 &#937; line limit and the
  factory setting. Two document defects found in `8830229 REV D` and published around:
  its two current blocks are captioned *&quot;At Anechoic High/Low Continuous&quot;* when
  `P85750-005C` Table 4 shows they are **DC currents at the high/low horn setting across
  continuous, T3 and T3/T4** &mdash; the figures agree and the caption does not; and
  **`PE-STRC-N` is listed twice** (4871141 and 4871142) with the second row's X in the
  White column, so it is almost certainly `PE-STWC-N` mislabelled.
  A live title defect found beside it: **`PE-STWC` carried its brand and SKU twice**
  &mdash; *&quot;Potter PE-STWC Potter PE-STWC PE Series LED Strobe&hellip;&quot;* &mdash;
  in the Shopify `title` field, so it cost the feed as well as the page. Corrected.
- **Two more live title defects, both in the Shopify `title` field and both costing two
  channels.** `ELTP-SG-W-R-10PK` is titled *&quot;Eluxa Trim Plate **Ceiling** &hellip;
  **White** (Pack of 10)&quot;* and the manufacturer's own photograph shows a **red**
  plate; its sibling `ELTP-4S-W-W-10PK` (&quot;**Wall Single Gang** &hellip; White&quot;)
  photographs as white, **so the trailing letter is the colour code, proven by the pair**
  &mdash; and the two titles also appear to have swapped their form factors, since `SG` is
  single gang and `4S` is 4-inch square. And `ELSTW-N`'s title carries
  **`153075110135185`**, the candela ladder 15/30/75/110/135/185 with its separators
  stripped &mdash; the punctuation-loss import again, one product at a time, after the 185
  frequency ranges, `ZR-MC-R`, `QAA-5415-70/25` and `FDX-008WKI`.

- **An ERP string would have imported another part's material.** `MX16RSF-US`'s ERP reads
  *&quot;TYPE B CALL STATION **SS** FLUSH MOUNT&quot;*. Eaton's ordering table says
  **Silver**, and `MX16-SSC` is separately *&quot;Stainless steel flush mount panel
  front&quot;* &mdash; so reading `SS` as stainless would have taken a different
  catalogue number's material onto this page. **An ERP description is a source of
  candidate words, never of facts**, which is the third time this file has had to say it
  (after the lossy `type` field and the `live_desc` placeholder).
- **On the Eluxa line the trailing `C` IS the ceiling marker, and this must not be read
  as contradicting the `ELSPKBB-R` finding.** `ELSPSTWC` was settled three ways &mdash;
  `TD450158EN` Table 3 by render, Table 4 prose, and installation sheet `P85968A` whose
  own heading is CEILING MOUNT. The `ELSPKBB-R` case is about **back boxes**, where the
  ceiling marker sits in the sibling's number (`LSPKBB-CR`) and `-R` is a colour; on the
  **appliances** the `C` after the mounting letter is ceiling. **Same brand, two different
  naming schemes, and which one applies depends on whether the part is an appliance or an
  accessory.** Also recorded: the Eaton **ceiling** install-sheet slug carries a
  **literal space** (`installation%20instructions-p85968a-...`) where the **wall** sheet
  uses a hyphen in the same position &mdash; find the slug, do not build it, for the sixth
  or seventh time.
- **A document that contradicts itself on a candela set, where the agent had a strong
  inference and PUBLISHED NOTHING &mdash; which is the right call and worth recording as
  such.** Eaton `TD450087EN` has **no row at all** for `ASB-24MCW-NW` (its own footnote
  says the model list &quot;is not all inclusive&quot;), and elsewhere disagrees with
  itself: page 1 gives the coloured-lens multi-candela set as **15/30/75/95** while Table 7
  splits by suffix &mdash; **all eight `MCC` rows at 15/30/75/95 and five of six `MCW` rows
  at 15/30/75/110** &mdash; re-checked row by row with word coordinates, so there is **no
  row shift and the document really is inconsistent**.
  The tiebreaker favours the table and is arithmetic: page 1's amber figure
  **11/22/56/82 is exactly 15/30/75/110 derated 25%**, i.e. the derate footnote applied to
  the *wall* set. So the live title's `15/30/75/95` looks like the MCC/MCW adjacent-row
  trap &mdash; **but that is a pattern inference, and candela in a title is a Merchant
  Center attribute**, so the figure was removed and **nothing asserted in its place**.
  Flagged; a carton or a price list settles it.
  **The bigger find on that sheet: Eaton lists the whole coloured-lens line to UL 1638
  general signaling, tests UL 1971 light distribution for AMBER ONLY, and derates blue by
  about 70%.** That is lens colour as a listing class on a fifth brand line, after Eaton
  Eluxa, System Sensor, Gentex and Siemens &mdash; and a blue unit here is a general
  signaling appliance, not a fire one. **A candela switch setting is not the delivered
  output on a coloured lens.**
  Also contradicting the briefing in the useful direction: **&quot;Blue&quot; and
  &quot;White&quot; in the live title are not in conflict** &mdash; Eaton has separate Lens
  Color and Base Color columns.
- **A datasheet's own Description and Features assert a strobe the ordering table denies.** Eaton
  `TD450198EN` (Oct 2025) says the MT4 series has an *&quot;integrated 15 candela LED strobe&quot;*
  and carries UL 1638 / ULC S526 visual listings &mdash; while **Table 3 gives `MT4-115-R` a Strobe
  Candela of `n/a`, no lens and no lettering**, coordinate- and render-confirmed. Only the two
  `-WH-V` members have strobes. That is the `ELFHNW-N` shape on a brand that states it in prose
  rather than by omission.
  **And the conditional-headline rule fired as briefed:** the A&amp;E paragraph's *&quot;99 dBA
  minimum&quot;* is **anechoic on one tone at one setting** &mdash; every distributor headlines it
  &mdash; where Table 2's **reverberant** rating per UL 464 for the same tone is **89 dBA HIGH /
  86 STANDARD**, with Bell at STANDARD the quietest at 74. Published with conditions; 99 excluded.
  Separately, **the `115` in the SKU is a series designator and not a voltage** (the table gives
  120 VAC by model), so the live title's &quot;120VAC&quot; was right &mdash; the `AS-75-R-WP`
  shape, benign this time.
- **THE `SS` SUFFIX IS TWO TOKENS, AND THIS FILE'S OWN NOTE WAS HALF THE ANSWER.** This file
  records that `MX16RSF-US`'s ERP string reads `SS` where Eaton's ordering table says
  **Silver**, and warns against reading it as stainless. That is right and incomplete.
  `TD450190EN` p4, model-attributed: `MX16RSS-US` &mdash; **Call Station USA Silver Surface**
  against `MX16RSF-US` **Silver Flush**, `MX16RRS-US` **Red Surface** and `MX16RRF-US`
  **Red Flush**. **The grammar is `MX16R` + Silver/Red + Flush/Surface**, so the `SS` in this
  SKU is *Silver + Surface*, **two independent tokens that happen to be the same letter**, and
  `MX16-SSC` remains a separate stainless-steel panel front. **A suffix decode recorded from
  one member of a family is not the family's grammar** &mdash; read enough rows to see which
  letters vary independently.
- **Eaton `mdmfiles` URLs already carry a size segment, and appending another silently serves the
  WRONG SIZE rather than failing.** The path shape is
  `eaton.com/mdmfiles/<contentId>/<ASSET>/<size>` with sizes `500x500_72dpi` through
  `2000x2000_72dpi`. Appending a new size to a path **already ending** `/1000x1000_300dpi` returned
  a file &mdash; at the old size. **Strip the trailing size segment before appending one.** A
  request that succeeds and returns something other than what you asked for is the same failure
  class as the redirect that discards the path and the search endpoint that ignores the query: the
  test is whether the response is what you asked for, not whether it is a 200.
- **28 of 36 rows in one harvest were products ALREADY DELIVERED, and the delivery-wide MD5 pass is
  what found it &mdash; by a marker, not by a hash.** A mixed-brand slice was built before the
  delivered-handle exclusion existed in the slice builder, so the agent re-researched 25 Eaton and 3
  System Sensor products whose CSVs had already shipped. The duplicate surfaced because the prior
  delivery's hash file carries **`md5: 'ERR'` for the 25 Eaton rows that failed to download** during
  an earlier pass, and grouping by md5 put all 25 in one bucket that intersected the new lot.
  **That is a false-positive collision doing real work**, and it is worth saying plainly: a sentinel
  value in a hash column will group everything that carries it, so a collision report must be read
  for *why* the group formed. Here the wrong reason found the right defect.
  **The rows were not simply dropped as duplicates &mdash; they were compared.** The new URLs are
  the same Eaton assets at **2000&times;2000** where the delivered ones are **1600&times;1600**: a
  genuine upgrade, and still dropped, because re-importing a handle whose placeholder MERGE has
  already run adds a second image rather than replacing the first. **A better version of a delivered
  row is a separate decision from a new row**, and it is the owner's.
  The lot shipped as **7 rows**, and the slice builder's delivered-handle check is the guard that
  should have run on its input.
- **Edwards prints reverberant and anechoic dBA IDENTICAL at all four taps, which is the
  opposite of two brands this file records.** On the G4S line UL 1480 reverberant and
  CAN/ULC-S541 anechoic are both **78/81/84/87**, coordinate- and render-confirmed with the
  25V/70V cell vertically merged. Eaton's Eluxa splits 80/78 reverberant against 91/86
  anechoic, and System Sensor splits by 2&ndash;3 dBA. **Do not assume a gap on this brand, and
  do not assume its absence elsewhere** &mdash; it is a per-brand measurement, not a physical
  law.
- **The Eaton bare-host lever FAILED to reproduce, and the negative is worth the line.** This
  file records `https://eaton.com` without the `www.` as a cheap lever after ~100 consecutive
  failures against `www.eaton.com`. Re-validating the 25 delivered Eaton photo URLs, **both
  hosts returned `RemoteDisconnected` on every attempt**, tried in that order per row. So the
  lever is not a fix &mdash; it is one more draw against the recorded per-connection
  intermittency, and this process lost every draw. The 25 rows stand as delivered and
  **unverified from here**, which the owner has been told; the recorded remedy is a different
  process, and that is now bounded by the owner's three-agent cap rather than by the host.


- **`8CD` in an Eaton Wheelock title is a COUNT, not a value (v2b52, 23 Sep 2026).** `HSR-N`'s live title read *&quot;12/24V, 8CD&quot;*. TD450049EN (Nov 2016, the Exceder data sheet, coordinator-verified) says *&quot;All strobe models feature an industry first of 8 candela settings on a single appliance&quot;*; the wall set is 15/15-75/30/75/95/110/135/185. So `HSR-N` is **Exceder**, not the legacy HS4 line. Install sheet `P85060E`: *&quot;Strobe devices for 12V are only approved by UL to be set at 15cd, and 15-75cd, and only to be powered by DC not FWR&quot;* &mdash; the live &quot;12/24V&quot; was true and incomplete. The Model Legend marks lettering codes *&quot;(strobes only)&quot;*: N none, A AGENT, AL ALERT; plain HSR = FIRE. `HSR-A` carries the same `8CD` token (flagged). There is **no Eaton SKU page for HSR-N**: its 404 matches a bogus SKU while HSR and HSR-A return 200 &mdash; a bounded negative. **The skuPage 404 size drifts (100,109 / 101,276 / 103,018 B) with identical &quot;Page Not Found&quot; content &mdash; compare content, not size.** Eaton's own HSR SKU page headline prints dB values (90/95/99) as &quot;cd&quot;. `urllib` + Safari UA pulled TD450049EN, P85060E and the CSFM PDF first try on both `www.` and the bare host.

- **PS-8-LP (audit t01):** install sheet P84905-002B matrix (coordinator-verified) `PS-8-LP 8A 120VAC RED`, `PS-8-B-LP` black, `PS-8E-LP` 240VAC. **&quot;-LP&quot; is carried by every family member and decoded nowhere**; &quot;low profile cabinet&quot; is a TD450003EN feature line, so it went in the title as a feature, not a decode. TD450003EN Table 1 prints PS-8E-LP as 220V against P84905's 240VAC; UL 864 9th Ed. (2017 sheet) vs 10th (install sheet). urllib+Safari fetched `skuPage.PS-8-LP.html` (180,536 B) from both hosts; the page lists every document under `.../lsmns/wheelock/wheelock-ps-8/`.
