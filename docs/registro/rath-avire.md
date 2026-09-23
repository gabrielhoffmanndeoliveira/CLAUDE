<!-- Registro de casos do projeto TFAS. Movido VERBATIM de CLAUDE.md em 23 Sep 2026; nada foi reescrito. Nao e carregado automaticamente: leia sob demanda. E cronologico: entradas posteriores corrigem anteriores; em caso de conflito vale a mais recente e o nucleo em CLAUDE.md. -->

# rath-avire

- **The fix is to work by BRAND, not by product, and the structure supports it:
  7,190 of the 7,900 sit in 20 brands.** Kidde Fenwal 1,508, Hochiki 798, Rath 708,
  Amerex 629, Space Age 480, Mircom 410, STI 394, Notifier 387, Westell 371, Power Sonic
  232, Fiplex 224, Edwards 206. A route mapped once per brand pays back hundreds of
  times, where a route found per product pays back once. The remaining **710 sit in 59
  small brands** and are a separate question &mdash; the one that decides it is how many
  of those 59 hosts answer the WordPress REST media API, because if most do, one script
  covers the whole tail.
  **Proven on the first brand within minutes of the redirect.** `avire-global.com`'s open
  media API was run over all 708 Rath SKUs by script, matching SKU to filename, at a hit
  rate around **36&ndash;46%** &mdash; call it 250 photographs from one script run against
  five from one agent run.
- **A fourth and fifth brand recovered by going at the CMS instead of the page, and one
  of them is the best document index found on this project.** `rathcommunications.com`
  is unreachable (connection reset on curl, `urllib` and WebFetch; `rath.com` fails TLS)
  and it does not matter: **RATH and JANUS are now AVIRE, a Halma company**, and
  `avire-global.com/en-us` is first-party, with datasheets headed &quot;RATH by AVIRE&quot;.
  Its **WordPress REST media API is open**:
  `https://www.avire-global.com/en-us/wp-json/wp/v2/media?search=<term>&per_page=100&_fields=id,source_url,media_details`
  returns every PDF **and** every image with true pixel dimensions, so one call finds the
  current datasheet and the product photograph together. **`power-sonic.com` has the same
  API open.** After Functional Devices, Space Age, HyperSpike and BRK, that is six brands
  recovered by reading `robots.txt`, the sitemap, the raw markup or the REST API rather
  than the rendered page. **When a brand's site is a JS shell or unreachable, go at the
  CMS** &mdash; and check whether the brand still exists under its own name.
- [CORRIGIDO — não generaliza para a linha, e grep não prova rebranding (logo é imagem); ver neste arquivo] **A brand can vanish from its own current documents, which is a vendor-field signal
  stronger than a rebrand notice.** This file records Avire datasheets headed *&quot;RATH
  by AVIRE&quot;*. On `3300FSN` the two **current** sheets are Avire-branded and the string
  **`RATH` appears zero times in either**. So the transitional heading is gone on this line
  and the store's vendor field is the only place the old name survives. Flagged, title
  untouched &mdash; brand is a feed attribute.
- **A wildcard SKU cannot match a query, and it is a feed defect with no research answer.**
  `2900-XX` contains a literal `XX`. Every route was tried and closed: `2900` appears
  **zero times** across the entire live AVIRE US site (nine sitemaps, the media API, the
  search endpoint), the four legacy RATH hosts all fail with connection reset to both
  `curl` and `urllib`-with-Safari-UA, and Wayback is egress-blocked. Search titles suggest
  the 2900 series spans pull stations, duty stations, dome lights and three sizes of
  annunciator console &mdash; **several device classes, so there is no single class noun
  even if that is right.** Left exactly as it was and flagged: the owner splits it into
  real part numbers or drops it from the feed.

- **A correction to this file: RATH has NOT vanished from current Avire documents.**
  This file records, from the `3300FSN` work, that the two current sheets are
  Avire-branded and `RATH` appears zero times in either. **That does not generalise to
  the line.** The 5.26.2026 series datasheet writes *&quot;RATH&reg; 2500-PWR24U&quot;*
  and the 2023 sheet *&quot;an additional interface device from RATH&reg;&quot;*, so the
  vendor field is not stale for the 2500 series. **A brand-vanished finding is per
  document line, not per brand** &mdash; the same scope error as the pack-count rule that
  had to be confined first to a category and then to a vendor.

- **The legacy RATH document estate is not merely unreachable &mdash; it is reachable and it lies.**
  `rathcommunications.com`, `rathnursecall.com`, `area-of-refuge.com` and `januselevator.com` all
  answer **HTTP 301 to `avire-global.com/en-us/` and serve the identical 442,703-byte Avire US home
  page for every URL**. Over HTTPS they fail at the proxy (`ws_closed_mid_exchange`); **over plain HTTP
  they return 200**, and that 200 is the home page rather than the page asked for. This file records
  the host as &quot;unreachable&quot;, which is the wrong and more dangerous description: a redirect
  that discards the path passes a status check, passes a byte-length check against itself, and returns
  content. **The reliable test is whether the response contains what you asked for**, and the redirect
  is a new fingerprint for that list.
  Against it, the Avire `?s=` site search is **honest** &mdash; controls: `SmartRescue` 8 product
  pages, `Pana40` 2, `2500` 14, invented term **0** &mdash; which is what made five deliberate nulls
  in that lot worth anything. Also confirmed there: **`urllib` gets 403 where `curl` gets 200** on the
  Avire media API, the Det-Tronics reversal on a second brand, so neither client is the reliable one.

- **An accessory documented in a MOUNTING GUIDE, which is the JCI-hub lesson on a new host.**
  `SUBPNBX` appears **twice in 798 Avire PDFs and both times in `AOR_Mounting_Guide.pdf`**:
  *&quot;Flush Mount Call Boxes: 2100-958NSR, 2400-808NSP, 2100-958NMBR, 2400-808NMP,
  **SUBPNBX (back box only)**&quot;*. The datasheets never mention it. This file already
  records *an accessory is usually not a document &mdash; grep the parent's material*; add
  that the parent's **mounting or installation guide** is where a back box lives, not its
  datasheet. Note the store's ERP wildcard `(958S__)` **understates** it: the manufacturer
  lists 2400-808 models too, so the title follows the document and not the ERP.
- **A title drafted and then killed by an IN-FAMILY suffix proof, which is the right
  standard.** `RP7700100BR` was about to be titled from its base number, which is documented
  four times first-party as a RATH battery-backed-up mains supply. Then
  `RP8500080-Solar-Tower.pdf` turned up reading *&quot;connected to RATH&reg; **Charger**
  #RP7700100AV&quot;* &mdash; **one suffix on this exact stem already denotes a different
  class of product.** With in-family proof that the suffix is load-bearing, carrying the base
  number's class noun onto `-BR` is the sibling trap, so nothing was written. **A suffix is
  load-bearing until a document says otherwise, and the cheapest proof is another suffix on
  the same stem.**
  Two Avire route facts came with it: the complete document library is enumerable at
  `wp-json/wp/v2/media?media_type=application` (**826 PDF URLs, 798 distinct files**), and
  **`wp/v2/product?search=` matches post META the rendered page does not contain** &mdash;
  `RP7700107` returned two SmartView products whose HTML contains the string zero times,
  which reads as a hit until you find the real source elsewhere.
- **A TEXT GREP CANNOT PROVE A REBRAND, AND THIS FILE'S OWN BRAND-VANISHED NOTE WOULD HAVE
  FIRED A FALSE FLAG.** This file records, from `3300FSN`, that Avire's current sheets are
  Avire-branded and `RATH` appears zero times &mdash; offered as a vendor-field signal. On the
  `8100-V4G` datasheet, **`RATH`, `Rath`, `AVIRE` and `Avire` each appear zero times in the
  text layer of both revisions**, and a **220 dpi header render shows the logo reads
  &quot;RATH&trade; by AVIRE&quot;**. The branding is logo art. So the store's vendor field is
  correct and needs no flag. **Take a brand-vanished finding from a render, never from a
  grep** &mdash; the same escalation ladder this file demands for tables, applied to a
  letterhead.
  The recorded Avire URL trap was also confirmed **with both controls**:
  `/product/8100-v4g/` returns HTTP 200 with `<title>8100-V4GS</title>`, **seven occurrences of
  V4GS and zero bare V4G**; bogus `?s=` returns 0 of each and the known-good `?s=8100-V4G`
  returns 2. **The endpoint is honest and the product URL is not.**
  **And the real separator is not hardware, which is the finding.** V4G and V4GS agree on every
  published figure &mdash; dimensions, weight, LTE Cat-4 150 Mb/s, the same eleven bands, the
  same battery, ports, antennas and temperature range. What differs is the **service bundle**:
  the V4GS sheet requires the `8100-12VDS` prepaid SIM, and the V4GS *installation manual*
  carries the only first-party sentence naming the bare part &mdash; *&quot;If purchasing the
  8100-V4G without an AVIRE SIM, a separate Verizon Voice and Data SIM card will need to be
  obtained.&quot;* No supersession is stated in four documents.

- **A submaster is not a standalone system (`2500-96XB`, v2b51).** The 2023 RC sheet: *&quot;Command Center and Sub-Master Stations are powered from the Distribution Module&quot;*, and the main unit's *&quot;System Includes Phone &amp; Distribution Module&quot;*. The Rev Sep 25 and 9.4.2026 sheets disagree on off-hook voltage, loop current and on-hook range (the newer gives &quot;20 mA typical&quot; outside its own 22&ndash;29 mA range); only agreed figures published. **The 9.4.2026 ordering table drops the 28, 76 and 96-zone rows without saying why** &mdash; flagged as lifecycle, not asserted. **The Avire media search matches FILENAMES only**: `96XB`, which appears only inside documents, returns `[]` (2 B) exactly like a bogus term, so carry a known-good term (`2500`).
