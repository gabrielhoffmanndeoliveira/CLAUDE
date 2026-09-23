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
