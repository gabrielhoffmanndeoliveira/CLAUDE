<!-- Registro de casos do projeto TFAS. Movido VERBATIM de CLAUDE.md em 23 Sep 2026; nada foi reescrito. Nao e carregado automaticamente: leia sob demanda. E cronologico: entradas posteriores corrigem anteriores; em caso de conflito vale a mais recente e o nucleo em CLAUDE.md. -->

# metodo-geral

- **Go to installation instructions for specs, not the operation manual.** For
  `FCM2041-U3` the installation document carried the full electrical ratings and
  mounting detail and the Operation Manual carried none of it.
- **On `customer.resideo.com/en-US/Pages/Product.aspx`, the `pid` needs the `/U` suffix
  kept and URL-encoded** (`TH6320WF2003%2FU`); bare `TH6320WF2003` returns
  &quot;not a valid material number&quot;. The strip-the-suffix rule applies to
  *searching*, not to this endpoint &mdash; and searching the `33-` document number
  directly was faster than either.
- **The sibling part is the dominant failure mode.** Part numbers differ by one
  character and describe different products. Find the full ordering table and
  confirm which row is this exact part before writing anything.
- **The generation trap:** one document number can cover two product generations
  at different revisions. Confirm the revision covers the part.
- **The adjacent-row trap, in the other direction: reusing a sibling's spec row.**
  `SPWL` (speaker only) is rated **79/82/85/88 dBA** at its four taps; `SPSWL`
  (speaker strobe) is **77/80/83/86**, two dB lower at every tap,
  in the same two documents. Copying the sibling's row would have published a wrong
  number on a page that otherwise looked right. Read the row for the exact part, even
  when the parts differ by one letter and the table looks uniform.
- **Splitting a sibling pair across two agents is worth doing, and the disagreement is
  the point.** `IO-SDC1` and `IO-SDC2` went to different agents with instructions to
  establish the real separator and to compare shared figures afterwards. Both
  independently found the same two differences &mdash; loop count *and* host panel, the
  iO-SDC1 being the only one that fits an iO64 &mdash; which neither could have guessed
  from the numeral. **And the cross-check caught a live defect:** one agent published
  `80 mA alarm` while the other established that `E85001-0135` **contradicts itself on
  alarm current in both revisions checked** (card table 80/70 mA, panel Loop-circuit
  block 125/115 mA) and had omitted it. The contradicted figure was removed before
  publishing, from the bullet **and from the closing paragraph, where it had survived
  the first pass**. Standby, which agrees across both tables and revisions, was kept.
  **Pair-split the obvious sibling pairs, and diff the shared numbers at merge.**
- **The owner's structured-data decisions are consolidated in
  `/tmp/tfas/DECISOES_DO_DONO.csv`** &mdash; **190 rows as of 22 Sep 2026** (29 when this note was written), each with
  the current value, a recommendation, the reasoning, and a confidence column that
  separates **10 demonstrably wrong** values from **6 judgement calls**, **4 feed /
  lifecycle decisions** and **3 unsourceable pack counts**. Append to that file
  rather than letting flags scatter across batch notes; ten batches of scattered
  flags is what made the consolidation necessary.
- **Discontinuation is a feed decision, not a copy decision.** Four SKUs in one batch
  were marked discontinued by their own manufacturer while carrying live prices and
  feed entries. House rules keep lifecycle out of the copy; that leaves the question
  open rather than answered, so it goes to the owner.
- **A correction can introduce a new error, so corrections need verifying too.**
  The RA100Z closing paragraph was rewritten on 21 Sep 2026 to fix two real faults,
  and the rewrite asserted that *"the RTS151 and RTS151KEY are key-operated remote
  test stations"*. **The RTS151 is magnet-operated** &mdash; it ships with an M02-04
  test magnet and has no key at all; the `KEY` suffix on its sibling is the entire
  difference between the two part numbers, and the sentence collapsed it. Caught two
  batches later only because the APA151 came through the queue and its agent was
  asked to rule on the live text. **Put corrected pages back through cross-reference
  review; do not treat a correction as settled because it fixed what it set out to
  fix.**
- **The type field's silence has an inverse case worth naming.** `ELFHNW-N` is typed
  **Horn Strobes** and has **no strobe** &mdash; `TD450159EN` Table 5 lists it under
  Sounders with an empty Strobe Candela column and draws its current from the
  &quot;Horn Only&quot; table. But the **title was already correct**, so the type agreed
  with nothing and still raised nothing; the mismatch surfaced only from the ordering
  table. The recorded rule is &quot;the type field is a signal when it disagrees with the
  title and no evidence when it agrees&quot;; this is the case where it disagrees with a
  *correct* title, which is the same defect pointing the other way. **Check the type
  against the document, not against the title.**
- **A spec that belongs to the parent, not the accessory, and differs by parent family.**
  Duct air velocity is a property of the **detector**, not of the sampling tube: 100 to
  4,000 ft/min for SuperDuct and Optica but **300 to 4,000 ft/min for the KI-SDH
  housing**. A tube page serves several families, so one velocity figure on it would be
  wrong for one of them. This inverts the recorded rule that *accessory specs often live
  in the parent's data sheet* &mdash; they do, and that is exactly why they may not be
  the accessory's specs at all. Check whether the figure varies across the parents the
  accessory fits before carrying it over.
- **A merged cell that changes whether a device may be installed at all.** `A05-0456`'s
  Candela Derating table merges *&quot;Do not use below 32 &deg;F&quot;* across the
  **15, 15/75 and 30 cd** rows &mdash; confirmed by word coordinates at y=618.9 and a
  300 dpi render. `SRK` is a standard-candela device, so it falls inside that cell. **A
  designer laying out on 15 cd in an unheated space would be specifying a device the
  manufacturer says must not be used there**, and no plain-text read of that table would
  show it. Published for exactly that reason. (75 derates to 44 cd and 95 to 70 cd at
  &minus;40 &deg;F; 110 and 115 unchanged.)
- **A supersession that the manufacturer does state, and a battery-box colour that it
  does not: two claims, opposite handling, same batch.** See the `FPTI-951-IV` and
  `BB-55F` entries above. The pair is worth keeping together because it shows the rule is
  not scepticism &mdash; it is the source. A sourced claim goes in the title; an unsourced
  one goes in the body or nowhere.
- **Tenth incomplete-product case, and the `CM` suffix is the whole warning.**
  `HPFF8CM` ships as a **bare chassis**: Honeywell Power `53499 Rev B4` &sect;1 reads
  *&quot;The HPFF8CM is a chassis-mount model &hellip; These separately sold cabinets are
  also referred to as the large equipment enclosure&quot;*, and `DH-60541:C1` marks the
  enclosure **&quot;Order separately.&quot;** At $819.90 a buyer expecting a boxed supply
  like the plain `HPFF8` receives a chassis with no backbox, no door and no batteries.
  **`CM` = chassis mount and `HPFF` = Honeywell Power FireForce**, both manufacturer-
  stated. The live copy named &quot;SBBD4 or EQBBB4&quot; where Table 2.1 lists **eight**
  cabinets across one-, two-, three- and four-unit sizes &mdash; an arbitrary pair, and
  **Honeywell hyphenates them** (`SBB-D4`, `EQBB-B4`), so the unhyphenated forms in the
  live copy would not match a search either.
- **A vendor's own product page can describe the successor, which makes it the worst
  place to take a photo from.** `avire-global.com/.../8100-v4g/` now describes the
  **8100-V4GS**, a newer model, and every image on it is named `8100-4gvs`. Taking the
  photo from the URL carrying the part number would have published the successor's
  picture. The images used are the dated upload files whose **filenames** carry
  `8100-V4G`. **A URL containing a part number is not evidence that its contents are that
  part** &mdash; the same lesson as the wrong-document-family rule, applied to a web page.
- **`catalogo_full.json` carries Shopify's real `sku` for all 16,031 products, and that
  ends the SKU-extraction problem.** Joining on `id` gave 1,261 of 1,261 rows with zero
  handle mismatches and zero disagreement with the partial `skus_B.json`. The handle-tail
  validation still earns its place as a *check* &mdash; it confirmed 1,258 and skipped
  exactly the three unrepresentable cases &mdash; but no extraction is needed. **Stop
  parsing titles for part numbers.**
- **`polyphaser.com` is Incapsula-gated, which is a new fingerprint and turns one open
  frequency reading into a BOUNDED negative rather than an unknown.** Both
  `polyphaser.com/Images/Downloadables/Datasheets/IS-50NX-C2_datasheets_US.pdf` and the
  series sheet return **~965 bytes of `text/html` containing `_Incapsula_Resource` and
  `NOINDEX, NOFOLLOW`**, to curl and to a full Safari user-agent alike. Add it beside
  Sucuri's 202-plus-`sgcaptcha` and Akamai's 456-byte Access Denied.
  **What that leaves is honest and worth stating precisely.** Search indexes the
  manufacturer's own datasheet under the page title *&quot;Type N F/F Coaxial RF Surge
  Protector, **125MHz**&quot;*, and four distributors agree on 125&ndash;1000 MHz &mdash;
  but distributor agreement is correlated copy and has been wrong five times on this
  project, and a search-result page title is not a document read. **So `1251000` stays
  open**, with a named cause rather than a shrug: the document exists, is first-party, and
  is behind a WAF. One fetch from an unblocked route settles it.
- **Addressing method can split a model line, and it changes the current draw.**
  `KIR-OSD` is the **rotary-addressed** Optica detector at 43 &micro;A standby and
  70 &micro;A alarm; the electronically-addressed twin draws 32 and 45 &micro;A. Two
  parts under one family name, differing in how the address is set, with a ~50%
  current difference that lands straight in a battery calculation. **The rotary /
  electronic split is a real separator on this brand** &mdash; do not read a shared
  family name as a shared spec sheet row.
- **A trailing numeral can be a count, not a model distinction.** `PCVS-2`'s `2`
  records **how many switches the unit contains**, not which model it is. So the
  sibling-part rule has a third form alongside &quot;one character apart&quot; and
  &quot;suffix encodes a protocol&quot;: **the number may be a quantity inside the
  product**, and a title that reads it as a generation number asserts something the
  manufacturer does not.
- **Three supersession claims in one batch, and the split was two to one again.**
  `SCWLED-CLR-ALERT`'s &quot;replaced by&quot; **is** manufacturer-stated &mdash;
  bulletin `M23.2SS`'s REPLACES table &mdash; so it stayed in the title. `KIR-OSD`'s
  and `GCSVWN`'s are unsourced and were moved to the body. That is now the settled
  handling and it has held across four batches: **the bulletin is the source, the
  datasheet almost never is, and an unsourced claim costs money in two channels if it
  sits in a feed attribute.**
- [CORRIGIDO — não reproduziu em mircom.com numa medição posterior; ver mircom-secutron.md &quot;did NOT reproduce&quot;] **A host can serve recompressed bytes per request, which silently disables MD5
  de-duplication.** Measured on mircom.com by an agent re-fetching four accepted images:
  one matched, and `1150` came back 41,939 &rarr; 36,222 bytes, `RTI-1` 85,713 &rarr;
  62,535, `EC-220A` 57,647 &rarr; 53,671 &mdash; **different bytes and different MD5 for
  the same URL**. So on an image-optimising host the `md5` and `bytes` in a harvest are
  **a measurement at download time, not an identity**, and every collision check built on
  them returns a clean result for the wrong reason. The perceptual hash is the
  replacement, and it is the second independent argument for the pass above.
- **`S3000` confirmed a FOURTH time, by a fourth reader on a fourth document.**
  `E85010-0055` page 1 prints it in the approvals block beside CSFM 7165-1657:0186/0193
  and the EN 54 marks. The &quot;bogus S3000&quot; note this file once carried is
  disproved four times over; leave it settled.

- **The `2099-` series is THREE sheets, not two, and the accessory pairing is
  line-specific.** This file records `S2099-0007` (moulded) with `S2099-0010` (releasing)
  as the exception inside it. `2099-9139` is in **neither**: it is in **`S2099-0009`,
  &quot;Non-Coded Manual Stations, Cast Metal Construction&quot;**, Rev 7 09/2020, row
  coordinate-verified as *&quot;Dual Action Station with PUSH Lever; SPST, N.O.&quot;*
  **So the lesson that produced the &quot;carry the exception&quot; rule needed one more
  exception carried** &mdash; and the compression failure it warns about is fractal.
  **The break-rod/breakglass accessory rule does NOT cross lines, and following it here
  would have cross-sold the wrong part.** Measured in both documents: `S2099-0007`
  Table 3 carries `2099-9803` breakglass and `2099-9804` break-rod and contains
  `2099-9829` **zero** times; `S2099-0009` is the converse &mdash; `2099-9829` (twelve
  replacement break rods) present, `2099-9803`/`2099-9804` **absent**, the word
  &quot;breakglass&quot; **absent**. **The cast-metal line has no breakglass option at
  all.** The live title was also missing both **dual action** and **cast metal**, and
  `2099-9138` one digit away is the single-action version of the same casting.
  Dimensions came from a 200 dpi render: page 3 is pure vector linework with no text
  layer, the invisible-dimension trap firing as briefed.
- **A manufacturer naming a product as its own predecessor.** Honeywell's 6820UEVS page
  reads *&quot;are direct replacements for the **6820UEVS**/5820XL-EVS FACP&quot;*.
  Nothing was published from it. Worth keeping beside the self-contradicting-document
  entries: a supersession sentence can be circular, and grepping for &quot;replacement&quot;
  would have returned it as a hit.
- **The same capacity figure belonging to two different batteries at different rates.**
  `PDC-121000` is **100.0 Ah at 20 hr and 95.0 Ah at 10 hr**; `PDC-121050` is **105.0 Ah
  at 20 hr and 100.0 Ah at 10 hr** &mdash; so **`PDC-121050`'s 10-hour capacity is exactly
  `PDC-121000`'s 20-hour figure**, and both are the same physical size. A bare
  &quot;100Ah&quot; is true of both products. This file already required the rate to be
  stated; here are two SKUs in one batch where omitting it makes the titles
  indistinguishable.

- **Datasheet page 3 is series boilerplate, byte-identical across models of different
  capacity.** PDC-122500's and PDC-12140's page 3 are the same bytes, and its *&quot;UL
  1989 certified for valve-regulated&hellip;&quot;* and *&quot;Sealed lead-acid&hellip;
  UN2800 non-spillable&quot;* lines are a **certification glossary attached to no
  model** &mdash; the series-wide-block trap in its purest form, because those sentences
  would have read perfectly naturally in any of the eleven titles. **No certification,
  &quot;sealed&quot; or &quot;non-spillable&quot; claim went into any of them.**
- **A metadata hit is not a text hit, and the JCI index is broader than the documents it
  describes.** The hub's `product_code` field lists `4100-5125` against `S4100-1031` &mdash;
  and the strings `4100-5125` and `RPS` each appear **zero times in that document**, which is
  the current 4100ES sheet covering the ES-PS/ES-XPS instead. The real rows are in the legacy
  `S4100-0031` Rev. 42, `S4100-0103` Rev. 11 and `S4100-0038` Rev. 15. **Grep the served PDF,
  not the index entry** &mdash; and this file already records the same hub disagreeing with
  its own served document on the revision number.
- **The merged-cell trap settled a mounting assignment that plain text got wrong.**
  `S4906-0001` Table 1 emits &quot;Wall&quot; after the `4906-9103` row and
  &quot;Ceiling&quot; after `4906-9114`; word coordinates put Wall at the midpoint of
  9101/9103 and Ceiling at the midpoint of 9102&rarr;9117, and a 300 dpi render confirms
  **wall is 9101 and 9103 only, so `4906-9102` is a CEILING model.** The live title was
  already right. Table 6 needed the same treatment: **ceiling draws 50/83/155/211 mA against
  the wall block's 40/63/124/168 mA**, so reading the wrong block understates current by
  about 25%.
- **A sibling one letter apart with a different part-number scheme and a different companion
  module.** Data Sheet 8302 is the first document a search returns for `PSX-12` and it
  covers **`PSX-12M`** &mdash; it contains &quot;PSX-12&quot; without the M **zero times**,
  its part number is `S54430-C27-A1` rather than a `500-` number, and it pairs with a
  **PSFA** where the PSX-12 pairs with a **PTB**. Writing from it would have published the
  wrong part number *and* the wrong companion. Note also **`TZC-8B` is `500-034110` and
  `PSX-12` is `500-034120`** &mdash; one digit apart, in the same batch.
  The &quot;no battery charger&quot; claim was supported **by mechanism**, not absence:
  `7322`'s A&amp;E list covers both supplies together and gives *&quot;a built-in charger for
  up to 100AH batteries&quot;* to the **PSC-12 alone**, its PSX-12 prose says the extender
  *&quot;expands the main Model PSC-12 power supply **and battery charger**&quot;*, and
  `charg` occurs **zero times** in the extender's own 12-page installation instructions.
- **A series-wide block is how a wrong class noun SURVIVES, and `49VO-WRF` shows the mechanism
  exactly.** The part was titled and typed a **Horn Strobe** and is **visible only**: `S49VO-0001`
  Rev. 7 heads the series *&quot;Visible Notification Appliances&hellip; V/O (visible only)&quot;*
  and lists UL 1971 and ULC S526, with **`464` occurring zero times in the document**. What would
  have kept the wrong title alive is that **`horn` and `audible` each occur exactly once, both in
  platform-level sentences** &mdash; *&quot;detect its own strobe and/or horn output&quot;* &mdash;
  which read as model-specific appear to license it. Neither is attributed to a 49VO model.
  **Tenth instance of the type agreeing with a wrong title and raising nothing.**
- **A suffix confirmed manufacturer-stated where this file had only an inference, and it
  independently vindicated a photo rejection.** `TD450184EN` (Feb 2026) Table 1 is
  model-attributed: `STH-2R-ELSTC-F | Red | Strobe Plate FIRE` and `STH-2R-ELSTC-N | Red |
  no ltr`, under a group heading reading **&quot;2 Horn&quot;**, with prose *&quot;Supplied
  with two STH-15SR horns and one ELSTC strobe&quot;*. So the numeral is a horn count, as
  recorded &mdash; **and this is the document that proves the look-pass rejection of a `2R`
  photograph showing four horns was correct.** A verification run months apart on a different
  workstream confirming an image decision is the strongest form of corroboration this project
  gets.
  **Document defect on the same sheet, nothing published from it:** its plain-speaker block
  says *&quot;**STH-2R** &mdash; Supplied with **four** horns&quot;*, the STH-4R sentence
  pasted onto the STH-2R entry. The `-ELSTC-` variant's own paragraph correctly says two.
- **A derivable library path that does not cover every model in its own series, proved by a
  bogus control.** This file records `altronix.com/library/pdf/data_sheets/DS_<MODEL>.pdf` as
  *fully derivable inside the library*. `DS_AL300ULPD8.pdf`, `DS_AL300ULX.pdf` **and a bogus
  control** all returned the identical stable **13,828-byte** `text/html` 404 &mdash; so the
  model-level path does not exist for this family and the real document is the **series** sheet
  `DS_AL300ULXseries.pdf`. **A route that is derivable for the models it covers is not thereby
  derivable for the series**, and only the bogus control distinguishes &quot;this model has no
  sheet&quot; from &quot;this route is dead&quot;.
  From that sheet, a scoping distinction worth copying: its agency block is explicitly headed
  **&quot;All Models:&quot; for UL 294 / UL 603 / UL 1069 / UL 1481**, while **CSFM is
  separately scoped to &quot;AL300ULX, AL300ULXX and AL300ULXJ only&quot;**. UL 1481 went in
  the title and CSFM deliberately did not. **A listings block can carry two scopes on one
  page**, which is the series-wide-block trap with the manufacturer doing the attribution
  correctly for once &mdash; so read the scope line, do not assume the block is uniform.
- **The colour convention was PROVEN rather than asserted, which is the right handling for a
  look-pass contradiction.** `0500-06180` passed MD5 and dHash as unique and the photograph is
  **white**, while the SKU `HSSPK24-1575WLPPR` and the store title both end in **R**. Instead of
  invoking the recorded convention, the agent rendered the catalogue pair side by side:
  `0500-06210 HSSPK24-1575WLP**W**` is white with FIRE lettering and
  `0500-06200 HSSPK24-1575WLP**R**` is red. **So either the colour letter or the manufacturer's
  own asset is wrong**, and one carton settles it &mdash; flagged, nothing published. The same
  pass re-measured `0600-01440` rather than trusting the record: byte-identical to `0600-01430`
  at 35,042 B, HPS-BB standard against HPS-DBB deep, **and depth is the entire difference
  between the two products.**
- **Two more non-discriminating search endpoints, and on one of them the BOGUS control alone
  would have passed it.** `e2s.com/?s=` returns 18,507 / 18,551 / 18,628 bytes and **zero
  product rows** for a real term, a bogus term *and* a family name alike &mdash; so a
  bogus-only control reads &quot;different bytes, endpoint works, part absent&quot; and is
  wrong. **Only the known-good control exposed it.** And `xtralis.com`'s `/sitemap.xml` and
  `/sitemap_index.xml` both return `text/html` at 229,957&ndash;233,962 bytes, so that brand has
  no sitemap route at all. Seventh and eighth instances.
- **`mircom.com/product-documents/` is a SECOND-CLASS index, not the library, and this file has been
  recommending it as though it were complete.** Four of one lot's twelve products are absent from
  its 2,132 filenames. **There is a second, undocumented directory:
  `mircom.com/wp-content/uploads/pdf/`**, serving `CAT-5620` (FA-1000 series), `CAT-5301` (Fire Alarm
  Accessories), `LT-600` and `LT-894`, with the same 146-byte `text/html` 404. **Probe both
  `/product_documents/` and `/pdf/`.** Also measured on that host: **`?s=` IS honest** (a real term
  returns search-results, an invented one returns no-results) **and still returns a false negative
  for `FX-LOC`, a product that certainly exists** &mdash; so a zero from it is uninformative in
  either direction, and the WooCommerce Store API 403s without a browser UA. Serial at 4 s across
  ~30 fetches drew no 429.
- **A suffix rule stated in an ordering table settles a model that has no row of its own.**
  `FX-LOCB` appears in no ordering row; CAT-5985 Rev. 7 reads *&quot;FX-LOC | Local Operating Console
  enclosure&hellip; **Add suffix 'R' for red door. Add suffix 'B' for black doors.**&quot;*, and
  CAT-5669 independently spells the red model `FX-LOCR`, **which proves the concatenation form**. So
  `FX-LOC`+`B` is black, sourced. That is a different and better thing than inferring a suffix from
  a pattern across siblings: **a stated rule plus one worked example of the rule is a manufacturer
  statement about the unlisted member.**
- **The series-block trap fired on `INX-10AC` and was avoided, and it is the mirror of the recorded
  `INX-10A` defect.** CAT-5321's Features bullet reads *&quot;Unit includes power supply, charger,
  red door, black backbox, transformer and battery leads&quot;* &mdash; that describes the
  **INX-10A**, whose ordering row says *&quot;c/w backbox and red door&quot;*. This file already
  records the live `INX-10A` page carrying the `-AC`'s chassis sentence; here the same document
  would have put the `-A`'s carton onto the `-AC`. **One Features bullet, two products, wrong in
  both directions.**
- **Two more documents pasting a sibling's model name into their own opening sentence.** CAT-5335,
  the `IPS-4848DS` sheet, opens *&quot;The **IPS-2424DS** Programmable Input Switches
  Module&hellip;&quot;* while every figure in that paragraph is 48/48/48 and matches the ordering
  row &mdash; **and LT-6022 Rev 0 carries the identical sentence with the correct model name**,
  which is what settled it. CAT-5620 pastes `FX-2003-12NXTDS` into its RM-1008A and UDACT-300A
  descriptions. **When a document names the wrong model, look for the same sentence in a second
  document of the same family**; the one that differs is the typo.
- **The stale-figure mechanism again, with the losing side matching a DIFFERENT MODEL's value.**
  CAT-5620's specification block headed `MCC-1024-12ADS/MCC-1024-12XTDS` gives *&quot;Power Supply
  Ratings: **6 Amps** max&quot;* &mdash; **exactly the `MCC-1024-6ADS` value** &mdash; while the
  model number, the ordering row and the body all say 12 A and the same block gives 10 A indicating.
  Same sheet, same part: the ordering row says it *&quot;Mounts in BBX-1024**DS**(R)&quot;* where the
  body, both enclosure rows and LT-600 throughout say **BBX-1024XT(R)**, and `BBX-1024DS` is not a
  model in the document. **Checking whether the losing figure is correct somewhere else identifies
  the mechanism and settles it**, for the third time on this project.
- **The sibling trap fired on a one-letter accessory pair, and both members are in this
  catalogue.** `QAA-4CLAS` &ne; `QAA-4CLA`: `LT-872` routes the **S** version to `QAA-5230S`
  amplifiers at **5 W max per zone**, `LT-859` routes the plain one to `QAA-5415` at
  **15 W** &mdash; and `QAA-5415-25`, the plain converter's host, was in the same lot.
  Cross-selling either is a live mis-sale.
  **A mechanism cross-check came back clean and is worth copying:** `CAT-9521` lists exactly
  two QAA amplifiers as Class B only &mdash; the QAA-5415 pair and the QAA-5230S &mdash; and
  those are exactly the two with Class A converters, while the non-`S` QAA-5230 and QAA-5160
  do Class A natively and have none. **A converter exists only where the amplifier cannot do
  it natively**, which predicts the accessory list from the amplifier table.
  This also narrows a note recorded last batch: *&quot;`4CLA` appears zero times in both QAA
  datasheets, an accessory is usually not a document&quot;* &mdash; on this brand **both
  converters have their own document**, filed under `LT-` instructions rather than in the
  `CAT-` amplifier sheets. The accessory is not in the *catalogue sheet*; it is not
  undocumented.
- **A ninth non-discriminating search endpoint, and again only the KNOWN-GOOD control exposed
  it.** `mircom.com/?s=` returned 166,818 bytes for a bogus term, **166,770 for
  `OGN-MONITOR-UL`, a part proven present in the manufacturer's own catalogue sheet**, and
  166,786 for `OGN-MONITOR-STD` &mdash; three different MD5s, no result rows in any, only
  echoed occurrences. A bogus-only control reads *&quot;different bytes, endpoint works, part
  absent&quot;* and is wrong. Excluded as evidence entirely. Also measured: the WooCommerce
  Store API is honest but useless here, because **OpenGN is a single product record** (`sku:
  OpenGN`) so no `OGN-*` SKU is a separate WooCommerce product; and the live OpenGN product
  page contains **zero `OGN-` tokens**. Two filenames of `CAT-5323` differing by a `-1` suffix
  are **byte-identical, one document, not two revisions.**

- **The merged-cell trap on `E85010-0069` p2, where word coordinates give a confident wrong
  answer.** The Agency Listings cell `UL, ULC, FM, CE, LPCB EN54*` sits at x=235&ndash;345;
  against column centres at 157 / 271 / 386 / 488 that reads cleanly as the second column's
  value. A 260 dpi render shows it **merged across three columns**, and that `UL, ULC, FM`
  belongs to **`3-LCDXL1` alone** &mdash; so that display carries no CE or LPCB EN54 listing,
  which decides whether it may go in a `3-4ANN-E`. Third instance of coordinates being not
  merely insufficient but actively misleading.
  Also on that sheet: **`3-4ANN` and `3-4ANN-E` have genuinely BLANK ship-weight cells**
  (coordinate- and render-confirmed, where 3-6ANN reads 6.28 lb), so no weight was published;
  and **catalogue number `3-CPUDR` is listed twice with two descriptions and two weights.**
- **A SECOND HOST THAT RE-ENCODES ON SERVE, so `md5` and `bytes` are a measurement and not an
  identity.** `apcfire.com` served one file at 21,056 bytes on a first fetch and stably at
  18,877 on three later ones, **same photograph, dHash Hamming 0, 158&times;600 both times**.
  After mircom.com that is two, so it is a property of image-optimising CMSes rather than a
  quirk. **Record the stable value with a note, and let the perceptual hash carry identity.**
- **The perceptual hash caught a pair MD5 could not, across two different product classes.**
  `HBT-Fire-W-H355R-W-H355-CEILING-HiRes` and `HBT-Fire-W-SD355-CEILING-HiRes` are **dHash
  Hamming 0 with different MD5s** &mdash; one photograph re-encoded, published for a SWIFT
  **heat** detector and a SWIFT **smoke** detector. And `HBT-Fire-W-GATE-W-DIS-D-CEILING-HiRes`
  is the thumbnail for **both** the gateway record and the display-driver record, where the
  visible object is the round gateway housing and Honeywell publishes a separate asset for the
  equivalent driver assembly. **Two more reasons a `sku_list` hit is not an attribution.**
- **The shared-asset trap on a second TX3 pair, which makes it a house pattern rather than a
  coincidence.** `TX3-CSR-6.2`/`6.4` and `TX3-PCR-620`/`640` are served **the same two image
  files across two different product pages** &mdash; exactly the recorded `TX3-CSR-35` /
  `TX3-PCR-35` case, where a 13.56 MHz smartcard reader and a 125 kHz proximity reader are
  visually identical. **Where two product classes are physically indistinguishable, one
  photograph will be published for both and no image check can separate them.** That is a
  reason to reject, not to choose.

- **A `null` with THREE incompatible readings, and naming them is what makes it useful.**
  `PS-632 F1` ($27.35) was left untouched. It is in no first-party route &mdash; the honest REST
  endpoint returns `[]`, and **the 329-product sitemap, a literal enumeration rather than a
  search, carries the entire 6 V range and no 632.** The three readings: the digits imply
  **3.2 Ah**, which exists in this family but as **`PS-630ST`**; the store's ERP reads
  `PS-632 6V3.5AH F1`, **byte-identical to PS-630's string except the model number** &mdash; the
  borrowed-sibling-row signature, and note it does not say 3.2 either; and **the price sits with
  the 12&ndash;13 Ah class at 3x PS-630's.** Not called invented, SKU untouched, and the agent
  explicitly declined to read across to `PS-630`. **One carton label or one price-list line
  settles which of the three it is; more searching will not.**

- **A break-rod documented in a FIREFIGHTER TELEPHONE CABINET sheet, found by text rather than
  by index metadata.** `2099-9804` is in six served PDFs, one of them `2084-0001` Rev. 11,
  **2084 Series telephone cabinets**, which lists it under a *Firefighter Phones Accessories*
  heading &mdash; and the JCI index `prodname` literally reads &quot;2099-9804 Firefighter Phone
  Break Rod&quot;. The live page named only pull stations, so it **understated the scope**, and
  the missing family is not a pull station at all.
  The recorded line-specific accessory rule held exactly: `S2099-0009` Rev 7 (cast metal)
  contains `2099-9804` **zero** times, `2099-9803` zero times and &quot;breakglass&quot; zero
  times, carrying `2099-9829` instead. **And the rod is supplied with the station and optional**
  &mdash; the opposite of the incomplete-product shape, which is worth saying because every
  other accessory finding in this file runs the other way. The live *&quot;3.5-inch long&quot;*
  is unsourced and was removed; five sheets call the rod **plastic** while `2084-0001` calls its
  door option a **glass** break-rod, so no material was published.

- **A GREP WITH A LITERAL SPACE GIVES A SILENT FALSE NEGATIVE ON EXTRACTED PDF TEXT, AND AN
  AGENT WAS ONE STEP FROM RECORDING A FALSE CORRECTION TO THIS FILE BECAUSE OF IT.** A lot-22
  agent first reported that this file's `FR` citation *&quot;did not reproduce&quot;*:
  `[Ff]lame [Rr]etardant` returned **zero** hits in `SLA_Technical_Manual.pdf`. **Extraction had
  put a newline inside the phrase.** Re-run with whitespace normalised, the manual says it
  verbatim &mdash; *&quot;Flame Retardant (FR) battery cases and lids are available where the end
  application dictates.&quot;* The agent caught its own error, re-ran every other critical grep
  normalised, and reported the near-miss rather than dropping it.
  **This is a new failure mode for the bounded-negative rule, and it is the most dangerous kind
  this project has**, because a zero-hit grep is exactly the evidence used here to disprove
  supersession claims, to bound a suffix as undecoded and to prove a document does not mention a
  part. Every one of those is a *negative measured by counting occurrences of a phrase*. **So:
  normalise whitespace (`re.sub(r'\s+', ' ', text)`) before grepping any extracted PDF text**,
  and treat a phrase-level zero found without it as unmeasured rather than as a result.
- **The model number is a capacity on only 4 of 12 again, and the SAME TOKEN means different
  things on two members of one series.** `PSH-655` &rarr; 5.5 Ah at 20 hr, so the `55` is the
  capacity; **`PSH-1255` &rarr; 6.0 Ah at 20 hr and 5.67 at 10 hr, so the same `55` is neither
  rate.** `PS-682` (8.48/8.03) and `PSH-1280` (8.5/7.92) likewise match neither. Every figure
  arithmetic-checked against its own stated discharge current, 12 of 12.
  **And the powersport family settles the shape outright: the 20-hour row is LITERALLY BLANK on
  all three `PT*` sheets**, along with Internal Resistance and Max Short Circuit Current &mdash;
  identically, so a template defect rather than extraction error. `PT7B-4` is 6.5 Ah at 10 hr,
  `PT9B-4` 8.0 and `PT14B-4` 12.0, with the sibling `PT12B-4` at 10 Ah confirming across four
  members that **the number is a JIS case size, not a capacity at any rate** &mdash; the
  `AS-75-R-WP` shape on a whole family.
  **`PT7B-4` and `PT9B-4` both read 115 CCA**, verified genuine by word coordinates rather than
  assumed to be a column shift (CCA at x&asymp;183, CA at x&asymp;210, each row on one y-line,
  dimensions matching each sheet). **So CCA alone cannot distinguish two SKUs this store
  carries**, which is why both titles carry Ah *and* CCA.
- **A chemistry claim declined on one lithium model and published on its sibling, from the same
  series.** `PSL-SC-12200` states `(LiFePO4)` in its own model heading; **`PSL-BT-122000` states
  it zero times, even with whitespace normalised.** The product page's Group Information block
  does say it, but that is a **series-level** block. Class noun taken from each model's own
  heading &mdash; &quot;Series Capable Rechargeable Lithium (LiFePO4)&quot; against &quot;Lithium
  Bluetooth&quot; &mdash; and no chemistry asserted on the second. Sixth declined cross-series
  import. (The charge voltage of 3.60&ndash;3.65 VPC across four cells at 12.8 V is the LiFePO4
  signature, and that is an inference, so it stayed out.)
  Same discipline on the class word: **`AGM` appears zero times in all six SLA and PSH
  datasheets** and three times in the `PT` sheets' own text, so it is in the powersport titles
  and in none of the others.
- **`NB1` decoded, extending the recorded series:** *&quot;TERMINAL POSTS with nut &amp; bolt
  connectors&quot;* on a **12 mm** plate, against NB2's 14 mm and NB3's 16 mm &mdash; read off a
  400 dpi render, as that panel has no text layer.
- **A token-order mismatch between the store and the manufacturer, resolved by keeping the
  store's form.** The ordering authority and the product-page SKU table both write
  `<model> FR <terminal>` (`PSH-1255 FR F2`) where the store writes `F2 FR`. **The configuration
  exists in every case; only the order differs.** The store's spelling was kept so the title
  matches its own SKU, with the meaning written out in words so either spelling reads correctly
  &mdash; and the mismatch went to the owner. Also recorded: **`PSH-1280` and `PSH-655` have no
  plain non-FR configuration at all**, while `PSH-1255` lists both.

- **A series-wide FEATURES bullet that is FALSE for a member, contradicted by three
  model-attributed signals on the same sheet.** `S4098-0059 Rev. 2` heads a page-1 block
  &quot;Heat detection:&quot; and says the detectors *&quot;Include both rate-of-rise and fixed
  temperature thermistor-based detection.&quot;* For `4098-5611` that is wrong three times
  over: Table 1 gives **&quot;Rate-of-rise temperature alarm: n/a&quot;**, Table 2 reads
  *&quot;4098-5611: Heat detector at a 135 &deg;F or 57.2 &deg;C fixed temperature&quot;*, and
  Table 3's Type column reads **Fixed temperature**. Column assignment confirmed by word
  coordinates on four clean x-positions and by a 300 dpi render.
  **This is stronger than the recorded `SD365T-IV` case and worth distinguishing.** There the
  family block named a property the member could not be shown to have; here the family block
  **asserts a function the member's own rows deny**. A family bullet is not merely unattributed
  &mdash; it can be flatly false for a member, so the question is never &quot;does this apply&quot;
  but &quot;what does this model's own row say&quot;.
  The same sheet contradicts itself on ambient range a second way: Table 1's heat columns give
  **32 to 122 &deg;F** while the prose paragraph, under a heat heading, gives **32 to 100
  &deg;F** with a 6 &deg;F/min fluctuation limit that is a *smoke*-detector guideline. The
  model-attributed table value was published.

- **Colour convention disproved by COLUMN POSITION rather than by absence, which is a cheaper
  and stronger proof.** For `SS-PHOTO-CO`, word coordinates put the ordering-table heads at
  White x=57.0, Ivory x=121.6, Black x=178.2; that row carries its part number at **x=57.0 with
  em-dashes at 121.6 and 178.2**, while every base row below it carries three numbers. So no
  ivory or black detector exists and colour is a `CK300-CO` kit &mdash; **a filled cell proves
  more than a missing string**, because an absence could always be an extraction failure.
- **A tenth non-discriminating search endpoint, and this one defeats an MD5 control outright.**
  `rfsworld.com/search?q=` returns the **home page at a constant 325,895 bytes with three different
  MD5s** for a real term, a bogus term and a known-good part &mdash; a nonce varies the hash while
  the content is identical, so an MD5-only control passes it and **the byte count is the tell**.
  Two more on the same brand family: `vikinggroupinc.com/?s=` (220,445 against 220,448 B) and
  `/search?keys=` (~138,199 B for everything). Against those, **`vikinggroupinc.com/products?text=`
  does discriminate** (no-results 158,867&ndash;158,881 B against 163,734&ndash;163,822 B) and is
  the one to use. Also measured: **`sdifire.com` now carries only seven products and its
  WooCommerce Store API returns `[]` for everything including a known-good term**, so it is useless
  as an existence test while its legacy PDFs still serve from `/wp-content/uploads/2018/08/` with
  an honest 146-byte 404.
- **A typo in a standard number left unrepaired, which is the `Ten-Xone` rule on a listing.**
  The Bedrock BTB65 flyer prints **&quot;IEC-61268&quot;**, almost certainly meant for IEC 60268-16,
  the speech-intelligibility standard. **No standard number went into the title.** Repairing an
  obvious typo is still writing a new claim, and a standards citation is the most expensive kind
  to get wrong.

- **A recorded blocked endpoint fired exactly as documented, one query after being cited.** This
  file records `safefiredetection.com`'s `?s=` search as returning near-identical bytes with the
  query echoed and **zero product rows**. Probing it for `RP2226` returned 144,047 bytes against
  a bogus control's 144,080 and **five occurrences of the term, every one an echo** (page title,
  `og:url`, the webpage JSON-LD url) &mdash; and counting actual product links gives **0 for both
  the real and the bogus query**. Read as a hit it would have &quot;confirmed&quot; SAFE
  catalogues the part; read correctly it is no evidence in either direction. **The recorded
  warning is what stopped it**, and the check that settled it was counting product rows rather
  than occurrences of the string.

