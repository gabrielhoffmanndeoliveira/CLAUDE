<!-- Registro de casos do projeto TFAS. Movido VERBATIM de CLAUDE.md em 23 Sep 2026; nada foi reescrito. Nao e carregado automaticamente: leia sob demanda. E cronologico: entradas posteriores corrigem anteriores; em caso de conflito vale a mais recente e o nucleo em CLAUDE.md. -->

# honeywell-edam-rotas

- **Supersession claims have their own source: Honeywell product-announcement
  bulletins.** The filename is a **descriptive slug with the bulletin number
  appended**, not the bare number: `.../downloads/M23.2SS.pdf` 404s, while
  `.../downloads/System-Sensor-L-Series-LED-Announcement-23.2SS.pdf` returns 200 &mdash;
  find the slug by search rather than constructing the path. `buildings.honeywell.com/content/dam/hbtbt/...` hosts bulletins that
  are **not** on `prod-edam`, and they carry an explicit three-column
  MODEL / DESCRIPTION / **REPLACES** table. Bulletin M23.2SS settled PC2WL in one
  fetch. **Try this first whenever a title claims "replaced by" or "replaces"** &mdash;
  a datasheet almost never states supersession, so the alternative is a reseller
  claim, and reseller supersession claims have now been wrong more than once
  (`XTRI-D` "Replaces HTRI-D" is in no Siemens document at all).
- **`lenel.com` and `cdn.lenel.com` answer HTTP/2 503, 371 bytes, `text/html`, to every
  client** &mdash; curl on both HTTP versions, `urllib` through the proxy, and WebFetch.
  Another stable failure fingerprint, like EDAM's 8,047-byte `application/javascript`.
- **`gamewell-fci.com/CatalogDocuments/` is blocked, with a new fingerprint:
  `application/javascript` at about **258,337 bytes**, and the size varies by a single
  byte with the requested filename.** That one-byte drift is itself the tell &mdash; a
  real document library does not serve two different documents 1 byte apart. Add it to
  the fingerprint list beside EDAM's 8,047-byte JavaScript, steelfire's 48,687 bytes,
  autocall's 103 bytes of `text/plain` and lenel's 371-byte 503. **Gamewell-FCI
  documents come from EDAM, not from gamewell-fci.com.**
- **Fiplex public-safety BDA gear IS first-party documented on EDAM, and the
  coordinator's premise that it was not is wrong.** Two briefings told agents to skip
  a Fiplex part if no manufacturer document existed; an agent found
  `prod-edam.honeywell.com` Document **`BD441.1`, 08/01/2023**, which tabulates HONBDA
  units by ordering part number with frequency plan (downlink and uplink MHz ranges),
  gain, power, battery, enclosure and UL 2524 2nd Edition listing. Two different EDAM
  paths served the same revision. An $8,948 unit did not have to be skipped.
  **The general lesson: &quot;relationship-sold&quot; describes how a category is
  bought, not whether it is documented.** BDA, flame-detection and Det-Tronics gear
  draw no search traffic, and it is easy to slide from that into assuming no
  datasheet exists. Check EDAM before writing off a line.
- **`alldataresource.com` cuts both ways, so the mime check decides which.** It served
  a **verbatim 382,945-byte mirror** of `HON-62084.02` whose footer, template and
  imprint match two sheets pulled directly from `prod-edam` &mdash; and it returns a
  **313,459-byte HTML shell** for a PDF it does not have. Same host, same request
  shape, one good and one poisonous. This is the `systemsensor.com` lesson again on a
  host the project already distrusted: **`file -b --mime-type` is what separates them,
  not the host's reputation.**
- **An agent report can assert a failure mode that does not exist, and checking costs
  one command.** A v2b17 agent reported that two Honeywell 404 pages in the scratch
  directory were &quot;saved as real PDFs&quot; that **&quot;pass the mime check and
  open cleanly in pymupdf&quot;**, and proposed it as a new trap where
  `file -b --mime-type` is insufficient. **It is not true.** Both files are the
  standard 8,047-byte EDAM 404, `file` reports `application/javascript`, and their
  first bytes are `\n<!DOCTYPE H`. The mime check catches them exactly as documented.
  Nothing was recorded from it. **Agent findings get the same verification as agent
  copy** &mdash; especially a finding that would *weaken* an existing safeguard, which
  is the most expensive kind to accept wrongly.
  (The same agent did find a genuine new fingerprint:
  `edwards-signals.com/files/<anything>.pdf` returns **HTTP 200 and 106,271 bytes of
  `text/html`** &mdash; caught by the mime check, as normal.)
- **Gentex path construction failed for the S-Series, so the direct-serve rule has a
  boundary.** `SHRR-Series1`, `S-Series1`, `STRR-Series1`, `SR-Series1` and `S-Series2`
  all 404 at 7,264&ndash;7,273 bytes of `text/html`. The real file is
  **`GN600_S-C-SC-H_Series_FINAL_R1.pdf`** (doc code SCSCH-01), found by search. The
  `fireprotection.gentex.com/files/<Model>-Series<n>.pdf` pattern works for some
  families and not this one &mdash; **find the filename, do not build it**, same as EDAM
  slugs and `qdigital.mx`.
- **&quot;Find the slug, do not build it&quot; has a boundary worth using.** EDAM holds
  two subdirectories this file had not recorded &mdash; `datasheets/flexbda-050526/`
  and `datasheets/fiplex-02022026/` &mdash; whose Fiplex passive-device slugs are long
  and descriptive. An agent found `HON-62071` by search and then **constructed the
  `HON-62072` sibling slug from it, and it resolved.** So: **within one document family
  in one dated subdirectory, the slug IS derivable from a sibling you already hold.**
  Eight guesses made without such a sibling all returned the fingerprint. Build from a
  known neighbour; never build from the document number alone.
- **EDAM case and root are independent axes, and the underscore rule is per-document.**
  Measured this batch: `DF_52004.pdf` (underscore) resolves while `DF-52004.pdf` and
  `df-52004.pdf` both return the 8,047-byte fingerprint under **both** roots; meanwhile
  `AVDS870-03.pdf` resolves **bare and correctly cased under the `honeywell-edam` root
  only**, with the `hon/hbt-fire` root, the lowercased form and the underscore form all
  failing for that same document. So the shapes do not compose into a rule &mdash; try
  bare, lowercased and underscore **against each root separately**, and accept that it is
  per-document.
- **CORRECTION to this file's own Scene7 note, and the correction matters more than the
  error: `?wid=2048` PADS THE CANVAS, it does not stretch, and `?scl=1` is how you get
  the master.** The coordinator recorded &quot;the parameter does not fetch a master, it
  **stretches**&quot; after measuring `2048&times;280` from a `320&times;280` bare asset.
  An agent measured it properly and the coordinator then verified directly on
  `HBT-Fire-WSK-HEAT-ROR-WSK-HEAT-CEILING-HiRes`: **bare 576&times;576, `?scl=1`
  1500&times;1500 at the identical 1.000 ratio, `?wid=2048` 2048&times;1500 &mdash; ratio
  1.365, content unchanged at 1500 px inside a wider empty frame.** So the rejection of
  those 127 images was right and the reason given for it was wrong, which is exactly the
  shape this file warns about in titles: a plausible description of a correct conclusion,
  never checked.
  **The practical consequence is larger than the semantics. The bare Scene7 URL is a
  ~576 px PRESET, not the master**, so a bare-URL harvest fails a 600 px floor on most
  assets and publishes a quarter of the available detail on the rest. Measured across the
  125 Scene7 rows already in the delivery: **33 get a genuinely larger image at `?scl=1`
  with the aspect ratio preserved exactly** &mdash; long edges going 576 &rarr; 1500, 864
  &rarr; 3072, 1053 &rarr; 3284 &mdash; the rest are already at their master, and 10 return
  403 to `?scl=1` and keep the bare URL. Upgraded in place.
  **So the rule is: `?scl=1` for the master, bare as the fallback, `?wid=` never.** And
  the fingerprint is sharper than recorded: a Scene7 miss is **HTTP 403, 20 bytes,
  `text/plain`, body `Unable to find image`** &mdash; this file had the size right and
  called it a 200.
- **The PIF endpoint in this file's own route note is the WRONG INDEX.**
  `joule-bt-hbt-meta-prod` is a **Salesforce support-case index**: it returns
  `case_number`, `contact_name`, `account_name`, `status`. No products, no assets. The
  product index is **`joule-bt-hbt-epim-product-prod`**, same path shape. The earlier
  Notifier harvest used the right one and the note recorded the wrong one, so every
  briefing since has been sending agents at support tickets.
  Two more Scene7 facts worth keeping: **asset ids carry no file extension** &mdash;
  `HBT-Fire-TRCW-LEFT-HiRes.png` 403s while the same id without `.png` serves, and the
  API's `name` field has the extension where `url` does not, **so build from `url`**; and
  **pooling assets by FILENAME across all records is a second, independent route** to the
  `sku_list` join, which surfaced 23 SKUs the join missed, including one whose correct
  asset hangs on a record whose `sku_list` does not contain it.
- **A document naming the wrong models in one row while the prose on the same page names
  the right ones.** System Sensor `WFDS518` covers only the EPS40 line, and its Switch
  Contact Ratings row is labelled **`EPS10-1` and `EPS10-2`**. The A/E paragraph on that
  page gives the same figures against the correct models, **so the numbers are safe and
  only the labels are wrong** &mdash; the inverse of the usual prose-versus-table
  conflict, where the numbers differ. Also two dimension statements that disagree, so no
  width was published.
  EDAM slug confirmed for that sheet: `WFDS518.pdf` and its lowercase form both return
  the fingerprint under both roots, while
  **`EPS40_Sup_Pressure_Switch_DataSheet_WFDS518.pdf` resolves under the
  `honeywell-edam` root only** &mdash; the `<Model>_<Description>_<DocNum>.pdf` shape.

- **`?download=false` is a SIXTH EDAM axis and it flips a 404 into a 200.** Measured
  reproducibly: `.../hon-ba-fire-dn-62112-l-ulc-n16-datasheet-19-feb-2026.pdf` returns
  the 8,047-byte fingerprint **2 of 2 tries**, and the identical path with
  `?download=false` returns **HTTP 200, 366,470 bytes, clean PDF, 2 of 2**;
  `?download=true` returns the fingerprint. So **a search result showing EDAM content at
  a path that 404s for curl may simply need the query parameter.** Not universal &mdash;
  it did not rescue the SLM-318 English slug. Also new: a dated subdirectory
  `datasheets/gamewell-101625/`, same shape as the recorded `flexbda-050526/`.
- **A live body naming a product that is a DIFFERENT CATALOGUE ITEM, and the document defines
  the right one twice.** `ZB-4-QC-MP`'s copy said *&quot;PWSC compression terminals&quot;*.
  **PWSC is a splicing connector** &mdash; DS 6592W calls PWS Splicing Sleeves and PWSC Splicing
  Connectors *&quot;the only approved methods of splicing the Detector&quot;*, and `A05-0288`
  files it under a Splicing Connector heading. **No document calls any terminal a PWSC
  terminal.** The live *&quot;NEMA 6P (IP67)&quot;* has the same status: the only enclosure
  rating in either document belongs to the fiberglass `ZB-HD-4-QC` and it is **NEMA 4X**. Both
  removed &mdash; a weakening, not a new claim &mdash; and both sit in the **description**, so
  they cost one channel.
  **The dedicated sheet could not be read and the block is total**, which is worth recording as
  a bounded negative rather than a gap: twelve consecutive attempts across two protectowire.com
  paths returned HTTP 202 with a 221&ndash;236 byte Sucuri `sgcaptcha`, defeating curl on both
  HTTP versions, a Safari UA, `urllib` through the proxy and WebFetch; EDAM mirrors only two
  Protectowire documents; and **archive.org has a snapshot but `web.archive.org` returns 403
  with a 24-byte egress-policy body.** Also: the EDAM Protectowire mirror is
  **`DS 6592W-1012` (2012)**, not the 2022 `DS6592AA-0622` revision this file cites &mdash; so
  the recorded 2022 finding cannot be reproduced from EDAM.
- **Three route facts, each with its control.** **A new EDAM zero-byte trap, live:**
  `datasheets/df-52416.pdf` (lowercase) returns **HTTP 200 with 0 bytes, `inode/x-empty`**
  while every other shape of that name returns the 8,047-byte fingerprint &mdash; a status-only
  check reads it as success, which is the `cdn.power-sonic.com` shape on a host this file treats
  as well understood. **`buildings.honeywell.com/content/dam/hbtbt/en/documents/document-lists/firelie/data-sheets/`**
  is a clean route with an honest control (`df-60440.pdf` &rarr; 205 KB PDF; a bogus name and
  `df-52416.pdf` alike &rarr; 404 at ~610 bytes `text/html`), so DF-52416's absence is a bounded
  negative &mdash; and the **manual** under `manuals-and-guides/user-manuals/52626.pdf` was both
  available and better, model-attributing the 240 VAC row where a datasheet would not. And
  **Resideo's residential hydronic line is a THIRD prefix at four zeros**:
  `TechLitDocuments/69-0000s/69-0404.pdf` and `60-0000s/60-2133.pdf`, after the `63-`/`67-`
  combustion line and the five-zero `33-00000s`.

- **Two more blocked-host facts, and one of them kills a route this file recommends by name.**
  **`session-manager.aero.joule.honeywell.com` is refused at the proxy gateway with `CONNECT
  tunnel failed, response 502`, zero bytes**, so the Honeywell product index recorded here
  (`joule-bt-hbt-epim-product-prod`) is unreachable from this environment entirely. And
  **`buildings.honeywell.com/us/en/products/by-brand/&lt;brand&gt;/&lt;slug&gt;` does NOT
  discriminate** &mdash; a real and a bogus slug both returned `application/javascript` at
  225,064 and 225,066 bytes. This file records that host as one where *the mime check works*;
  that is true of the `/products/.../&lt;slug&gt;` path and **false of the `by-brand/` path**,
  so the honest statement is per-path and not per-host. `gamewell-fci.com`'s fingerprint has
  also drifted: **258,629 and 258,627 bytes** against the ~258,337 on record, the one-byte-drift
  tell still holding.

