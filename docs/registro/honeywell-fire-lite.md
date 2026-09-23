<!-- Registro de casos do projeto TFAS. Movido VERBATIM de CLAUDE.md em 23 Sep 2026; nada foi reescrito. Nao e carregado automaticamente: leia sob demanda. E cronologico: entradas posteriores corrigem anteriores; em caso de conflito vale a mais recente e o nucleo em CLAUDE.md. -->

# honeywell-fire-lite

- **For any PAM-series relay, go to `apcfire.com/wp-content/uploads/` first.** Air
  Products and Controls publish their own current sheets there &mdash;
  `DS-RL-1-G25-PAM-Series.pdf` (2026-01) tabulates PAM-1/-2/-4/-SD side by side. The
  Honeywell/Fire-Lite mirror `DF-52068:A` is from **2014**, is **superseded** (it gives
  the PAM-4 coil floor as 9 VDC where APC now says 12), and is **internally
  inconsistent** (its table says the PAM-4 has an LED; APC's says it does not). An
  agent had a correction drafted off that mirror and killed it after reading APC's own
  sheet.
- [CORRIGIDO — `-IV` é cor E protocolo; ver honeywell-notifier.md, &quot;-IV IS BOTH A PROTOCOL AND A COLOUR&quot;] **The `-IV` suffix encodes a PROTOCOL, not a colour, and it is a Honeywell-wide
  convention rather than a Gamewell quirk. Measured: 52 SKUs, and not one names a
  protocol in its title.** Confirmed independently on a second brand the batch after
  Gamewell: Fire-Lite `DF-61011:C` prints *&quot;NOTE: '-IV' suffix indicates CLIP and
  LiteSpeed device&quot;*, and installation sheet `I56-6525-000` says it in full &mdash;
  *&quot;H365, H365R, and H365HT will support only LiteSpeed protocol mode. H365-IV,
  H365R-IV, and H365HT-IV will support either LiteSpeed or CLIP.&quot;* So on Gamewell
  it is Velociti-or-CLIP and on Fire-Lite LiteSpeed-or-CLIP: **the same idea, ivory as
  legacy service stock carrying the dual-protocol build.**
  The catalogue holds **52 SKUs ending `-IV`** &mdash; Notifier 27, System Sensor 10,
  Gamewell-FCI 8, Fire-Lite 7 &mdash; of which **51 are detectors, sensors or bases**,
  and **0 mention CLIP, LiteSpeed or Velociti anywhere in the title.** That is a
  functional difference a specifier needs, absent from a Merchant Center feed attribute
  on up to 51 pages.
  **Treat it as a routing note, not a defect list.** The convention is proven on two
  brands and two product lines, not on Notifier or on System Sensor bases (a base has no
  protocol of its own), so **when an `-IV` part comes through the queue, check its
  protocol in the ordering block** rather than rewriting 51 titles from a pattern. This
  project's own history is unambiguous that a pattern is a reason to check and never a
  licence to rewrite.
- [CORRIGIDO — `-IV` é cor E protocolo; ver honeywell-notifier.md, &quot;-IV IS BOTH A PROTOCOL AND A COLOUR&quot;] **The `-IV` protocol finding was confirmed a second time inside the same batch, by a
  different agent on a different product line.** Agent 2 had `H365R-IV` and agent 3
  `SD365T-IV`; both found the note independently, and `DF-61010:C`'s ordering block
  carries it in the same words as `DF-61011:C` &mdash; *&quot;'-IV' suffix indicates
  CLIP and LiteSpeed device&quot;*, against white heads listed **&quot;LiteSpeed
  only.&quot;** Two brands, three product lines, four documents. The routing note above
  stands, and **any collection logic or copy treating `-IV` as a colour variant is
  wrong.**
- **The series-wide spec block is a new shape of the adjacent-row trap.**
  `DF-61010:C`'s System Specifications prints one thermal line for the whole SD365
  family &mdash; fixed 135 &deg;F, rate-of-rise 15 &deg;F/min, high-temperature
  190 &deg;F &mdash; **with no model attribution**, while the Product Line entry for
  `SD365T-IV` names only a fixed-temperature device. Reading the series block as if it
  described the part would have published a rate-of-rise claim on a fixed-temperature
  detector. **A spec block that covers a family is not a spec for any member of it.**
- **The A&amp;E paragraph quoting a DIFFERENT ROW, and this one understates a design
  calculation by a factor of two.** Gentex `551-0045-04` page 4 specifies *&quot;an
  operating current of **47 mA** or less at 24 VDC for the 15 Cd strobe circuit **with an
  amber lens**&quot;*. The blue, green and red lenses share a different row entirely:
  **105 mA at 15 cd rising to 310 mA at 110 cd**, against amber's 47/64/113/145/178.
  **Anyone quoting the A&amp;E headline for a blue unit understates NAC load by roughly
  2x**, and NAC load is what sizes a power supply and a circuit.
  This is a third distinct shape of the same family. The recorded ones are
  *prose-contradicts-table* (Eaton's mangled candela set) and *series-wide block with no
  member attribution* (`DF-61010:C`). **This one is neither: the A&amp;E paragraph is
  correct, specific and attributed &mdash; to the wrong lens.** So the check is not
  &quot;does the prose disagree with the table&quot; but **&quot;which row is the prose
  talking about&quot;**, and an A&amp;E paragraph naming a variant is quoting one row of
  several.
- **A catalogue number under the wrong brand, proved by counting occurrences in the two
  brands' own manuals.** `N-FPJ` sits in this store under vendor **Fire-Lite**. It is a
  **Notifier** number: `DN-60779:C` (Notifier NFC-FFT FirstCommand) names it, and the
  Fire-Lite twin `DF-60735:C` (ECC-FFT) names **`FPJ-F`** in exactly the same slots. What
  settled it is a count, not an absence: **`N-FPJ` appears ZERO times in the 32-page
  Fire-Lite ECC-FFT manual `LS10031-000FL-E:C`, where `FPJ-F` appears 43 times.** Brand is
  a Merchant Center feed attribute, so the title was left alone and the flag went to the
  owner, with the relationship stated in the body. **Wrong-document-family avoided twice
  inside this one part:** the agent fetched and then *rejected* `54418:C` and `351204 B`,
  which cover the IFP-FFT and SK-FFT systems and contain zero `N-FPJ` &mdash; their
  single-gang box dimensions were deliberately not imported.
- **Twenty-second product-class error, and it is the plug-in-head shape for the THIRD
  time.** `SD365R-IV` ($220) was titled *&quot;Replacement Duct Smoke Detector&quot;*.
  `DF-61010:C` Product Line reads **&quot;SD365R-IV: Ivory, low-profile intelligent
  photoelectric sensor, remote test capable, **for use with DNR/DNRW duct smoke detector
  housings**&quot;** &mdash; the housing carrying the sampling tubes and duct interface is a
  separate product. After `PAD200-DD` and `D4S` that is three brands doing the same thing,
  and **the `type` said Smoke Detectors and agreed with the wrong title, raising nothing**
  for the eighth time.
  **The series-block trap fired exactly as briefed and was avoided:** `DF-61010:C`'s System
  Specifications prints *fixed 135 &deg;F / rate-of-rise 15 &deg;F per minute /
  high-temperature 190 &deg;F* **with no model attribution**, while this model's Product
  Line entry names no thermal element at all and `SD365T` is the version that has one. No
  thermal claim published, and the copy says why.
- **The route note in this file named the wrong document, and the right one is one digit
  away.** The briefing pointed at `DF-61010:C` as the SD365/H365 family sheet. **`H365`
  appears zero times in it** &mdash; that is the SD365 *photoelectric smoke* sheet, and
  the heat sheet is **`DF-61011:C`**, slug `H365_DF-61011.pdf`. Bare, lowercase,
  underscore, `hon-ba-fire-` and the `hon/hbt-fire` root all returned the 8,047-byte
  fingerprint for it. Also worth knowing before it costs a fetch: **`I56-6525-000` is the
  H365 installation sheet**, served from EDAM's `user-manuals/` directory, while
  `DF-61011:C` separately cites `I56-6525` as the *Applications Manual for System Smoke
  Detectors* &mdash; a document-number collision on one brand.
- **The catalogue number sets a DEFAULT, not the hardware, and the datasheet alone would
  have published an incomplete answer.** `H365R`'s `R` **is** rate of rise, stated and
  model-attributed in `DF-61011:C`. But installation sheet `I56-6525-000` adds two things
  the datasheet does not: Note 4 says H365R defaults to **a 135 &deg;F fixed element *and*
  rate of rise**, and the General Description says **all six H365 models are field
  programmable from the panel** to any of the three behaviours. So the part number picks
  the fall-back, and the sensing circuit is one thermistor in every model. **That is the
  go-to-installation-instructions rule paying for the fourth time**, and it is a different
  shape from the usual one &mdash; not a missing electrical rating, but the *scope* of
  what the catalogue number is claiming.
  **The series-block trap fired as briefed and was avoided:** `DF-61011:C`'s System
  Specifications prints fixed 135 &deg;F / RoR 15 &deg;F per minute / high-temp 190 &deg;F
  as one unattributed family line, and every thermal figure published is model-attributed
  instead.
  **Unresolved and flagged rather than guessed:** `DF-61011:C` says
  *&quot;Mounting: B300-6(A) flanged base, **included**&quot;* while `I56-6525-000` step 1
  says *&quot;Wire the sensor base **(supplied separately)**&quot;*. Two Fire-Lite
  documents, one part, contradicting on the carton, and the SD365 sheet carries no
  Mounting line so there is no third signal. The copy tells the buyer to confirm.
  **And that contradiction has a live cost the batch found on its own:** the `H365HT`
  **title** read *&quot;Addressable Heat Detector **Includes Base**&quot;* &mdash; the
  only one of six family members asserting it, and asserting exactly what Fire-Lite's own
  two documents cannot agree on. The same title **omitted the 190 &deg;F rating**, the one
  thing that distinguishes the HT, while its sibling `H365` does carry its 135 &deg;F.
  Corrected to `Fire-Lite H365HT Addressable High Temperature Heat Detector, 190F,
  LiteSpeed Only` &mdash; the unsourced claim removed, which is a weakening, and the two
  restatements taken from `DF-61011:C`'s own model-attributed rows.
- **The page-chrome lifecycle trap, FOURTH instance &mdash; and this time it reached a search
  summary as a fact.** A web search reported that Fire-Lite `FM900` *&quot;is a discontinued
  product on Honeywell's website&quot;*. Curling that URL returns **HTTP 404, 219,857 bytes of
  `text/html`**, and the only occurrence of the word is the JS UI label
  `&quot;discontinuedText&quot;:&quot;Discontinued&quot;`, attached to nothing &mdash; on a page
  that does not exist. No lifecycle claim published. **A summarising layer can turn page
  furniture into a sourced-sounding sentence, and a 404 is not an obstacle to it.**
- **`Ten-Xone` is in no Fire-Lite document, and neither is `Ten-Zone`.** The `MS-10UD-7E` title
  read *&quot;Ten-Xone, 24-Volt Fire Alarm Control Panel&quot;*, which reads as a one-character
  typo inviting a one-character fix. Both strings appear **zero times** in manual `52626 Rev C7`;
  what Fire-Lite states is *&quot;the MS-10UD is a ten zone FACP&quot;* and *&quot;MS-10UD - ten
  programmable IDCs&quot;*. So the agent wrote `10-Zone` from the manufacturer's own words rather
  than repairing the typo into a claim &mdash; **correcting an obvious typo is still writing a
  new title, and it needs the same source as any other.** The trailing `E` was confirmed as
  volts and not watts, model-attributed: `MS-10UD-7E (FLPS-7 Power Supply): 240 VAC, 50 HZ, 2.20
  amps`. Defect field: **Shopify `title`**, so two channels.


- **BG-12 family separated from `DF-52004:A1` plus three installation sheets (v2b51).** BG-12S single action, pigtails, hex lock; BG-12SL the same with key lock; BG-12/BG-12L dual action, screw terminals; BG-12LO outdoor, no box; BG-12LX addressable dual action (`DF-52013:D`). **Document defect:** DF-52004 reads *&quot;BG-12SL: Same as BG-12 with key lock&quot;* while BG-12 is dual action and `I56-2269-004` makes BG-12SL single action &mdash; the installation sheet wins. The Features list (terminal strip, push-in/pull-down) is series-wide and describes the dual-action models; not imported. Trim ring spelled `BG12TR` in datasheets and `BG-TR` in the install sheet, so not named. Routes: `DF_52004.pdf` (underscore) resolves again; installation sheets resolve at `.../installation-guides/I56-xxxx-xxx.pdf?download=false`. A web summary invented pigtail wiring steps that are not in `I56-2263-005`.
