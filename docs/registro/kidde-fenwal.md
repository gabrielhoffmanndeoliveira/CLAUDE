<!-- Registro de casos do projeto TFAS. Movido VERBATIM de CLAUDE.md em 23 Sep 2026; nada foi reescrito. Nao e carregado automaticamente: leia sob demanda. E cronologico: entradas posteriores corrigem anteriores; em caso de conflito vale a mais recente e o nucleo em CLAUDE.md. -->

# kidde-fenwal

- **A hazardous-location listing hiding in a suffix every distributor reads as a finish.**
  Kidde Fenwal `27121-20` was a bare `Brand PartNumber` title. Fenwal 12.01.D Table 2 puts
  `-20` in **Class I Groups A, B, C and D; Class II Groups E, F and G** (Division 1 and 2)
  while `27121-0` sits in the row **without Group A**; every distributor calls `-20`
  stainless steel and `-0` brass, and **the manufacturer states no material at all.**
  Correlated distributor copy for the sixth time, and the suffix encodes the thing a
  specifier actually filters by.
  **Both tables came off a 300 dpi render, because that PDF's text layer emits cells one
  character per line in reverse** &mdash; `27121` extracts as `1 2 1 7 2` &mdash; with the
  Contact Operation column vertically merged. Plain extraction is not merely unreliable
  there, it is unusable. Also settled from the same render: **27121 CLOSES on temperature
  rise where 27120 opens**, and it is **rate compensation** &mdash; the fifth such part,
  now across three brands, so the three-class taxonomy is thoroughly not a Thermotech
  quirk.
- **THE DESCRIPTION FIELD IS CARRYING THE ERP'S OWN STOCK CODES, AND THOSE CODES SAY
  WHAT THE PRODUCT IS WHERE NO OTHER FIELD DOES.** Found 22 Sep 2026 while asking why the
  remaining nameless titles are so heavily Kidde Fenwal. The live body of
  `Kidde Fenwal 0200-260W-CH` is, in its entirety, **`GAUGE-LL_60T-HORZ`**. Its sibling
  `0200-IT12-260W-CH` is **`GAUGE-LL+4-20MA_60T-HORZ`**. `0354-16-CH` is
  **`VALVE-BALL_1.00NPT`**; `0800-1-62` is **`CONDENSER-R404A_230V_1P_1HP`**;
  `1-85-194425-2xx` is **`Nozzle_360_1&quot; NPT Stainless Steel`**.
  **The mechanism that finds them is an underscore.** No English product description
  contains one; it is the ERP's own field separator leaking through. **123 of 16,031
  products, 121 of them Kidde Fenwal, and inspecting all 123 found no false positive.**
  **The first attempt over-fired at 3,222 and the reason is the usual one.** It tested
  &quot;all capitals, short, no lowercase word&quot;, which is a *shape*, and it fires on
  every terse but perfectly correct ERP-derived description in the catalogue
  (`8 POINT ZONE/RELAY MODULE`, `RELAY MODULE WITH 10 FORM C RELAYS`). Those are English.
  The underscore is a *mechanism*, and it cut 3,222 to 123 with no loss.
  **What the 123 turn out to be is the finding.** Liquid-level gauges (67), stainless
  discharge nozzles in NPT and BSP (20), R404A condensing units (12), relief, ball,
  solenoid and thermostatic expansion valves (14), 9 kW heating elements, a manway gasket:
  **the hardware of a Kidde low-pressure CO&#8322; storage unit and its piping.**
  **93 of the 123 are typed &quot;Fire Alarms&quot;**, every gauge and every nozzle among
  them. And **97 of the 123 are also on the nameless-title list &mdash; 42% of the 229 that
  remain** &mdash; so one family accounts for nearly half of that workstream.
  **Two things make this cheap rather than merely embarrassing.** First, the codes are
  internally self-consistent and read like a key: `GAUGE-LL` against `GAUGE-LL+DC` against
  `GAUGE-LL+4-20MA`, where the 4&ndash;20 mA option appears in the catalogue number as an
  inserted **`IT12`** token; `HORZ` against `VERT`; and a dimension before `T` whose
  implied decimal moves (`0200-1375W-CH` &rarr; `03.75T`, `0200-2220W-CH` &rarr; `22T`).
  Second, the twenty nozzles need no decode at all &mdash; their codes are already plain
  English.
  **But the code is the store's own data, not a manufacturer document, so reading it is a
  claim.** This file already decided that case: `34 NPT` &rarr; `3/4 NPT` was left
  unapplied because a thread size needs a document. An inch dimension and the expansion of
  `T` and `DC` need the same bar, and an agent is verifying the key against Kidde's own
  parts list rather than publishing an inference. **A `null` title is the right answer if
  the key cannot be sourced**, because it tells the owner the fix is a parts list and not
  more searching.
  Recorded separately as a data defect: the twenty nozzle SKUs literally end in **`-2xx`**,
  an ERP wildcard that has leaked into the Shopify SKU field.
- **`kidde-fenwal.com/Media/Data Sheets/` is a new trap of the REDIRECT kind**: it 301s to
  the site root, **byte-identical for a real and an invented filename**, so no first-party
  copy is retrievable there. The mime check alone does not catch it &mdash; the bogus
  control does. That is a third distinct Kidde-Fenwal failure shape after the
  1,279,593-byte `LocalMedia` HTML and the ordinary 404.
- **A bogus control that is defeated by a CSRF token, which is the subtlest instance yet.**
  Hochiki's AssetBank returns **14,749 bytes for a real keyword, a bogus keyword and no keyword
  at all &mdash; with three DIFFERENT MD5s**, because the page embeds a per-request CSRF token.
  **An MD5-only control passes it and a byte-count control catches it**, which is the inverse
  of the usual case where the page echoes the query and the bytes drift. Sixth non-discriminating
  endpoint on this project, and the first where the varying element is invisible to a reader.
  Also: `assetfile/<id>.pdf` serves real PDFs but carries **no `content-disposition`**, so an id
  sweep yields anonymous files with no attribution &mdash; the Kidde-Fenwal problem, no route to
  evidence.

- **ModuLaser electronics are catalogued by Kidde-Fenwal, not by Edwards, and the vendor string is a product line (v2b51).** `9-30783-KID-ULF` sits in `K-76-1500 Rev AD` (effective July 2026), reached as `kiddefenwal.com/?wpdmdl=3120` (713,101 B, `application/pdf`; a bogus `?wpdmdl=` returns 47 B `text/plain`). Ordering row verbatim: *&quot;9-30783-KID-ULF ModuLaser Detector Module (FM/UL/ULC compliant)&quot;*, with `-KID-EN` the EN 54-20 twin and the display modules (`-30780` Minimum, `-30781` Standard, `-30782` Command) separate catalogue numbers. **So the Edwards route in `edwards-kidde.md` fits only the RedPipe/RP fittings sold as ModuLaser; for the electronics go to the Kidde-Fenwal wpdmpro index.** Vendor `Modulaser` flagged. Store titles for `-30780`/`-30781` call both &quot;Control Display Module&quot;; the document distinguishes a colour TFT Standard module from an LEDs-only Minimum module.

- **In-line releasing-circuit devices (audit t04):** `06-220023-001` Class B and `76-800000-004` Class A &mdash; K-76-850 Rev AD (Feb 2026, `?wpdmdl=3123`) p14 MISCELLANEOUS (coordinator-verified) and K-84-900 Rev AF. Both typed Cables in the store (flagged); both carried the same truncated import title. &quot;Replaces 70101338 per Bulletin 2020-08K&quot; is in no document in the wpdmpro index.

### t09 (23 Sep 2026)

- **85-220032-001:** K-85-3006 (Rev AD at suppression.com, Rev AE at eunixfire.com; Kidde-branded mirrors that agree on every row; not in the wpdmpro index). It is a 3-way directional valve, 3 in. grooved, nickel-plated carbon steel, with solenoid and placement monitor, for ECS and ADS; the -100 variant is explosion-proof. **"ECS 360" in the store titles is in neither revision.** The four sibling valves share the same truncated title (queued), and the -001 description is truncated (pending_fixes).
- **76-600000-200:** K-76-606 Rev AB (May 2009, centuryfp.com mirror). It is the **key maintenance switch** (4PDT, stainless plate), and the 06-236881-001 backbox is separate and not stocked. productType Backboxes was flagged.
- **Routes:** the kidde-fenwal.com Media redirect trap still holds (1,775,527 B `text/html` for real and bogus names alike). wpdmpro `?search=` matches titles only. The WP media API returns [] even for the known-good K-76-850 (it does not discriminate).
- t10 (23 Sep): wpdmpro works first-party: `?wpdmdl=3126` = K-84-900 Rev AF (Jan 2026), 3121 = K-76-227 Rev AC; a bogus id returns 47 B text/plain. **84-900001-002** is the AEGIS-PHX control unit **with** door-mounted release, abort and key bypass switches (-001 has none). **70-600000-100** is the SmartOne programmer "complete unit"; -101 is the programmer plus SLC adapter only, and 06-220197-001 is the accessory kit. Two productType errors (a control unit typed Enclosures, a programmer typed Modules) were flagged.
- t11 (23 Sep): **81-994706-625**: the CO2 manual 81-CO2MAN-001 (Sep 2013, 324 pp., on store.centuryfp.com under the misleading filename `KIDDE-81-870486-000-DATA-SHEET.pdf`), Table 8-17, lists the 5/8" "I" valve for 75/100 lb cylinders and every component in the live title. K-81-1000 Rev AA (`?wpdmdl=3124`) and K-81-1005 Rev AA (`?wpdmdl=3125`) confirm the 5/8" Type I valves on high-pressure CO2 cylinders. **The kit numbers 81-994706-xxx are in no document found.**
