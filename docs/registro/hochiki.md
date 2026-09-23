<!-- Registro de casos do projeto TFAS. Movido VERBATIM de CLAUDE.md em 23 Sep 2026; nada foi reescrito. Nao e carregado automaticamente: leia sob demanda. E cronologico: entradas posteriores corrigem anteriores; em caso de conflito vale a mais recente e o nucleo em CLAUDE.md. -->

# hochiki

- **Three live defects in one batch that all sit in the DESCRIPTION and not the title,
  and one that sits in the title alone.** `FSL100-IR3-W`'s certification string
  (`Div2EN54-10` is two approvals joined at a lost bullet &mdash; substantively correct,
  just unreadable), `DVP-120M`'s *&quot;120V&quot;* (it is a **90&ndash;250 VAC universal
  input** panel, stated identically in a 2016 manual and a 2025 data sheet), and
  `FN-PS776`'s *&quot;220V&quot;* (Hochiki documents **120 or 240 VAC selected by jumper
  R72** &mdash; fitted is 120, removed is 240, and **there is no 220 V setting**). Against
  those, `429022`'s wrong agent class sits in the **title**. **Saying which field each one
  is in is what sizes it**: three cost the page, one costs the page and the Merchant
  Center feed.
  `FN-PS776`'s *&quot;9th Edition&quot;* was **confirmed** as UL 864 9th Edition rather
  than a product revision, by a replacement-parts table listing `FN-PS4` as 8th Edition
  against `FN-PS402` as 9th &mdash; **one character changes the UL edition on this brand**,
  which is a sibling trap worth keeping.
- **URL-counting cannot work at all on a derived-path host, and MD5 is what replaces it.**
  Every Hochiki product has **its own** derived URL, so URL reuse is zero by construction
  and rule 6's counting method returns nothing. MD5-ing the indexed library &mdash; 519
  codes, 562 images &mdash; found **139 codes (27%) serving bytes identical to another
  product's**. That killed two rejections the counting method could never have seen:
  `0600-01440` (HPS-D**BB**, the *deep* back box) is byte-identical to `0600-01430` (the
  standard one), **and depth is the entire difference between the two products**; and
  `HCVX8-R`, an **8**-zone panel, is byte-identical to the **4**-zone `HCVX-4R`.
  **The converse also held, which is why both checks are needed:** MD5 called
  `0500-06180` unique and only looking caught that the unit in the photograph is **white**
  where the SKU's own sibling naming fixes the trailing letter as **red**.
- [CORRIGIDO — `hochikieurope.com/casestudies/` tem renders por peça; ver neste arquivo &quot;SIXTH TIME&quot;] **A brand can be two companies, and the coverage number is meaningless until you split
  them.** Of 798 Hochiki SKUs, **369 are Hochiki *Europe* part numbers** (`1226370-00`
  shape), and **Hochiki Europe publishes no per-part images at all** &mdash;
  `hochikieurope.com/images/products/` is keyed by *range* (`esp-intelligent-`,
  `cdx-conventional-`), the same family-asset pattern that made Det-Tronics a true zero,
  and its AssetBank DAM returns **the identical 14,749-byte login page for a real and a
  bogus keyword**. Every one of the 22 hits is Hochiki **America**. So &quot;Hochiki
  2.8%&quot; is really *a usable route on 429 products and a documented zero on 369*.
  Three more recon corrections from the same run: Secutron **16% &rarr; 6.1%**, Napco
  **&quot;no&quot; &rarr; 1.8%** (bounded by probing all 167 SKUs across 7 filename
  spellings and 2 extensions, 1,568 requests, against a clean 280-byte 404), and Hochiki
  **3&ndash;15% &rarr; 2.8%**, at or below its own floor.
- **A search endpoint whose MD5 and byte count both differ from a bogus control and which
  still returns a false negative.** `safefiredetection.com`'s site search gives 144,058
  bytes for a real query against 144,085 for a bogus one, and the real term appears seven
  times in the response &mdash; **every occurrence an echo** (title, `og:url`, input value),
  with **zero product rows**. The part *is* on the site, on its category page. So **a
  hash-only or byte-only bogus control passes this one**, where it caught Hochiki's
  `productsearch`. Third instance after Hochiki and Interstate Batteries, and the rule is
  now unambiguous: **the test is whether the response CONTAINS WHAT YOU ASKED FOR**, not
  whether it differs from a control.
- **A FIFTH non-discriminating search endpoint, and the byte count is the tell for the fifth
  time.** `hochikieurope.com/?s=` returned **exactly 39,632 bytes** for a real term, a second
  real term and a bogus term, differing in MD5 only because the page echoes the query. After
  `hochikiamerica.com/ecom/productsearch`, `pottersignal.com/search`, Interstate Batteries,
  safefiredetection and Napco's tag index, this is now a *category* of host rather than a
  quirk. **The reliable test remains whether the response contains what you asked for.**
  And the same brand confirms the converse from the other side: **Hochiki America has two
  search routes and only one is honest** &mdash; `/products-search?qs=` discriminates and
  prints *&quot;There are no results for this search&quot;*, and it is what produced both
  Hochiki positives here.
  New first-party routes mapped: **Hochiki Europe's document library is open and enumerable**
  through `hochikieurope.com/product/<range>`, which embeds
  `assets.hochikiglobal.com/assetbank-hochikieurope/assetfile/<id>.pdf` links &mdash;
  `assetfile/16132.pdf` is the 56-page **Product Guide ISS33:MAR26** carrying a model-attributed
  entry for every ESP part **plus a colour-swatch legend and the parenthetical colour
  convention** (`YBO-R/3(WHT)`, `CHQ-CB (WHT)/WL`). And **Hochiki America serves datasheets at
  `hochikiamerica.com/img/product/description/<Name>_<MM-YYYY>.pdf`**, honest 302-byte 404,
  with product URLs of the form slug-plus-code (`/ms-ra-remote-alarm-led-0400-01270`).
- **A RECORDED NEGATIVE DECAYED FOR THE SIXTH TIME, AND THE SHAPE IS NEW: THE NEGATIVE WAS
  ABOUT ONE DIRECTORY AND WAS SILENTLY GENERALISED TO THE HOST.** This file states that
  *&quot;Hochiki Europe publishes no per-part images at all&quot;* because
  `hochikieurope.com/images/products/` is keyed by **range**. The range keying is true; the
  conclusion is false. **`hochikieurope.com/casestudies/` carries high-resolution per-part
  studio renders human-named with the catalogue number** &mdash; `ALN-EN-WHT.png`,
  `ATJ-EN(WHT)_plan.png`, `CHQ-POM (cmyk300dpi).jpg` at 3008&times;2000,
  `CCP-W-IS CALL POINT 3060 V2.1106.png`. **Five of the batch's six hits came from a directory
  called &quot;casestudies&quot;**, which nobody had opened.
  Every previous instance of this rule was a negative that *expired* &mdash; a host changed, a
  path moved. **This one was never true as stated**: the measurement was correct and its scope
  was widened by a sentence. So the rule needs a second half: **when recording a host-level
  negative, record the path you actually tested**, because a bare &quot;this brand publishes
  nothing&quot; cannot be audited and therefore never gets re-run.
  **And the complementary rule held exactly:** a construction probe of
  `/casestudies/<sku>.png|.jpg` over all 776 SKUs in six normalisations &mdash; **~3,100
  requests against a clean 1,027-byte 404 control** &mdash; returned **one hit, already known**.
  The filenames are human-authored prose. What worked was crawling the sitemap and matching
  longest-SKU-owns-file. **Find the filename, do not build it**, for the eighth or ninth time.
- **The shared-identifier placeholder signature, at 1/60th the scale of the one this catalogue
  started from.** Hochiki Europe's BIM icons at `images/resources/*-bim-object-*.png` are all
  **71&times;93**, with **17 files byte-identical** at one md5 and 3 more at another &mdash; a
  per-SKU *filename* over one icon. That is the grey `MediaImage` mechanism exactly (7,738
  products, one id), and it would pass any check that looked for a null or a missing file.
  **Count products per identifier, whatever the scale.**
  New fingerprint from the same host family: the Azure CDN derived path
  `hochikiamerica-1.azureedge.net/img/product/<CODE>_1-Z.jpg` 404s at **302 bytes `text/html`,
  md5 `62aae8b5…`**, identical for three invented codes &mdash; **and the path is
  case-insensitive**, so `_1-Z.JPG` returns byte-identical bytes and a naive shape sweep
  double-counts its own hits.
- **Hochiki measured properly: 6 of 776 (0.77%), and the denominator is the full 776.** A regex
  sweep for licence, software, training, certification, freight, calibration and service over
  all 776 titles returns **zero** &mdash; this brand has no non-photographable rows, so unlike
  Notifier, Space Age or Kidde Fenwal the rate is not hiding a padded denominator.
  **The binding ceiling is catalogue coverage: 745 of 776 (96%) own no asset of any kind on
  either Hochiki host**, because 368 are Hochiki *Europe* numeric codes (`1212300-00`) that
  Hochiki America's catalogue cannot contain. Of the 26 SKUs that *do* own a filename,
  **19 die on image size** &mdash; seven have a genuinely per-part Europe image at **100&times;90**
  with no larger rendition, and twelve resolve only to the 71&times;93 BIM icon. **Matching was
  never the constraint**: every one of the 26 was resolved. Three ceilings, and only the
  smallest of them is the one a better matching rule could move.
  Paging is broken three ways on that site and is worth not chasing: `&page=N` is **silently
  ignored** (byte-identical 143,361 B for pages 2 and 3), the `href` the page prints returns
  **404 at 38,814 B**, and the AJAX endpoint returns **HTTP 500** with every field its own
  JavaScript sends. A 126-term vocabulary sweep built the census instead.

- **THE 75-TITLE DEDUP WAS CASE-SENSITIVE AND LEFT SIX BEHIND, AND THE LAST TWO SWEEPS BOTH
  REPORTED ZERO.** Re-run against a live pull with a **case-insensitive** comparison, the
  brand-and-SKU-repeated mechanism returns **6**, not 0:
  `Hochiki CWSB-E BACKBOX Hochiki CWSB-E **Backbox** &hellip;`,
  `Ultratech IM-12180 **UltraTech** IM-12180 &hellip;`, and four more. In every one the second
  copy differs from the first **only in capitalisation** &mdash; `BACKBOX` against `Backbox`,
  `Ultratech` against `UltraTech` &mdash; so the original fix's own verification, which is
  what the batch-40 and batch-43 sweeps reproduced, could not see them.
  **The lesson is not &quot;lowercase your comparisons&quot;. It is that a fix and its
  verification shared a defect**, so the check confirmed the fix on exactly the population
  the fix could reach and was blind on exactly the population it missed. **Two clean sweeps
  in a row measured the same blind spot twice.** Where a mechanism is used both to *apply* a
  change and to *verify* it, a second, differently-written check is the only thing that can
  find what both missed &mdash; and the cheapest version is to vary one parameter, here case.
  All six fixed under the same no-claim guards as the 75 (the new title a literal prefix
  removal, strictly shorter, ASCII, &le;150, balanced parentheses, SKU still present).
  **Two riders went to the owner rather than into the edit**, because the dedup is a no-claim
  edit and these are not: `IM-1272F1` carries an **unverified &quot;(Replaces IM-1270)&quot;**
  and `HCP CALL POINT KEY` carries an **unverified &quot;10 Pack&quot;**. Removing either is
  a claim; the duplication fix is not. **Fix only the part of a defective title that decides
  nothing.**

### t07 (23 Sep 2026)

- **DH-101-A** (datasheet Rev 2 07/2026, installation instructions HA-06-485 06/25) is an **addressable DCP duct detector with the ALO-V head included**, not a bare housing. The two documents disagree on the head type ("Analog Photoelectric" vs "Multi-Criteria"), so neither word was used. Only the 7.5 in. exhaust tube is in the kit; the STS-2.5/5.0/10.0 intake tube is ordered separately.
- **WHES24-75WR** (F0134 Rev2 08/2025): part code 0500-05780, 75 cd, 24 VDC; "W = Wall mount, R = Red faceplate", so R is the faceplate colour, not the lettering. Datasheet filenames carry stale dates (`WHE_Series_10-2021.pdf` is Rev2 08/2025).
- An exact-code query to `/products-search?qs=` redirects to the product page with no result links; the bogus control prints "no results". A bogus datasheet name returns a 302 B `text/html` 404.
- This prompted the Hochiki twin scan (see varreduras-e-auditorias.md): 32 model-vs-part-code duplicate pairs.
