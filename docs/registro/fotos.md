<!-- Registro de casos do projeto TFAS. Movido VERBATIM de CLAUDE.md em 23 Sep 2026; nada foi reescrito. Nao e carregado automaticamente: leia sob demanda. E cronologico: entradas posteriores corrigem anteriores; em caso de conflito vale a mais recente e o nucleo em CLAUDE.md. -->

# fotos

- **The photo work was sorted by the wrong metric, and the owner's second screenshot
  proved it. 22 Sep 2026.** After the first photo batch the owner sent **the same admin
  screenshot again** and asked whether it had been fixed. It had not, and none of the
  eleven products on it would have been fixed for a very long time. The reason is the
  sort: the photo queue was ranked by `impressions x 30 + revenue / 50`, the same shape
  as the text queue. **7,384 of the 7,900 products without a photograph have ZERO
  impressions**, and every product on the owner's screen was one of them. So **93% of the
  problem was ranked below everything else** and the visible catalogue never moved.
  **Impressions are the right sort for text and a circular one for photographs.** A thin
  page with traffic is one that copy can lift &mdash; that is why the text queue is built
  that way. A photograph is not competing for an organic ranking: it is a Merchant Center
  feed attribute and the thing a buyer sees after they arrive. Ranking it by the traffic
  the page already earns asks the wrong question, and it systematically protects the
  products that look worst.
  **The second error was rate.** Eight products per agent run against 7,900 is roughly a
  thousand agent runs. That was never going to finish, and it should have been obvious
  from the first batch rather than from the owner asking twice.
- **The bulk match needs a token-boundary rule, and the test that proved it also caught
  the trap.** A naive substring match of SKU against filename scored 6 hits in 12 on the
  Rath sample &mdash; **and one of the six was wrong**: `8100-V4G` matched a file named
  `16x9-Training-Image-8100-V4G**S**.png`, which is the **successor model**, exactly the
  trap an agent had flagged on that same part a batch earlier. Substring matching
  publishes the successor's photograph onto the predecessor's page.
  **The fix is a mechanism: the SKU must be followed by a non-alphanumeric character or
  end of token.** On a 14-SKU sample it **rejected 32 near-matches** and dropped the hit
  rate from 50% to 36%. It also rejected some legitimate files (`2500-205FM.png` for SKU
  `2500-205`), which is the correct direction to err: **a missing photograph is a
  placeholder, and a wrong photograph is a lie that looks convincing.** Any brand whose
  part numbers carry option suffixes &mdash; batteries, BDA gear, notification appliances
  &mdash; needs this rule, and the naive match must never be used to publish.
- **The photo pipeline's first batch: 5 real photographs of 8, and the verification
  chain is the reusable part.** `foto01`, 22 Sep 2026. Rule applied: manufacturer-hosted
  images only, the source must name the exact part number, and **the coordinator measures
  the file rather than trusting the agent's numbers.** All five re-fetched independently:
  mime and pixel dimensions matched the agent's report exactly, and all five were then
  **looked at**.
  **Four of the five are self-evidencing, which is the strongest form this can take:**
  the Power-Sonic labels read `MODEL PS-1290 F2 / 12 Volt 9.0 Amp. Hr.` and
  `PSL-SC-1270 / 12.8V 7.2AH / 92.16WH` in the photograph, and the RATH unit's front
  panel reads `BOSS CONTROLLER / AREA OF REFUGE`. **A part number printed on the product
  in the picture cannot be a sibling's photo.** The fifth, a plain grey enclosure showing
  nothing, rested on an agent's claim that it is the same photograph the datasheet
  embeds &mdash; so the coordinator **checked it**: the PDF headed `2500-PWR24U` embeds a
  520 &times; 520 JPEG that is the identical pose, latch position, cable gland and
  lighting. Verified, published.
  **Three nulls, each for a stated reason, and accepting them is the point.** A series
  image showing the wrong role and the wrong cabinet size; a correct captioned datasheet
  photo that extracts at **243 &times; 374**, under the 600 px floor; and a brand that
  publishes no photograph at all (line drawings and page furniture only). **`null` is a
  correct answer and it was accepted three times out of eight.**
  **Two mechanical facts for the next batch.** `productCreateMedia` **appends**, so the
  placeholder stays `featuredMedia` until `productReorderMedia` moves the new image to
  position 0 &mdash; without that step the work is invisible. And **the placeholder must
  not be deleted**: the same `MediaImage` id is referenced by 7,738 products, so a
  delete could strip it from all of them. Reorder, never delete.
- **Half the catalogue has no product photograph, and the first scan for it returned
  zero. 22 Sep 2026, and the owner found it before any scan did.** He sent a screenshot
  of an admin list showing grey placeholder icons and asked for photos. A bulk pull of
  `featuredMedia` and `media` over all 16,031 active products reported **zero products
  with no image** &mdash; true, and useless. **Every product has a media record; three
  of them are TFAS placeholder images shared across the catalogue.** Counting products
  per `MediaImage` id is what finds it:
  `43649142325472` on **7,738** products, `38254642888928` on 127, `41631160795360` on 35.
  **7,900 of 16,031 active products (49%) carry no real photograph** &mdash; 30,608
  six-month impressions and **$1,520,466 of ERP revenue**. Of those, **7,113 also have a
  description under 120 characters** and **1,376 have all three defects at once**
  (placeholder, thin description, bare `Brand PartNumber` title). Top vendors: Kidde
  Fenwal 1,508, Hochiki 798, Rath 708, Amerex 629, Space Age 480. Ranked list in
  `/tmp/tfas/SEM_FOTO_REAL_ranked.json`; the top 200 carry 21,300 of the 30,608
  impressions and $703,245.
  **The method lesson is the sharp one, and it is a new shape for this file.** Every
  previous scan here failed by **over-firing** &mdash; matching a shape and returning
  hundreds of correct products. This one failed by **measuring the wrong property**:
  it asked *is there an image* when the question was *is the image of this product*.
  A presence check cannot see a wrong value, and a placeholder is a wrong value that
  passes every presence check there is. **Before running a scan, say out loud what a
  defective product would look like in the data &mdash; not what a defective product
  looks like on the page.** Here the signature is not a null, it is a **shared id**,
  and nothing about "no photo" suggests looking for duplicates.
  **The working rule for the photo pipeline: a wrong photo is worse than a placeholder.**
  A grey box tells a buyer nothing; the adjacent catalogue row's photo tells them
  something false, looks entirely convincing, and is discoverable only by accident. That
  is the sibling-part failure mode with no textual trace at all, so it gets the strictest
  handling in the project: the image must be served by the manufacturer's own domain, the
  source page or document must name the **exact** part number, the agent must measure the
  real mime type and pixel dimensions of the downloaded file rather than trust the page,
  and **`image_url: null` is an accepted answer**. No reseller, Amazon, eBay or
  image-search asset &mdash; that is a rights rule as well as a correctness one, since a
  manufacturer image on a distributor page is ordinary channel practice and a scraped
  reseller photo is not. Batches live in `/tmp/tfas/foto/fotoNN/`.
- **The publishing route for photographs is a CSV, not GraphQL, and the owner was right
  to ask.** The GraphQL route costs two calls per product &mdash; `productCreateMedia`
  **appends**, so the TFAS placeholder stays `featuredMedia` until a second
  `productReorderMedia` call moves the new image to position 0 &mdash; and roughly 20k
  tokens of coordinator context per batch of thirty. A Matrixify import CSV carries
  `Handle, Command, Image Src, Image Position, Image Alt Text, Image Command` and **sets
  the position directly, so there is no reorder step at all**, at any row count. Against
  7,900 placeholder products that is the difference between ~260 paired mutations and one
  file. Builder: `/tmp/tfas/csv/build_csv.py`, which takes any harvest JSON and emits the
  CSV.
  **Two safety properties are built into the builder rather than left to discipline.**
  First, **the handle is read from the placeholder census by id and never taken from the
  harvest file** &mdash; a harvest row whose id is not in the census is rejected outright,
  so a hallucinated or stale handle cannot reach the import. Second, `Image Position: 1`
  with `Image Command: MERGE` **pushes the placeholder to position 2 rather than deleting
  it**, which matters because a single MediaImage id (`43649142325472`) is referenced by
  7,738 products: a `REPLACE` that removed it could strip the image from all of them.
  **Reorder, never delete** &mdash; and dropping the placeholder afterwards is a separate,
  deliberate decision, not a side effect of publishing a photo.
  Before handing over any such CSV, **HEAD every URL in it**: the 60-row Rath file was
  checked end to end (HTTP 200 and a `content-type` of `image/*` on all 60) in about
  fifteen seconds, which is cheap against an import that half-fails.
- **An exact match on a structured SKU field is still not enough, and the Notifier harvest
  proved it three ways.** The briefing said that because Honeywell's product search returns
  an explicit `sku_list`, an exact string join needs no boundary rule. **Wrong on every
  count.** (a) **Family records:** only 1,662 of 4,433 records carry a single SKU; the rest
  bundle up to **160** catalogue numbers under one image, so an exact match hands you a
  sibling's photo &mdash; `ABB-2`, an empty annunciator **back box**, matched a photo of the
  **module that mounts inside it**, and one Fiplex record covers a NEMA cabinet and a rack
  chassis together, so its single image is necessarily wrong for one of them. (b) **The
  manufacturer attaches the wrong asset outright:** `002-474`, correctly matched and
  correctly titled &quot;ID3002 Fire Alarm Panel&quot;, carries an asset named
  `ba-bms-V5049A1565-right` &mdash; **a photograph of a building-management globe valve**,
  confirmed by rendering it. The asset-name prefix encodes Honeywell's business unit and has
  to be gated against the product's own domain. (c) **The SKU is not the second whitespace
  token:** wrong on 15 of 387 Notifier titles, eleven of which carry a real trailing
  `&quot; A&quot;` in the SKU (`SD-851E A`, `ECO1002 A`).
  **So the photo pipeline's boundary rule is not a filename-matching quirk to be skipped
  when a structured field exists.** It is the same sibling-part failure this file records
  fifteen times in the text pipeline, and a structured field can be *wrong* as easily as a
  filename can be *ambiguous*.
- **The generic-placeholder mechanism generalises, and it is the same trick that found
  TFAS's own grey box.** A manufacturer's image library has its own placeholders, and a
  hand-written reject list (`hbt-icon-`) misses most of them: `ba-fire-DAS-Cabinets` is
  attached to 12 products and reachable by **108 of the 224 Fiplex SKUs**,
  `hbt-fire-Passive-DAS-Devices` to 22, `hon-ba-fire-notifier-general` to 11. **Count
  distinct products per image URL instead** &mdash; 6,353 of 6,674 images are used exactly
  once, and essentially everything shared is generic. That is precisely how the TFAS
  placeholder was found, by counting products per `MediaImage` id rather than looking for a
  null. **A shared identifier is the signature of a placeholder, in any catalogue.**
  **One evasion worth knowing: byte-identical images under two different asset names.**
  Five rows survived the URL-sharing check and were caught only by MD5 &mdash; `020-573` and
  `020-574` shared one group shot of four different boards. Add an MD5 pass to every brand.
- **Correct photograph, unusable framing: a third answer beside hit and miss.** 58 of the 88
  verified Notifier images are **2048 &times; 280** strips &mdash; genuine, manufacturer-
  published, correct-product renders in which the subject occupies about a tenth of the
  frame. They are not wrong, so rejecting them as defects would be false; they are also not
  what a buyer wants in a grid thumbnail. Scene7 crop parameters did **not** fix it
  (`crop`, `cropN` and `wid` in either order all returned the original aspect), so the
  honest handling is to **split the CSV** and let the owner choose a small-but-correct photo
  over a grey box. Cut used: aspect ratio 3:1. **Record framing as a third outcome
  alongside `null`**, because collapsing it into either one misreports the work.
- **A structured-field join is authoritative about which RECORD an image hangs on and
  silent about which PRODUCT the photograph shows. This is the sharpest thing the photo
  work has produced, and it cost 25 wrong photographs to see.** STI's CMS exposes an exact
  `modelId`, so the raw join hits 335 of 393 &mdash; and **25 of those carry an image whose
  original filename names a different catalogue number**: `STI-9116` &rarr; `9115.jpg`,
  `STI-1230CP6` &rarr; `1130CP6.png`, `EP242410-T2` &rarr; `EP242410-T1.png`,
  `STI-15C20ML` &rarr; `STI-15C10ML-red.jpg`, `UB-2` and `UB-2PN` sharing one
  `UB-2PN-R.png`, four `NT-SS*-EN` pointing at French and Spanish label files. **The
  manufacturer reuses one photograph across variants and the filename is the only trace.**
  So the boundary rule is not a crutch for brands that lack structured data &mdash; it is a
  second, independent check that must run *alongside* the structured join. Strip a brand
  prefix (`STI-`, `KIT-`) and decorations (`-red`, `-1`, `-600x600`, `(2)`) before
  comparing, **testing every stripping level** so a genuine suffix like `KIT-18015-9` is not
  eaten.
- [CORRIGIDO — o teto de 4% vale só para a galeria LifeLines; `/PublicMedia/ProductImages/<SKU>` entregou 84; ver neste arquivo &quot;A SECOND, DERIVABLE, FIRST-PARTY EDWARDS IMAGE LIBRARY&quot;] **The Edwards photo route is ~4%, not the ~75% this coordinator briefed, and the
  &quot;403-vs-404 tell&quot; does not exist.** Measured three ways that agree: the whole
  LifeLines image library is **254 assets in 14 Cloudinary folders**, it overlaps the 206
  Edwards placeholder products by **8**, and a brute probe of 202 SKUs &times; 14 folders
  &times; 2 filename shapes &mdash; **5,740 requests** &mdash; returned **2** hits, both
  already found by the structured route. Every miss was a plain **404 with a zero-byte
  body**; no 403 appeared in ~5,900 requests. **The ceiling is 8.** The unmatched 197 are
  EST4/EST3 cards, EDGE modules, cabinets and SIGA international variants, which the
  gallery simply does not photograph &mdash; a catalogue-coverage gap, not a routing failure,
  and the same is true of the 84 unmatched STI EuroStopper parts, which are absent from
  STI's own product index under any `modelId`.
  Three route facts worth keeping. **The Edwards image host is `images.carriercms.com`**
  (Cloudinary, Carrier's CMS), not edwardsfiresafety.com, and the version segment is
  optional. The LifeLines pages are **Yext-built and embed a percent-encoded JSON blob at
  `document.c_edwardsLifelineResources`**, one record per asset with a curated `title` like
  `&quot;SIGA-OSD -- Signature Optica Smoke Detector&quot;` &mdash; a structured field, so
  the filename fallback was never needed. And **Cloudinary transcodes on the extension**, so
  `.jpg` and `.png` both return 200 for one asset: **the extension is not an identity
  signal** and cannot be used to infer the stored format.
- **THE PHOTO RULE, FOUND BY LOOKING: a manufacturer's own filename can name a different
  product from the one in the photograph.** Power-Sonic publishes
  `power-sonic.com/wp-content/uploads/2025/08/PGFT-12V180.jpg`. **The printed label on the
  battery in that image reads `FT-12V160`** &mdash; verified by the coordinator, who
  downloaded the file and looked at it. First-party host, exact filename match, clean mime,
  600 &times; 552 px: **every mechanical check passes and the photograph is of another
  product.**
  This is the last defence of filename matching falling over. The project's boundary rule
  exists because a filename can be *ambiguous*; the STI batch showed a structured `modelId`
  can be *silent* about which product the photo shows; and this shows a filename can be
  **wrong at the source**. **So the only sufficient check is reading the part number off the
  product in the image** &mdash; which is exactly what the text pipeline's best cases do
  (`TM8-PCA REV` silkscreened on the board, `PSL-SC-1270 / 12.8V 7.2AH` on the label).
  **Build contact sheets and look.** Nothing cheaper catches it. Tesseract is installed and
  is useless here &mdash; it reads synthetic text fine and returns nothing on angled,
  low-contrast product renders &mdash; so this is a human-eye step, not an OCR step.
  Thirteen further rejections came from the same pass and each names a specific
  contradiction: `T-PB-303-0`/`-1` carry a printed overlay reading *&quot;(Model 202-1 shown
  here)&quot;*; `PG-12V65 M6 FR` shows a label reading **UL94 HB**, the non-flame-retardant
  case, on an FR part number; `PS-1270 F2`, `PS-1280 F2` and `PS-6100 F2` show **F1**
  terminals; `CM-6 WHITE` is shown in **gray**. And the check cuts both ways: the PHR
  series labels read *&quot;UL94 V-0 flame retardant&quot;*, **positively confirming** eight
  FR part numbers.
- **313 products have no product NAME at all &mdash; the title is brand plus part number
  and nothing else. The owner found them, twice, before any scan did.** He sent an admin
  screenshot of rows reading *&quot;TCS Basys TS3030&quot;*, *&quot;Silent Knight
  6820UEVS&quot;*, *&quot;Mircom MGC-4050&quot;* and asked when they would be fixed.
  **The mechanism, once stated, is trivial and had never been run: strip the vendor string
  and the SKU out of the title and see whether anything is left.** 313 of 16,031 have
  nothing left. **156 of the 313 are additionally typed the generic &quot;Fire Alarms&quot;**,
  so the class noun is absent from *both* fields and the product is invisible to anyone who
  does not already know its part number &mdash; which is the whole population a descriptive
  title exists to reach.
  **This is the third time the owner has found a defect class before the pipeline did**,
  after the photo placeholders and the photo queue's wrong sort, and the pattern in all
  three is the same: **the scans looked for wrong values and never for missing ones.** The
  entity audit, the truncation scan and the family-type scan all test something the title
  *says*; none of them tests whether it says anything.
  Concentration: **Kidde Fenwal 107, Power Sonic 88, Rath 24, Mircom 22**, then a long tail.
  Only 2,983 six-month impressions and $57,895 of ERP revenue across all 313, so the
  traffic case is weak &mdash; **and that is exactly the circularity the photo work already
  corrected: a page with no product name cannot rank for a product name.** Ranked list in
  `/tmp/tfas/TITULOS_SEM_NOME.json`. A dedicated title-only agent is now working the top
  twelve at the owner's instruction.
- **The look pass produced its best catch yet, and neither of the other two checks could
  have made it: a four-zone panel SKU carrying a photograph of a two-zone panel.**
  `MS-4E`'s best candidate was Honeywell's own Scene7 asset
  `HBT-Fire-MS-2-RIGHT-HiRes`, and **Honeywell's own `sku_list` carries `MS-4E` on that
  record**. The coordinator downloaded it and zoomed the front panel: it is silkscreened
  **MS-2** and shows exactly **ZONE 1 and ZONE 2**. A four-zone panel has four.
  **Look at what each check would have said.** The structured field says MS-4E. The
  filename says MS-2. A reader trusting the structured field publishes a two-zone panel on
  a four-zone page; a reader trusting the filename rejects a row that Honeywell itself
  asserts. **Only the product in the photograph settles it, and here it is settled twice
  over &mdash; by the printed model name and by a countable feature.** That is the
  strongest form this rule takes: **prefer a photograph whose own content can be counted
  against the spec.**
  Seven more rejected in the same pass, including `90518` matched to
  `ba-fire-90510-primaryimage` (a different Gamewell SKU, and the photo is a firefighter
  telephone cabinet), `006820CB` &mdash; **a bare cabinet SKU shown with a fully populated
  panel**, the incomplete-product trap in picture form &mdash; and `AM100`/`BTB65`, whose
  best files are **operating-manual covers** that pass mime, size and every filename filter.
- **A placeholder that says so in words, and passes every mechanical check.** Hochiki's
  derived image path served `0300-03230` an **&quot;IMAGE COMING SOON&quot; graphic**:
  HTTP 200, `image/jpeg`, 900 &times; 900, on the manufacturer's own CDN at a path built
  from Hochiki's own product code. Status, mime, size and dimensions all pass. It was
  caught **by eye**, then corroborated by MD5 &mdash; the same bytes sit under 11 other
  codes. Add it to the placeholder shapes beside the 3,264-byte PNG and the grey
  `MediaImage` this catalogue started from.
- **The MD5 duplicate check was right and its SCOPE was wrong, and eight rounds of
  verification did not catch it.** Counting image URLs across the **eight photo CSVs
  together**, immediately before handing them to the owner, found **4 URLs on 11 rows**.
  Every lot had been MD5-checked against itself and none against the others, so a shared
  asset that straddled two files passed every check there was. Two were real defects:
  Avire's **`G2540-or-G2510.png` on five Rath SKUs** &mdash; the filename names *two*
  models and it was sitting on five &mdash; and Honeywell's
  **`HBT-Fire-WSK-HEAT-ROR-WSK-HEAT-CEILING-HiRes` on two Silent Knight SKUs**, where the
  asset name again names two products, a rate-of-rise detector and a fixed one. Seven rows
  dropped.
  **The other two were correct and had to be kept, which is the part that needed
  judgement rather than a filter.** `macurco-cx-12-co` and `macurco-cx-12-co-ladbs` share
  one photograph legitimately, because **LADBS is an approval designation and not a
  product variant** &mdash; established by a different agent, in a different workstream,
  on a different day. A blanket &quot;drop every shared URL&quot; rule would have thrown
  away four correct rows.
  **The lesson is not &quot;add a cross-file check&quot;; it is that a duplicate check is
  a statement about a POPULATION, and the population has to be the whole delivery.** This
  is the same mechanism that found the grey `MediaImage` on 7,738 products and the generic
  `ba-fire-DAS-Cabinets` on 108 Fiplex SKUs &mdash; **count products per identifier**
  &mdash; applied at the wrong scope. Final delivery: 1,370 rows, 1,370 distinct handles,
  and a HEAD over all 1,368 URLs returning **200 and `image/*` on every one**.
- **MD5 IS NOT SUFFICIENT FOR IMAGES EITHER, and a perceptual hash found 29 wrong
  photographs that eight rounds of verification had passed.** An agent proposed it from
  the Westell library and the coordinator ran it over the **whole 1,370-row delivery**,
  downloading every image fresh. Two checks, and the second is the new one:
  **MD5 across the whole delivery** found 16 groups where a URL-count found 4, because
  the earlier pass compared *URLs* and these are **different URLs serving identical
  bytes**. **A 16&times;16 dHash at Hamming 0** then found 13 more groups &mdash; *the same
  photograph re-encoded*, which MD5 cannot see at all.
  **What made it usable was stopping at Hamming 0.** At &le;10 the pass returns **280
  pairs**, almost all correct: Amerex's small-parts catalogue is full of O-rings, valve
  stems and gauges that genuinely look alike, and Power-Sonic batteries differ mainly in
  a label. That is the over-firing signature this file records for every keyword scan
  &mdash; **&quot;visually similar&quot; is a shape**. **&quot;Pixel-identical content
  under two asset names&quot; is a mechanism**: it proves one photograph, and then the
  only question is whether the two products are the same product.
  **And that question still needed reading, which is why it is not a filter.** Of the 29
  groups, **16 were correct and kept**: every Amerex `-P006`/`-P024`/`-P500` set is the
  *same part in a different carton* (&quot;Seal Tamper (yellow) Sales Pack of 6 / 100 /
  500&quot;), and the two Macurco pairs share a photo legitimately because **LADBS is an
  approval designation, not a variant**. **13 were real and 29 rows were dropped**:
  STI `7520OB`/`7521OB` and `7522`/`7523` are **key lock against thumb lock**, visible on
  the cabinet; Power-Sonic `PDC-12260 NB2` shares a photograph with `PG-12V28 M5 FR`,
  **a flame-retardant part**, which is the `UL94 HB` trap already on record; four Amerex
  rivets (`AL Lever`, `AL Handle`, `BR Lever`, `BR Handle`) share one picture; two gauges
  reading **200 BCF and 240 DC** share one, and the dial reading *is* the product; two
  nameplates whose printed text is the entire difference share one; and Mircom
  `TX3-CSR-35` (13.56 MHz smartcard) and `TX3-PCR-35` (125 kHz) share one byte for byte.
  **Add a dHash pass at Hamming 0 beside the MD5 pass, over the whole delivery, on every
  brand.** Ten lines, no numpy.
- **Three photo brands measured, and in all three the ceiling is CATALOGUE COVERAGE, not
  matching or routing.** Westell **8 of 297 (2.7%)**: 216 SKUs have no page on
  westell.com at all, and **62 of the 81 that do carry no product photograph** &mdash;
  logo and category icons only. RFS **2 of 28**, and it is a *resolution* ceiling: 17 of
  28 have a first-party page at the exact part number, but RFS's main image is usually a
  `_ti` thumbnail at **320&times;200** with no larger rendition, so eight otherwise
  perfect matches died on size alone. Comba **3 of 28**, on **combausa.com** &mdash; not
  comba-telecom.com, which is a solutions site with no per-SKU catalogue at all &mdash;
  and the gap is on the expensive half: no per-part record for **any** CriticalPoint NG
  BDA. Mircom **14 of 380 (3.7%)**, where **only 146 of our 380 SKUs are named anywhere
  on the site**, giving 9.6% of what the site actually covers.
  **Three denominators for one brand is the point.** Mircom is 3.7% raw, 4.5% excluding
  69 `RPL-`/`RB-` raw-material SKUs no manufacturer photographs, and 9.6% of SKUs the
  site mentions. **A coverage rate without its denominator is not a number**, and this
  file has now had to correct five of them.
- **The look pass rejected a row that passed every mechanical check, on a countable
  feature, for the second time.** `STH-2R-ELSTC-F` is served an asset named for itself,
  from its own SKU page, at 1600&times;1600 &mdash; **and the photograph shows four horns
  on the cluster box.** The store's own sibling `STH-4R` is titled &quot;Speaker Cluster,
  **4** STH 15 SR&quot;, so the numeral is a horn count and a `2R` part must show two.
  That is the `MS-4E`/`MS-2` shape exactly (a four-zone SKU on a two-zone panel's photo),
  and it says something this file should state plainly: **where a part number contains a
  quantity, the photograph can be checked against it, and that is the strongest
  verification available short of a printed label.**
  Conversely the same pass **confirmed 14 Eluxa rows no filename check could have**: the
  lens colour is visible and matches the suffix every time (`-NA` amber, `-NB` blue,
  `-NR` red, `-NG` green), ceiling models are round where wall models are rectangular,
  and `ELSTRC-*` lacks the louvered horn grille `ELHSRC-*` has.
- **The `BAD` filename word-list in the CSV builder is a SHAPE, and it rejected five real
  photographs.** `MRI-4045-M-Secutron-with-UL-logo.png` is a product photograph with a
  brand mark **added to it**, not a logo image &mdash; and three of the five were parts
  whose model number an agent had read off the label at 3&times; zoom. The mechanism the
  filter actually wants is *&quot;the asset IS a logo&quot;*, so the fix is: **when the
  filename stem starts with the SKU, the token-boundary match already proves the asset
  belongs to this part and the word-list must not override it** &mdash; with a trailing
  `-PK\d+` stripped from the SKU first, since a pack suffix is a carton quantity and the
  manufacturer files the photo under the bare number. 17 of 17 Secutron rows then pass.
  **This is the over-firing lesson inside my own tooling**, which is where it is hardest
  to see: the filter had been silently correct for 1,300 rows because no earlier brand
  put a brand mark in a filename.

- **The photo delivery measured per vendor for the first time, and the gap is concentrated in
  exactly one brand.** 1,418 distinct handles delivered across thirteen CSV lots, counted against
  the 7,900-product placeholder census:

  | vendor | placeholders | delivered | left |
  |---|---|---|---|
  | **Kidde Fenwal** | 1,508 | **0** | 1,508 |
  | Hochiki | 798 | 22 | 776 |
  | Rath | 708 | 44 | 664 |
  | Amerex | 629 | **408** | 221 |
  | Space Age | 480 | 80 | 400 |
  | Mircom | 410 | 42 | 368 |
  | STI | 394 | **305** | 89 |
  | Notifier | 387 | 90 | 297 |
  | Westell | 371 | 82 | 289 |
  | Fiplex | 224 | 0 | 224 |
  | Monaco / Fireray / Aiphone | 166 | 0 | 166 |

  **Kidde Fenwal is 19% of the whole problem and has never been attempted**, because this file
  records it, in one sentence with Amerex and Fiplex, as *&quot;a brand needing a dealer image pack
  from the manufacturer, not a different filter.&quot;* **Amerex was in that same sentence and
  subsequently yielded 408.** So one of the three names in that recorded negative was simply wrong,
  and nobody re-tested the other two.
  **That is the recorded-negative-decays rule for the fifth time**, after Edwards
  &quot;not on their own site&quot;, the &quot;bogus&quot; `S3000`, `DN-7045` &quot;dropped
  entirely&quot; from EDAM, and the `apcfire.com` path. A harvest agent is now re-testing Kidde
  Fenwal against the current route list, which has grown five times since that note was written.
  **The general point is about how this file records negatives: a brand-level zero should name the
  routes that were tried**, because a bare &quot;needs a different route&quot; cannot be audited and
  therefore never gets re-run. The three brand names sitting in one sentence is what let a wrong one
  hide next to two that may be right.

- **The owner asked for ten more agents, and the right answer was to change the MIX rather than
  argue the ceiling.** This file records six concurrent as the limit, measured &mdash; and the
  measurement is about the *coordinator*, who is serial: every returning batch costs 10&ndash;15
  minutes to validate against the schema, read the strongest claim personally, publish, record and
  commit. **But that cost is not the same per workstream**, and the file had never said so:
  a photo harvest returns a JSON the coordinator processes by script at ~1,448 tokens per delivered
  row; a title-only lot returns one line per product, validated by script and published in one
  aliased mutation; an enrichment batch returns six 1,100-character bodies that must each be read.
  **So fourteen agents were launched with only three on enrichment** &mdash; six photo, four
  title-only, one forensic &mdash; and the queue behind the coordinator stays roughly where six
  enrichment agents would have put it. **State the constraint, then engineer around it; do not
  refuse the number.**
- **Kidde Fenwal re-tested: the recorded negative was roughly right about the NUMBER and wrong
  about the REASON, and the difference decides what to do next.** This file called it &quot;a brand
  needing a dealer image pack&quot;, which reads as *undocumented*. It is the opposite:
  **344 first-party datasheets, openly served, no bot protection, and 131 of 400 SKUs named
  verbatim in them.** What is missing is **per-part imagery above the size floor**, and the ceiling
  is size and attribution, not routing. **5 of 399 photographable, 1.25%.**
  **The denominator is the finding.** Of 400: 138 Kidde electronics, 98 cylinders and heads,
  **97 CARDOX low-pressure-CO&#8322; storage hardware** &mdash; the ERP-string liquid-level gauges,
  R404A condensers and valves already recorded here &mdash; which appear **zero times in all 344
  documents** because they are third-party OEM components inside a Kidde vessel. **No route will
  ever reach those 97.** And a population correction worth keeping: **zero of the 400 are
  Edwards/kidde-esfire lineage**, so the two-lineage hypothesis is right in general and that route
  does not apply to this brand at all.
  **Route A, better than the one on record:** `kiddefenwal.com/wp-json/wp/v2/wpdmpro?per_page=100`
  enumerates the library exactly &mdash; **350 documents with titles** &mdash; against the 206 the
  recorded `?wpdmdl=` id-sweep found. **Route B dies on one number:** the site media API is open at
  763 images and **every per-product image is 485&times;400**; product images at or above 600 px are
  **zero**. The two pools are disjoint, measured: a dHash of 157 datasheet-extracted images against
  703 site images returns **0 matches at Hamming &le;6**.
  **And the five delivered have NO URL** &mdash; they are embedded in PDFs and published nowhere as
  standalone assets, so they cannot enter the Matrixify pipeline, which keys on `Image Src`. Left as
  `image_url: null` with the local path recorded. **The reason to care is not the five: the
  datasheet-extraction route is the only route that ever clears 600 px on this brand**, so a
  bytes-upload path is the prerequisite for the brand at all.
- **The &quot;dealer image pack&quot; this file speculated about EXISTS, is public, and is thirty-nine
  photographs &mdash; three of them reachable.** An agent found it while proving the Kidde-ES route
  does *not* apply; the coordinator then downloaded and measured all five packs directly, because
  the framing was doing a lot of work. `kidde-esfire.com`'s literature library has two categories
  this file never recorded, **`Images` and `CAD Drawings`**, and `Images` serves exactly five open
  ZIPs from `myeddie.edwardsfiresafety.com/PublicMedia/Images/` (bogus control: the documented
  1,245-byte 404).
  **Measured, because the sizes mislead.** *Genesis Photography* (3.6 MB) is the prize: **12 images
  filed per catalogue number** &mdash; `EG4SVRF - Wall Speaker-Strobe.jpg`, `EGCSVWA - Ceiling
  Speaker-Strobe ALERT.jpg` &mdash; at 1,044&times;1,079 to 2,400&times;2,500, far above the floor.
  *Optica* (32 MB) is five images at up to 6,799&times;4,275, **none of whose models are in this
  catalogue**. *FX Panels* is four, filed by marketing name rather than catalogue number.
  **And *Evolve Series* is 131 MB of THIRTEEN marketing renders by colour and angle, with no
  catalogue number anywhere** &mdash; the family-asset pattern this project rejects.
  **Cross-matched against the catalogue: 16 numbers, 5 already have a photograph, 5 are not in the
  store, and THREE are reachable placeholder products** (`EG4SVWA`, `EGCSVWA`, `EWGSVMRF`).
  **Individual files do not resolve** &mdash; three probes, all the 1,245-byte 404 &mdash; so this
  is a ZIP-only pool and needs the same bytes-upload path as the Fenwal five.
  **The transferable lesson is about sizing a find from its bytes.** 131 MB read as a trove and is
  thirteen renders; 3.6 MB read as trivial and is the only per-SKU pool in the set. **Enumerate and
  measure before valuing a route** &mdash; the same discipline this file demands of a scan's
  precision, applied to a download.
- **THE CSV BUILDER DESTROYED THREE HARVEST FILES, AND THEN SILENTLY REJECTED EVERY ROW OF
  THE REBUILDS &mdash; two failures in one tool, both wearing the shape of a legitimate
  result.** The first was argument order: `build_csv.py` takes **OUTPUT FIRST**, and calling
  it `build_csv.py <harvest.json> <out.csv>` overwrote `HARVEST_rath2.json`,
  `HARVEST_powersonic2.json` and `HARVEST_monaco_aiphone_fireray.json` with a 70-byte CSV
  header. **All three were recovered in full from the agents' scratch directories** &mdash;
  nothing re-harvested, every id re-asserted against the input file, every hit's MD5 and
  byte count re-measured from retained local downloads.
  **The second failure is the instructive one.** Re-run correctly, the builder reported
  `0 rows, 450 rejected` with the reason **&quot;url not https&quot;** on rows carrying a
  perfectly good https URL &mdash; because the harvest schema had moved to `image_url` and
  `width`/`height` while the builder still read `url` and `w`/`h`. **A rejection with a
  stated reason reads as a finding**, and &quot;this brand yielded nothing&quot; is exactly
  what several brands legitimately yield here, so the output was plausible. That is the
  empty-`live_desc` failure in tooling rather than in data: **the wrong value wore the shape
  of the expected one.**
  Both fixed as mechanisms rather than as discipline: the builder now **refuses any output
  path not ending in `.csv`** and any file that is both a source and the output (tested, it
  refuses), and it accepts either key spelling rather than rejecting silently. **The general
  rule: a tool that can destroy its input should make that unrepresentable, and a
  zero-row result should be read as a question about the tool before it is read as a fact
  about the data.**
- **Three brand zeros, each with a measured mechanism, and two of them are ceilings no route
  can lift.** **Aiphone 0 of 27**: the brand's entire product-photo convention is
  `<model>_500x375.jpg` &mdash; 650 such files, `full` size 500&times;375 &mdash; so it is
  **below the 600 px floor by construction**, and even a perfect match fails. 24 of the 27
  are spare handsets, screws, connectors, a capacitor and `COP-` custom-order numbers, of
  which **zero product slugs and zero media filenames begin with `cop-`**. **Monaco 0 of 95**:
  the brand's complete media library is ~88 items of which **exactly one is a product
  photograph**, at 500&times;374; its 168-page catalogue *does* carry per-part photographs,
  embedded at ~195 px with no hosted URL. **Space Age 7 of 400**, where 84 non-SF products
  are &quot;correct photograph, under the floor&quot;. **Kidde Fenwal 5 of 399** by
  extraction, **and those five have no URL at all** &mdash; embedded in PDFs, published
  nowhere as standalone assets, so they cannot enter a Matrixify import that keys on
  `Image Src`. **Fourteen verified photographs across three brands now exist and cannot be
  delivered**, which makes a bytes-upload path the prerequisite for those brands rather than
  a nicety.
- **THE DELIVERY-WIDE dHASH PASS FOUND SEVEN DEFECTS NO PER-LOT CHECK COULD SEE, AND THE
  LOOK PASS THEN RESOLVED THREE OF THEM &mdash; ONE IN THE *KEEP* DIRECTION, WHICH IS NEW.**
  Every image in the delivery was downloaded fresh and hashed: **1,481 of 1,506** (the 25
  failures are all Eaton `RemoteDisconnected`, the recorded per-connection intermittency, not
  a defect). **28 MD5 groups and 31 dHash-0 groups**, of which **11 were already known from
  URL counting** &mdash; so **20 groups are pairs serving identical content under different
  URLs**, invisible to the URL check and, where the bytes differ, invisible to MD5 too.
  **Most were correct and had to be kept**, which is why this can never be a filter: eleven
  Amerex pack groups (`-P006`/`-P024`/`-P500`, the same part in a different carton), four
  Secutron `-PK10` pairs and one `-PK15`, two Fireray EN-against-UL approval pairs, two
  Macurco LADBS pairs, and two Power-Sonic `- ECOM` pairs &mdash; the last settled outright by
  the store's own ERP string, **`Battery+ind.box`**, an individual retail carton of the
  identical battery. `SSU00481` against `SSU00481BP` is the same shape: one TCC rail, a 5-pack
  and a 100-pack.
  **Seven rows were dropped, and each names its contradiction.** Two Rath pairs straddled
  *two different lots*, so neither lot's own check had ever compared them:
  `2100-956SIP` (VoIP phone) against `2100-956SS` (ADA smartphone), and `2100-ALARM-S`
  (**Surface** MT) against `2100-ALARM` (**Flush** MT) &mdash; mounting is visible, so one
  photograph cannot be both, and nothing in either image says which. **Both members of both
  pairs dropped**, because the failure here is not *which one is wrong* but that the image
  attributes to neither.
  **And three Power-Sonic pairs were settled by reading the label at 3&times;**, each keeping
  one member and dropping the other: `PG-12V28H M5` keeps its photo (label
  *`PG-12V28H M5 / Terminal Type: M5 / UL94 HB / 28 Ah @ 20-hr, 26 Ah @ 10-hr`*) and
  `PS-12280 NB2` loses it; `PSH-1280 F2 FR` keeps its photo (label *`PSH-1280 FR F2 /
  UL94 V0 / 8.5 Ah`*) and `PS-1290 F2` loses it; and `PDC-12260 NB2` loses its photo to
  `PG-12V28 M5 FR`, which this file already recorded and which had come back.
  **The new thing is the MMF-302-6 case, where looking said KEEP BOTH.** Fire-Lite
  `MMF-302-6` and Silent Knight `SK-ZONE-6` are served **byte-identical** Scene7 assets under
  two different asset names, across two lots &mdash; the shape that has always meant a
  defect. The coordinator downloaded and enlarged it: it is a **bare green PCB carrying no
  brand mark and no model number at all**, silkscreened `ZONE MOD`, `SLC`, `EXTERNAL SUPPLY`
  and **BASE ADDRESS +0 through +5**, with a UL label reading `SEE I56-1799 REV. 006`. Six
  zones, which is what *both* catalogue numbers claim. That is the recorded `B501` precedent
  &mdash; one Honeywell board sold under several Honeywell brands &mdash; and **the absence of
  a silkscreened model number is what makes one photograph legitimately correct for two SKUs.**
  Every previous look-pass instance in this file is a rejection; this is the first time
  looking *saved* rows a mechanical rule would have thrown away.
  **So the pass has to run at the scope of the whole delivery and its output is a question,
  not a verdict.** Final: **1,499 rows, 1,499 distinct handles, every handle present in a live
  pull, and 84 of 84 URLs in the four new lots returning 200 and `image/*`.**

- **My photo-slice builder did not exclude products already DELIVERED, only products already
  adjudicated, and it cost an agent ~22 products of wasted research on one 549-product slice.**
  The builder excluded ids appearing in any `HARVEST_*.json`; but a harvest rebuilt under a new
  name no longer covers rows whose CSV had already shipped, so **the delivered CSV rows are a
  different population from the adjudicated harvest rows.** Fixed in
  `/tmp/tfas/foto/build_in.py`, which now excludes on three grounds in order &mdash; not in the
  placeholder census, already adjudicated by a harvest, **already delivered in a CSV lot** &mdash;
  and prints all three counts so the exclusion is auditable. **The delivered file is the
  authority on what is done, not the working file that produced it.**
- **Two new generic-placeholder shapes, both caught by counting products per identifier rather than
  by a word list.** Eaton serves **`WHEELOCK-COLLAGE-C`** as the only asset on several SKU pages
  (`PS-KEY`, `STH-4R`) &mdash; a family collage, not a product. And Gentex publishes **one family
  render per series page**: 34 product pages carry 74 distinct non-generic images across a
  95-product placeholder set, so **Gentex is a documented zero on per-SKU photography**, with
  constructed `/images/uploads/<SKU>.(png|jpg)` returning **7,276&ndash;7,291 bytes of `text/html`,
  the size drifting with filename length** &mdash; the one-byte-drift tell recorded for
  gamewell-fci.com, on an image host. Resideo returned a documented zero on the same lot.
- **The look pass rejected a row on the PHYSICS of the product class, which is a stronger check
  than a printed label and it is available more often.** `5251B` &mdash; System Sensor's own title
  is *&quot;Heat Detector Head, 135 Fixed, Requires Base&quot;* &mdash; was served
  `HBT-Fire-5251B-5251RB-5151-CEILING-HiRes` from Honeywell's own Scene7, at 1500&times;768,
  mime-clean, **with the SKU first in the filename and present in the record's `sku_list`.** Every
  mechanical check passes. Zoomed, the unit in the photograph carries a **black louvred optical
  labyrinth with vertical insect-screen fins and a flat sensing disc** &mdash; a photoelectric smoke
  chamber. A heat detector has no chamber of that kind at all. Rejected.
  **Two independent grounds, and the second generalises:** the filename names **three** catalogue
  numbers (`5251B`, `5251RB`, `5151`), which is the `G2540-or-G2510.png` family-asset shape; and the
  SKU is a **bare head that requires a base**, while the picture shows head, base and ceiling skirt
  assembled &mdash; the incomplete-product trap in picture form, after `006820CB`. **So when a
  photograph cannot be checked against a printed model number, check it against what the product
  class physically IS**: a heat detector has no smoke chamber, a strobe has no horn grille, a
  visible-only appliance has neither.
- **A contact sheet confirmed six suffix decodes at once, which is the cheapest verification in this
  project.** The six L-Series low-frequency sounders photograph exactly as their letters predict:
  `HWL2` white **rectangular wall**, `HGWL2` white **visibly narrower** wall, `HRL2` red wall,
  `HGRL2` red narrow wall, `HCWL2` white **round ceiling**, `HCRL2` red round ceiling. **`C` is
  ceiling, `W`/`R` is the colour and `G` is compact &mdash; all three readable off the picture.**
  Where a suffix encodes something visible, the photograph is evidence about the SUFFIX and not only
  about the product, and one sheet settles a whole family.

- **A NEW RULE, DECIDED AGAINST AN AGENT'S DEFENSIBLE JUDGEMENT CALL: AN ASSET NAMED FOR A
  BASE MODEL IS NOT EVIDENCE FOR A VARIANT SKU, EVEN WHEN THE DIFFERENCE IS INVISIBLE.**
  Two Fire-Lite rows arrived with the reasoning stated openly and the call left to the
  coordinator, which is the right way to hand up a judgement. `ES-200XC` was served
  `HBT-Fire-ES-200X-STRAIGHT-HiRes` and `MS-5UD-3E` was served `HBT-Fire-MS-5UD-RIGHT-HiRes`;
  zoomed, the panels are silkscreened **`ES-200X`** and **`MS-5UD`**. The agent's argument was
  that the photograph *confirms the model line* and is *silent* on a suffix that is not a
  visible attribute &mdash; a ULC listing and an export voltage &mdash; the opposite of the
  `MS-4E` case in the same lot, where the photograph **contradicts** a countable feature.
  **That reasoning is sound and the rows were still dropped, because all three independent
  signals name the base model**: the filename, the silkscreen, and a family `sku_list`
  bundling both. Nothing points at the variant. &quot;The difference is invisible&quot; is an
  **inference about what the variant looks like**, not evidence about what is in the frame
  &mdash; and this project does not publish an inference into a field a buyer reads.
  **The converse still holds and must not be collapsed with this**: an asset with an internal
  or descriptive name on a **single-SKU** record is fine (`hbt-Fire-P1906458-primaryimage` for
  `H355`), and so is a photograph whose subject genuinely carries no model marking &mdash; the
  `MMF-302-6`/`SK-ZONE-6` bare PCB that is correct for two SKUs at once.
  **Handled as a merchandising decision rather than a research one**, which is what keeps it
  consistent: both went to the owner beside the pending E2S question, where accepting a family
  render for a configuration SKU would recover about 20 of 25. **If the owner accepts a base
  render for a listing or voltage variant, these come back.**
- **Three brand vendor-field errors found by a photo agent, which is becoming a routine
  by-product.** Four `Universal` SKUs are **Neomounts (ex-NewStar)** AV mounts and one is a
  Kalatel/UTC supply &mdash; the three hits were harvested from neomounts.com, the actual
  manufacturer. Three `Federal Signal by The Signal Source` SKUs are **E2S part numbers**, and
  `FSEX-*`, `FHEX-24SMR` and `K8550C095A-02` appear **nowhere** in Federal Signal's own
  426-URL catalogue. After `SF-`/Space Age and `Fireray`/Edwards that is a third and fourth
  umbrella vendor string hiding another manufacturer's namespace. **A photo harvest reaches
  the manufacturer's own site, which is exactly the check a catalogue audit cannot do from
  inside Shopify.**
- **TWO DELIVERED PHOTOGRAPHS ARE THE WRONG DOOR FINISH, AND THE MANUFACTURER'S OWN MEDIA
  TITLE IS WHAT PROVES IT &mdash; a structured field that is MORE reliable than the
  filename, which is the reverse of everything this file records.** A later Mircom harvest
  measured the delivered `BB-1002DS.png` and `BB-1003D.png` as red-doored, and the
  coordinator verified both independently: among saturated pixels, **`BB-1002DS.png` is
  93.5% red** and **`BB-1003D.png` 38.8%**, against **0.3%** for `BB-1002DS-1.png` (visibly
  brushed stainless) and **0.0%** for `BB-1003D_White.png`. Looked at directly, the first two
  are plainly red doors. `LT-617` states the convention twice: **`S` = stainless, no suffix =
  white.** Both files sit on the same Mircom pages as their correct alternatives.
  **Mircom's FILENAMES are wrong here and its WordPress media TITLES are right** &mdash;
  `BB-1002DS.png` is titled `BB-1002DR` and `BB-1003D.png` is titled `BB-1003DR`, both naming
  the red variant the picture actually shows. Two more on the same host run the same way
  (`FXD-008WKI-front.jpg` titled `FDX-008WKI`, `KB-10_backbox_left.jpg` titled `KB-101`), and
  one runs the other way (`products-mir6s-mir6b-…` alt-titled `CX-91S-12TDS`, where the
  filename is right and the alt is wrong). **So on this host the media `name`/`alt` is a
  genuine second structured field, it must be matched ALONGSIDE the filename, and where the
  two disagree the photograph decides.** That won two of seven hits and refused one.
  **The correction ships as a MERGE at position 1, not a REPLACE.** This file records that a
  `REPLACE` which removed the shared placeholder could strip it from 7,738 products &mdash; a
  concern recorded and never tested, and not worth testing on a live import. A MERGE puts the
  correct photograph first and leaves the wrong one at position 2, which is a safe, reversible
  improvement; **the leftover has to be removed by hand on two products, and saying so is part
  of the delivery.**
  **The general point: a delivered lot is not closed.** These two passed every check the
  pipeline had at the time &mdash; first-party host, exact filename match, clean mime, above
  the floor, no URL or MD5 collision &mdash; and were caught only because a *later* harvest of
  the same brand measured colour. **A later pass over the same brand is a check on the earlier
  one**, and it is cheaper than it sounds.
- **A SECOND, DERIVABLE, FIRST-PARTY EDWARDS IMAGE LIBRARY, AND THE RECORDED 4% CEILING WAS
  MEASURED ON THE WRONG LIBRARY.** This file states the Edwards photo route is ~4%, with a
  measured ceiling of **8 products**, proved three ways including a 5,740-request brute probe.
  Every one of those measurements was correct **about the LifeLines/Cloudinary gallery**, and
  the sentence that recorded them did not say so. There is another:
  **`https://myeddie.edwardsfiresafety.com/PublicMedia/ProductImages/<SKU>.{png|jpg}`** &mdash;
  a **derivable per-SKU path**, multi-megabyte masters up to 3783 &times; 5675, honest 404
  (the documented 1,245-byte `/PublicMedia/` miss). **110 of 198 SKUs resolved first try**, and
  the lot delivered **84 Edwards photographs against a recorded ceiling of 8**.
  `/PublicMedia/Images/`, `/Product Images/`, `/ProductImage/` and `/Media/ProductImages/` all
  404 for a known-good SKU, so `ProductImages` is the only spelling.
  **The failure was not the measurement, it was the write-up.** This file already says a
  brand-level zero must name the routes that were tried, because a bare &quot;needs a different
  route&quot; cannot be audited and never gets re-run. The Edwards note named its evidence in
  detail and still generalised a *library* result to a *brand* &mdash; the same shape as
  &quot;Hochiki Europe publishes no per-part images&quot;, which was a statement about one
  directory while `casestudies/` sat unopened. **Two instances in two days: when recording a
  negative, name the PATH, and when reading one, ask what it was measured on.**
  The route reaches **Kidde `E`-prefix Genesis numbers** too (`EG1VWN`, `EG4SVWA`, `EWGSWN`).
  Probed against the 400 Kidde **Fenwal** placeholder SKUs it returns **2 hits** &mdash; so this
  file's &quot;zero of the 400 are Edwards/kidde-esfire lineage&quot; is very nearly right and
  not exactly right, and the two exceptions cost 800 requests to find.
- **THE PERCEPTUAL HASH DEGENERATES ON WHITE-BACKGROUND PRODUCT PHOTOGRAPHY, AND IT COST SIX
  CORRECT ROWS. This file recorded two of its own dHash rulings as real defects and BOTH WERE
  WRONG.** Closing out the held Amerex lot, the within-lot pass returned three dHash-0 groups.
  Looking at all three &mdash; which is the step this file insists on and which had been skipped
  for these &mdash; gave two different answers.
  **The four rivets are four different renders.** `01060-P024` (AL Lever) is matte light grey
  with a small domed head on a long thin shank; `01064-P024` (AL Handle) has a visibly larger
  head on a shorter, thicker shank; `01563-P024` and `01564-P024` are the brass versions, whose
  heads render dark and specular where the aluminium ones are matte. **`23093-P006`, a black
  dust cap, carried the identical hash and is not a rivet at all.** And **the two gauges are two
  different dials**: `03523-P001` reads **USE WITH HALON 1211 ONLY** with a 100 mark and
  `05225-P001` reads **USE WITH DRY CHEMICAL ONLY** with a 140 mark, matching their own ERP
  strings (`Gauge 200 BR BCF` &mdash; BCF is Halon 1211 &mdash; against `Gauge 240 BR DC`)
  exactly. Five products and two products, seven correct photographs, all previously ruled
  duplicates.
  **The mechanism is visible in the hash itself and is the guard to add.** These images are
  about 97% white with a narrow subject: mean luminance 247, standard deviation 30. A 16&times;16
  dHash of such an image collapses to a **repeating column pattern** &mdash;
  `h=3000300030003000&hellip;` for all five rivet-group members, `h=200060006000e000&hellip;`
  for both gauges &mdash; with a **popcount of 28 and 31 of 256 bits**. That is almost no
  information, and two unrelated near-blank images will collide. Against it, the one group that
  was real carries **popcount 116**: `26909` and `26910`, two Amerex FAST FLOW extinguishers,
  whose pixel difference maxes out at **5 of 255 with zero pixels differing by more than 30**
  &mdash; the same render re-encoded, nothing visible to tell the two catalogue numbers apart,
  so both were dropped on the recorded nothing-distinguishes rule.
  **So the pass needs a degeneracy guard, and it is one line: ignore a dHash-0 group whose hash
  popcount is below about 40 of 256, or whose 16-bit rows repeat.** Positive evidence of
  difference was available the whole time and was not read &mdash; **different MD5s, different
  byte lengths and different pixel dimensions** (876 against 852 px tall) across all four
  rivets. A collision between images that are demonstrably different files is a hash failure,
  not a finding.
  **The method lesson is the one this file keeps having to relearn, this time about its own
  tooling: a mechanism is only a mechanism inside its domain of validity.** &quot;Pixel-identical
  content under two asset names&quot; really is a mechanism, and the recorded warning against
  running it at Hamming &le;10 was right. What nobody checked is that the *metric itself* stops
  measuring anything when the image is nearly blank &mdash; so the pass silently changed from
  proving one photograph to proving one background. **A scan that returns a group is a question;
  a scan whose statistic has collapsed is not even that.**
  Lot shipped as 18 rows.

- **THE PHOTO WORK IS 22% DONE BY PRODUCT AND ABOUT 82% DONE BY AVAILABLE YIELD, AND THAT IS
  THE NUMBER THAT SHOULD DECIDE WHAT HAPPENS NEXT.** Tallied 23 Sep 2026 across all 26 CSV
  lots: **1,745 rows, 1,743 distinct handles, and every one present in the 7,900-product
  placeholder census** &mdash; the two repeats are the deliberate Mircom door corrections.
  **6,157 remain.** Projecting each remaining vendor at its own recorded rate:

  | | products left | projected |
  |---|---|---|
  | brands with a **measured ceiling under 4%** | **4,293** | **~55** |
  | the five brands still worth working | **1,091** | **~304** |
  | everything else | 773 | ~16 |
  | **total** | **6,157** | **~375** |

  **So four fifths of what is still obtainable sits in 18% of the remaining products**
  &mdash; Amerex 203, Rath 607, Edwards 114, Power Sonic 84, Macurco 83 &mdash; and the other
  4,293 are projected to yield about fifty-five photographs between them.
  **Kidde Fenwal alone is 1,508 products, 24% of everything left, at a measured 1.25%** &mdash;
  and its five hits have **no hosted URL at all**, being extracted from PDFs, so they cannot
  enter a Matrixify import that keys on `Image Src`. **Hochiki is 770 at 0.77%**, of which 369
  are Hochiki *Europe* numeric codes whose manufacturer publishes nothing per part. Fiplex,
  Napco, Monaco, Gentex and Resideo are **measured zeros**, 675 products between them.
  **Be honest about which figures are which.** The zeros and the sub-4% rates are *measured*,
  each from a named probe with a control. The five worth working carry rates *derived* from
  delivered-against-attempted, which is weaker &mdash; Amerex at 65% because 408 of 629 already
  shipped, Edwards at 42% because 84 of 198 did. Those five could come in lower; the 4,293
  will not come in meaningfully higher, because their ceiling is **catalogue coverage**, not
  matching and not routing.
  **The consequence is a recommendation rather than a queue: work the five, then stop.** What
  remains after that is not a research problem and no better filename rule will move it &mdash;
  it is a request to five manufacturers for a dealer image pack, exactly the one that turned out
  to exist for Kidde/Edwards Genesis (39 photographs, three of them reachable products). **A
  coverage ceiling that is a property of the manufacturer's own catalogue cannot be engineered
  around, and saying so is more useful than another batch.**

- **A datasheet's OWN product photograph showing another model's printed label &mdash; the
  Power-Sonic filename trap, one layer in.** The PTZ7S datasheet's product render carries a label
  reading a 30 Ah `&hellip;CLBS-FS` part, read at 700 dpi. This file records that manufacturer
  *filenames* name the wrong product on three brands; here the wrong product is inside the
  manufacturer's own PDF, where there is no filename to disagree with. **The photo pipeline's
  look pass applies to datasheet-extracted images too.**

- **Import reconciliation, 23 Sep 2026 (live bulk pull of featuredMedia):** of 1,743 delivered handles, **1,684 now show a real photo; 59 still show a placeholder.** 25 Eaton (`lote10b`) and 6 Westell (`lote9b`) failed because those hosts block Shopify's fetcher (same blocks this environment hits) &mdash; they need a bytes-upload path, not a URL import. **28 Siemens rows from `lote7` were the 28 warnings of the main import:** `mall.industry.siemens.com/mall/collaterals/...i.jpg` answers 200 to curl here but Shopify's fetch failed, and the files are **300&times;300** &mdash; below the 600 px subject floor adopted after that lot, so they are **retired, not retried**. A delivered lot is only done when a live pull says so. Catalogue-wide placeholders: 6,203 of 16,031.
