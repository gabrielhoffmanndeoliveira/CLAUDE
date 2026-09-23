<!-- Registro de casos do projeto TFAS. Movido VERBATIM de CLAUDE.md em 23 Sep 2026; nada foi reescrito. Nao e carregado automaticamente: leia sob demanda. E cronologico: entradas posteriores corrigem anteriores; em caso de conflito vale a mais recente e o nucleo em CLAUDE.md. -->

# napco

- **The family-disagreement scan re-run on a live pull, 22 Sep 2026 &mdash; and it
  over-fired for the first time, with a mechanism behind it worth fixing.** 16,031 active
  products, 131 families of three or more, **54 families disagreeing on `type`, 94
  divergent members**. But **25 of those 94 are one defect repeated: the stem rule
  collapses a product LINE into a family.** `PAD100` (7 members: bases, heat detectors,
  relay modules, CO detectors, speakers), `PAD300` (8), `SIGA` (13: bases, duct detectors,
  kits, mounting plates, smoke detectors) are **series prefixes, not families** &mdash; a
  catalogue of different device types sharing a prefix cannot &quot;agree&quot; on a type
  and it is not a defect when it does not.
  **The guard is a mechanism, not a threshold: a family is variants of ONE product, and a
  line is a catalogue under a prefix. Drop any group whose flagged members span three or
  more distinct types, or that has eight or more members spanning two or more.** That
  removes all 25 and leaves **69 real divergences across 49 families**, which is the number
  to work from.
  **The scan independently rediscovered two already-confirmed defects** &mdash;
  `FST-951-IV` (thermal detector typed Smoke Detectors) and `P2WLED-P` (horn strobe typed
  Strobes) &mdash; which is the strongest validation this kind of scan can offer, and it
  did the same thing on its first outing.
  **The clearest new finds, all structured data and therefore flagged rather than applied:**
  `TX3-WRT-2H` is a **key fob transmitter typed Batteries**; six Napco `GEMC-*` and
  `SLE-*-CB` **commercial burglary devices are typed Fire Alarms, Sensors, Enclosures and
  Carbon Monoxide Detector**; `GBC-120-2` is a **gas boiler controller typed Fire Alarms**;
  `FSP-951R-BP` is a remote-test photo detector **typed Duct Detectors**; and two Westell
  `CS40-` amplifiers are typed Fire Alarms while their own sibling is correctly typed BDA.
  Note the owner's standing rule is about **titles** &mdash; no &quot;(Security)&quot; or
  &quot;Non-Fire&quot; in a title &mdash; and says nothing about the `type` field, which is
  a separate Merchant Center attribute. A burglary device typed Fire Alarms is a
  categorisation error, not a warning label.
  **And the outlier-is-not-the-defect caveat fired again, on eight products at once:** the
  `LENS-A2/B2/G2/R2/A3/B3/G3/R3` lens attachments are typed **Lens** inside families typed
  **Strobes**. The minority is right &mdash; a lens is not a strobe &mdash; so what needs
  adjusting is the family, not the eight. **The scan reports that a family disagrees, never
  which member is wrong**, for the fourth time.
  Full list in `/tmp/tfas/SCAN_familia_type_REAIS.json`.
- **Twentieth product-class error, and the live page was ANOTHER MODEL's copy end to end,
  separated by one letter.** `SLE-LTEV-CFB-PS` was titled and described as a **dual path
  cell/IP** communicator with **&quot;Panel-powered Technology&quot;**. Napco's own document
  library, read directly by the coordinator, titles its wiring diagrams
  ***&quot;SLE-LTEV-CFB-PS &amp; SLE-LTEA-CFB-PS (Sole Path)&quot;*** &mdash; twice, in the
  CAD and PDF entries &mdash; and lists the **dual path** models separately as
  `SLE-LTEVI-CFBPS, SLE-LTEVI-CFB, SLE-LTEVI-FIRE&hellip;`, **the `I` variant**. The
  datasheet separately says panel power *&quot;excludes Direct AC-Powered '-PS'
  models&quot;*, so the live page asserted both halves of the sibling's spec and neither of
  this part's.
  **The store does not carry the `-I-` variant at all**, which is why nothing ever
  contradicted it: this is the borrowed-copy signature (`PAD200-DD`, `4-NET-SM`, `INX-10A`)
  with **no sibling page in the catalogue to disagree**. A buyer specifying a dual-path
  communicator to satisfy an AHJ received a cell-only one.
  Suffixes settled from Napco's own text: **LTEV Verizon, LTEA AT&amp;T, CFB commercial and
  residential Fire and Burglary, PS the SLE-ULPS-R supply and 16.5V transformer mounted
  inside the red housing.** Those are included; the **4&ndash;7 Ah battery is not**, and the
  24-hour standby needs it. Route: `tech.napcosecurity.com` gates its PDFs behind a dealer
  login, **but its tag index is open** &mdash; `/techlibrary/tagresults/tag/<sku_underscored>`
  lists every document title for a SKU, and the titles alone carried the answer.
- **A tag-index query form that returns a false negative, and the control is what caught
  it.** This file records `tech.napcosecurity.com/techlibrary/tagresults/tag/<sku_underscored>`
  as the open route. For `SLE-MAX2LCBTFC` the **underscore form returns 0 results** and
  the **hyphen form returns 2 documents** &mdash; both forms work, depending on how the
  tag was entered. The agent only knew the zero was false because the underscore form
  *did* work on the control SKU from the briefing, **which proved the endpoint alive and
  the query wrong rather than the host empty.** Carry a known-good control into every
  negative.
  And the part is not what its SKU suggested: **the series is `MAX2L`, not `MAX2`**
  (siblings `SLE-MAX2L-C`, `SLE-MAX2L-Z`), where **MAX2 is dual-carrier and MAX2L
  tri-carrier** &mdash; so carrying MAX2 specs across would have been wrong. It is also
  **not a fire communicator at all**: Napco files it under *Connected Home &amp; Business*
  with compliances **UL 1610 and UL 987 and no UL 864**, while the fire products are the
  separate StarLink Fire MAX2 line. Seventh instance of the recorded &quot;Napco `SLE-*-CB`
  intrusion devices typed Fire Alarms&quot; family, and this SKU contains `CB`.
- **A manufacturer contradicting itself on the product CLASS, and the right answer was to
  publish both.** Napco's `FLX2-255` specification block calls the panel
  **Addressable** and its own Ordering line calls it **Conventional**. The agent declined
  to pick a side and the published copy says so in one sentence: conventional zones on the
  fire bus, addressable devices once a `GEMC-FW-SLC` module is fitted, which is what makes
  both statements true. **This is the shape to copy when a document disagrees with itself
  about what a thing IS** &mdash; the prefer-the-table rule settles a *number*, and a class
  question sometimes has a both-are-true resolution that neither statement states.
- **Three more search endpoints that silently ignore the query, and one that returns 406 to
  everything.** `pottersignal.com/search?q=` gives a **byte-identical 80,279-byte response
  with one md5 for a real and a bogus term** &mdash; the `hochikiamerica.com/productsearch`
  shape exactly, second instance. `aiphone.com/?s=` renders client-side and returns ~3,565
  characters of text with no result list for every probe including the control.
  `detectortesters.com/catalogsearch/result/?q=` returns **HTTP 406 to every query**,
  control included. Against those, `know.aiphone.com/search?query=` **does** discriminate
  (bogus &rarr; empty array) but indexes documents only, so a numeric query returns spurious
  hits &mdash; `213505` matched a French install manual whose whole indexable body is the
  word &quot;download&quot;. **Carry a known-good control into every negative**, which is
  also what told one agent that a Napco tag query returning zero was the wrong query form
  rather than an empty host.
- **The Napco tag-index false negative reproduced exactly, and only a control reveals it.**
  `tech.napcosecurity.com/techlibrary/tagresults/tag/GEM_P3200` returns 475,901 bytes while
  the hyphenated `GEM-P3200` returns 343,340 &mdash; **byte-identical to the bogus
  control**. This file already records the underscore/hyphen split; what is new is the
  measurement showing the failing form is indistinguishable from an empty host without a
  known-good control beside it.
- **The Napco tag-index form inverted, and an MD5 control would have passed the empty
  result.** On `GEM-TOUCH` the **hyphenated** form returned 343,340 bytes &mdash; *the same
  length as the bogus control* &mdash; while the **underscored** form returned 352,634 and
  six real documents. That is the opposite way round from the recorded `SLE-MAX2LCBTFC`
  case, so **neither form is the right one; carry both and a control.** And all three MD5s
  differ because the page echoes the search term, **so an MD5-only control wrongly passes
  it** &mdash; the byte count is the tell. Fourth instance of a search endpoint that defeats
  the obvious control, after Hochiki, Interstate Batteries and safefiredetection.
  Also measured: `napcosecurity.com`'s product-page 404 is **30,439 bytes against the 30,430
  on record** &mdash; host-fingerprint decay again &mdash; and
  `tech.napcosecurity.com/techlibrary/downloadfile/id/<n>` returns an identical
  340,811-byte shell for every id, confirming that only the tag index titles are usable.
- **TWENTY-THIRD COORDINATOR PREMISE WRONG, AND IT WOULD HAVE CREATED A DEFECT RATHER THAN
  FOUND ONE.** The v2b43 briefing said `GEM-P1632` is *&quot;almost certainly a Napco Gemini
  INTRUSION panel, not a fire panel&quot;* and predicted a ninth instance of the recorded
  `GEM-*`/`SLE-*-CB`-typed-Fire-Alarms error. **It is a combination unit.** Napco's own UL
  block in `WI808F` lists **UL 1023 Household Burglar *and* UL 985 Household Fire Warning**,
  CSFM listing `7167-0992:0118` calls the family *&quot;combination fire and burglary alarm
  control units&quot;*, and **zones 7 and 8 are two-wire smoke detector zones**. The Shopify
  `type` of Control Panels is **correct and needs no owner flag**.
  **What disproved it was the briefing's own instruction** &mdash; *the listing is what settles
  the class*. Worth stating because every other entry in this file is a premise that would have
  *missed* a defect; this one would have **manufactured** one, by flagging a correct structured
  field on a catalogue where a burglary device typed Fire Alarms is a known real error. **A
  pattern with eight confirmed instances is still a reason to check and not a licence to
  conclude.**
- **Three briefing warnings that pointed at the wrong document and were still worth giving.**
  The v2b44 briefing carried this file's `S4902-0003`/`S4906-0003` warnings &mdash; the
  incoherent &quot;125 kHz to 12 kHz&quot; frequency response, the 25 V against 70.7 V dBA
  split, the `CA` ULC suffix &mdash; to `4903-9197`. **None applies to `S4903-0019-5`**, which
  prints a coherent 400&ndash;4000 Hz, gives **one** speaker dBA row with no voltage split, and
  has no `CA` member. The warnings still forced the checks that found the real defect above.
  Two other premises wrong in the same briefing, both of which would have produced a **false
  correction**: `SLE-ANTEX` is **Napco's own series name**, not a truncated SKU, so the live
  title was brand + SKU + series and entirely legitimate; and `COSMO-4W` and `COSMOD4W` are
  **two different catalogue numbers in one ordering table**, not a lost hyphen. **A
  punctuation-stripping catalogue makes every unusual spelling look like a defect** &mdash;
  check the ordering table before calling one.
- **The tag-index separator has no right answer, measured a third time.** On `SLE-ANTEXT50` the
  **underscored** form returned 348,719 bytes with two real results while every **hyphenated**
  form returned 343,341&ndash;343,345 against a bogus control of **343,340** &mdash; empty, and
  indistinguishable without the control, with all three MD5s different. And the same session
  found `SLE_MAX2LCBTFC` **empty in the underscored form**, the opposite of what this file
  records for that SKU. **Neither separator is &quot;the&quot; right one; carry both and a
  known-good control every time.** Useful tell: the bogus control prints *&quot;of 0
  Results&quot;* in words, which is worth grepping for rather than comparing sizes.


- **`SLE-ANTEXT30` settled from first-party sheet A745 (v2b51).** `napcosecurity.com/media/pdfs/A745-SLE-ANTEX-Sheet10-30-24.pdf` (359,963 B): the digits are cable length (*&quot;SLE-ANTEXT30 As above, with 30&apos; cable&quot;*), 695&ndash;3000 MHz, 50 W, Type N. **The sheet contradicts itself on VSWR** (prose &quot;1:5:1&quot;, spec block both &lt;1.5:1 and &lt;2.0:1) &mdash; none published. Distributor copy (10 W, stainless radiators, SMA adaptor) is an older generation. Tag index: **underscore form `SLE_ANTEXT30` returned 348,719 B with 2 results; hyphen form 343,343 B, 0 results, against a bogus control at 343,340** &mdash; fourth measurement, the separator still has no fixed answer. `downloadfile/id/<n>` is a 340,811 B login shell; a bogus id 404s at 389,249 B. Store types `SLE-ANTEXT50`/`75` as Cellular Communicators while 30/04/100 are Antennas; flagged.

- **`GEM-P9600` is a combination burglary and HOUSEHOLD fire panel, the second Gemini confirmed after GEM-P1632 (v2b51).** `WI742F` UL LISTINGS: UL 1023, UL 985, UL 609, UL 1610, UL 365; **UL 864 zero times**, so the copy says household fire, not commercial. The tag index carries listing text (the CSFM *&quot;combination fire and burglary alarm control unit &hellip; Model H299 enclosure&quot;*). Document defects: WI742F says ACM modules give access control *&quot;of the GEM-X255 control panel&quot;* (pasted from the X255 manual), and prints EOL130 as &quot;130W, 3W&quot; &mdash; the Omega trap, 130 &#937;. Tag index again: `GEM_P9600` 69 results, `GEM-P9600` 0 at 343,340 B, bogus 343,342 B, known-good `GEM_P1632` 45. The `media/pdfs` 404 measured 30,430 B again.

- **`FW-2S` from a verbatim distributor mirror of a first-party instruction sheet, and FW-RM1 is REQUIRED, not optional (v2b52).** Napco `WI1805A 04/10` is behind the dealer login; ADI's `cdn.adiglobaldistribution.us/pim/Original/<n>/` serves it, and a homecontrols.com scan agrees on every spec cell. Coordinator-verified: working voltage **8.5&ndash;14 VDC** (12 V only, against FW-2's 8&ndash;35), standby 43.6 &micro;A; the wiring diagram reads **&quot;FIREWOLF FW-RM1 REVERSING MODULE REQUIRED FOR SOUNDER OPERATION (SEE WI1809)&quot;** where the live copy called it optional. The live &quot;85 dB&quot; appears in no Napco document read and was removed. **No UL standard is named**, so the 217-vs-268 question stays open; fire use rests on Napco's compatible-panel list. Tag index: `fw_2s` returned 5 results (353,817 B); the hyphen form returned 343,336 B against a bogus control at 343,339 (&quot;of 0 Results&quot;) &mdash; the underscore won this time. `napcosecurity.com/sitemap.xml` 404s at 30,443 B.

### e10 (23 Sep 2026): NAE-ET10

- It is a Napco **E-Access** mullion reader (not iSecure or ArmorIQ). Napco A810 (©1.2022) and A793A (2023, the Continental CAE-ET10 twin) have identical tables with the **Voltage and Current row labels swapped**. Warranty says Lifetime on the sheet and 5 years on the Access Pro page, so it was not published. Tag index: NAE-ET10 and NAE_ET10 both "of 0 Results" (343,339 B, against 343,342 B for the bogus control); the known-good GEM_P1632 returned 45 results. The `media/pdfs` 404 is 30,430 B.
