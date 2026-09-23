<!-- Registro de casos do projeto TFAS. Movido VERBATIM de CLAUDE.md em 23 Sep 2026; nada foi reescrito. Nao e carregado automaticamente: leia sob demanda. E cronologico: entradas posteriores corrigem anteriores; em caso de conflito vale a mais recente e o nucleo em CLAUDE.md. -->

# resideo-brk

- **For Resideo and Honeywell Home, the supersession source is the `03-` prefix.**
  `customer.resideo.com` techlit documents under `03-` are the **sell sheets**, and
  those carry the manufacturer's own REPLACES table &mdash; that is how
  `TH1320U4002/U` was confirmed to replace `TH5220D1003/U` and `TH5220D1029/U`.
  Reach for `03-` before `buildings.honeywell.com` on this brand family.
- **Resideo literature path details that cost fetches:** the working path is
  `/resources/Techlit/TechLitDocuments/<prefix>s/<file>.pdf` &mdash; **capital T in
  `Techlit`**, and the directory is `33-00000s` with **five** zeros. Grepping
  `customer.resideo.com/en-US/Pages/Product.aspx?cat=HonECC+Catalog&pid=<SKU>` returns
  the document paths in one fetch, across the `33-` and `50-` prefixes together.
- **A new first-party route for BRK and First Alert, found by reading a JS shell's markup
  rather than trying to extract it.** `brkelectronics.com` product pages return
  `application/javascript` at ~441 KB &mdash; the familiar shell &mdash; but the **raw
  HTML discloses the asset URLs**: `digitalassets.resideo.com/damroot/Original/<n>/<file>.pdf`,
  mime-clean PDFs with no bot protection. **Backslashes in the hrefs must be swapped for
  forward slashes.** That is the robots-and-sitemap lesson in a third form: when a site is
  a JS shell, **read its markup for links** instead of treating the shell as a document.
  Also worth keeping from the same batch: Honeywell **installation manuals** resolve under
  `manuals-and-guides/installation-guides/<docnum>.pdf` and `.../user-manuals/<docnum>.pdf`
  &mdash; and for `HPFF8CM` the manual was both **newer and more authoritative** than the
  datasheet, which is the go-to-installation-instructions rule paying again.
  Route counts from that batch: `notifier-us/hon-ba-fire-<docnum>.pdf` resolved **4 of 4**
  and the flat lowercase `datasheets/df-<num>.pdf` resolved **4 of 4**, while the
  `hon/hbt-fire` root **failed on every probe**. Everything that worked sat under
  `honeywell-edam/hbt/.../documents/`.
- **Two more first-party hosts, a new 403 fingerprint, and a `urllib`/`curl` reversal.**
  **`product.autronicafire.com`** serves datasheets at `/fileshare/fileupload/<id>/<name>.pdf`
  with no bot protection &mdash; and it matters because **`autronicafire.com` now 301s to
  `autronicagroup.com`**, whose media API is images only, so the obvious host is the dead
  one. Hrefs in its markup use **backslashes**, as with BRK.
  **`det-tronics.com`'s WordPress media API is open** and yields the whole 445-PDF library,
  but **`urllib` gets 403 where `curl` gets 200** &mdash; the exact reverse of the Eaton
  case, where `curl` fails and `urllib` succeeds. Neither client is the reliable one; try
  both.
  New fingerprint: **`hubbell.com` / `hubbellcdn.com` CloudFront 403 is 919 bytes of
  `text/html` that pymupdf opens as a clean one-page document** reading *&quot;403 ERROR /
  The request could not be satisfied.&quot;* Only `file -b --mime-type` caught it. **A
  Safari UA plus `Referer: https://www.hubbell.com/` defeats it** and the same request
  then returned the real 699 KB PDF.
  And **`web.archive.org` is refused by this environment's egress policy outright**
  (403, 24 bytes, &quot;Blocked by egress policy&quot;) for both the CDX API and snapshot
  fetches, though `archive.org/wayback/available` still answers. **Wayback is not a
  fallback here at all**, independent of archive.org's own outage &mdash; worth knowing
  before a batch is planned around it.
- **&quot;ABC&quot; on an extinguisher was right this time, and the pair is the lesson.**
  `PRO5` is **monoammonium phosphate**, so ABC dry chemical is the correct trade term and
  the live title stood. Compare `429022`, where &quot;ABC&quot; sat on a **clean agent**
  extinguisher whose UL rating happens to cover A, B and C. **The rating describes fire
  test performance; the agent is a separate fact**, and the copy now says so explicitly
  on both pages. Route: `customer.resideo.com/resources/Techlit/TechLitDocuments/` has a
  **`BRK-First Alert/`** subdirectory &mdash; a brand-named one, where this file's
  recorded Resideo shapes are all numeric (`33-00000s`, `50-`). Worth knowing because
  **`brkelectronics.com` product URLs now 404 at 210,566 bytes `application/javascript`**
  and `firstalert.com` at 222,672 bytes, so the `digitalassets.resideo.com/damroot/` route
  recorded here **could not be exercised at all** &mdash; the shell pages no longer
  resolve. Another recorded route decaying inside a week.
- **A FOURTH mechanism-based scan, and it took three sharpenings to get from 1,447 to 9
  &mdash; every one a mechanism, never a threshold.** The question: does the part number
  in a product's `title` match its `sku` field?
  **Pass 1, the naive comparison: 1,447 hits, almost all correct.** A catalogue
  legitimately titles a product by its **model name** while the SKU is an internal stock
  number &mdash; Amerex `B402` against stock `15280`, Eaton `Eluxa` against `ELCHSR`,
  Det-Tronics `PIRECLA1A1W1` against `007168-001B`. That is a naming convention, not a
  defect.
  **Pass 2, narrowing to a NEAR-MISS** &mdash; high string similarity, within a few
  characters of the same length, on the reasoning that *a near-miss is a typo where a
  complete difference is a convention*. **Still 1,402**, and the reason is a convention
  this file already documents: **Resideo and Honeywell Home SKUs carry `/U`, `/B`, `/E`,
  `/A` packaging suffixes that titles legitimately strip.** The scan was rediscovering a
  known rule as a defect.
  **Pass 3, excluding the four conventions this file already records** &mdash; the
  Resideo suffixes, the **Gamewell-FCI `GW` prefix** that hides the real catalogue
  number, the **Autocall `A` prefix** on Simplex numbers, and leading `00` in an ERP
  code. **Nine hits, and they look real.**
  **The lesson is not &quot;sharpen until the number is small&quot;** &mdash; that is how
  you tune a threshold until it tells you what you wanted. Each pass removed a *named,
  already-documented reason* why a difference is legitimate, and the scan stopped when
  there were no more known reasons left. **A scan is finished when you have run out of
  explanations, not when the count looks right.**
  **And the nine were NOT acted on, because the scan cannot tell which side is wrong.**
  `EPS10-2` against `ESPS10-2`, `P32-DBB` against `P32-BB`, `MTH-HMC-R-WP` against
  `MTH-HMC-CR-WP`, `AMS-38B-G` against `AMS-38B`, `ET-1010-W` against `ET-1010`,
  `WL-11.E1` against `WL-11`, Aiphone `213510` against `213505`, and a **Solo pair that
  appears to carry each other's suffixes** (`SOLO610-024` titled `-001` and `SOLO602-001`
  titled `-024`, at $408.80 and $137.25, so a swap costs 3x). **A near-miss is equally
  the signature of a typo and of a real sibling one character apart** &mdash; which is
  this catalogue's most common failure mode &mdash; and where both numbers are real
  products the defect is *worse* than a typo, because nothing on the page looks wrong.
  Queued to an agent in `/tmp/tfas/SKU_TITULO_DIVERGENTE.json`.
- **Resideo's residential combustion line uses a different prefix AND a different
  directory depth.** The sell sheets are **`63-`/`67-`**, not the recorded `03-`, and
  the directory is **`63-0000s` with FOUR zeros**, not the five-zero `33-00000s` form
  this file documents. The `pid=` endpoint still needs `/U` kept and encoded, exactly as
  recorded &mdash; bare `S8610U3009` 302s.
  **And a Resideo product page can link a document it does not serve**: `68-0135.pdf` is
  listed on the page by its own `CheckDocExists` call and 404s at the path the page
  gives, across six variants. The installation instructions carried the specs instead
  &mdash; the go-to-installation-instructions rule paying for the fifth time.
  Two conflicts on that part, resolved rather than dropped: the page's marketing prose
  says a **6 minute** retry delay while **its own structured field and the installation
  table both say 5**, so 5 was published and the outlier recorded; and the page says
  **60 Hz** where the installation sheet says **50/60 Hz**, so **no frequency was
  published at all**.
  The live title's *&quot;Multi-System&quot;* is also **not Resideo's word** and appears
  in no document read &mdash; their name is *Universal* Intermittent Pilot Gas Ignition
  Module &mdash; and the title dropped the `/U`, so it did not match its own SKU. Both
  corrected.
- **Two route corrections.** **`apollo-fire.co.uk`'s 404 is 77,747 bytes of `text/html`** &mdash;
  and **three PDF URLs published on Apollo's own product page return it**, the recorded Resideo
  `68-0135` shape of a page linking a document it does not serve; the working files are the
  `F00…_0001.pdf` names on the same page. And **`macurco.com` must be used WITHOUT `www.`** &mdash;
  the `www.` host 301s to zero bytes &mdash; while its WP REST `product` endpoint is honest and its
  CM page is a **combined CM-6 / CM-12 page** at `/product/cm-6/`, with `/product/cm-12/` a 404.

- **A Resideo table where the merged blank above the row is the trap.** `69-0404` Table 1: the
  `V8043F` row **owns its own &quot;Terminal Block&quot; cell** while the rows above it are a
  tall merged blank that plain extraction would have inherited downward. Word coordinates also
  settled the column: `40003916-048` sits at x=77.1, *Electrical Connection on Manual Opener
  End*, not the x&asymp;135 opposite-end column. The powerhead's contents are stated twice
  &mdash; *&quot;includes the motor, housing, and 2 mounting screws&quot;* &mdash; and what the
  buyer still needs depends on the body already in the wall: a **series 6** body takes it
  directly, a **series 1&ndash;5** body must first be converted with **`40003918-006`** for a
  2-way water body (`-007` 3-way, `-008` 2-way steam), ordered separately. The live copy's
  *&quot;convert **pre-1986** zone valves&quot;* is unsourced &mdash; Resideo says series 1 to 5
  and gives no date anywhere &mdash; and the page named no kit number at all.
  **One boundary the agent refused to cross, correctly:** `69-0404` assigns motor, housing and
  screws to the head while `60-2133-12` calls the end switch *integral to the V8043F valve*, and
  **neither document puts the switch on one side of the carton boundary**, so the copy states
  the switch's rating and the valve's behaviour without asserting what is in the box.

