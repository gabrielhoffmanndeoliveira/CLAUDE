<!-- Registro de casos do projeto TFAS. Movido VERBATIM de CLAUDE.md em 23 Sep 2026; nada foi reescrito. Nao e carregado automaticamente: leia sob demanda. E cronologico: entradas posteriores corrigem anteriores; em caso de conflito vale a mais recente e o nucleo em CLAUDE.md. -->

# power-sonic

- **Eaton's own filenames name the wrong product five times in 61, and every one would
  have published a visibly different appliance.** `ELMTSR-A`, a multitone strobe **horn**,
  is served `ELSPSTR-C`, a **speaker** strobe; `ELSTW-NG`, a **white wall strobe**, is
  served `ELHSR_NG_*`, a **red horn strobe**; `EL3RMTSTA-ALW` (ALERT lettering, amber) is
  served `EL3RMTSTANW_C` (no lettering, white); plus `ELMTW`&rarr;`ELFHNW-C` and
  `STH-2R-ELSTC-N`&rarr;the `-F` variant. **All five were caught by the token-boundary
  rule.** After Power-Sonic naming another product and Secutron mislabelling its own
  correct photograph, that is a third manufacturer whose filenames are unreliable &mdash;
  **this is now the norm, not the exception.**
  Route: `https://www.eaton.com/us/en-us/skuPage.<SKU>.html` carries
  `https://www.eaton.com/mdmfiles/<contentId>/<ASSET>/<size>`, sizes `500x500_72dpi`
  through `2000x2000_72dpi`. **The asset id is not derivable** &mdash; 29 unmatched SKUs
  probed across three constructed shapes returned **0 hits, all 403**. `curl` fails as
  documented and **`urllib` plus a Safari UA worked first try on ~120 fetches in one
  process**, the per-connection intermittency in the lucky direction for once. Its miss
  is a clean 403 with no body.
- **A held title, and the reasoning is the model for this class of hold.**
  `PDC-12400 M6` ($187.90) was left exactly as it was. The SKU is **not in Power-Sonic's
  current 15-member PDC catalogue**, established three independent first-party ways each
  with its own bogus control: the WP product REST API, the product sitemap, and the
  derivable datasheet path. **It was not called invented and the SKU was not touched**
  &mdash; a negative bounds the search, not the catalogue, and distributors stock legacy
  parts. But a mechanism came with it: **`PS-12400` is a current 40 Ah part whose case
  dimensions are identical to `PDC-12480`'s**, same box different series, and the store
  prices PDC-12400 **above** PDC-12480 despite the lower number. Flagged; a purchase
  order or a carton settles it.
  **And the distributors were available and were refused on evidence.** Three of them
  give PDC-12400 as &quot;40Ah&quot;, and **the same page that does calls `PDC-122000`
  214 Ah where the manufacturer says 215.0** &mdash; wrong on a sibling in the same
  breath. Eighth instance.
- [CORRIGIDO — com nome encontrado o CDN serve PDF real; só nome inventado dá 0 bytes; ver neste arquivo &quot;zero-byte question is SETTLED&quot;] **The `cdn.power-sonic.com` zero-byte trap is worse than recorded: it returns HTTP 200
  and 0 bytes for parts that genuinely exist**, not only for misses. So it is not a
  404-in-disguise &mdash; **it serves nothing for anything**, and a &quot;hit&quot; there
  means nothing in either direction. The byte guard is mandatory. Also measured: the
  datasheet-path 404 shape **drifts a few bytes with the filename** (280,493 for a bogus
  name against 280,471 for a real-looking one), so compare the shape and not an exact
  byte count &mdash; the same one-byte-drift tell recorded for gamewell-fci.com.

- **The nameless-title queue's sort is now degenerate, and that settles how to batch it.**
  Of the 229 titles still carrying only `Brand PartNumber`, **every single one has zero
  six-month impressions and zero ERP revenue** &mdash; the first six batches took
  everything with any signal at all. So `impressions x 30 + revenue / 50` is a tie across
  the whole remaining population and cannot order anything.
  **Sort by brand instead, for the same reason the photo work does**: 199 of the 229 sit in
  four vendors (Kidde Fenwal 104, Power Sonic 57, Mircom 20, Rath 18), and a route or an
  ordering-syntax block mapped once pays back across the whole family. Batch 7 came out as
  twelve Power-Sonic batteries from one datasheet family, which is not a coincidence of the
  sort so much as the only thing left for it to do.
  **And it is the photo-queue circularity argument again, one workstream over**: zero
  impressions is not evidence that these pages do not matter, because **a page with no
  product name cannot rank for a product name.** The traffic case was always going to be
  nil by construction.
- **The Power-Sonic model number means a different thing on every series, and the ERP is
  wrong roughly half the time.** Two title batches, 23 SKUs, with the load-bearing figures
  **read directly by the coordinator off each datasheet by word coordinates**:
  `PG-12V103` is **110.0 Ah at 20 hr and 100.0 at 10 hr**, matching neither; its neighbours
  `PG-12V55` (60.0/56.0) and `PG-12V55S` (56.6/55.0) are **two adjacent part numbers where
  the same two digits mean different things**; `PG-2V600` is **636.0/600.0**, so the number
  is the 10-hour rate; `PGFT-12V180` is **180.0/170.0**, so there the number is the 20-hour
  rate &mdash; *the opposite of its own sibling series*; and on **PHR the number is not a
  capacity at all** (`PHR-12100` is 28.0 Ah).
  **The store's ERP string was wrong on six of eleven checkable rows in one batch**,
  including four capacities, and its rate *labels* were wrong too (`PGFT-12V180 ... @10hr`
  where 180 is the 20-hour figure). **So the ERP is a candidate, never a fact** &mdash; the
  third distinct way this file has now had to say that, after the lossy `type` field and the
  `live_desc` placeholder. Every published title states both rates where they differ, which
  is not a nicety: without the rate, `PG-12V103` and `PG-2V600` are simply not comparable
  claims.
  **A `null` returned for the right reason:** `PGFT-12V125` is absent from the datasheet path
  in five spellings, from the product REST API (bogus control returns `[]`, so the endpoint
  is honest) and from the product sitemap &mdash; the PGFT series has six members and this is
  not one. **Not called invented, SKU untouched, and the agent explicitly declined to read
  across to the real sibling `PGFT-12V150`.**
  Two more measured facts: **`power-sonic.com/?s=` is non-discriminating** (one product hit
  for a real term *and* for a bogus one), so use `wp/v2/product?search=`; and **`AGM` appears
  zero times in the PHR datasheets**, so the agent used Power-Sonic's own headline
  &quot;High-Rate Discharge Battery&quot; rather than importing the class word from the PG and
  PGFT sheets &mdash; a cross-series import declined, the fifth time on this project.
- **The Power-Sonic model number is the 20-hour capacity on only 4 of 12, and the ERP string was
  wrong on 5 of 12 &mdash; both measured on one batch.** Three models carry the **10-hour** figure
  in the number (`PS-121400` 147.0/140.0, `PS-122000` 226.0/200.0, `PS-122500` 265.0/250.0) and
  five match **no rate at all** (`PHR-12400` 113.8, `PHR-1290` 20.0, `PS-1220` 2.9, `PS-12200HD`
  22.0, `PS-1230` 3.4). Every title states the rate and the three 10-hour cases state **both**, so
  a buyer who ordered expecting 140 Ah can see why the sheet says 147.
  **What makes this batch's numbers trustworthy is the third check, and it is reusable:
  arithmetic.** Beyond word coordinates and a 300 dpi render, the agent multiplied each sheet's
  own stated discharge current by its hours and got the stated capacity on all twelve at both
  rates &mdash; `PS-1220` at 0.14 A &times; 20 h = 2.8 &asymp; 2.9, where a 2.0 Ah cell would draw
  0.10 A. **A datasheet that states a current and a capacity states its own checksum.**
  Two live sibling traps came with it. **`PS-1220` and `PS-1229L` carry the SAME 20-hour capacity,
  2.9 Ah**, with identical dimensions, internal resistance and short-circuit current, differing
  only in weight &mdash; so **capacity alone cannot distinguish two SKUs the store carries**, and
  `L` is defined in no document. And `PS-12200HD`'s case line reads **&quot;ABS Plastic Rated to
  UL94:HB&quot;** closed, where the other eleven read &quot;HB or V-0 optional&quot;: **there is no
  FR version of the HD.**
  **`FR` is manufacturer-defined and `UL94 V-0` is not.** The SLA Technical Manual says *&quot;Flame
  Retardant (FR) battery cases and lids are available&hellip;&quot;*, so &quot;Flame Retardant
  Case&quot; is publishable &mdash; but no document equates FR with V-0, so joining the two is an
  inference and no V-0 claim was made. The ERP's &quot;V0 case&quot; rests on that same inference.
- **The `cdn.power-sonic.com` zero-byte question is SETTLED, and the correcting agent was right.**
  With filenames **found** (linked from a product page) it serves real PDFs &mdash;
  `SLA_Technical_Manual.pdf` at 2,167,620 bytes, mime-clean. A **bogus** name returns **HTTP 200,
  0 bytes, `inode/x-empty`**. The coordinator's failed reproduction used a *constructed* filename,
  which is the very thing this file forbids, so the failure was the path and not the host. **The
  byte guard stays mandatory** &mdash; the miss is a 200 &mdash; but the host is usable.
  *And the datasheets are not there at all*: they live on
  `power-sonic.com/wp-content/uploads/datasheets/<slug>.pdf`, whose 404 is `text/html` at
  280,472&ndash;280,481 bytes, matching the recorded drifting shape. Also: **a product page needs
  its trailing `-L`** or it returns 302 with zero bytes, and **`PS-12260`'s slug is
  `ps-12260-12261`**, a combined page &mdash; the slug is not derivable from the SKU.

- **Destroying a file and rebuilding it found a defect in the version that was lost.** The
  Power-Sonic rebuild replaced `NO.get(sku) or '<generic fallback>'` with a hard `NO[sku]`
  lookup, which raised on exactly one SKU: **`PG-12V28 M5` had been recorded as
  &quot;no token-boundary match anywhere in the media library&quot; and that was false.** It
  is a look-pass rejection &mdash; its only asset shows a label reading `PG-12V28 FR` with
  `UL94 V0`, the flame-retardant build, on a SKU carrying no `FR` &mdash; the same shape as
  five of its siblings. So the true count is **25 look-pass rejections, not 24**.
  **A `.get()` with a fallback is a silent `else` branch**, and a plausible fallback text is
  the hardest kind to catch. The rebuild also caught the agent's own verification over-firing
  in the same breath: counting look-pass rejections by keyword regex gave 26, one of them a
  genuine no-candidate row whose reason merely *mentioned* an asset. Counting by mechanism
  &mdash; the row's own verdict field &mdash; gives 25. **Scan for a mechanism, not a shape,
  applies to your own checks.**
- **The look pass caught the APC filename trap, and the sibling files convict it.**
  `T-PB-202-0.jpg` shows a chassis whose label reads **&quot;POWER SUPPLY MODEL NO. T-PB
  202-1&quot;**. Its siblings `T-PB-303-0.jpg` and `T-PB-303-1.jpg` carry the **same
  photograph** and *do* carry an overlay saying &quot;(Model 202-1 shown here)&quot;. So all
  three are the 202-1, **two admit it and one silently does not** &mdash; which is stronger
  than the Power-Sonic case, because the manufacturer demonstrates on its own neighbouring
  files that it knows the disclaimer is needed.
- **The Power-Sonic model number matched NEITHER rate on a third series, and one 5 Ah gap sits
  between two stocked SKUs.** Measured with the arithmetic check (stated discharge current
  &times; hours must equal stated capacity): `PS-12550` is **56.6 Ah at 20 hr / 55.0 at 10 hr**
  and `PS-12750` is **80.0 / 75.0**, so on both the number is the **10-hour** figure;
  `PS-1238` is **4.0 / 3.72** and matches neither. `PS-445` is a **4 VOLT** battery whose title
  carried no voltage at all while its four lot-mates are 12 V. **Every title now states the rate
  and, where they differ, both rates** &mdash; without it these are not comparable claims.
  Also settled from the terminal renders: **`F1` is the 0.187 in. Faston and `F2` the 0.250 in.**,
  which is a real difference between two connectors a buyer cannot interchange.

- **The series-boilerplate page PROVED byte-identical rather than asserted, which is the right
  standard for a negative.** The approvals page of `ps-610` (1.0 Ah) and `ps-62000` (190.8 Ah)
  is **byte-identical, md5 `c8446543a5b8`**; `ps-650ls` and `ps-6360` share `a3d1ea6dad7b`, the
  two variants differing only by a **one-minute export timestamp**. It is a glossary of what the
  standards mean, attached to no model &mdash; so no certification, CE, IEC 60896, RoHS,
  &quot;sealed&quot;-as-certified or UN2800 non-spillable claim is in any title.
  **And the one document that looks like it would settle a certification does not.**
  `cdn.power-sonic.com/documents/UL1989_DoC_S0.pdf` is a **self-signed Declaration of
  Compliance**, scoped at *series* level across ten product lines, containing **zero model
  numbers**, saying *&quot;designed, manufactured, and evaluated to comply&quot;*. That is not a
  per-model UL Listing. The `SLA_Technical_Manual.pdf` likewise **contains no model numbers at
  all**. **A document can be first-party, current and mime-clean and still be unable to answer a
  per-model question** &mdash; check what it is scoped to before quoting it.
- **Two SKUs in this store that no title can separate, and saying so is the deliverable.**
  `PTX14AHLBS-FS` and `PTX14AHBS-FS` carry **identical rows in every column** of Power-Sonic's own
  table &mdash; 12 V, 12 Ah, 210 CCA, 273 CA, 9.7 lb, 1.2 A, Terminal A, 5.2 &times; 3.5 &times;
  6.5 in. The manufacturer *does* decode the part number (Applications Guide p20: `PTX|14|A|H|L|-BS|-1`
  = AGM / performance classification / case size / **higher CCA** / **polarity location** /
  bottle-supplied electrolyte / terminal), and the only token that differs is **polarity
  location**, which no document resolves to a side. **So the two titles differ only by part
  number, deliberately.** One carton label settles it.
  What the decode *did* settle is the buying decision on the rest of the lot: **`-FS` ships charged
  and sealed and `-BS` needs a bottle of acid**, proved three ways (plain text, word coordinates at
  x=171.5 &quot;AGM READY TO GO&quot; against x=303.0 &quot;LOCALLY ACTIVATED AGM&quot;, then a
  300 dpi render). That is in the titles. And **the model number is a capacity on none of the
  four** &mdash; PTZ7S 6.0 Ah, PTZ10S 8.6, PTZ12S 11.0, PTX14AHL 12.0, all at 10 hr with the 20-hour
  row **literally blank** on every sheet, identically, so a template defect and not extraction
  error.
