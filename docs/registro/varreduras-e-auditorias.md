<!-- Registro de casos do projeto TFAS. Movido VERBATIM de CLAUDE.md em 23 Sep 2026; nada foi reescrito. Nao e carregado automaticamente: leia sob demanda. E cronologico: entradas posteriores corrigem anteriores; em caso de conflito vale a mais recente e o nucleo em CLAUDE.md. -->

# varreduras-e-auditorias

- **The dropped-decimal trap:** a title copied from the adjacent catalogue row
  loses a decimal point and asserts a value ten times too large. Edwards lists
  `EOL-4.7` (4.7 kΩ) and `EOL-47` (47 kΩ) on consecutive rows; the store's
  EOL-4.7 page carried the EOL-47 text while separately stocking the real EOL-47.
  A full scan of the 19,440 active products found exactly one such case, so the
  pattern is closed catalogue-wide, but it recurs whenever a new row is copied.
- **Every keyword scan over this catalogue has over-fired by one to two orders of
  magnitude. Assume the next one will too, until a mechanism is stated.** The tally:
  product types 922 findings &rarr; 11 real; feed titles 1,325 &rarr; 109; cross-page
  consistency 59 &rarr; 0; punctuation-stripped titles 589 &rarr; 19. The fix is the
  same every time: **do not scan for a shape, scan for a mechanism.** "Title ends in a
  bare number" is a shape and catches pack counts, voltages and part numbers. "Slash or
  hyphen stripped, so `FM/CSA/ATEX/IECEx` reads `FMCSAATEXIECEx` and `0-20 mA` reads
  `020 mA`" is a mechanism, and it lands on 19 products with almost no false positives.
  The punctuation case also shows **when to stop**: 19 products carrying 887
  impressions is 47 each, below the old list's abandoned tail at 29, so it was recorded
  and **not applied**. And the rows were left marked unverified on purpose &mdash;
  reading `34 NPT` as `3/4 NPT` is a claim about a thread size and needs a manufacturer
  document, the same bar as any other spec. A pattern is a reason to check, never a
  licence to rewrite.
- **The first scan on this catalogue that did NOT over-fire, and the reason is exactly
  the stated principle.** Run 21 Sep 2026: group active products by vendor plus a
  part-number stem, keep families of three or more, and flag a family whose members
  **disagree with each other on the `type` field**. 41 families qualified, 18 members
  were flagged, 12 were confirmed live, and **8 were real defects** &mdash; roughly 67%
  precision against 1&ndash;8% for every keyword scan before it. It also
  **independently rediscovered `P2WLED-P`**, a defect already confirmed and sitting in
  the owner's file, which is about the best validation a new scan can offer.
  The difference is not sophistication, it is that &quot;a family contradicts itself&quot;
  is a **mechanism**: a store cannot be right when two members of one product line carry
  different class nouns, so every hit is at minimum a real question. Compare
  &quot;`type` contains a suspicious word&quot;, which is a shape and fires on every
  correct product too. The catch found: `FST-951-IV` is titled *Plug-In **Thermal**
  Detector* and typed **Smoke Detectors**; `SCRLED-BP10` is a strobe typed
  **Accessories**; `SPSCWLED-P`, `SPSWLED-P` and `ELMTSR-A` each drop the speaker or
  horn from a combination appliance; `P2RLED-LF` and `P2WLED-LF` are typed Strobes
  while their own sibling `PC2RLED-LF` is correctly typed Sounder Strobes.
  **Two limits worth stating so the next person does not overclaim it.** First, the
  stemming is conservative &mdash; only 41 families of 16,031 products qualified &mdash;
  so this is a floor on the defect count, not a census. Second, and more important,
  **the outlier is not always the wrong member.** In the low-frequency families the
  minority typed *Sounder Strobes* was the correct one and the majority typed *Horn
  Strobes* was the loose one, because an LF device is a sounder by NFPA 72's 520 Hz
  requirement and not a horn. The scan reports **that a family disagrees**, never
  **which member is wrong**; deciding that still takes reading the part.
- **Widening that scan taught the same lesson a fourth time, and then a new one.**
  Loosening the stem to &quot;drop the last hyphen segment&quot; took the flag count
  from 18 to **203** &mdash; the over-firing signature, immediately. The fix was a
  mechanism, not a threshold: **a short trailing segment is a variant suffix, a long
  one is model identity**, so only drop a final segment of two characters or fewer.
  That gives 106 families and **52 outliers**, and inspecting all 52 rather than
  reporting the number is what made it useful.
  **The new lesson is a reframing, and it matters more than the count. In a large
  share of these families the MAJORITY is wrong and the minority is right** &mdash;
  `ELMTSR-N` and `ELMTSW-NA` are correctly typed Horn Strobes inside a family typed
  Strobes; `P2WLED-SP` likewise; `VSR-CR-3` is correctly typed Switches in a family
  typed &quot;Fire Alarms&quot;; `AFAWS-BX` is correctly typed Backboxes in a family
  typed Doors; and **`HONBDA-7S27B-IB-18` is correctly typed BDA inside the family
  typed Annunciators**, which is the already-confirmed `-IB-10` defect found from the
  other direction. So &quot;outlier&quot; is the wrong word for what this scan
  returns: **it finds a broken family by its one healthy member.** Counting outliers
  therefore *understates* the defect, which is the opposite of every previous scan on
  this catalogue and worth remembering before anyone sizes the work from the flag
  count. A good part of the rest are mere taxonomy-granularity differences &mdash;
  Kits against Bezel Kits, Relays against Relay Modules, Surface Boxes against
  Backboxes &mdash; real inconsistencies but not worth a write.
- **The pack-count census itself matched a phrase, not a mechanism, and missed three
  titles.** The 27 were found by the wording *&quot;Bulk Pack with N Units&quot;*;
  `FST-951-BP`, `FSP-951-BP` and `FSP-951R-BP` read *&quot;White Bulk Pack 10&quot;*
  and were invisible to it. Re-run as a mechanism &mdash; *a `-BP` SKU whose title puts
  an integer next to a pack word in any order* &mdash; over all **66** `-BP` SKUs, it
  returns **28 asserting titles** with almost no false positives. **30 rows now, 25 of
  them convention-only, $1,403,392.** Note the shape: the over-firing rule
  (&quot;scan for a mechanism, not a shape&quot;) has an **under-firing twin**, and a
  phrase match is the purest example of it. A scan that returns a suspiciously tidy
  number deserves the same scepticism as one that returns 1,325.
- **Never audit for defects against `catalogo_full.json`. It is a snapshot, and a
  snapshot finds defects that were fixed hours ago.** A title scan over the 264
  ad-labelled products flagged five non-ASCII titles and, worse, appeared to show that
  the `OH921` supersession correction recorded in this file had been reverted. **All of
  them were already correct in the live store**; the snapshot predated the fixes by a
  few hours. The scan is still fine for finding *enrichment candidates* &mdash; title
  length, missing class noun, description size do not flip back &mdash; but **every
  defect finding must be confirmed live before it is reported or acted on.** This is
  the same shape as the entity audit that flagged 655 of 663 pages: measuring the wrong
  artefact, confidently.
- **A proposed scan died on its own worked example, before it was built. Worth keeping
  because the reasoning failed in the way this file warns about, one paragraph after
  citing that warning.** The coordinator saw that `A050-9101`'s page described a
  &quot;**2050FS**&quot; panel and never named `A050-9101`, called it a third instance of
  the wrong-product shape after `4-NET-SM` and `PAD200-DD`, and proposed a catalogue-wide
  scan for **descriptions whose body never contains their own SKU**.
  **`A050-9101` IS the 2050FS.** Autocall `AC4098-0060` Rev. 4, 05/2025, Table 1, read
  directly by the coordinator after the agent contradicted the briefing: *&quot;A050-9101
  | Red | 2050FS FACU with 4 x 40 LCD display, single MX addressable initiating loop with
  50 devices maximum and 2 conventional NAC circuits | 175 mA | 215 mA&quot;*. The
  catalogue number appears **once** in its own datasheet and `2050FS` appears **23
  times**, because the ordering number and the marketing model name are different strings
  and the datasheet is written around the latter. The live copy was substantively right.
  **So the scan is a shape, not a mechanism, and would have over-fired exactly as every
  keyword scan on this catalogue has.** &quot;The body does not contain the SKU&quot;
  fires on every page correctly written around a model name &mdash; which is most panel,
  appliance and series pages in the store. Sharpening it to &quot;the body names a
  *different* model number&quot; does not save it either: this page names 2050FS and is
  correct. What separates `4-NET-SM` from `A050-9101` is whether the named thing **is the
  same product**, and no scan can know that. **Do not build it.**
  The two real cases stand on their own and were both found by an agent reading the page
  against the ordering table, which is the method this file already records as the one
  that works for cross-references.
- **An import truncated titles at 150 characters, and the cliff in the histogram proves
  it. Second mechanism-based scan on this catalogue that did not over-fire, and the
  cleanest yet.** Run 22 Sep 2026 against a live pull while agents were working.
  **The mechanism: a title with unbalanced parentheses cannot be correct.** Not a shape,
  not a keyword &mdash; there is no legitimate title that opens a bracket and never closes
  it. **102 of 16,031 titles qualify, and inspecting all 102 found no false positive**,
  against 1&ndash;8% precision for every keyword scan in this file and 67% for the
  family-disagreement scan. **Precision only &mdash; its recall was measured seven
  batches later and is about 25&ndash;30%; see the re-measurement in the batch-25 sweep.**
  They split into two different defects:
  - **79 with an unclosed `(`** &mdash; cut off mid-phrase: *&quot;&hellip;Temporal 4
    Capabilities Plain (no&quot;*, *&quot;&hellip;(Availability Limited to Quantity&quot;*,
    *&quot;&hellip;(Notifier Marketing PN:&quot;*.
  - **23 with a stray `)`** &mdash; a different mechanism, where the opener and part of its
    content were lost: `Potter PE-LFHNW 4871013) Low Frequency Sounder`,
    `Resideo 900748 BP10) Seal Ring`, `Simplex 4098-9784 discountinued)true Alarm Base`.
  **The proof of the cause is the length histogram, not the sample.** Across the newest
  product-id blocks, title lengths climb to a plateau at 145&ndash;149 characters
  (107, 97, 88, 88, 76) and then go to **17 at exactly 150 and ZERO at 151 and above**.
  A natural distribution does not end in a cliff. **Titles in the new blocks land at
  145&ndash;150 at 5.51%, against 0.51% in the older blocks** &mdash; an 11x difference,
  and every one of the 79 broken titles sits in a new block, none in an old one. This is
  the same shape as the Aiphone non-ASCII finding: **the defect clusters in one import,
  so it is fixable at the source rather than one product at a time.**
  **The 79 are the detectable tail, not the whole problem.** Roughly **456 new-block
  titles sit in the truncation band**; the 79 are merely the ones whose cut happened to
  fall inside a bracket. The rest were cut too and end at a word boundary, so they look
  fine and are invisible to any scan.
  **Not fixed, and deliberately so.** The truncated text is *missing*, so reconstructing
  79 endings would be inventing them &mdash; the one thing this project never does. This
  is a data question for the owner: re-import the affected block with the full titles.
  Ids saved in `/tmp/tfas/TITULOS_TRUNCADOS_ids.json`. Titles are Merchant Center feed
  attributes, so a title ending mid-word costs money in two channels.
  **Two mechanism flaws found and fixed while building this scan, worth keeping because
  they are the general failure mode of such rules.** A first pass flagged
  &quot;comma with no following space&quot; as an ERP field separator &mdash; it fires on
  every **thousands separator** (`1,000'`, `4,064 Points`, `3,000 Hz`), including a title
  written the same day. And it flagged `EA` as an ERP abbreviation &mdash; it fires inside
  **model numbers** (`IX-EA`, `ATJ-EA`, `GWBDA-EA-AU-MDA`). Both fixes were mechanisms,
  not thresholds: require a non-digit after the comma, and require the token not be inside
  a hyphenated run.
- **A scan suggested by an agent, run, and mostly negative &mdash; recorded because the
  negative is the useful part.** An agent noticed `GCAVWF-CVR` is a replacement cover and
  asked whether any `-CVR` SKU is merchandised as a device. **Ten `-CVR` titles exist and
  all ten say &quot;Cover&quot;**, so the dangerous form &mdash; a bare cover sold as an
  appliance &mdash; does not occur. Two carry the wrong `type`: `G4AVRF-CVR` is typed
  **Horn Strobes** and `G4VRF-CVR` **Strobes**, where the other eight are typed Covers.
  Titles right, structured field wrong, which is the milder half of the usual signature.
- **Verification sweep at batch 29 (1,091 pages, 22 Sep 2026): clean a FIFTH time, and the
  non-ASCII count is still falling on its own.** One bulk query, 16,031 active products.
  All **1,076** tracked ids present in the active catalogue &mdash; **zero missing**, with
  the in-flight batch excluded before reading the number, as the method note requires.
  Exactly **four** pages under 400 visible characters and all four are the deliberate
  skips: `SM7100-L8` (22 chars), `90521` (30), `BDA-TP10-L2` (74) and `BDA-NMP01250` (96).
  Non-ASCII titles: **49 of 16,031**, down 56 &rarr; 50 &rarr; 49 across batches 14, 24 and
  29, and **every one is still `&reg;` (24), `&deg;` (23) or `&trade;` (5), zero outside
  that set**. **Zero titles contain a literal HTML entity.** The unbalanced-parenthesis
  count is **102, unchanged** &mdash; expected, because those are truncated titles whose
  text is missing and which this project deliberately does not reconstruct.
  **A new use for the same pull, and it is worth making routine: validate the photo CSVs
  against it.** A Matrixify image import keys on `Handle`, so a handle that has changed
  since the harvest fails silently or lands nowhere. All **643** rows across the four photo
  CSVs were checked against the live handle list: **zero invalid**. That costs one pass
  over a file already on disk and it protects an import the owner runs by hand.
- **A narrow, document-grounded scan for the releasing-gear defect, and three of five
  families came back clean.** Releasing equipment merchandised as ordinary fire equipment
  has fired four times here, so the live catalogue was checked against the part-number
  families whose documents this project has **actually read**: `RP-2002*`, `IPA-*`,
  `4099-9015`, `2099-91*`, `RMS-1T*`. **`RP-2002` and `RP-2002E` both now say &quot;Agent
  Release Control Panel&quot;** &mdash; the correction propagated to the 240 V sibling
  without anyone doing it separately, which is the first time a fix here has been observed
  to carry across a family. `IPA-100`/`IPA-4000` and `4099-9015` are clean too. **And the
  seven `2099-91xx` stations that do NOT say releasing are almost certainly right**,
  because `2099-` is the non-coded manual station line with releasing as one sheet inside
  it &mdash; the exception a coordinator summary once dropped, now protecting seven titles
  from a wrong flag.
  **`RMS-1T` is the outlier and it is incoherent across six members**: `-KL` is a
  Pre-Action Release station while `-WP` is a plain &quot;Single Action&quot; one on the
  same stem; `-WP YELLOW` says **Dual-action** where `-WP` says Single, and yellow is the
  release-station colour convention; `-KO` sits under vendor **Kidde** where all five
  siblings are Potter; `-KO` is typed **Keys** and titled a Station while `-WP-KL` is typed
  a Pull Station and titled a **Key**, so one of those two pairs is inverted; `-WP-LP` has
  **no class noun at all**; and `-KL`'s title carries a stray `)` from the truncated
  import. Queued in `pending_fixes.md` to be **pair-split across two agents**, which has
  paid three times here.
- **Verification sweep at batch 25 (1,004 pages, 22 Sep 2026): clean for the fourth
  time running, and the non-ASCII title count is now FALLING.** All 1,004 tracked ids
  present in the active catalogue, **zero missing**. Exactly **four** pages under 400
  visible characters and all four are the deliberate skips (`SM7100-L8`, `90521`,
  `BDA-TP10-L2`, `BDA-NMP01250`). The ASCII title check: **50 of 16,031**, down from 56
  at batches 14 and 19, and **every one is still `&deg;`, `&reg;` or `&trade;`** &mdash;
  25, 23 and 5, zero outside that set. **The drop is the rule working twice over:** six
  of those 56 came through the queue and were rewritten in ASCII, so the count falls as
  the pipeline touches them, and no new one has been introduced across roughly 330
  titles written since batch 14. Cost: one bulk query, 16,031 products, about 40 seconds.
- **The truncation scan re-measured on a second pull, seven batches later, and the
  numbers hold &mdash; but the recall estimate is now measured rather than argued.**
  102 unbalanced-parenthesis titles, unchanged. The 150-character ceiling is confirmed
  catalogue-wide: **749 titles sit at 140&ndash;150, exactly 0 at 151&ndash;155**, and
  the six above 150 are Resideo and Aiphone products from a different import entirely.
  Against a background of ~85&ndash;105 titles per 5-character band from 125 to 139, the
  140&ndash;149 bands hold **238 and 493** &mdash; a 3.6x pile-up against the cap.
  A random sample of 30 from the band, read one by one, found **roughly half clearly cut
  mid-sentence** (*&quot;&hellip;Space for Up to 12Ah Batteries. H:355mm W:436mm&quot;*,
  *&quot;&hellip;Has Built in Class&quot;*, *&quot;&hellip;Replacement Detector Only, Does
  NOT&quot;*). So the real count is **300&ndash;400, and the parenthesis scan's recall is
  about 25&ndash;30% at 100% precision.** Worth stating plainly: **that scan is recorded
  in this file as the cleanest ever run here, and it is &mdash; on precision. Its recall
  was never measured and is poor.** A scan is two numbers, and this project has only ever
  reported one of them.
  **The upstream cause is visible in the same band: 350 of the 749 contain a sentence
  break.** Marketing prose was written into the `title` field, which is why titles reach
  a 150-character cap at all. Fixing the cap without fixing that produces 749 long titles
  instead of 749 truncated ones.
- **The no-name title census under-counted, and the mechanism that fixed it also found a
  second defect nobody had named.** The recorded census found **22** nameless Mircom
  titles; stripping the vendor string *and* the SKU and asking whether anything remained
  gives **71 of 380 (18.7%)**. And **57 of those 71 repeat the brand and part number
  twice** &mdash; the literal title is `Mircom FX-6000MNS-CH Mircom FX-6000MNS-CH`. That
  is a **distinct import defect from truncation and from namelessness**, it is
  mechanically detectable in one line, and a v2b33 agent independently found the same
  shape on `PE-STWC`. Worth a catalogue-wide scan.
- **Verification sweep at batch 35 (1,218 pages, 22 Sep 2026): clean a SIXTH time
  &mdash; and the sweep's own raw number was wrong for a new reason, which is the
  finding.** One bulk query, 16,031 active products, under a minute. **All 1,195 tracked
  ids present in the active catalogue, zero missing**, with the in-flight v2b36 excluded
  before reading the number as the method note requires.
  **But the thin-page count came back as 45 where every previous sweep returned 4**, and
  the cause is not a failure: **the title-only workstream creates products that are
  TRACKED without being ENRICHED.** Those 41 products got a corrected title and their
  description was never written, by design &mdash; they came from the no-product-name
  census, not from the impressions queue. Split properly: **1,154 enrichment pages, of
  which exactly 4 sit under 400 visible characters, and all four are the deliberate
  skips** (`SM7100-L8` 22 chars, `90521` 30, `BDA-TP10-L2` 74, `BDA-NMP01250` 96). The 41
  title-only products are 41 of 41 under 400, exactly as expected.
  **That is the same shape as the recorded &quot;exclude the in-flight batch&quot; note,
  on an axis that did not exist when it was written.** The sweep measures *&quot;did a
  page this project claims to have written actually get written&quot;*, and a second
  workstream that deliberately writes only one field breaks the equation between
  &quot;tracked&quot; and &quot;should have a body&quot;. **Define what the denominator
  means before reading the number** &mdash; the generalised version of the rule this file
  has now had to apply to coverage rates, tail statistics and scan precision.
  Other checks on the same pull: **non-ASCII titles 49 of 16,031, every one `&reg;` (24),
  `&deg;` (23) or `&trade;` (5), zero outside that set** &mdash; unchanged from batch 29
  across roughly 90 further titles written since. **Zero titles contain a literal HTML
  entity.** Unbalanced parentheses **102, unchanged**, which is expected: those are
  truncated titles whose text is missing and which this project deliberately does not
  reconstruct.
  **And the title-only products are now a small, honest queue of their own:** 41 pages
  with a good title and a body under 400 characters. They are not queue-worthy by score
  &mdash; the whole 313-product no-name census carries only 2,983 impressions &mdash; so
  they should be picked up opportunistically rather than promoted ahead of
  `ranked_v2_byscore.json`.

- **Verification sweep at batch 40 (1,215 pages, 22 Sep 2026): clean a SEVENTH time &mdash; and the
  denominator was wrong for a SECOND new reason, which is the finding.** One bulk query, 16,031
  active products. The raw count of thin pages came back as **110** where every sweep before batch 35
  returned 4. Split properly it is **4**, and the extra 99 are not failures at all: they are the
  **deliberately abandoned tail of the retired old queue**. Directories `b34`&ndash;`b39` hold
  `slice.json` files that were built and then dropped when `ranked.json` was retired &mdash; sliced,
  never researched, never published, and correctly excluded from the queue ever since. A sweep that
  defines &quot;tracked&quot; as *anything with a slice file* reads 99 deliberate abandonments as 99
  silent failures.
  **That is the batch-35 lesson on a new axis, and it should have been anticipated.** Batch 35 found
  that the title-only workstream creates products that are *tracked without being enriched*; this
  finds that a *retired queue* leaves slices that were tracked without ever being started. Both are
  the same defect: **the sweep measures &quot;did a page this project claims to have written actually
  get written&quot;, and any artefact that records intent rather than work breaks the equation.**
  The correct denominator is **the v2bNN slices plus the old-list batches actually published**
  (`b01`&ndash;`b33`), minus the in-flight batch. On it: **1,215 ids, zero missing**, and exactly
  **four** pages under 400 visible characters &mdash; the four deliberate skips (`SM7100-L8` 22 chars,
  `90521` 30, `BDA-TP10-L2` 73, `BDA-NMP01250` 95). Seven more read as thin in the snapshot and were
  **published minutes after the pull**; all seven confirmed live afterwards by direct query, which is
  the snapshot rule firing on a file one hour old.
  Other checks on the same pull: **non-ASCII titles 47 of 16,031**, every one `&deg;` (23), `&reg;`
  (22) or `&trade;` (5), **zero outside that set** &mdash; 56 &rarr; 50 &rarr; 49 &rarr; 47 across
  batches 14, 24, 29 and 40, still falling on its own as the queue rewrites titles for substantive
  reasons. **Zero titles contain a literal HTML entity.** Unbalanced parentheses **102, unchanged**,
  as expected for truncated titles this project deliberately does not reconstruct.

- **The nameless-title census re-run: 180, not 98 &mdash; and the brand-duplication fix CREATED some
  of them.** This file's running figure was &quot;98 remain of the original 313&quot;, with a caveat
  already attached that the 57 products which became bare `Brand PartNumber` *after* the dedup were
  not in that file. Re-run properly against a live pull &mdash; strip the vendor string and the real
  `sku` field and ask whether anything is left &mdash; the answer is **180**: Mircom 65, Power Sonic
  47, Rath 19, Kidde Fenwal 10, then a tail.
  **Mircom is the whole mechanism in one vendor.** Its titles read `Mircom FX-6000MNS-CH Mircom
  FX-6000MNS-CH`; the fix collapsed them to `Mircom FX-6000MNS-CH`, which is *correct* and is also a
  title with no product name in it. **Fixing one import defect exposed another that was hiding
  underneath it**, and a count of the second defect taken before the first was fixed was necessarily
  too low.
  **So the rule is: a census is re-run, never decremented.** Subtracting what you fixed from an old
  census assumes the population is static, and every fix in this project that rewrites a title moves
  products into and out of these classes. Current list in `/tmp/tfas/TITULOS_SEM_NOME_v2.json`.

- **A fifth mechanism-based scan, clean on its first run: a page that spells its own part number two
  different ways.** Mechanism: **a title token of six or more alphanumerics that the description
  writes WITH a separator** &mdash; the product contradicting itself about punctuation, which cannot
  be correct in either direction. **21 hits, no false positives**: Simplex `49049176` against
  `4904-9176`, Det-Tronics `006300001` against `006300-001` (six of them), Apollo `ORBOP42003MAR`
  against `ORB-OP-42003-MAR`, RFS `5556000MHz` against `555-6000MHz`, BRK `SMCO100VAC` against
  `SMCO100V-AC`. That is the punctuation-stripping import found **by mechanism** for the first time,
  after six instances found one page at a time by agents reading. List in
  `/tmp/tfas/PONTUACAO_autocontradicao.json`; **not applied**, because choosing which spelling is
  right is a claim about a part number and needs the manufacturer, exactly as `34 NPT` did.

- **Verification sweep at batch 43 (22 Sep 2026): clean, and the denominator question is now
  routine rather than a surprise.** One bulk pull, 16,031 active products. On the audited
  enrichment population &mdash; v2 slices plus the old-list batches actually published, minus
  the in-flight batch **and minus the 177 title-only products, which are tracked-but-not-enriched
  by design** &mdash; **zero missing** and exactly **four** pages under 400 visible characters,
  all four the deliberate skips (`SM7100-L8` 22 chars, `90521` 30, `BDA-TP10-L2` 73,
  `BDA-NMP01250` 95).
  Catalogue-wide on the same pull: **47 non-ASCII titles, every one `&deg;` (23), `&reg;` (22)
  or `&trade;` (5), zero outside that set** &mdash; 56 &rarr; 50 &rarr; 49 &rarr; 47 across
  batches 14, 24, 29 and 43, still falling on its own. **Zero** titles carrying a literal HTML
  entity. **Zero** titles repeating brand and SKU as separate tokens, so the 75-title fix has
  held. Unbalanced parentheses **102, unchanged**, as expected for truncated titles this
  project deliberately does not reconstruct.
  **Three sweeps in a row have now had a denominator correction rather than a finding**
  (batch 35 title-only, batch 40 abandoned-tail slices, batch 43 both at once). That is the
  useful shape to expect: **the sweep's job has become defining its own population correctly,
  and the page-level result has been clean seven times running.**

- **The nameless-title census re-run live: 94, down from 180**, after title lots 7&ndash;17.
  Power Sonic 35, Mircom 30, Rath 9, TCS Basys 5, then a tail of ones and twos. Recorded
  because this file's own rule is *a census is re-run, never decremented* &mdash; and the
  re-run also picks up the six titles above, which become countable only once their
  duplication is gone. Other checks on the same 16,031-product pull: **non-ASCII titles 47,
  every one `&deg;` (23), `&reg;` (22) or `&trade;` (5), zero outside that set**; **zero**
  titles carrying a literal HTML entity; unbalanced parentheses **102, unchanged**. List in
  `/tmp/tfas/TITULOS_SEM_NOME_v3.json`.

- **dHash at Hamming 0 over-fires on tall narrow objects of identical silhouette, so even the
  strict setting needs the look pass.** This file recommends stopping at Hamming 0 precisely
  because &le;10 returns 280 mostly-correct pairs. At **0** it still collided three times here:
  two SFP transceiver pairs differing only in label text, and **`4-24L18S-E` against
  `4-24L24S-E`, which are visibly different** &mdash; 18 larger switches against 24 one-per-LED.
  Hamming 0 proves *identical bytes after re-encoding*, which is a mechanism; it does not prove
  the products differ, and on a family of near-identical faceplates it does not even prove the
  images are the same. **The hash narrows the question; only looking answers it.**
- **THE SWEEP HAS BEEN AUDITING 71% OF THE PUBLISHED WORK AND NEVER SAID SO. Fourth
  denominator correction in four sweeps, and the first where the missing population is
  REAL WORK rather than an artefact of intent.** Re-run 23 Sep 2026 on a fresh live pull:
  building the tracked set from `<dir>/slice.json` as every previous sweep has done gives
  **935 ids**, against a recorded progress figure of 1,311. The gap is not a discrepancy to
  reconcile &mdash; **376 published old-list pages have no slice file on disk at all.** Only
  16 `bNN` directories retain one (b18&ndash;b39), so b01&ndash;b17 and the rest were
  published before that convention or were cleaned, and the sweep has silently excluded
  them since it was written.
  **The fix was available the whole time and is one join:** `/tmp/tfas/BASELINE_555_publicadas.csv`
  is the durable per-id record of the old list, kept for the 30- and 60-day measurement.
  Folding it in gives **935 + 555 = 1,311 exactly**, which reconciles against the progress
  figure for the first time.
  **On the correct population: zero missing from the active catalogue, and exactly four
  pages under 400 visible characters** &mdash; `SM7100-L8` (22 chars), `90521` (30),
  `BDA-TP10-L2` (74), `BDA-NMP01250` (96), the four deliberate skips. Clean an **eighth**
  time.
  **The batch-40 note found slices recording INTENT without work; this is the inverse,
  work with no artefact recording it** &mdash; and it is worse, because a sweep that cannot
  see a page cannot report it missing. **A verification sweep's first job is to prove its
  denominator equals what the project claims to have done**, and until today this one never
  did that arithmetic.
  Other checks on the same 16,031-product pull: **non-ASCII titles 47, every one `&deg;`
  (23), `&reg;` (22) or `&trade;` (5), zero outside that set** &mdash; unchanged from batch
  43. **Zero** titles carrying a literal HTML entity. Unbalanced parentheses **102,
  unchanged**. **Zero** titles repeating brand and SKU case-insensitively, so the six-title
  case-insensitive fix has held. The nameless-title census re-run live is **37**, down from
  94 after five more title lots &mdash; re-run, never decremented, per the recorded rule.

- **A SIXTH MECHANISM-BASED SCAN, RUN BECAUSE THE PREVIOUS ENTRY SAID IT WAS WORTH RUNNING, AND
  IT FOUND FOUR PRODUCTS LISTED TWICE AT TWO PRICES &mdash; SEPARATED BY AN INVISIBLE
  CHARACTER.** The `P32-BB` duplicate-title finding implied a scan nobody had run: **do two SKUs
  in one vendor carry the same title?** Six groups, 14 products, all inside one vendor. But the
  title scan was the *weaker* of the two it suggested. The sharper one is on the SKU:
  **two SKUs that differ only in whitespace cannot be two products.**
  **Four collisions, and the character is `U+00A0`, a non-breaking space, not an ordinary one.**
  `PRETROFIT` / `PRETROFIT&#160;`, `PSOLAR` / `PSOLAR&#160;`, `1-06-118537-001` /
  `1-06-118537-001&#160;`, `1-B7482-201` / `1-B7482-201&#160;`. Two more SKUs carry a trailing
  `U+00A0` with no twin (`6-01-7171-1129` has **two**), so six SKUs in 16,031 are affected and
  **zero SKUs are exactly duplicated between products** &mdash; every collision is explained by
  the invisible character alone.
  **The creation timestamps give the mechanism outright, and it is two different failures with
  one cause.** The Kidde Fenwal pairs were written **three seconds apart in one import**
  (23:08:23 and 23:08:26; 23:13:38 and 23:13:40 on 17 Jul 2026), so the source file carried the
  same part twice, once with the character. The Napco pairs are the other shape: the clean
  product dates from **January 2025** and its twin from **that same July 2026 import**, which
  **failed to match the existing product because the identifier does not equal itself** and
  created a duplicate instead of updating it.
  **The cost is visible in the prices**: $72.60 against $82.70, $44.00 against $38.15,
  $1,720.80 against $1,998.85, $3,738.35 against $4,830.35 &mdash; the last a $1,092 spread
  between two listings whose titles, types and descriptions are **byte-identical**. A buyer
  searching the store gets two results; Merchant Center gets two offers for one part number.
  **This is the `868STRC-AQ` defect one field over, and that is the general lesson.** This file
  records a title whose part number carried a double-encoded zero-width space *&quot;so the part
  number did not match itself&quot;*, and an Aiphone title with a non-breaking hyphen inside the
  model number. **The catalogue-wide non-ASCII audit was only ever run on TITLES.** The same
  corruption is in the `sku` field, from the same class of import, and nobody looked &mdash;
  because the scan was defined by the field it was first found in rather than by the mechanism.
  **Run the non-ASCII check on every identifier field, not just the one where it was noticed.**
  Nothing was changed: a SKU is a Merchant Center identifier and choosing which of two live
  listings survives is the owner's. Seven rows appended.
- **THE FOLLOW-THROUGH FOUND THE SHARPEST CASE OF ALL, AND IT IS THE SAME PRODUCT THIS FILE
  ALREADY THINKS IT FIXED.** The entry above ends *&quot;run the non-ASCII check on every
  identifier field, not just the one where it was noticed.&quot;* Run immediately, over
  `sku`, `vendor`, `productType` and `title` on all 16,031 active products:
  **`vendor` 0, `productType` 0, `title` 46 (23 `&deg;`, 21 `&reg;`, 5 `&trade;`, zero outside
  that set), `sku` EIGHT.** Six are the trailing `U+00A0` above. **The other two have no twin,
  so the collision scan could not see them**, and one of them is this:
  **`868STRC-AQ`'s SKU is, live today, `868STRC-AQ` followed by `U+00E2 U+20AC U+2039`.** That
  is byte-for-byte the double-encoded zero-width space this file records as having been found in
  **the TITLE of this exact product** and normalised on 21 Sep 2026. Verified live: the title is
  clean ASCII now, the handle still carries its own leaked form (`edwards-868strc-aqa`, left
  alone on purpose to avoid breaking the URL), and **the SKU was never looked at.**
  **Three fields on one product: one fixed, one deliberately left, one never checked &mdash; and
  the one never checked is the Merchant Center identifier.** The recorded note even *says* the
  corruption &quot;had already leaked into the handle&quot;, which shows the author knew it
  spread across fields and still did not enumerate them. **A defect found in one field is a
  question about every field of that record.**
  The eighth is Eaton's `DB4BULGD870N2CPCR&#160; C:1.5` &mdash; a `U+00A0` and then an ordinary
  space before a configuration token welded onto the catalogue number.
  **And the negative control in the same run is what keeps the mechanism honest: 377 SKUs
  contain an ordinary internal space and nearly all are legitimate** (`PS-1270 F2`,
  `OX SENSOR`, `STI EP141207-T`). &quot;A SKU contains a space&quot; is a **shape** and
  over-fires; &quot;two SKUs differ only in whitespace&quot; and &quot;a SKU contains a
  character outside ASCII&quot; are **mechanisms** and return 4 and 8 with no false positives.

- **THE NAMELESS-TITLE QUEUE HAS A FLOOR, AND IT IS NOT ZERO. Fifth denominator correction on
  this project, and a new kind.** The census was re-run live rather than decremented, as the
  recorded rule requires: **37 titles remain that are brand plus part number and nothing else**,
  matching the previous count exactly. But the number that matters is the split, which nobody
  had taken:

  | | n | what it is |
  |---|---|---|
  | never sliced | **6** | real work: 4 TCS Basys, 1 Viking, 1 Westell |
  | in the lot the owner paused | **11** | real work, deliberately stopped |
  | **deliberate nulls** | **20** | already researched and correctly declined |

  **So 313 &rarr; 180 &rarr; 94 &rarr; 37 reads as progress toward zero and the floor is about
  twenty.** Those twenty are products an agent looked at and refused to title, each for a stated
  reason that research cannot lift: `DHS40-HG-SCH-1-A` behind a WAF with every FCC route blocked,
  `PS-632 F1` with three incompatible readings, `PDC-12400 M6` and `PGFT-12V125 M6 FR` absent
  from the manufacturer's current catalogue, `2900-XX` a literal wildcard SKU, `OGN-MONITOR-STD`
  whose `STD` is polysemous inside one product line, `FREIGHT` which is not a product.
  **What settles them is a price list, a carton label or a dealer login &mdash; not another
  batch.** That is worth saying to the owner in those words, because &quot;37 left&quot; invites
  the wrong instruction.
  **And the general rule: a queue built by subtracting what you finished cannot see the items
  you correctly declined.** They look identical to untouched work from outside, so they
  accumulate at the bottom and every later batch re-slices them. The fix is the three-way split
  above &mdash; never sliced, in flight, declined &mdash; computed from the lot files rather
  than from the census.
- **Verification sweep at batch 49 (1,322 pages, 23 Sep 2026): clean an EIGHTH time &mdash; and
  for the first time in five sweeps the DENOMINATOR NEEDED NO CORRECTION, because the previous
  four corrections are now encoded in the query rather than remembered.** One bulk pull, 16,031
  active products. Population = the v2 slices (768) plus the old list taken from
  `BASELINE_555_publicadas.csv` (555), **minus the in-flight batch** and **minus the 279
  title-only products, which are tracked-but-not-enriched by design** &rarr; **1,322 audited,
  zero missing**, and exactly **four** pages under 400 visible characters: `SM7100-L8` (22),
  `90521` (30), `BDA-TP10-L2` (73), `BDA-NMP01250` (95), all four the deliberate skips.
  **That is the useful outcome of four embarrassing sweeps.** Batch 35 found title-only products
  breaking the equation between tracked and enriched; batch 40 found 99 abandoned slices from the
  retired queue; batch 43 hit both at once. Each was written up as a lesson, and a lesson that
  stays a lesson gets re-learned &mdash; **what stopped it was moving the exclusions into the
  script.** The sweep now states its own population in its output line, so the number cannot be
  read without seeing what it was measured on.
  Catalogue-wide on the same pull: **46 non-ASCII titles, every one `&deg;` (23), `&reg;` (21)
  or `&trade;` (5), zero outside that set** &mdash; 56 &rarr; 50 &rarr; 49 &rarr; 47 &rarr; 46
  across batches 14, 24, 29, 43 and 49, still falling on its own as enrichment rewrites titles
  for substantive reasons. **Zero** titles carrying a literal HTML entity. **Zero** titles
  repeating brand and SKU as separate tokens, bar the one known false positive whose `sku` field
  literally contains the vendor string. Unbalanced parentheses **102, unchanged**, as expected
  for truncated titles this project deliberately does not reconstruct.

- **Audit mode begins, 23 Sep 2026 (owner paused enrichment after v2b52).** First owner-approved structured-data write: **54 `productType` corrections** from the decision file's &quot;demonstrably wrong&quot; rows whose recommended value already exists in the live taxonomy (group A; 55 rows, one duplicate `FST-951-IV`). Pre-checked live by `nodes(ids:)`, applied in two aliased mutations of 27, zero `userErrors`, old values in `/tmp/tfas/BACKUP_tipo_grupoA_antes.json`. Group B (51 types needing a new or ambiguous category name, 13 vendors) awaits the owner in `AUDITORIA_tipo_vendor_para_aprovar.csv`.
- **A new truncation mechanism with no parentheses needed: the title's last 40 characters reappear in the live description followed by more text.** 180 titles of 120+ characters (e.g. *&quot;&hellip;(Notifier Marketing PN:&quot;* continuing *&quot;NFXI-BS-W)&quot;* in the body). This is *provable* truncation with the continuation on the page, so a short proper title can be written from the store's own text plus a manufacturer document &mdash; still agent work, because choosing where the name ends is a claim. Union with unbalanced parentheses (102), `?`-destroyed characters (13), SKU absent from the title (28, after excluding the Det-Tronics and Amerex ordering-code conventions **and SKUs whose whitespace tokens each appear in the title** &mdash; `PS-1280 F1` titled `PS-1280 &hellip; F1 Terminals` is fine, a normalised-contiguous test flagged it) and nameless titles (41) gives **309 products** in `/tmp/tfas/audit/FILA_titulos.json`, ranked `impr&times;30 + rev/50`, after removing ids already researched in any slice, title lot or the SKU/title divergence task. Only 38 carry ERP revenue and 58 impressions, so the queue is short on value and long on correctness.

- **Control-character scan, 23 Sep 2026:** titles containing `[\x00-\x1f\x7f]` across 16,031 live products = **1** (`CS40-U34-U4D-HE`, a garbled ERP string with U+0001/U+0002, found by an enrichment agent first); SKUs = 0. Add to the sweep; the one hit is queued for a title lot.

### t05 (23 Sep 2026): four title fixes approved by the owner, found in passing by e05

- **HMS-2S:** the title said "Double Action", a class error. Siemens 6316C (A6V11524007) calls it Two-Stage: the lever gives the first stage, a keyswitch gives the second, on a dual address, and it is for Canada only (ULC/FM). Double action is the HMS-D, which the store sells at $439. New title: `Siemens HMS-2S (500-033460) Intelligent Two-Stage Manual Pull Station with Keyswitch, Dual Address, Canada ULC Version`.
- **CS04-070/071/072-429:** the titles said "2 W / 3 W / 4 W", a wrong unit: the number is the way count from the SPD2/3/4 model string. Both 2026 Westell order guides agree on 300 W. The frequency stays out of the title because Westell contradicts itself: the model string says 698-2.7K, while the frequency column gives 450–2700 for the 2-way in both guides. The Ancillary guide also misprints the 4-way model as SPD3. productType "Fire Alarms" was flagged.
- Pattern: a number stuck after a comma at the end of an ERP string (`, 2 W`) can be a field from another column (way count). Candidate for a mechanism scan: titles whose "N W" equals the N of an `SPD<N>`/`-<N>-Way` token in the same title.
- productType for CS04-070/071/072-429 changed from Fire Alarms to BDA (owner-approved 23 Sep), matching every other Westell passive in the store. The e05 BDA-on-passives flags were closed: BDA is the store convention for the family.

### Scan: data-sheet sentence in the title (23 Sep 2026, prompted by GWPID-95P in e07)

- **Mechanism:** an import pasted the data sheet's opening sentence into `title` ("Brand SKU The Brand SKU Interfaces…", "…Note: Use This Part Number…", "…It Includes: 1. …"). Regex on the title after its first two tokens: `The|This|These|It|Its + word`, or a prose verb (`provides, interfaces, offers, features a, is designed, can be, Note:, It Includes`). The vendor string "by The Signal Source" had to be removed first: it produced 48 of the 66 raw hits.
- **Result on the live.jsonl snapshot (16,031 active):** 18 hits.
  - Not defects (3): the two Resideo "The Round®" thermostats (the product name) and GWPID-95P (already fixed in e07; the snapshot is stale).
  - **15 defects, so precision 15/18. Recall unknown:** sentences without these trigger words are missed.
- **Fixed unilaterally (5):** each new title is a literal prefix of the old one, with the SKU still present, ASCII, 150 characters or fewer, and no tail collision. The five: Kidde Fenwal 85-150000-520, 85-154000-500, 38-401140-060 and 06-231866-856, and Notifier 020-569.
- **Queued for an agent lot (10), in `/tmp/tfas/audit/FILA_t07_frase.json`:** 4904-9176, FSI-851, FSL-751, D2xC1X05, DH-101-A, WHES24-75WR, MIX-M502MAP, DA-4DS (191 characters, over the limit), 85-150000-530 and 90-150000-000.
  - The last two have the same truncated title and the same price ($3,354.70); duplicate-or-successor was flagged to the owner.
