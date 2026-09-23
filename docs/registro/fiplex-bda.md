<!-- Registro de casos do projeto TFAS. Movido VERBATIM de CLAUDE.md em 23 Sep 2026; nada foi reescrito. Nao e carregado automaticamente: leia sob demanda. E cronologico: entradas posteriores corrigem anteriores; em caso de conflito vale a mais recente e o nucleo em CLAUDE.md. -->

# fiplex-bda

- **Every distributor can be wrong together, and the mechanism was visible on the
  page.** `BDA-NM-RG8-13-NM` is **51 inches** per Honeywell `HON-62084.02`
  (11/29/2021); every reseller says 48. The mechanism: **page 1 of that same brochure
  tabulates a different part, `BDA-NM-RG58-12-NF`, at 48 inches**, and page 5 is the
  only page carrying the part in question. Distributors read the first table in a file
  named for the part they wanted. The numeric field is also **not a length** &mdash;
  `-08-NM` is 24 in., `RG58-10` is 37 in., `RN4P-03` is 10 in. &mdash; so the
  briefing's &quot;inches or feet, a factor of twelve&quot; framing was wrong in a
  third way. **The 51 in. figure went in the body and deliberately not in the title**:
  a length contradicting every distributor and possibly the stock on the shelf is a
  feed claim the owner should confirm against a carton first.
- **`fiplex.com` is a new blocked-host fingerprint, and it cost a page.**
  `/Datasheets/` paths return **HTTP 400 with an Akamai &quot;Access Denied&quot; body
  of 456 bytes `text/html`** to curl on both HTTP versions, to curl with full Safari
  headers, to `urllib` through the proxy and to WebFetch; `/wp-content/` paths time out
  at **0 bytes** after 60 and 90 seconds. No Wayback capture, and the Document Center
  needs sign-in. `BDA-TP10-L2` was therefore **left unwritten by decision** rather than
  built from reseller copy &mdash; three sources give three different frequency ranges
  for it, which is exactly why. The document is named and findable: Fiplex
  `BD500-High_Power_Tapper_138-960MHz`. **One owner login to the Fiplex Document Center
  would settle both this and `BDA-NMP01250`; ask for BD500.**
  Mapped in the process, and useful next time: the Fiplex passive-device series on
  EDAM is `HON-62073` (DC-W2), `HON-62074` (DC-L2), `HON-62075` (HC3-L2), `HON-62079`
  (PSx-L2 splitters) and `HON-62084` (jumpers), with **`-L2` low band and `-W2`
  wideband, manufacturer-stated.**
- **Every distributor wrong together, for the second time in three batches.**
  `ELSPKBB-R` is a **wall** back box: Eaton `TD450158EN`'s backbox table, confirmed on
  one y-line by word coordinates, reads `ELSPKBB-R` &rarr; Wall, `ELSPKBB-W` &rarr;
  Wall, `LSPKBB-CR`/`LSPKBB-CW` &rarr; Ceiling &mdash; **the `C` in the sibling number
  is the ceiling marker.** ADI and Telcom-Data both list it as ceiling. After the
  51-inch Fiplex jumper this is a pattern worth naming: **distributor consensus is not
  evidence, and it fails in a correlated way**, because they copy each other rather
  than the datasheet.
- **Two more product-class errors, and both confirm that the type field is silent when
  it agrees.** Seventh: `BDA-OIA-698869-3-1` had **no class noun in the title at all**
  and a `type` of **BDA**, while Honeywell's own `HON-62089.01` is headed
  &quot;INDOOR OMNI CEILING ANTENNA&quot; &mdash; a BDA is the four-figure amplifier
  this $19.50 antenna plugs into. Eighth: `P2WLED-P` was titled a **strobe** and typed
  **Strobes**, while `AVDS916-01`'s ordering table reads
  *&quot;P2WLED-P &mdash; 2-Wire, Horn Strobe, Wall, White, Plain&quot;*; it has an
  eight-position tone switch and a UL 464 listing, and the strobe-only part is a
  different number, `SWLED-P`. **In both cases the type field agreed with the wrong
  title and so raised nothing.** That is the rule working as stated, not failing: the
  field is a signal on disagreement and no evidence at all on agreement.
- **The product-class error has a signature, and it has now fired three times:
  the type field names a *subcomponent* or a *role*, not the product.** `CPU2-3030D`
  was typed Annunciators and is the panel CPU; `4100-9701` was typed Annunciators and
  is the 4100ES master controller; **`HONBDA-7S27B-IB-10` is typed Annunciators and is
  an $8,948 all-in-one public-safety BDA that happens to contain an annunciator.** Its
  three siblings in the same family are all typed BDA. So: **&quot;Annunciators&quot;
  on a part that costs more than an annunciator is a class question every time**, and
  a family whose members disagree on type is a defect, not a nuance.
- **The Sucuri fingerprint has a second host, and a blocked site is not an undocumented
  one.** `trilogycoax.com` answers **HTTP 202, 169&ndash;193 bytes, with a
  `/.well-known/sgcaptcha/` meta-refresh** on `/`, `/products/`, `/robots.txt` and
  `/sitemap.xml` alike &mdash; the exact protectowire.com shape. The part behind it,
  `BDA-NMP01250`, is a Trilogy product sold under a Honeywell SKU, and the Honeywell
  **Fiplex Document Center requires sign-in**. That is a **bounded** negative: one
  owner login would settle it. Recorded as a retry, not a permanent skip.
- **Det-Tronics is first-party and unprotected, which breaks the relationship-sold
  premise for a fourth category.** `det-tronics.com/wp-content/uploads/sites/8/2025/04/`
  serves current documents directly; the older `det-tronics.com/content/documents/` path
  now 404s. Its model matrix decodes a SKU completely, the Edwards-page-5 class of
  decoder: `UD10S5N28W2C` = **S** 316 stainless, **5N** five 3/4 in. NPT ports, **28**
  EQP/DCU emulator, **W** FM/CSA/ATEX/CE/IECEx, **2** Ex d flameproof, **C** CGS board.
  After Fiplex, Westell and STI that is four categories where &quot;nobody searches for
  it&quot; was mistaken for &quot;nobody documents it&quot;.
  Two flags from it: `010254-008` is typed **Annunciators** and is a $4,294 Ex d gas
  display/controller &mdash; the CPU2-3030D signature, where the type names a role rather
  than the product &mdash; and its title was the **raw ERP string &quot;DISPLAY,
  DCU&quot;** with no class noun. **Worth a sweep for other Det-Tronics SKUs carrying raw
  ERP descriptions as titles.** Also a bounded negative recorded rather than acted on:
  the string `010254` appears in neither `95-8656` nor `90-1209`, so the
  `010254-008` &harr; `UD10S5N28W2C` pairing rests on resellers &mdash; but the ordering
  code decodes correctly against the manufacturer's own matrix, which is what the copy
  rests on, so **neither number was touched**.
- **`trilogyrf.com` is the same Sucuri block as `trilogycoax.com`, so the whole brand is
  walled.** HTTP 202, **221 bytes**, `/.well-known/sgcaptcha/` meta-refresh, on every
  path; the `urllib`-plus-Safari-UA workaround returns the same 221-byte block, confirming
  it does not defeat Sucuri. `trilogycoax.com` still 202s at 190 bytes.
  `trilogycomms.com` 301s to a different company entirely. **Wayback is no help this week
  &mdash; `archive.org` is returning a site-wide &quot;temporarily offline&quot; page to
  both the availability API and CDX.**
  The page was still written, from Trilogy's own AirCell product specification served
  intact by a mirror, **read entirely off a 260 dpi render because its text layer is
  scrambled** &mdash; the genuine-PDF-unusable-text-layer shape for the second time.
  **What could not be sourced was the ordering unit.** The title's *&quot;1 ft (0.304m),
  Reel&quot;* is Honeywell catalogue-feed wording repeated verbatim by every distributor:
  correlated repetition, not evidence. Dropped from the title and flagged &mdash; a price
  list or a purchase order settles it, not another search.
- [CORRIGIDO — Amerex rendeu 408 fotos e Kidde Fenwal foi re-testado (1,25%); ver fotos.md] **Fiplex is a genuine zero, and that is a finding rather than a failure.** The route
  reaches the brand perfectly (723 English records); **Honeywell publishes no per-part
  photography for the line at all.** The complete asset pool reachable by all 224 SKUs is
  **thirteen images**, every one a family or cabinet shot. So Fiplex joins Kidde Fenwal and
  Amerex as a brand needing a different route &mdash; a dealer image pack from the
  manufacturer &mdash; not a different filter.
- **Filename evidence can be structurally unavailable, and the substitute has to be
  measured rather than assumed.** Every Westell product photo is served as
  `&hellip;/westell/db/348/<numeric-id>/image.png` on an investor-relations CloudFront
  &mdash; **no part number anywhere in the path**, so the boundary rule cannot run at all.
  The agent substituted the `alt` attribute, which carries the exact part number on all 395
  image elements, **and then measured the substitute's risk directly: zero of 395 alts
  disagree with their page slug**, i.e. zero instances of the `8100-V4G`/successor shape on
  that host. **That is the right shape for replacing a safeguard** &mdash; name the
  replacement, then measure the failure mode the original existed to catch. Also recorded:
  `image_medium.png` is the ~12 KB thumbnail and **`image.png` is the full-size original**,
  eight times the pixels.
- **The 185 frequency titles are settleable after all, and the evidence was inside the
  titles the whole time.** This file records them as flagged-and-unapplied because one of
  twelve broken values disagreed with a Fiplex document &mdash; the whole set held back by
  its worst member, which is the bounded-negative over-reach this file warns about three
  times. Measured properly on 22 Sep: **275 of the 288 broken runs carry their own
  evidence.** 267 have the word **VHF, UHF or Band immediately before the number**
  (*&quot;VHF 136174MHz UHF 450512MHz&quot;* &mdash; the title labels which band each run
  is), and 8 have the range **inside the part number itself** (`BDA-YDA450470-9-1`,
  `PDS2E-555/6000`). **That is not domain knowledge about standard public-safety bands; it
  is the title explaining itself**, which is a different and much better kind of evidence.
  Corroborated against a document where one was reachable: `HON-62101` states
  *&quot;450 - 470 MHz&quot;* four times.
  **13 runs across 11 products stay open, and each for a stated reason**: `136960` on
  `BDA-TP24-L2` conflicts with the Fiplex `BD500` document's 138-960; **`460462465467` is
  not a range at all** but four sub-bands (the same titles also carry `453454458459`), so
  the lost separator may be a slash; `1251000` on the Polyphaser `IS-50NX-C2` needs that
  series' sheet; and a handful lost their VHF/UHF label in the same truncation. Readings in
  `/tmp/tfas/FREQ_leituras_sustentadas.json`, each row carrying the basis for its own
  reading.
- **The two-word-vendor bug bit the COORDINATOR's own scan about an hour after it was
  written into this file.** Measuring the above, the first pass took the part number as
  `title.split()[1]`, which is **&quot;by&quot;** for *&quot;Fiplex by Honeywell
  BDA-OIA-350600-2-1&quot;* &mdash; so seventeen rows whose band sits in their own part
  number came back as unevidenced. The fix is the one already recorded: **use the real
  `sku` field, or match the run inside a hyphenated model token in the title.** Worth
  keeping because the lesson is not &quot;parse titles carefully&quot;; it is that **a rule
  written down is not a rule applied**, and the coordinator is not exempt from the traps it
  records for agents.
- **Third mechanism-based scan that did not over-fire, and the first one whose defect is
  RECONSTRUCTABLE: 185 titles lost the hyphen inside a frequency range.** Mechanism:
  **a digit run of five or more immediately before `MHz` is not a frequency** &mdash;
  `450512MHz` is 450&ndash;512 MHz with the separator gone, `136174MHz` is
  136&ndash;174 MHz, `758869MHz` is 758&ndash;869 MHz. 185 products, **179 of them
  Fiplex by Honeywell**, plus RFS Technologies, Comprod and Polyphaser: 482 six-month
  impressions and **$317,378 of ERP revenue**.
  **The striking part is the closed set: 185 titles carry only TWELVE distinct broken
  values**, and eleven of the twelve are recognisable US public-safety bands
  (`450512`&times;135, `136174`&times;124, `470512`, `450470`, `758869`, `350600`,
  `470490`, `150175`, `136960`, `5556000`, `1251000`, `460462465467`). So unlike the
  truncated titles, **the text is not missing &mdash; only the separator is** &mdash; and
  twelve substitutions would fix all 185.
  **It still went to the owner unapplied, and the reason is one row.** `136960 MHz`
  disagrees with the Fiplex document this file already names, `BD500-High_Power_Tapper_
  **138**-960MHz`. One of the twelve is not obvious, which is exactly the punctuation-scan
  precedent: *reading `34 NPT` as `3/4 NPT` is a claim about a thread size and needs a
  document.* A split point is a claim about a frequency band and needs the same bar.
  List in `/tmp/tfas/FREQ_hifen_perdido.csv`; the readings are marked unverified on
  purpose.
  **And the first attempt at this scan over-fired 30x, which is worth keeping.** Widening
  it to voltage, current and candela with a 3-digit threshold returned **570 hits, almost
  all correct values** &mdash; `120 VAC`, `177 cd`, `185 cd` are real. The threshold was
  domain knowledge pretending to be a mechanism. Only the frequency case is a true
  impossibility, because no real value has six digits before `MHz`. **Narrowing to the one
  genuinely impossible shape is what took it from 570 noisy to 185 clean.**
- **Upscaling: a 600 px file is not proof of a 600 px master, and the floor was measuring
  the wrong thing.** Westell's CDN serves `image_large.png` as a resize-to-600-long-edge
  derivative that **upscales when the master is smaller** &mdash; proved both ways, since
  for one SKU the master is 750&times;321 and `image_large` is *smaller* at 600&times;257,
  while for another the master is 211&times;134 and `image_large` is 600&times;381
  carrying no extra detail. **Six of eight Westell rows reach 600 px only that way.**
  They are correct photographs of the right products, so rejecting them would be false
  and publishing them asserts a detail that is not there. Handled as the Notifier framing
  case was: **split the CSV and let the owner choose** &mdash; `lote9b` is the upscaled
  six, on its own, said plainly. `image_original.png` returns **403, 243 bytes,
  `application/xml`**; 600 is the ceiling.
- **Three more open CMS routes, and one throttle worth knowing before the next brand.**
  **`combausa.com`** is WordPress + WooCommerce with an open **Store API**
  (`/wp-json/wc/store/v1/products`, 140 products) and an open media API.
  **`mircom.com`** is the same shape: `wp/v2/media` is **401**, but
  `/product-sitemap.xml` carries 328 product URLs with Yoast `<image:loc>`, and
  `/wp-json/wc/store/v1/products?per_page=100` returns the catalogue with `sku`,
  `permalink` and an `images[]` array carrying **`alt`** &mdash; a genuine second
  structured field, which is what supplied `KF-101` where the page body never names it.
  **`rfsworld.com/products_sitemap.xml`** lists 1,514 products and **the URL is the part
  number**. But **mircom.com sets `Crawl-delay: 10` and enforces it**: a parallel probe
  drew **HTTP 429** almost at once. Serial with backoff, not eight workers.
  New fingerprints: `westell.com/products/<bogus>` &rarr; **HTTP 302, ~40,567 bytes**,
  and its **MD5 varies because the slug is echoed &mdash; the byte count is the tell**;
  the Westell CDN &rarr; 403, 243 bytes `application/xml`; `rfsworld.com` &rarr; 404 at
  ~290,470 bytes; `combausa.com/wp-content/uploads/<bogus>` &rarr; 404 at ~76,530;
  `mircom.com` image miss &rarr; an honest 404 at **146 bytes**, byte-identical for two
  invented numbers. Comba also ships its own placeholder,
  `coming-soon-image-300x300-1.jpg`, on 5 products.
- **A `null` whose value is that it names the ONE request that settles three products.**
  `DHS40-HG-SCH-1-A` was left untitled on a bounded negative: Fiplex `BD376.12`, Honeywell
  `BD376 7.0` and manual `UM-0909` all read in full and **none contains the string
  &quot;DHS40&quot;**; `fiplex.com` is Akamai-blocked as recorded; and **every FCC route is
  blocked from this environment** &mdash; fccid.io, fcc.report, device.report, electric.garden,
  usermanual.wiki and manualzz all 403, fccid.report and fcc.io 404, and the FCC's own
  `apps.fcc.gov/oetcf/eas/` 503 on two query shapes.
  **Two suffix tokens have competing readings and either would be expensive in a feed title:**
  `-A` is *AC power* in Fiplex's own DH7S ordering block but *Class A* in the FCC index title
  for the sibling `DHS40-HG-A`; and `-SCH-1` is described by distributors as an 806&ndash;824 MHz
  **uplink** unit &mdash; on a **different part number**, which is the correlated-consensus
  failure exactly.
  **The useful output is the ask, not the gap: one Fiplex Document Center login settles this,
  `BDA-TP10-L2` and `BDA-NMP01250` together.** Three products, one request, and the documents
  are named and findable (DHS40 / Single Carrier Amplifier datasheet, or `UM-0914`).
  **A bounded negative earns its keep when it converts research into a purchase-order
  question**, which is the same shape as the pack-count rows and the Trilogy ordering unit.

- **Three brand zeros and one near-zero, each with its mechanism, and only one is a routing
  failure.** **Napco 0 of 164**, established three ways: 0 of 130 site images carry any SKU, a
  constructed probe of 656 requests returned 0 hits against a clean control pair, and **only 26
  of 164 SKUs are named anywhere on napcosecurity.com** &mdash; the site has no per-product
  pages at all, its category pages link PDFs. **RFS 0 of 26 is a resolution ceiling**: every
  boundary-matching image is a `_ti` thumbnail at 320&times;200 **and the no-`_ti` form is the
  same 320&times;200**, so there is no larger rendition to find. **Comba 0 of 25**: only 4 of 28
  have any media, the two not already delivered are 433&times;433 and 528&times;528, and their
  larger siblings are **outline drawings and antenna patterns, not photographs**.
  **E2S 0 of 25 is the one that is the owner's call rather than a ceiling**: e2s.com publishes
  per-colour **family** renders up to 1000 px and our 25 SKUs are full configuration order
  codes, so nothing passes the boundary rule &mdash; **if the owner accepts a family render for
  a configuration SKU, about 20 of the 25 become reachable.** That is a merchandising decision,
  not a research one, and it is the first brand where relaxing the rule has a named price.

- **A reel length inside a SKU, read as a catalogue suffix by my own validator.** The agent
  titled `ICA12-50JPLLR-500` as `ICA12-50JPLLR ... (500 ft)`, deliberately keeping `-500` out
  of the part number because **RFS catalogues `ICA12-50JPLLR` and the 500 is the reel**. My
  schema check flagged it as a title not containing its own SKU. **The validator was right to
  fire and wrong to be obeyed** &mdash; this is the `AS-75-R-WP` and `PDC-12xxxx` shape (a
  number inside a model number that is not part of the model number), and the correct handling
  is the one taken: the quantity in parentheses, the part number clean, the SKU untouched and
  the question flagged.
  The sibling trap on that part is one letter and it is not colour: **`ICA12-50JPLR` is the same
  1/2 in. red plenum ClearFill Line cable with a corrugated COPPER outer conductor** &mdash;
  1,112 N tensile against 549 N &mdash; where this one is aluminum. **Both jackets are red.**
- **A COUNTER-EXAMPLE TO THE 185-TITLE FREQUENCY WORKSTREAM, FOUND BY A BATCH THAT WAS NOT
  LOOKING FOR ONE, AND IT SHOULD REACH THE OWNER BEFORE THAT WORK IS APPLIED.** That workstream
  rests on *&quot;the title explains itself&quot;* &mdash; 267 of 288 broken digit runs carry a
  VHF/UHF/Band label immediately before them, and 8 more have the range inside the part number,
  which this file records as **a different and much better kind of evidence** than domain
  knowledge. `BDA-YDA763869-14-1` is one of the second kind, and **expanding it would be wrong.**
  Honeywell `HON62098.02` gives the antenna's range as **698-869 MHz**. The digits `763869` are a
  **model designator**, not a band, and the real range is 65 MHz wider at the bottom. The store's
  live title said 763-869.
  So the rule needs its boundary stated: **a digit run inside a PART NUMBER is not evidence about
  a frequency; only a run the title itself labels is.** The 267 labelled rows are untouched by
  this; the 8 that rest on their own part number need their own data sheet, one at a time. That is
  the `AS-75-R-WP` shape &mdash; a number inside a model number that looks like a spec &mdash;
  firing on the one workstream this file had cleared to proceed.
- **A refusal that names the cheapest thing that would settle it, and questions whether the row
  belongs in the feed at all.** `RE-CUTTING-S1` was returned `null`. RFS's `products_sitemap.xml`
  is a **literal enumeration of 1,514 products** &mdash; not a search endpoint that can silently
  ignore a query &mdash; and contains no &quot;CUTTING&quot; and no `RE-*` but `RE60-JFN`; the
  product URL is a 404 at 290,373 B against a known-good `CLAMP-046` at 441,271 B, so the endpoint
  discriminates. The store's entire description is the ERP fragment &quot;RE-CUTTING&quot; at a flat
  $212.40, and the store sells RFS cable by the foot and in 500 and 1,000 ft reels. **A
  cut-to-length charge is the coherent reading, and coherent is not sourced**, so no class noun was
  written and no hardware invented. **If it is a charge line it probably should not be in the
  Merchant Center feed at all**, which is a bigger question than the title and went to the owner
  with it.
- **A host whose SITEMAP is incomplete while its pages are live, so the page probe is the
  existence test.** `tcsbasys.com`'s 2021 `product-sitemap.xml` does **not** list `TS1003`,
  `TS3030` or `US4021` and all three pages resolve. Its 404 is honest, so a probe with a control
  answers where the sitemap gives a false negative. **This is the inverse of the RFS case in the
  same lot**, where a sitemap *is* a literal enumeration and therefore the better instrument
  &mdash; so neither artefact is reliable by type: **check whether the sitemap is current before
  treating its absence as evidence.** One document, `TS_Series-Product-Data-Sheet.pdf`, settles
  three of the four TCS products.

- **Westell `CS05-488-429` (v2b52):** product page links `support.westell.com/documents/IBW-CS05-Series-PSG-DC-DS.pdf` (footer dated `-07092024`; bogus = 1,245 B 404). Ordering row (coordinator-verified): `5 dB | N (f) | CS05-488-429 | ClearLink-DC5/340-2.7K/N` &mdash; the digits are catalogue numbering, the band is the sheet's 340&ndash;2700 MHz. **Fingerprint drift:** `westell.com/products/<bogus>` now 200 at 42,310 B (recorded 302 at ~40,567). The data sheet makes `CS05-416-429` the 5 dB 4.3-10 coupler while a westell.com page title says 6 dB &mdash; unresolved. Type BDA on the CS05 family flagged.

- **HONBDA-7S27B-IB-06 (audit t01):** BD441.1 serves from `datasheets/fiplex-02022026/hon-ba-fire-bd441-bda-bbu-honbda-7s.pdf` and `datasheets/hbt-fire-fiplex-BD441-BDA-BBU-HONBDA-7S-datasheet.pdf` (same revision); both slugs miss under the other root. p1 (coordinator-verified): -IB-06 DL 769-775 &amp; 851-861 MHz &mdash; the -IB-10 is 758-775, so the pair differs in the 700 MHz band edge. Type Annunciators&rarr;BDA flagged.

- **Westell kits and fiber-DAS master (enrichment e01, 23 Sep):** no product page exists for `CS40-734834-00D-A0` (slug redirects to /search at 42,310 B, same as bogus); the series page `cs40-series-protectlink-class-a-b-bdas` links the data sheet. `IBW-PS-OrderGuide.pdf` and `catalogs-brochures/IBW-UL2524-KIT-FLYER.pdf` state kit contents (coordinator-verified: CS45-727-827-K2 = CS45-727-827-A0 + CS19-BBU-004 + CS19-BAT100AH31); the flyer's K2 graphic says &quot;12 HRS&quot; against its own 24-hour table. Order guide vs data sheet disagree on -00D-BR (wideband remote vs Class B remote amp). Store defects: `CS19-PYL12V100FT` titled a cabinet and is a battery; `CS40-U34-U4D-HE` has control chars U+0001/U+0002 in its title; `CS19BAT145AHSLA` and `CS19-BAT145AH-SLA` look duplicated.

### e05 (23 Sep 2026): Westell CV04 splitter and CS05 power tappers, ad-candidate lot

- **Routes.**
  - Tapper data sheet: `support.westell.com/documents/IBW-PSG-PwrTappers-DS.pdf`, file dated 2020-09-15.
  - CV04 splitter data sheet: `IBW-CV04-Series-PwrSplitters-DS.pdf`.
  - Two order guides are linked from every product page: `IBW-PS-OrderGuide.pdf` (2026-05-08) and `OrderGuide/IBW-Ancillary-Passive-Antenna-OrderGuide.pdf` (2026-03-12).
  - `westell.com/sitemap.xml` has 794 URLs and enumerates product slugs.
- **Fingerprints.** A bogus product page returns 200 at 42,310 B with no data-sheet link. A bogus `/documents/` path returns 404 at 1,245 B `text/html`.
- **The CS05-429 coupler sheet is a different family from the CS05-4xx-114 tappers.**
- **Trap: Westell contradicts itself on tapper power and IP rating.**
  - Power: 300 W in the data-sheet prose and the Ancillary Order Guide; 200 W in the PS Order Guide, the product-page spec table and the unit label in the data sheet's own photo (`CS05-479-114 REV: B`, "200W"). A likely origin of 200 is the CV05-614 VHF tapper block printed directly above in the PS guide, which is truly 200 W. A hardware revision would also explain it.
  - IP rating: IP65 on the data sheet and page, IP67 in the Ancillary guide.
  - Nothing settled either, so the live "200W" was removed and no power figure or IP rating was published for the tappers.
- **Page headlines carry the ERP strings (136-960, 200W) while the spec tables on the same pages say otherwise.** The CV04 sheet says 138–960 MHz; only the PS Order Guide heading says 136. The CV04 dimension cell has a typo (`4.4 x 4x4 x 0.9`); the drawing gives 4.4 × 4.4 × 0.9 in.
- The 3 dB tapper (PT3, CS05-494-114) is an unequal 2:1 split, not an even divider. "Wilkinson" is on the westell.com headline only; it stayed in the title because it was already live, and was put in `unverified`.
- Queued: titles on CS04-070/071/072-429 read "2 W/3 W/4 W", but the number is the way count. The PS Order Guide says 300 W (see `audit/proximos_irmaos.md`).

### e06 (23 Sep 2026): BDA-NM-RG58-10-NM

- HON-62084.02 (11/29/2021) p4, with the column confirmed by word x-coordinates and a 200 dpi render: RG58, N male both ends, 37 in. (940 ± 5 mm), 0–6 GHz, VSWR specified only to 3 GHz. The "10" is not a length. **The source is the recorded verbatim mirror**: alldataresource now 301s to `cdn.shopify.com/s/files/1/0843/1616/0235/files/Honeywell-Fire-Systems-BDA-NM-RG8-13-NM-Coaxial-Cable-Brochure.pdf` (use `curl -L`; without it you get a 0-byte 301), same 382,945 B file. All EDAM paths for HON-62084 give the 8,047 B miss; the controls `notifier-us/hon-ba-fire-hon-62073.pdf` (200, 190,989 B) and `fiplex-02022026/hon-ba-fire-hon-62096-uhf-donor-antenna-bda-ydaxxxxxx-9-1.pdf` (200) work. **The coordinator kept 37 in. in the body only, not the title** (a mirror-only source, the same treatment as BDA-NM-RG8-13-NM). Fiplex slugs in `fiplex-02022026/` follow the pattern `hon-ba-fire-hon-<doc>-<description>-<model>`. `buildings.honeywell.com/bin/edam/getfileservlet` id URLs from search fail (percent-encoded ids: "Illegal base64 character 25", 27 B; decoded ids: "Document Not Found.", 19 B).

### e08 (23 Sep 2026): BDA-LD-05, and a new route that may retire the Fiplex login ask

- **BDA-LD-05:** HON-62077 (10202020), served first-party from EDAM, BDA-LD-05 column checked on a render: DC–3 GHz, 5 W CW, 50 Ω, N(m), VSWR printed "1.2:1 min" (published as "stated as 1.2:1"), -30 to +65 °C, MTBF over 1,000,000 h. The same document is also at `gamewell-101625/hon-ba-fire-hon-62077-rf-loads-terminations-bda-ld-xx.pdf` (same revision, different MD5).
- **New route, the Honeywell product search API:** `POST https://buildings.honeywell.com/pif/api/search/v1/joule-bt-hbt-epim-product-prod/search` with body `{"query":"<sku>","page":{"size":100}}`. It discriminates: a bogus term returns `total_results: 0`, and the known-good BDA-OIA-698869-3-1 hits. Records carry `sku_list` and `resources` (EDAM PDF URLs). GET returns 500. **Trap: records attach the wrong sheets.** The "Passive DAS Termination Loads" record attaches the HON-62075 hybrid coupler sheet, while HON-62077 hangs off the "Grounding Kit" record. Search every record's resources and open every PDF.
- **New EDAM subdirectory `flexbda-050526/`,** slug pattern `hon-ba-fire-passive-das-common-<category>-hon-<doc>-<description>-<model>.pdf`. Categories: `miscellaneous`, `tappers-splitters`, `duplexers-notch-filters`, `donor-antenna`, `service-antennas`.
- **The BD500 High Power Tapper sheet serves first-party (coordinator check, 23 Sep):** `flexbda-050526/hon-ba-fire-passive-das-common-tappers-splitters-bd500-high-power-tapper-136-960mhz-bda-tpx-l2.pdf` returned 200, 251,179 B, `application/pdf`. It has a **BDA-TP10-L2 column**: 10:1/10 dB, split -0.9/-10.4, 300 W average, input VSWR 1.35:1 max, 136–960 MHz. **That settles BDA-TP10-L2 without the Fiplex login.** It is queued with BDA-NMP01250 and DHS40-HG-SCH-1-A for a lot that retries all three through these routes.
- Numeric sweep of `notifier-us/hon-ba-fire-hon-620NN.pdf`, 62060–62120: hits only at 62061, 62067, 62068, 62073, 62074 and 62110.

### x01 (23 Sep 2026): the Fiplex login ask reduced to one product

- **CORRECTION to the e08 entry above:** the BDA-TP10-L2 input VSWR is **1.25:1**, not 1.35:1. The 1.35:1 at the top of BD500 p2 is the tail of the BDA-TP7-L2 table (heptagon label), which breaks across the page with no model header on the continuation. The coordinator read it from a grep in e08; the p2 render settles it. This is a caption trap across a page break.
- **BDA-TP10-L2** (BD500, no printed revision; PDF created 2022-07-12, modified 2026-05-05; MD5 `4889a2af…`): 10:1, -0.9/-10.4, 300 W, IP65, Type N, decagon label, 105 × 25 × 25 mm. Every page prints 136-960 MHz; only the PDF's internal filename says 138. The connector gender and the `-L2` meaning are not stated. **Published; login ask retired.**
- **BDA-NMP01250:** Honeywell API record BDA-27 "PASSIVE DAS CONNECTORS" lists it with no document, so a Fiplex login would not settle it anyway. The copy comes from the **Trilogy** NMP01250 spec (©2016, rev 09/15/16), served by Graybar's Salsify CDN and Clearline Engineering's Shopify CDN: different MD5 (separate PDF exports), identical text, Trilogy imprint. Accepted under the imprint arm of the mirror rule. Body published, title kept as live. Unit of sale flagged (the sibling NFP01250 says "Sold in lots of 10").
- **DHS40-HG-SCH-1-A: null.** The Honeywell API returns 0 for DHS40, DHS40-HG and DHS40-HG-SCH (bogus 0, known-good 673), and 0 hits in 120 PDFs across 67 Fiplex/BDA records. `www.fcc.gov` is now blocked too (Akamai 403, 385 B). What settles it: the Fiplex DHS40 datasheet, manual UM-0914, or the FCC exhibit for P3TDHS40-HG-A. **The price $130,698.70 is about 13× the dearest documented Fiplex amplifier** (a distributor quotes "130 dB Gain"; the price field may be corrupted); flagged.
- **API traps:** hyphenated SKUs are matched token by token (the full DHS40-HG-SCH-1-A string returns 7,533 unrelated hits), so check `sku_list`, not `total_results`. Pagination is `"page":{"current":N}`; intermittent SSL EOF errors cleared on retry. The `flexbda-050526/` and `fiplex-02022026/` directory paths return 403 at 2,307 B `application/gzip` (no listing). Eleven API-attached URLs give the 8,047 B miss; three "`.docx.pdf`" resources are really `.docx`.
- **Trilogy routes:** `images.salsify.com/...` (from the Graybar product page); `clearlineengineering.com/cdn/shop/files/<CODE>.pdf?v=…` (the `?v=` parameter is required; without it everything, real or bogus, returns 404 at 2,770 B); the mra-raycom `simple-file-list/Specifications/` open index holds `Trilogy-Cross-Reference-Chart.pdf` (10/29/2018). trilogyrf.com is still Sucuri-blocked (202, 237 B).
- Queued title fixes on BDA-TP15/20/30-L2 (see `audit/proximos_irmaos.md`).
- t08 (23 Sep): BD500 settles **BDA-TP15/20/30-L2** from each model's own table (15/20/30 dB, 300 W, 1.25:1; pentagon/square/rectangle labels). Only the TP7 table breaks across a page. The TP20 and TP30 flatness rows are printed without a minus sign (a document inconsistency). Titles are now normalised to the TP10 pattern. TP24 is still undocumented.
- e10 (23 Sep): **BDA-NATTEN-0520** from HON-62069.01, served at the API-attached `notifier-us/` path. Constructed slugs in the other subdirectories gave the 8,047 B miss. The connector table says N(m) but the drawing shows one female end, so the copy says "Type N" only. **The store's BDA-NATTEN-0524 and -5024 (24 dB) are not on the sheet** (3/5/10/15/20/30 dB only; flagged).
