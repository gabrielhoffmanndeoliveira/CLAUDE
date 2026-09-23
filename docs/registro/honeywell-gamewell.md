<!-- Registro de casos do projeto TFAS. Movido VERBATIM de CLAUDE.md em 23 Sep 2026; nada foi reescrito. Nao e carregado automaticamente: leia sob demanda. E cronologico: entradas posteriores corrigem anteriores; em caso de conflito vale a mais recente e o nucleo em CLAUDE.md. -->

# honeywell-gamewell

- **A table caption can sit *below* its table, which inverts the obvious reading.**
  Gamewell-FCI `9021-60930` C places captions under the tables they label, so plain
  reading attributes every caption to the table above it &mdash; one row off, silently.
  This is the merged-cell trap's cousin: same fix, `page.get_text(&quot;words&quot;)`
  with y-coordinates, and the same rule &mdash; **never take a row-to-label assignment
  from reading order alone.**
- **The coordinator predicted a live claim was wrong and the live claim was right.
  Worth recording because the scepticism, not the page, was the error.** The
  `ATD-L3R-IV` page said the `-IV` models run both Velociti and CLIP while the
  suffix-free part is Velociti only, and the briefing told the agent *&quot;that is a
  strong, specific, falsifiable claim and it is the kind that is usually wrong &mdash;
  a finish suffix does not normally change a communication protocol.&quot;* It does
  here. Gamewell-FCI `9020-0620 Rev G` lists all six members with the protocol against
  each finish, and its Description paragraph gives the mechanism outright: *&quot;For
  legacy installations, service detectors are available in the classic ivory color
  that will operate in both Velociti and CLIP protocol for backwards compatibility.
  Service models are designated by the -IV part number.&quot;* **Ivory is a
  service-stock designation that carries a dual-protocol build, not a colour option**
  &mdash; two independent places in one document agreeing. The general lesson is not
  &quot;trust the live page&quot;; it is that **&quot;that kind of claim is usually
  wrong&quot; is a prior, not evidence**, and it has to lose to a document like any
  other prior. The same confirmation cleared the held `ASD-PTL3` page, whose closing
  makes the identical claim on the parallel photoelectric line.
- **The `GW` prefix hides the real manufacturer catalogue number, and it has now fired
  twice in two batches.** `GWPID-95` is `PID-95` in `CS-2044` Rev B; `GWRCE-95` is
  `RCE-95` throughout `CS-2045` Rev C including its Ordering table. **In both cases the
  `GW` form appears in no Gamewell-FCI document at all** &mdash; recorded as a bounded
  negative both times, with the real number added in parentheses rather than the SKU
  being touched. **There are 30 Gamewell-FCI `GW*` SKUs and only one already names a
  catalogue number in its title.** So the routing rule for this brand is: **search the
  part number with the `GW` stripped**, and expect the documents to be filed under the
  bare form. Beware the false friends &mdash; of 83 `GW*` SKUs, **50 are Gentex**, where
  `GWHS…` is a genuine Gentex weatherproof horn-strobe family and nothing is hidden.
- **EDAM has BOTH slug orders, so try both before searching.** The briefing gave
  `<Model>_<DocNum>.pdf` from `SD365_DF-61010.pdf`; an agent found
  **`DF-61012_ANN-100.pdf`** resolves too &mdash; `<DocNum>_<Model>.pdf`, the reverse.
  Eight other guesses for that document returned the 8,047-byte fingerprint. And **the
  bare `<docnum>.pdf` route is stronger than recorded for Gamewell-FCI**:
  `9021-60758.pdf`, `9020-0649.pdf` and `9020-0541.pdf` all resolved first try, three in
  a row. For that brand it is the cheapest route, not a long shot.
- **A stale model list can sit in a PDF's text layer without ever being rendered, and a
  grep alone reads it as a generation conflict.** Gamewell-FCI `9020-0617`'s text layer
  opens with `ASD-PL2F/ASD-PTL2F ASD-PL2FR` &mdash; **Series 2** codes &mdash; while a
  150 dpi render of page 1 shows only *&quot;Velociti Series 3 Detectors /
  Photoelectric Detectors&quot;*. The Series 2 strings are invisible leftovers. This is
  the **inverse of the invisible-dimension trap**: there the text layer was missing data
  that the page showed, here it carries data the page does not. Same remedy both ways.
  **Render before calling a generation conflict**, not only when a figure seems absent.
- **Tenth product-class error, and the type agreed with the wrong title again.**
  `ASD-PTL3` was titled *&quot;Thermal Sensor&quot;* and typed **Heat Detectors**, while
  `9020-0617` Rev K's ordering block reads *&quot;ASD-PTL3: **Photoelectric smoke
  detector** with thermal sensing&quot;* under a heading of &quot;Photoelectric
  Detectors&quot;, listed to **UL 268 7th Edition**. A buyer filtering for heat detectors
  gets a smoke detector, and one filtering for smoke detectors never sees it.
  **Its thermal class is separately contested inside that one document** &mdash; page 1
  prose says *135 &deg;F **fixed temperature*** and the page 3 spec block says
  ***Rate-of-Rise**: greater than 15 &deg;F/minute or 135 &deg;F*. Both give 135 &deg;F,
  so 135 &deg;F is published and neither class word is asserted. It is **not** rate
  compensation.
- **EDAM paths are case-sensitive, and this cost the verification a round trip.**
  `.../datasheets/DF-52397.pdf` returns the 8,047-byte fingerprint; **`df-52397.pdf`,
  lowercase, returns a 261 KB PDF.** An agent separately found the same for separators:
  **`DF_52004.pdf` (underscore) resolves where `df-52004.pdf` (hyphen) 404s.** So the
  path shapes to try, each one fetch, are now: bare `<docnum>.pdf`, **lowercased**,
  **underscore-for-hyphen**, `<Model>_<DocNum>.pdf` and `<DocNum>_<Model>.pdf`. Also
  recorded: `9020-0616.pdf` 404s under the flat directory while
  `datasheets/MS-7AF-Datasheet.pdf` serves that exact document, so **the bare-docnum
  route is strong for Gamewell-FCI but not universal &mdash; a model slug can be the
  filing key instead.**
- **The pack-count audit itself had the wrong document family &mdash; sixth instance.**
  Two of the 22 open rows are **Gamewell-FCI**, not System Sensor: `AOM-2RF-BP` and
  `MS-7AF-BP`. Both were recorded as &quot;six documents checked&quot; where all six
  were System Sensor L-Series appliance sheets that could not mention a Gamewell relay
  module or pull station under any circumstances. Checked properly now:
  `9020-0625` Rev I 04/19 lists only `AOM-2RF` in Ordering Information with zero
  occurrences of BP/bulk/pack, and `9020-0616` Rev F 11/17 lists twelve MS-7 variants
  and no `-BP`. Both are still negatives &mdash; but they are *now* negatives, and were
  not before. **A negative result is only worth what the document family is worth; an
  audit that carries one brand's citation list across a vendor boundary is asserting
  something it never checked.**
- **The &quot;prefer 9021- over AVDS&quot; rule has now failed twice, and the boundary is
  the same both times.** `9021-60931` is the right-sounding Gamewell-FCI L-Series wall
  speaker-strobe sheet and contains **zero occurrences of &quot;LED&quot;**, so it cannot
  carry an LED part; `AVDS-62174:A` is the only sheet that does. That repeats the
  `P2WL-P` / `9021-60929` case exactly. **Prefer a document family only until you have
  checked that it contains the part** &mdash; and the cheapest check is a grep for a word
  the part's own number implies.
- **Route notes.** **`xtralis.com/file/<id>`'s miss fingerprint is a drifting RANGE, not one
  number**: `text/html` at **226,237&ndash;226,241 bytes**, drifting a byte or two with the
  id &mdash; this file records a single 226,238, which is the gamewell-fci one-byte-drift
  tell again. **Xtralis product pages enumerate their own file ids with titles**, so
  `grep -oE 'href=&quot;[^&quot;]*/file/[0-9]+&quot;'` plus the anchor text on
  `xtralis.com/product/<id>/<slug>` gives a titled document list in one fetch.
  **`DN-7045` is reachable at exactly one shape** &mdash;
  `datasheets/notifier-us/hon-ba-fire-dn-7045.pdf` under the `honeywell-edam` root &mdash;
  with bare and revision-letter forms all returning the 8,047-byte fingerprint under both
  paths. And **Amerex's `/learning-center/product-brochures/` raw markup lists 60 PDFs**
  under `/upl/downloads/content-blocks/`, mime-clean, confirmed by the coordinator.- **Seventeenth incomplete-product case, manufacturer-stated verbatim, and it is an
  &quot;Addressable FACP&quot; that cannot address anything out of the box.** Verified
  directly by the coordinator in Gamewell-FCI `9021-60730` Rev H Ordering Information:
  ***&quot;SLP-RED: SLP addressable FACP with red door and black S3, SLP-BB backbox.
  Requires either an SLC-PM or an SLC95-PM for SLC loops.&quot;*** The card that gives the
  panel its addressable loop is a separate catalogue number, and the same page defines both
  (`SLC-PM` System Sensor protocol, `SLC95-PM` Apollo). **The condition is now in the
  title**, because a buyer specifying an addressable panel and receiving one with no loop
  card is the most expensive version of this trap yet.
  **And the coordinator's routing caution was disproved in the same fetch:** the briefing
  warned that an `SLP-` prefix might hide the real catalogue number, as `GW` does on this
  brand. `SLP-RED` is **verbatim** in Gamewell-FCI's own ordering block.
- **`-RB` does NOT mean &quot;replacement board&quot;, and the disproof is a cabinet.** The live
  `FLPS-7-RB` read as a replacement board; the same suffix sits on **`S3BB-RB`, which
  `9021-60730` Rev H describes as an SLP red cabinet with an inner door.** A cabinet is not a
  board. Across the family the suffix marks the replacement/retrofit **ordering variant**:
  `SLP-RB` motherboard, `FLPS-7-RB` power supply, `S3BB-RB` cabinet. Gamewell never expands the
  letters &mdash; recorded as a bounded negative, not guessed.
  What settles the relationship positively is **Table 8.2.1 of the S3 UL Listing Document,
  whose columns are Accessory/Sub-Assembly then Part Number**: the row reads
  `FLPS-7 | FLPS-7-RB | Power Supply`, so the assembly has one name and the orderable thing
  another. **And it is the incomplete-product trap inverted for the second time**: this number
  appears inside *two other products'* &quot;Requires the following:&quot; lists
  (`SLP-RETROFIT` and `S3BB-RB`), render-confirmed at 300 dpi because those lines were orphaned
  in plain extraction. The live &quot;120V AC, 7A&quot; was correct and the `type` is correct.
- **A live body that is another PRODUCT CLASS's spec block entirely, and a cable cannot have
  the quantity it asserts.** `GW71332`'s whole description read
  *&quot;Interface Cable: Non-condensing-93%: Nodes: 250: +32F to +120.2F&quot;* &mdash; panel
  environmental specifications scraped onto a **ribbon cable**, and **a cable has no node
  count**, which is the tell available without any document. The identical wording sits on a
  distributor page, so it is correlated copy in one direction or the other. The live **title**
  was fine, so this cost one channel.
  **Third recorded instance of the `GW` prefix hiding the real catalogue number on this brand**,
  after `GWPID-95`&rarr;`PID-95` and `GWRCE-95`&rarr;`RCE-95`: Gamewell prints **&quot;P/N
  71332&quot;**, and the `GW` form appears in no Gamewell document read. SKU untouched, bare
  number named in the body. The part is documented **only** in a mirror &mdash; *IdentiFlex 630
  Installation &amp; Operation Manual, P/N 71165 Rev 3.0, 9-25-96* &mdash; and the two
  independent mirrors' normalised text is **word for word identical on all three `71332`
  sentences**, which is what licensed using it. A search snippet calling `71165` the panel's
  part number was wrong: **it is the manual's own number**, printed on the cover.


### e06 (23 Sep 2026): E3BB-RD/INCC

- 9020-0649 Rev X (06/20) resolved bare and first try, as did 9020-0613 (Rev O). `gamewell-101625/hon-ba-fire-9020-0649.pdf` gives the 8,047 B miss, while `gamewell-101625/hon-ba-fire-9020-0542.pdf?download=false` works. p2 D-size row: "E3BB-RD/INCC: Enclosure, Command Center, Red, 'D' Size", 19-3/8 × 41 × 4-1/2 in. The enclosure is the backbox and outer door only; the inner doors (E3ID2-D/E3ID3-D) and the E3-INCC-D-PLATE are separate. **Trap: the 9020-0649 p4 capacity table labels two different rows "E3BB-BD".** INCC sheet 9020-0542 Rev K does not list the enclosure.
- t06 (23 Sep): E3-INCC-D-PLATE had the title "Command Center Module", a class error. It is now "…Command Center Module Mounting Plate, D Size" per 9020-0649 Rev X p2; the old title is a substring of the new one. The store SKU is `E3-INCC-DPLATE` (sibling `E3-INX-DPLATE` follows the same pattern; flagged). E3ID3-D's title was normalised to the sibling E3ID2-D pattern (it had raw quotes); its type "Command Centers" → "Doors" was flagged.
