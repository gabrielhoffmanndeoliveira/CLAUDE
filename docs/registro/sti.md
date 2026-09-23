<!-- Registro de casos do projeto TFAS. Movido VERBATIM de CLAUDE.md em 23 Sep 2026; nada foi reescrito. Nao e carregado automaticamente: leia sob demanda. E cronologico: entradas posteriores corrigem anteriores; em caso de conflito vale a mais recente e o nucleo em CLAUDE.md. -->

# sti

- **Two more first-party hosts mapped.** `support.westell.com/documents/<slug>-DS.pdf`
  serves Westell datasheets directly, no bot protection, mime-clean &mdash; **so the
  &quot;relationship-sold means undocumented&quot; premise fails for a third category**,
  after Fiplex and Det-Tronics. And **STI's real document host is
  `cdn.sanity.io/files/4ikv42xc/production/<hash>.pdf`**, linked from `sti-global.com`
  product pages; `sti-usa.com` is only the footer address, so paths cannot be
  constructed &mdash; read the product page. STI publishes three documents per product,
  and the **sales data sheet carries a Build-Your-Model ordering-syntax block** that
  decodes the number character by character, the same class of decoder as Edwards
  catalogue page 5 and Eaton `TD450158EN` Table 3.
- **Two more self-contradicting documents, both resolved by publishing nothing.**
  Siemens Data Sheet **6306** says *&quot;Durable metal design&quot;* in its A&amp;E
  bullets and *&quot;constructed of durable, molded polycarbonate material&quot;*
  in the Specifications paragraph **immediately below, on the same page**; the
  installation sheet states no material, and the reseller pages repeat the
  polycarbonate line, which is the datasheet prose rather than a third source. No
  material claim published. Two **STI** documents disagree on the polycarbonate
  temperature range &mdash; sales sheet &minus;40 to 250 &deg;F, installation sheet
  &minus;40 to 284 &deg;F. No temperature published. **That is now five documents in two
  batches contradicting themselves on a spec**, which makes it ordinary rather than
  remarkable: budget for it, and treat &quot;the document says so&quot; as needing a
  second reading of the same document.
- **The handle is a better SKU authority than the title's second token, and the check is
  mechanical.** Shopify handles here are `<vendor-slug>-<sku-slug>`, so slugifying a
  candidate token and comparing it to the handle tail **validates the extraction without a
  human reading samples**. That caught `STI-9623 Beam Smoke&hellip;`, whose title is missing
  its brand prefix so token 2 is the word &quot;Beam&quot;, and it confirmed the other 597
  across two brands. Where it cannot confirm &mdash; a SKU spanning two whitespace tokens
  (`3-IDC 8/4-E`), a duplicated brand token, an underscore the slug cannot represent
  &mdash; **skip the row rather than guess**; three were skipped on that basis.
- **The duplicated-vendor-token scan, and the same over-firing in miniature.** Three
  Macurco Cal-Kit titles read *&quot;Macurco **Macurco** Cal-Kit 1&quot;* because
  **the Shopify `sku` field is itself `Macurco Cal-Kit 1`** and the title is vendor plus
  SKU. Scanning for it by normalised prefix returned **314 hits, nearly all false**:
  `STI STI-3150` is correct, because the vendor is `STI` and the part number *begins*
  with `STI`, and stripping the hyphen makes the two look like one repetition.
  **The mechanism is whitespace: the vendor repeated as two SEPARATE TOKENS.** That
  returns **5** &mdash; the three Cal-Kits, `Notifier Notifier NC-100`, and
  `STI STI EP141207-T`. Fixed on the three published this batch.
  A second, cleaner mechanism found the related defect: **brand and part number repeated
  verbatim** (`Mircom ANC-6000 Mircom ANC-6000`) returns **75 products, 57 of them
  Mircom** &mdash; which matches, exactly, the count a Mircom photo agent reached
  independently from the other direction. Two routes to the same number is the best
  validation a scan gets.
- **A recorded contradiction did not reproduce, and the honest finding is that it belongs to a
  different product.** The briefing told an agent to publish nothing if it hit this file's recorded
  STI polycarbonate split (&minus;40 to 250 &deg;F against &minus;40 to 284 &deg;F). Measured on
  `STI-7520`: **`284` appears zero times** in the English sales sheet, the French sales sheet and the
  installation sheet, and **the install sheet states no temperature at all**. Two documents do not
  disagree &mdash; one is silent, and 250 &deg;F is corroborated verbatim across two languages.
  **A contradiction recorded on one product of a brand is not a standing rule for the brand**, which
  is the pack-count scope error (category &rarr; vendor &rarr; document line) firing a fourth time.
- **The STI Build-Your-Model block is model-attributed and the manufacturer's own web copy
  is not.** `STI-751` + **`0` Key Lock / `1` Thumb Lock** + back-box letter + `-OW` white
  polycarbonate, confirmed three ways (plain text, word coordinates with the digit and its
  label on one y-line, and a 300 dpi render showing the arrows). Meanwhile STI's two product
  pages describe the *identical* back box differently, one saying &quot;Open White Back Box
  for Flush Mount Applications&quot; and the other only &quot;Open Back Box&quot;. Same lot,
  same price: **the separator is the lock and nothing else**, the 7520/7521 finding
  generalised. Also on that sheet, an approvals line naming **exactly these two SKUs**:
  *&quot;UL **Recognized Component**&quot;*, which is a weaker claim than Listed and is what
  the titles say.
- **A CROSS-LOT COLLISION THAT THE LOOK PASS RESOLVED THREE WAYS AT ONCE, AND IT IS THE
  CLEANEST INSTANCE THIS PROJECT HAS.** The delivery-wide dHash found STI `13310FR` (already
  delivered in lote2), `13310NR` and `13320NR` serving **pixel-identical content under three
  different asset URLs** &mdash; invisible to URL counting, invisible to MD5, and invisible to
  each lot's own within-lot check because the members sat in two different lots.
  Their titles: `13310FR` *&quot;Red Housing, F&hellip;&quot;*, `13310NR` *&quot;Red Housing,
  N&hellip;&quot;*, `13320NR` *&quot;**Horn**, Red Housing, N&hellip;&quot;*. The render, read
  once, shows a Universal Stopper dome cover with **a blank red band carrying no lettering and
  no horn grille**. So one photograph **positively confirms** the no-label, no-horn member and
  **positively contradicts** the other two. `13310NR` kept; `13320NR` and `13310FR` dropped.
  **That is better than the usual outcome.** The recorded ladder's step (d) is *nothing
  distinguishes &rarr; drop both*, which is what the two Rath pairs got. Here the image itself
  adjudicated, so the answer is not a cautious withdrawal but a decision with evidence.
  **Where a shared render shows an externally visible feature, the feature IS the
  discriminator** &mdash; and a horn grille, a label, a lock type, a terminal shape and a
  countable zone are all externally visible.
- **STI: the product record is the WRONG primary route and the asset library is the right one,
  which inverts what this file records.** The recorded finding is that STI's CMS `modelId` join
  is authoritative-but-silent and the filename rule is a *second* check. Measured on 85
  products: **only 26 have a product record at all, and 23 of those 26 carry a `featuredImage`
  whose `originalFilename` names a different catalogue number** &mdash; `STI-9116`&rarr;`9115.jpg`,
  `STI-13720FR`&rarr;`STI-13710FR.png`, `STI-14300NC`&rarr;`STI-14300NY.png`, four `NT-SS*-EN`
  pointing at French and Spanish label files.
  **The Sanity dataset is publicly queryable by `originalFilename` and that route hits 76 of
  85.** `https://4ikv42xc.api.sanity.io/v2021-10-21/data/query/production?query=` with
  `*[_type=="sanity.imageAsset" && originalFilename match "STI-13*"]` &mdash; 47,809 image
  assets against 1,280 product docs, bogus pattern returns `[]`, and **the `url` field is the
  native-resolution original with no transform needed.** So: **when a structured field is
  wrong, the filename index may still be right, and on this brand it is the better primary
  route.** 78.8% delivered against a documented 4% ceiling on Edwards &mdash; the difference is
  entirely which index you query.
  Selection rule that made it usable, worth copying: after stripping a trailing `-N` duplicate
  counter, **the normalised filename stem must EQUAL the normalised SKU, or SKU+`-en`** &mdash;
  which rejects the language variants, the combination shots naming a second catalogue number,
  the state variants (`-triggered`, `-rest`, `-no-power`) and the bare colour letters.
- **A contact-sheet artefact that nearly read as an image defect, and the fix is one line.**
  Several STI PNGs showed a black bar in the contact sheet; it was `convert('RGB')` dropping
  the alpha channel, not the image. **Composite onto white before looking.** Recorded because
  the failure mode is worse than a wasted rejection: a reviewer who sees black regions often
  enough **learns to ignore them**, which is exactly the habit the look pass exists to prevent.
- **The Scene7 `sku_list` is authoritative about which RECORD an image hangs on and silent about
  which PRODUCT it shows &mdash; and a mixed lot of 448 products put a number on how often that
  matters.** Of the rejections, a large share read *&quot;the `sku_list` contains this SKU but the
  record bundles N catalogue numbers and none of its assets names this SKU&quot;*: `SPXCDULNG1` sits
  in a record bundling **242** catalogue numbers under two assets both named `Sensepoint_XCD`;
  `DNRA` in one bundling 4 under 20 assets, none naming it; `CCM2-ANTKIT-EXT2` in one bundling 5.
  **A family record is not a per-part attribution**, so the structured join has to be gated by the
  filename rule and not trusted in its place. This file already records that principle from the STI
  `modelId` case; the new part is the scale &mdash; the bundling is the normal shape of Honeywell's
  index, not an edge case.
- **The duplicated-vendor-token scan's false positive is STRUCTURAL and has now fired
  twice, and checking it is what stopped a title being broken.** The mechanism returned two
  rows. `Notifier Notifier NC-100` is real and was fixed. **`STI STI EP141207-T` is
  correct**, because **the Shopify `sku` field for that product is literally
  `STI EP141207-T`** &mdash; the vendor is inside the SKU, so the title is vendor + SKU
  exactly as it should be, and removing one `STI` would leave a title that no longer
  contains its own SKU. That is the recorded Macurco Cal-Kit shape on a second brand.
  **So the guard is not &quot;use the real `sku` field&quot; &mdash; this scan already
  does.** The guard is the assertion that runs after the edit: **the SKU must still appear
  verbatim in the new title**, which is what refused this row. A no-claim edit still needs
  its postcondition checked, because the mechanism that finds a defect and the mechanism
  that proves a fix safe are different mechanisms.
- **A dropped letter in a Shopify title, and the manufacturer's own product record settles
  it rather than the dictionary.** The same STI title read *&quot;EnviroArmour Waterproof
  **olycarbonate** NEMA Enclosure&quot;*. It is tempting to call that an obvious typo and
  repair it &mdash; but this file records from `Ten-Xone` that **correcting an obvious typo
  is still writing a new title and needs the same source as any other**, and here the
  repaired word is a **material**, which STI does vary (it sells fiberglass enclosures too).
  Settled positively: STI's own CMS product document for `modelId: EP141207-T` is titled
  ***&quot;EnviroArmour&reg; Polycarbonate Enclosure - Tinted&quot;***. Fixed, with the
  assertion that the new title is exactly one character longer than the old.
  **Route note, and it extends a recorded one:** this file records the STI Sanity dataset as
  an **image-asset** index queryable by `originalFilename`. It also serves **product
  documents**: `*[_type=="product" && modelId match "EP141207*"]{modelId,title,_id}` returns
  the manufacturer's own model-attributed title. Bogus pattern &rarr; `[]`, so the endpoint
  is honest. **That makes it a first-party structured source for STI class nouns and
  materials, not only a route to pictures.**

- **The title-duplication half of that scan is nearly clean, and its one hit is a false positive
  with a known cause.** Six groups of identical titles, 14 products, **every group inside one
  vendor** &mdash; four Det-Tronics and two Kidde Fenwal. The Det-Tronics groups are the recorded
  brand convention working as designed (the **title** carries the ordering code `PIRECLA11A1T1`
  and the **SKU** the internal stock number `014046-201B`), so the titles are not wrong in kind
  &mdash; but three products share one title and **their pages are identical except for the stock
  number buried in the body**, which is the only place the `B`/`E`/`P` suffix appears at all.
  **One of those three costs $721 more than the other two**, while both sibling families price
  every suffix identically, so either that price is wrong or the suffix means something no
  visible field carries. Flagged, not touched.
  Worth pairing with the outcome of the brand-and-SKU-repetition re-run on the same pull:
  **exactly one hit, `STI STI EP141207-T`, and it is correct** &mdash; the `sku` field is
  literally `STI EP141207-T`, vendor plus a space plus the part number, so the title is vendor
  plus SKU. The postcondition that refused it (*the SKU must still appear verbatim in the new
  title*) is what makes that scan safe to apply unilaterally, and it has now held twice.

