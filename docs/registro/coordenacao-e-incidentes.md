<!-- Registro de casos do projeto TFAS. Movido VERBATIM de CLAUDE.md em 23 Sep 2026; nada foi reescrito. Nao e carregado automaticamente: leia sob demanda. E cronologico: entradas posteriores corrigem anteriores; em caso de conflito vale a mais recente e o nucleo em CLAUDE.md. -->

# coordenacao-e-incidentes

- **Heat detectors have three classes, not two.** Fixed temperature and rate of rise
  are the obvious pair; **rate compensation** is the third and a whole product line is
  built on it. A high-expansion shell encases slower struts carrying opposing
  contacts, so on a fast rise the shell lengthens first and the contacts close *below*
  the rating, cancelling thermal lag &mdash; and it self-restores on cooling. A
  briefing that offers only "fixed or rate-of-rise" will push an agent toward the
  wrong answer; Thermotech's `302-ET-135` is rate compensation and neither of those.
- **The coordinator may tighten or soften agent copy, but must not introduce a new
  factual claim without agent-grade research.** Every inline edit made during
  publishing on 21 Sep 2026 was checked afterwards. The ones that restated an agent's
  sourced finding, or that made a claim *weaker* (keeping a catalogue number in
  parentheses rather than promoting it, softening an inferred bracket claim, restoring
  a `/U` suffix), were all sound. **Both edits that went wrong were the two where the
  coordinator supplied the substance** &mdash; the RA100Z rewrite and the THM04R3000
  swap. The pattern is clean enough to be a rule.
- **DITEK: the coordinator's `-R5`/`-R8` filename premise was invented, and the host has
  a fingerprint.** `DTK-2MHLPF-Series-DS-R5.pdf` and every `R4`&ndash;`R9` variant return
  **HTTP 404 with an HTML shell of exactly 152,678 bytes** &mdash; a new stable failure
  signature for `diteksurgeprotection.com`. Real filenames carry no revision at all and
  are linked from the **series page**, and the current revisions are **Rev 6 and Rev 19**,
  not 5 and 8. What the documents do settle decisively: `DTK-2MHLP24FWB` (F) and
  `DTK-2MHLP75BWB` (B) are identical on service voltage, MCOV, clamping voltage and the
  20,000 A surge rating and differ in **exactly two rows** &mdash; max continuous current
  **1 A against 5 A**, and failure mode **open circuit against short to ground**. And
  **`WB` is manufacturer-stated**: *&quot;includes single position mounting base&quot;*.
- **Ninth coordinator premise wrong, and the agent's handling of it is the model.**
  The briefing called `FSL-E3` a &quot;fiber SLC/loop module&quot;. `9021-60783` Rev F
  makes it an **ARCNET network module** &mdash; one transmit or receive channel for the
  `RPT-E3-UTP` repeater and INI-VG voice gateways, not an SLC device-loop card. But the
  agent did **not** rewrite the class noun out of the title, because
  **the document is itself titled &quot;FML-E3/FSL-E3 Fiber Loop Modules&quot;** &mdash;
  that *is* the manufacturer's product name, which house convention explicitly permits.
  It kept the name in the title, put *&quot;This is a network card, not an SLC device
  loop card&quot;* as the second sentence of the body, and flagged the `type` to the
  owner. **That is the right shape for every case where the manufacturer's own name is
  the confusing thing** &mdash; the opposite handling from `CPU2-3030D`, where the
  manufacturer's &quot;Primary Display&quot; wording was allowed to set the title and
  misled. Fiber mode settled positively for the exact part: single-mode, 9/125 &micro;m,
  LC, 30 dB, 0.079 A, against FML-E3's multi-mode, 62.5/125, ST, 8 dB, 0.053 A.
- **A lossy slice file silently disarms the catalogue's best cross-check, and both
  agents will report the loss as a fact about the catalogue.** Building v2b13 from the
  revenue CSV, the coordinator wrote `'type': ''` into every `aN_in.json` because that
  CSV did not carry the field. Two agents then reported, as a finding, that all their
  products had an empty Shopify `type`. **Only 1 of the 264 is actually empty, and
  catalogue-wide only 52 of 16,031 (0.3%).** The agents were reporting the input file,
  faithfully. This is the hand-transcribed-id failure in a new shape: **a briefing that
  is wrong in a *blank* is harder to catch than one wrong in a value**, because nobody
  disputes a blank.
  It cost real signal. Restoring the field and re-reading the 18 products against the
  agents' own class conclusions immediately produced **two disagreements, both real**
  &mdash; `HONBDA-7S27B-IB-10` and `OSE-HPW` below. **The rule: any slice file must be
  built from `catalogo_full.json`, carrying `type` and `handle` verbatim; never
  default a field the agents are asked to reason about.**
- **`DACT-UD2` was typed &quot;Cellular Communicators&quot; and reports over telephone
  lines.** Manual `53037:B` &sect;1: *&quot;transmits system status to UL listed Central
  Station Receivers via the public switched telephone network&quot;*; two modular phone
  jacks, RJ31X, REN 0.0B, FCC Part 68, **no radio in the product at all**. DACT stands
  for Digital Alarm Communicator/Transmitter. The briefing predicted this from the
  acronym alone and the document confirmed it &mdash; **an expansion of the part's own
  initialism is a free class check worth running before any fetch.**
- **The Windsor `google_ads` connector serves TWO businesses, and a query without an
  account filter silently blends them.** `151-468-5549` is **TFAS SHOPIFY**;
  `192-200-0533` is **The House Supplier**, a heating-supplies business. Earlier work
  in this file correctly scoped to `151-468-5549`; a query on 22 Sep dropped the filter
  and returned both, and the coordinator read a House Supplier Shopping campaign
  (`SHOPPING GABRIEL 8-3-2026`) as if it were TFAS's, complete with a recommendation
  built on it. **The owner caught it.** It is the same shape as auditing against the
  stale snapshot: measuring the wrong artefact, confidently, and reporting a
  conclusion from it. **Always pass `accounts: [&quot;151-468-5549&quot;]`.**
- **So the 264 go into a dedicated PMax, and the coordinator's own argument against
  that was wrong.** The objection recorded earlier was *&quot;a second PMax asks the
  same algorithm the same question&quot;*. **It is not the same question.** The
  incumbent campaign was asked *&quot;where do I spend $100k across 16,031
  products?&quot;* and with 16,000 better-signal alternatives it never reached these
  264 &mdash; which is precisely why they show zero spend in twelve months. A campaign
  filtered to those 264 and nothing else asks *&quot;spend this budget here&quot;*, and
  **with no alternative inventory the algorithm has nowhere else to go.** That is the
  mechanism the `custom_label_0` asset group exists to create.
  Still required: **exclude the same 264 from the incumbent PMax** by listing group, so
  the measurement stays clean if it ever does start bidding on them. And the
  **$500/day the owner chose is defensible for PMax** in a way it would not be for
  Shopping &mdash; PMax needs conversion volume to leave learning, and starving the
  budget is its own failure mode. Two to three weeks with no tROAS, then set one.
- **The coordinator typed product ids from memory into a live query, one batch after
  writing the rule against it.** Building v2b22, the slice file was already on disk with
  every id in it, and the ids that went into the Shopify query were **invented** &mdash;
  seven of eight returned `null` and the eighth returned a completely unrelated product
  (`G1TW`, a trim ring). Nothing was written, because it was a read.
  **The near-miss is the point.** Had that been a publish rather than a query, one real
  product would have received another product's copy, silently, exactly as in the v2b03
  briefing incident. The existing rule says *never hand-transcribe an id into a
  briefing*; this shows the rule is too narrow. **Never type an id anywhere &mdash;
  briefing, query, mutation or note. Read it from the file, every time, even when the
  file is open and the id feels familiar.** The cost of reading it is one command.
- **The coordinator compressed a nuanced agent finding into a flat rule, and the flat
  rule was wrong for the very next instance. This is the lossy-slice-file failure moved
  into prose.** A v2b20 agent reported, correctly and completely, that the Simplex
  `2099-` series is the **non-coded manual station line** and that releasing stations are
  **one data sheet inside it**, `S2099-0010`. Writing the next briefing, the coordinator
  compressed that to *&quot;`2099-` is the non-coded manual pull station line, **not** a
  releasing line&quot;* &mdash; dropping the exception. The next `2099-` part to come
  through, `2099-9149`, **is in `S2099-0010`**: *&quot;Non-Coded Manual Stations for
  Releasing Applications&quot;*, Table 1, UL 38 listed for releasing service, and absent
  from `S2099-0007` entirely.
  **So it is a product-class error in a feed title** &mdash; a release station sold as a
  pull station &mdash; and the `type` field said **Pull Stations** and agreed with the
  wrong title, raising nothing. That is the recurring signature again.
  **And it is the incomplete-product trap for the eighth time:** the sheet says *&quot;a
  blank area on the front of the station allows the selection of a label&hellip; (label
  kit is ordered separately)&quot;* and Table 1 notes **&quot;requires label kit
  4099-9802&quot;** &mdash; six labels covering clean agent, extinguishing, CO&#8322;, foam,
  sprinkler and manual. At $38 the buyer receives an unmarked releasing station. This is
  the `4099-9015` case almost exactly, one series over.
  A third thing the compression would have cost: the coordinator asked the agent to diff
  against `2099-9803`, the replacement **breakglass** published the day before. Wrong
  accessory &mdash; `2099-9149` is a **break-rod** station and takes `2099-9804`. Acting
  on the briefing would have cross-sold the wrong part.
  **The rule: when an agent's finding carries an exception, carry the exception.** A
  summary that drops the &quot;except&quot; is not a shorter version of the finding, it is
  a different and false one &mdash; and it is harder to catch than a wrong value, because
  it reads as a clean general rule.
- **The coordinator's scepticism was the error again, for the second time.** A briefing
  flagged the live `TH4210U2002/U` stage claim &mdash; *&quot;up to 2 Heat/1 Cool heat
  pumps; up to 1 Heat/1 Cool conventional&quot;* &mdash; as the kind of claim that is
  usually wrong. **Two independent Resideo documents confirm it**, submittal
  `33-00285----04` and the `03-00306` comparison chart, and the only thing the live copy
  had omitted was the qualifier *with electric aux heat*. That is the `ATD-L3R-IV` shape
  exactly: **&quot;that kind of claim is usually wrong&quot; is a prior, not evidence, and
  it has to lose to a document like any other prior.** Worth stating as a count now: twice
  the coordinator has predicted a live claim was wrong and twice the page was right.
- **Fourteenth product-class error, and the first where a listing code explained an
  apparent nonsense in the title.** `49AV-WWFO-BA` asserts **15/75/WP75/WP185 cd**, which
  reads as a broken candela ladder with 75 appearing twice. It is not: **15 and 75 cd are
  the UL 1971 settings and WP75 and WP185 are the UL 1638 settings**, two listings on one
  appliance with **different temperature ranges** (32 to 120 &deg;F against &minus;31 to
  150 &deg;F) and different humidity limits. 75 cd appears twice because it is rated twice.
  **Every element of that title checked out.** Generalises: a candela set that looks
  malformed may be two listings concatenated, and the temperature ranges are the tell.
  Two routing corrections came with it. The part is **not** in `S49AV-0001` and **not** in
  the `S4906-0001` family the briefing pointed at; the weatherproof wall models are in
  **`S49WP-0001-5`**, and `S49WP-0002` is the parallel **ULC** document with a *different*
  candela set (20/30/75) &mdash; so mixing the two would attribute a ULC figure to a UL
  model. Wrong document family again, and the `-BA` suffix is confirmed a second time as
  **assembled in the USA**.
- **A number inside a model number can look like a spec and be denied by the
  manufacturer in the same document. New shape, and the strongest title defect yet.**
  `AS-75-R-WP` was titled *&quot;AS Horn 75CD Red Weatherproof&quot;*. Siemens Data Sheet
  2578 (Rev. 5, Sept 2015), read directly by the coordinator, carries **Note 1 verbatim:
  &quot;Models AS-75-WP and AS-75-R-WP do not provide a 75cd setting.&quot;** Note 2 gives
  the real ratings &mdash; **115 cd per UL 1638 outdoor and 30 cd per UL 1971 indoor**
  &mdash; and the ratings table row agrees (115 | 30/180 | 30).
  **The document contradicts itself and the note wins**: the ordering row does read
  &quot;AS Horn | Strobe: 75CD Weatherproof, Red&quot;, which is the shorthand the store
  title inherited, while the note on the same page denies it and the ratings table
  corroborates the note. Two signals against one piece of shorthand.
  **So the `75` is a series designator, not a candela value**, and the live title was
  asserting a setting that does not exist, in a Merchant Center feed attribute, on a
  product where candela is exactly what a specifier filters by.
  **Fifteenth product-class error came free with it:** the sheet is headed *&quot;AS &amp;
  AH &mdash; **Audible Horn | Strobe** / Audible Horn Appliances&quot;*, so **AS is the
  horn-strobe line and AH is the horn-only line**. The title said Horn and the `type` says
  Horns, agreeing with the wrong title and raising nothing &mdash; the signature again.
  **Generalises: when a title's number matches a fragment of the model number, check
  whether it is a spec at all.** The briefing had already flagged &quot;a horn has no
  candela&quot; as a class question; the answer turned out to be both that *and* a
  phantom figure.
- **Plain extraction can emit two tables in the wrong order, so the CAPTIONS attach to
  the wrong bodies.** On `TD450157EN` page 3, `get_text()` hands back &quot;Table 2.
  Strobe Ratings&quot; joined to the ELHS/ELHNC body and &quot;Table 3. Horn-Strobe,
  Current Ratings&quot; joined to the ELST/ELSTC body &mdash; the two swapped. Word
  coordinates show the ELST table physically **above** the ELHS one, and a 220 dpi render
  settles it. **Anyone trusting plain text would have read strobe currents out of the
  horn-strobe table**, and would have concluded the briefing's warning about that table
  was wrong.
  This is the caption-below-its-table trap (`9021-60930`) one level up: there a caption
  attached to the wrong table *within* reading order, here two whole tables are
  interleaved. Same remedy, same rule &mdash; **never take a caption-to-body assignment
  from reading order alone.**
- **The owed `P85756F` verification is NOT discharged, and saying so is the point.**
  A v2b27 agent reported it as discharged, having read the **wall** sheet `P85750D` and
  found Note 5 verbatim. But the published `ELSTWC-ALA` sentence cites the **ceiling**
  sheet `P85756F`, and this file already recorded that the note appears word for word in
  the wall sheet &mdash; so the agent independently re-confirmed a fact already on record
  rather than the one outstanding. **That is genuine corroboration** (two independent
  readers now on `P85750D`, and &quot;private&quot; still appears zero times in it) and it
  raises confidence, but the document the copy cites remains unread by anyone but its
  original agent. The coordinator's own attempt failed: four constructed
  `eaton.com/.../eluxa/` paths for `P85756F` all returned HTTP 404 &mdash; **find the
  slug, do not build it**, again. Debt stands.
- **A search-engine result is not evidence about the catalogue, and it cost one query to
  prove.** A v2b26 agent flagged what looked like **duplicate product pages** &mdash;
  `/products/bb-55f` alongside `/products/fire-lite-bb-55f-battery-box`, and
  `/products/notifier-dp-disp2` alongside `/products/notifier-dp-disp2-dress-plate`
  &mdash; and correctly told the coordinator to verify live rather than against a
  snapshot. **Both short handles return `null`**: `productByIdentifier` finds neither,
  and a product search returns exactly one active SKU each. The URLs exist only in a
  search index. **That is the snapshot rule with a new artefact in the slot**: a search
  result is a cache of something that may never have been current, and it is one degree
  staler than the snapshot this file already warns about. The agent's handling was right
  &mdash; flag it, do not act on it &mdash; and the check cost one query.
- **THE `P85756F` DEBT IS DISCHARGED, and the coordinator read it directly.** This file
  has carried an outstanding verification since v2b22: the `ELSTWC-ALA` copy cites Note 5
  of Eaton ceiling installation sheet `P85756F`, and no one but its original agent had
  read that document. **A v2b27 agent found the slug by search** &mdash;
  `eaton.com/content/dam/.../eluxa/eaton-eluxa-installation-instructions-p85756f-elhsc-clear-amber-lens.pdf`
  &mdash; and the coordinator then fetched it independently: **859,067 bytes,
  `application/pdf`, 2 pages.** Item 5 of its sheet-level `NOTES:` block reads verbatim
  ***&quot;Amber strobes are not to be used as a Visual Public Mode alarm notification
  appliance.&quot;*** and **&quot;private&quot; and &quot;Private&quot; each appear zero
  times**, so the published sentence &mdash; which states the prohibition and adds that
  no document states the complement &mdash; stands exactly as written.
  **Note what closed it: a search, not a construction.** The coordinator's four attempts
  to build the path all returned HTTP 404. This is the fifth or sixth time on this project
  that *find the slug, do not build it* has been the difference between a document and a
  dead end.
- **Twelfth coordinator premise wrong, and it breaks a signature this file had been
  treating as reliable.** The `4100-9706` briefing flagged its live sentence &mdash;
  *&quot;Same as 4100-9701 above except with Color ES Touchscreen Display user
  interface&quot;* &mdash; as **copy borrowed from an adjacent catalogue row**, the tell
  recorded three times here (`PAD200-DD`, `4-NET-SM`, `INX-10A`). It is not borrowed.
  **It is Simplex's own Table 8 row for this exact model**, almost word for word, in
  `S4100-1031 Rev. 22`.
  **So the borrowed-copy signature has a false positive, and it is a common one: a
  manufacturer catalogue that itself writes rows as &quot;same as the one above,
  except&quot;.** Every previous instance was a store page carrying a *sibling's* text;
  here the store faithfully carried the *manufacturer's* text about the right part. The
  discriminator is not the phrasing &mdash; it is **whose row it is**, which only the
  ordering table answers. The real defect left is small and different in kind: **the word
  &quot;above&quot; dangles** on a product page where `4100-9701` does not appear.
  Worth pairing with the outcome on the class question: `4100-9706` **is** the 4100ES
  Master Controller, and its `type` of Control Panels is correct &mdash; so this page
  does *not* repeat the `4100-9701` error where the same controller was typed
  &quot;Annunciators&quot;. The premise was wrong twice over.
- **The coordinator fed an agent a placeholder in a field it was asked to reason about,
  and the agent caught it. Third instance of the lossy-slice-file failure.** Building
  `foto01`, `2500-PWR24U` already had good published copy, so its `live_desc` was written
  as the literal string *&quot;[ja enriquecida no v2b25 - copia completa presente. FALTA
  SO A FOTO.]&quot;*. The agent echoed it back verbatim, **flagged it, and told the
  coordinator not to publish that description** &mdash; which is exactly right and is what
  stopped a live page being overwritten with a note to self. The recorded rule was
  *never default a field the agents are asked to reason about*; this adds that **a
  human-readable note is a default too**, and a more dangerous one than a blank, because
  it looks deliberate.
- **The series-wide-block trap again, and this time a web summary repeated the wrong figure
  for the specific part.** `E85010-0130`'s page-1 feature bullet reads *&quot;Supports up
  to 250 intelligent Signature detectors and 250 Intelligent Signature Modules&quot;* &mdash;
  that is the **two-circuit** figure belonging to the `3-SDDC2`, while the model-attributed
  specifications table gives **125 detectors and 125 module addresses per 3-SDC1 card**.
  Confirmed by the coordinator in the same fetch. **And the briefing's hypothesis was wrong
  in the safe direction:** the live sentence *&quot;Comes with one 3-SDC1 Device Card&quot;*
  is **verbatim** Edwards Ordering Information for the `3-SSDC2`, so the page was right and
  the danger was the headline nobody had questioned.
- **`X-WP-Total` over-reports what a WordPress media API will actually serve**, measured on
  four hosts: power-sonic claims 2,035 and yields **1,766**; apcfire 536 &rarr; 499; macurco
  1,664 &rarr; 1,633; det-tronics 801 &rarr; 786. Re-paginating under three different
  `orderby`/`order` combinations recovered **zero** extra items, so those are ceilings, not
  pagination bugs. Do not treat the header as a completeness target.
  Related, and it cost a briefing: **the vendor string is two words on some brands**, so
  &quot;the SKU is the second whitespace token&quot; returns `Sonic` on 232 of 232 Power
  Sonic titles. **`catalogo_full.json` carries a real `sku` field** &mdash; join on `id` and
  use it. It also carries the variant (`PS-1290 F2`, `CX-12-CO LADBS`), which is exactly
  what the terminal-type and housing-colour rejections above turn on.
- **A voltage in a live title that the manufacturer does not make, and the mechanism is a
  typo in ONE line of ONE revision that every distributor copied.** `90215A-801-06-L`
  ($2,657) was titled *&quot;Distributed Audio (25/70/**200V**)&quot;*. HyperSpike's
  Installation and Mounting Manual `98030A-MAN-TCPA10 Rev G`, **downloaded and read
  directly by the coordinator**, says *&quot;five field-selectable power taps that run off
  of **25 V, 70 V, and 100 VRMS** audio systems&quot;* &mdash; and the string `200` appears
  **zero times in its fourteen pages**. In spec sheet `TCPA-10 SS Rev. F` it appears
  **exactly once**, in the model-syntax line, against **five** places saying 100 V: the Key
  Features bullet, the A&amp;E paragraph, the tap-table column headings and the sound-output
  table, whose own columns read *Watts @ 25V / @ 70V / @ 100V*.
  **This is the stale-figure rule with a new origin.** The recorded cases are prose carried
  over from a superseded revision (Eaton's 87 dB) and an A&amp;E paragraph quoting the wrong
  row (Gentex's amber current). Here it is **one field of a model-number syntax block**,
  which is the very thing this file elsewhere calls the best decoder there is. A syntax
  block decodes reliably and is not thereby immune to a typo &mdash; **cross-check its
  fields against the spec tables like any other prose.** The same title also carried an
  orphan word **&quot;ohm&quot; with no number**; it is 8 ohm, stated in the syntax block
  and the A&amp;E paragraph together.
- **THIRD instance of the coordinator briefing a description defect as a title defect, and
  this file already records the rule against it.** The `HCWL-LF` briefing said *&quot;the
  live title lists candela values&quot;*. It does not: the title is
  *&quot;System Sensor HCWL-LF Low-Frequency Compact Sounder&quot;* and the candela list
  sits in the description `<h2>`, which the agent saw because **`aN_in.json` carries both
  fields and the prose only claimed one**. The recorded rule is *&quot;say which field a
  defect is in before sizing it&quot;*, written after making this same error twice in one
  batch. **Writing a rule down does not stop it recurring; the input file is what stopped
  it**, which is the whole argument for the slice file being the authority.
  **And the real title defect was a different one.** `9021-62013:C`, read directly by the
  coordinator, gives `HCWL-LF&dagger;: Low frequency sounder, **ceiling**, white` against
  `HGWL-LF&dagger;: **Compact** low frequency sounder, **wall**`. So **&quot;Compact&quot;
  in the live title is the sibling's attribute** &mdash; and that sibling is a *wall*
  device, so the one word imported the wrong form factor and the wrong mounting at once.
  `C` is ceiling and `W` is white, confirming the title's &quot;Ceiling&quot; was right all
  along.
  **The candela list is the wall sounder-strobe row on a device with no strobe.** The same
  sheet's A/E section splits them: *&quot;Wall units: 15, 30, 75, 95, 110, 135, and 185.
  Ceiling units: 15, 30, 75, 95, 115, 150, and 177.&quot;* The live description carried the
  **wall** set, on a **ceiling** part, that is a **sounder only**. Three errors in one
  string, and the corrupt `95,N110` inside it was merely the visible one.
  A document defect found and not published from: that sheet's page-1 feature bullets call
  `HGRL-LF`/`HGWL-LF` *&quot;Compact **ceiling**-mount sounders&quot;* while its own
  ordering block and dimension table make them **wall**, and the same bullet mangles the
  ceiling line as `HCRL-LF, HCWLA-LF, HCRL-LF, HCWLA-LF`, **omitting `HCWL-LF` entirely**.
  So the store's wrong word has an innocent origin in the manufacturer's own bullet.
- **A search endpoint that SILENTLY IGNORES THE QUERY, on a host whose sibling endpoint
  honours it &mdash; and it would have matched all 798 SKUs.** Verified by the coordinator:
  `hochikiamerica.com/ecom/productsearch?searchterm=` returns **143,192 bytes for `SLR`,
  143,192 for `ALK` and 143,216 for `ZZZQQQ999XX`** &mdash; the same 24 products for every
  term, real or invented. The sibling route `/products-search?qs=` does honour it: 92,565
  bytes for a real term against **46,729 for the bogus one**.
  **The ignoring endpoint is the one the site's own product-search page links to**, which
  is what makes it dangerous. This is the JCI-hub *&quot;search is ignored, grep the
  blob&quot;* shape, except there the whole index came back and was useful; here a
  *truncated* list comes back and looks like a result.
  **And note precisely what catches it, because the obvious check does not.** The three
  responses have **different MD5s**, since the page echoes the search term &mdash; so
  hashing the bogus control against a real one says &quot;different, therefore the query
  works&quot;. What gives it away is the **byte count being near-constant across a real and
  an invented term**, and the product list being identical. **A bogus-query control must
  compare what came back, not whether the bytes differ.**
- **The coordinator's scepticism was the error for the THIRD time, and this one was an
  agent catching itself.** A Mircom file named `FX-400R_front_sm.jpg` shows a panel
  **silkscreened &quot;3318&quot;**, and mircom.com's own FX-3318 page shows the same
  faceplate &mdash; the exact shape of the Power-Sonic `PGFT-12V180.jpg` / `FT-12V160`
  case, where a manufacturer filename named one product over a photograph of another.
  It is not that. Datasheet **`CAT-5981`** embeds this exact red panel on page 1 while
  page 5 reads `FX-400R &mdash; Addressable Fire Alarm Control Panel - Red door`:
  **3318 is the shared display-bezel designation of the RAM-3318-LCD family, not a panel
  model.** *&quot;That kind of claim is usually wrong&quot; is a prior, not evidence* —
  and a document, not a suspicion, settled it. Third instance.
- **Two releasing-gear parts in a row that were NOT mis-merchandised, which is worth
  recording because the pattern was four for four.** `4004-9302`'s live title already
  said &quot;Basic Releasing Panel&quot; and Simplex's own document is titled *&quot;4004R
  Suppression Releasing Panel&quot;*. The coordinator's hypothesis &mdash; that
  &quot;Basic&quot; hid a label-kit equivalent, as on `4099-9015` and `2099-9149` &mdash;
  was **half right in a more useful way**: there is no label kit, and what is missing is
  **two 12 V batteries, a 2081-9046 coil supervision module required one per releasing
  circuit, and a maintenance switch required per circuit under NFPA 72**. Table 1 never
  says what &quot;Basic&quot; excludes and there is no non-basic model in it, so the word
  was kept and nothing inferred from it.
- **Yellow is NOT the release-station colour, and the manufacturer says so in words.**
  The briefing warned that `SG-WP-YL` might be a release station, since yellow is the
  release convention this catalogue has flagged before on `RMS-1T-WP YELLOW`. SigCom's
  own sheet states: *&quot;There is no agency standard, outside of red for fire, that
  dictates what color is to be used for a specific application.&quot;* Its yellow labels
  span HAZMAT, EVACUATE, MEDICAL, TORNADO, DOOR RELEASE, FOAM **and** a release set. So
  the colour carries no class information at all, and the part is a **weatherproof cast
  metal back box** for SG-42 stations. **The warning still earned its place &mdash; it
  forced the check &mdash; but the convention it rested on is not a convention.**
- **An ERP assembly prefix read as a product attribute, and the correction is a positive
  one.** `SLM-318`'s title is the raw ERP string *&quot;Assembly, FNL, Loop Card,
  CLP&quot;*, and the briefing guessed `FNL` was a panel family and `CLP` a protocol.
  **`FNL` appears zero times in three Honeywell documents** and turns up on the entirely
  unrelated `NFN-GW-PC-HNSF` gateway (*&quot;Assy, FNL, HS NFN GW SGL, Fiber&quot;*), so
  it is a Honeywell ERP token. **`CLP` is settled positively**: `HON-62115:A`'s footnote
  reads *&quot;SLM-318 version identifier is printed on the PC board: **CLP-PCB or
  CLP2-PCB**&quot;* &mdash; the protocols are FlashScan and CLIP, and CLP names the board.
  **That distinction is not academic: the two boards carry different self-test loop
  limits** (CLP-PCB 7,200/4,500/2,800/1,800 ft at 23 &#937;; CLP2-PCB
  11,000/6,900/4,350/2,700 ft at 35 &#937;). The agent published the CLP2 figures because
  that is what the current datasheet prints, and **refused to read the ERP token as a
  board revision** &mdash; correctly, since that would be a claim off an ERP string.
  Third instance of the raw-ERP-title shape after `010254-008` (&quot;DISPLAY, DCU&quot;)
  and `MX16RSF-US`'s &quot;SS&quot;.
- **A suffix-family list in my own briefing was wrong, and the agent corrected it from
  the ordering table.** I wrote that `-CLR-ALERT` is the amber alert model.
  `AVDS-62174:A` gives **`SPSWLED-ALERT` = AMBER lens** and **`SPSWLED-CLR-ALERT` =
  CLEAR lens** &mdash; `-CLR-` is the clear one, which is what the letters say once you
  read them. Worth recording because this file now carries several suffix decodes, and
  **a decode repeated from memory into a briefing is exactly the hand-transcription
  failure in a new field.**
- **SEVENTEENTH coordinator premise wrong, and it would have put a wrong capacity in a
  feed attribute on the one field a battery buyer filters by.** The briefing told an
  agent that on the Power-Sonic PDC line *&quot;the number is the 20-hour capacity&quot;*,
  generalising from two SKUs settled in an earlier batch. **Measured across all eleven
  datasheets, four diverge.** Verified directly by the coordinator on two of them:

  | model | number implies | 20-hr | 10-hr |
  |---|---|---|---|
  | `PDC-121300` | 130 | **128.0** | 120.0 |
  | `PDC-12480` | 48 | **45.4** | 43.2 |
  | `PDC-122000` | 200 | **215.0** | **200.0** |
  | `PDC-122500` | 250 | **265.0** | **250.0** |

  **On two of them the model number is the TEN-hour figure and the 20-hour capacity is
  15 Ah higher; on two it matches no rate at all.** Corroborating that the number is not
  a capacity: **`PHR-12400` is 113.8 Ah at 20 hr** &mdash; the same `12400` token, a
  different series, nothing like 40 or 400.
  **So this is the `AS-75-R-WP` shape on a whole product family**: a number inside a
  model number that looks like a spec. The instruction to state the rate in every title
  was right for a stronger reason than the one given &mdash; **it is not a nicety, it is
  the only way these titles can be correct**, because `PDC-122000` at 200 Ah and
  `PDC-121300` at 130 Ah are not comparable claims. The two 10-hour parts were published
  with **both** rates so a buyer who ordered expecting 200 Ah can see why the sheet says
  215.
- **A terminal-code taxonomy that enumerates codes and carries no semantics, and the
  correction to this file's own note.** Batch 5 recorded that Power-Sonic's
  `wp-json/wp/v2/ps_terminal_type` lists `U` with an **empty description**. True but
  understated: **all 29 descriptions are empty**, so the route confirms which codes are
  real and decodes none of them. **The datasheet drawing is the only decoder** &mdash;
  and it has no text layer, so all six codes here were read off **300 dpi renders**:
  `F2` Faston 0.250 &times; 0.032 in. tabs, `M5` T15 threaded insert 5 mm stud, `M6`
  threaded insert 12 mm body, `M8` labelled verbatim *&quot;T11 THREADED INSERT &mdash;
  8mm STUD&quot;*, `NB2` and `NB3` *&quot;TERMINAL POSTS with nut &amp; bolt
  connectors&quot;* on 14 and 16 mm plates. **`NB2`/`NB3` were a coordinator guess and
  are now manufacturer-confirmed.**
  **And batch 5's bounded negative on `U` can be closed**: the PDC-12600 sheet draws it
  &mdash; **tapered terminal posts with separate positive (17.4 mm) and negative
  (15.9 mm) profiles, torque 11.0&ndash;14.7 N&times;m.** Not &quot;universal&quot;.
- **Eighteenth coordinator premise wrong: `napcosecurity.com` DOES serve per-product
  PDFs.** The briefing said the brand's documents were reachable only through the open tag
  index at `tech.napcosecurity.com/techlibrary/tagresults/tag/<sku_underscored>` (titles
  only, PDFs behind a dealer login). **`napcosecurity.com/media/pdfs/<DOCNUM>-<slug>.pdf`
  serves them directly**, and its 404 is a stable **30,430-byte** fingerprint. The tag
  index is still the way to *find* the document number; it is not the only way to read the
  document.
- **A correction to this file that the coordinator could NOT reproduce, recorded as
  unsettled rather than accepted or rejected.** This file states that
  `cdn.power-sonic.com/documents/` returns HTTP 200 and **zero bytes for everything, real
  filenames included**. An agent reported that as wrong &mdash; that real names serve real
  PDFs and only a bogus name gives 0 bytes. The coordinator tested it and got **0 bytes and
  `inode/x-empty` for BOTH** a real-looking path and a bogus control.
  **That does not disprove the correction, and saying why is the point: the coordinator's
  probe used a CONSTRUCTED filename**, which is the exact thing this file says not to do.
  So the failure may be the path, not the host. **Neither the original note nor the
  correction is settled**, and the next person should test it with a slug found by search.
  Recording a failed reproduction as a failed reproduction, rather than as a result in
  either direction, is the honest form here.
- **The type field disagreed with the title and THE FIELD WON, which is the rule's other
  half finally firing.** `4906-9132` was titled a **speaker strobe** and typed **Horn
  Strobes**. Simplex `S4906-0010`, fetched and read directly by the coordinator, settles it
  three ways: the document's own title is *&quot;Weatherproof Notification Appliances
  (non-addressable) Wall Mount Visible Only (V/O) and **Audible/Visible (A/V)**&quot;*; its
  Table 1 row reads, by word coordinates, `4906-9132 | (A/V) | White | Red`; and page 3 heads
  a current block **&quot;A/V Models 4906-9131 and 4906-9132&quot;**. It is a horn strobe.
  **And the live title omitted &quot;weatherproof&quot;** &mdash; it is a **NEMA 3R** unit
  requiring a separate weatherproof box, so a buyer specifying an indoor appliance received
  an outdoor one needing a part they did not order. **Both defects sat in the Shopify
  `title`, so both cost two channels.**
  This file's rule is *&quot;the type field is a signal when it disagrees with the title and
  no evidence when it agrees&quot;*, and nine recorded cases are the type agreeing with a
  wrong title. **This is the first published case where it disagreed and was right**, which
  is what makes the rule worth keeping rather than a post-hoc excuse.
- **A candela split that is not wall-versus-ceiling but a letter in the model number.** The
  briefing assumed the 49VO ladder differed by mounting. `S49VOC-0001` Table 9 gives the
  **49VO** model 15/30/75/110 cd and the **49VOH** model 110/135/185 cd, **both ceiling
  mount, in one document** &mdash; so the `H` is the high-candela variant and the live
  title's ladder was already right. The index also returned `S49VOC-0002` for the same part;
  it contains the exact string **zero** times and its models are all weatherproof
  `49VOH-APPLC-O`, so the hit was a substring artefact. **A search hit on an index is not
  evidence the document contains the part.**- **THE COORDINATOR ALMOST STRIPPED A CORRECT, MANUFACTURER-STATED CLAIM OUT OF A TITLE
  BY READING HALF A TABLE HEADER.** Verifying `15271`'s title claim *&quot;Vehicle Bracket
  Included&quot;*, the coordinator pulled Amerex's *Fire Extinguishers at a Glance* sheet,
  read the header row by coordinates, and got `TYPE | (CAPACITY) | MODEL | (INCH) |
  BRACKET | BRACKET | BRACKETS | BRACKETS | OPTION`. No &quot;included&quot; anywhere &mdash;
  so the plan was to weaken the title, on the precedent of Ansul `429022`, where exactly
  that claim was unsourced and removed.
  **The header is TWO LINES.** The line above reads `AGENT | SIZE | DIAMETER | **INCLUDED**
  @289 | USCG@361 | OPTIONAL@427 | RUBBER STRAP@504 | DOLLY@548`, and the B386T row carries
  `818@289 Vehicle@300` &mdash; **dead centre in the column headed INCLUDED BRACKET.** The
  claim is manufacturer-stated, corroborated by the parts book (818 = `01211-P`
  Vehicle/Marine bracket, all 5 lb and 5-1/2 lb aluminum valve models), and it was published.
  **This is the caption and merged-cell family of traps firing on the COORDINATOR'S OWN
  VERIFICATION rather than on an agent's extraction**, which is a first. This file records
  the escalation ladder &mdash; plain text, word coordinates, render &mdash; as a rule for
  agents reading datasheets; the lesson here is that **a spot-check is an extraction too**,
  and a single-line coordinate read of a multi-line header is the same error as trusting
  plain text. It is also the coordinator's scepticism being wrong for the fourth time, after
  `ATD-L3R-IV`, `TH4210U2002/U` and the Mircom `FX-400R` photograph.
- **The coordinator typed a placeholder id into a LIVE mutation. Third instance, and the first that
  reached the API.** Publishing eight titles, the variables object was hand-assembled in the tool call
  instead of being pasted from the file the builder had just written, and one entry read
  `gid://shopify/Product/9840961946: PLACEHOLDER`. **Nothing was written** &mdash; GraphQL rejected the
  whole document, so all eight aliases failed together &mdash; but that is luck of a specific kind:
  **the placeholder happened to be syntactically invalid.** A plausible-looking wrong id would have
  been accepted and would have published one product's title onto another, silently, which is exactly
  the v2b03 briefing incident and the v2b22 query incident.
  This file already says *never type an id anywhere &mdash; briefing, query, mutation or note* and
  *build each briefing from its own `aN_in.json`, programmatically*. The gap it leaves is the
  **publish step**: the rule was written about briefings and queries and the mutation payload was
  still being assembled by hand. **So: emit the variables object with a script, `cat` it, and paste
  that output unmodified.** Three incidents, three different fields, one cause &mdash; a human reading
  a value off a screen and retyping it.

- **Verified before publishing, and both were live title changes resting on an absence.**
  `4901-9820` was titled *&quot;Logo Only&quot;*: Simplex `S4901-0010 Rev. 10 01/2020`, fetched and
  read by the coordinator, contains **`Logo` zero times**, heads Figure 1 *&quot;Red Cover with
  White Lettering&quot;*, and lists only two covers, `4905-9988` and `4905-9989`, **both lettered
  FIRE**. And `TG-7FE-V`'s new title asserts a **listing scope**, the most expensive claim class in
  a feed attribute: Telguard install guide `56052601`, fetched from EDAM, tabulates
  **`TG-7FE-V` (Verizon) | Systems in United States | UL 1610, UL 864** against
  **`TG-7FE-A` (AT&amp;T) | United States and Canada | UL 1610, ULC-S304, UL 864, ULC-S559**.
  The Verizon model has no Canadian listing and the store sells into a market where that matters.
- **Two more coordinator premises wrong, and one of them was wrong on every letter.** The briefing
  decoded `GCHFWF-S7VMC` as *H horn, S7 a 7 W tap, C ceiling*. Edwards `E85001-0641` Issue 2.3:
  **`HF` is High Fidelity** (520 Hz &mdash; there is no horn on the appliance at all), **`S7` is the
  70 Vrms speaker input** (the taps are 1/4 to 2 W), and **`C` is the clear lens** &mdash; ceiling is
  the leading `GC`. `S7` read as a wattage would have put a wrong electrical spec in a feed title.
  Separately, **&quot;a power supply for fire is UL 864&quot; is wrong**: UL 864 covers control
  units and **UL 1481** is the standard for a fire-signalling *power supply*, and the `AL600ULXB`
  carries **UL 294, UL 603 and UL 1481 at once** &mdash; there was no either/or to resolve.
- **The `Q` prefix is not a family and an agent proved it by finding the accessory inside it.**
  The briefing assumed Mircom's `QAA`/`QCC`/`QBB`/`QAD`/`QMT` middle letters encode a device class.
  **`QAA` alone spans two classes**: `QAA-5415`/`-5160`/`-5230` are audio amplifiers at ~$1,500,
  and **`QAA-4CLA` is a $134 Class A converter &mdash; a 16-terminal block that replaces the
  amplifier's own terminal strip.** `LT-859` is headed *&quot;QAA-4CLA CLASS A CONVERTER FOR
  QAA-5415 AMPLIFIER&quot;*, and **`4CLA` appears zero times in both QAA amplifier sheets** &mdash;
  an accessory is usually not a document, for the second time.
  **Six of that lot's twelve are enclosures, chassis or cards, and four are priced like panels.**
  `FX-6000MNS-CH` at **$2,037** is typed **Control Panels** and is *&quot;a backplate&hellip; mounted
  into the BBX-FXMNS-6000 backbox&quot;* &mdash; **and that backbox is a separate $1,999 SKU in this
  same store.** `QBB-6001` at $1,136 is an empty cabinet whose sheet uses the word **required**
  twice. **Eleven of twelve `type` values are wrong or useless**, and on the chassis the field
  pointed the wrong way rather than staying silent.
- **TWENTY-SECOND coordinator premise wrong, and it was wrong twice in one sentence about a defect
  this file itself defined.** The `PCAM` briefing called its title *&quot;one of the ~300&ndash;400
  titles truncated at 150 characters&quot;* and said it *&quot;ends in an unclosed
  parenthesis&quot;*. Measured straight out of `a1_in.json`: the title is **85 characters** and its
  parentheses are **balanced**. It is in neither population. What it actually is: brand, SKU,
  product name and **the first marketing bullet of the description**, cut at the period inside
  `for max.` &mdash; the full sentence still live in the body. **Different mechanism, different
  fix, and both halves were checkable for free against the input file the briefing was written
  from.** This file's own rule is *say which defect a title has, not only which field it is in*;
  the coordinator broke it while citing the population it defines.
- **The `_IN_` prefix, and a wrong filename in my own message.** The Rath agent was asked to
  re-assert against `IN_rath2.json`; the file on disk is **`_IN_rath2.json`**, with a leading
  underscore, and the agent said so rather than quietly using the file it had. It also noted
  that a builder pointed at a nonexistent input is one plausible way a header-only file gets
  written. **The coordinator named a file from memory** &mdash; the same hand-transcription
  failure as an id, in a new field, one turn after patching the builder against exactly that
  class of accident.

- **Two parts lists of one manufacturer use DIFFERENT COLUMN ORDERS for the same data.**
  Simplex `579-1006` runs PC Board &rarr; Installation Instruction; `579-330` runs Installation
  Instructions &rarr; PC Board. Reading one onto the other swaps `566-284` and `574-925`. **The
  tie-break is self-proving: `574-925` is the document number printed on the Replacement
  Instructions PDF itself.** This file records the same shape *within* one Kidde document
  (`K85005-0129`, two tables leading with different models); here it is across two documents of
  one brand, which is harder to notice because nothing on either page looks wrong.
  **And the coordinator conflated those two lists last batch**: this file's claim that
  `579-1006` page 14 tabulates `742-590` and `742-394` together is wrong &mdash; **`742-394`
  appears zero times in `579-1006`** and the `742-590` row is on page 3. `742-394` is in `579-330`.
- **The coordinator read a number out of the WRONG FIELD of its own slice file.** The v2b43
  briefing told an agent that `TH6100AF2004/U` had *&quot;1,148 characters of live title&quot;*.
  The live title is **65 characters**; **1148 is the value of the `impr` field**, sitting two
  keys away in the same JSON object. There was no title-length defect at all.
  This file already records the rule that produced the fix for this class &mdash; *build each
  briefing from its own `aN_in.json`, programmatically* &mdash; and the briefing **was** built
  from the right file; the coordinator then read the wrong key out of it. **So the rule needs
  its last inch: reading a value by eye out of a correct file is still transcription.** Fourth
  instance in this family, after the scrambled ids, the typed-from-memory query and the
  by-eye batch split.
- **THE TITLE-ONLY SLICE FILE SHIPPED NO `type` FIELD FOR SIXTEEN LOTS, AND AN AGENT HAD TO
  TELL ME.** The lot-16 input carried `id`, `vendor`, `sku` and `title` and nothing else, so
  **the catalogue's single most productive structured-field signal was unavailable for every
  one of the 148 titles written so far.** That is the lossy-slice-file failure for the fifth
  time &mdash; after the blank `type` in v2b13, the human-readable note in `live_desc`, the
  empty `live_desc` across four batches, and the ERP string read as fact &mdash; and this time
  in the workstream nobody had guarded, because the guards were all written for the
  *enrichment* builder.
  **The cost is invisible and therefore worth naming:** ten recorded product-class errors in
  this catalogue had a `type` that agreed with a wrong title and raised nothing, and two had a
  type that disagreed and was right. On a title-only lot the type is the *only* second opinion
  available, since there is no live description to read. Fixed in `build_titulos.py`, which
  joins `type` and `handle` from `catalogo_full.json` verbatim and **asserts that no field an
  agent is asked to reason about comes back empty**. Note what the assertion cannot do: nine
  of lot 17's twelve are typed the generic &quot;Fire Alarms&quot;, which is present and
  carries no information &mdash; **a non-empty field is not thereby a signal.**
- **&quot;MONITOR&quot; means a computer display, and the briefing read it as supervisory
  monitoring.** `OGN-MONITOR-UL` is *&quot;Comark UL/ULC 24&quot; Monitor&quot;* for the
  `OGN-UL-STD` rack appliance, and **`OGN-UL-STD` is not a licence at all** &mdash; it is a
  $19,861.90 Xeon E5-2609v4 server with 16 GB, 2 TB and a UL 864 listing. Both senses of the
  word sit on one sheet whose own headline is *&quot;centralized event monitoring
  solution&quot;*. Only three of the seven `OGN-` products are licences.
  **`STD` is polysemous inside this one product line** &mdash; the 10&ndash;99 connection band
  in `OGN-FLSLIC-STD` and the hardware tier (against PRO/ENT) in `OGN-UL-STD` &mdash; which is
  precisely what blocked writing a title for `OGN-MONITOR-STD`. **Returned `null` with the ask
  named**: zero hits across all three language editions of `CAT-5323 Rev 10`, `LT-6674`,
  `LT-6701`, the brochure, the legacy `CAT-5325` and the live product page; **one Mircom price
  list settles it and more searching will not.** The plausible reading (a non-UL companion
  monitor, $739 against $5,396) was deliberately not written.
  **A price inversion checked and found coherent rather than flagged:** the FLSLIC rows are
  marked *&quot;(Price per connection)&quot;*, so $3,549 for ONE against $2,160 for 10&ndash;99
  is a volume-discount curve, not a defect. **Checking a suspicious number and reporting that
  it is fine is worth as much as finding one that is not.**
- **A rejection message that named a plausible wrong reason, fixed in the builder.** Rows with
  `image_url: null` were reported as **&quot;url not https&quot;**, which reads as *a good URL
  we refused* rather than *there was no candidate*. That is the same defect class as the
  builder's earlier silent zero-row run: **a stated reason reads as a finding**, and a
  misleading one costs a reader the truth about their own tool. Now prints
  `no image_url (deliberate null)`.
- **All three documents the briefing named for a Simplex part were the wrong family, and the
  right one is found only in the index's `product_code` metadata.** `4906-9140` is in neither
  `S4906-0001`, `S4906-0003` nor `S4906-0010`; it is in **`S4906-0011` Rev. 4, 10/2018**, whose
  index filename is **`4906-0011.pdf` with no `S` prefix** and whose title and filename both
  omit the model. **Grep the whole blob, not one field.**
  Two consequences worth keeping: the recorded `125 kHz to 12 kHz` house-template defect **does
  not exist in this document** (a coherent 2400&ndash;3700 Hz sweep), and there is **no
  prose-versus-table candela conflict** &mdash; page 1, Table 2 and Table 5 all give
  135/177/185. **A warning is about a document, not about a brand**, which is the third time
  this file has had to say it.
  The merged-cell warning did fire and **all three rungs agreed for once**: plain text emits
  Wall/Ceiling after the wrong rows, word coordinates put &quot;Ceiling&quot; at y-centre 216.25
  against a merged block centred 216.3, and a 300 dpi render confirms Ceiling spans 9140 and
  9142. The `FIRE` lettering came from the **figure**, not the Lettering column, which says only
  &quot;White&quot;.
- **A pack count that is manufacturer-stated in the body text AND both ordering tables, and it
  is the first such row that is a candidate to ADD rather than to remove.** Siemens `ID-SP` is
  **two blank plates per package**, in Data Sheet `8327` and `6327` alike. Every open row in
  `PACKCOUNT_decisao.csv` is a title asserting a count on convention; this is the inverse &mdash;
  the live title asserts nothing and the documentation supports a count. It went to the owner
  rather than into the title, because **adding a pack count to a feed attribute is a new claim
  and that decision is the owner's even when the documentation is good.**
  The briefing flagged it as the `FC901-U3` bare-electronics shape and **it is the opposite
  case**: an accessory, complete as sold. The A&amp;E listings block (UL 864 / ULC / FM / CSFM /
  NYCFD) is scoped to the *enclosure family*, and **a blank plate has no function to list**, so
  no listing was claimed &mdash; the `3-LDSM` precedent on a sheet-metal part.
- **I NAMED AN INPUT FILE THAT DID NOT EXIST, AND THE AGENT FOUND THE REAL ONE AND SAID SO
  BEFORE USING IT.** `build_titulos.py` prepends `lote` to its argument; I passed `lote21`, so
  it wrote **`_TITULOS_lotelote21.json`** while the briefing named `_TITULOS_lote21.json`. The
  agent reported the discrepancy, **verified the file it found was the right lot before
  working it**, and wrote its output to the name the briefing asked for.
  **This is the `_IN_rath2.json` incident again, and that is the point:** the recorded rule is
  *never type a value from memory*, and both instances are a coordinator naming a **file** from
  memory rather than an id. The fix this time is a mechanism rather than discipline &mdash; the
  builder now **refuses any argument beginning with `lote`** and names the mistake. Tested; it
  refuses.
  **And the recovery mattered more than the bug**: a sibling lot was in flight under the same
  wrong name, so the correction went to that agent mid-run with the filename and the two
  terminal decodes this lot had just settled. **A briefing is correctable while the agent is
  still working**, which is cheaper than letting it return a lot built on a guess.
- **On this 6 V family the model number matches NO RATE seven times out of eleven, and ZERO
  times is it the 10-hour figure** &mdash; which is the opposite distribution from the 12 V
  lots, where several were the 10-hour capacity. Every figure read off that model's own current
  datasheet and arithmetic-checked; **the two costliest verified directly by the coordinator on
  one y-line each**:
  `PS-62000` is **190.8 Ah at 20 hr (9.54 A) and 180.0 at 10 hr (18.0 A)** where the model
  number says 200 **and the store's ERP says 210** &mdash; a standby calculation sized on either
  over-claims. `PS-630` is **3.5 Ah, not 3.0**, a 17% under-read and the largest relative gap.
  **So the instruction to state the rate in every title is not a house preference, it is the
  only form in which the family is comparable** &mdash; and this lot contains the proof:
  **`PS-6100` and `PS-6120` are the same physical box** (5.94 &times; 1.97 &times; 3.7 in.,
  12.0 m&#937; both) and **PS-6100's 20-hour capacity, 12.0 Ah, is exactly the number inside
  PS-6120's model number.** A buyer comparing &quot;PS-6120 = 12 Ah&quot; against
  &quot;PS-6100 = 12.0 Ah&quot; cannot separate them; the real answer is 12.0 against 13.0 Ah at
  20 hr in an identical case.
  **Two terminal codes this file recorded as undecoded are stated verbatim**, off 400 dpi
  renders of the models' own Available Terminals panel: **`SP` = Spring**, *&quot;Fully
  collapsible spring type terminals&quot;* &mdash; independently corroborated by the store's ERP
  string `PS-650LS 6V5.0AH SPRING`, **the one place the ERP added information rather than
  removing it** &mdash; and **`FP` = FASTON POLARIZED**, *&quot;Positive: 'F2', Negative:
  'F1'&quot;*, a wide 0.250 in. positive and narrow 0.187 in. negative, i.e. a keyed pair that
  resists reverse connection. That is a real buying attribute and it is in the title.
- **CORRECTED SAME DAY, AND THE CORRECTION IS THE WHOLE FINDING: the v2b48 slice was NOT
  missing. The builder wrote it to a directory named `48` while every briefing, every publish
  path and every previous batch uses `v2bNN`.** Both agents were pointed at `v2b48/`, found
  nothing, and were right; the file had been built correctly all along and was landing where
  nobody was looking. Proved by recovering it: `48/a1_in.json` holds exactly `GW71332`,
  `NP-200R`, `4098-5611`, `D4P120`, `ABP-1`, `4010-9521` and `48/a2_in.json` the other six
  &mdash; **the builder's own split of the `4098-5610`/`4098-5611` pair matches what the two
  agents independently reconstructed from the live store.**
  **And the first diagnosis, written into this file an hour earlier, was wrong in the expensive
  direction: it said &quot;the builder never ran&quot;.** That is a fact about a *program*, and
  it points at reliability. The truth is a fact about a *name*, and it points at a
  five-character fix. A wrong diagnosis that sounds like the right shape of diagnosis is the
  hardest kind to catch, and this one survived a commit.
  **It is the same bug as the `build_titulos.py` prefix mistake, one week apart**: a script
  whose directory naming does not match the convention the rest of the pipeline uses. Both are
  now unrepresentable rather than things to remember &mdash; the builder normalises `49`,
  `v2b49` or `v2b49/` to the same `v2bNN`, prints where it is writing, and **re-reads both slice
  files from disk before reporting success**, refusing on a missing file or an empty `id` or
  `sku`. An empty `type` **warns and names the row** instead of refusing, because a blank type
  is a real catalogue fact for 52 of 16,031 products &mdash; and the warning exists so it gets
  *said in the briefing*, which is the v2b13 failure's actual remedy.
  **The guard immediately paid twice.** It fired on v2b49 naming `P32-DBB`, whose type really is
  blank; that product is the one the batch was asked to adjudicate, and an agent handed a blank
  field with no warning reports the blank back as a finding. And re-running the builder after
  the fix revealed a second hazard nobody had considered: **the `used` set is computed by
  scanning every `<dir>/slice.json`, so a second run silently produces a DIFFERENT twelve
  products** &mdash; the first run's own slice now counts as used. Two agents were already in
  flight against briefings describing the first twelve. Recovered by deleting the stray slice
  and re-running, which reproduced the original twelve exactly. **A slice builder is not
  idempotent, and re-running it while agents are working is a way to hand them somebody else's
  products.**

- **How the agents handled it is the part worth copying, and it is the fourth lossy-slice
  instance &mdash; the first where the file was ABSENT rather than wrong.** No `v2b48/` directory
  existed when the agents started; agent 2 polled for two minutes, reported it plainly, and
  rebuilt its slice programmatically &mdash; filtering `catalogo_full.json` by the six SKUs
  named in the briefing prose, pulling those products **live** from Shopify by `sku:` search
  with no ids in the query, and asserting every snapshot id against its live id before writing.
  **It transcribed nothing.** Agent 1 did the same. The coordinator then re-verified all twelve
  ids live by `nodes(ids:)`: all twelve active, and **each product's live `sku` appears verbatim
  in the title the agent wrote for it**.
  **A missing file is the safe version of this failure and an empty field is the dangerous one.**
  The recorded instances &mdash; a blank `type`, a human-readable note in `live_desc`, four
  batches of empty `live_desc` &mdash; all wore the shape of a plausible value and three of them
  survived because of it. An absent file cannot be mistaken for anything, so the agents stopped
  and said so. **The builder's assertions protected against a wrong slice and nothing
  protected against a slice nobody could find**, which is the same gap one level out.
  A third thing surfaced only in the reports: agent 1, unable to tell which half of the split
  pair was its own, **resolved its own scope by reading the OTHER agent's working directory.**
  It worked, it was declared plainly, and it is exactly the cross-contamination the
  never-transcribe-the-assignment rule exists to prevent &mdash; an agent inferring its scope
  from a peer's draft is one bad draft away from two agents writing the same product.
  A second thing the briefing got wrong and the file would have settled: it named **both** halves
  of the `4098-5610`/`4098-5611` split pair in one agent's prose and said &quot;the other is with
  agent 1&quot;, which disambiguates nothing. Agent 2 researched both, delivered `4098-5610` and
  put a fully validated `4098-5611` in a clearly named extra file rather than guessing. Agent 1
  turned out to hold `4098-5611`, so the guess was right and the extra file was not needed.
  **Naming a pair without saying which half is whose is the by-eye batch split again**, one
  layer down.

- **The container restarted mid-session, and what it cost is worth recording because the
  answer is almost nothing.** Every durable artefact survived: `/tmp/tfas` intact, the git
  repository clean and pushed, the owner's decision file at 475 rows, the delivery hash
  file, all twenty-six photo CSVs, all slice directories. **The only casualty was
  `live.jsonl`** &mdash; and that is a *derived* file, re-pulled in one bulk query in under
  a minute. The two in-flight research agents died and were relaunched against the same
  slice, which was intact and identical, so nothing had to be re-decided.
  **That is the architecture working rather than luck.** The things that would have been
  expensive to lose &mdash; decisions, published work, the method file &mdash; are all
  either in Shopify, in git, or in a CSV; the things that vanished are all reconstructible
  from one query. Worth stating so nobody is tempted to treat a snapshot as a source of
  truth to be protected: **it is cheaper to re-pull a snapshot than to back one up**, and
  this file's own snapshot rule says a stale one is a hazard anyway.

- **The title builder was still reading two SNAPSHOTS, one workstream after the enrichment
  builder was fixed for exactly that.** `build_titulos.py` joined `TITULOS_SEM_NOME_v2.json`
  (three censuses stale) against `catalogo_full.json` (a snapshot this file warns about by name
  twice). Patched to take the newest census and join the **live** bulk pull, with the empty-field
  assertions kept. **A fix applied to one builder is not applied to the pipeline** &mdash; when a
  defect class is found in one script, grep for the same pattern in its siblings, because the
  second instance will not announce itself.

- **THIS FILE IS NOW 712 KB, ABOUT 178,000 TOKENS, AND EVERY AGENT LOADS ALL OF IT BEFORE IT
  FETCHES ANYTHING. Measured 23 Sep 2026, because the owner said limits were being consumed too
  fast and the agents were the obvious suspect.** They may not be the main one. The breakdown:
  **`## The enrichment pipeline` alone is 673 KB of the 712 KB &mdash; 168k of the 178k tokens
  &mdash; and it is 603 top-level bullets**, almost all of them worked case notes. Every other
  section together is under 40 KB.
  **The arithmetic is the point.** A batch runs the coordinator plus two or three agents, and a
  subagent inherits the project instructions, so **one batch pays roughly 700k tokens of method
  file before a single document is downloaded.** The recorded figure for a day's nine agents was
  2.69M tokens total; on today's file size the method file alone would be a large fraction of
  that. **The cost grows every time this file records a finding, which is exactly what the owner
  instructed it to do** &mdash; so the instruction and the budget now pull against each other,
  and that is worth stating rather than quietly absorbing.
  **What is NOT proposed: deleting anything.** The owner's standing instruction is to write
  findings down, this file's whole value is that a recorded trap catches its next instance, and
  five recorded negatives have already decayed and been caught precisely because they were
  written out in full. **The proposal is a split, and it is the owner's call:** an operative core
  loaded as project instructions &mdash; the standing order, the house style, the publishing
  mechanics, the research rules, the route list, the live conventions &mdash; against a case log
  kept in the repository and read on demand or handed to an agent as a named file when its
  subject matter is in the batch. Measured above, the core is a few thousand characters and the
  log is 673 KB.
  **The general lesson is about how a method file ages.** Each entry here was worth writing when
  it was written, and the cost of an entry is paid once while the cost of the file is paid on
  every turn of every agent forever. **A file that is loaded automatically has a budget, and
  nobody was tracking it** &mdash; which is the same shape as every denominator error in this
  file: a number that matters, that nothing in the process measures.

- **Half a batch published on its own, and it is the right shape for a planned stop.** The
  owner asked to slow to one agent and to name a pause point while three were in flight.
  v2b50's agent 2 had already written its output, so those six were validated and published
  immediately rather than held for their batch-mates &mdash; six aliased mutations, zero
  `userErrors`. **A batch is a scheduling unit, not a publishing unit**, and treating it as
  atomic would have left verified work sitting in a file across a session boundary for no
  reason. The other half's slice stays on disk and re-runs from `a1_in.json` unchanged.
  **Worth noting as drift rather than a defect:** all six ran **1,135&ndash;1,229 visible
  characters** against the house range of 700&ndash;1,100, passing only on the 1,230 hard
  ceiling. The validator accepts it and the copy is sound, but a whole batch sitting against
  the ceiling means the soft range has stopped binding &mdash; the same shape as the recorded
  bullet-count drift, and worth a briefing sentence rather than a rewrite.

