<!-- Registro de casos do projeto TFAS. Movido VERBATIM de CLAUDE.md em 23 Sep 2026; nada foi reescrito. Nao e carregado automaticamente: leia sob demanda. E cronologico: entradas posteriores corrigem anteriores; em caso de conflito vale a mais recente e o nucleo em CLAUDE.md. -->

# siemens

- **`/api/khub/maps` has patchy, not partial, coverage of the US fire catalogue.**
  It carried the XMS pull stations, `ILED-XC`, `ABHW-4S` and `HI921` first try, and
  **did not carry the MSM line, `FDT421` or the MTH appliances at all** &mdash; one
  agent grepping it for horn/notification terms got 22 rows of which 2 were fire, the
  rest European HVAC. So it is worth one grep of the `metadata` ProductType field,
  and no more: **when it misses, web-search the A6V asset number and go straight to
  `/go/`**, which has worked every time. A bare
  `sid.siemens.com/api/khub/documents/<id>/content` URL also turns up in search
  results directly, with no `/go/` round trip.
  For a legacy Siemens part, web-search the A6V asset number and go straight to
  `/go/<AssetID>`. Also note `support.industry.siemens.com/cs/attachments/...`
  returns `text/html` at ~440 bytes for the same asset that `/go/` serves properly.
- **Siemens: the document index is down, but two ways in work.**
  `https://sid.siemens.com/api/khub/documents` returns HTTP 504 after ~60 s, every
  time. Two proven workarounds: (1) `https://sid.siemens.com/api/khub/maps` **does**
  respond and returns the whole index (~1,276 entries, 8.5 MB JSON) &mdash; grep the
  blob as with the JCI hub, then fetch HTML topic books via
  `/api/khub/maps/<id>/topics` and `/api/khub/maps/<id>/topics/<topicId>/content`.
  (2) **The pretty URL resolves the opaque document id even while the index is down:**
  `curl -D - https://sid.siemens.com/go/<AssetID>` returns `303` with
  `location: .../v/u/<hashId>`, and `/api/khub/documents/<hashId>/content` then serves
  the PDF. So **any Siemens A6V asset number can be fetched directly.** This unblocks
  Siemens, 189 products and 82,982 impressions of `ranked_v2`, and it is what cost
  `SL2HSWR-F` its candela values in an earlier batch.
- **A second innocent origin for a false &quot;replaces&quot; claim: the data-sheet
  revision line.** Siemens sheets carry `Supersedes sheet dated 5/06 (Rev.1)` in the
  footer. **That supersedes a *document*, not a product**, and it sits on exactly the
  older sheets a reseller would be reading. Grepping for `supersed` therefore returns a
  hit on almost every legacy Siemens sheet that means nothing about the catalogue. Read
  what the word is attached to before counting it.
- **The Siemens coexistence sentence, misread as supersession. Hit twice; assume it
  is behind every Siemens "Replaces" claim.** Siemens data sheets carry an
  Installation paragraph of the form *"Model X may be installed on the same SLC with
  the following &hellip; Y devices"*. That is devices sharing a loop, not one
  replacing the other. Two store titles were built on it:
  `XTRI-D "(Replaces HTRI-D)"` and `OH921 "(Replaces HFPT-11)"`, and **neither claim
  appears in any Siemens document.** The OH921 case is worse than a bad cross-
  reference: HFPT-11 is the FirePrint *thermal* detector, a heat detector, while
  OH921 is photo-plus-thermal multi-criteria &mdash; and the store stocks an HFPT-11
  page separately. The heat-only member of the 921 family is `HI921`. Both titles are
  corrected, with the interoperability statement moved into the body.
- **A summarising fetch can manufacture a lifecycle claim out of page chrome.** An agent's
  WebFetch of a Honeywell Buildings SWIFT page reported the product *&quot;marked as
  discontinued&quot;*. Curling the same page shows `Discontinued` appears **only as a UI
  label string inside the page JavaScript** (`discontinuedText`), attached to nothing.
  Had that reached the owner it would have been a discontinuation flag on a live product,
  sourced from a template. **Never take a lifecycle claim from a summarising fetch; curl
  the page and find what the word is attached to** &mdash; the same discipline the
  Siemens `Supersedes sheet dated` footer already demanded, one layer further out.
- **`sid.siemens.com/go/` resolves A6V ASSET numbers only, never part numbers.**
  `/go/FC901-U3` 303s to an `unresolved` deeplink. Web-search the A6V number first, then
  call `/go/<A6V>`; that worked first try on two documents. Also confirmed, and worth
  knowing before spending the fetch: `/api/khub/maps` contains the string `FC901`
  **zero times** &mdash; its Cerberus entries are DMS, PACE and PRO Modular only &mdash;
  and `file -b --mime-type` reports **`text/plain`** for that 8.5 MB JSON.
- **Ninth incomplete-product case, and the priciest yet in proportion: `FC901-U3` is
  panel electronics with nothing to mount them in.** Siemens Data Sheet `9813`'s
  Electronics Package block lists the kit as exactly two items &mdash; `FCM901-U3` main
  board and `FP2011-U1` 170 W supply &mdash; while the Specifications paragraph on the
  same sheet says the FC901 FACP *&quot;consists of a main board, a 170-Watt power supply,
  **and a Model FH901-U3 / R3 system enclosure**&quot;*. Three components; the kit is two
  of them. **At $911.90 the buyer receives no enclosure**, and separately no battery
  bracket (required for seismic certification), no trim kit, no batteries.
  The `type` field said **Boards** and agreed with the raw-ERP title, raising nothing
  &mdash; fifth instance. It is not a board: a buyer filtering for boards gets a two-part
  kit, and a buyer filtering for control panels never sees it. Note the sibling
  `FCM901-U3` genuinely *is* a board, which is presumably how the field was set.
- **&quot;Platinum&quot; is a colour, and a merged cell hid it.** `4007-9102` was a
  three-way question &mdash; finish, feature tier or model designation. `S4007-0001`
  Rev. 22 Table 3 lists `4007-9101` **Red** and `4007-9102` **Platinum** against one
  vertically merged Description cell, confirmed at 250 dpi. Also settled: the panel is a
  **complete enclosed unit** including one `4007-9801` zone/relay card, and the two 12 V
  batteries are not in it.
  By contrast `FCI2016-U1` is a **bare board**: installation instructions `A6V10356958`
  show the FC922 built from **eleven separately located items**, and the box holds none
  of the back box, doors, operating unit, supply, trim kit, battery bracket or batteries.
  **Two Siemens panel-family parts in one batch, opposite answers** &mdash; which is why
  the complete-product question has to be asked per part and never inferred from the
  family.
- **A part number that does not match itself, in a feed attribute, for the second time.**
  The live `ZR-MC-R` title rendered the Siemens catalogue number as **`Part 500636169`**
  with the hyphen stripped, while its own description body had it correctly as
  `(500-636169)`. Siemens prints `500-636169`. That is the `868STRC-AQ` shape in
  miniature &mdash; a part number in a title that cannot match a search for itself &mdash;
  and it is the same punctuation-stripping mechanism as the 185 frequency ranges, showing
  up one product at a time. Corrected in the title.
- **The queued `ZH-MC-W` title defect now has its missing class noun, from a sibling's
  research.** That title is a part number plus an unsourced supersession parenthetical
  with **no class noun at all**. Data Sheet 2584 describes `ZH-MC-W | 500-636162` as
  *&quot;Z Horn: Multi Candela (Wall), White&quot;* and `P84860-001C` Table 1 gives
  `ZH-MC` an **X in the Horn column plus a 15/30/75/110 cd strobe** &mdash; so
  **`ZH-MC-W` is a horn strobe**, and **`ZR` is the strobe-only half of the Z Series while
  `ZH` is the half with a horn**. Siemens' own &quot;Z Horn&quot; wording is itself the
  misleading part, which is the `FSL-E3` situation: keep the manufacturer's name and put
  the class in the body.
- **Route notes from v2b29.** A **new EDAM path shape**: the `hon-ba-fire-` prefix extends
  beyond `datasheets/` into `manuals-and-guides/**installation-guides**/`, where
  `hon-ba-fire-52544.pdf` resolved at 2.15 MB after the bare, `hbt-fire-` and
  `user-manuals/` forms all returned the 8,047-byte fingerprint. **Potter's real path is
  `pottersignal.com/product/datasheet/<docnum>-<REV>-<MODEL>_DATASHEET.pdf`** for current
  sheets and `<docnum>_<MODEL>.pdf` for older ones &mdash; find it from the product page,
  do not build it, because `8830102_IPA-4000.pdf` 404s while Rev K is
  `8830102-K-IPA-4000_DATASHEET.pdf`. And **`xtralis.com/file/<id>` is not uniformly PDF**:
  `/file/12021` returned 226,238 bytes of `text/html` where `/file/12016` and `/file/12064`
  served clean PDFs, caught only by the mime check &mdash; enumerate the file ids from the
  `xtralis.com/product/<id>` page. `sid.siemens.com/go/<A6V>` worked first try on both
  assets, and **the sibling check paid again: the SL ceiling series is 15/30/75/95 cd
  against the wall's 15/30/75/110**, so the two sheets cannot be crossed.
- **The Gentex coexistence sentence, confirmed independently from the other side of the
  pair.** `S1209`'s title asserted *&quot;Replaced by S&quot;* with **no class noun at
  all**. Searched in the S1209 data sheet `551-0001-02`, the S1209 manual `550-0008-AAC`
  and the S/C/SC/H sheet `SCSCH-01`: **replac, supersede, discontinu and obsolete connect
  the two nowhere**, and the only documented link is the tandem-interconnect compatibility
  list. That is the Siemens *&quot;same SLC&quot;* failure on a **third brand**, and both
  halves of this pair were researched by different agents in consecutive batches, each
  reaching it independently.
  **And the disproof here is a mechanism, not an absence:** the S is multi-criteria,
  **5.5 in.** across, UL 217 **9th Edition**, 0.045 &rarr; 0.055 A; the S1209 is
  **photoelectric, 6.25 in.** across. A successor three-quarters of an inch smaller **leaves
  a ring on every retrofit**, so it is not a drop-in even if someone wanted it to be.
- **Thirteenth coordinator premise wrong, and this one would have published a candela
  setting that does not exist.** The v2b32 briefing told an agent the Siemens SL2
  ceiling set was **15/30/75/95 cd**. Siemens Data Sheet 2600 gives
  **15, 30, 75, 110, 150 and 177 cd** on a six-position slide adjuster, and **there is
  no 95 cd setting on the series at all.** Note where the wrong number came from: 95 cd
  **is** a real ceiling setting &mdash; on the System Sensor L-Series. This is the
  `ELSTWC-ALA` cross-brand adjacent-row trap operating one level up, **inside the
  coordinator's own briefing** rather than inside a live page. Same mechanism, same
  brand pair, second instance.
- **A supersession claim disproved in BOTH directions, which is stronger than a bounded
  negative.** The live `HFPT-11` title carried *&quot;(Replaced by OH921)&quot;*. The
  agent searched both HFPT-11 documents for `OH921`, `HI921`, `replac`, `supersed` and
  `discontinu` &mdash; **zero hits** &mdash; and then searched Siemens' own **OH921**
  installation document for `HFPT` &mdash; **zero hits**. Every previous supersession
  disproof on this project searched the *claimed predecessor's* documents only, which
  leaves open that the successor's sheet states it. Checking the other side costs one
  fetch and closes that gap. This file already records the same claim being wrong once
  before, from the Siemens coexistence sentence; it is now wrong in both directions.
  Claim moved to the body with the class difference stated: **OH921 is multi-criteria
  smoke, HFPT-11 senses heat alone, and the heat-only 921 is `HI921`.**
- **A back-box answer that runs OPPOSITE to the Gentex and System Sensor pattern, and it is
  manufacturer-stated.** This file records two brands where an appliance's outdoor listing
  is **conditional on a separately ordered box** (Gentex's GBBB, System Sensor's MWBB). On
  Siemens the MSM line inverts it: DS 6184 p1 reads ***&quot;Both the weatherproof and
  explosion-proof models are shipped complete with backbox. (Backbox is optional with other
  models&hellip;)&quot;*** &mdash; so `MSM-BOX` exists **for the models that lack one**.
  **Do not carry a back-box convention across brands in either direction.**
  Two things the agent declined to assert on that part, both right: **&quot;single
  action&quot; is nowhere in the sheet** (Siemens distinguishes models only by adding
  *Double Action* to `MSM-KD`), so the copy names the double-action sibling and lets the
  table speak; and **`NEMA` and `outdoor` each occur zero times**, so no NEMA type was
  claimed on a part titled weatherproof.
- **A featured photograph on a series sheet is captioned for ANOTHER model, and a
  summarising fetch fell for it.** DS 6184's page-1 image is captioned `MSM-INST` and page 2
  `MSM-KD-WP`; a web summary duly reported that `MSM-K-WP` *&quot;appears to be a
  double-action model based on the Siemens data sheet&quot;*. That is the page-chrome
  lifecycle trap's cousin: **the image, not the text, is what misled**, and it is a live
  mis-assignment trap for any summarising tool on a multi-model sheet.
- **Route notes.** **`fireprotection.gentex.com/resources` is a single page listing ~90
  first-party PDF paths** &mdash; one fetch enumerates the whole Gentex library, which is
  the answer to that brand's family-by-family path construction (this family failed on four
  constructed names at 7,270&ndash;7,276 bytes, the second family after the S-Series against
  the GB bells where it worked first try). **`sid.siemens.com/go/<A6V>` resolved first try
  on all six Siemens assets**, while two `api/khub/documents/<hash>/content` URLs taken from
  search results served **the wrong document entirely** &mdash; resolve the A6V number
  first. And **a Siemens installation document may resolve as a MAP rather than a
  document**: `/r/<hash>/root` means use `/api/khub/maps/<id>/topics` then
  `/topics/<topicId>/content`.- **A supersession HELD at the coordinator's own gate, and the reason is worth more than
  the row.** `BEAM1224S`'s live title carries *&quot;(Replaced by OSI-R-SS)&quot;* and an
  agent reported finding the **System Sensor Product Announcement, February 2019**, on
  letterhead, with an explicit *&quot;New Model No. OSI-R-SS | **Replaces** BEAM1224 and
  BEAM1224S&quot;* table &mdash; and proposed keeping the claim in the title, which this
  file's rule permits when a manufacturer states it.
  **The coordinator could not retrieve that document.** A web search returns only
  distributor pages &mdash; ADI, Anixter, Silarius and **this store's own listing** &mdash;
  which is the correlated-consensus problem exactly, and five constructed EDAM slugs for an
  OSI-R datasheet all returned the 8,047-byte fingerprint. So the page was **held, alone,
  while the other five published**, and the agent was asked for the URL, host, byte size,
  mime, document number and the verbatim row.
  **Holding cost nothing, and that is the point of doing it here rather than arguing.** The
  live title already carries the claim, so not publishing leaves the status quo; publishing
  would newly rest a feed attribute on a document nobody but its finder has seen. **A claim
  that is already live is not thereby verified, but it is also not made worse by waiting.**
  Recorded as an open verification debt, the way the `P85756F` debt was carried for five
  batches before a search closed it.
  Worth keeping from the same row anyway: the agent ran the **mechanism check in the
  favourable direction** and said so. This file's `SIGA-HRS` test asks for a spec that would
  have to be equal if a supersession were true, and there it *fell* (70 ft to 50 ft),
  disproving the claim. Here it **improves**: `BEAM1224(S)` reaches 328 ft only with the
  `BEAMLRK` kit required beyond 230 ft, where the successor is stated as 16&ndash;328 ft
  standard with no kit. **A mechanism check that corroborates is as informative as one that
  refutes**, and this file had only recorded the refuting case.
- [CORRIGIDO — não reproduziu: 302 &quot;Object moved&quot; para artigos reais e inventados; ver neste arquivo] **The dropped word was the one that separates two stocked catalogue numbers.** The live
  `HTRI-M` title said *&quot;Single Interface Module&quot;*. Siemens' own Industry Mall calls
  `HTRI-M` the **&quot;Mini Single Input Module&quot;** and `HTRI-S (500-033370)` the
  **&quot;Single Input Module&quot;** &mdash; and the store carries both. **The missing word is
  &quot;Mini&quot;.** Note the routing trap that made it findable: Data Sheet `6304 Rev. 8` is
  titled *HTRI-Series Interface Modules* and lists **only** HTRI-D/-R/-S &mdash; `HTRI-M` and
  `500-034000` appear **zero times in it** &mdash; so the obvious document is the wrong family,
  and every spec in it belongs to the full-size modules that take a 4 in. box and ship with a
  faceplate. New route: **`mall.industry.siemens.com/mall/en/buildingtechnologiesusa/Catalog/Product/<number>`
  is a usable first-party endpoint** &mdash; 403 to WebFetch, **HTTP 200 to `curl` with a Safari
  UA** &mdash; giving the market-facing number, the description, the **PLM lifecycle status**
  and net weight, and it discriminates (bogus article &rarr; 33,648 bytes, no `productMfn`).
  It records `HTRI-M` as **&quot;Product phase-out since 05-16-19&quot;**, which explains its
  absence from the current sheet; flagged to the owner, nothing published.
- **ONE SIEMENS DATASHEET, THREE INCOMPATIBLE STATEMENTS, AND THE INSTALLATION SHEET RESOLVED
  IT BY ARITHMETIC RATHER THAN BY AUTHORITY.** Data Sheet `7322`: page 1 A&amp;E says
  *&quot;PSC-12 and PSX-12 **each include** a PTB&quot;*; page 2 prose says *&quot;when **more
  than one** PSX-12 is used, a second PTB is required&quot;*; the page 3 parts table says
  *&quot;only required for applications with **more than two** PSX-12 extenders&quot;*. Both of
  the latter render-confirmed at 300 dpi, and **`8322` reproduces the identical pair** &mdash;
  a house-template defect, not extraction error.
  **The resolution is a mechanism and it is better than picking a side.** Installation
  instructions `315-034877-4` label **P4 and P5, each &quot;To PSC-12 or PSX-12&quot;**, so one
  board serves **two** supplies. With up to three PSX-12s per system, the &quot;more than
  two&quot; threshold is arithmetically impossible. **The copy publishes the two connections
  and neither sentence**, which lets a buyer count their own supplies.
  **And the page-1 A&amp;E bullet is disproved by Siemens' own kit table**, read off a 260 dpi
  render because the rotated column headers extract one character per line: the columns are
  *PSC-12 / PTB Kit*, *PSX-12* and *PTB (Only)*, and **the PSX-12 column contains no PTB**. The
  *PTB (Only)* column holds exactly one entry, **&quot;Four #10 Hex Nuts&quot;** &mdash; so the
  bare PTB SKU ships as a board and four nuts. That is the carton question answered from a
  table nobody would think to open.
- **A new Siemens route that sidesteps the recorded 504 entirely, and a failed reproduction
  recorded as such.** `cache.industry.siemens.com/dl/files/<n>/<id>/att_<n>/v<r>/A6V*.pdf`
  serves A6V assets first-party and mime-clean with **no `/go/` round trip and no khub call**,
  where `support.industry.siemens.com/cs/attachments/...` returns **403 at 442 bytes**.
  Against that, this file records `mall.industry.siemens.com/.../Catalog/Product/<article>` as
  answering HTTP 200 to curl with a Safari UA; it returned **HTTP 302 with a 235-byte
  &quot;Object moved&quot;** for two real article numbers **and an invented one alike**.
  **Recorded as a non-reproduction rather than a correction**, on the `cdn.power-sonic.com`
  precedent &mdash; the earlier measurement may have been on a different article shape, and
  saying so honestly is what lets the next person test it properly.


- **`PAD5-6A` (v2b52):** Data Sheet 3364 (A6V11231624) Rev. 4, Sep 2025, from `cache.industry.siemens.com/dl/files/869/109790869/att_1047634/v3/A6V11231624.pdf`. Kit = PAB-ENCL black 1HU enclosure + PAD-5-MB with one adapter plate + FP2011-U1 170 W &mdash; complete, not the `FC901-U3` shape; batteries not in the kit list. The sheet contradicts itself on 1HU battery capacity (18 vs 35 Ah) and 6.5 vs 6 A &mdash; neither battery figure published. Type Kits flagged.

- **[Correction of a briefing compression] SL (first generation) HAS a 95 cd setting; the &quot;no 95 cd&quot; rule is SL2 only (audit t04).** Data Sheet 2594 (A6V11396487) Rev. 5 Feb 2023 p4 row `SLSCW-F | S54329-F15-A1 | Strobe | Ceiling | Clear | WHITE | FIRE` (coordinator-verified); p1 *&quot;multi-candela settings (15 | 30 | 75 | 95cd)&quot;*; P85582-001A agrees. SL2 (Data Sheet 2600) is 15/30/75/110/150/177. Data Sheet 2600 Rev 3 states no supersession of SL. A bogus A6V via `/go/` returns a 2,611 B &quot;unresolved&quot; page.
