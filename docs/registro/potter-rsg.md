<!-- Registro de casos do projeto TFAS. Movido VERBATIM de CLAUDE.md em 23 Sep 2026; nada foi reescrito. Nao e carregado automaticamente: leia sob demanda. E cronologico: entradas posteriores corrigem anteriores; em caso de conflito vale a mais recente e o nucleo em CLAUDE.md. -->

# potter-rsg

- **A datasheet can contradict itself by three orders of magnitude, and the majority
  inside the document can be the wrong side.** Potter `8820099 REV A` gives the door
  holder's current as **&quot;.020 ma @ 24VDC&quot;** in its prose **and again** in its
  Technical Specifications box, while the model table reads **20 mA**. Two places
  against one, and the two are wrong &mdash; .020 mA would be a physically absurd
  holding current for an electromagnet. **Prefer-the-table beat two-against-one**,
  which is worth knowing: the rule is about *which kind of statement* is reliable, not
  about counting occurrences. That page also needed a **200 dpi render** to read which
  cells are shaded, because the note *&quot;holding forces correspond with shaded
  values&quot;* is invisible in the text layer &mdash; 40 lb with 24 VDC, 35 lb with
  120 VAC.
- **`RSG` is a Potter Electric Signal Company brand**, and Potter serves the document
  first-party (`8820099 REV A`), so no mirror is needed. Its model-number syntax block
  decodes `DH24120FB` completely: `DH` door holder, `24120` dual 24 V and 120 V, `F`
  flush, `B` brass. **Note the four mount styles it lists are Surface, Flush, Ground
  and Recessed &mdash; there is no &quot;semi-flush&quot;**, which is distributor
  wording that had reached the store title.
- **A keyword-based cross-page consistency audit does not work on this catalogue, and
  it is not worth rebuilding.** Attempted 21 Sep 2026: extract every part number
  mentioned in a published page, look up that part's own title, and flag where the
  mentioning page's class noun disagrees. It produced **59 findings, all false
  positives.** Two structural reasons, and both are inherent to the house style:
  1. **Enumerations.** 39 of 59 had another part number between the mention and the
     class noun &mdash; *"PAD100-IB isolator, PAD100-RB relay, PAD100-SB sounder"*
     attributes "sounder" to whichever item the window happens to start at.
  2. **The remaining 20 were relationship statements, not identity statements.**
     *"TRI-S is the same module without the relay"*, *"P2RK-R ships without a back
     box"*, *"BB-100 takes two 100 Ah batteries"* &mdash; the class noun belongs to a
     property of the part, not to what the part is. **The closing paragraph of the
     house style exists precisely to state relationships**, so nearly every class noun
     in it is grammatically the wrong one to test.
  The weak positive: 698 heavily cross-referencing pages produced no genuine
  contradiction under a naive scan. **Cross-reference checking works when an agent
  reads the live sentence and rules on it** &mdash; that is what caught the RA100Z
  error &mdash; and it does not work mechanically. Keep putting live sentences in
  front of agents; do not build the scanner.
- **Twelfth product-class error, and it is the incomplete-product trap for the fourth
  time.** `PAD200-DD` was titled and sold as a duct smoke detector, and its 616-character
  page said *&quot;The unit comes complete with housing and head&quot;* &mdash; a
  sentence lifted from the **PAD200-DUCT** feature list (*&quot;Ships complete with
  housing and head&quot;*) and applied to a bare head. Potter `8830167 Rev B` and
  `8830166 Rev A` both name `PAD200-DD` as the **Detector Head Model** inside the
  complete units, and their Engineering Specifications read *&quot;The housing shall
  contain a detector base and PAD200-DD duct smoke detector head.&quot;* At $81 the
  buyer received a sensing head with no housing, no base, no exhaust tube and no
  sampling tubes. The complete units are `PAD200-DUCT` and `PAD200-DUCTR`. **The type
  field said Duct Detectors and agreed with the wrong title, raising nothing &mdash;
  fourth instance.** Note the tell here was not the word &quot;required&quot; and not a
  &quot;comes with&quot; clause but **existing copy borrowed from the sibling's feature
  list**, which is a third signature for this trap.
- **The Thermotech 302 family: a whole product line mislabelled with a class word that
  is not a class, and the fix generalised from one SKU to five.** `302-135` came through
  v2b21 titled *&quot;Rate-Anticipation Heat Detector&quot;*. An agent found that
  **&quot;rate-anticipation&quot; appears zero times** in Potter `8820047 REV B` *and*
  zero times in the legacy Thermotech (Ogden, Utah) sheet, while &quot;rate
  compensation&quot; appears three times in each. The coordinator then fetched the legacy
  sheet directly &mdash; because this was about to change live titles &mdash; and it says
  it outright: *&quot;All models operate on the principles of a rate compensation
  detector&quot;* and *&quot;These rate compensation type detectors are available in
  either 135&deg; F. or 194&deg; F. ratings. All four basic models&hellip;&quot;*
  **Note why this is not the series-wide-spec-block trap.** That trap is about an
  unattributed *measured value* in a family block. This is a statement of **operating
  principle explicitly quantified as &quot;all models&quot;** &mdash; the definition of
  the class, not a number. Those are different kinds of statement and only one of them
  transfers to a member.
  The store disagreed with itself across eight SKUs: two said Rate Compensation, three
  said Rate-Anticipation, three named no class at all. **Five titles corrected**, which
  the family-disagreement scan would have flagged and a keyword scan never would.
  The document also settles the suffixes, and two were carrying real information no
  title mentioned: **`EPM` is Explosion Proof Mounting** (Fig. 4, *&quot;for
  installation in hazardous locations&hellip; **For Interior use**&quot;*, Killark series
  JL hub) and **`ET` is `AW` plus a plastic hexagonal grip bushing with 1/2 in. conduit
  threads** &mdash; both figures otherwise read identically as &quot;hermetically sealed,
  no special back box, indoor and outdoor&quot;. Two explosion-proof-mount detectors were
  being sold without the words &quot;explosion proof&quot; anywhere in the title.
  **And a cross-link between two products in one batch, which is the argument for
  batching related parts together:** the Solo 423 tester's manufacturer claim list names
  fixed temperature, rate-of-rise and combination detectors and **does not name rate
  compensation** &mdash; so the store sells a tester and a detector class the tester's own
  documentation does not claim to cover. Recorded, nothing asserted either way.
  New fingerprint from the same work: **`pottersignal.com` 404s return
  `application/javascript` at 78,087 bytes**; `brooksequipment.com/files/Thermotech/`
  served the legacy sheet clean at 7.6 MB, mime-checked.
- **A model-number syntax block can have more tokens than it looks like, and this file's
  own decode was one short.** It recorded Potter `DH24120FB` as `DH` door holder /
  `24120` voltage / `F` flush / `B` brass. The syntax block in `8820099 REV A` is
  **six** tokens &mdash; `DH (24120) (S) (P) (C) (1)` = Door Holder / Model-Voltage /
  **Mount Style** / **Powdercoated** / **Finish** / Coils &mdash; so in `FPC` the `P` is a
  standalone *powdercoated* token and only `C` is the finish. Corroborated by the
  accessory tables, where `PC` suffixes are chrome and bare `B` is brass, brass not being
  powdercoated. The mount-style finding held exactly: **there is no &quot;Semi-Flush&quot;**,
  and the live `<h2>` also carried **&quot;Box&quot;**, which is not part of this
  catalogue number at all &mdash; the surface back box is `DHBBPC`, a separate accessory a
  flush unit does not use. **Distributor consensus split rather than failing together
  here**, one saying Semi-Flush and another Flush Mount, which is the first time in five
  instances that they disagreed with each other.
- **Seventeenth product-class error, and the first where the live copy was ANOTHER
  PRODUCT'S copy end to end.** The `INX-10A` page described the **INX-10AC** in every
  sentence: *&quot;The INX-10AC provides 10 amperes of power and mounts inside the
  BB-5014 enclosure.&quot;* Mircom `CAT. 5321 Rev. 9` Ordering Information separates them
  outright &mdash; `INX-10A` is *&quot;Intelligent NAC Expander, 10 Amps **c/w backbox and
  red door**&quot;* while `INX-10AC` is *&quot;**Addressable Chassis. Mounts into BB-5008
  or BB-5014 enclosure**&quot;*, and there is a third, `INX-10ADS`, for a BBX-1024DS.
  **So the enclosure sentence was false for the part it sat on**, and in the direction
  that costs the buyer least but confuses most: the INX-10A *ships with* backbox, door,
  transformer, charger and battery leads.
  **This is the incomplete-product trap read backwards**, and worth naming as such: every
  previous instance was a bare component sold as a complete product, and here a complete
  product was described as a bare chassis. The signature is the same &mdash; **copy
  borrowed from a sibling's ordering row** &mdash; which is the third time that exact
  signature has fired (`PAD200-DD`, `4-NET-SM`, now this).
  One bounded negative came with it: the live *&quot;FM Approved&quot;* is **unsourced**
  &mdash; `CAT-5321` lists UL, ULC and an NYC Fire Department mark only, and the string
  &quot;FM&quot; appears **zero times in the 130-page `LT-899` manual**. Not denied, not
  repeated.
- **Three coordinator premises wrong in one briefing, and all three were warnings that
  fired on correct pages.** (1) The briefing said *&quot;Exceder is not Eluxa, do not import
  a candela figure&quot;* &mdash; `LHSW3`'s live `15/30/75/110 cd` **is Exceder's own set**,
  in `TD450117EN` Table 4, and the white finish was confirmed by x-coordinate (the X sits
  in the White column at x=341.8 against Red at x=303.4). (2) It said the `R` in
  `PAD200-DUCTR` was the obvious guess and that this project had been wrong about an `R`
  before &mdash; here it **is** a relay, manufacturer-stated: *&quot;Analog Addressable Duct
  Detector W/Relay&quot;*. (3) It warned that `PAD200-DD`'s bare-head defect might extend to
  `PAD200-DUCTR` &mdash; it does not; that unit *&quot;ships complete with housing and
  head&quot;*. **A warning that forces a check and turns out to be wrong is still worth
  giving**, which this file has now said three times; what is not acceptable is stating the
  guess inside it as fact.
  The `IPA-4000` arithmetic checked out exactly too: *&quot;thirty-one additional SLCs each
  with a maximum of 127 devices&quot;* is verbatim Potter and **32 &times; 127 = 4,064**.
- **Fourth instance of releasing gear merchandised as ordinary fire equipment, and this one
  turned on the ORDERING line rather than the page heading.** `IPA-4000` was titled
  &quot;Fire Alarm Control Panel&quot;, which is Potter's own page heading and therefore not
  false &mdash; but its **Ordering line reads &quot;Fire Alarm *Releasing* Control
  Panel&quot;**, releasing is standard (Pre-Release and Release indicators fitted, I/O
  circuits built for manual release stations and abort switches), and the title now says so.
  After `4099-9015`, `2099-9149` and `RP-2002` this is a settled pattern. **Also corrected in
  the same title: &quot;4,064 Points&quot; &rarr; &quot;4,064 Addresses&quot;**, because
  &quot;addresses&quot; is Potter's word in every occurrence and this panel separately has
  **200 logic points**, so &quot;points&quot; names two different things on one page.
- **The same batch produced a fourth signal for prefer-the-table, and it is the strongest
  shape yet: the stale side matches a DIFFERENT MODEL's sheet.** Potter `8830197 Rev C`
  gives the PAD200-PCD sensitivity as **1.1&ndash;3.5 %/ft (3.6&ndash;11 %/m)** in its table
  and **1.0 to 3.7 %/foot** in its Description paragraph and a Features bullet. Three things
  side with the table and none is &quot;tables beat prose&quot;: its metric conversion is
  coherent (1.1 %/ft = 3.6 %/m, where 1.0 %/ft would be 3.28); the sibling `PAD200-PCHD`
  sheet at the **same revision and date** carries the identical table value; and **the prose
  figure is word-for-word the value on the `PAD200-PD` sheet**, where it appears in both
  prose *and* table. So the prose was pasted from another product's document. **When a
  document contradicts itself, check whether the losing figure is correct somewhere else**
  &mdash; that identifies the mechanism and settles it.
- **Two more route corrections, both narrowing rules this file states too confidently.**
  Potter's working path is **`pottersignal.com/product/datasheet/<docnum>_<MODEL>.pdf`**,
  not the `<docnum>-<REV>-<MODEL>_DATASHEET.pdf` form recorded last batch &mdash; and the
  whole category is enumerable from `.../addressable-fire-alarm-system/smoke-detector`,
  **30 datasheet paths in one fetch**, which beats guessing either form. Also: the reseller
  spelling `PAD200-PHCD` is wrong; Potter publishes **`PAD200-PCHD`**. And the Eaton
  `urllib`-plus-Safari-UA route worked **first try on every file** in this session's agent
  while failing for another process in the same hour &mdash; per-connection intermittency
  confirmed a third time.
- **A FOURTH rate-compensation part, found by an agent that was not told to look for
  one.** `HFPT-11` is rate compensated at 135 &deg;F &mdash; stated in its own document
  &mdash; and **neither the title nor the live copy said so**, both reading as a plain
  thermal detector. The Thermotech 302 family was the first line found this way, and
  that was a title-level correction across five SKUs. **So the three-class taxonomy is
  not a Thermotech quirk**: it spans at least two brands and a second panel ecosystem,
  and any briefing that offers an agent only &quot;fixed or rate-of-rise&quot; is
  pushing it toward a wrong answer on a field that is otherwise invisible.
- **Twenty-third product-class error: the `PAD200-DD` shape repeats exactly one series
  up, and this time the store's two fields contradicted EACH OTHER.** `PAD300-DD` was
  titled an &quot;In-Duct Smoke Detector&quot; and typed **Smoke Detectors**. Potter
  `8830208 Rev D` gives the PAD300-DUCT's Detector Head Model as **PAD300-DD**, its
  Engineering Specifications read *&quot;The housing shall contain a detector base and
  PAD300-DD duct smoke detector head&quot;*, and its feature bullet is **&quot;Ships
  Complete with Housing and Head&quot;** &mdash; the same sentence that was borrowed onto
  the PAD200-DD page. At $75.05 the buyer gets a twist-on head; bases (`PAD300-4DB`,
  `PAD300-6DB`) and STN sampling tubes carry their own stock numbers.
  **Carry the exception, because it is not the same as PAD200-DD:** Potter **does**
  approve this head for direct in-duct plenum mounting, UUKL listed. It is not useless
  alone &mdash; it is **baseless** alone, which is a narrower claim and the one the copy
  makes.
  **And the parent's spec is not the child's, which inverts a rule in this file.**
  Listed air velocity is **300&ndash;3,000 ft/min for the head against 300&ndash;4,000
  for the PAD300-DUCT housing**, with humidity splitting too (0&ndash;93% against
  10&ndash;85% RH). This file records that *accessory specs often live in the parent's
  data sheet*; here the parent's figure would have been **wrong** on the child. Both
  directions are real: read the parent to find the number, then check whether it is
  attributed to the part.
- **A third first-party document for the Thermotech 302 family, and it is the only one
  that splits the listings per model.** Gamewell-FCI **`CS-2519 Rev. B`** is headed
  *&quot;302 Series Rate-Compensation Heat Detector&quot;* &mdash; a third independent
  confirmation of the rate-compensation class finding, on a third brand's letterhead
  &mdash; and its listing rows differ by model: **`302-EPM-135` and `302-EPM-194` read UL
  alone where the `302`, `-ET` and `-AW` rows read FM and UL.** Anyone quoting a
  family-level agency line onto an EPM part asserts an FM approval that document does not
  give it. Same series-wide-block trap, on an *approval* rather than a spec.
- **The SKU-versus-title scan came back, and its nine hits split three ways &mdash; which
  is exactly why the scan was queued to an agent instead of applied.** Six titles were
  corrected and three were left alone, and the three left alone are the valuable ones.
  **Three are one product with one field wrong**, and the fix is a title. `ESPS10-2` is a
  transposition of `EPS10-2` &mdash; **confirmed directly by the coordinator, because
  removing a part number from a live title is a claim**: Safe Signal's own `sitemap.xml`
  enumerates the whole pressure-switch range (EPS10, EPS40, EPS120, EPSA10/40/120, EPSEXP
  and the EXP variants) and **`ESPS` appears zero times in it**. Note what makes that
  stronger than the usual negative: **a sitemap is a literal enumeration, not a search
  endpoint that can silently ignore the query** &mdash; the failure mode this file records
  for `hochikiamerica.com` and now `pottersignal.com/search`. `AMS-38B-G`'s `-G` is
  distributor syntax for the grey finish (Potter's catalogue gives one model number against
  four stock numbers, and the live body already names stock `4370015`), and `WL-11.E1`'s
  `.E1` is **load-bearing**, not noise: Aiphone's own manual prints *&quot;Device No.
  WL-11.En / n : Destination No&quot;* and tabulates `.E1` as US and Canada at +18 dBm
  against five other regions, with the bare `WL-11` appearing zero times un-suffixed.
  **Three are two real products one character apart, and no title was proposed for any of
  them.** That is the outcome the scan was built to reach: a near-miss is equally the
  signature of a typo and of a sibling, and where both numbers are real the defect is worse
  than a typo because nothing on the page looks wrong.
  **`MTH-HMC-R-WP` is the dangerous one and it is worse than the flag suggested: the page's
  three fields name two different products.** Siemens' ordering table, coordinate-verified
  one y-line each, gives `MTH-HMC-CR-WP | 500-636185 | Hi Multi-Candela **Ceiling**
  Weatherproof, Red` against `MTH-HMC-R-WP | 500-636187 |` the same with **no Ceiling**. The
  live page carries the **ceiling** catalogue number and the word **&quot;Wall&quot;** in
  its body. **A buyer reading the words gets one unit and a buyer matching the part number
  gets the other**, at $147.95. `P32-DBB` is the same shape with the vote 3&ndash;1: title,
  description wording and Potter stock number `1000444` all say the **shallow** box while
  only the SKU says **deep**. And `213505`/`213510` are Aiphone's black and white handsets,
  where the SKU, the body and both stations named in the title are the **white** one and
  only the title's number is black.
  **The rule this sharpens: a third identifier is what breaks a two-field tie.** On all
  three the SKU and the title disagree and neither is self-evidently right; what settles
  each is a *catalogue number, a stock number or a colour word already on the page*, and in
  two of the three it sides against the SKU. **Look for the third field before ruling on
  the first two** &mdash; and where the answer depends on which unit is physically in
  stock, that is the owner's, not research's.
- **`https://eaton.com` WITHOUT the `www.` is a cheap new lever on this project's worst
  host.** An agent hit ~100 consecutive failures against `www.eaton.com` &mdash; urllib read
  timeouts, curl `INTERNAL_ERROR` on HTTP/2 and `Empty reply` on HTTP/1.1, WebFetch 503
  &mdash; then dropped the `www.` and got the PDF first try. Another document had come back
  from `www.` an hour earlier, so this is the recorded per-connection intermittency again
  and not a fix; but it is one fetch. **Try the bare host before concluding the Eaton route
  is down.**
  Two more route facts: **Potter's Security catalogue** at
  `pottersignal.com/product/literature/PotterSecurity_catalog.pdf` carries a complete stock
  number / model number / description list and decoded two rows of that task in one fetch;
  and **Detector Testers puts its product code in four independent places on one page**
  &mdash; a `scrolforsku` block, `window.dataLayer`, the quote-request link and the Magento
  `catalog_product_view_sku_<CODE>` cache handle &mdash; so a JS shell can carry a
  structured field four times over while its search endpoint is useless.
- **A wrong voltage in a feed title, and the store's own description already had it right.**
  `APS10A/230` was titled **115VAC**. Edwards `E85005-0127` Issue 1.6 Ordering Information
  reads *&quot;APS10A/230 | 10-Amp Auxiliary Power Supply (**220V**)&quot;* and the
  Specifications give *&quot;120VAC **or 220-240VAC**&quot;*. **The live description body
  said 230Vac and was right** &mdash; the page contradicted itself and the wrong half sat in
  the Shopify `title`, so it cost two channels while the correct value cost none.
  **The whole title is a distributor catalogue string pasted from the sibling**:
  *&quot;Auxiliary/Booster Power Supply 10A Total Expanded Cabinet 26A/H Capacity
  115VAC&quot;* appears verbatim on third-party sites **under the plain `APS10A` SKU**. That
  is the borrowed-copy signature (`PAD200-DD`, `4-NET-SM`, `INX-10A`, `SLE-LTEV-CFB-PS`) with
  a new origin: **borrowed from a distributor rather than from a sibling's own row**.
  **And the bogus &quot;26A/H&quot; has a findable origin too**, which is the useful half:
  both revisions say the cabinet takes **two 24 Ah** batteries, and the string `26` occurs
  once in either document &mdash; as the APS6A's **shipping weight, 26 lb**, in the column
  beside the model rows. An adjacent-cell error made at the distributor and inherited whole.
- **The `RMS-1T` family resolved, and it is a case where THREE of six pages were right and the two
  worst defects are the owner's to settle, not research's.** Six live pages contradicting each
  other on action count, class, vendor and type. The decoder is
  `pottersignal.com/product/tool/rms.pdf`, which **has no text layer at all** and was read entirely
  off a 200 dpi render.
  **The decode, and it kills the obvious wrong reading:** the digit before `T` is the **switch
  function** (1 SPST, 2 DPST, 3 SPDT, 6 DPDT), and **`T` is the TERMINAL BLOCK variant** &mdash;
  the Model table gives `1P` terminal block &quot;None&quot; with leads against `1T` terminal block
  &quot;A&quot;. **`T` is not the T-handle**: the engineering spec calls for a &quot;T type pull
  handle&quot; on *every* model including `1P`. `LP` is **Dual Action**, cast **&quot;LIFT &amp;
  PULL&quot;** on the cover in the installation drawing; `KL` is the key-lock reset; `KO` is
  **key operated, no pull**, verbatim in the Contact Type cell. **`RMS` is expanded nowhere** and
  was recorded as a bounded negative rather than guessed.
  **Four of the six are definitively NOT releasing equipment, decided by the ordering line.** Potter
  splits the family across two bulletins &mdash; `8900097` standard die-cast stations and `8910014`
  special application &mdash; and in the special-application bulletin a releasing unit **always
  carries a colour word AND a Wording** plus a stock number in the 10006xx band. The four sit in
  `8900097` as bare model strings.
  **The two that remain are the interesting ones and both went to the owner.**
  `RMS-1T-WP YELLOW`: **two Potter stock numbers share the identical model string and differ only
  in the Wording column &mdash; 1000682 HAZ MAT and 1000620 PREACTION RELEASE** &mdash; and the
  store SKU carries the colour but not the wording, so **it is not a complete Potter order code.**
  The title was corrected only where demonstrable (the live one said *Dual-action* where both
  candidates read SPST Single Action, and glossed HAZ MAT lettering as a hazardous-*location*
  rating, which is the separate `RMS-6T-EXP`) and **deliberately asserts no wording**.
  `RMS-1T-KL`: **the title and the SKU name two different products** &mdash; SKU in `8900097` as
  stock 1000451, a standard single-action station, against a title claiming Pre-Action Release with
  stock `1000688`, which appears **zero times in every Potter document read** though it falls inside
  the observed special-application band. **No title proposed**, and the stray `)` from the
  truncation import was **deliberately not fixed alone**, because fixing it would leave a
  tidy-looking title asserting the wrong product.
  **And the merged-cell trap fired twice on one table with three methods giving three answers.**
  `8900097` merges &quot;Single Action&quot; down five rows and &quot;SPST&quot; down three; plain
  text attached that SPST to one model, **word coordinates attached it to a different one**, and
  **only the 300 dpi render showed it spans all three.** First recorded instance of coordinates
  being not merely insufficient but actively wrong where plain text was also wrong &mdash; the
  three-step ladder earning its third step outright.
  **Colour encodes nothing about class, on a second brand.** Potter release stations exist in blue,
  red and yellow, and yellow exists in non-release wordings (EMERGENCY, GAS, HAZ MAT). After
  SigCom's *&quot;There is no agency standard, outside of red for fire&quot;*, the yellow-means-
  releasing convention is now disproved twice.
  Route: **`pottersignal.com/sitemap.xml` enumerates 625 document URLs in one fetch**, which is how
  all four bulletins were found, and `/product/tool/` is a directory this file did not record.

- **A borrowed dimension row settled by a THIRD signal, on a round appliance that cannot have
  one.** Simplex `S4903-0019-5` prints *&quot;Housing Dimensions (including lens) 7-1/4 in. H
  &times; 5 in. W &times; 2-5/8 in. D&quot;* for `4903-9197`, a **round ceiling** speaker
  strobe. Three signals against it, and the third is the one that settles it: a round housing
  cannot have H &ne; W; the document's own title and page-1 photograph say Round, Ceiling
  Mount; and **7-1/4 &times; 5 in. is verbatim the wall-series cover row (`4905-9996`/`9997`)
  in sibling sheet `4903-0015`.** That is the recorded *&quot;check whether the losing figure
  is correct somewhere else&quot;* rule firing for the second time, after the Potter
  `PAD200-PCD` case &mdash; and it converts &quot;the document contradicts itself&quot; into
  &quot;this row was pasted from that document&quot;. No dimension published.
  **Its candela table has no text in its cells at all** &mdash; the marks are 6.9 pt filled
  rectangles, so the assignment was made by column x-span (30 cd spans 186.3&ndash;261.1 and
  the mark sits at 220.0&ndash;226.9) and render-confirmed. A table whose cells contain no
  characters is a new extraction shape: plain text returns nothing to be wrong about, which is
  more dangerous than returning something wrong.
- **Potter serves per-SKU images at a 330 px preset with no larger rendition**, so that brand fails
  the 600 px floor on matching rather than on routing. Third brand where the binding ceiling is
  **image size** rather than filename matching or catalogue coverage (after Space Age's 200&times;200
  originals and RFS's `_ti` 320&times;200 thumbnails). **Say which of the three ceilings a coverage
  number hit**, every time.
- **A THIRD IDENTIFIER, and for the first time it was the EXISTENCE OF A SIBLING SKU IN THIS
  STORE &mdash; which stopped a product-class error the documents would have caused.**
  `PTS-C CABLE` was about to be titled a plug-type sprinkler valve supervisory switch, and every
  Potter document supports that: catalogue `8900063-AC`'s stock table reads
  `1010201 | PTS-C | Plug type supervisory switch` and datasheet `5401078 REV J` is headed
  `PTS-C PLUG TYPE SUPERVISORY SWITCH`. **The store already sells that switch separately**
  &mdash; confirmed live by the coordinator: SKU `PTS-C`, typed Supervisory Switches,
  **$279.65**, against this one at SKU `PTS-C CABLE`, typed Cables, **$78.30**.
  This file's recorded rule is *&quot;a third identifier is what breaks a two-field tie&quot;*,
  written where a SKU and a title disagreed. **Here the manufacturer's documents and the
  store's own fields disagreed**, and the tie-breaker was neither: it was **another product in
  the same catalogue at a different price**. The generalisation is cheap and new:
  **before titling a part from its manufacturer document, ask whether the store already sells
  that exact thing under another SKU. If it does, the one you are holding is something else.**
  One Shopify query.
  The bounded negative that came with it is the good kind, because it converts research into a
  purchase order: **no Potter document catalogues a PTS-C cable at all.** The word
  &quot;cable&quot; appears **zero times** in the 36-page catalogue, and the two datasheets each
  name exactly three stock numbers (`1010201` switch, `5490344` tamper screws, `5250062` hex
  key) and no cable &mdash; the `DN-62046` inverted proof, Potter numbering replacement stock
  when it means to. The 8 ft / 18 Ga figures describe the cable **as supplied on the switch**
  and were deliberately kept out of the title. A price list settles it; another search will not.
- **TWO PRODUCTS IN THIS STORE CARRIED THE IDENTICAL TITLE, AND THE MANUFACTURER'S OWN TABLE
  SAYS THEY ARE DIFFERENT DEPTHS.** `P32-BB` at $27.85 and `P32-DBB` at $35.80 were both titled
  *&quot;Potter P32-BB ...&quot;*. Potter bulletin **`8900097` Rev N**, fetched and read directly
  by the coordinator because this changes a live title, lists them one row apart in its
  Accessories block: **`P32-BB | 1000444 | Surface mount back box`** against
  **`P32-DBB | 1000445 | Deep surface mount back box`**, and the Description paragraph on the
  same page independently says the line is *&quot;available with **shallow and deep** surface
  mount back boxes&quot;*. Price corroborates from a third direction, the deep box costing more.
  **The `type` field was LITERALLY EMPTY on the `P32-DBB` product while its sibling reads
  Backboxes** &mdash; one of 52 blank types in 16,031 &mdash; so the structured field could not
  disagree with the wrong title and the store simply had two identical titles at two prices.
  **A duplicated title inside one family is a mechanism, not a shape**, and nothing in this
  file's scan inventory tests for it: the recorded scans test what a title *says* (entities,
  truncation, unbalanced parens, family `type` disagreement, brand-and-SKU repetition), and
  none asks whether **two SKUs in one vendor carry the same title string**. That is one group-by
  and it is worth running.
  **One question was left to the owner rather than answered, and the distinction matters:** the
  title was corrected because three signals agree on what `P32-DBB` IS &mdash; but **if the part
  physically on the shelf under that SKU is the shallow box, then the defect is in the SKU and
  not in the title.** Research cannot see a carton; that is the `RMS-1T-KL` and `PS-632 F1`
  shape, and it goes to the owner.
- **A live body claiming a finish the manufacturer attributes to a DIFFERENT product on the same
  page.** The `P32-DBB` page said the box is red. Potter's *&quot;High-gloss red enamel
  finish&quot;* bullet and its *&quot;Red with raised white letters&quot;* specification line
  both attach to the **pull station**, and the two back-box rows carry no colour at all. Removed
  &mdash; a weakening, not a new claim. Same shape as `BB-55F`, where every distributor said red
  and the manufacturer numbered only the `R` sibling.
