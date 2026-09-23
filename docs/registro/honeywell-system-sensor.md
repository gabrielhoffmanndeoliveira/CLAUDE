<!-- Registro de casos do projeto TFAS. Movido VERBATIM de CLAUDE.md em 23 Sep 2026; nada foi reescrito. Nao e carregado automaticamente: leia sob demanda. E cronologico: entradas posteriores corrigem anteriores; em caso de conflito vale a mais recente e o nucleo em CLAUDE.md. -->

# honeywell-system-sensor

- **Two cheap verification tricks worth reusing.** An MD5 comparison **proves** a mirror
  verbatim instead of arguing about it: `prod-edam.honeywell.com`'s
  `hbt-fire-I56-5100-001-manual.pdf` and `mainelectricsupply.com`'s
  `syssbbgwl-8.pdf` are byte-identical at 322,407 bytes. And **a document renumbering
  is not a new product**: Edwards `85001-0581` (2013, EST branding, one model) became
  `E85001-0640` (2020, Carrier branding, three models), and seven years apart the sound
  levels, currents, dimensions and temperature range agree exactly. An `E` prefix plus
  a different number is the same line.
- **`alarmax.com/customer/docs/skudocs/` filenames are not derivable from the SKU.**
  It is the right host for Eaton, but `syssbbrl-8.pdf` and `SYS-SBBRL.pdf` both 404 for
  System Sensor. Search the filename, same lesson as EDAM slugs and `qdigital.mx`.
- **EDAM paths cannot be constructed from the document number**, and a failed EDAM
  fetch has a fingerprint: **`application/javascript`, about 8,047 bytes, every time**.
  `AVDS916-01.pdf` exists under no `products/` tree; the file is published as
  `.../literature-and-specs/datasheets/L-Series-LED-Indoor-Horns-Strobes-and-Horn-Strobes-Data-Sheet.pdf`.
  Search for the slug, do not build it.
  **Softened 21 Sep 2026, because &quot;cannot&quot; was too strong and costs a free
  fetch.** A bare `<docnum>.pdf` under `/datasheets/` **does** resolve for some
  Gamewell-FCI documents: `9020-0625.pdf` returns a 106 KB PDF while `9020-0616.pdf`
  returns the 8,047-byte JavaScript. So **try the bare document number once** &mdash; it
  is one fetch and it hit on the first Gamewell part tried &mdash; then fall back to
  searching the slug. Two more EDAM shapes worth knowing: a `<Model>_<DocNum>.pdf`
  convention (`SD365_DF-61010.pdf`, `H365_DF-61011.pdf`), and **per-brand
  subdirectories under `/datasheets/`**, of which `farenhyt/` is the one that unlocked
  a third view of the System Sensor L-Series.
- **A manufacturer's own domain can serve navigation chrome that pymupdf opens as a
  seven-page document, and this is the worst version of the extraction trap yet.**
  `systemsensor.com/en-us/Documents/<file>.pdf` returns **HTTP 200**, 112 KB, mime
  `application/javascript`, and `fitz.open()` succeeds and reports **7 pages** whose
  text begins &quot;&bull; &lt; Back to Building Automation&quot; and continues through
  the site menu. Nothing about the fetch looks wrong: right host, right filename, 200,
  six figures of bytes, a document that opens. The **only** signal is
  `file -b --mime-type`, which is why that check is not optional. It cost a false
  negative here &mdash; `AVDS865` was briefly recorded as carrying no bulk pack when it
  had never actually been read; the real sheet (`AVDS865-05`, 859 KB, from EDAM) agrees,
  but that was luck, not method. **A first-party host earns no trust the mime check
  would not have given it.**
- **The strongest disproof of a supersession claim is a mechanism, not an absence.**
  `SPCWL` carried &quot;(Replaced by SPCWLED)&quot;. Bulletin M23.2SS's REPLACES table
  holds **only horn strobes, strobes and lenses &mdash; no speakers at all**, which by
  itself is just another negative result. What settled it was positive and structural:
  `AVDS-62174:A`, dated **08/29/2024 and therefore after the whole LED conversion**,
  still lists SPCWL under a live &quot;L-Series Speaker&quot; heading, and its
  &quot;L-Series with LED Speaker Strobes&quot; table contains **SPSCWLED but no
  SPCWLED**. The reason is obvious once stated: **a speaker has no strobe, so an LED
  strobe refresh had nothing to change on it.** The claim is SPCWL confused with
  SPSCWL, whose real successor is SPSCWLED. **When a supersession claim looks wrong,
  ask what the refresh actually changed &mdash; if the part lacks the component that
  was refreshed, that is a reason, and a reason beats a missing row.**
- **Never conclude a part number is invented from a negative search result.**
  `THM04R3000` was called an invented part number on 21 Sep 2026 and removed from a
  live page, because it "appears in no Resideo document". It appears in **submittal
  33-00461**, the document that actually covers that product, twice &mdash; in the
  T10+ model list as "THM04R3000 (EIM)" and as the heading of its own electrical
  ratings table. The search had covered every **RedLINK** document; the T10+ Pro is a
  **RedLINK 3.0 / Wi-Fi** generation product whose EIM does not use the RedLINK 2.0
  `THM5421Rxxxx` numbering, so the one settling document was outside the search
  space. The replacement part number was real but belonged to the **wrong product
  generation** &mdash; the sibling-part failure mode operating one level up. Reverted.
  **A negative result bounds the search, not the catalogue.** Removing a live part
  number is a claim and needs positive evidence, the same bar as adding one; and
  check the generation before the part number.
  **It has now happened twice in one day, and the second time it came from an agent,
  not the coordinator** &mdash; so state this rule in every briefing. A v2b09 agent
  reported that the live `SS-CO` page's reference to `SS-PHOTO-CO` was unsupported,
  because neither part appears in `SPDS-62165`, the SS-Series ordering table. That is
  the **smoke and heat** datasheet; the CO products are a separate document family.
  `SS-PHOTO-CO` has its own datasheet (`SPDS-62171` Rev. B, 5/7/2024: *"Combination
  smoke and CO detector"*, UL 268 7th edition and UL 2075) and its own installation
  guide. Verified positively, nothing changed, one search and one download.
  **Wrong document family both times.**
- **When two Honeywell documents disagree, prefer the part-specific manual over a
  sibling brand's catalogue sheet.** Fire-Lite `DF-60059:G` (a 2015 catalogue sheet)
  and System Sensor `I56-3737` (the part's own manual) disagree on **five** `B224RB`
  figures at once &mdash; diameter (6.1 in. against 6.85 in.), standby current
  (&lt;500 &micro;A against 170 &micro;A), relay set times, AC contact rating (0.9 A
  against 0.5 A at 125 VAC) and single-gang box compatibility. **Only the intersection
  was published.** The diameter split may be an old-style/new-style generation
  difference &mdash; resellers list both &mdash; but no document says so, so nothing
  was claimed. Five disagreements in one pair is not a typo; it is two generations or
  two sources, and neither is resolvable from the documents alone.
- **A load-bearing restriction can live in an asterisk footnote hanging off the
  ordering table, where grepping the body returns a false negative.** The live
  `WAV-CWL` page claims the wall bases fit only L-Series devices *&quot;manufactured
  after 26 April 2019, date code 9045 and later&quot;* while the ceiling bases are
  unrestricted. **Confirmed in three documents** &mdash; `SPDS902-04` (3/10/2022, a
  revision newer than the `SPDS902-01` the sibling page used), `SPDS902-01` and
  Gamewell-FCI `9021-61070:C` &mdash; in almost the page's own words. **But the note is
  a footnote on the table, not prose.** Anyone checking that claim by searching the
  datasheet text would have found nothing and called it unsourced, which is the
  wrong-document-family failure in miniature: right document, wrong part of it.
  **Read ordering-table footnotes before declaring a compatibility claim unsupported.**
- **`RFP`'s &quot;5-Pack&quot; is unsourced, and this is the pack-count mechanism from
  the other side.** `AVDS870-03` (10/10/2023) **states pack quantities when it means
  to, on the same page, in the same Ordering Information block** &mdash; `TR-2`,
  `TRC-2`, `TR-2W`, `TRC-2W` each marked &quot;(5-pack)&quot;, `TRCWLA-10` and
  `TCRLA-10` &quot;(10-pack)&quot;, plus a footnote about bezel packs &mdash; and the
  two retrofit-plate rows carry **nothing**. `AVDS882-03` (2020) and `AVDS4004` (2015)
  do the same. **Three revisions across ten years, numbering RFP's neighbours and
  declining to number RFP.** That is exactly the `DN-62046:C` proof inverted, and it
  makes the negative positive. Title left untouched; flagged to the owner.
- **Eighth coordinator premise proven wrong, and this one was stated as &quot;almost
  certainly&quot;. The `R` in `B200SR-LF` is not a relay.** The briefing told an agent
  the `R` was &quot;almost certainly a relay, but verify&quot;; the agent verified and
  found `I56-4152-005` lists six terminals with **no relay in the terminal table or
  either wiring diagram**. The real separator is **addressability**: Gamewell-FCI
  `9021-60843 Rev F` names the part verbatim *&quot;Low Frequency Intelligent
  **Non-Addressable** Programmable Sounder Base&quot;*, while `SPDS53602` says the
  **B200S-LF** *&quot;listens in to the communication between the attached sensor head
  and the FACP to adopt the same address as the detector&quot;*, giving the panel
  control of volume, tone and group. So `B200S-LF-IV` and `B200SR-LF-IV` are genuinely
  different products and the store is right to carry both. **What the letter `R`
  actually stands for is still unsourced across six documents** and is recorded as a
  bounded negative, not guessed &mdash; the functional difference is documented, the
  letter is not, and those are different claims.
- [CORRIGIDO — preferir `9021-` só depois de grep confirmar que a ficha contém a peça; falhou 3 vezes; ver neste arquivo &quot;prefer the `9021-`&quot;] **The pack count IS manufacturer-stated &mdash; in a document nobody had opened.
  Four searches across two batches concluded &quot;unsourceable&quot; and all four were
  bounded wrong.** System Sensor document **`9021-62013:C`, 9/25/2020** (L-Series Low Frequency)
  carries, in its Ordering Information block, the footnote
  **&quot;&dagger;Add -BP10 to order bulk pack of 10 units&quot;**. The dagger is
  attached to the sounder-only models &mdash; HRL-LF, HWL-LF, HGRL-LF, HGWL-LF,
  HCRL-LF, HCWL-LF and their ULC variants. **That settles 5 of the 27 asserting titles
  and $2,054,439 of the $3.45M, including the largest single one, `HWL-LF-BP10` at
  $1,842,048** (plus `B300-6-BP` and `B501-WHITE-BP` via Fire-Lite `DF-61010:B`).
  **25 titles and $1,403,392 remain open** across the LED, strobe, speaker and
  detector families &mdash; and that is now a *mechanism*, not an absence. See below.
  **Two lessons, and the second is the transferable one.** First, the wrong-document
  -family failure again, for the fifth time &mdash; the agents searched the datasheets
  for the *product*, and the statement sits in the ordering block of a *different
  family's* sheet. Second, the document families differ: **`AVDS910-02` covers
  the same product and does NOT carry the footnote**, so on this brand **prefer the
  `9021-` document family over the `AVDS` one**.
  **CORRECTED 22 Sep 2026, twice over, and both corrections came from an agent
  contradicting this file.** (a) The document number is **`9021-62013`, with no `-E`
  suffix** &mdash; verified by the coordinator directly, where the bare name returns a
  206 KB PDF and `9021-62013-E.pdf` returns the 8,047-byte fingerprint. The `E` was
  never a revision letter; the revision is **`:C`**. (b) **The old/new framing was
  wrong on the dates.** `AVDS910-02` is **11/02/2020** and `9021-62013:C` is
  **9/25/2020**, so the `AVDS` sheet is the *later* document and still lacks the
  footnote. **The difference is between document families published weeks apart, not
  between an old revision and a new one** &mdash; which makes the rule stronger, not
  weaker: it is not that System Sensor added carton quantities over time, it is that
  one family states them and the other does not. Scope and per-SKU basis in `/tmp/tfas/PACKCOUNT_decisao.csv`.
- [CORRIGIDO — baterias também têm quantidade declarada, e a regra vale só para Honeywell; ver honeywell-notifier.md &quot;BATTERIES are a third&quot; e xtralis-vesda.md] **The pack-count negative is now a rule with a boundary: Honeywell states bulk packs
  for BASES and for LOW-FREQUENCY SOUNDERS, and for nothing else &mdash; across three
  sibling brands.** The untried route was the sibling-brand twin, and it was worth
  running: EDAM turns out to carry a **`datasheets/farenhyt/` subdirectory**, so the
  same System Sensor L-Series hardware is documented a **third** time under Silent
  Knight's Farenhyt brand (`hbt-fire-351574-L-Series_Horns_HornStrobes_Wall.pdf`,
  `hbt-fire-351575-..._Ceiling.pdf`). Nine documents now checked across System Sensor,
  Fire-Lite and Farenhyt &mdash; `AVDS916-01`, `AVDS865-05`, `AVDS868-02`, `AVDS910-02`,
  `AVDS871-02` (ECS/MNS speakers), `9021-60928`, `9021-60929`, `AVDS885-01` and the two
  Farenhyt sheets. **Not one lists any `-BP` number.** Meanwhile `DF-61010:C`
  (5/28/2020, a newer revision than the `:B` cited earlier) states both base packs
  outright, and `9021-62013:C` states the LF sounders. So the split is not by brand and
  not by document age: **Honeywell states a carton quantity for bases and LF sounders
  and declines to for strobes, horn strobes and speakers.** That converts
  &quot;six documents checked&quot; from a bounded negative into a positive finding
  about how this manufacturer documents, which is the bar the `SPCWL` case set &mdash;
  *a mechanism beats a missing row.* The remaining titles rest on convention, and
  **the cheapest authoritative fix is still a purchase order or a carton label**, not a
  tenth document.
- **Pack counts in this catalogue rest on convention, not on documents, and the
  distinction is now measured.** Three `-BP10` SKUs came through v2b13 and **not one
  manufacturer document states the carton quantity.** The current L-Series datasheet
  `AVDS916-01` (10/03/2023) lists **no `-BP` model at all** in its ordering table,
  `M23.2SS` lists none, and in `I56-0022-000` the string &quot;BP&quot; appears **zero
  times**. Two things sharpen that into a real gap rather than an omission:
  `AVDS916-01` **does** state pack quantity when it means to
  (&quot;Each bezel pack ships in a package of 5&quot;), and a sibling Honeywell brand
  states it outright &mdash; Fire-Lite `DF-61010:B` says *&quot;B300-6-BP: Bulk pack of
  B300-6, package contains 10&quot;*. So System Sensor's silence on `-BP10` is a real
  gap, and **the suffix plus distributor consensus is convention, not the manufacturer
  bar.** Two live titles assert &quot;10 Units&quot; on that basis. All three went to
  the owner rather than being changed, because pack counts in titles are a Merchant
  Center feed attribute. **The cheapest authoritative fix is a purchase order or a
  carton label, not another search** &mdash; and the decision generalises, because the
  store's whole &quot;Bulk Packs&quot; collection runs on the same convention.
- **The pack-count question is 27 titles and $4.6M, not three &mdash; and there is a
  research route nobody had tried.** Measured 21 Sep 2026: **67 SKUs carry a `-BP`
  suffix**, **27 assert a quantity in the title**, and the family holds **$4,602,239 of
  ERP revenue**. 25 of the 27 are System Sensor, worth $3.37M, and the largest single
  one is `HWL-LF-BP10` at **$1,842,048**. The route: **System Sensor does not state pack
  counts in its own datasheets, but Honeywell states them for the identical part in a
  sibling-brand document** &mdash; Fire-Lite `DF-61010:B` says *&quot;B300-6-BP: Bulk
  pack of B300-6, package contains 10&quot;*, and `B300-6-BP` sits in this catalogue
  under vendor System Sensor. So for several of these the answer may be in the
  **Fire-Lite twin**, not the System Sensor sheet. Test that on the five largest before
  falling back to a purchase order or a carton label. Scope and per-SKU documentary
  basis in `/tmp/tfas/PACKCOUNT_decisao.csv`.
- **A stale figure can be proved stale by the PREVIOUS revision, which is a third
  signal rather than a coin flip.** Eaton `TD450158EN` (May 2025) prose says the Eluxa
  speaker has a &quot;listed sound output of up to **87 dB** at 10 feet&quot; while its
  own Table 2 runs to **90 dBA**. 87 dBA is *exactly* the maximum of the September 2021
  revision, whose taps stopped at 2 W where the 2025 taps run to 8 W. So this is not
  prefer-the-table-by-rule: the prose is a **carry-over from the superseded revision**,
  and knowing that is what settles it. **When a document contradicts itself, pull the
  previous revision &mdash; the stale side often matches it exactly.**
  The same sheet has a **row-label defect**: the 2025 Table 2 labels its rows
  &quot;(Wall) **ELSPT**&quot; and &quot;(Ceiling) **ELSPTC**&quot;, neither of which is
  a model in the document.
  **CORRECTION, same day, and it is the &quot;a correction can introduce a new error&quot;
  rule firing on this file's own newest entry.** The first version of this note said the
  2021 revision prints the same table with `ELSPK/ELSPKC` and `ELSPST/ELSPSTC` rows
  carrying **identical values**, and called that the licence for quoting a 2025 wall row.
  The next agent was briefed with it, checked, and **it is not true**: the 2021 Table 2
  has **five** tap columns reading 75/79/82/85/87 and separates neither wall from ceiling
  nor 25 from 70.7 VRMS, while the 2025 table runs seven columns and separates both.
  What actually licenses the row is a **third document**: installation sheet
  **`P85967A` (2025)**, whose Table 2A is **explicitly headed for models
  &quot;ELSPK (Speaker), ELSPST (Speaker-Strobe), ELSPST-A (Amber)&quot;** and reproduces
  the 2025 wall values cell for cell. The 2021 revision corroborates only the weaker
  claim &mdash; that speaker and speaker strobe carry identical numbers as separate rows.
  **So the instruction sheet is model-attributed where the datasheet is not**, which is
  the conditional-headline rule pointing across documents for the third time.
  The speaker-equals-speaker-strobe result still stands and is still the **opposite** of
  the System Sensor `SPWL`/`SPSWL` case, where the two differ by 2 dBA at every tap. Two
  brands, opposite behaviour, neither assumable. **And the System Sensor figures have a
  generation boundary this file did not state:** 77/80/83/86 is the **xenon** `SPSWL`;
  `AVDS-62174:A` gives the **LED** line 76/79/82/83 for speaker strobes against
  79/82/85/88 for speakers, a 3 dBA gap. Do not reuse the xenon row on an LED part.
  Also recorded: the filename this file carried for that document is dead, the live one
  is `eaton-eluxa-speaker-and-speaker-strobe-clear-and-amber-lens-td450158en-us.pdf`
  under `/lsmns/eluxa/`, and **`web.eaton.com` returns HTTP 200 with 86,227 bytes of
  `text/html`** for the old name &mdash; another host that pymupdf opens happily and only
  the mime check catches.
- **A private-mode appliance sold as an ordinary one: the class error at the listing
  level rather than the noun level.** `SPSWLED-ALERT` is titled and typed as a speaker
  strobe, and it is one &mdash; but `I56-0024-000` (4/15/2024) &sect;1.4 says in the
  manufacturer's own words that the **amber lens ALERT** models are *&quot;**private
  mode** notification appliances intended to alert **trained personnel**&quot;*, with the
  speaker listed to ANSI/UL 1480 (public mode) and the strobe to **ANSI/UL 1638 (private
  mode)**, where the clear-lens models in the same manual are public mode throughout.
  Nothing in the title is false, so this is not one of the fourteen product-class errors;
  it is a **materially different purchase hiding behind a correct class noun**. Per house
  rules it went in the body and not the title, and to the owner as a possible Merchant
  Center category question.
  Consequence for the copy, worth stating because it is easy to get wrong in the other
  direction: the candela values were published as **switch settings** rather than as a
  rated output, because UL 1638 private mode is not the UL 1971 basis on which a
  clear-lens candela is rated, and neither current document states UL 1971 for any model.
- **EDAM has a SECOND datasheets root, and a document declared gone may simply be in the
  other tree.** The System Sensor 5600 series is not under the known
  `content/dam/hon/hbt-fire/en-us/products/literature-and-specs/datasheets/` &mdash;
  `5600.pdf`, `5624.pdf` and `A05-1004.pdf` all return the 8,047-byte fingerprint there.
  It lives under **`content/dam/honeywell-edam/hbt/en-us/documents/literature-and-specs/datasheets/`**
  as `5600-Series_DataSheet_SPDS3001.pdf`. **Try the second root before concluding a
  Honeywell document has been dropped** &mdash; this file already records `DN-7045` as
  &quot;dropped entirely&quot;, and that conclusion was reached without it.
  (`SPDS300.pdf` in the same directory is byte-for-byte the same text as `SPDS3001.pdf`:
  two filenames, one document, not two revisions.)
- **The page-chrome lifecycle trap has now fired three times, on three pages, and the
  mime check caught the hosts.** `SRK`'s live copy said &quot;(Discontinued)&quot;. Both
  `buildings.honeywell.com` and `systemsensor.com` return **`application/javascript`**
  shells (225 KB and 112 KB), and the only occurrences of the word are the JS UI label
  `&quot;discontinuedText&quot;:&quot;Discontinued&quot;` and a nav entry &mdash; attached
  to nothing, as in the two earlier cases. **Positive evidence pointed the other way:**
  the 23 Feb 2022 outdoor brochure lists SRK, SRK-R and SRK-P as current wall-mount
  strobes. Nothing published; flagged as a lifecycle/feed decision.
  **And the `K` suffix IS decoded here**, unlike `PC2WKLED-P` where no document defined
  it: the same brochure states *&quot;model numbers with a 'K' suffix are outdoor-rated
  products listed to **UL 1638** and rated from &minus;40 &deg;F to 151 &deg;F, with a
  NEMA 4X or 3R rating&quot;*. So the convention is real and documented on System Sensor;
  it simply was not stated in the document family the other part sat in. **A bounded
  negative in one document family says nothing about the convention.**
- **The coordinator offered a cross-family import and the agent refused it. First time
  the wrong-document-family rule has fired PREVENTIVELY.** The briefing offered a System
  Sensor outdoor brochure sentence defining the `K` suffix (*&quot;models with a 'K'
  suffix are outdoor-rated products listed to UL 1638&quot;*) as a possible answer for
  `PC2WKLED`, whose own L-Series documents do not define it. The agent checked
  `AVDS-62173:A`, `I56-0040-000` and `A05-0456`, found that **none defines the letter**,
  observed that every outdoor-table model carries `K` and no indoor-table model does
  &mdash; *an inference from two ordering tables, not a manufacturer statement* &mdash;
  and **put nothing about the letter in the copy.** Recorded because every previous
  instance of this rule in this file is a post-mortem; this is the first where the import
  was offered and declined before it reached a page. A convention documented on one
  product line is not documented on another.
- **A table can carry the WRONG HEADER INSIDE ITSELF, which defeats caption-matching
  entirely.** `AVDS-62173:A` p2: the left table is captioned *&quot;UL/ULC Maximum
  **Strobe** Current Draw&quot;* above it, while its own blue in-table header reads
  *&quot;UL/ULC Maximum **Horn** Current Draw and Sound Output&quot;* &mdash; on a body
  that is candela against current. So the caption above and the header inside disagree,
  and plain extraction additionally emits three captions in an order that attaches each
  to the wrong body. **Render was the only resolution.** Add it to the ladder: caption
  below its table (`9021-60930`), two tables emitted in swapped order (`TD450157EN`), and
  now a header that contradicts its own caption.
- **A part's own name can misdescribe its product class, and the store title will
  inherit the error.** `EOLR-1` was briefed &mdash; by this file's coordinator, as a
  stated fact &mdash; as an end-of-line resistor, and the store title read "System
  Sensor EOLR-1 End-Of-Line". System Sensor manual I56-2185-004 calls it an *epoxy
  encapsulated SPST normally open relay activated by 9 to 40 VDC*. It has **no
  resistance and no wattage at all**. A buyer searching for an EOL resistor was
  landing on a relay. Note the Shopify `type` field said "Relays" and was right while
  the title was wrong: **when a structured field disagrees with the title, that is
  a signal, not noise.**
- **Eleventh incomplete-product case, and it is a SENSING HALF sold as a finished duct
  detector.** `D4S` was titled &quot;Duct Smoke Detector&quot;. System Sensor installation
  instructions **`I56-2967-002R`**, fetched and read directly by the coordinator, say it in
  one sentence: ***&quot;The D4120 duct detector consists of D4P120 Power Board component
  and the D4S Sensor component.&quot;*** The D4S has **four wiring terminals** (Tamper Y,Y
  / +R / &minus;B) and **no power board**, so it carries **none of the alarm-initiation,
  auxiliary or supervisory relay contacts** a complete detector has and cannot work alone;
  it wires to the Sensor 2 terminals of a D4120 or D4P120. The ordering table files it
  under **Accessories** as *&quot;4-wire photoelectric sensor component only&quot;*. **The
  `type` said Duct Detectors and agreed with the wrong title, raising nothing** &mdash; the
  signature for the seventh time. Also corrected: the D4S/D4P120 footprint is
  **7.75 &times; 5 &times; 2.5 in.**, not the D4120's 14.38 &times; 5 &times; 2.5.
- **The CK300-BL pack count is the Honeywell mechanism reproducing on a third document
  family, which is as clean a confirmation as the rule has had.** `SPDS899-01`, `SPDS901`
  and `SPDS-62169-B` all describe the kit as *&quot;Color Kit (includes cover and trim
  ring)&quot;* with **no quantity**, and **each of the three states the bulk packs for
  `B501-WHITE-BP` and `B300-6-BP` in the same table**. Bases numbered, accessory not, three
  times over. Title left exactly as it was; flagged.
- **Three briefing premises wrong in one batch, and the third is a document-family
  correction worth keeping.** (1) `SSM24-10`'s fire-versus-general-signalling split **does
  not exist**: `WFDS74501` gives one Service Use line for the whole series &mdash; fire
  alarm, general signalling *and* burglar alarm &mdash; and `SSM24-10A` is the **ULC
  Canadian** model of the same bell, not a different listing class. (2) `CX-6` is dual-gas
  as briefed, but the family is **six parts**, and **the ETL listing to UL 2075 applies to
  the CX-6 models only** &mdash; the CX-12 line-voltage twins are merely *&quot;designed to
  meet&quot;* it. (3) **This file's rule &quot;prefer the `9021-` document family over the
  `AVDS` one&quot; has a boundary**: `9021-60929` is the right family for `P2WL-P` and is
  **unusable** &mdash; headed *&quot;Wall Horn, Horn Strobe&quot;*, its two ordering blocks
  list **no P-prefix model at all** (render-confirmed) while its own Note 2 references
  &quot;P, S, PC, SC products&quot;. `AVDS865-04` carries the row. **Prefer a family only
  until you have checked that it contains the part.**
  Also from that part, and the reason its 12 V claim survived: *&quot;12/24 Volt&quot;* is
  true **only at 15 and 30 cd** &mdash; at 75 cd and above it is 24 V only. Published with
  the condition rather than dropped.
- **`P2GWKLED-P` settled character by character, and the `K` import was declined a second
  time.** `AVDS-62173:A` p4 reads *&quot;P2GWKLED-P &mdash; 2-Wire, Compact Horn Strobe,
  Wall, White, Plain&quot;* with the note *&quot;All -P models have a plain housing (no
  'FIRE' marking on cover).&quot;* So **G = compact wall, K = outdoor, -P = no FIRE
  lettering**, and the old title, while not false, dropped the two facts that decide the
  purchase. **The sheet names no UL standard anywhere** &mdash; not 464, 1971 or 1638,
  only file numbers &mdash; so the outdoor brochure's &quot;K means UL 1638&quot; sentence
  was offered and **declined for the second time on wrong-document-family grounds.** Two
  preventive refusals now, on two parts, by two agents.
  The caption defect on that page fired exactly as briefed and word coordinates settled
  it: three captions emit in reading order over the left-hand table, and coordinates show
  **x 54&ndash;235 is the strobe-only table and x 276&ndash;540 the horn-only one**, so
  the stray &quot;Horn Current Draw&quot; caption at x=57 belongs to the right-hand body.
  **Strobe-only currents were deliberately not published on a horn strobe.** The
  horn-strobe table below it pairs wall and ceiling candela across ten columns
  (110 WALL/115 CEILING, 135 WALL/150 CEILING, 177 CEILING/185 WALL), which reads as an
  incoherent ladder in plain text; only the WALL columns were quoted.
- **The `SPCWL` supersession finding runs the OTHER way for `SPSCWL`, and the claim still
  does not survive &mdash; which is the mechanism working in both directions.**
  `AVDS-62174:A` (08/29/2024): **`SPSCWL` appears 0 times and `SPSCWLED` 8 times**, while
  on the same page, under a live &quot;L-Series Speaker&quot; heading, the strobe-less
  `SPCWL`, `SPCRL`, `SPWL` and `SPRL` keep their original numbers. One page, one date:
  **the strobe got refreshed and the speaker did not**, which is exactly the reason this
  file gives for why `SPCWL` was NOT replaced.
  **But it is still not manufacturer-stated.** `M23.2SS`'s REPLACES table holds only
  horn strobes and strobes, and the bulletin says in words that speaker strobes
  *&quot;will convert to the new L-Series with LED platform in early 2024&quot;* &mdash;
  pointing at a **future** announcement that five constructed slugs failed to find.
  Claim moved to the body, same handling as `SPSCRLED`; the title gained the class noun
  it completely lacked (it was `Brand PartNumber (Replaced by X)`, the `ZH-MC-W` shape).
  **The specs are the XENON row and that distinction now has a second confirmation.**
  77/80/83/86 dBA at the four taps, coordinate-verified with captions *above* their
  tables and no swap &mdash; which independently reproduces on the **ceiling** pair the
  2 dBA speaker-versus-speaker-strobe gap this file recorded on the **wall** pair.
- **A recorded negative decayed again, and it was one this file states flatly.**
  &quot;EDAM has dropped some Notifier documents entirely &mdash; `DN-7045` 404s under
  both `notifier-us/` and the flat datasheets directory.&quot; It does not:
  **`datasheets/hon-ba-fire-dn-7045.pdf` under the `honeywell-edam` root returns 417,057
  bytes, mime-clean.** The old negative was reached before the `hon-ba-fire-` prefix was
  known. That is the third recorded negative overturned in two days, after Edwards
  first-party and &quot;bogus S3000&quot;. **A negative in this file is only as good as
  the route list that was current when it was written** &mdash; and this file's route
  list has grown five times since.
  Three more route facts from the same batch: a **new EDAM slug form**,
  `<Descriptive>_DataSheet_<DocNum>.pdf` (`L-Series_Spkrs_SpkrStrobes_Ceiling_DataSheet_AVDS866.pdf`),
  which none of the bare, lowercase or underscore shapes reach; **`AVDS-62174` resolves
  under two names 267 bytes apart** (`AVDS-62174-A.pdf` and `BA-Fire-AVDS-62174-A.pdf`);
  and **Potter's category URL recorded here is wrong** &mdash; the working form has no
  `/product/category` segment, it is
  `pottersignal.com/addressable-fire-alarm-system/smoke-detector/<model>`.
  Also: **a search-indexed EDAM URL can 404.** The exact installation-guide URL a search
  returned for manual `52411` 404s at every variant; the document came from a distributor
  mirror, imprint-verified and flagged as mirror-sourced.
- **The type-disagrees-with-a-CORRECT-title case, second instance.** `EPS40-2` is typed
  **Power Supplies** and is a sprinkler pressure supervisory switch &mdash; but its live
  title was **already correct and verbatim System Sensor ordering wording**. That is the
  `ELFHNW-N` shape, not the usual signature where the type agrees with a wrong title and
  raises nothing. Worth stating as a pair now: **the type field disagreeing tells you to
  check, and says nothing about WHICH field is wrong.**
- **A supersession disproved in BOTH directions across four documents, with the innocent
  origin identified &mdash; and the origin is the coexistence trap on a new brand pair.**
  `SS-FIRE-CO`'s title asserted *&quot;(Replaces SK-FIRE-CO-W)&quot;*. Measured: `SK-FIRE-CO`
  occurs **0** times in `SPDS-62170` Rev B and **0** in manual `I56-1409-001`; `SS-FIRE-CO`
  occurs **0** times in the SK-FIRE-CO-W sheet and **0** in `351181`, where `replac`,
  `supersed` and `discontinu` are each 0 as well.
  **The origin: `SPDS-62170` says the SS-Series detectors support current &quot;SK,
  LiteSpeed and SS Protocol&quot; systems &mdash; where `SK` is a PROTOCOL name**, not the
  sibling part number. That is the Siemens *&quot;may be installed on the same SLC&quot;*
  failure on a third brand pair, and the two parts really are near-identical four-sensor
  detectors under different Honeywell brands, which is what makes it plausible. Removed from
  the title and **not asserted in the body either**, since nothing sourced connects them.
- **Twenty-first coordinator premise wrong: the Amerex `810` is a different BRACKET FAMILY,
  not a variant.** The briefing asked what separates it from `818`/`821`/`817`/`818S` and
  carried over the rule learned on the 818 &mdash; *the valve, not the cylinder weight,
  decides*. **That rule is a fact about the STRAP group only.** A 200 dpi render puts `810`
  under **&quot;Heavy-Duty Box-Type Vehicle Brackets&quot;** while 818 and 821 sit under
  **&quot;Vehicle/Marine/Aviation Brackets&quot;**; the parts book's Vehicle/Marine page
  lists 818 and 821 and **does not contain `810` at all**; and `810` has its own hole-pattern
  drawing headed &quot;AMEREX BOX TYPE BRACKETS&quot;. **Box brackets are selected by
  CYLINDER DIAMETER**, a labelled column, and every row containing `810` reads 7.
  So the live &quot;7-inch cylinder&quot; claim was right, and the page had missed that it
  is a **USCG** bracket on nine models. **A decode learned on one family of a brand does not
  cross to another family of the same brand** &mdash; the same shape as the `9021-`/`AVDS`
  boundary and the System Sensor `K` suffix, now on a mechanical accessory.
  Material deliberately not claimed: the sheet's *&quot;(Red Brackets are Galvanized)&quot;*
  note attaches to `810NM`/`809G`/`810G`/`811G`, which render **red**, while the plain `810`
  renders black.
- **The `9021-`/`AVDS` boundary failed for the THIRD time, on a third document.** The
  obvious sheet for a ceiling strobe, `AVDS868`, contains **zero occurrences of
  &quot;LED&quot;** &mdash; it is the xenon ceiling sheet &mdash; and `AVDS-62173:A` is the
  weatherproof one, also zero. Only `AVDS916-01` carries the part. **Prefer a document
  family only until you have grepped it for a word the part number implies**; that check
  costs one grep and has now saved three parts.
  New document defect from it: `AVDS916-01` prints *&quot;SCRLED-P | Strobe, Ceiling,
  **White**, Plain&quot;* on an **SCRLED** number whose own neighbours read Red. The agent
  named the sibling in the closing rather than repeat the colour.
- **A manufacturer-authored document with NO document number, reachable only from a distributor:
  a new shape for the supersession rule, and it was resolved by holding.** The live `BEAM1224S` title
  claimed &quot;(Replaced by OSI-R-SS)&quot;. The announcement is real and is System Sensor's own:
  **February 2019**, imprint verified on a 150 dpi render (swirl logo, `3825 Ohio Avenue, St. Charles,
  IL 60174`), PDF metadata naming an author and `Acrobat PDFMaker 19 for Word` at a Central-time
  offset, and a **MODEL / REPLACES / DESCRIPTION table read by word coordinates** &mdash; header
  columns at x=48/156/322, the row reading `OSI-R-SS | BEAM1224 and BEAM1224S | Conventional Beam
  Detector with Reflector` &mdash; plus the prose *&quot;This new offering directly replaces the
  BEAM1224(S)&quot;*.
  **It still failed two tests the `M23.2SS` precedent passed.** It carries **no document or bulletin
  number of any kind** (searched for every numbering shape this project knows; the only 5-digit run in
  the file is the ZIP code), and the only reachable copy sits on **anixter.com**, a distributor, under
  a `/content/dam/Suppliers/Honeywell/` literature tree. Five constructed EDAM slugs returned the
  8,047-byte fingerprint and no second mirror exists.
  **Claim moved to the body; the title now carries none of it.** The body states it as System Sensor's
  own February 2019 announcement, which is true and sourced, and the owner's file records that **one
  first-party retrieval promotes it back to the title**. Worth stating the principle plainly: this is
  **not** correlated distributor consensus &mdash; a manufacturer-authored REPLACES table is a
  different and much better thing &mdash; but *where a document is served* and *who wrote it* are
  separate questions, and a Merchant Center attribute needs both. Note also a fingerprint drift on the
  way: the `systemsensor.com` JS shell measured **136,651 bytes** here against the ~112 KB on record.

- **A supersession that WAS manufacturer-stated and was sitting in the wrong field, earning
  nothing.** `SCRL`'s replacement by `SCRLED` is in bulletin **M23.2SS**'s MODEL / DESCRIPTION /
  **REPLACES** table outright &mdash; and it was living in the description `<h2>` while the
  Shopify title said nothing. **This file records the opposite case repeatedly** (an unsourced
  claim sitting in a title and needing to move down); this is the first where a *sourced* claim
  was sitting in the body and needed to move **up**. Moved. The adjacent `SCRLED-P`/`SCRL-P` row
  is separately what proves the plain `SCRL` carries FIRE marking.
  **And the document-family grep works in reverse for a legacy part**: `AVDS868-02` contains
  &quot;LED&quot; **zero** times and &quot;xenon&quot; twice, so for a xenon part the *absence*
  of &quot;LED&quot; is the confirmation rather than the disqualification. The recorded
  `AVDS916-01` &quot;SCRLED-P ... White&quot; defect is in the **LED** document and does not
  touch this one.
- **A cross-family import declined for the SIXTH time, and this one was offered with two
  supporting reasons.** The `SPSWKLED-CLR-ALERT` briefing offered the recorded amber
  private-mode finding and the outdoor brochure's *&quot;K means UL 1638&quot;* sentence. The
  agent checked `AVDS-62185-00` (03/17/2025) and declined both: **&quot;private&quot; appears
  zero times and no UL standard number appears anywhere in the sheet** (UL 1638, UL 1971 and
  1480 all zero; page 1 carries file numbers only), and the sheet's own notes define the suffix
  as a **cover marking** &mdash; *&quot;All -P models have a plain housing (no 'FIRE' marking on
  cover.)&quot;*, *&quot;All -ALERT models have 'ALERT' marking on cover.&quot;*, *&quot;All -B
  models have 'FIRE/FEU' marking on cover.&quot;* Outdoor status was taken from the ordering row
  and the sheet's own NEMA 4X / IP56 statements instead.
  **And the same-name trap was live in a web summary.** The right-sounding `AVDS1131` sheet is
  **SpectrAlert Advance, a different generation** &mdash; it contains `SPSWKLED` zero times and
  carries a different candela ladder (15, 15/75, 30, 75, 95, 110, 115, 135, 150, 177, 185), and
  a summary quoted **those** figures for this part. The LED wall ladder is
  15/30/75/95/110/135/185, coordinate-verified. System Sensor separately states that replacing a
  SpectrAlert Advance product **requires a new L-Series with LED back box**, so `SPSWK-CLR-ALERT`
  and `SPSWKLED-CLR-ALERT` are not interchangeable even mechanically.

- **A speaker-only dBA row printed under a speaker-strobe label, caught because a SECOND sheet
  separates them.** `AVDS871-02` p2 prints *&quot;Wall-Mount **SPS** Series 88 85 82 79&quot;*;
  `AVDS867-03` p3 splits the same data into two separately captioned tables, **Speaker Strobe
  77/80/83/86** and **Speaker 79/82/85/88**, captions coordinate-verified *above* their bodies
  with no swap. 77/80/83/86 published. **That independently reproduces the recorded 2 dBA
  speaker-versus-speaker-strobe gap from a third document**, and the xenon generation was
  confirmed positively rather than inferred &mdash; both sheets state the strobe *&quot;shall
  consist of a xenon flash tube&quot;*.
- **A cross-family import declined for the SEVENTH time, and the briefing had offered it as a
  recorded fact.** I pointed the agent at `I56-0024-000`'s private-mode sentence for
  `SPSWL-ALERT`. **That manual is the L-Series with LED family: `SPSWL-ALERT` occurs zero times
  in it and `SPSWLED-ALERT` once.** What the agent published instead comes from the part's own
  family &mdash; `AVDS871-02` p1 puts amber-lens ALERT strobes *and speaker strobes* under
  **ANSI/UL 1638 general signalling**, with candela published as **switch settings**. Same
  conclusion, sourced from the right generation.
