<!-- Registro de casos do projeto TFAS. Movido VERBATIM de CLAUDE.md em 23 Sep 2026; nada foi reescrito. Nao e carregado automaticamente: leia sob demanda. E cronologico: entradas posteriores corrigem anteriores; em caso de conflito vale a mais recente e o nucleo em CLAUDE.md. -->

# outros-fabricantes

- **Protectowire blocks `curl` too, but differently from Eaton.** Most
  `protectowire.com/wp-content/...` paths return HTTP 202 with an `sgcaptcha`
  meta-refresh (Sucuri), and the Eaton `urllib`-plus-Safari-UA workaround does **not**
  defeat it; some paths pass intermittently. What works reliably is
  `prod-edam.honeywell.com`, which mirrors Protectowire PDFs verbatim. Given the
  Anixter lesson, cross-check the mirrored revision against any Protectowire-hosted
  document that does come through &mdash; a 2012 mirror and a 2022 original agreed
  exactly on the PHSC temperatures, so there was no generation gap there.
- **Functional Devices publishes first-party PDFs through Salesforce CMS, and the path
  is derivable.** Their site is a JS shell and every guessed `/pdf/`, `/downloads/` and
  `/documents/` path 404s, but `robots.txt` discloses `/document/`, and
  `https://www.functionaldevices.com/sitemap-managedcontent-sfdc_cms__document-1.xml`
  lists every document as `.../document/<slug>-<MC-key>`. Swapping the prefix to
  `https://www.functionaldevices.com/sfsites/c/cms/delivery/media/<MC-key>` serves the
  PDF. Two fetches turned a mirror-only brand into a first-party one. **When a brand's
  site is a JS shell, read `robots.txt` and the sitemap before giving up on it.**
- **Titles must be plain ASCII, and 80 were not.** A catalogue-wide scan on
  21 Sep 2026 found **136 of 16,031 active titles carrying non-ASCII characters**,
  carrying 52,451 impressions. 80 were normalised (curly quotes and primes to
  `&quot;`-equivalent plain quotes, `&times;` to `x`, en dash to hyphen, vulgar
  fractions to `3/4` and `1/2`, bullets to hyphens); `&deg;`, `&reg;` and `&trade;`
  were deliberately left alone as harmless and widely accepted. Five were **not
  styling but corruption**:
  - `Edwards 868STRC-AQ` carried **double-encoded UTF-8 of a zero-width space**
    (`U+00E2 U+20AC U+2039`) immediately after the part number, so the part number
    did not match itself. **The corruption had already leaked into the handle**
    (`edwards-868strc-aqa`), which was left alone to avoid breaking the URL.
  - Two titles contained a literal **`&nbsp;`** &mdash; titles are plain text, not
    HTML, so it displayed as those six characters.
  - `Aiphone IXGW&#8209;LC` used a **non-breaking hyphen** inside the part number,
    so a search for `IXGW-LC` could not match it.
  - A Napco title used `&#9679;` as a sentence separator.
  **The corruption clusters: 33 of the 80 are Aiphone and 34 sit in the newest
  product-id block**, which points at a specific import rather than gradual drift.
  Check titles for non-ASCII after any bulk import, and remember titles are Merchant
  Center feed attributes &mdash; a mangled part number costs money in both channels.
- [CORRIGIDO — na revisão 2022 (`DS6592AA-0622`) os modelos 220 °F têm UL 50 ft; ver neste arquivo &quot;decayed in the document itself&quot;] **A generalisation that survives one test still needs its boundary found.** The
  Protectowire rule "listed spacing is a function of temperature, not jacket" was
  derived on the XLT jacket, tested again on EPC, and **breaks at 220 &deg;F** &mdash;
  PHSC-220-EPC and -220-XCR have **no UL spacing at all** and FM 25 ft. Max ambient is
  likewise temperature-driven at 190 &deg;F but jacket-driven at 356 &deg;F (EPC 221,
  XCR 250). Confirming a pattern twice is not the same as knowing where it stops.
- **DITEK reissued its whole `SPS-` datasheet series in 04/26, so any DITEK figure
  quoted from an earlier revision needs rechecking.** `DTK-MRJPOEX` is the worked
  example: every reseller and all older literature say 802.3af/at and &quot;PoE Plus,
  HiPoE ready&quot;, while `SPS-100042-010` **Rev 11** carries a four-row IEEE table
  adding **802.3bt Type 3 (60 W) and Type 4 (100 W)**. Also corrected: **DITEK's site
  is `diteksurgeprotection.com`**, not `ditekcorp.com`, which only survives inside
  older install sheets. And the ordering syntax is settled from the manufacturer's own
  tables: **`B` = fails short to ground and 5 A max continuous, `F` = fails open
  circuit and 1 A, `WB` = includes the single-position mounting base.** Two agents
  reached that independently from opposite ends of the pair and every shared figure
  agreed &mdash; 20,000 A, UL 497B, 30&ndash;12 AWG, &minus;40 to 158 &deg;F,
  3.25 &times; 1.5 &times; 2.65 in. **Pair-splitting paid again.**
- **The conditional-headline rule paid on its first reuse, one batch after it was
  written.** It was recorded from `D1xB2XH1…`, where the datasheet headlines
  &quot;86.37cd&quot; flat and only the instruction sheet reveals that is the 1 Hz
  value. The next E2S part, `D1XS2FDC024CS1A1R`, was briefed with it and **the same
  shape fired**: the datasheet's headline **123 dB(A)** turns out, in instruction
  manual `D190-00-101-IS Issue 6`, to be the **maximum at high power on tone 4**, with
  **118 dB(A) nominal on tone 44** and 120/115 at default power. The copy quotes the
  figures with their conditions. **A written-down trap that catches its next instance
  is the whole return on writing traps down**; this one now has two independent
  confirmations on one brand, so treat any single headline acoustic, candela or current
  figure on a configurable device as conditional until the instruction sheet's table
  says otherwise.
- **A headline spec can be conditional on a setting the datasheet does not mention.**
  E2S datasheet `1-21-200` headlines *&quot;86.37cd &ndash; UL1971 Public mode
  fire&quot;* with no qualifier. Instruction sheet `D191-00-261-IS Issue 3` Tables
  3A/4A/5A show that 86.37 cd is the on-axis value **at the 1 Hz / 60 fpm flash setting
  only**; the same unit is **58.57 cd at 1.33 Hz and 51.65 cd at 1.5 Hz**. A designer
  who sets 90 fpm on a layout drawn for 86 cd is about 40% short. The same sheet is the
  only place the **UL 1638** listing appears &mdash; the datasheet names UL 1971 alone.
  **Generalises: when a datasheet states a single value for something the device can be
  set to vary, find the instruction sheet's table before quoting it.** This is the
  prose-versus-table rule pointing across documents rather than within one.
- **Distributor consensus fails in a correlated way, which is why it is not evidence.**
  Third instance in four batches. `ELSPKBB-R` is a **wall** box (Eaton's backbox table,
  confirmed on one y-line by coordinates: the `C` in `LSPKBB-CR` is the ceiling marker)
  and ADI and Telcom-Data both call it ceiling. `BDA-NM-RG8-13-NM` is 51 in. and every
  reseller says 48. And **every reseller copy of the DITEK `120S` sheet is stale on four
  figures at once** &mdash; UL 1449 4th against the current **5th** Edition,
  &minus;40 to 185 &deg;F against **&minus;31 to 104 &deg;F**, the wrong depth, and
  40&ndash;400 Hz against **50/60 Hz**. They copy each other, not the datasheet, so
  agreement among them carries no independent weight at all.
- **Bosch is a blocked brand with a 128-byte fingerprint, and the sitemap route does not
  reach it.** `resources.boschsecurity.com` and the Azure CDN are **refused at the proxy
  gateway with 502 to CONNECT**; `resource.boschsecurity.com` (singular) 301s every
  `/documents/` path to the site root; and `cdn.commerce.boschsecurity.com`,
  `cdn2.commerce...`, `commerce...` and `catalog.boschbuildingtechnologies.com` all answer
  **HTTP 200 with a 128-byte `text/html` body** for every path, including URLs taken
  straight from search results. **128 bytes joins EDAM's 8,047, steelfire's 48,687,
  autocall's 103 and lenel's 371 on the fingerprint list.** The robots/sitemap route this
  file recommends *does* resolve (`catalog.boschbuildingtechnologies.com/sitemap-products.xml`,
  10.7 MB) but carries only the &quot;lifesafetysystems&quot; storefront with **no US fire
  products at all** &mdash; so that route has a boundary, and this brand is outside it.
  `D296` was written from two Bosch-authored documents reached through mirrors three
  years apart, agreeing exactly on every figure quoted.
- **A carton-contents change between revisions is a real product change, and the older
  document is the trap.** Bosch's 2014 `D296` manual says a **D306** remote indicator
  plate ships with each detector and that the **D308 test kit is not supplied**; the 2017
  data sheet's Parts Included list gives a **D344-RL** plate **and** the D308 kit, and
  never mentions the D306. Anyone reading only the manual would tell a buyer to order a
  test kit they already have. **Prefer the newer revision for carton contents
  specifically** &mdash; it is the field most likely to change without any spec changing.
- **A summarising fetch can shift a table by one row, and the shift is invisible because
  the output looks tidy.** WebFetch on the Space Age category page returned a clean model
  table giving `SSU00651` **32** termination points. The manufacturer's own `LT10221
  Rev. J` says **64**, as does the product URL slug. The summary had not hallucinated a
  number &mdash; it had **misaligned the rows**, so every value was some other model's.
  This is the SWIFT lifecycle-label lesson one layer over: that one warned against taking
  a *lifecycle claim* from a summarising fetch, and this shows the same tool failing on
  *numeric table data*, where the result reads as authoritative because it is
  well-formatted. **A summarising fetch is not evidence about a table. Download the
  document.**
- **A new extraction shape: a genuine PDF whose text layer is unusable.** Space Age
  install sheet `LT10322` downloads as real `application/pdf`, opens in pymupdf, and
  `get_text()` returns **custom-encoded punctuation soup** &mdash; not navigation chrome,
  just garbage. **This is distinct from the EDAM and systemsensor.com traps, where
  `file -b --mime-type` is the tell.** Here the mime check *passes* and the document is
  still unreadable without a render. So the check separates a fake PDF from a real one and
  says nothing about whether the real one can be read; **if extracted text looks like
  noise rather than prose, render, do not conclude the document is wrong.**
- **The robots-and-sitemap route has now paid on a third brand, and the host was wrong in
  the catalogue.** `www.spaceagelectronics.com` fails at the proxy with
  **`CONNECT tunnel failed, response 502`, zero bytes**, on `/robots.txt` and
  `/sitemap.xml` alike &mdash; a new fingerprint. The real host is **`www.1sae.com`**,
  whose product pages are a Magento JS shell with **zero PDF links in the HTML** and whose
  `robots.txt` is a **1-byte file** &mdash; but `/sitemap.xml` is a live 260 KB index that
  led to the category page and three documents under `/media/assets/product/documents/`.
  After Functional Devices and HyperSpike that is three brands recovered this way.
- **Identical third-party listing files prove a single manufacturer.** The MR-relay
  brand tangle &mdash; one family under four store vendors &mdash; was settled not by
  any website's claim but by APC's and Space Age's documents citing the **same** UL
  `S3403`, MEA `73-92-E` and CSFM `7300-1004` files. One listee, one manufacturer,
  two catalogue numbers. Use this whenever a brand question looks unanswerable.
- **THE MIME CHECK IS NOT SUFFICIENT FOR IMAGES, and this is the first host that proves
  it.** `1sae.com` (Space Age) answers a miss with **HTTP 200, `image/png`, 3,264 bytes,
  md5 `74471fe1e675f0eef008b3980535c469`** &mdash; **byte-identical for every bogus path**,
  verified by the coordinator against two invented part numbers. It is a *real PNG*. Status
  passes, `file -b --mime-type` passes, PIL opens it and reports dimensions. **Only an
  MD5 or byte-length comparison discriminates.**
  This file has treated `file -b --mime-type` as the non-optional gate since the
  `systemsensor.com` trap, and for documents it still is. For images it is not: **a host can
  serve a genuine image as its 404.** That is the image-side twin of the genuine-PDF-with-
  unusable-text-layer finding &mdash; in both cases the check that separates fake from real
  says nothing about whether the real thing is the thing you asked for. **So every photo
  route needs a bogus-SKU control measured by MD5, not by mime**, and the control must run
  at download time rather than on a HEAD. Checked on the 80 Space Age rows: **zero are the
  placeholder.**
- **Three coverage estimates corrected, each for a different reason, which is why the
  denominator has to travel with the number.** Space Age 32% &rarr; **16.7%**, and the
  binding constraint is not matching but **image size**: 107 of 190 candidates die on the
  300 px floor because 1sae originals are routinely 200 &times; 200. Westell 29% &rarr;
  **19.9%**, because **216 of our 371 SKUs have no page on westell.com at all** &mdash; the
  site carries 420 products total. Mircom 16% &rarr; **7.3%**, and that gap is *rule
  strictness*: **26 of the 49 earlier hits fail the full boundary rule**, being group shots
  (`MIX-4001-4002-group_sm.jpg`) or longer-SKU-owns-file (`MIX-4040-M` owning `MIX-4040`).
  **Matching, sizing and catalogue coverage are three different ceilings and they do not
  substitute for one another.**
- **And the &quot;196 of 710 behind WordPress&quot; figure does not survive a change of
  definition &mdash; only 113 of 502 do.** The two agents used different tail boundaries
  (one took vendors with 60 products or fewer, the other excluded every brand being worked
  elsewhere), and the headline number moved by 40% without either being wrong. **A tail
  statistic is a statement about a cut, not about the catalogue**, and this file should
  carry the cut with the number every time.
  Three corrections worth keeping from the same work: **&quot;probe at `per_page=100`&quot;
  is necessary but not sufficient** &mdash; Apollo returns `[]` on an unfiltered page 1 and
  real rows on page 2, so **probe with `search=<term>`**; **title token 2 is wrong on 22.7%
  of tail rows**, not the ~4% measured on the big brands, because the tail is full of
  multi-word vendors (`E2S by The Signal Source`); and **three hosts return HTTP 200 for a
  file that does not exist** (`diteksurgeprotection.com` 151,291 B `text/html`,
  `honeywell.scene7.com` 20 B `text/plain`, `sdifire.com` 146 B `text/html`), so the mime
  check is what separates them &mdash; and DITEK's 404 measured **151,291 bytes here
  against the 152,678 this file has on record**, which is the host-fingerprint decay rule
  firing again.
- **A brand field so wrong it looked like a missing route.** 31 of the 44 products under
  vendor **`Fireray`** are **Edwards/EST** &mdash; EST4 cabinets and annunciators (`4-*-E`),
  Signature closets (`3-RCC*`) and FireWorks licences; only about 13 are genuine FFE beam
  detectors. The agent could not find photographs for them **because the brand is wrong,
  not because the photographs are missing.** Flagged to the owner. Related and useful:
  `sdifire.com` now serves Detectortesters/XTR2 content, because **SDi and No Climb are
  both Halma**, so one host covers SDI, TruTest, SCORPION, Detector Testers and Urban.
- **The identical-listing-files rule run IN REVERSE, and it reassigns a manufacturer.**
  This file records that *identical* third-party listing files prove a single
  manufacturer, which is how the MR-relay brand tangle was settled. `SSU-PAM-1` is the
  same argument backwards: **different listing files prove different manufacturers.**
  CSFM listing **`7300-1555:0101`** (07/12/2024), covering SSU-PAM-1/-2/-4/-EOLR/-SD,
  names the listee as **FUNCTIONAL DEVICES, INC., Sharpsville IN**, and the UL letter
  gives Functional Devices **file S7312** (UUKL). Air Products and Controls' PAM-1 sits
  under **file S3403**, MEA 73-92-E, CSFM 7300-1004. **Both documents were fetched and
  read by the coordinator directly**, because this overturns a recorded route note.
  The specs differ in three measured ways &mdash; **depth 1.2 in. against 0.77**,
  **&minus;30 to 104 &deg;F against 32 to 120**, **30 mA against 50 mA at 120 Vac** &mdash;
  so it is not a relabel either.
  **Fourteenth coordinator premise wrong, and wrong twice over in one sentence:** the
  briefing said *&quot;the `PAM-1` is an Air Products and Controls part, and Space Age
  sells it under an `SSU-` prefix inside their own enclosure&quot;*. There **is** no
  enclosure &mdash; Space Age's own table gives Enclosure type as **Encapsulated**, a
  potted 1.5 &times; 1.2 &times; 1.2 in. body with six flying leads &mdash; and it is not
  an APC part.
  **The new trap shape is the sharpest thing here: a first-party host serving somebody
  else's listing document.** `1sae.com` itself serves `/pam-ul.pdf`, which is a **2005 UL
  directory page for Air Products and Controls file S3403**, listing PAM-1/-2/-4/-SD and
  containing **no `SSU-` model at all**. A reader taking &quot;the manufacturer's own site
  serves this UL document&quot; as evidence reaches exactly the wrong conclusion. **Check
  whose name is on a listing document, not whose site served it.** The copy states only
  that the APC PAM-1 is a different part under a different listing file; the vendor field
  went to the owner.
- **Host-fingerprint decay, third instance, on a path this file recommends by name.**
  `apcfire.com/wp-content/uploads/DS-RL-1-G25-PAM-Series.pdf` **now 404s at 146 bytes
  `text/html`**; the live path carries the dated subdirectory,
  `/wp-content/uploads/**2026/01/**`. After the `myeddie /Media/` redirect and DITEK's
  151,291-against-152,678 bytes, this is the rule firing a third time in two days:
  **re-measure a recorded path or fingerprint before building a batch on it.**

- **An entire BRAND is mis-filed, 161 SKUs of it, and the agent's own estimate of the
  scope was four times too small.** `SF-RP5204X` and `SF-RP5206X` carried raw ERP
  descriptions (*&quot;3/4 TEE 10/PK&quot;*) under vendor **Space Age**. They are
  **SAFE Fire Detection, Inc.** parts &mdash; that company's own RedPipe data sheet
  states `RP5204 = 3/4&quot; TEE` and `RP5204X = 10 pack`.
  **The negative was validated before it was trusted**, which is what makes it evidence:
  1sae.com's catalogue search returns a real result page for `MR-101` and its no-results
  page for `SF-RP5204X`, `SF-RP5209` **and** `redpipe`, so the query is honoured and the
  miss is real.
  **The agent sized it at ~39 SKUs from the `SF-RP*` family. The live catalogue holds 161
  SKUs with an `SF-` prefix and every single one is under vendor Space Age** &mdash; 146
  six-month impressions and $16,932 of ERP revenue, spanning RedPipe, RedGear, Safecable,
  Cirrus, ProPoint, ProLocator and the Hybrid/PPP aspirating line. Confirmed directly on
  `safefiredetection.com`'s WordPress search (bogus control `ZZQQXX999` &rarr; **0 rows**,
  so the endpoint is honest): **RedPipe and RedGear return their own product pages**, and
  ProPoint Plus and Hybrid return **SAFE's own training exams** &mdash; supporting rather
  than conclusive for those two, and the remaining families were not checked.
  **So `SF-` looks like a whole manufacturer's namespace filed under the wrong brand.**
  Nothing was changed: vendor is a Merchant Center attribute. **And the method lesson is
  to check the scope of a brand finding against the live catalogue rather than against
  the family that surfaced it** &mdash; a prefix is a census question, and the agent could
  only see its own six.
- **A pack count the manufacturer DOES state, and the store contradicting itself about
  it.** `RP5204X`/`RP5206X` are stated as 10-packs by SAFE Fire Detection &mdash; and
  **six siblings in this catalogue already carry &quot;10/PK&quot; in their titles while
  these two carry nothing.** That is the inverse of the usual pack-count problem: not an
  unsourced claim to remove, but a sourced fact the store states inconsistently. Still
  not applied, because adding one is a new feed claim and the decision is the owner's.
- **A usable new Honeywell fingerprint, where the recorded one is useless.**
  `buildings.honeywell.com/us/en/products/.../<slug>` returns **`text/html` for a real
  slug and `application/javascript` (~225 KB) for a bogus one**, so **the mime check
  discriminates there** &mdash; unlike `/search?q=`, which this file records as returning
  byte-identical 219,852-byte 404s for every term, now confirmed a second time on two
  different queries. **The same host can be honest on one route and useless on another.**
  Also: **a new DITEK failure shape &mdash; HTTP 200 with a ZERO-byte body** on
  `/products/<sku>/`, distinct from the ~151&ndash;152 KB shell on record; the **series
  page** works and carries the model descriptions and PDF links, which is this file's
  &quot;filenames are linked from the series page&quot; rule paying again. And **the bare
  host `diteksurgeprotection.com` fails at the proxy where `www.` works.**
- **Two long-range prism kits, one part number in every reseller's copy.** `1010-000`
  serves the **Fireray One and Hub Reflective** at 50&rarr;120 m; **`5000-004`** is a
  different part number for the **Fireray 5000** at 50&rarr;100 m (FFE assembly sheet
  `24-0090-03`). Every distributor merges them and quotes both ranges under `1010-000`.
  **And the trap was structural, not just textual: FFE files `24-0090 Fireray Long Range
  Prism Kit Installation Guide` under `Fireray_Accessories/Fireray_5000/`** &mdash; so
  reading the folder name as the product would have crossed the two kits. **A directory
  path is not an attribution**, which is the URL-contains-a-part-number lesson one level
  over.
  Route: **`ffeuk.com` is first-party, unprotected and mime-clean, and is HubSpot CMS,
  not WordPress** &mdash; `/wp-json/` returns a **122,693-byte `text/html` 404**, a new
  fingerprint &mdash; while **`ffeuk.com/resources` is a single page carrying 358 PDF
  links**, so one fetch enumerates the whole library. `ffeus.com/sitemap.xml` returns
  **zero bytes**. FFE is a Halma company, like Avire/RATH and SDi.
- **A host that returns HTTP 200 with a ZERO-BYTE body, second instance.**
  `cdn.power-sonic.com/documents/` does it for any nonexistent file, and
  `curl -o /dev/null -w %{http_code}` reads that as success &mdash; an agent &quot;found&quot;
  three catalogue PDFs that way and all three were empty. Same shape as the DITEK
  `/products/` case. **Only a byte count or MD5 catches it**, which is the image-side
  lesson (`1sae.com`'s 3,264-byte real PNG 404) reappearing on documents.
  Related and sharper: **`interstatebatteries.com/products/<anything>` is a generic JS
  shell at 233,695 bytes for both a real and an invented SKU, containing zero occurrences
  of the requested SKU and differing only in a nonce meta tag** &mdash; so **the MD5
  differs and an MD5-only control wrongly passes it.** Pair it with the Hochiki
  `productsearch` case: in both, the bytes differ and the content is the same. **The
  reliable test is not whether the response differs, it is whether it contains what you
  asked for.**
- **A distributor supersession killed by a MECHANISM rather than by an absence, on Apollo.**
  ADI lists `SA4700-102APO` as *&quot;(Replaces 55000-847SIL, 55000-847APO)&quot;*. `replac` and
  `supersed` appear **zero times across five Apollo documents**, and both legacy numbers are still
  **current rows** in PP2090 Issue 29 and on the live BRE/LPCB certificate &mdash; which alone is
  only the `4099-9005` shape, proving nothing either way. What settles it is that
  **`SA4700-102APO` carries the 20C isolator at Equivalent Detector Load 1 and `55000-847APO` the
  older 20D at EDL 4**, so they are not interchangeable for loop-isolator design regardless of
  intent. Not in the live title, so nothing was removed; recorded so nobody adds it.
- **Eleven shared image URLs across the 1,506-row delivery, and ALL ELEVEN are correct
  &mdash; which is why this check can never be a filter.** Counted at the only scope that
  works, the whole delivery rather than per lot. Four Secutron `-PK10` pairs and one `-PK15`
  are **the same part in a different carton**; two Fireray pairs are **one product with two
  approvals** (EN against UL/FM, stated in FFE `24-0461`, and FFE publishes one render per
  product type); two Macurco pairs share a photograph because **LADBS is an approval
  designation, not a variant**; and the two Power-Sonic `- ECOM` pairs are settled by the
  store's own ERP string, which spells it out: **`Battery+ind.box`, an individual retail
  carton of the identical battery.** A blanket drop-every-shared-URL rule would have thrown
  away eleven correct rows. **The duplicate check tells you two products share one
  photograph; whether that is a defect is a question about the two products.**
- **A failed disproof, reported as such, and it sharpens the recorded 1sae finding rather
  than overturning it.** This file records *&quot;1sae originals are routinely 200&times;200,
  and 107 of 190 candidates died on the pixel floor&quot;*. An agent tried to overturn it:
  the bare path serves 200&times;200 while a Magento cache rendition serves **700&times;875**,
  which looks exactly like the recorded note measuring the wrong artefact. **It is not.
  The 700&times;875 frame is padding and adds zero product pixels** &mdash; measured on one
  asset, the subject is 104&times;160 at 200&times;200 and 103&times;159 at 700&times;875, and
  on three delivered rows the rendition actually *loses* subject pixels.
  **So the mechanism is sharper than the recorded number: the binding constraint is the
  PRODUCT'S OWN PIXELS INSIDE THE CANVAS, which no rendition improves.** Across 103
  candidates the best subject long edge available at any of seven cache hashes was
  **100&ndash;199 px on 92 of them**. A harvest measuring the *file* would have shipped all
  92 as 700 px hits carrying 150 px of product &mdash; a new shape of &quot;passes every
  mechanical check&quot;, and the reason the delivered rows now carry `subject_w`/`subject_h`.
  **An agent reporting that its own correction failed is worth more than one that quietly
  drops it.**
- **A vendor mis-filing corroborated from the opposite direction, which is the best
  validation a census gets.** The live-catalogue scan found **161 `SF-` SKUs filed under
  vendor Space Age** and all of them SAFE Fire Detection parts. A photo agent working a
  400-product slice of that same vendor, with no access to that census, independently
  counted **157 of its 400 (39%)** and mapped the families &mdash; SafeCable 39, RedPipe 39,
  numeric Hybrid/PPP/Cirrus spares 37, RedGear 31. Two routes, two populations, one answer.
  **And it found the useful corollary: SAFE publishes per-part photography for ten RedPipe
  fittings and nothing else**, so that brand's 1.3% is a documented near-zero rather than a
  routing failure.
- **&quot;A null may well be the right answer&quot; was wrong, and the honest search endpoint
  is what disproved it.** The briefing predicted `COP-IXDVF-NR1G` would be unfindable, since
  **zero Aiphone product slugs and zero media filenames begin with `cop-`**. Aiphone publishes
  a first-party spec sheet for it (11/24) plus a price-list row, and
  **`know.aiphone.com/search?query=` discriminates** (bogus &rarr; `[]`, 2 bytes) where
  `aiphone.com/?s=` does not. Note Aiphone spells it **two ways in its own literature** &mdash;
  `COP-IXDVF-NR1G` in the price list, matching the store SKU, and `COP-IX-DVF-NR1G` in the
  knowledge base. Neither is a defect. **`COP` = Custom Order Product.**
- **A genuine PDF with an ASCII-shifted text layer, which is a new shape of the unusable-text
  trap.** `LT-931` page 2 extracts as `4%,%0(/.% #)2#5)4` and `1!-4` &mdash; a font encoding
  offset by 0x20, so &quot;TELEPHONE CIRCUIT&quot; and &quot;QAMT&quot; come back as
  punctuation soup. Mime passes, the document is real, and **page 1 extracted cleanly**, so a
  reader checking only the first page would never see it. Separately `LT-872`'s **entire text
  layer is 107 characters**, the title line alone: its 16-terminal block, four circuit groups
  and the 5 W per zone note are all vector, and **nothing signals the data is missing.**
  Add both to the ladder beside Space Age's `LT10322`.
- **A RECORDED RULE DECAYED IN THE DOCUMENT ITSELF, NOT ON A HOST &mdash; the Protectowire
  &quot;breaks at 220 &deg;F&quot; finding is a fact about the 2012 revision.** This file
  records, as a worked example of *a generalisation that survives one test still needs its
  boundary found*, that PHSC-220-EPC and -220-XCR **have no UL spacing at all**. That is true
  of the sheet it was measured on and **not of `DS6592AA-0622`, June 2022**, where both rows
  carry **UL 50 ft / 15.2 m** and the string `N/A` appears **zero times**.
  Every previous decay recorded here is a *route* going stale &mdash; a path moved, a
  fingerprint drifted, a host changed. **This is the first where the manufacturer changed the
  answer**, and the note that decayed was not a route note but one of this file's better
  method lessons. So the rule needs restating: **a recorded spec finding carries the revision
  it was measured on, or it is not a finding.** The boundary the original note found was real;
  it has simply moved.
  **And the same pair of revisions turned a bounded negative into a positive.** This file
  records `2W` as *&quot;two-wire, read the surrounding rows&quot;* &mdash; an inference from
  the TRI-Wire row below it. The 2022 sheet **renames that same row `PHSC` with the identical
  value**, 0.185 ohms/ft. The manufacturer renamed the label to the product line, which
  settles it outright. **When a reading rests on an inference, check whether a later revision
  states it.**
  A load-bearing footnote came with it, absent from the 2012 sheet: **the recommended UL 521
  maximum ambient for open-area layouts is 100 &deg;F for all 155 models**, while the table's
  115 &deg;F is the **Special Application** figure. A designer reading only the table works to
  the wrong limit.
- **Two Altronix product families conflated in one briefing, and the listings do not
  transfer.** I told an agent that a fire-signalling power supply is UL 1481 rather than
  UL 864, citing `AL600ULXB`'s UL 294 + 603 + 1481. In `DS_AL602ULADA.pdf` the strings `1481`,
  `294` and `603` appear **zero times each**; its only listing is **UL 864, &quot;Control Units
  and Accessories for Fire Systems&quot;**, plus FM, CSFM and NYC DOB. `AL600ULXB` is an
  access-control/burglary/fire **board** at 7.1 &times; 4.5 in. and 0.8 lb; this is a 9.6 lb
  unit in a **red BC400 enclosure**, manufacturer-stated. **A listings set belongs to a product
  family, and two Altronix numbers three characters apart are not one family.**
  Also: **the live title understates the rating** &mdash; 6 A against the datasheet's and
  Altronix's own headline **6.5 A**, render-confirmed &mdash; and the siblings match their
  numerals exactly (AL802ULADA 8 A, AL1002ULADA 10 A), so **only the 602 runs above its own
  number**. `ADA` is defined in no Altronix document read; recorded as a bounded negative.
- **A NEW IMAGE-SIDE 404 FINGERPRINT, WORSE THAN THE RECORDED `1sae.com` ONE.**
  `detectortesters.com/media/catalog/product/…` returns **HTTP 200, `image/jpeg`, 1,692 bytes,
  md5 `c0459a796c5b8ee74254472c235a7460`** for any nonexistent path &mdash; a real JPEG **on
  the exact Magento path where every genuine product image also lives**. Status passes, mime
  passes, PIL opens it. `1sae.com`'s 3,264-byte PNG at least sits on a host this project
  already distrusted; this one is indistinguishable from a hit without an MD5 or byte
  comparison. **Every photo route needs its bogus-SKU control measured at download time.**
- **And a live TITLE defect found by looking at a correct photograph.** `FPMA-W25`'s title
  says **Black**; Neomounts states **&quot;Color: Silver&quot;** for that article number with
  Black as a separate variant, and the render is silver. **The photograph is right and the
  title is the defect** &mdash; the reverse of every look-pass case on record, where the title
  was the fixed point and the image was judged against it.
- **Four part numbers refused as adjacent-row substitutions, none called invented.**
  `AOR-5-DSL` against Talkaphone's catalogued `AOR-5-DKL` (the bogus path returns the honest
  102-byte 404 while `-DKL` returns a real 3.6 MB image); `MSR-100W/W` against APC's
  `MSR-100R/W`; `STS-1.5`/`STS-2.0` against APC's 2.5/5.0/10.0 range; `SPARE1046` against
  Detector Testers' 1002&ndash;1060 with no 1046. **In all four the near neighbour was
  available and was not taken**, which is the rule working at the point where it costs
  something.

- **The terminal DRAWING gallery is a superset of the ORDERING list, and only one of them is
  authority.** The `PS-6100` sheet draws F1, F2 **and** FP while its Configuration Options block
  lists only `F1 / F1 VDS / F2 / FR F1`. **The Configuration Options block is the ordering
  authority**; the drawing shows what the factory can fit, not what the catalogue sells. Same
  shape as the recorded Altronix case where a derivable library path covers the models it covers
  and not the series.
- **A new document defect, and the NEWER revision is the one that does the attribution.** Bosch
  `2700030219` V12 writes the D7050TH thermal element as **&quot;35 &deg;F (57 &deg;C)&quot;**
  where V5 prints 135; only 57 &deg;C, on which all three revisions agree, was published. But
  **V12 also scopes UL 521 / CAN/ULC-S530 to &quot;D7050TH only&quot; where V5 does not** &mdash;
  so the revision carrying the typo is the one that prevents a series-listing error. **Read all
  the revisions rather than picking the newest or the cleanest**; they fail in different places.
  Also: V5's Parts Included table is dropped from V10 and V12, so no carton claim was made.
- **Three incomplete-product cases in one half-batch, and one of them names a gap in the
  STORE.** `SBB-D4` is sheet metal at $430.25 with no door, lock or keys &mdash; and
  `DR-D4`, `DR-D4R`, `DR-D4B` and `BP2-4` are **all live SKUs here**, so the closing paragraph
  points at products TFAS sells. `SS-PHOTO-CO`'s installation step 1 reads *&quot;Wire the
  sensor base (supplied separately)&quot;*. **`D7050` is the one worth the owner's attention:
  Bosch states the `D7050-B6` base is required twice, and that base is NOT a SKU in this
  store**, so a buyer cannot complete the assembly from TFAS at all. **An incomplete-product
  finding is also a merchandising finding** &mdash; check whether the required part is stocked,
  because the answer decides whether the copy can help the buyer or only warn them.

- **An AI summary committed the adjacent-row trap INSIDE ITS OWN SUMMARY, on a part two rows
  down.** A search summary attributed to Viking `904757` the wording *&quot;align a UniVario flame
  detector in the vertical as well as the horizontal axis / 22.5&deg; increments&quot;*. Reading
  the page shows that belongs to **`922485`, the Mounting ANGLE bracket, the next part on the same
  page**. Nothing from it was published. This file records summarising fetches shifting a table by
  one row and manufacturing a lifecycle claim out of page chrome; this is the same failure with no
  table involved at all &mdash; **two adjacent catalogue entries welded into one answer.**
- **&quot;Viking&quot; is TWO UNRELATED MANUFACTURERS under one vendor string, and the negative
  was validated with both controls before it was trusted.** `904757` is **Viking GmbH / UniVario**
  industrial fire detection (Minimax Viking), not Viking Group Inc sprinkler hardware: Product
  Sheet `312-810_005` heads it *&quot;UniVario Detector Accessories &mdash; Mounting Bracket
  MX5000, Part no.: 904757&quot;*, and the store's own ERP body already reads &quot;MX5000
  BRACKET&quot;. Viking Group Inc's product search returns its no-results size for it (158,867 B
  against a bogus control at 158,881 and a known-good `VK502` at 163,822) &mdash; **so the endpoint
  discriminates and the miss is real.** Every other Viking SKU in the store is sprinkler material.
  Fifth umbrella vendor string hiding another manufacturer's namespace, after `SF-`/Space Age,
  `Fireray`/Edwards, `Universal`/Neomounts and `Federal Signal`/E2S. Flagged; vendor is a feed
  attribute.

- **Altronix `AL1002ULADA` matches its own numeral where the 602 did not (v2b51).** `DS_AL1002ULADA` Rev. 06222023: 10 A total, 2.5 A per output, UL 864 only (1481/294/603 zero times, as on the 602). Installation guide Rev. 062320 states the contents: *&quot;power supply, red enclosure, cam lock, and battery leads&quot;* plus an ALEOL2K2 resistor. The datasheet and product page disagree on weight (9.8 against 12 lb), BTU/hr (49 against 31) and humidity, so none was published. **New trap: `altronix.com/products/<bogus>` answers HTTP 200 by serving `/products/index` (870,502 B)** &mdash; a redirect that drops the path; test whether the page contains the SKU. Library 404 still 13,828 B. `ADA` still undecoded.

- **Solo / Detector Testers suffixes are customer-variant codes, manufacturer-stated (audit t01, 23 Sep).** SDS0081CA Rev 2 (15 Dec 2017) &sect;1.1: *&quot;Trade Name SOLO C6-XXX (XXX denotes customer variant)&quot;* (coordinator-verified); SDS0066US Rev 9 says the same for the A4. So `-024` vs `-001` is neither a pack nor a region &mdash; which settles the earlier SOLO610/602 note for the aerosol families; for the 770 baton it is an inference. The store carries **three listings of one C6 aerosol** (SOLOC6, -001, -024; the $321.25 -024 is probably SDi's &quot;cases of 12&quot;) and two of the 770 baton. `sdifire.com/wp-content/uploads/2026/05/2024-SDi-Product-Guide-1.pdf` lists order codes; `detectortesters.com/<slug>` answers a bogus slug with an honest 406/0 B.
- **Rixson `140-90003` is in no manufacturer source** (bounded negative). The 2013 Rixson catalogue (ASSA ABLOY HK asset path) shows 996 and 997 are physically different (1-1/2 in. adapter housing, surface wiring, 4-1/8 in. projection against 2x4 box, concealed, 2-5/8 in.); its text layer interleaves the 994/996 blocks &mdash; render. nortonrixson.com is client-rendered; `/en/search?q=` 404s at 192 KB. Title left untouched; SKU flagged.

- **Protectowire's block is SiteGround `sgcaptcha`, not Sucuri (audit t04):** header `sg-captcha: challenge`, 202 at 216&ndash;229 B, also on the `pwire.net` alias; a bogus filename gets the same 202. **Eight cached &quot;Protectowire PDFs&quot; under /tmp/tfas/enrich/v2b05|v2b08|v2b11|v2b45 are sgcaptcha HTML saved as .pdf.** ELR-HD-1A-QC's sheet is DS-8945B (unreachable); title left as is.

- **E2S configuration codes decoded by E2S's own request builder (enrichment e01):** raw markup of `/product/13317` concatenates base + options into exactly `D1xC1X05RDC024CN1A1R/C` (colour values end in &quot;/&quot;). UL 1638 on-axis rating for D1xC X05 is **12 cd at 1 Hz, 20 VDC, clear lens** (fire appendix `D190-00-301-IS-UL Issue B` p11) against datasheet headlines of 143 cd IES / 250 cd calculated &mdash; third conditional-headline instance on E2S. **HyperSpike:** `hyperspike.com` is now an unrelated IT template; the real host is `ultra-hyperspike.com` (`/media/<id>/` PDFs; WP media API returns `[]` for real and bogus). 72377B-801 is named three ways across three Ultra documents, which disagree on whether pole bands are included.

### e04 (23 Sep 2026): Apollo 55200-940APO (XP95 I.S. manual call point)

- Certification: Baseefa `BAS02ATEX1290X` Issue 13 (8 Feb 2021) and IECEx BAS 12.0091X; Ui 28 V, Ii 93.3 mA, Pi 0.67 W. Apollo PP1095/2024 Issue 6b requires a 28 V shunt-zener barrier or galvanic isolator (29600-098, which is stocked) **and** an XP95 protocol translator, on spurs or radials only. **No UL or FM listing** appears in any Apollo I.S. document, which matters for a US store (flag). PP1095 says devices made after 1 June 2024 fall under PP5138, a generation split. PP5138 was found only on reseller mirrors and was not cited.
- Route: the Apollo 404 is 77,747 B, reproduced with the bogus `F0009999_0001.pdf`. On the product page only `39215-451-Issue-1_XP95-IS-MCP.pdf` is dead. Several certificate PDFs are scans with no text layer (F0000827, F0007055, F0007247, the Lloyd's Register certificate): render them. The product page and the installation guide disagree on quiescent current (300 vs 230 µA) and on dimensions, so both were left out.

### e06 (23 Sep 2026): Thermocable (UK linear heat detection cable)

- Route: `thermocable.com/resources/downloads/<category>` pages list `/downloads/<id>/<exact filename>.pdf`. A wrong filename gives an HTML 404 of ~51,086 B. The 2020 catalogue URL returned by search is now a 404 (51,126 B). The Accessories Guide 2024 Rev 3.1 is served at ids 30/36/47/52/64 with the same MD5. The HTML pages never mention clips, so grep the PDFs.
- **A1541 and A1388 appear in no Thermocable document.** The documented 50 mm stainless clip is A1149-100, the Standard J Clip (50 × 20 mm). "J-lock" appears only in the Cold Storage guide (2026-02-16), which recommends stainless J-lock clips with silicone sleeves and fixings no more than 1 m apart. The live title claims (50 mm, pack of 100) were kept but are unsourced (flag); the body says the A1541 number is not in the 2024 guide.
- e08 (23 Sep):
  - **Apollo 58002-300APO** (PP5143/2024 Issue 1): Discovery/CoreProtocol, loop-powered, 15 tones, 7 volume levels; the isolator works only when the unit is on an XPERT 8 base; **APO is Apollo's own suffix**. Sound is conditional: 95 dB(A) maximum at 1 m on the data sheet, 87 dB(A) typical at volume 7 in installation guide 39215-488. PP5143 and PP2203 Issue 25 disagree on tone frequencies, so none were published. No UL listing (flag, the same as 55200-940APO).
  - **APC 7-CO** is named only in the SL-701 FAQ `20007127_0001` p3 ("The model number for the sensor head is 7-co") and in brochure `20004021_0001`. `apcfire.com/wp-json/wp/v2/product?search=` is honest (bogus → `[]`). A bogus `/wp-content/uploads/2021/07/` file 404s at 146 B and a bogus `/product/` page at 52,349 B. The brochure and the product page disagree on SL-701 ambient temperature (0–70 vs 0–60 °C).
- t07 (23 Sep), **E2S:**
  - The D2x line is Class I Div 2 / Zone 2 aluminium equipment, **not explosion-proof** (Ex ec / Ex tc). Source: datasheet 1-34-020 (footer 8 Jul 2026), Part Codes table.
  - The bare `D2xC1X05` is only the product-type field, so it is a **wildcard SKU**; it was flagged, and the store also sells the configured -DC024CN1A1R/C and /R. Only the D2xC1X05DC024 is UL 464/1638 listed, and in Private Mode only.
  - A file served as `D189-01-501-IS_Issue_3` is really D189-00-501-IS Issue 12: read the header, not the filename.
  - A bogus `/product/99999-zz` returns an honest 404 of 35,499 B.
- e09 (23 Sep), **E2S D1XL1FV725CN1A1R:**
  - The part-code table (datasheet 1-22-160, 8 Jul 2026) decodes V725 / C / N / 1 / A / 1 / R.
  - **The series headline is overridden by the model's own row:** the datasheet p1 says "Class I & II Div 1, T5 to +85 °C", but manual D190-00-201-IS Issue 5, sheet 2, rates D1xL1-V725-A at T4 to 85 °C and T5 to 80 °C. Class II Div 1 belongs to version D only, which excludes the 25/70 V transformer.
  - The PDF also carries UL fire sheet D190-00-201-IS-UL Issue A, with per-tap UL 1480 dB(A).
  - The filename/header mismatch recurs: `D190-01-201-IS_Issue_5` is really D190-00-201-IS.
  - productType is empty on this product and on the siblings D2XL1FV725CN1A1R and D1XL2FV725CN1A1R (flagged).
- t08 (23 Sep), **Aiphone DA-4DS:** the store's run-on title was Aiphone's own product-page sentence. `aiphone.com/wp-json/wp/v2/search?search=` is honest (bogus 0, known-good IX-DV 10). The DA-2/4DS installation manual FK0954 is an image-only 2002 scan, so render it.
- e10 (23 Sep):
  - **DITEK DTK-3MB:** "3-position mounting base (6 pairs)", 3.25 × 4.5 in., on SPS-100010-001 Rev 19 and -003 Rev 6 (04/26). The base-dimension row repeats the 2.65 in. module height, so only the footprint was published. `/wp-json/wp/v2/search?search=` is honest; `/products/<sku>/` returns 200 with 0 B. The family's productType disagrees (DTK-4MB is "Modules"; flagged).
  - **Apollo ORB-HT-11018-APO:** PP2631/2019 Issue 1 maps CS to 11006, and 11018 is its flashing-LED version. **CS = static (fixed temperature); CR is the rate-of-rise twin.** Declared to EN 54-5; **no UL listing, the third Apollo item so far** (flagged). The Apollo WP REST API was down (2,728 B maintenance page for real and bogus alike); `products-sitemap.xml` (524 URLs) and the product pages worked. The Apollo 404 now measures 78,529 B.
- t12 (23 Sep), **SDi / Detector Testers:**
  - `detectortesters.com` returns 406 to curl, but `urllib` with a Safari UA gets 200. Product slugs are the order codes; a bogus slug returns 404 at about 99,934 B. `sdifire.com` `wp/v2/search` and `wp/v2/media` discriminate.
  - **TS3 is the Testifire 1000/2000 capsule and TES3 is the XTR2 cartridge; they are different consumables.** The live "TES1" on the XTR2 kit was wrong.
  - Old-to-new code map (SDi, Sep 2024): TESTIFIRE1001 → TESTIFIRE-XTR2, TESTIFIRE1000 → -XTR2-HEAD, TF1851 → -XTR2-20F, TF1823 → -XTR2-30F.
  - Duplicate flagged: the listing with SKU TS3, "(TS3-3PACK-024)", against TS3-3PACK-001.
