<!-- Registro de casos do projeto TFAS. Movido VERBATIM de CLAUDE.md em 23 Sep 2026; nada foi reescrito. Nao e carregado automaticamente: leia sob demanda. E cronologico: entradas posteriores corrigem anteriores; em caso de conflito vale a mais recente e o nucleo em CLAUDE.md. -->

# edwards-kidde

- [CORRIGIDO — Edwards é first-party (LifeLines + myeddie /PublicMedia/); ver neste arquivo &quot;SUPERSEDED 22 Sep 2026&quot;] **Mirror paths must be *found*, not *built* &mdash; including `qdigital.mx`.**
  Calling it "the one path-predictable mirror" was too strong: it worked on paths
  discovered by search and **failed on a constructed one**
  (`/content/Edwards/TSD-CJ/...` returned HTML). Two more hosts that answer with a
  readable HTML shell rather than a 404: `edwards-signals.com/files/<anything>.pdf`,
  and `steelfire.com/UserFiles/Docs/<guess>.pdf`, which returns **identically
  48,687 bytes for every guessed filename** &mdash; a stable fingerprint like EDAM's
  8,047-byte `application/javascript`. Mirrors that served verbatim Edwards PDFs on
  21 Sep: `cdn.lsicloud.net/kendall/Resources/AD/`,
  `externalassets.unilogcorp.com/ASSETS/DOCUMENTS/ITEMS/EN/`,
  `savemoreonfirealarmparts.com`, and `steelfire.com` for a *searched* filename.
  Also note `85001-0584` is the **Intelligent** (Signature/SIGA-SD) SuperDuct sheet and
  is what a search for "SuperDuct datasheet" lands on first; the **four-wire** family
  is documented by bulletin `3100685` and installation sheets `3100686` (sensor) and
  `3100687` (controller).
- **SUPERSEDED 22 Sep 2026: Edwards IS first-party, and the LifeLines library is
  found.** This file said for four days that &quot;Edwards documents are not on
  edwardsfiresafety.com&quot; and that PDFs had to come from verbatim mirrors. That is
  wrong, and it was wrong because nobody had looked for the library the file itself
  flagged as worth finding. An agent found it; the coordinator verified all three
  claims directly, because it overturned a recorded rule.
  **Route 1: `https://www.edwardsfiresafety.com/lifelines/<category>`** &mdash; e.g.
  `/lifelines/speakers-strobes-horns-bells-and-chimes`. Plain HTML, HTTP 200, no bot
  protection, ~108 KB, and it embeds direct links to roughly 35 catalogue sheets per
  category. **Route 2: those PDFs live on
  `https://myeddie.edwardsfiresafety.com/PublicMedia/Catalog%20Sheets/`** with the slug
  form `E85001-NNNN -- <Descriptive Title>.pdf`, mime-clean `application/pdf`.
  **The old `myeddie` shell fingerprint was right about the wrong path, and the
  distinction is the whole finding.** A control with a bogus filename returns:
  **`/PublicMedia/Catalog Sheets/` &rarr; a clean HTTP 404 at 1,245 bytes**, while
  **`/Media/Catalog Sheets/` &rarr; HTTP 200 with an 8,909-byte shell.** So `/Media/`
  is the poisoned path and `/PublicMedia/` is the real library. **The mirrors &mdash;
  lsicloud, unilogcorp, steelfire, qdigital, savemoreonfirealarmparts &mdash; are no
  longer needed for Edwards catalogue sheets.** This unblocks the SIGA parts still in
  the queue. `est.net` and `edwardsfiresafety.com/files/import/` remain shells.
  **Kidde has the same library and it is machine-readable**: `kidde-esfire.com`'s own
  JavaScript discloses `POST /LiteratureLibrary/GetCategoryNavigation` with
  `categoryName=<name>`, returning JSON with every PDF URL for that category. Its JS
  namespace is literally `EdwardsPublic` &mdash; one codebase, two brands, which is the
  thread that led to the Edwards library in the first place.
  **The lesson is about this file, not about Edwards. A recorded negative decays.**
  &quot;Not on their site&quot; was true when tested and stayed in force as fact long
  after; the note even carried its own to-do and nobody ran it. **Re-test a
  host-level negative before building a batch around the workaround.**
- [CORRIGIDO — `kidde-esfire.com/Content/Documents/` dá 404 de 1.245 B; as fichas Kidde vêm do myeddie via API de literatura; ver neste arquivo &quot;Route correction&quot;] **Kidde serves its own PDFs and needs no Edwards mirror.**
  `kidde-esfire.com/Content/Documents/` responds directly with no bot protection.
  And the E/K prefix swap is the same line: **`K85001-1021` (Kidde, Issue 1, 2019) and
  `E85001-1021` (Edwards, Issue 1.1, 2020) agree exactly** &mdash; candela set,
  20 &#937; sync limit, 6.8 &times; 1.82 in., every current value. Kidde EGCAVWF is
  Edwards GCAVWF. This extends the `85001-0581` &rarr; `E85001-0640` rule: a prefix
  change on a shared document number is branding, not a different product.
- **The Omega trap:** `Ω` often extracts as the letter `W`. An extracted "50W" in
  a resistance spec is almost always 50 Ω. **Five hits.** The fifth: an Edwards
  wiring diagram rendering a NAC end-of-line as `EOL 15 KW`, settled as **15 kΩ** by
  the technical reference manual. The fourth was Edwards
  literature printing an ordering table as `4.7KW, 3.6KW and 1.1KW` where the
  manufacturer's own technical reference prints the same parts with real &#937;
  symbols.
  **The inverse case is real and more dangerous: a legitimate `W` that looks like the
  trap.** Protectowire prints `Resistance 2W Models: .185 ohms/ft`, where **`2W`
  means two-wire**, as opposed to the three-conductor TRI-Wire line directly below
  it &mdash; not 2 watts and not 2 &#937;. An agent applying the Omega rule
  mechanically would have "corrected" a correct value. Read the surrounding rows
  before substituting; the rule is a prompt to check, not a find-and-replace.
- **Check `file -b --mime-type` before trusting any extraction.** A 404 that returns
  an HTML shop page still opens in pymupdf and "extracts" pages of navigation chrome
  that read like content. `alldataresource.com` does this, and so does
  `myeddie.edwardsfiresafety.com`, which answers **HTTP 200 with an HTML shell** for
  any filename.
- **Two title defects the scan surfaced that no keyword search would have, both
  queued for agent research rather than acted on.** First: **`4-NET-SM` is titled
  &quot;Dual Line Dialer&quot; inside a family that is uniformly SFP network
  controllers** &mdash; `4-NET-CAT` copper, `4-NET-MM` multimode, `4-NET-SMD`/`-SMU`
  single-mode single-fiber, `4-NET-SMH` single-mode dual-fiber. **`SM` means
  single-mode everywhere else in the family**, a dialer is a DACT, and the part is
  $1,522. That is the adjacent-row trap, and **fiber mode is one of the three
  highest-risk title fields in this catalogue**, so it needs the Edwards EST4 ordering
  table and not a pattern. Note the type field was **no help at all** &mdash;
  `4-NET-SM` and `4-NET-CAT` are both the generic &quot;Fire Alarms&quot;, agreeing
  with the wrong title; **the entire signal came from the siblings.** Second:
  **`ZH-MC-W`'s complete title is &quot;Siemens ZH-MC-W (Replaced by SLHSWW-F)&quot;**
  &mdash; a part number and a parenthetical, with **no class noun and no descriptive
  name at all**, whose one substantive claim is an unsourced supersession sitting in a
  Merchant Center feed attribute, on the brand where exactly that claim has already
  been wrong twice. Its family also splits on class and on price ($272.15 against
  $101.40 for three siblings). Both are in `pending_fixes.md`.
- **Tenth coordinator premise wrong: `WG4RF-HVMHC` is not a residential Kidde number.**
  The briefing warned it &quot;looks like a residential/consumer Kidde number&quot; and
  told the agent to establish the UL standard first. It is an **85001-series commercial
  Genesis WG4 outdoor horn strobe**, and the suffix reads straight off the ordering
  table: **H horn, VM visual multi-candela, HC high candela.** The warning was still
  worth giving &mdash; it forced the check &mdash; but the guess inside it was wrong.
  **And the E/K prefix-swap rule is confirmed for a third time:** Kidde `K85001-0628`
  Issue 1.1 (2020) and Edwards `85001-0628` Issue 2.2 (2013) agree **exactly** on every
  candela, current, dB, dimension and temperature figure, seven years apart.
- **Eleventh product-class error, and the giveaway was a new one.** `3-SDC1` was titled
  *&quot;Signature Driver Controller Module&quot;*. Edwards heads its Ordering
  Information **&quot;3-SDC1: Signature Device Card &ndash; upgrades a 3-SSDC1 to a
  3-SDDC1&quot;**, and lists the controllers separately: *&quot;3-SSDC1: Single
  Signature Driver Controller. **Comes with one 3-SDC1 Device Card**&quot;* and
  *&quot;3-SDDC1: Dual … **Comes with two 3-SDC1s**&quot;*. A buyer ordering a loop
  controller received a plug-in card that does nothing without a controller already in
  the cabinet. That is the `4099-9015` / `A49CMT-APPLW` incomplete-product shape, but
  **the tell here is not the word &quot;required&quot;** &mdash; it is **the sibling
  rows stating what they come with**. Add that to the checklist: when a catalogue
  number appears inside another product's &quot;comes with&quot; clause, it is a
  component, not the product. The `type` field said Modules and agreed with the wrong
  title, so it raised nothing again.
- **The E/K prefix rule reaches down into part numbers, not just document numbers.**
  Same document number, different brand: `K85001-0667` is titled *&quot;Genesis LED
  **EG1** Series&quot;* and `E85001-0667` *&quot;Genesis LED **G1** Series&quot;*, with
  every spec matching (16&ndash;33 VDC/VFWR, 15/30/75 cd, 20 &#937; sync,
  3 &times; 4-5/8 &times; 1-1/8 in., &minus;0.71 in. box offset, 32&ndash;122 &deg;F).
  Trim rings follow it too: `EG1TR`/`EG1TW` against `G1TR`/`G1TW`. **So a Kidde
  catalogue number on this line is the Edwards number with an `E` prefix** &mdash;
  search both forms, and reach for Kidde's first-party host rather than an Edwards
  mirror. An MD5 check also proved verbatim mirroring the cheap way again: `K85001-0640`
  came back byte-identical from two unrelated mirrors.
- **A corroborating diagram can argue for the wrong reading, and only the render
  settles it.** On `E85001-0640` p6 plain text gives *&quot;Base height from box:
  0.8 in. | 1.4 in.&quot;* across three model columns. Word coordinates put both at
  cell-centre, and a 200 dpi render shows **0.8 in. spans the AB4G *and* AB4GT columns
  while 1.4 in. is AB4G-LF alone.** The page-3 exploded diagram groups
  &quot;SIGA-AB4GT(-LF)&quot; together, **which argues the other way** &mdash; so the
  one piece of apparent corroboration was the trap. Same merged structure on the
  Listings and Resonant-frequency rows. **When a merged cell and a diagram disagree,
  the render of the table wins.**
- **A document defect can persist across revisions and across brands, which tells you
  it is the source and not your extraction.** `E85001-0640` and its Kidde twin
  `K85001-0640` both print the CAN/ULC-S525 row with **low dBA louder than high**
  (Temporal 24 VDC: 95 low, 91 high) &mdash; the same inversion, 2.5 years apart, under
  two brands. Nothing published from that row. Likewise all three SWIFT AV base
  datasheets print &quot;RF Operating Voltage Range 3.3 VDC&quot; and, two rows later,
  &quot;RF Operating Voltage 12 VDC&quot;. **Reproducing across revisions rules out
  extraction error and rules in a real document defect &mdash; which is a reason to
  publish nothing, not a reason to pick one.**
- **The SIGA-HRS supersession claim is settled, and what settled it was a
  consequence, not a citation.** Two agents in different batches searched independently
  &mdash; `E85001-0647` in **both** its revisions (Issue 2.1, 2018 and Issue 2.2, 2020)
  and the legacy `85001-0243` Issue 6 &mdash; for HRS, HFS, replac, supersed,
  discontinu and legacy, in both directions, and found nothing; every claim traces to
  resellers. That alone was only a bounded negative and the title was left alone for a
  batch. What decided it: **the two generations carry different UL listed spacing,
  70 ft for HFS/HRS against 50 ft for HFD/HRD.** A successor with *shorter* listed
  spacing is not a drop-in &mdash; a layout drawn on 70 ft needs more devices when
  re-equipped &mdash; so an unqualified &quot;Replaced by&quot; in a feed title was not
  merely unsourced but misleading in a way that costs the buyer. Claim moved to the
  body with the spacing difference stated. **Generalises: when a supersession claim
  cannot be sourced, look for a spec that would have to be equal if it were true.**
- **Two agents described the same E/K fact and one of them explained it wrongly; the
  sharper version wins.** Agent 2 reported *&quot;the Kidde catalogue number is the
  Edwards number with an `E` prefix&quot;* from `K85001-0667` (&quot;EG1 Series&quot;)
  against `E85001-0667` (&quot;G1 Series&quot;). Agent 1, reading each document's own
  syntax block, found the mechanism: **Edwards' series code is `GC` and Kidde's is
  `EGC`** &mdash; the `E` is *inside the series code*, not a prefix bolted onto a part
  number. Descriptively the two agree; mechanistically only one is right, and the wrong
  framing would mispredict any part whose series letters differ some other way.
  **Also found: a real product difference under one document number** &mdash; Kidde
  lists the GP10 wiring plate as *&quot;required, included with device&quot;* and
  Edwards as *&quot;required, ordered separately&quot;*, and Kidde's sheet drops the
  FEU/FUEGO and ALERT variants Edwards carries. **So the prefix-swap rule means the
  same hardware, not necessarily the same carton.**
- **The Kidde literature API's category names are enumerable, which removes its one silent
  failure.** A wrong `categoryName` returns the top-level nav in `Markup` with `Content`
  **empty** rather than an error, so a bare category looks identical to a typo. The fix:
  any request returns that nav, and `re.findall(r'>([^<>]+)</a>', Markup)` yields the 20
  real names. Note SuperDuct sits under &quot;Intelligent Initiating Devices&quot; and
  &quot;Conventional Initiating Devices&quot; &mdash; **not** under any name containing
  &quot;Duct&quot;. Also: `myeddie.edwardsfiresafety.com/**PrivateMedia**/Catalog Sheets/`
  serves real PDFs too, so `/PublicMedia/` is not the only live path and only `/Media/` is
  poisoned.
- **A live page can be right and the catalogue still wrong, when a suffix is unsourceable.**
  `SIGA-OSD-IN` carried *&quot;Note: Manufactured in India&quot;* in its body. The `-IN`
  suffix appears in **none** of five Edwards documents &mdash; `E85001-1001` Issue 1.5
  (which lists `SIGA-OSD` and `SIGA-OSD-NL` only), installation sheet `3102595-EN`,
  `E85001-1002`, `E85001-1004` or the Signature Factbook `E85000-0371` &mdash; and
  &quot;India&quot; appears zero times in all five. **The suffix was not called invented
  and the SKU was not touched**, which is the `THM04R3000` lesson holding; the country
  claim was removed because it is unsourced and is not a spec; and the page now says
  plainly that no Edwards document read defines `-IN`. One reseller says it means a
  built-in isolator, which is correlated distributor consensus and was neither repeated
  nor contradicted. **Flagged to the owner, because an unsourceable suffix is still a
  Merchant Center title attribute.**
- **The E/K carton split is confirmed on a second document number, so it is a rule and
  not a one-off.** `E85001-1021` Issue 1.2 marks the GP10 wiring plate *&quot;required,
  ordered separately&quot;* while `K85001-1021` Issue 1 marks it *&quot;required, INCLUDED
  WITH DEVICE&quot;* &mdash; same two places in the document, same hardware on every
  figure (candela set, 20 &#937; sync, 6.8 &times; 1.82 in., UL files S218/S5389).
  Identical to the `85001-0667` finding on a different number. **A prefix swap means the
  same hardware and not necessarily the same carton**, and Edwards again carries `-FR`
  and `-SP` variants Kidde drops.
  Route note worth keeping: **Kidde uses the Edwards slug form**, so the Kidde URL builds
  from the Edwards LifeLines filename with the `E` swapped for `K` &mdash;
  `kidde-esfire.com/Content/Documents/K85001-1021%20--%20Genesis%20LED%20GC%20Series...pdf`
  resolves where the bare `K85001-1021.pdf` 404s at 1,245 bytes.
- **RESOLVED 22 Sep 2026: `S3000` is a ULC file number, and this file's own &quot;bogus
  S3000&quot; note was wrong.** The coordinator fetched Edwards `E85010-0130` from
  `myeddie.../PublicMedia/Catalog Sheets/` (866,133 bytes, mime-clean) and read page 1
  directly: **`S3000` occurs twice, in the Approvals block, printed under the ULC mark**
  &mdash; once under the EST4 column and once under EST3, beside CE, FM and EN54. A
  v2b27 agent had reported the same thing from `E85010-0057` and the coordinator could not
  retrieve that document at the time; a second agent found it on a second sheet and it now
  has two independent readings plus a direct one.
  **Nothing live ever depended on it** &mdash; the `4-24L24S` page was rewritten wholesale
  &mdash; but the episode is the cleanest instance in this file of its own rule being
  broken by the person who wrote it: *never conclude a part number is invented from a
  negative search result.* &quot;Bogus&quot; was the coordinator's word for a string it had
  not looked up, it survived in this file for a day and a half, and it was overturned by an
  agent both times it was tested. **A recorded negative that was never positively checked
  is a claim, and it decays the same way a host fingerprint does.**
- **A recorded negative decayed again, and this time inside a single day.** This file states
  that `myeddie.edwardsfiresafety.com/Media/` is the poisoned path returning HTTP 200 with
  an 8,909-byte shell. **It now 302-redirects instead**, while `/PublicMedia/` gives a clean
  1,245-byte 404. The fingerprint was real when measured and is already stale. Re-measure a
  host fingerprint before building a filter on it, exactly as the Edwards first-party
  finding required re-testing &quot;not on their site&quot;.
- **Two tables on ONE datasheet using DIFFERENT column orders. New shape, and it would have
  published wrong currents.** Kidde `K85005-0129` Issue 1.3: the **Features by model**
  table leads with `K-RLCD-2` while the **Specifications** table leads with `K-RLCD-C-2`.
  Reading the current draw off the features order gives **61/90 mA** where the correct
  figures are **62 mA standby and 91 mA alarm**. Both tables had to be rendered (280 and
  260 dpi) because plain text returns bare tick glyphs. Add it to the caption ladder
  alongside caption-below-table, tables-emitted-swapped and header-contradicts-caption:
  **column order is not a property of the document, it is a property of each table.**
  The `-C-` is settled as **common controls** (Reset, Signal Silence and Drill added to the
  Ack/Silence and Lamp Test every model has); **the trailing `-2` is not decoded in any
  document read** and was recorded as a bounded negative rather than guessed.
- **A `myeddie` PublicMedia path CAN be constructed, which narrows the rule rather than
  breaking it.** `E85010-0130 -- Signature Driver Controller Modules.pdf` resolved at
  866 KB, mime-clean, built by hand. The difference from every failed construction is that
  **the document number AND its title came from a search first**; the slug is then
  buildable from those two. So: *find the number and title, then build the slug* &mdash;
  never build from a document number alone. Related: the Edwards `/lifelines/control-panel`
  category carries **zero** catalogue sheets (only four policy PDFs), while
  `control-panels-and-accessories`, `signature-series` and `fire-alarm-control-panels` all
  **404 at 17,844 bytes**; recover the 20 real slugs with
  `grep -o 'lifelines/[a-z0-9-]*'` on `edwardsfiresafety.com/lifelines`.
- **The `DN-62046` inverted proof fired again, on one ordering block.** `E85001-0279`
  Issue 1.1 marks the `276-K1` reset key *&quot;Supplied with all Key Reset Stations&quot;*
  and marks the **general alarm key `276-K2` (USA) / `32997` (Canada)** with nothing. Same
  page, same author, same date: a manufacturer that states what is supplied when it means
  to, declining to state it for the adjacent part. **A buyer of a two-stage presignal
  station gets no GA key**, which is the key the second stage needs.
  Also settled on that part, and left open by the briefing: `SIGA-270P` is **single action,
  two stage (presignal)** &mdash; not double action &mdash; and it **uses two module
  addresses** where `SIGA-270` and `SIGA-278` each use one. It also needs a **different
  back box** from its siblings: a 1-1/2 in. deep 4 in. square with a 1-gang raised cover,
  not the 2-1/2 in. deep 1-gang box.
- **`S3000` confirmed a third time, independently, on a third document.** The Kidde FX data
  sheet prints **`Agency Listings: UL864 (S3000), ULC-S527, CSFM, FDNY`** in its panel
  specification table, render-confirmed. Three agents, three documents, one answer: it is a
  UL file number. The note calling it &quot;bogus&quot; is disproved, not merely unresolved.
- **A category nobody had anticipated: 16 products for which no photograph can exist in
  principle.** FireWorks `FW-*` seats and servers, `4-CUSWL`, `TRNG-F-EST4-CERTIF` and five
  Universal items are **software licences and a training certification**. With 41 generic
  bulk goods (Genesis Cable, Reliablewire, Casil, Windy City Wire, Interstate, Yucel) that
  is **57 products that must come out of the denominator before any coverage rate is
  computed.** The recorded rule is that a denominator has to travel with a rate; this adds
  that **the denominator itself needs auditing for things that are not photographable.**
- **A required accessory sold only in a carton of ten is a purchasing fact, not a
  spec.** Edwards states the **GRSW** wiring plate is required for `GCSVWN` and sells
  it **only as a 10-pack**. A buyer ordering one appliance cannot order one plate. That
  belongs in the closing paragraph next to the sibling parts, because it is the thing
  the buyer gets wrong &mdash; and it is the `4099-9015` / `A49CMT-APPLW` incomplete-
  product trap with a quantity attached.

- **Two agents in one batch converged on the same sibling separator from opposite ends,
  and the earlier of them had already been published.** Agent 1 corrected `1505-AQN5`'s
  title from *&quot;Semi-Flush&quot;* to flush wall mount; agent 2, working `1504-AQN5`
  independently, found the same Kidde document and established that **the pair differs
  by catch plate length alone** &mdash; 2-5/8 in. against 1-5/8 in., render-quantified
  &mdash; which is also why the 1504 alone takes the long `CS2598-5` armature where the
  1501, 1502, 1505, 1508 and 1509 take the short `CS2595-5`. Checked live after both
  published: the two titles agree and neither asserts a mount style the other denies.
  **Pair-splitting paid for the fourth time**, and it is worth noting the failure this
  avoided: had only one agent seen the pair, &quot;Semi-Flush&quot; would have been
  corrected on one page and left standing on its sibling.

- **A part documented in exactly one place, and it is not a catalogue sheet.** `3-LRMF`
  is **absent from every current EST3 catalogue sheet and from the Submittal Guide**; the
  only Edwards statement naming it is in the **EST3 Installation and Service Manual
  `270380-EN`**, verbatim in revisions 016 and 017 from two unrelated mirrors: *&quot;If
  there are empty rail spaces in a cabinet, you should consider installing 3-LRMF blank
  plates to fill up the spaces.&quot;* **LRM = Local Rail Module**, manufacturer-stated in
  `E85010-0099`. **Check the installation and service manual before writing off a legacy
  Edwards accessory as undocumented** &mdash; and note the resellers asserting EST3X fit
  are unsupported: EST3X does use LRMs but `3-LRMF` appears zero times in `E85005-0134`.
  Route: **Edwards LifeLines has a level deeper than its index shows.**
  `/lifelines/control-panel` is empty, but the percent-encoded nav JSON inside the index
  HTML discloses **`/lifelines/control-panel/est3-platform/`** &mdash; follow the 301
  &mdash; which lists **40 EST3 PDFs** including the Submittal Guide. Same for
  `est3x-platform`.
- **The class noun was right and the buying decision was still missing.** `SA-CLA` really
  is a &quot;Class A adapter module&quot; in Kidde's own words, so this is not a
  product-class error &mdash; but it is a **bare option card** that mounts on plastic
  standoffs and a plug connection directly on the panel main board, and it fits **only the
  two-NAC FX-64 and VS1**. The four-NAC FX-1000 and VS4 are Class A ready and take no
  adapter at all. **The panel family is what a buyer gets wrong**, so it went in the
  title. Thirteenth incomplete-product case, and the first where the existing class noun
  needed no correction.
  Route: **the Kidde literature library reaches Edwards' `myeddie` PublicMedia store** —
  `POST kidde-esfire.com/LiteratureLibrary/GetCategoryNavigation` with
  `categoryName=Small Building Life Safety Solutions` returns the FX and VS catalogue-sheet
  URLs directly.
- **THE COORDINATOR SPLIT A BATCH BY EYE AND HALF A BRIEFING WENT TO THE WRONG AGENT.
  This is the v2b03 hand-transcription failure in its third and worst form, and this
  file's existing rule was too narrow to catch it.** Building v2b34, the slice script
  wrote `a1_in.json` and `a2_in.json` correctly. The coordinator then read the script's
  **printed listing** and assigned products to the two briefings **from the screen**,
  getting three of six wrong in each direction. Agent 2 was briefed at length on
  `SIGA-CRH`, `PAD300-DD` and `2099-9139` &mdash; including the whole
  `S2099-0010` break-rod-versus-breakglass paragraph &mdash; **and held none of them**,
  while the three it did hold (`FSP-851R`, `PRO5`, `P2GWKLED-P`) got no routing notes at
  all. The briefing also called `SIGA-CRH` *&quot;the batch's biggest at 1,934
  impressions&quot;*, a figure belonging to a product outside that agent's slice.
  **Nothing was published wrongly, and the reason is the rule that did hold:** the
  briefing says the file is authoritative and the prose is a hypothesis, so the agent
  worked its file, flagged the mismatch as its headline finding, and wrote six correct
  products. The cost was research effort, not a defect.
  **The rule generalises past ids, again.** This file already says *never type an id
  anywhere &mdash; briefing, query, mutation or note*, written after ids were typed into
  a live query. That is still too narrow: **the id was never the thing transcribed here.
  The product-to-agent ASSIGNMENT was.** So: **build each briefing from its own
  `aN_in.json`, programmatically, and never from a listing of the whole slice.** A
  coordinator reading a twelve-row table and writing two six-row briefings is doing
  manual transcription whatever the field is called.
- **A carrier with no LEDs, named &quot;LED Support Module&quot;.** `3-LDSM` reads as a
  display and is not one. `E85010-0055`: EST3 Control Display modules normally mount over
  a local rail module, which feeds them power and drivers by ribbon cable, and *&quot;when
  a display module is required where no local rail module exists, an LED Display Support
  Module 3-LDSM mounts to the local rail providing support for one Control Display
  Module.&quot;* **Its Technical Specifications row gives N/A for number of LEDs, N/A for
  LED colors and N/A for switches** &mdash; the manufacturer states the absence outright.
  **Series-block trap avoided in the same document:** Note 1 reads *&quot;All Control
  Display Modules are UL and ULC listed&quot;*, and the 3-LDSM is **not** a Control
  Display Module but the thing that carries one, so **no UL or ULC listing was claimed
  for it** &mdash; only the page-1 approvals block. That is the `SD365T-IV` rule applied
  to a listing rather than a temperature.
- **A clean complete-product NEGATIVE, stated as such.** `SIGA-CRH`: all four
  &quot;required&quot; hits in `E85001-0644` are ordinary usage (*&quot;twisted wire is
  not required&quot;*, *&quot;minimum load required&quot;*), **`SIGA-MP` appears 0
  times**, and there is no separate plate catalogue number &mdash; where the plain
  `SIGA-CR` needs a 1-gang box **with** a SIGA-MP plate. So the `H` is settled and is not
  a naming trap: one relay, **two identical Form C sets that transfer together**, **7 A
  at 120 V against SIGA-CR's 0.5 A**, on a double-gang or 4 in. square box.
  **A free generation check worth copying:** Issue **1.0** was pulled from a second
  mirror and its Specifications block is **byte-identical to Issue 1.1** after whitespace
  normalisation, 1,554 characters each. Every figure published is stable across both.
  One lead deliberately not published: the mirrored installation sheet `3102238-EN`
  carries **&quot;Current, 8.4 A max. (AC or DC)&quot;**, a row the first-party datasheet
  lacks. Every other figure on it matches exactly, but that one is in no first-party
  document read. **One first-party fetch settles it.**
- **Two wrong-document-family instances in one batch, and one of them would have read as
  an invented part number.** `EWGSVMRF` appears **zero** times in `K85001-1031`
  (&quot;Outdoor Speakers and Speaker-Strobes&quot;) and **zero** in `K85001-1030`
  (&quot;Outdoor Horns, Strobes and Horn-Strobes&quot;) &mdash; the two obvious sheets.
  It is in `K85001-1056`, the outdoor **Extended Candela** sheet. And `6820UEVS` appears
  **zero times in the 6820EVS datasheet and zero times in its 170-page installation
  manual**; it is real and documented on Honeywell's own product pages. **Two more
  reasons the rule holds: a negative bounds the search, not the catalogue.**
  The `E/K` prefix rule was also confirmed again in the form this file already states:
  **the `E` is inside the series code**, Kidde's being `EWG` where Edwards' is `WG`, and
  the syntax block splits `EWGSVMRF` as `EWG` outdoor Genesis + `SV` speaker-strobe +
  `M` extended candela + `R` red + `F` FIRE. The coordinator's guess that `VM` meant
  visual multi-candela was wrong.
- **The `3X-FIB` fibre-mode answer is &quot;neither&quot;, and that is a class of answer
  this file did not have.** Fibre mode is recorded here as one of the three highest-risk
  title fields. `E85005-0133` p9: *&quot;3X-FIB &mdash; Fiber motherboard&hellip; **Used
  with MMXVR, SMXHI2 and SMXLO2**&quot;* &mdash; **the card carries no optics at all.**
  Mode is set by a separately catalogued transceiver: SMXLO2/SMXHI2 single mode with
  Duplex SC, MMXVR multimode with ST. **Any copy qualifying this card with a mode asserts
  something Edwards deliberately leaves open**, and nothing in the live title did.
  &quot;Fiber Motherboard&quot; is verbatim Edwards ordering wording, so this is the
  `FSL-E3` shape &mdash; keep the manufacturer's name, put the class detail in the body
  &mdash; not the `3-LDSM` carrier error.
  **Three document defects on one page of that sheet, nothing published from any.**
  `E85005-0133` p6, confirmed by word coordinates and a 400 dpi render: the **diagram
  callouts are swapped**, each illustration labelled with the other product's card; the
  **Cable type row is empty** while the string `50/125, 62.5/125, or 100/140 for` has
  landed on the **Connectors** row truncated after &quot;for&quot;, and the same string
  occupies the **MMXVR optical Budget cell** where a dB figure belongs, so **MMXVR's
  budget is unstated**; and p9 gives **`3X-NET` and `3X-NET8` the identical
  description**. The first two reproduce identically in the adjacent 3X-FIB8 table, which
  rules out extraction error. **No cable core size was published, and 50/125 was
  specifically not attributed to the single-mode transceivers.**
- **`S3000` confirmed a FOURTH time, on the document the coordinator could not
  previously retrieve.** This file records that a v2b27 agent read it off `E85010-0057`
  and that the fetch failed at the time. That document is now in hand: **`S3000` is
  printed in its page-1 Approvals block beside `7165-1657:0186/0306`, the ULC mark, CE
  and the EN 54 lines.** So the ULC-file-number finding has confirmations on
  `E85010-0130`, the Kidde FX sheet, and **its own original source**. The old
  &quot;bogus S3000&quot; note is disproved on the document that produced it. Leave it
  settled; the slug is `E85010-0057 -- EST3 Zoned Audio Amplifiers.pdf`, built by hand
  after a search gave both the number and the title.
- **Sixteenth incomplete-product case, proved by an INVERTED come-with clause.**
  `3-ANNCPU3` ($1,232.25) was titled &quot;Annunciator CPU&quot; and typed Annunciators.
  `E85010-0069` files it under *&quot;CPU, Support Module, &amp; LCD Displays&quot;*, and
  the heading above the finished units reads **&quot;Base Annunciators (Come with two
  3-ANNSM annunciator support modules, a CPU, and doors&hellip;)&quot;**. Ship weight
  **1 lb against 6&ndash;10.5 lb** for a base annunciator; mounting space **two**. So the
  buyer receives a board &mdash; no cabinet, wallbox, doors or display modules. That is
  the `3-SDC1` shape: **a catalogue number appearing inside another product's come-with
  clause is a component.**
  **Handled per the `FSL-E3` precedent**: &quot;Annunciator CPU&quot; is Edwards' own
  ordering description, so it was kept and **&quot;Module&quot; added** rather than the
  class noun rewritten.
  Its Specifications table is the worst merged cell of the batch: **Agency Listings
  &quot;UL, ULC, FM, CE, LPCB EN54&quot; spans three columns and renders visually under
  the `3-ANNSM` header**, so naive pairing gives `3-ANNCPU3` the wrong listing set.
  Settled by column-centre arithmetic cross-validated on a four-distinct-value row, then
  by render.
- **THE SLICE FILE SHIPPED AN EMPTY `live_desc` FOR FOUR BATCHES, AND IT IS THE
  LOSSY-SLICE-FILE FAILURE FOR THE FOURTH TIME &mdash; a silent REGRESSION introduced by
  an unrelated change.** Measured exactly across all 53 slice directories rather than
  estimated: batches before **v2b26** have no `live_desc` key at all, which is honest
  &mdash; the briefing was openly the only source of live text. **v2b26 through v2b32
  carried the field POPULATED**, seven batches of real live copy. **v2b33, v2b34, v2b35 and
  v2b36 carried it PRESENT AND EMPTY** &mdash; 48 products whose agents were promised the
  live description and handed `&quot;&quot;`.
  **The cause is the interesting part: the regression rode in on the batch-size change.**
  `build33.py` was written to implement the owner's 12-products-and-two-agents instruction,
  and in the rewrite it took the live copy as `p.get('descriptionHtml','')[:1400]` where
  `p` comes from **`catalogo_full.json`, which carries no `descriptionHtml` field at all**
  &mdash; its keys are id, handle, title, vendor, type, vis, inv, created, sku, price,
  impr, rev. The previous builder had sourced it elsewhere and nobody diffed the output.
  **Note how it hid.** The two earlier instances were a blank `type` and a human-readable
  note in a field; both were *visible* in the file and an agent reported each one within
  the batch. This was visible too and four batches of agents said nothing, because an empty
  string in that field reads as &quot;this product has a thin description&quot; &mdash;
  which is exactly what every product in this queue has. **The defect wore the shape of the
  expected value**, which is why it survived four batches where a blank `type` survived
  one.
  The fix is a join, not a default: `build37.py` takes `type` from `catalogo_full.json`
  (verbatim, as the rule requires) and `handle`, `title`, `vendor` and `descriptionHtml`
  from the **live** bulk pull `live.jsonl`, whitespace-collapsed to 1,600 characters, and
  **asserts the slice is 12 long and prints which rows came back with an empty
  `live_desc`**. On v2b37 that list was empty and the live bodies immediately paid: they
  surfaced `SIGA-HRD-FCN`'s *&quot;FCN: Manufactured in China&quot;* (the `SIGA-OSD-IN`
  shape exactly), `49VO-APPLC`'s *&quot;order cover separately&quot;* and a shipping notice
  inside a description, none of which the coordinator would have known to brief.
  **The general rule this sharpens: assert on the slice, do not eyeball it.** Every input
  field the agents reason about should be checked for emptiness by the builder, because the
  coordinator reads a slice listing for *products* and never for *missing fields*.
- **The Kidde Fenwal ERP codes decoded, 96 titles written, and the `T` is TONS &mdash;
  the coordinator's inch reading was wrong and the agent proved it with a SET MATCH.**
  The briefing read `GAUGE-LL_60T-HORZ` as a 60-inch dimension. It is **60 tons**: the
  hardware is **Kidde/Chemetron CARDOX Low Pressure CO&#8322;**, a refrigerated ASME vessel
  holding CO&#8322; at about 0 &deg;F and 300 psi with an R-404A package, and the
  manufacturer prints its range in the ERP's own notation.
  **What settles it is not the bullet, it is the set.** Computed first-hand from the store's
  own ERP strings: the horizontal tonnages are **{2.75, 3.75, 4, 6, 8, 10, 12, 14, 18, 22,
  26, 30, 34, 38, 42, 46, 50, 60}** &mdash; eighteen values &mdash; and the vertical ones
  **{6, 14, 26, 30}**, four. The agent reports those are exactly Kidde's eighteen horizontal
  and four vertical tank sizes, zero extras and zero missing, and the **endpoints 2.75 and
  60 are the manufacturer's own stated range**. A 2.75-inch-to-60-inch gauge ladder is not a
  thing, and a four-value vertical subset nested inside the horizontal set is a tank-size
  pattern, not a dimension. **`DC` is manufacturer-decoded too** &mdash; Kidde's option list
  offers exactly two, *&quot;Liquid Level Gauge with Dual (NO/NC) Contacts&quot;* and
  *&quot;with 4-20mA Output Signal&quot;*, against exactly two ERP tokens, and
  `0200-9275W-DC-CH` spells `DC` in its own part number.
  **The nozzles are the big catch and they went the other way.** The briefing offered
  &quot;Kidde CO&#8322; nozzles&quot;; Kidde's own CO&#8322; nozzle sheet `K-81-1170` tabulates every
  CO&#8322; nozzle as `803xxx`/`842xxx`/`9xxxxx`, **identified by orifice code and never by a
  degree pattern**, and nothing of the `85-1944xx` form appears. The mechanism is the
  document-series prefix: `K-81-` documents 81-series CO&#8322; parts, `K-85-107` documents
  **`85-`** ADS fan nozzles at 180&deg; and 360&deg;. So **180/360 as a discharge pattern is
  right and &quot;CO&#8322;&quot; is wrong**, and the twenty published titles carry the class,
  the degree, the size, the thread and the material and **deliberately assert no agent.**
  That is a product-class error avoided in a feed attribute, on the coordinator's premise.
  **Two SKU defects, one of which the coordinator missed:** the `-2xx` wildcard is confirmed,
  **and there is a stray leading `1-`** &mdash; Kidde's number is `85-1944xx-2XX` and the
  store's SKU is `1-85-1944xx-2xx`. Neither touched.
  **`1090-4` was HELD and it is the sharpest row in the set: three fields, three products.**
  Its Shopify title reads *&quot;Cylinder ARG 110 Filled YL&quot;* (a filled argon cylinder),
  its ERP reads `CONTROLLER-TEMP_NEMA1-DISPLAY`, and its `type` is Annunciators. The live
  title is certainly wrong &mdash; and **replacing one unsourced claim with another is not an
  improvement**, so nothing was written and it went to the owner.
  Published: **96 of 121**, in four aliased mutations of 24, every `userErrors` empty. 24 were
  returned unchanged because they already had a product name &mdash; **the coordinator's
  &quot;all 121 are nameless&quot; was wrong, only 96 were.**
  Route: **`kiddefenwal.com/?wpdmdl=<id>` serves the file and a plain HEAD returns
  `content-disposition: filename=&quot;<docnum>_print.pdf&quot;`**, so sweeping ids builds the
  whole 206-document index. **New fingerprint, reproduced by the coordinator:
  `kiddefenwal.com/LocalMedia/Data Sheets/<anything>.pdf` returns HTTP 200 with
  1,279,593 bytes of `text/html`** &mdash; byte-identical for a real and an invented filename,
  and every `LocalMedia` URL still in Google's index is dead.
- **Two coordinator premises wrong on one part, and the live page was right.** `RP5209` was
  briefed as probably the `SF-`/Space Age shape &mdash; a SAFE Fire Detection part filed
  under the wrong vendor. **Edwards catalogues `RP5209` itself**, under ModuLaser, in
  `E85001-0633`, and **the live description is verbatim Edwards ordering wording**,
  including the *&quot;English/Spanish&quot;* that reads like ERP junk and is Edwards' own
  text: the NFPA wording is printed bilingually **along the pipe**. The SAFE RedPipe family
  really does share the numbering, so the brand link is real &mdash; but **this is the
  `PIP-018` shape, not the `OSE-HPW` shape, because the store's own brand has a first-party
  document for the part.** Nothing corrected.
  One conflict flagged rather than resolved: **Edwards says 7.5 ft and SAFE says 8 ft for
  the same number**, with the 15 ft variant agreeing. Published Edwards' figure; pipe is
  bought by the foot, so a carton settles it.
- **Two routing corrections on Edwards, and one is a part in the wrong panel generation.**
  There is **no `/lifelines/control-panel/est4x-platform/` page** &mdash; the slash form
  301s to the bare form and the bare form 404s at 17,844 bytes. And **`4X-LCD-LC` is an
  EST3X part, not EST4**: EST4's display is the `4-LCD` colour touchscreen in `E85014-0007`,
  where `4X-LCD-LC` occurs **zero times**. It is in `E85005-0133`, whose Accessories row
  states the separator outright &mdash; `4X-LCD` *&quot;English language&quot;* against
  `4X-LCD-LC` *&quot;**Insertable language**, shipped with English inserts. Order alternate
  languages separately.&quot;* **What `LC` stands for is in no document read**, recorded as
  a bounded negative rather than guessed.
  Its live title was a 145-character ERP string cut at the 150 cap (*&quot;&hellip;Shipped
  with English&quot;*) &mdash; but **unlike the 79 unbalanced-parenthesis cases the missing
  text is recoverable from the manufacturer's own row**, so a proper short title was written
  rather than the ending reconstructed. That is the right handling and worth distinguishing:
  **this project refuses to invent a truncated ending, not to write a new title.**
- **A look-pass rejection that is the Power-Sonic shape on an extinguishing agent, which is the
  worst place for it.** `45-550451-901` had the best paper case in its batch: its Kidde datasheet
  states verbatim *&quot;The part number for ordering the ECS-500 System 450 lb. cylinder with
  liquid level indicator is 45-550451-901&quot;*, the sheet is titled **Fluoro-K**, and page 1
  carries a cylinder photograph with the subject filling the frame. Every mechanical check passes.
  **Zoomed 6&times;, the cylinder's own label reads &quot;Fire Suppression System with HFC-227ea
  Agent&quot;** &mdash; Kidde reused the HFC-227ea photograph on the Fluoro-K sheet. **On an
  extinguishing product the agent IS the distinction**, which is the `429022` &quot;ABC on a clean
  agent&quot; defect waiting to happen in a picture rather than a word.
- **A series-wide LISTING block where three of the listed standards belong to a component the
  part does not have.** Edwards `E85001-0283` gives the whole 964/965 family *&quot;UL 1971,
  UL 1638, UL 1480, ULC S526, ULC S541, CE, FM, CSFM, MEA&quot;* &mdash; and **UL 1971, UL 1638
  and ULC S526 are strobe standards while `965-1A-4RW` has no strobe**, `1A` being the
  speaker-only code (proven against the `-5A`/`-7A`/`-3A`/`-8A` candela codes in the same
  ordering table). That is the `3-LDSM` shape: a family listing line is not a listing for a
  member that lacks the listed component. The closing paragraph says so explicitly.
  Also settled there, manufacturer-stated: **964 Series is 25 Vrms and 965 Series is 70 Vrms**,
  and the final letter is the finish, proven by the `965-1A-4RR` &quot;Speaker, Red&quot; /
  `965-1A-4RW` &quot;Speaker, White&quot; pair on one y-line.
- **A part in NEITHER obvious document, found in an installation sheet's figure callout.**
  `4-CABL0505` appears **zero times** in `E85014-0004` *&quot;EST4 Cabinets and Chassis&quot;*
  (fetched first-party, bogus control = the documented 1,245-byte 404), whose only `4-CABL`
  row is `4-CABLUSBLG`. It is in the **4-CAB16D Series Door Assembly Installation Sheet**
  `3102273-EN REV 001`, as **callout (10) of Figure 5**, read off a 300 dpi render: a UI flex
  cable running J1&rarr;J2 between two `4-8ANNFA` frame assemblies on the inner door. **Eleventh
  wrong-document-family instance, and the second where the answer was a figure callout rather
  than a table** &mdash; for an accessory, go to the parent's *installation* material and read
  its exploded diagram, not its catalogue sheet.
- **A live page telling the buyer to order a cable the manufacturer says this model does not
  need &mdash; the inverse of the incomplete-product trap.** The `3-4ANN` body ended
  *&quot;or one 3-LCDXL1 (Order 3-LCDXL1KBL Separately)&quot;*. Edwards `E85010-0069` says the
  opposite **in two places in one ordering block**: the 3-LCDXL1 row scopes the cable to
  *&quot;3-6ANN or 3-10ANN annunciator boxes&quot;* with 3-4ANN absent, and the cable's own row
  reads ***&quot;Not required with 3-4ANN and 3-LCDXL1 applications.&quot;***
  **Every recorded instance of this family costs the buyer a missing part; this one costs them
  an unnecessary one**, which is milder and much harder to notice, because nobody complains
  about a part they did not need.
  The real omission on that page was elsewhere and larger: **the wallbox is a separate
  catalogue number** (`4ANN/B` flush, `4ANN/B-S` surface), so at $2,797.50 the buyer gets an
  annunciator with nothing to mount it in and nothing on its four positions. **Sixteenth
  incomplete-product case** &mdash; and note it is *not* the `3-ANNCPU3` bare-board shape: this
  one genuinely is a finished Base Annunciator with CPU, two support modules and doors. My
  inference was half right, which is the useful half to record.
- **The E/K carton split confirmed on a THIRD document number, and a route correction with
  it.** Edwards `E85001-0668` marks the GP10 wiring plate *&quot;required, **ordered
  separately**&quot;* and *&quot;in **packs of 10**&quot;*; Kidde `K85001-0668`, same number,
  marks it *&quot;required, **included with device**&quot;*. Same hardware, opposite carton,
  after `85001-0667` and `85001-1021`. It also confirms **the `E` is inside the series code**
  (Kidde's title is &quot;**EG4** Series&quot;) and that Kidde drops the `-FR`/`-SP` variants.
  **Route correction: `kidde-esfire.com/Content/Documents/` returned the 1,245-byte 404 for
  all three constructed names.** The literature API &mdash; POST, **`www.` host required**, the
  bare host 301s &mdash; returns hrefs pointing at **`myeddie.edwardsfiresafety.com/PublicMedia/Catalog Sheets/`**.
  **Kidde sheets are served from the Edwards store**, which is the one-codebase-two-brands
  finding reaching the asset layer.
- **A shell whose MD5 varies because it echoes the path, so an MD5-only control passes it.**
  `genesiscable.com` is now a Southwire storefront returning an identical **75,721-byte HTML
  shell with a different MD5 every time**; **the byte count is the only tell.** That is the
  fourth distinct way a bogus control can be defeated, after the query-echo (byte drift), the
  CSRF token (invisible variation) and the constant-length ignore (near-identical bytes).
  The parts do resolve first-party at `southwire.com/p/<sku>` &mdash; **and those pages carry
  no product photograph at all**, so Genesis is a **measured** zero rather than an assumed
  one, and the Edwards-Genesis hypothesis in the briefing was wrong: all 21 are Genesis Cable.
- **A purchased software activation merchandised as hardware.** `MODBUS-CGW` is a **feature
  license** applied in the CLSS App against the account's token balance &mdash; no hardware is
  shipped, and the gateway (`HON-CGW-MBB`, or `CGW-MB` board plus `CGW-BB` enclosure) is a
  separate purchase. Every hardware specification a reader would take from its page belongs to
  the gateway. That is the incomplete-product trap with **nothing physical in the box at all**,
  which is a category beyond the fourteen recorded cases, and it joins the FireWorks licences
  and `TRNG-F-EST4-CERTIF` in the not-photographable population from the other direction.
- **Being derivable, first-party and exactly named is STILL not evidence about what is in the
  frame: 20 rejections after every mechanical check passed.** On that route, four Edwards
  module renders carry **another product's catalogue number printed on the label** &mdash;
  `SIGI-CC1I` and `SIGI-CC2I` both read `CAT. NO. SIGA-MAB / CLASS A/B MODULE`, `SIGI-CRI`
  reads `CAT. NO. TCDR / TEMPORAL PATTERN GENERATOR`, and **`SIGI-IOI` serves a wildcard
  mock-up label** reading `CAT. NO. SIGA-Mxx / XXXXXP / YYYYY / COMPATIBILITY I.D. #0.0`.
  A fifth, `SIGI-CC1SI`, is captioned DUAL INPUT on a single-input SKU. One serialised unit
  carrying barcode `4800000772` is served for **four** different catalogue numbers.
  So the ladder is now complete and each rung has failed in the wild: a **filename** can name
  the wrong product (Power-Sonic), a **structured `modelId`** can be silent about it (STI),
  Honeywell's own **`sku_list`** can assert the wrong record (`MS-4E`), and now a
  **path derived from the catalogue number itself** can serve another part. **Nothing short of
  reading the label or counting a feature in the photograph is sufficient.**
- **A derivable path can be variant-BLIND on one sub-family and variant-AWARE on another, on
  one host &mdash; and the boundary is findable mechanically once you have seen one case.**
  Found by eye (`EG4SVWA` claims ALERT marking and its render shows none), then bounded by
  probing every hit's lettering and colour siblings and comparing bytes:
  `EG4SVWA` &equiv; `EG4SVWN` &equiv; `EG4SVWF` &mdash; **one unlettered render standing for
  ALERT, none and FIRE** &mdash; and `G4SRF` &equiv; `G4SRN`, `G4SWF` &equiv; `G4SWN`,
  `G4LFVRF` &equiv; `G4LFVRN` &equiv; `EG4SVRF`. But `EGCSVWA`/`EGCSVWN`/`EGCSVWF` are **three
  distinct files**, and `GCSWN` &ne; `GCSWF`, `G1ARF-E` &ne; `G1ARN-E`.
  **The sweep over all 110 hits returned exactly the three groups found by eye and no others.**
  Blanket trust publishes three wrong lettering variants; blanket distrust throws away the whole
  G1 family. Corroborated by the Kidde ZIP's own human-written filenames, which distinguish
  `&quot;EG4SVWA - Wall Speaker-Strobe.jpg&quot;` (no ALERT) from
  `&quot;EGCSVWA - Ceiling Speaker-Strobe ALERT.jpg&quot;`. **Look once, then bound it by
  probing siblings** &mdash; that converts an anecdote into a measured boundary for a few
  hundred requests.
- **THE SIBLING-SKU CHECK FIRED AGAIN, ONE LOT AFTER IT WAS WRITTEN DOWN, AND THIS TIME IT
  SAVED A TITLE RATHER THAN A CLASS NOUN.** The `SIGA-OSHD-IN` agent proved the `-IN` suffix is
  in **no** Edwards document &mdash; zero occurrences across `E85001-1003` Issue 1.6,
  `E85001-1001` Issue 1.5 and both Submittal Guides, with the Ordering block listing only
  `SIGA-OSHD`, `-NL` and `-B` &mdash; correctly declined to call it invented, left the SKU
  alone, and **dropped it from the title**, writing `Edwards SIGA-OSHD ...`.
  **The store sells `SIGA-OSHD` as a separate product.** So the new title would have been
  indistinguishable from another live SKU's. The `-IN` was restored, and the body now says
  plainly that no Edwards document read defines it.
  **The general rule is the `PTS-C CABLE` one, and it now has both directions:** *before
  writing a title, ask whether the store already sells something under that exact name.* There
  it stopped a $78 cable being titled as the $280 switch its documents describe; here it
  stopped a suffix being dropped off a part whose bare number is a different product.
  **And it sharpens the recorded `ICA12-50JPLLR-500` precedent**, which is the case that looks
  identical and is not: there the trailing token was **proven** to be a reel length, so keeping
  it out of the part number asserted something sourced. Here the suffix is **unsourced**, so
  dropping it asserts that it is not part of the catalogue number &mdash; which is exactly the
  kind of claim this project does not make from an absence. **An unsourced suffix stays in the
  title; a sourced non-suffix comes out.**
- **An ordering-syntax block with OVERLAPPING BRACKETS, which is a new shape of the extraction
  trap and the first one that is a drafting error rather than a layout artefact.** Rendered at
  280 dpi: on the Edwards GC sheet the Genesis Series bracket spans exactly `GC` and the
  Functions bracket spans `AV`. On the G4S sheet **the Series bracket spans `G4S` while the
  Functions bracket underneath spans `SV` &mdash; the two overlap on the `S`**, assigning one
  character to two tokens. The ordering table settles it (`G4SWF` under Speakers, `G4SVWF`
  under Speaker-strobes): the parse consistent across both sheets is series `G4`/`GC`, then
  function `S`/`SV`/`A`/`V`/`AV`, then colour, then marking.
  **So `S` is the speaker-only function token and the part has no strobe.** This file elsewhere
  calls the manufacturer syntax block *the best decoder there is*; it has now been shown to
  carry a typo in one field (HyperSpike's 200 V) and here to be **geometrically ambiguous**.
  Read it against the ordering table like any other prose.
- **A supersession refuted by the mechanism check in the UNFAVOURABLE direction, on both halves
  of a pair.** `4098-5610` and `4098-5611` carried &quot;(Replaces 4098-9613)&quot; and
  &quot;(Replaces 4098-9612)&quot;. Neither is manufacturer-stated in either direction &mdash;
  the new numbers appear zero times in the legacy sheet `S4098-0014-10` and the legacy numbers
  zero times in the current `S4098-0059 Rev 2`, and across the 961-record JCI index **no single
  document's metadata lists both generations**. What makes it worse than unsourced is the
  `SIGA-HRS` test: **UL and ULC listed spacing falls from 70 ft to 50 ft**, render-confirmed on
  both sheets (the legacy figure in a cell merged across all four legacy models, the new one in
  each model's own cell). A layout drawn on 70 ft needs more devices when re-equipped, so an
  unqualified &quot;Replaces&quot; in a Merchant Center attribute is not merely unsourced but
  costs the buyer. Claims moved to the body with the spacing difference stated.
  Two further differences argue the same way and none was carried across: the legacy rate of
  rise is *&quot;Between 15&deg; &amp; 25&deg; F/min&quot;* where the new part is
  *&quot;&ge;20&deg;F/min, only in effect above 90&deg;F&quot;*, and the legacy sheet carries FM
  ratings and calls the line **rate compensated** while the current sheet states neither for the
  56xx parts. **That is a fifth brand on the rate-compensation list and a reason NOT to import
  it**, since the successor generation does not claim it.

- **A number inside a catalogue number that is a TERMINAL COUNT, read by the store as a
  DIAMETER &mdash; and the correction propagates to an untouched sibling.** `KC2-SB4` was titled
  *&quot;Kidde KC2-SB4 **4&quot;** Standard Base&quot;*. Kidde `K85001-0599`, fetched through the
  literature API and read by the coordinator with word coordinates, gives four rows on four
  y-lines:
  `KC2-SB` Standard base, 4 terminals, **4&quot; dia.** &middot; `KC2-SB4` Standard base
  **w/trim skirt**, 4 terminals, **6&quot; dia.** &middot; `KC2-RB` Relay base, 4 terminals,
  aux. relay, 4&quot; dia. &middot; `KC2-RB4` Relay base **w/trim skirt**, 4 terminals, aux.
  relay, **6&quot; dia.** The token `6&quot;` sits at x=418.9 on the `-SB4` line and `w/trim`
  appears only on the two `-4` lines.
  **So the trailing `4` is the terminal count and the skirt marker, and the live title took it
  for the diameter** &mdash; asserting 4 inches on a 6-inch base, in a Merchant Center attribute,
  on a brand where the store sells both sizes at the identical $6.70. This is the `AS-75-R-WP`
  and `PDC-12xxxx` shape (a number inside a model number that is not the spec it resembles) with
  a new twist: **the resembled spec is a real property of the SIBLING**, so the wrong reading is
  true of a part the store also stocks.
  **`KC2-RB4` carries the same defect and was NOT touched**, because it is not in this batch;
  it went to the owner's file. Worth stating as a rule, because this file records the opposite
  case: the `RP-2002`/`RP-2002E` correction *propagated* across a family on its own, and that is
  a property of how Shopify stores titles, not something to rely on. **When a title defect is
  decoded from an ordering table, check the whole table for siblings carrying it** &mdash; the
  decode costs nothing extra and the sibling is one row away.
- **Two Kidde printings of ONE document number disagreeing on a figure that belongs to neither
  part in question.** The Kidde and Edwards printings of document `0599` give maximum wind
  velocity as **300 ft/min against 4,000 ft/min** and carry different host-panel lists. Neither
  was published, and the reason is cleaner than the disagreement: **both figures belong to the
  detector head, not to the base** this page sells. The `3-LDSM` precedent &mdash; a family
  listing or rating line is not a property of the carrier &mdash; applied to a document conflict
  that therefore did not need resolving at all.

- **TWO EDWARDS GENESIS GENERATIONS USE DIFFERENT SUFFIX GRAMMARS IN DIFFERENT ORDERS, AND
  THIS FILE'S OWN DECODER NOTE POINTS AT THE WRONG SHEET.** This file says page 5 of the
  Edwards catalogue sheets carries a Model Number Syntax block that decodes any G1/G4/GC part.
  **`Syntax` occurs ZERO times in `E85001-0573`**, the legacy Genesis Wall Horns and Strobes
  sheet &mdash; that block exists only on the **LED** sheets (`E85001-0667`/`0668`).
  **The two grammars run in opposite orders**, which is why two real parts look unrelated:
  legacy is `G1` + colour (`R` red / blank white) + marking (`F` FIRE / blank) + `-` + function
  (`VM` visual multi-candela), giving `G1F-VM`; LED is `G1` + function (`A`/`V`/`AV`) + colour +
  marking, giving `G1VWF`. **A suffix grammar is a property of a generation, not of a brand**
  &mdash; the recorded `MX16RSS-US` lesson (read enough rows to see which letters vary
  independently) with a second axis, time.
  And this file's note that `G1RF` and `G1VF` &quot;do not exist&quot; is **half right**:
  `G1RF-VM`, `G1RF-HDVM` and `G1R-VM` are real legacy rows; only `G1VF` appears nowhere.
- **THE OWNER FLAGGED ONE TITLE AND IT OPENED A 34-PAIR DUPLICATE, A THREE-WAY VENDOR SPLIT AND A
  DEFECT CLASS THE NON-ASCII AUDIT CANNOT SEE. His words were &quot;Edwards RP2226 ?? Test Point
  &mdash; Test Point is ModuLaser not Edwards&quot;, and he was right about the catalogue being
  wrong and wrong about which field.**
  **Edwards DOES catalogue `RP2226`.** `E85001-0633 -- Air Sampling Pipe and Fittings`, fetched
  from the first-party `myeddie /PublicMedia/` store and read directly by the coordinator (4
  pages, 1,243,185 bytes, mime-clean), carries the row verbatim: ***&quot;RP2226 &mdash; Test
  point for 3/4&quot; pipe &mdash; Can be used with CPVC and ABS&quot;***. That is the recorded
  `RP5209` precedent exactly &mdash; the `PIP-018` shape, where the store's brand has a
  first-party document for the part &mdash; so the vendor string is not invented and **ModuLaser
  is Edwards' product line, not a manufacturer**.
  **What IS wrong is that one Edwards sheet is split across three vendor strings.** Of the 175
  `RP*` SKUs live: **Modulaser 30, Space Age 39, Edwards 2**, Rath 103 (an unrelated numbering)
  and Napco 1. Twenty-two of the numbers in that one sheet sit under two different brands, and
  **the sheet mentions neither &quot;RedPipe&quot; nor &quot;SAFE&quot; once** &mdash; while the
  store's own published `RP5205X` copy says *&quot;manufactured as RedPipe by Safe Fire
  Detection&quot;*, sourced elsewhere. Thirteen more Modulaser-branded SKUs (`RP5211`, `RP5214`,
  `RP5217`, `RP5248`&ndash;`RP5256`, `RP7125`) are **not in the Edwards sheet at all**, which is
  the honest boundary: Edwards resells part of the RedPipe range, not all of it.
  **The expensive finding is the duplication, and it was invisible until the vendor question was
  asked.** `SF-RP2226` (Space Age, $16.65) and `RP2226` (Edwards, $12.60) are the same fitting.
  **34 pairs, and EVERY ONE carries a different price** &mdash; SF- dearer on 22 and cheaper on
  12, median **+24%**, worst `RP5240` at $225.10 against $334.55, and the nine sample-hole markers
  `RP5248`&ndash;`RP5256` at **$20.65 against $7.60, 63% apart**, identical parts. Two search
  results for one part, two Merchant Center offers for one number. This is the recorded U+00A0
  duplicate-listing shape at family scale, and with **no invisible character to blame** &mdash;
  here the two SKUs differ by a real `SF-` prefix, so the whitespace mechanism could never find
  it. **The mechanism that does is: strip a known reseller prefix and ask whether the bare number
  is also a SKU.**
- **A DEFECT CLASS THAT PASSES THE NON-ASCII AUDIT BECAUSE THE CORRUPTION DESTROYED THE
  EVIDENCE.** The `??` in that title is not punctuation &mdash; it is where `3/4&quot;` used to
  be, two non-ASCII characters (probably a vulgar fraction and an inch mark) replaced by literal
  question marks at import. Scanned live: **14 titles contain a literal `?`, and not one is a
  real question mark.** An em dash in four Edwards `4-CAB`/`4-FWAL1` titles, a degree sign in
  Modulaser `CM10906` (*&quot;Sweeping 90? Elbow&quot;*), an inch mark in Edwards `CM10941`
  (*&quot;3/8? Quick Connects&quot;*), `&le;` in five Comba couplers (*&quot;PIM: ?-161dBc&quot;*),
  `&reg;` in Fireray `FW-FAST` (*&quot;AutoCAD? Reader&quot;*), and one unidentified in Aiphone
  `TB-SE` (*&quot;TC?M Series&quot;*).
  **This file records the non-ASCII title count as 46 and falling, clean for five sweeps. That
  audit is correct and it is blind here, because `?` IS ASCII** &mdash; the corruption did not
  mangle the character into another non-ASCII byte the way `868STRC-AQ` did, it **deleted** it.
  So a scan for the wrong value cannot see a defect that replaced the value with a legal one.
  That is the same shape as the photo placeholder census, where asking *is there an image* could
  not see *is the image of this product*; and the same as the SKU corruption found two entries
  above, where a defect known in one field was never looked for in another. **Third instance in
  three days of a scan being defined by the artefact it was first found in.**
  **Only `RP2226` was corrected, and the other thirteen deliberately were not.** Its replacement
  is Edwards' own row, so the new title asserts nothing new: `Edwards RP2226 Test Point for 3/4
  in. Air Sampling Pipe, CPVC and ABS`. The other thirteen would each need their own source
  &mdash; the `Ten-Xone` rule, that repairing an obvious typo is still writing a claim &mdash;
  and the cheap fix for all of them is a re-import with the right encoding, not thirteen research
  tasks. Flagged.

- **`SIGA-GRD` is louvered sheet steel, not a wire guard (v2b52).** `E85001-1005` Issue 1.1 (coordinator-verified): *&quot;16-gauge steel louvered construction&quot;*, 7.27 in. diameter, listed detectors SIGA-PD/PCD/PCD-CA/COD/COD-CA and bases SIGA-SB/RB/IB (columns by word coordinates); &quot;wire&quot; appears **zero times**. The live title's &quot;Wire Guard&quot; was unsourced and the product type wrong in kind. Sold as the guard only; `SIGA-DGSB` surface adapter and `SIGA-DGMF` flange are separate. Route: the `/lifelines/intelligent-initiating-devices` percent-encoded JSON gave the PublicMedia slug directly.

- **`721UT` (v2b52):** legacy sheet `E85001-0598 -- 700 Series Self-Diagnostic Smoke Detectors.pdf` and its K twin still serve from myeddie `/PublicMedia/Catalog Sheets/` though absent from LifeLines and the Kidde API (slug built from a searched number + title; bogus control = 1,245 B 404). Heat Sensor Ratings (721UT, 713-5U): fixed 135 &deg;F, RoR 15 &deg;F/min above 105 &deg;F (coordinator-verified). Head only; needs a six-terminal base (702U) per UTC install sheet `13083-EN Rev J`, mirrors only (cdn.thefirepanel.com, locksandsafes), imprint-verified. **E85001-0598's own compatibility table omits the 721UT.** `K85001-0598` adds 741UT to the heat row though 741UT is not in its own ordering table. Standby current, temperature range, sensitivity, wire gauge and reset time disagree between the two documents &mdash; none published.

- **`?` in EST4 door titles is a lost en dash (audit t01):** `4-CAB24DR` and `4-CAB24DL` both came from one import of Edwards ordering strings. E85014-0004 Issue 2.3 p5 (6,758,602 B on myeddie, coordinator-verified): *&quot;4-CAB24DR Door Assembly &ndash; Red outer door and black inner door with 24 user interface spaces, mounts to 3-CAB14B wallbox&quot;*. The title was not truncated.

- **3-EVDVR vs 3-EVDVRA are parallel, not a supersession (audit t02).** E85010-0069 Issue 1.1 p4 (coordinator-verified): `3-EVDVR LED/SWITCH Driver Module, For EDWARDS Graphics` and `3-EVDVRA ... Assembly for Third-party Graphics`, both current. The live title's &quot;discontinued, USE 3-EVDVRA&quot; would send a buyer with Edwards graphics to the wrong part. &quot;ENVOY&quot; appears only on resellers. `/lifelines/whats-new` now 404s at 17,844 B.

- **4-CAB24DL (audit t03):** E85014-0004 Issue 2.3 p5: *&quot;Metallic bronze outer door and black inner door &hellip; mounts to 3-CAB21B wallbox, 65.0 lb&quot;* &mdash; a different wallbox from 4-CAB24DR's 3-CAB14B. The `L` is undecoded in the document, so the store's &quot;Long&quot; on 4-CAB24DRL is unsourced. The four EU `-E` doors are vendored &quot;Fireray&quot; (flagged). Page 2: backboxes, doors and chassis are &quot;ordered and shipped separately&quot;.

- **`WG4WF-SVMCEWGSVMWF` is two catalogue numbers welded into one SKU (audit t04):** WG4WF-SVMC = legacy Genesis WG4 speaker-strobe 15/29/70/87 cd (K85001-0626, Kidde imprint, **WG4 numbers with no E** &mdash; the E-inside-the-series-code rule holds for the Genesis LED generation, not WG4); EWGSVMWF = Genesis LED outdoor extended-candela speaker-strobe 15/30/75/115 cd (K85001-1056). Neither states a replacement. Title null; SKU flagged to EWGSVMWF.

- **(enrichment e02)** `E85005-0128 -- R-Series Remote Annunciators` Issue 1.1 still serves from myeddie /PublicMedia/ though absent from LifeLines; it is the only first-party sheet for the non-`-2` R-Series and the Dec 2025 EST3X Submittal Guide still cites it (coordinator-verified row: *&quot;RLCD-CR LCD text annunciator with common controls. English. Red.&quot;*). Its features table puts RLCD first and its spec table RLCD-C first &mdash; the K85005-0129 two-column-order trap again. **MN-FVPN is hardware** (E85010-0143 under `/lifelines/incident-management-platform/`), briefed as a licence &mdash; wrong; p4 contradicts itself on size. **4-2ANN** (E85014-0003 Issue 3.1 p7): ships with 4-LCDANN, 4-ANNCPU, bronze outer and black inner door; 4-2ANNMT wallbox and 4-NET SFP controllers separate &mdash; the live title had been cut at &quot;Order Wallbox&quot;. Kidde literature API category &quot;Annunciation&quot; is valid.

### e03 (23 Sep 2026): Kidde Genesis LED EGC and WG4 outdoor, ad-candidate lot

- **EGCVRF / EGCAVWN (K85001-1021 Issue 1.1, ©2025).** The document contradicts itself on mounting. Page 2 says "UL 1971-listed for use indoors as ceiling-mounted"; pages 2 and 4 say "listed to be both wall mounted or ceiling mounted". Nothing settled it, so the copy claims ceiling only. Kidde Issue 1.1 names **GP10 or GSRW-10** as the required room-side plate, included with the Kidde device. Edwards E85001-1021 Issue 1.2 lists only GP10, sold separately. The E/K carton split holds on the current issue. Strobe current is 35 mA VDC / 45 mA VFWR at every candela setting (p3 render).
- **WG4 speakers vs horns: two sheets, two temperature floors.** K85001-0626 (speakers) gives -31 °F; K85001-0628 (horns and strobes) gives -40 °F. Use each figure only for its own part. WG4 numbers carry no `E` in the Kidde imprint. There is no GP10 plate in this line.
- **WG4 suffix, from pairing across sheets rather than a syntax block:** `-HVMC` = standard candela and `-HVMHC` = high candela; in 0626, `-SVMC` = clear lens and `-SVMA` = amber lens. So the final `C` reads as the clear lens and the `H` before it as high output. The older note "HC = high candela" is only half right. This decode is by pairing only, so it stays out of copy.
- **WG4WN-HVMC candela is conditional:** 15/29/70/87 cd indoor (UL 1971), 6/12/28/35 cd outdoor at -35 °C (UL 1638), 1/3/8/10 cd CAN/ULC-S526 at -40 °C. UL rates current at 16 V (127–351 mA); the copy gives the 24 VDC figures (107–238 mA) and labels them.
- The sibling WG4WN-S is ARCHIVED in the store.

### e06 (23 Sep 2026): EC2-SB and SD-T78

- **EC2-SB:** E85001-0599 Issue 1.2 p2, "Standard base, 4 terminals, 4" dia.". The 4 in. is the base diameter, not the box size; the coordinator's suspicion was wrong. There is no EC2 installation sheet on LifeLines (`/lifelines/conventional-initiating-devices` lists catalogue sheets only).
- **SD-T78:** K85001-0326 Issue 1, "78 inch (1980mm) Air Sampling Inlet Tube". It also appears in -0583, -0584, -0585 and -2006. **Ship weight disagrees across Kidde sheets (2.2, 4.1 and 7.5 lb)**, so it was left out. K85001-2006 misprints the row as "SD-T78 8-inch", a dropped digit shown by the part number, 1980 mm and the shared 7.5 lb; its pages carry both "E85001-2006 Issue 1" and "K85001-2006 ISSUE 1.1" headers. `K85001-2005` 404s at 1,245 B although the Kidde API lists it (PrivateMedia).
- e07 (23 Sep): **WG4WA-S** is in K85001-0626 Issue 1.1 p4 under **ECS/MNS Appliances**: White, ALERT, Speaker Only (merged cells, confirmed on a render). "ALERT Marking" went into the title. The Edwards E85001-0626 accessories add the 449 gray box, which the Kidde issue lacks. The store's 74347U title says "Red", but the sheet gives no colour (queued).
