<!-- Registro de casos do projeto TFAS. Movido VERBATIM de CLAUDE.md em 23 Sep 2026; nada foi reescrito. Nao e carregado automaticamente: leia sob demanda. E cronologico: entradas posteriores corrigem anteriores; em caso de conflito vale a mais recente e o nucleo em CLAUDE.md. -->

# xtralis-vesda

- **Two structured fields wrong the same way corroborate each other.** `OSE-HPW` has
  vendor `Vesda` and type `Aspirating Smoke Detectors`. VESDA is Xtralis's aspirating
  line; **OSID (Open-area Smoke Imaging Detection) is a separate Xtralis line**, and
  every manufacturer document says &quot;OSID by Xtralis&quot;. An OSID emitter is
  open-area optical imaging, not aspiration. The agent found the brand error from the
  documents and the restored type field confirmed it from a second direction. Honeywell
  owns both lines, which is presumably how they merged. **Decide vendor and type
  together when they are wrong together.**
- **The pack-count boundary is a fact about HONEYWELL, not about manufacturers, and
  Xtralis proves it by stating carton quantities routinely.** `PIP-018`'s title asserts
  **PK10**, and unlike every Honeywell `-BP` case that claim is **manufacturer-stated**:
  Xtralis's own *VESDA Pipes and Fittings &mdash; Europe* catalogue (`xtralis.com/file/495`,
  p. 11) lists **&quot;PIP-018 &mdash; 25mm Air Sampling Test Point, Pack of 10, Red&quot;**,
  and `PIP-007`, `PIP-004`, `144-013`, `222-059` and many others carry &quot;Pack of
  10&quot; in the same catalogue. **This is the first documented pack count in the project
  outside Honeywell bases, LF sounders and batteries.**
  The correction that matters is to how the rule was phrased. This file worked toward
  &quot;bases, low-frequency sounders and batteries, and nothing else&quot; as though it
  were a fact about how *manufacturers* document. It is a fact about **Honeywell**. A
  different vendor states carton quantities as a matter of course, so **the convention
  question has to be asked per brand**, and a Honeywell-derived negative says nothing
  about Xtralis, STI, Potter or anyone else. That is the same over-reach as the battery
  correction &mdash; evidence covering two categories, conclusion covering all of them
  &mdash; one level further out, at the vendor boundary instead of the category boundary.
  Two more results on that part, both from deliberately checking rather than assuming:
  it is **VESDA, not OSID** (it sits in Xtralis's own VESDA pipe range, so the vendor
  field is right and this is not the `OSE-HPW` case), and although it appears **inside an
  End-of-Life bulletin** it is there as the **surviving alternative** to a discontinued
  PVC adapter, not as a discontinued product. A part named in an EOL bulletin is not
  thereby end-of-life &mdash; read which side of the table it is on.
  **The title's PK10 was left exactly as it was** and went to the owner's file anyway,
  because a pack count in a title is a feed attribute and the decision is the owner's
  even when the documentation supports it. Route recorded: `xtralis.com/file/<id>` serves
  PDFs directly with no bot protection, and **the metric 25 mm range is in the Europe
  edition only** &mdash; the Americas sheet (`file/623`) does not list `PIP-018` at all,
  which is worth knowing before writing off any other `PIP-*` part as undocumented.
- **&quot;Check the other regional edition&quot; runs in both directions.** Last batch
  `PIP-018` was documented in the Xtralis **Europe** catalogue and absent from the
  Americas sheet; this batch `E700-SP-DCL-PNT` is in the **Americas** sheet
  (`xtralis.com/file/623`, Doc. 17748_12, June 2024) and absent from Europe. Neither
  edition is the superset, so a miss in one is not a negative until the other is checked.
  And a second **positive** pack count from that source: *&quot;50 per roll&quot;* is
  manufacturer-stated verbatim for `E700-SP-DCL-PNT` &mdash; it is **not** currently in
  the title, so unlike the Honeywell cases this is a claim the owner could now add rather
  than one resting on convention. The colour &quot;White&quot; in the live body has no
  basis: the only stated label colours are red and grey, and the &quot;ABS white
  colour&quot; phrase in the EOL notice attaches to the sampling point, not the label.
- **Gentex is a third manufacturer that states carton quantities, which further confines
  the pack-count rule to Honeywell.** The S/C/SC/H series sheet prints **&quot;24 units
  per carton, 28 pounds per carton&quot;**. With Xtralis already established as stating
  them routinely, that is two vendors outside Honeywell documenting what Honeywell
  documents only for bases, LF sounders and batteries. **The open pack-count rows in
  `PACKCOUNT_decisao.csv` are a question about Honeywell's documentation habits and must
  not be generalised to any other brand** &mdash; and for a non-Honeywell part, the
  carton quantity is probably findable rather than unsourceable.
- **A pack count that IS manufacturer-stated, in two independent places, and it further
  confines the Honeywell rule.** `VP-ELB-90`'s live title claims *&quot;Box with 20
  Units&quot;*. Xtralis `Doc. 17748_12` (Part No. 29813, June 2024) ordering block reads
  **`VP-ELB-90 | 90&deg; Elbow - 3/4&quot;, 20 per box`**, and independently the product
  bulletin's discontinued-alternative table gives `P-ELB-90 &quot;QTY 20&quot;` &rarr;
  `VP-ELB-90 &quot;20 PER PK&quot;` &mdash; which is also a **manufacturer-stated
  supersession**, rare enough to note. Second documented pack count outside Honeywell
  after `PIP-018`.
  **But the same block shows why a sourced count cannot be generalised:** within this one
  range the 45&deg; elbow and union are **10**, the coupling and tee **15**, the end cap
  **25**. A pack count is a per-SKU fact even inside one family from one vendor.
  The regional rule fired both ways a third time: `VP-ELB-90` is **Americas-only**, and
  the Europe edition has no `VP-*` parts at all &mdash; its 90&deg; elbow is the 25 mm ABS
  `PIP-017` at ten per pack.
- **Nineteenth product-class error, and it is the most expensive single word yet: the
  title named the one feature that DISTINGUISHES the model it is not.** `VES-A00-P-UL`
  ($8,595) was titled *&quot;Scanner LED Display&quot;*. Xtralis's Ordering Information
  (Doc. **36105_05**, Nov 2024, `xtralis.com/file/12016`), **fetched and read directly by
  the coordinator because this changed a live title**, reads:
  `VES-A00-P-UL | VESDA-E VES **with LEDs**, Plastic Enclosure - UL` against
  `VES-A10-P-UL | VESDA-E VES **with 3.5&quot; Display**, Plastic Enclosure - UL`.
  **The display is exactly what separates the two models**, so a buyer who wanted a screen
  was pointed at the one without it, $336 cheaper. Corroborated twice more on the same
  page: the spare-parts rows give `VSP-968` &quot;Front Cover - Plastic - **LEDs**&quot;
  against `VSP-969-04-S` &quot;Front Cover - Plastic - **LCD - 3.5&quot; Display**&quot;.
  **Three things make this worth keeping beyond the one page.** (a) The datasheet's prose
  *does* say &quot;intuitive touch screen display&quot; &mdash; it covers both models, so
  this is the series-wide-block trap and the model-attributed table wins. (b) **The `type`
  field was CORRECT and disagreed with the title** (&quot;Aspirating Smoke Detectors&quot;
  against a title with no class noun at all), the type-as-signal rule firing as documented
  rather than staying silent. (c) **The description body was already verbatim-correct
  Xtralis wording** and only the Shopify title was wrong, so this cost the Merchant Center
  channel specifically &mdash; say which field before sizing it.
  **The innocent origin is findable and is Honeywell's house wording:** Notifier `DN-7070:S`
  p6 writes *&quot;VEP-A00-P-NTF: &hellip; with **LED display**&quot;* against
  *&quot;VEP-A10-P-NTF: &hellip; with LED **and LCD** display&quot;*. Not a screen.
  **And the store carries the superseded SKU beside it**, confirmed live: `VES-A00-P` at
  $7,753 is the UL 268 **6th Edition** part that Xtralis Product Bulletin Doc **37870_01**
  (May 2024) discontinues, naming `VES-A00-P-UL` as its replacement &mdash; a
  manufacturer-stated supersession, so it went in the body, and the EOL page went to the
  owner's file. **Generation trap avoided inside it:** the 6th-Edition product guide gives
  1,837 ft of pipe and 0&ndash;39 &deg;C where the `-UL` sheet gives 1,706 ft and
  32&ndash;100 &deg;F. Wrong document family for this SKU.
- **&quot;Xtralis states carton quantities routinely&quot; now has a boundary of its own,
  and it is the RFP proof inverted on a vendor this file used as the counter-example.** In
  one ordering block on one page Xtralis numbers every neighbouring label &mdash;
  `E700-SP-DCL-PNT` 50 per roll, `E700-SP-DCL` 200 per roll, `E700-SPLR` 10 per sheet,
  `E700-SPLG` 8 per sheet &mdash; and item 18 reads only **&quot;VSP-950 Test Point Pipe
  Labels.&quot;** with no quantity. The store's *&quot;12 per sheet&quot;* is distributor
  convention. **A vendor-level positive is no more transferable than a vendor-level
  negative**, which is the same over-reach this file already corrected twice at the category
  boundary and once at the vendor boundary.
- **The vendor field looked wrong and was RIGHT, and knowing which shape you are in
  takes reading the document.** `XCL-VEA-H2-RA` sits under vendor **Vesda** and is a
  Sensepoint XCL gas detector, which is a Honeywell Analytics line &mdash; so the
  briefing called it the `OSE-HPW` case (a Vesda-vendored OSID part) and told the agent
  to flag it. **It is not.** The manufacturer's own product name for that order code is
  **&quot;VESDA Sensepoint XCL&quot;**, and Xtralis doc `33770_02` opens *&quot;Xtralis
  the manufacturer of the market leading VESDA Aspirating Smoke Detection technology has
  developed **with its sister company Honeywell Analytics** a new concept of aspirated
  gas detectors&quot;*, with the approvals footnote *&quot;These Listings/Approvals are
  owned by Xtralis, a Honeywell company.&quot;* **Vendor untouched, and it needs no owner
  flag.** This is the `PIP-018` shape, not the `OSE-HPW` shape: **the brand looks wrong
  until you read the document**, and the two shapes are indistinguishable from outside.
  Also settled there: **1000 ppm is the RANGE, not a set point** &mdash; it sits in the
  Available Sensors list beside *&quot;CO: 300ppm (adjustable 50&ndash;1000ppm)&quot;*,
  where the adjustable ones say so and H2 does not. And **the H2 variant is NOT UL 2075
  listed**: the sheet states UL 2075 for &quot;(CO and CH4)&quot; only, a variant
  boundary inside one family.
- **A live page describing the wrong half of an assembly, caught by the manufacturer's own
  FAQ.** `VSP-965`'s copy said the sampling module *&quot;continuously draws air from a
  protected area through an air sampling pipe network&quot;*. Xtralis FAQ `Doc. 26841_15`
  answers the exact question: the sampling module **ensures a representative sample is taken
  BEFORE the aspirator**, so the chamber sees particles unaffected by the aspirator's
  scrubbing. **The part that draws the air is the `VSP-963`.** Same family, adjacent number,
  opposite function &mdash; and an FAQ document, not a datasheet, is what settled it.
- **A live body error inherited from the MANUFACTURER's own website, not written by the
  store.** `059-007`'s copy said *&quot;1.5 m suction hose&hellip; T-piece
  **02-1007-25**&hellip;&quot;*. The Xtralis Europe catalogue says **2 m**, red &mdash; and
  **`buildings.honeywell.com` carries that identical wrong sentence on its own product page
  while its own product title says 2 m.** So Honeywell contradicts itself and the store
  inherited it whole. `02-1007-25` occurs **0 times** in both regional catalogues and the
  bulletin; dropped, and **deliberately not called invented**.
  **The `DN-62046` inverted proof fired again on the pack count:** neighbours `144-013` and
  `PIP-018` say *&quot;Pack of 10&quot;* in the same ordering block and `059-007` says
  nothing, so it is not a multi-pack &mdash; and the title asserts none, so there was
  nothing to flag.
- **The inverse case: the STORE was right and the distributors were repeating a series-wide
  block.** `VER-A30`'s datasheet prose headlines a 3.5 in. touchscreen for the whole VESDA-E
  remote family, and **two web searches repeated it back as a fact about the VER-A30
  specifically**. Three signals say otherwise: Xtralis names the A10 models **Remote Display**
  and this one **Access Point** in its own ordering block; the datasheet lists
  VESDAnet/Ethernet/USB as a *separate configuration* from the display one; and max power is
  **1.159 W against 2.112 W for the VER-A10-0**, column-verified by x-coordinate. At $1,450.95
  with 35 characters of live copy, a buyer wanting a screen could easily have bought this.
  **The display fact went in the body and deliberately NOT the title**, because Xtralis writes
  &quot;(No Relays)&quot; and never writes &quot;no display&quot; &mdash; so asserting the
  absence in a feed attribute would go further than the manufacturer does.

- **`VP-ELB-45` pack count is manufacturer-stated: 10 per box (v2b51).** Doc `17748_12` (`xtralis.com/file/623`, June 2024) ordering row *&quot;VP-ELB-45 45&deg; Elbow - &frac34;&quot;, 10 per box*&quot;*, confirmed by the coordinator. Title count unchanged, recorded in the owner's file as documented. UL 1887 / V-0 / 0&ndash;200 &deg;F are range-level statements about the pipe-and-fittings package; the live body's &quot;Socket to Socket&quot; was unsourced and dropped.

- **SKU `8000` is a VP-TEE listing with a bogus SKU (audit t04):** `8000` occurs 0 times in 17748_12 (file/623) and file/495 while VP-TEE occurs 3 times (&quot;Tee - 3/4, 15 per box&quot;). The store also sells VP-TEE under its own SKU at $37.30 against $64.30 here &mdash; a duplicate listing. Title left untouched (null); SKU and duplicate flagged.
