<!-- Registro de casos do projeto TFAS. Movido VERBATIM de CLAUDE.md em 23 Sep 2026; nada foi reescrito. Nao e carregado automaticamente: leia sob demanda. E cronologico: entradas posteriores corrigem anteriores; em caso de conflito vale a mais recente e o nucleo em CLAUDE.md. -->

# mircom-secutron

- **The MD5 pass is not a nicety; it caught nine rows the URL-reuse count could not see.**
  URL counting isolated the obvious generics exactly as designed (Mircom's `ul.jpg` on 60
  pages, `csfm-1.jpg` on 59, Westell's logo on all 420). **MD5 then dropped 24 more
  candidate rows**: `T12-DG`/`T32-DG`/`T48-DG`/`T90-DG` are **one byte-identical family
  photo published under four different filenames**, and `IGB1B` &equiv; `IAVHORN` are two
  **unrelated** products sharing one image. Without it those ship looking perfect.
- [CORRIGIDO — `QAA-5415-70/25` não existe; são dois modelos; ver neste arquivo &quot;QAA-5415-70/25 DOES NOT EXIST&quot;] **Reading the label paid on parts where the riskiest token was the one confirmed.**
  Secutron `FH-400-LF-*` badges read **`MGC 520 Hz`** &mdash; **520 Hz confirms the `-LF`
  low-frequency suffix on the product itself**, which is the highest-risk token in those
  SKUs. `RAM-1032TZDS` and `RAX-1048TZDS` were settled by **counting windows on an
  enlargement**: 4 &times; 8 = 32 with system controls (main chassis) against 6 &times; 8 =
  48 with none (adder), matching both titles exactly. And one Hochiki label carries a
  **moulded number that is not the catalogue number** (`712400334` against `1217170-00`),
  recorded in the row rather than treated as a mismatch.
  Two catalogue defects fell out in passing: **`QAA-5415-70` has lost a `/25`** &mdash;
  Secutron's own media title is `QAA-5415-70/25` &mdash; which is the punctuation-stripping
  import again, after the 185 frequency ranges and `ZR-MC-R`; and **Secutron's own filename
  calls an *adder* chassis &quot;Main&quot;** on `RAX-1048TZDS`, where the image is right
  and the filename is wrong. **A manufacturer filename has now been wrong in both
  directions** &mdash; naming another product entirely on Power-Sonic, and mislabelling its
  own correct photograph here.
- **A fourth punctuation-loss instance, and it is per-row rather than global.**
  `FDX-008WKI`'s own description body reads *&quot;the FDX-008W/**KI** Connects&quot;*
  while its Shopify title has lost the slash &mdash; the same mechanism as the 185
  frequency ranges, `QAA-5415-70/25` and `ZR-MC-R`. **But seven Mircom SKUs do retain
  their slashes** (`CM-45/4`, `QAA-5230S-70/25`, `1032/81`), so the import did not strip
  them globally; it lost them on some rows. That matters for any fix: it is not a
  reversible transformation applied uniformly, so each row needs its own evidence.

- **A second Secutron/Mircom title defect where two SKUs carry the IDENTICAL title.**
  `MRI-4045-M-PK8` and `MRI-4070-M-PK8` both read *&quot;4000 Series Multi (8) Isolator
  Module - Package of 8&quot;*, verified live. Three independent confirmations settle the
  first: the label in Secutron's own photograph reads **`MRI-4045-M MULTI-RELAY MODULE`**
  with Relay 1&ndash;8 groups, Secutron's catalogue page is titled &quot;MRI-4045-M MULTI
  RELAY MODULE&quot;, and the single-module siblings agree (`MRI-4045` Dual Relay,
  `MRI-4070` Isolator). **A buyer specifying short-circuit isolators received relay
  modules.** Corrected; the `type` still reads Isolator Modules and went to the owner.
- **75 titles repeated their own brand and part number verbatim, and fixing them was the
  rare case where a scan CAN be applied unilaterally.** The literal title was
  *&quot;Mircom ANC-6000 Mircom ANC-6000&quot;*. Mechanism: **the live title opens with
  `vendor + &quot; &quot; + sku` twice, adjacently** &mdash; built from the real `sku`
  field, never parsed out of the title &mdash; which cannot fire on a correct product and
  cannot be a coincidence. 75 hits, **Mircom 57**, Talkaphone 6, Potter 4, Det-Tronics 3,
  System Sensor 2, Napco, STI and Genesis one each. All 75 pushed in three aliased
  mutations of 25, every `userErrors` empty.
  **Why this one did not need the owner and the SKU-vs-title nine did.** Removing a
  duplicated substring **adds no claim and removes no information** &mdash; the new title
  is a literal substring of the old one, asserted by the builder before the mutation went
  out, along with ASCII, the 150-character cap and no-op guards. Compare the nine
  near-misses, where every candidate fix was *choosing between two real part numbers*.
  **The distinction is not &quot;title versus structured data&quot;; it is whether the
  edit decides anything.**
  **And the honest consequence: 57 of the 75 become a bare `Brand PartNumber`**, because
  the duplicated string was the entire title. That is still strictly better &mdash; a
  repeated part number in a Merchant Center attribute reads as spam and dilutes matching,
  where a thin title is merely thin &mdash; but it means **the no-product-name census
  grows from 313 to roughly 370**, and those 57 are now correctly visible to the title
  workstream instead of hiding behind a repetition. A fix that makes a defect *countable*
  is worth it even when it does not make the product findable.
- **Eaton's two failure modes are per-ROUTE, not only per-connection.** In one agent
  session `eaton.com` **without the `www`** served the PDF first try through
  `urllib` with a Safari UA, while the `www.eaton.com` **HTML SKU pages**
  `RemoteDisconnected` on all eleven attempts. This file records the intermittency as
  per-connection; add that the PDF route and the HTML route can fail differently in the
  same process.- **A syntax block found, twelve titles written from it, and the one suffix it does NOT
  cover was left blank rather than guessed.** The Mircom `BB-10xxD*` enclosures were twelve
  bare `Brand PartNumber` titles whose entire description was the same string again.
  **Verified first-hand by the coordinator in `LT-617` Rev. 20**, the RA-1000 installation
  manual: *&quot;**No suffix R is for white door. Suffix R is for red door. Suffix S is for
  stainless steel door.**&quot;* &mdash; printed twice &mdash; plus
  *&quot;The finish of all enclosures is painted semi-gloss off white, the backbox is
  black.&quot;* The capacity is Mircom's own words too: *&quot;Backbox for **one / two /
  three / eight / twelve** annunciator chassis with&hellip;&quot;*, so **the digits are the
  chassis count**, corroborated four ways.
  **The `B` suffix is the interesting part, because it is sourced for exactly one model and
  the other four titles therefore carry no finish at all.** `DB` appears **zero times in
  LT-617** &mdash; confirmed by the coordinator &mdash; and Mircom's own BB-1001 page says
  *&quot;BB-1001DB &ndash; Black door&quot;* and nothing else does. The agent then measured
  the site search **with a bogus control and two positive controls** and found
  `BB-1002DB`, `BB-1003DB`, `BB-1008DB` and `BB-1012DB` all return the **no-results
  baseline byte count**. And there is a live alternative reading: Mircom sells *&quot;Painted
  **Beige** Metal Door&quot;* accessories on another line. **So four titles are correct and
  not distinguishable from their siblings in the feed**, which is the honest outcome; one
  price list settles all four.
  **A marketing-versus-installation contradiction, resolved by publishing no mount style.**
  Four Mircom marketing sources call these *&quot;Semi-Flush Enclosure&quot;*, while
  `flush` appears **zero times** in both installation documents &mdash; and `LT-934`
  documents a **separate** `BB-1001SSF/WF/RF` family headed **FLUSH MOUNT**. A distinct
  `-F` family argues the plain `D(R)(S)` models are not the flush ones. That is the Potter
  `DH24120FB` &quot;semi-flush&quot; case with **the brand's own marketing on the wrong
  side**, which is new: there the wrong word came from distributors.
  Route, and it is the best Mircom finding: **`mircom.com/product-documents/` is a single
  page listing all 2,132 product PDFs** under `wp-content/uploads/product_documents/`, so
  one fetch enumerates the whole library. Also measured: the **WooCommerce Store API search
  covers titles and SKU only, not description text**, while the WP `?s=` search does cover
  bodies &mdash; and **that site's WC `sku` field is unreliable** (the BB-1001 record carries
  `sku: &quot;BB-1002&quot;`), so **join on the product name, not the SKU**. The bare
  `www.mircom.com` 301s to zero bytes; use the apex host.
  Two document defects recorded and not published from: `LT-617` Table 2 gives Mounting B
  **greater than** the enclosure height on the BB-1008 and BB-1012 rows where B &lt; H on
  all three smaller sizes; and `CAT. 5504`, **the stainless sheet**, repeats a boilerplate
  note that *&quot;All BB-1000D Series Enclosures are available in a white colour&hellip;
  and a red exterior&quot;* on a page whose only three models are stainless &mdash; a
  series-wide note that cannot describe its own members.- **THE COORDINATOR'S TOP-RISK WARNING WAS BACKWARDS, AND THE REAL DEFECT WAS A DIFFERENT
  ONE ON THE SAME PAGE.** `FSD-751P` was briefed as *&quot;the highest-risk part in the
  batch&quot;* and as the probable **fourth** instance of the bare-sensing-head trap after
  `PAD200-DD`, `D4S` and `SD365R-IV`. It is not: Notifier `DN-6821`, **fetched and read
  directly by the coordinator**, calls it *&quot;The FSD-751P **air duct smoke
  detector**&quot;* throughout, its Product Line block reads *&quot;Duct detector **housing
  with** FlashScan photoelectric smoke detector&quot;*, and two panel sheets say
  *&quot;FSD-751P: FlashScan photo duct detector **with housing**&quot;*. **The live title's
  class noun and the `type` field were both already right.**
  **But the briefing's keyword found a real incomplete-product fact one line lower**, and
  the coordinator confirmed it verbatim: ***&quot;NOTE: Inlet tube is required and must be
  purchased separately. Order one inlet tube for each duct smoke detector ordered.&quot;***
  The buyer gets housing and detector and no tube, and `ST-1.5`/`ST-3`/`ST-5`/`ST-10` are
  sized to duct width. **So the pattern-matching premise was wrong and the discipline it
  imposed &mdash; check the ordering table for the word &quot;required&quot; &mdash; paid
  anyway.** This file has now said three times that a warning which forces a check is worth
  giving even when its guess is wrong; this is the first time the guess was the *top-risk*
  one and still wrong.
  Also worth keeping: **reseller copy split both ways on this exact question** (one says
  &quot;Housing&quot;, another &quot;Photoelectric **Head**&quot;), which is precisely why
  distributor consensus settles nothing.
  **And the wrong-document-family signature was MEASURED rather than assumed.** No search
  reached `DN-6821`; every query returned the low-flow `DN-6955` family, where `FSD-751P`
  occurs 18 times and `FSD-751PL` 18 times &mdash; **every occurrence is inside
  &quot;PL&quot;**. What found the right document was **a sweep of
  `notifier-us/hon-ba-fire-dn-<6850..6960>.pdf`, one request per number**, grepping each hit
  for a standalone `FSD-751R?P(?!L)`. **A numeric EDAM sweep is cheap and it works.**
- **A positive control is what reveals an endpoint that returns a false negative, and a bogus-only
  control reads it as honest.** Mircom's WooCommerce Store API returns **0 rows for
  `search=BBX-1024`**, a product that certainly exists, and 0 for the bogus term as well &mdash; so
  a bogus-only control concludes *&quot;honest endpoint, part absent&quot;* and is wrong on five of
  twelve. The `?s=` route does discriminate, and **the tell is the byte count, not the MD5**, since
  the page echoes the query. **Carry a known-good control as well as a bogus one.**
  Route worth keeping: **`mircom.com/product-documents/` is a single 939 KB page listing all 2,132
  product PDFs**, so one fetch enumerates the library and filename construction is unnecessary; a
  document miss there is an honest 404 at **146 bytes**.
- **Five incomplete-product cases in ONE lot of twelve, all manufacturer-stated.** `FX-4000MNS` is a
  main network **board** that *&quot;mounts in the BBX-FXMNS enclosure&quot;* &mdash; and **that
  enclosure is a separate ~$1,999 SKU in this same store**; `FX-LOC`/`-LOCB`/`-LOCR` are console
  **housings** (*&quot;consists of backbox, inner door and outer door&quot;*, with the installation
  sheet showing the installer fastening the RAXN-LCD and RAX-1048TZDS **to** the inner door);
  `INX-10AC` *&quot;mounts into backboxes BB-5008 or BB-5014 instead of it's own enclosure&quot;*;
  `MCC-1024-12XTDS` bolts into a separately ordered BBX-1024XT(R). **Mircom merchandises chassis and
  enclosures at panel prices**, and ten of those twelve carry the generic `type` &quot;Fire
  Alarms&quot;, so neither field warns the buyer.
- **A part documented ONLY in wiring-diagram callouts, and the agent claimed no form factor.**
  `MP-301` appears verbatim twice, in two independent documents, as *&quot;10K, 2W ELR / MODEL MP-301
  / MANUFACTURED BY MIRCOM&quot;* on audio speaker circuits &mdash; and in **no** Mircom ordering
  table, including the Fire Alarm Accessories catalogue, which lists only `MP-300`/`-300R`/`-300S`
  &quot;End Of Line **Plates**&quot;. Distributors call it a resistor plate; that catalogue rates the
  plate *&quot;up to 47K @ **1W**&quot;* against MP-301's **2W**, **a mechanism arguing it is not
  that plate** &mdash; and an inference either way, so the title says resistor and asserts no form
  factor. Sibling trap: `MP-302` is 22K 1W on the QAA amplifiers.
- **`DS` is undecoded on Mircom and the tempting cross-family import was declined.** It sits on
  modules, on enclosures and on panels, so it is not a finish code. **`BB-1001DS` *is*
  &quot;Stainless Steel&quot;** &mdash; but that is the `BB-1001 D/DR/DS/DB` **door**-code family, a
  different scheme, and carrying it across would be the `PC2WKLED` case again. Fifth preventive
  refusal of a cross-family import on this project.

- **CORRECTION, VERIFIED BY THE COORDINATOR: `QAA-5415-70/25` DOES NOT EXIST, AND THE
  &quot;RESTORE THE LOST SLASH&quot; FIX WOULD HAVE MERGED TWO REAL PRODUCTS INTO A PART
  NUMBER THE MANUFACTURER DOES NOT MAKE.** This file records, from a Secutron photo harvest,
  that *&quot;`QAA-5415-70` has lost a `/25`&quot;* and lists it beside the 185 frequency
  ranges and `ZR-MC-R` as punctuation-stripping. A title agent contradicted it and the
  coordinator fetched both first-party catalogue sheets, because it overturns a recorded
  finding and would have changed a live SKU.
  **Measured on `CAT-9521` and `CAT-9626X`, both mime-clean, both 2 pages:**
  `QAA-5415-70/25` occurs **0 times in each**, while `QAA-5415-70` and `QAA-5415-25` each
  occur **5 times in each** &mdash; two separate single-voltage models, stated outright in
  `LT-6751`: *&quot;the QAA-5415-70 is a 70 Volt amplifier and the QAA-5415-25 is a 25 Volt
  amplifier&quot;*, and the instruction sheet's own filename is
  `LT-6751-QAA-5415-70-QAA-5415-25-Instructions.pdf`.
  **And the proof is positive rather than an absence, which is what settles it.** The same
  two sheets carry `QAA-5230-70/25`, `QAA-5230S-70/25` and `QAA-5160-70/25` at four to five
  occurrences each &mdash; **the manufacturer writes the dual-voltage suffix when it means to,
  on three neighbouring models in the same table, and declines to on the 5415 pair.** That is
  the `DN-62046` inverted proof on a model-number separator.
  **The live catalogue confirms it from the third direction: the store carries BOTH**
  `QAA-5415-25` (vendor Mircom) **and** `QAA-5415-70` (vendor Secutron) **as separate
  products**, matching the two models exactly. So restoring the slash would have asserted a
  non-existent catalogue number on one page and left its real sibling orphaned.
  **The lesson is about where the wrong note came from.** It was read off a *sibling brand's
  media title*, which is a filename, and this file separately records three manufacturers
  whose filenames name the wrong product. **A punctuation-stripping catalogue makes every
  unusual spelling look like a defect** &mdash; and the check that distinguishes them is
  whether the *ordering table* writes the separator on that model, not whether some other
  artefact does. Nothing was changed; the `PONTUACAO_autocontradicao.json` list stands as
  unapplied for exactly this reason.
  Flagged to the owner and not acted on: the pair sits under **two different vendor strings**,
  Mircom and Secutron, which are sibling brands &mdash; the `B501` shape, where no brand is
  wrong and the store disagrees with itself inside one family.
- **Three corrections to this file from one Mircom harvest, and the honest one is the failed
  reproduction.** (a) **The per-request recompression did NOT reproduce**: four accepted
  images re-fetched byte-identical with identical MD5s, on plain `/uploads/products/` URLs
  with a Safari UA and no query string. **Reported as a failed reproduction rather than a
  refutation** &mdash; the earlier observation may have been on a different URL shape, and
  recording that honestly is what the `cdn.power-sonic.com` precedent requires. (b) **`?s=` is
  honest but this file's tell for it is wrong**: it discriminates on result links while
  **every response, control included, is 164&ndash;170 KB**, so the byte count carries nothing
  here. **Count the result `<a href>` links.** It also matches substrings, so it over-fires
  &mdash; and a `?s=` zero is **not** evidence of no asset, proven by `KB-101`, which returns
  zero while owning a correctly-titled asset in the media library. (c) **The REST lockdown is
  broader than recorded**: `wp/v2/posts`, `wp/v2/pages` and `wp/v2/search` are **401** as well
  as `media`, while `wp/v2/product`, `wp/v2/mir_literature` and `wc/store/v1/products` are
  open &mdash; and the Store API `sku` field is not merely unreliable, it is **absent on 118
  of 327 records**.
  **A new route that paid and would not have been guessed:** Mircom's **product-release recap
  posts** (`/products-released-in-2021/`, `/2025-product-releases/` and ~20 more) yielded 140
  additional assets and are **the only place three SKUs appear at all**. And the **NitroPack
  CDN mirror** on WP Engine enumerates every rendition in its srcset, which established the
  400 px and 125 px ceilings **without probing for them**.
- **Mircom measured properly: 7 of 296, and matching was not the constraint on any axis.**
  **215 of 296 (72.6%) are named nowhere** on either mircom.com or secutron.com &mdash;
  corroborated by a 30-SKU random search sample returning effectively 30/30 zero. Of the 81
  that are named, only 34 have any candidate asset; of those 34, **20 failed the look pass or
  the boundary rule and 7 more are the correct product below 600 px**. **Secutron adds
  nothing**: 10 of our 366 are named there and **zero only there**.
  **One owner decision covers five products at once**, which is the useful shape: nine
  rejections are the populated-enclosure trap (`006820CB` precedent), and **three of them are
  otherwise perfect** &mdash; the BB-100x doors, where the finish is measurable and identifies
  the right file. If the owner accepts a manufacturer's own populated illustration for a bare
  enclosure, those three become hits **and the two wrong-colour rows above get fixed in the
  same pass**.
- **An index FILENAME produced a false negative on the one document that settles two parts.**
  Mircom's document index files `LT-674` as `LT-674_QMT-5300_and_QZT-5301_...`, so grepping the
  index for `QZT-5302` returns **zero hits** &mdash; while the document's own **title page reads
  &quot;QMT-5300A, QMT-5302 and QZT-5302&quot;**. This file already records the JCI-hub rule to
  grep the `filename` field rather than the title; this is that rule's failure mode, and the
  remedy is the same one recorded for accessories: **grep the served document's text, not the
  index entry.**

- **FX-4003-12N is chassis-at-panel-price again (audit t02):** CAT-9209 Rev. 10 (Apr 2026) p1 caption *&quot;Display, Backbox and Door are sold separately&quot;* (coordinator-verified); all three required parts are stocked, so the title now says so.

### t08 (23 Sep 2026): MIX-M502MAP

- CAT-5950 Rev. 2 p2: "MIX-M502MAP Zone Interface Module"; "Add suffix A for ULC listed model". It supervises two-wire 24 V smoke detectors on Style D (Class A) or Style B (Class B). **"White", "Universal" and "NO devices" in the old title are unsourced**; the BB-400W white row is a separate back box, not the module colour. The coordinator removed ", UL" from the proposed title (a listing asserted in a title is an owner flag). The family's productType disagrees (Monitor Modules vs Modules), and MIX-M502MA's $28.00 price looks off against $107.55 / $207.05 (flagged).
- **Store API `search=` gives false negatives:** it returned 0 for M502, for the known-good M500MAP and for a bogus term alike. `wp/v2/product?search=` is honest (known-good 1, bogus 0), and the "MIX-M500 Series" record lists UL/ULC pairs.
