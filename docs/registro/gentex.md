<!-- Registro de casos do projeto TFAS. Movido VERBATIM de CLAUDE.md em 23 Sep 2026; nada foi reescrito. Nao e carregado automaticamente: leia sob demanda. E cronologico: entradas posteriores corrigem anteriores; em caso de conflito vale a mais recente e o nucleo em CLAUDE.md. -->

# gentex

- **Gentex's documented path does not cover the PLACE line.**
  `fireprotection.gentex.com/files/PLACE-Series1.pdf` and `PL1K-Series1.pdf` both
  404. PLACE lives on `placehomesolutions.com`, which is Gentex-operated (Zeeland MI
  footer, Gentex `551-` document numbering) and therefore first-party.
- [CORRIGIDO — caminho construído falha por família; use `fireprotection.gentex.com/resources`; ver neste arquivo] **Gentex serves datasheets directly** from `fireprotection.gentex.com/files/<Model>-Series<n>.pdf`,
  with no bot protection. Beware though: one Gentex revision has a **blank Part Number
  column** while another populates it, so confirm the catalogue number on the revision
  you actually have.
- **A "Replaces X" claim belongs in a title only when a manufacturer document states
  it.** Three claims in one batch gave three different answers: `PC2WL`&rarr;`PC2WLED`
  is stated outright in a Honeywell bulletin and stays in the title; `SPSCRLED` vs
  `SPSCRL` is unstated but strongly supported by omission across two datasheet
  revisions; `GN-503`&rarr;`SC` is a sound *distributor* equivalence that Gentex
  never makes. When it is not manufacturer-stated, **move it to the body** &mdash;
  the part number still earns the query match, without a feed attribute asserting
  something unsourced. Titles feed Merchant Center, so an unverified claim there
  costs money in two channels.
- **Three independent structural reasons can settle a self-contradicting datasheet, and
  that is stronger than preferring the table by rule.** Gentex's S-Series sheet lists
  `SHRR` among the models that *&quot;feature electrochemical CO sensing&quot;* in its
  Standard Features prose, while the ordering table gives the SHRR row **no CO bullet**
  (word coordinates: bullets at Smoke x=222.7 and Heat x=314.9, nothing at CO x=268.8).
  Three things side with the table, and none of them is &quot;tables beat prose&quot;:
  SHRR is a **917-** S-Series number where every CO model is **918-**; the Product
  Listings give the S Series **ANSI/UL 217 only**, UL 2034 being reserved for SC/C; and
  the SHRR harness diagram is labelled **HEAT ALARM CONTACTS** where STRR/SCRR says
  &quot;CO or HEAT&quot;. No CO claim was published either way. **When a document
  contradicts itself, look for a third and fourth signal rather than applying the
  table-over-prose rule mechanically** &mdash; the rule tells you which to bet on, the
  corroboration tells you whether to publish at all.
- **Ninth product-class error, and the first where the store contradicts itself.**
  Gentex `STRR` was titled &quot;Multi-Criteria Smoke **Detector**&quot; and typed
  &quot;Multi Criteria Detectors&quot;, so the type agreed and raised nothing. Gentex's
  own document calls the whole family a **&quot;Smoke Alarm&quot;** and lists it under
  **ANSI/UL 217 9th Edition**: a self-contained 120 VAC dwelling-unit alarm with its own
  horn and a 9V battery, which is a materially different purchase from a UL 268 system
  detector on an SLC. **The store's own sibling page for the SR was already titled
  &quot;Smoke Alarm&quot;**, so the catalogue disagreed with itself and nobody noticed.
  When two pages in one family use different class nouns, one of them is wrong.
- **A wrong dBA figure in a live title, verified by the coordinator, and the document
  never contained the wrong number at all.** `GB6-24` was titled *&quot;85 Dba at 10
  Feet&quot;*. Gentex `551-0042-04`, fetched and read directly: the model table row reads
  `GB6-24 | 904-1278-002 | 24 VDC | 6&quot; | 100 mA | **95 dBA**`, and the A&amp;E
  paragraph independently specifies *&quot;peak sound output of **95 dBA** or
  greater&quot;*. **`85 dBA` occurs zero times in the document.** Not a
  prose-against-table conflict and not an extraction artefact &mdash; the figure was
  simply never there, which is the cheapest kind of defect to confirm and the easiest to
  miss, because 85 dBA is the plausible number a reader expects on a notification
  appliance.
  Two things came with it. **Gentex path construction worked first try here**
  (`fireprotection.gentex.com/files/GB-Series1.pdf`, 538 KB, mime-clean) where it failed
  for the S-Series &mdash; so that route is family-by-family, not broken. And **Gentex
  states a carton quantity for a notification appliance** &mdash; *&quot;20 units per
  carton&quot;* on the datasheet face &mdash; which is the category Honeywell declines to
  state. Third vendor outside Honeywell doing so.
- **Coloured lens is a listing class on a THIRD brand, and it is not just amber.** Gentex
  lists the GE3 Colored Lens Series to **ANSI/UL 1638 and ANSI/UL 464, CAN/ULC S525/S526,
  and explicitly NOT UL 1971**, with the note that *&quot;ANSI/UL 1971 is not applicable to
  emergency communications devices, but readings were obtained using the measurement
  procedure specified under ANSI/UL 1971.&quot;* So the candela are rated output with no
  derating, but **the appliance is an emergency-communications device, not a fire
  strobe** &mdash; Gentex names severe weather and emergency response as the applications.
  After Eaton (amber forbidden as a public-mode fire appliance) and System Sensor (amber
  ALERT is private mode, UL 1638), that is **three brands and the finding now extends
  from amber to blue, green and red**. Treat any non-clear lens as a listing question.
- **The Siemens coexistence sentence has a Gentex twin, and ONE sentence plausibly
  generated TWO of this catalogue's recorded defects.** All three occurrences of `S1209` in
  Gentex's current sheet are a single tandem-interconnect instruction: *&quot;use
  brown/yellow wire to tandem interconnect this device to S, SR &hellip; **as well as the
  Gentex GN-503 Series, CO1209 Series and S1209 Series**&quot;*. That is devices sharing an
  interconnect wire, exactly the Siemens *&quot;may be installed on the same SLC&quot;*
  failure on a different brand. `replac`, `supersed` and `discontinu` each appear **zero
  times** in the document.
  **`GN-503` is in that same sentence** &mdash; and this file separately records the
  `GN-503`&rarr;`SC` &quot;equivalence&quot; as distributor wording Gentex never makes. So
  **check any Gentex &quot;replaces&quot; claim against that one sentence before spending a
  search.** Separately confirmed and worth keeping apart from the claim: Gentex's own page
  marks the S1209 Series **DISCONTINUED but names no successor** &mdash; a lifecycle fact
  that does not license a supersession claim, and it went to the owner's file rather than
  the copy.
- **&quot;Nursery&quot; is a FEATURE SET, and the ordering table says so where the prose
  does not.** `PL1N` was a nameless `Brand PartNumber` title. Gentex's model matrix in
  first-party `551-0085-AAA`, read by word coordinates and confirmed at 300 dpi, gives
  PL1N **Smoke and CO and neither Heat nor Natural Gas**, and makes it **the only one of
  the four PLACE models** carrying air quality monitoring, video with intercom and a white
  noise generator. So the qualifier names capabilities, not a tone, a lens or a listing.
  **Class noun defended rather than assumed:** it is a self-contained 120 VAC dwelling-unit
  alarm to **ANSI/UL 217 9th Edition and ANSI/UL 2034 4th Edition**, so &quot;Alarm&quot;
  is right and &quot;Detector&quot; would be the `STRR` error again.
  **A coordinator premise wrong in the cheapest possible way:** the briefing said the live
  title looked truncated. It is complete in `a2_in.json` &mdash; **the ellipsis was in the
  briefing's own prose**, where the coordinator had trimmed it to fit. That is the
  `PAD100-6DB` snapshot error with the snapshot replaced by the briefing itself.
  Gentex also states **12 units per carton**, a fourth vendor outside Honeywell doing so.
  Not added to the title; flagged.
- **A WRONG CATALOGUE NUMBER in a feed title, and the innocent origin was visible on the
  same page.** `GB10-120`'s title carried **`(901-1281-002)`**. Gentex `551-0042-04`,
  fetched and read directly by the coordinator: **`904-1281-002` appears once and
  `901-1281-002` appears zero times.** The origin is right there &mdash; **`901-0242-000`
  is the GBBB back box**, so `901-` is a real Gentex prefix and the digit swap produces a
  string that looks entirely plausible. A catalogue number that does not match itself is
  the `868STRC-AQ` and `ZR-MC-R` shape for the third time, and it costs both channels.
  Corrected. Its sibling `GB10-24` separately **duplicated the model token** &mdash;
  *&quot;Gentex GB10-24 GB10-24 (904-1279-002)&hellip;&quot;* &mdash; with a correct part
  number; that is the 75-product brand-plus-SKU-repeated family found by scan this
  session. Both also carried a literal `&quot;` inch mark. All fixed.
  **And the check that mattered was doing it per model rather than per family.**
  `GB6-24` is on record here for a live title claiming **85 dBA** where the document says
  **95**. The briefing told the agent to check `GB6-120`'s dBA **against the document
  rather than against the sibling's corrected value** &mdash; and `GB6-120` asserts no
  dBA at all, so there was nothing to correct. A corrected sibling is not evidence about
  its neighbour.
- **Two document defects worth the file.** `DN-6821` misprints a metric conversion as
  *&quot;5.500 in. (**13.970 mm**)&quot;* &mdash; 5.5 in. is 139.70 mm &mdash; while
  14.375 in. and 2.750 in. on the same line convert correctly, **and it reproduces in both
  the FSD-751P and FSD-751RP blocks**, which rules out extraction error. Inches only
  published. And **Siemens DS 2580 contradicts itself on dBA while omitting the part
  entirely**: prose gives wall-mount SE up to 89 dBA and ceiling 87, the table gives
  77/79.5/82.5/85/88 for `SE`, `SEC`, `SE-MC-C` and `SE-HMC` &mdash; and **`SE-MC`, the wall
  multi-candela series, is not in that table at all.** No dBA figure published, and the
  temperature and humidity note was omitted too because it sits under the same table that
  excludes the part.- **A candela pair in a title that is TWO LISTINGS, not two settings &mdash; the
  `49AV-WWFO-BA` shape for the second time, and this one under-specifies a fire layout by
  five times.** `GEC24-1575WR` was titled *&quot;Fixed 15/75 Candela Strobe&quot;*, which
  reads as a ladder or a selectable range. Gentex `551-0049-03`, **fetched and read directly
  by the coordinator**, prints the cell as ***&quot;15 (ANSI/UL 1971) / 75 (ANSI/UL
  1638)&quot;*** &mdash; four times on the sheet. **UL 1971 is the public-mode fire rating
  and UL 1638 is general signaling**, so a designer taking 75 cd as the fire figure
  specifies a fifth of the devices actually needed. The appliance is fixed output; neither
  number is a switch position.
  Two more things verified in the same fetch. **The catalogue number checks out character by
  character** &mdash; `904-1127-002`, unlike last batch's `GB10-120` where the store carried
  `901-` against Gentex's `904-`. And **the model is printed `GEC24-15/75WR`, with a slash
  the store's SKU has lost** &mdash; the punctuation-stripping import for the **sixth**
  time, after the 185 frequency ranges, `ZR-MC-R`, `QAA-5415-70/25`, `FDX-008WKI` and
  `ELSTW-N`. SKU untouched; the manufacturer's form is in the body so either search matches.
  Also on the face of that sheet: **&quot;24 units per carton&quot;**, so Gentex is the
  fourth non-Honeywell vendor on record stating carton quantities.
- **A TWO-DOCUMENT TRANSPOSITION, LOCALISED BY A NEIGHBOURING COLUMN THAT AGREES.** Gentex
  data sheet `551-0032-04` gives the `GX93` 12 VDC as 81/86 dBA and 24 VDC as 78/83 &mdash; the
  12 V unit louder, which is already odd. Installation manual `550-0176-KAE` gives the **exact
  opposite**: 24 VDC 81/86, 12 VDC 78/83. Both rendered at 300 dpi, both read as extracted.
  **What makes this diagnosable rather than a coin flip is that the CURRENT columns of the two
  documents agree exactly** (24 V: 18 / 21.1 mA; 12 V: 13 / 7 mA). That pins the transposition
  to the decibel columns alone and **rules out a whole-table swap or a row shift.** No dBA was
  attached to any voltage; only the model table's range, 78&ndash;86 reverberant and 90
  anechoic, was published. A third figure exists in the manual's prose (&quot;75-85dBA&quot;).
  **Generalises: when two documents disagree on one column, check whether an ADJACENT column
  agrees. If it does, the defect is local and you know exactly what not to publish; if it does
  not, you are looking at two different products or two generations.**
- **A family LISTINGS bullet that would have published an audible listing on a device with no
  horn, and two model-attributed signals separate the pair.** Gentex `551-0050-07`'s Product
  Listings gives **ANSI/UL 464 and 1971 to &quot;the GE3 Series appliances&quot;** &mdash; a
  family containing both `GEC3-24WW`, a horn strobe, and `GES3-24WW`, strobe only. What
  separates them: the manual attributes UL 1971 to *&quot;the GEC24, GES24, GEC3-24, **GES3-24**
  strobe&quot;* and UL 464 to *&quot;your **horn and horn/strobe**&quot;*; and **the CSFM
  listing prefixes differ &mdash; 7125-0569:123 for the GES3-24 against 7135-0569:122 for the
  GEC3-24**. A listing *number* is a per-class identifier and is therefore better evidence than
  a family bullet. Both catalogue numbers checked character by character after the `GB10-120`
  901-/904- swap and **both are correct**.
  `GEC3-24WW`'s live title **had no class noun at all** &mdash; `Gentex GEC3-24WW (904-1315-002)
  Wall Mount` &mdash; the `ZH-MC-W` shape, in the Shopify title field, so it cost the feed too.
  Document defects on that sheet, nothing published from either: the 15 cd / 12 VDC cell gives
  **106 mA nominal against a UL maximum of 92**, a maximum below its own nominal and unique to
  that cell; and the ordering table gives all four GEC3 models a single **62&ndash;82 dBA**
  range matching neither the 24 V column (66&ndash;82) nor the 12 V (60&ndash;79). The
  **100 dBA** headline is anechoic.
- **A SUPERSESSION CAN LIVE IN A SALES ANNOUNCEMENT RATHER THAN IN EITHER PRODUCT'S DATA
  SHEET, AND A DATA-SHEET-ONLY SEARCH RETURNS A FALSE NEGATIVE. This corrects a recorded
  finding.** This file records the Gentex `S1209` *&quot;Replaced by S&quot;* claim as unsourced,
  on the grounds that `replac`, `supersed` and `discontinu` connect the two in none of the data
  sheets &mdash; and that measurement was right. **The document exists and is not a data sheet.**
  `fireprotection.gentex.com/files/Product_Announcement-3-19-24.pdf`, fetched and read directly
  by the coordinator (126,853 bytes, `application/pdf`, 1 page), is a letter from Gentex's Sales
  Director dated 19 March 2024 saying verbatim: *&quot;These new alarms will replace our current
  offering of the S1209 Series, CO1209 Series and GN-503 Series. We will continue to manufacture
  the legacy alarms through June 30, 2024, pending component availability.&quot;*
  **So the claim went INTO a feed title**, which is rare here: `Gentex CR &hellip; Replaces CO1209
  Series`. **And it stayed at series level, because that is all the letter says.** The letter
  announces *&quot;Attached is a cross reference chart&quot;* and **the chart is not in the PDF**,
  so the part-for-part mapping every reseller asserts &mdash; and that four store pages assert
  &mdash; has no source. The agent narrowed to the series claim on its own and was right to.
  **The ask that follows is worth more than the page: one Gentex cross-reference chart settles
  `CO1209`, `CO1209F`, `S1209` and the C Series pages at once.** It is an attachment to a sales
  e-mail, so no amount of searching produces it &mdash; the rep does. Flagged, with the
  end-of-manufacture date (30 Jun 2024) as a separate lifecycle question, since the store still
  sells both legacy SKUs as current.
  **The generalisable half: a supersession lives wherever the manufacturer chose to announce it.**
  This file already records the Honeywell product-announcement bulletins as the supersession
  source for that brand, and the System Sensor `OSI-R-SS` letter as a manufacturer-authored
  REPLACES table with no document number. This is the third shape &mdash; a dated sales letter on
  letterhead &mdash; and it means **&quot;absent from both data sheets&quot; bounds the data
  sheets, not the catalogue.**

- **Commander 5 (GS/GHS/GWS) names no UL 1971 listing, where Commander 2/3/4 do (v2b51).** Data sheet `CDOC-300501 Rev 001` (3/2/2026) and manual `550-0788` list the GS strobes to ANSI/UL 1638; the string `1971` occurs zero times in both, whitespace-normalised. Published as a bounded fact with an AHJ caveat, not as &quot;not UL 1971&quot;. **`GSR` means red FACEPLATE in the data sheet (904-0627-002) and red LENS in the manual** &mdash; one code, two meanings inside one product line. Store `GSPR` (904-1455-002) is titled &quot;Speaker Only&quot; and is a plain red GS strobe per the data sheet; queued in `pending_fixes.md`.
- **The Gentex `C` title now carries the series-level supersession only** (&quot;Replaces CO1209 Series&quot;), matching `CR`; the ordering-row CO bullet (word x=268.8, render-confirmed) shows no relay on `C`. The store's `CO1209`/`CO1209F` titles still assert one-for-one mappings no retrievable Gentex document makes; queued.
