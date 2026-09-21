# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository status

This repository holds no application source. It is the working root for a
consulting engagement on **thefirealarmsupplier.com** (TFAS), a US Shopify Plus
fire-alarm parts distributor with roughly 19,440 active products. All product
data lives in Shopify and is reached through the Shopify MCP server; the only
files tracked here are this guidance file and `.gitignore`.

## Standing instruction

**Run the enrichment pipeline continuously until the project is complete. Do not
stop between batches to ask permission, and do not sit idle waiting.** When a
batch of research agents is running, use that time to prepare the next slice,
run audits, or apply queued fixes. Report findings as they land; do not pause
for approval to continue.

The one standing exception: changes to **structured product data** that feed
Google Merchant Center (the `vendor`/brand field, product type, pack counts
asserted in titles) are flagged for the owner rather than applied unilaterally.
Description and title corrections need no approval.

## The enrichment pipeline

Goal: replace thin product descriptions with verified copy, working down a
priority list ranked by six-month Search Console impressions.

**The live queue is `ranked_v2_byscore.json`, not `ranked.json`.** See *The
priority list was defective* below: `ranked.json` was built with two
undocumented filters that hid the highest-traffic thin pages, and it is retired.
Its first 555 positions were published (18-21 Sep 2026) and are excluded from
the v2 list; **positions 555-654 of the old list were deliberately abandoned**,
because those 100 products carry 2,888 impressions between them against
1,424,884 still waiting in v2. Do not resume the old list.

Working files live outside the repo, in `/tmp/tfas/enrich/`:

- `ranked_v2_byscore.json` — **the live queue**, 5,074 candidates sorted by
  `impressions x (1 - chars/700)`. Record shape:
  `{"id","handle","title","vendor","type","sku","price","vis","inv","impr","rev","created","score"}`
- `ranked.json` — retired. Kept only as the record of what was published first,
  and as the baseline source for `/tmp/tfas/BASELINE_555_publicadas.csv`.
- `catalogo_full.json` (in `/tmp/tfas/`) — all 16,031 active products with their
  full descriptions, from `bulkOperationRunQuery`. Re-pull it before rebuilding
  the queue; it is a snapshot, not live.
- `v2bNN/slice.json` — the 18-product slice for batch NN
- `v2bNN/agent{1,2,3}.json` — per-agent research output
- `v2bNN/varsA.json`, `v2bNN/varsB.json` — validated publish payloads, 9 each
- `pending_fixes.md` — corrections queued against already-published pages

**Progress: 823 pages published** — 555 from the old list plus v2b01 through
v2b15 — plus 80 title-encoding fixes applied
catalogue-wide. One product,
`SM7100-L8`, was deliberately skipped as unverifiable rather than written from
reseller data.

**Never hand-transcribe product ids into an agent briefing.** On v2b03 all six
ids typed into the prose of one briefing were wrong &mdash; transcribed by eye
from a slice listing and scrambled. Two of the wrong ids were *other real
products in the same batch*, so had the agent trusted the prose it would have
published thermostat copy onto the wrong thermostat pages: plausible-looking,
silent, and discoverable only by chance later. Nothing broke solely because the
briefing also said "read the ids from `aN_in.json`, which is authoritative".

The rule that follows: **a briefing names products by SKU and points at
`aN_in.json` for every id.** Never paste an id, and never write "id X is NOT
yours" corrections &mdash; they were themselves wrong. Agents must take `id`
from the input file and echo it back, and the merge step must assert that each
returned `id` matches the input file before anything is published.

Batch loop: slice 18 products → split 6/6/6 across three concurrent
`general-purpose` research agents → validate → merge → publish in two aliased
`productUpdate` mutations of nine.

### Publishing

Use `mcp__Shopify__graphql_mutation` with aliased batch mutations (`u0:`, `u1:` …),
nine per request. The input type is **`ProductUpdateInput!`** (not `ProductInput!`),
and the tool parameter holding the document is **`query`** (not `mutation`).

### House style for `descriptionHtml`

One single-line string, no newlines.

1. `<p><strong>Brand PartNumber</strong> &mdash; one-line identification.</p>`
2. One context paragraph: what the part does and why it exists.
3. `<ul>` of 4–7 verified specs.
4. Closing paragraph naming the specific sibling parts a buyer could confuse it with.

- 700–1100 visible characters (tags stripped); hard ceiling 1230.
- Tags allowed: `<p> <ul> <li> <strong> <sub> <em>` only. No headings, links, attributes.
- Entities allowed: `&mdash; &quot; &times; &deg; &micro; &ndash; &nbsp; &#937; &amp;` only.
- No raw `"` or `'` characters. Use `&quot;` for inches.
- Titles: `Brand PartNumber Descriptive Name, qualifiers`.

**`&amp;` was added to the whitelist on 21 Sep 2026, and the reason is worth keeping.**
The old list could not express an ampersand at all: `&amp;` was not on it and a bare
`&` is not an entity, so **`AT&amp;T` was literally unwritable in a description**. An
agent hit this on a dual-SIM communicator and had to route the carrier names into the
title instead. Brand names with ampersands recur &mdash; `AT&amp;T`, `Air Products
&amp; Controls` &mdash; and Shopify decodes `&amp;` to a plain `&` on storage anyway,
so there was never a reason to exclude it. **A whitelist that cannot express a real
brand name is a bug in the rule, not a constraint to write around.**

**Titles and descriptions have different character rules, and they do not conflict:**
a description may use `&deg;` and the rest of the whitelist; a **title must be plain
ASCII**, because titles are Merchant Center feed attributes. The earlier decision to
leave `&deg;`, `&reg;` and `&trade;` alone in existing titles was about **not churning
27 titles for a cosmetic**, not a licence to introduce them. So: never put a non-ASCII
character in a title you are writing; do not rewrite an old title purely to remove one.

**The entity and newline rules are input discipline, not storage properties.**
Shopify **decodes HTML entities and re-inserts newlines** when it stores
`descriptionHtml`. A page sent as one line containing `&mdash;` comes back
multi-line containing a raw em dash. The rules still matter at the input end &mdash;
`&quot;` keeps inch marks from terminating the GraphQL string literal, `&#937;`
survives extraction and transport, and the whitelist holds copy to a narrow
repertoire &mdash; but **never audit published pages for entities or newlines.** That
measures Shopify's normalizer, not the copy. A first pass of exactly that audit
flagged 655 of 663 pages, including ones published minutes earlier in the same
session.

**Verify publication against the live catalogue, not the batch manifests.** A sweep
on 21 Sep 2026 found two of 645 "published" pages were never actually written &mdash;
`gamewell-fci-90521-line-filter` (30 chars, correctly skipped as unverifiable but
still counted) and `silent-knight-rbb` (38 chars, a genuine miss). One bulk query
costs 19 seconds; run it every ten batches.

**Re-run at batch 14 (805 pages): clean, and the sweep is now cheap enough to keep.**
All 555 old-list pages and all 270 v2 slice ids are present in the active catalogue
&mdash; **zero missing**. Across both sets exactly **three** pages sit under 400
visible characters, and all three are the knowingly-unwritten ones: `90521` and
`SM7100-L8`, unverifiable by decision, and `BDA-NMP01250`, skipped in v2b13 because
its real manufacturer is Trilogy behind a Sucuri block and the Honeywell Fiplex
Document Center needs a login. **No silent failure has appeared in three batches.**
The non-ASCII title check was re-run at the same time: **56 of 16,031 titles**, and
**all 56 carry only `&deg;`, `&reg;` or `&trade;`** &mdash; the three characters
deliberately left alone, with **zero outside that set**. That is zero drift across
roughly 130 further titles written since the batch-11 sweep, so the ASCII rule is
holding at the point of writing.
**One method note for the next sweep:** the raw count of thin pages was 19, but 16 of
those were the slice of the batch *currently being researched* &mdash; sliced, not yet
written. Exclude the in-flight batch before reading the number, or the sweep looks
like it found sixteen failures every time.

**House style drifted during the project, and reformatting is not worth it yet.**
58 of 645 published pages carry a bullet count outside 4&ndash;7, almost all early
old-list batches written as all-prose before the `<ul>` structure settled. The
content is sound; the shape is not. Those 63 flagged pages carry 861 impressions
each against 1,586 each for the next 63 unenriched pages in the queue &mdash; so
rewriting good copy into the right shape loses to writing copy where there is none.
Revisit after the high-impression band is done.

### Research rules given to every agent

- Never invent a number, dimension, current draw, listing, temperature, or compatibility.
- Never trust search snippets, reseller pages, Amazon, or AI summaries for specs.
  Download the manufacturer PDF with `curl` and extract locally with `pymupdf`.
  For scrambled tables use `page.find_tables()` or `page.get_text("words")` with
  coordinates; when the text layer fails, render the page at 300 dpi and read it.
- **The JCI hub carries Ansul too, under `specialhazards` &mdash; and the segment is
  the business unit, not the brand.** `https://docs.johnsoncontrols.com/specialhazards/api/khub/documents?search=<term>`
  returns a **1,449-document index** in the same shape as the Simplex hub
  (`id`/`filename`/`title`/`metadata`, `ft:locale`, `ft:lastEdition`, non-English
  duplicates), and `search` is ignored there too, so grep the JSON. Download via
  `/specialhazards/api/khub/documents/<id>/content`. The segments `ansul`,
  `ansul-us`, `tycofs`, `chemguard`, `tyco`, `fire`, `johnsoncontrols`, `jci` and
  `ansulfire` **all 404**. So **when a JCI brand seems missing, guess the business
  unit, not the brand name** &mdash; Chemguard, Skum, Pyro-Chem and Williams should
  sit here too. This unlocks Ansul, 27 products and 14,768 impressions of the v2
  queue, and settled a part in two fetches that would otherwise have gone to
  resellers.
- **`/api/khub/maps` has patchy, not partial, coverage of the US fire catalogue.**
  It carried the XMS pull stations, `ILED-XC`, `ABHW-4S` and `HI921` first try, and
  **did not carry the MSM line, `FDT421` or the MTH appliances at all** &mdash; one
  agent grepping it for horn/notification terms got 22 rows of which 2 were fire, the
  rest European HVAC. So it is worth one grep of the `metadata` ProductType field,
  and no more: **when it misses, web-search the A6V asset number and go straight to
  `/go/`**, which has worked every time. A bare
  `sid.siemens.com/api/khub/documents/<id>/content` URL also turns up in search
  results directly, with no `/go/` round trip.
  For a legacy Siemens part, web-search the A6V asset number and go straight to
  `/go/<AssetID>`. Also note `support.industry.siemens.com/cs/attachments/...`
  returns `text/html` at ~440 bytes for the same asset that `/go/` serves properly.
- **Gentex's documented path does not cover the PLACE line.**
  `fireprotection.gentex.com/files/PLACE-Series1.pdf` and `PL1K-Series1.pdf` both
  404. PLACE lives on `placehomesolutions.com`, which is Gentex-operated (Zeeland MI
  footer, Gentex `551-` document numbering) and therefore first-party.
- **Simplex documents: use the Johnson Controls document hub.** A GET on
  `https://docs.johnsoncontrols.com/simplex/api/khub/documents?search=<term>`
  returns a JSON index of ~961 Simplex documents with `title` and
  `documentApiEndpoint`. `search` and `limit` are effectively ignored, so it
  returns the whole index &mdash; grep the JSON rather than trusting ranking.
  Download with `https://docs.johnsoncontrols.com/simplex/api/khub/documents/<id>/content`
  (note the `/simplex/` segment; the bare `/api/` path 404s). This reaches
  current datasheets that are not otherwise linkable, and it settled the 4081
  end-of-line range in one call after four other documents had left a gap.
- **For Resideo and Honeywell Home, the supersession source is the `03-` prefix.**
  `customer.resideo.com` techlit documents under `03-` are the **sell sheets**, and
  those carry the manufacturer's own REPLACES table &mdash; that is how
  `TH1320U4002/U` was confirmed to replace `TH5220D1003/U` and `TH5220D1029/U`.
  Reach for `03-` before `buildings.honeywell.com` on this brand family.
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
- **Manufacturer ordering-syntax blocks beat every other decoder.** Page 5 of the
  Edwards catalogue sheets carries a Model Number Syntax block that decodes any
  G1/G4/GC part letter by letter; Eaton `TD450158EN` Table 3 does the same for Eluxa.
  Reading the syntax block is how `G1VRF` was settled, and it also showed that the
  coordinator's guessed siblings `G1RF` and `G1VF` **do not exist** in the current
  series &mdash; `G1RF...` numbers are the legacy xenon generation.
- **A manufacturer document can contradict itself; prefer the table over the prose.**
  Eaton TD450158EN's A/E Specifications paragraph lists the Eluxa ceiling candela set
  as "15, 20, 110, 150 and 177" &mdash; five values, with 30 and 75 mangled &mdash;
  while Table 4 and page 1 both give the correct six. Anyone quoting the prose
  paragraph publishes a wrong number.
- **Accessory specs often live in the parent panel's data sheet.** There is no BB-100
  data sheet; Notifier `DN-7070` (the NFS2-3030 sheet) carries dimensions and capacity
  for BB-100, BB-200, NFS-LBB and BB-UZC together. Check the parent panel before
  concluding an accessory is undocumented.
- **Go to installation instructions for specs, not the operation manual.** For
  `FCM2041-U3` the installation document carried the full electrical ratings and
  mounting detail and the Operation Manual carried none of it.
- **Siemens: the document index is down, but two ways in work.**
  `https://sid.siemens.com/api/khub/documents` returns HTTP 504 after ~60 s, every
  time. Two proven workarounds: (1) `https://sid.siemens.com/api/khub/maps` **does**
  respond and returns the whole index (~1,276 entries, 8.5 MB JSON) &mdash; grep the
  blob as with the JCI hub, then fetch HTML topic books via
  `/api/khub/maps/<id>/topics` and `/api/khub/maps/<id>/topics/<topicId>/content`.
  (2) **The pretty URL resolves the opaque document id even while the index is down:**
  `curl -D - https://sid.siemens.com/go/<AssetID>` returns `303` with
  `location: .../v/u/<hashId>`, and `/api/khub/documents/<hashId>/content` then serves
  the PDF. So **any Siemens A6V asset number can be fetched directly.** This unblocks
  Siemens, 189 products and 82,982 impressions of `ranked_v2`, and it is what cost
  `SL2HSWR-F` its candela values in an earlier batch.
- **Protectowire blocks `curl` too, but differently from Eaton.** Most
  `protectowire.com/wp-content/...` paths return HTTP 202 with an `sgcaptcha`
  meta-refresh (Sucuri), and the Eaton `urllib`-plus-Safari-UA workaround does **not**
  defeat it; some paths pass intermittently. What works reliably is
  `prod-edam.honeywell.com`, which mirrors Protectowire PDFs verbatim. Given the
  Anixter lesson, cross-check the mirrored revision against any Protectowire-hosted
  document that does come through &mdash; a 2012 mirror and a 2022 original agreed
  exactly on the PHSC temperatures, so there was no generation gap there.
- **Mirror paths must be *found*, not *built* &mdash; including `qdigital.mx`.**
  Calling it "the one path-predictable mirror" was too strong: it worked on paths
  discovered by search and **failed on a constructed one**
  (`/content/Edwards/TSD-CJ/...` returned HTML). Two more hosts that answer with a
  readable HTML shell rather than a 404: `edwards-signals.com/files/<anything>.pdf`,
  and `steelfire.com/UserFiles/Docs/<guess>.pdf`, which returns **identically
  48,687 bytes for every guessed filename** &mdash; a stable fingerprint like EDAM's
  8,047-byte `application/javascript`. Mirrors that served verbatim Edwards PDFs on
  21 Sep: `cdn.lsicloud.net/kendall/Resources/AD/`,
  `externalassets.unilogcorp.com/ASSETS/DOCUMENTS/ITEMS/EN/`,
  `savemoreonfirealarmparts.com`, and `steelfire.com` for a *searched* filename.
  Also note `85001-0584` is the **Intelligent** (Signature/SIGA-SD) SuperDuct sheet and
  is what a search for "SuperDuct datasheet" lands on first; the **four-wire** family
  is documented by bulletin `3100685` and installation sheets `3100686` (sensor) and
  `3100687` (controller).
- **Edwards documents are not on edwardsfiresafety.com.** Every `/documents/`,
  `/products/` and `/literature` path 404s, and `est.net` and
  `edwardsfiresafety.com/files/import/` return an HTML shell for any filename. Edwards
  PDFs have to come from verbatim mirrors, so cross-check two documents of different
  dates against each other. Finding the real Edwards LifeLines library URL is worth
  doing before the next Edwards-heavy batch; several SIGA parts are still in the queue.
- **Functional Devices publishes first-party PDFs through Salesforce CMS, and the path
  is derivable.** Their site is a JS shell and every guessed `/pdf/`, `/downloads/` and
  `/documents/` path 404s, but `robots.txt` discloses `/document/`, and
  `https://www.functionaldevices.com/sitemap-managedcontent-sfdc_cms__document-1.xml`
  lists every document as `.../document/<slug>-<MC-key>`. Swapping the prefix to
  `https://www.functionaldevices.com/sfsites/c/cms/delivery/media/<MC-key>` serves the
  PDF. Two fetches turned a mirror-only brand into a first-party one. **When a brand's
  site is a JS shell, read `robots.txt` and the sitemap before giving up on it.**
- **Two cheap verification tricks worth reusing.** An MD5 comparison **proves** a mirror
  verbatim instead of arguing about it: `prod-edam.honeywell.com`'s
  `hbt-fire-I56-5100-001-manual.pdf` and `mainelectricsupply.com`'s
  `syssbbgwl-8.pdf` are byte-identical at 322,407 bytes. And **a document renumbering
  is not a new product**: Edwards `85001-0581` (2013, EST branding, one model) became
  `E85001-0640` (2020, Carrier branding, three models), and seven years apart the sound
  levels, currents, dimensions and temperature range agree exactly. An `E` prefix plus
  a different number is the same line.
- **`lenel.com` and `cdn.lenel.com` answer HTTP/2 503, 371 bytes, `text/html`, to every
  client** &mdash; curl on both HTTP versions, `urllib` through the proxy, and WebFetch.
  Another stable failure fingerprint, like EDAM's 8,047-byte `application/javascript`.
- **`alarmax.com/customer/docs/skudocs/` filenames are not derivable from the SKU.**
  It is the right host for Eaton, but `syssbbrl-8.pdf` and `SYS-SBBRL.pdf` both 404 for
  System Sensor. Search the filename, same lesson as EDAM slugs and `qdigital.mx`.
- **On `customer.resideo.com/en-US/Pages/Product.aspx`, the `pid` needs the `/U` suffix
  kept and URL-encoded** (`TH6320WF2003%2FU`); bare `TH6320WF2003` returns
  &quot;not a valid material number&quot;. The strip-the-suffix rule applies to
  *searching*, not to this endpoint &mdash; and searching the `33-` document number
  directly was faster than either.
- **Kidde serves its own PDFs and needs no Edwards mirror.**
  `kidde-esfire.com/Content/Documents/` responds directly with no bot protection.
  And the E/K prefix swap is the same line: **`K85001-1021` (Kidde, Issue 1, 2019) and
  `E85001-1021` (Edwards, Issue 1.1, 2020) agree exactly** &mdash; candela set,
  20 &#937; sync limit, 6.8 &times; 1.82 in., every current value. Kidde EGCAVWF is
  Edwards GCAVWF. This extends the `85001-0581` &rarr; `E85001-0640` rule: a prefix
  change on a shared document number is branding, not a different product.
- **Gentex serves datasheets directly** from `fireprotection.gentex.com/files/<Model>-Series<n>.pdf`,
  with no bot protection. Beware though: one Gentex revision has a **blank Part Number
  column** while another populates it, so confirm the catalogue number on the revision
  you actually have.
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
- **A table caption can sit *below* its table, which inverts the obvious reading.**
  Gamewell-FCI `9021-60930` C places captions under the tables they label, so plain
  reading attributes every caption to the table above it &mdash; one row off, silently.
  This is the merged-cell trap's cousin: same fix, `page.get_text(&quot;words&quot;)`
  with y-coordinates, and the same rule &mdash; **never take a row-to-label assignment
  from reading order alone.**
- **EDAM has dropped some Notifier documents entirely.** `DN-7045` 404s under both
  `notifier-us/` and the flat datasheets directory. `honeywellbuildings.in` is a
  Honeywell-operated regional site that still serves them &mdash; first-party, but
  older revisions, so cross-check against a current datasheet before using it.
- **Resideo literature path details that cost fetches:** the working path is
  `/resources/Techlit/TechLitDocuments/<prefix>s/<file>.pdf` &mdash; **capital T in
  `Techlit`**, and the directory is `33-00000s` with **five** zeros. Grepping
  `customer.resideo.com/en-US/Pages/Product.aspx?cat=HonECC+Catalog&pid=<SKU>` returns
  the document paths in one fetch, across the `33-` and `50-` prefixes together.
- **Eaton and Wheelock block `curl`, and the `urllib` workaround has now failed
  too.** Both HTTP/2 and HTTP/1.1 with browser headers fail against eaton.com
  (INTERNAL_ERROR or empty reply) and WebFetch gets 503. Python `urllib` through
  `HTTPS_PROXY` with a Safari user-agent worked on 21 Sep and **failed later the
  same day** on three Eluxa PDFs ("Remote end closed connection without response").
  Treat it as worth one attempt, not as the answer.
  **`www.alarmax.com/customer/docs/skudocs/` is the fallback to try first** &mdash; it
  served `TD450188EN` at its **July 2024** revision, so unlike the Anixter mirror it
  is current. `objects.eanixter.com` still works but **carries superseded revisions**:
  it had the 2016 MT4 datasheet describing xenon flashtubes where the current one
  specifies LED.
  **Eaton document numbers are close together and easy to swap:** `TD450158EN` is the
  Eluxa **high-fidelity speaker** sheet (the one whose A/E prose mangles the ceiling
  candela set), while `TD450188EN` is the Eluxa **outdoor horn/strobe** sheet &mdash;
  and in the latter the A/E prose and the table *agree*. The mangled-prose warning is
  about one document, not about Eaton generally.
- **The sibling part is the dominant failure mode.** Part numbers differ by one
  character and describe different products. Find the full ordering table and
  confirm which row is this exact part before writing anything.
- **The Omega trap:** `Ω` often extracts as the letter `W`. An extracted "50W" in
  a resistance spec is almost always 50 Ω. **Five hits.** The fifth: an Edwards
  wiring diagram rendering a NAC end-of-line as `EOL 15 KW`, settled as **15 kΩ** by
  the technical reference manual. The fourth was Edwards
  literature printing an ordering table as `4.7KW, 3.6KW and 1.1KW` where the
  manufacturer's own technical reference prints the same parts with real &#937;
  symbols.
  **The inverse case is real and more dangerous: a legitimate `W` that looks like the
  trap.** Protectowire prints `Resistance 2W Models: .185 ohms/ft`, where **`2W`
  means two-wire**, as opposed to the three-conductor TRI-Wire line directly below
  it &mdash; not 2 watts and not 2 &#937;. An agent applying the Omega rule
  mechanically would have "corrected" a correct value. Read the surrounding rows
  before substituting; the rule is a prompt to check, not a find-and-replace.
- **The dropped-decimal trap:** a title copied from the adjacent catalogue row
  loses a decimal point and asserts a value ten times too large. Edwards lists
  `EOL-4.7` (4.7 kΩ) and `EOL-47` (47 kΩ) on consecutive rows; the store's
  EOL-4.7 page carried the EOL-47 text while separately stocking the real EOL-47.
  A full scan of the 19,440 active products found exactly one such case, so the
  pattern is closed catalogue-wide, but it recurs whenever a new row is copied.
- **The generation trap:** one document number can cover two product generations
  at different revisions. Confirm the revision covers the part.
- **Heat detectors have three classes, not two.** Fixed temperature and rate of rise
  are the obvious pair; **rate compensation** is the third and a whole product line is
  built on it. A high-expansion shell encases slower struts carrying opposing
  contacts, so on a fast rise the shell lengthens first and the contacts close *below*
  the rating, cancelling thermal lag &mdash; and it self-restores on cooling. A
  briefing that offers only "fixed or rate-of-rise" will push an agent toward the
  wrong answer; Thermotech's `302-ET-135` is rate compensation and neither of those.
- **The adjacent-row trap, in the other direction: reusing a sibling's spec row.**
  `SPWL` (speaker only) is rated **79/82/85/88 dBA** at its four taps; `SPSWL`
  (speaker strobe) is **77/80/83/86**, two dB lower at every tap,
  in the same two documents. Copying the sibling's row would have published a wrong
  number on a page that otherwise looked right. Read the row for the exact part, even
  when the parts differ by one letter and the table looks uniform.
- **The merged-cell trap.** A vertically merged table cell emits its text at a
  position in the stream that implies the **wrong** grouping, and `find_tables()`
  can fail on the same table without erroring. On Simplex `S4906-0001` plain
  extraction put six SKUs under Ceiling and two under Wall in an order that invited
  exactly the wrong assignment. **Only `page.get_text("words")` with y-coordinates
  settles a merged cell.** Re-check any mounting, candela or variant column read out
  of a selection table by plain text.
- **The invisible-dimension trap.** Older Notifier "Document NNNNN" drawings carry
  their dimensions as **vector linework, not text**. For `ABS-2D` (doc 52032)
  `get_text()` returned prose only, `find_tables()` returned garbage, and
  `get_images()` showed nothing but a logo &mdash; **nothing signalled that data was
  missing.** Rendering at 200 dpi and reading the image was the only route. Treat any
  enclosure document whose text carries no inch figures as a render-and-read job.
- **Check `file -b --mime-type` before trusting any extraction.** A 404 that returns
  an HTML shop page still opens in pymupdf and "extracts" pages of navigation chrome
  that read like content. `alldataresource.com` does this, and so does
  `myeddie.edwardsfiresafety.com`, which answers **HTTP 200 with an HTML shell** for
  any filename.
- **The JCI hub has an `autocall` segment too.**
  `https://docs.johnsoncontrols.com/autocall/api/khub/documents/<id>/content` serves
  Autocall documents directly, alongside the known `/simplex/` and `/specialhazards/`
  segments &mdash; more confirmation that the segment is the business unit. Autocall
  part numbers are Simplex numbers with an `A` prefix. Meanwhile
  **`autocall.com/uploads/resources/Datasheets/*.pdf` is blocked and returns 103 bytes
  of `text/plain`** for every request &mdash; a new failure fingerprint alongside EDAM's
  8,047-byte JavaScript and steelfire's 48,687 bytes.
- **On the JCI hub, grep the `filename` field, not the title.** The document that
  settled `4906-9101` is titled "Visible Notification Appliances with Synchronized
  Flash" &mdash; containing neither "4906" nor "TrueAlert". Its filename,
  `S4906-0001.pdf`, is the reliable key.
- **`prod-edam` holds separate `notifier-us/` and `notifier-aus/` trees with
  different documents for the same part number.** Prefer `-us`; a regional variant
  may genuinely differ. Also, an old revision on EDAM is not necessarily superseded
  &mdash; `DN-6643:A1` is from 2008 and is still the newest Notifier publishes for
  the NBG-12 Series.
- Never state stock, lead time, or condition.
- **A second innocent origin for a false &quot;replaces&quot; claim: the data-sheet
  revision line.** Siemens sheets carry `Supersedes sheet dated 5/06 (Rev.1)` in the
  footer. **That supersedes a *document*, not a product**, and it sits on exactly the
  older sheets a reseller would be reading. Grepping for `supersed` therefore returns a
  hit on almost every legacy Siemens sheet that means nothing about the catalogue. Read
  what the word is attached to before counting it.
- **Splitting a sibling pair across two agents is worth doing, and the disagreement is
  the point.** `IO-SDC1` and `IO-SDC2` went to different agents with instructions to
  establish the real separator and to compare shared figures afterwards. Both
  independently found the same two differences &mdash; loop count *and* host panel, the
  iO-SDC1 being the only one that fits an iO64 &mdash; which neither could have guessed
  from the numeral. **And the cross-check caught a live defect:** one agent published
  `80 mA alarm` while the other established that `E85001-0135` **contradicts itself on
  alarm current in both revisions checked** (card table 80/70 mA, panel Loop-circuit
  block 125/115 mA) and had omitted it. The contradicted figure was removed before
  publishing, from the bullet **and from the closing paragraph, where it had survived
  the first pass**. Standby, which agrees across both tables and revisions, was kept.
  **Pair-split the obvious sibling pairs, and diff the shared numbers at merge.**
- **The Siemens coexistence sentence, misread as supersession. Hit twice; assume it
  is behind every Siemens "Replaces" claim.** Siemens data sheets carry an
  Installation paragraph of the form *"Model X may be installed on the same SLC with
  the following &hellip; Y devices"*. That is devices sharing a loop, not one
  replacing the other. Two store titles were built on it:
  `XTRI-D "(Replaces HTRI-D)"` and `OH921 "(Replaces HFPT-11)"`, and **neither claim
  appears in any Siemens document.** The OH921 case is worse than a bad cross-
  reference: HFPT-11 is the FirePrint *thermal* detector, a heat detector, while
  OH921 is photo-plus-thermal multi-criteria &mdash; and the store stocks an HFPT-11
  page separately. The heat-only member of the 921 family is `HI921`. Both titles are
  corrected, with the interoperability statement moved into the body.
- **Two current parts in parallel document lines look exactly like a supersession
  pair from outside.** `4099-9005` carried "(Replaces 4099-9002)". `4099-9002` is a
  real, current Simplex part &mdash; listed in `S14099-0001` Rev 7 (02/2021) &mdash;
  and `4099-9005` sits in `S4099-0005` Rev 4, **the same revision month**. Two
  concurrent document lines (one IDNet-only/ULC-oriented, one IDNet-or-MAPNET II),
  neither stating a replacement in either direction. So "the other part still exists
  and is documented" does **not** disprove a supersession claim, and it does not
  support one either; only a manufacturer statement settles it.
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
- **A "Replaces X" claim belongs in a title only when a manufacturer document states
  it.** Three claims in one batch gave three different answers: `PC2WL`&rarr;`PC2WLED`
  is stated outright in a Honeywell bulletin and stays in the title; `SPSCRLED` vs
  `SPSCRL` is unstated but strongly supported by omission across two datasheet
  revisions; `GN-503`&rarr;`SC` is a sound *distributor* equivalence that Gentex
  never makes. When it is not manufacturer-stated, **move it to the body** &mdash;
  the part number still earns the query match, without a feed attribute asserting
  something unsourced. Titles feed Merchant Center, so an unverified claim there
  costs money in two channels.
- **The owner's structured-data decisions are consolidated in
  `/tmp/tfas/DECISOES_DO_DONO.csv`** &mdash; 29 items as of 21 Sep 2026, each with
  the current value, a recommendation, the reasoning, and a confidence column that
  separates **10 demonstrably wrong** values from **6 judgement calls**, **4 feed /
  lifecycle decisions** and **3 unsourceable pack counts**. Append to that file
  rather than letting flags scatter across batch notes; ten batches of scattered
  flags is what made the consolidation necessary.
- **Titles must be plain ASCII, and 80 were not.** A catalogue-wide scan on
  21 Sep 2026 found **136 of 16,031 active titles carrying non-ASCII characters**,
  carrying 52,451 impressions. 80 were normalised (curly quotes and primes to
  `&quot;`-equivalent plain quotes, `&times;` to `x`, en dash to hyphen, vulgar
  fractions to `3/4` and `1/2`, bullets to hyphens); `&deg;`, `&reg;` and `&trade;`
  were deliberately left alone as harmless and widely accepted. Five were **not
  styling but corruption**:
  - `Edwards 868STRC-AQ` carried **double-encoded UTF-8 of a zero-width space**
    (`U+00E2 U+20AC U+2039`) immediately after the part number, so the part number
    did not match itself. **The corruption had already leaked into the handle**
    (`edwards-868strc-aqa`), which was left alone to avoid breaking the URL.
  - Two titles contained a literal **`&nbsp;`** &mdash; titles are plain text, not
    HTML, so it displayed as those six characters.
  - `Aiphone IXGW&#8209;LC` used a **non-breaking hyphen** inside the part number,
    so a search for `IXGW-LC` could not match it.
  - A Napco title used `&#9679;` as a sentence separator.
  **The corruption clusters: 33 of the 80 are Aiphone and 34 sit in the newest
  product-id block**, which points at a specific import rather than gradual drift.
  Check titles for non-ASCII after any bulk import, and remember titles are Merchant
  Center feed attributes &mdash; a mangled part number costs money in both channels.
- **Discontinuation is a feed decision, not a copy decision.** Four SKUs in one batch
  were marked discontinued by their own manufacturer while carrying live prices and
  feed entries. House rules keep lifecycle out of the copy; that leaves the question
  open rather than answered, so it goes to the owner.
- Unverifiable claims go in an `unverified` array with the reason, never in the copy.
- Always ask agents to contradict the briefing. **Seven** of the coordinator's own
  premises have been proven wrong this way; that is the point.
- **A generalisation that survives one test still needs its boundary found.** The
  Protectowire rule "listed spacing is a function of temperature, not jacket" was
  derived on the XLT jacket, tested again on EPC, and **breaks at 220 &deg;F** &mdash;
  PHSC-220-EPC and -220-XCR have **no UL spacing at all** and FM 25 ft. Max ambient is
  likewise temperature-driven at 190 &deg;F but jacket-driven at 356 &deg;F (EPC 221,
  XCR 250). Confirming a pattern twice is not the same as knowing where it stops.
- **For any PAM-series relay, go to `apcfire.com/wp-content/uploads/` first.** Air
  Products and Controls publish their own current sheets there &mdash;
  `DS-RL-1-G25-PAM-Series.pdf` (2026-01) tabulates PAM-1/-2/-4/-SD side by side. The
  Honeywell/Fire-Lite mirror `DF-52068:A` is from **2014**, is **superseded** (it gives
  the PAM-4 coil floor as 9 VDC where APC now says 12), and is **internally
  inconsistent** (its table says the PAM-4 has an LED; APC's says it does not). An
  agent had a correction drafted off that mirror and killed it after reading APC's own
  sheet.
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
- **The coordinator may tighten or soften agent copy, but must not introduce a new
  factual claim without agent-grade research.** Every inline edit made during
  publishing on 21 Sep 2026 was checked afterwards. The ones that restated an agent's
  sourced finding, or that made a claim *weaker* (keeping a catalogue number in
  parentheses rather than promoting it, softening an inferred bracket claim, restoring
  a `/U` suffix), were all sound. **Both edits that went wrong were the two where the
  coordinator supplied the substance** &mdash; the RA100Z rewrite and the THM04R3000
  swap. The pattern is clean enough to be a rule.
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
- **The same mechanism on the `vendor` field fires almost not at all, which is itself
  the result.** 42 families, **2** split across brands. `B501` has four members under
  System Sensor and one, `B501-BL`, under Fire-Lite &mdash; and Honeywell genuinely
  sells that base under several brands (Notifier `DN-62046:C` lists it too), so no
  brand is *wrong*; the defect is the store disagreeing with itself inside one family.
  `E3-TRIMKIT` has the `-A` under Gamewell-FCI and the `-B` and `-C` under Honeywell,
  and **here the minority is the correct one**: the E3 series is Gamewell-FCI's panel
  line and &quot;Honeywell&quot; is the generic umbrella. Second outing, second time the
  outlier-is-not-the-defect caveat fired.
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
- **A headline spec can be conditional on a setting the datasheet does not mention.**
  E2S datasheet `1-21-200` headlines *&quot;86.37cd &ndash; UL1971 Public mode
  fire&quot;* with no qualifier. Instruction sheet `D191-00-261-IS Issue 3` Tables
  3A/4A/5A show that 86.37 cd is the on-axis value **at the 1 Hz / 60 fpm flash setting
  only**; the same unit is **58.57 cd at 1.33 Hz and 51.65 cd at 1.5 Hz**. A designer
  who sets 90 fpm on a layout drawn for 86 cd is about 40% short. The same sheet is the
  only place the **UL 1638** listing appears &mdash; the datasheet names UL 1971 alone.
  **Generalises: when a datasheet states a single value for something the device can be
  set to vary, find the instruction sheet's table before quoting it.** This is the
  prose-versus-table rule pointing across documents rather than within one.
- **A summarising fetch can manufacture a lifecycle claim out of page chrome.** An agent's
  WebFetch of a Honeywell Buildings SWIFT page reported the product *&quot;marked as
  discontinued&quot;*. Curling the same page shows `Discontinued` appears **only as a UI
  label string inside the page JavaScript** (`discontinuedText`), attached to nothing.
  Had that reached the owner it would have been a discontinuation flag on a live product,
  sourced from a template. **Never take a lifecycle claim from a summarising fetch; curl
  the page and find what the word is attached to** &mdash; the same discipline the
  Siemens `Supersedes sheet dated` footer already demanded, one layer further out.
- **DITEK: the coordinator's `-R5`/`-R8` filename premise was invented, and the host has
  a fingerprint.** `DTK-2MHLPF-Series-DS-R5.pdf` and every `R4`&ndash;`R9` variant return
  **HTTP 404 with an HTML shell of exactly 152,678 bytes** &mdash; a new stable failure
  signature for `diteksurgeprotection.com`. Real filenames carry no revision at all and
  are linked from the **series page**, and the current revisions are **Rev 6 and Rev 19**,
  not 5 and 8. What the documents do settle decisively: `DTK-2MHLP24FWB` (F) and
  `DTK-2MHLP75BWB` (B) are identical on service voltage, MCOV, clamping voltage and the
  20,000 A surge rating and differ in **exactly two rows** &mdash; max continuous current
  **1 A against 5 A**, and failure mode **open circuit against short to ground**. And
  **`WB` is manufacturer-stated**: *&quot;includes single position mounting base&quot;*.
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
- **A correction can introduce a new error, so corrections need verifying too.**
  The RA100Z closing paragraph was rewritten on 21 Sep 2026 to fix two real faults,
  and the rewrite asserted that *"the RTS151 and RTS151KEY are key-operated remote
  test stations"*. **The RTS151 is magnet-operated** &mdash; it ships with an M02-04
  test magnet and has no key at all; the `KEY` suffix on its sibling is the entire
  difference between the two part numbers, and the sentence collapsed it. Caught two
  batches later only because the APA151 came through the queue and its agent was
  asked to rule on the live text. **Put corrected pages back through cross-reference
  review; do not treat a correction as settled because it fixed what it set out to
  fix.**
- **The product-class error is the most common real defect in this catalogue's
  titles &mdash; six cases now, and the last two both came from the manufacturer's own
  wording.** A relay sold as a
  resistor (`EOLR-1`), a riser monitor as a plain monitor (`SIGA-RM1`), a controller
  as a detector (`TSD-CJ-C01`), a horn strobe as a horn (`MTH-MC-R`), and a panel CPU
  as a display (`CPU2-3030D`). **The last one came from the manufacturer's own
  wording:** "NFS2-3030 Primary Display" is Notifier's verbatim heading in DN-7070,
  but it names the part's *role* and reads as an add-on annunciator, when the part is
  the CPU that the panel cannot run without. It is also the first where the Shopify
  `type` field gave no warning &mdash; it said "Annunciators", leaning the same wrong
  way. **So the type field is a useful signal when it disagrees and no signal at all
  when it agrees; verify the class from the document either way.** The sixth is
  Simplex `4100-9701`, typed **Annunciators**: `S4100-1031` Rev. 22 Table 8 lists it
  as the 4100ES **master controller** &mdash; 32-bit controller board, CPU card holding
  the site program, IDNet 2 loop card and the ES-PS supply. The panel does not run
  without it. That is the CPU2-3030D shape exactly, one generation of panel later, so
  **treat any &quot;display&quot;, &quot;annunciator&quot; or &quot;interface&quot;
  wording on a panel-family part as a class question until the ordering table settles
  it.**
- **Two more product-class errors, and both confirm that the type field is silent when
  it agrees.** Seventh: `BDA-OIA-698869-3-1` had **no class noun in the title at all**
  and a `type` of **BDA**, while Honeywell's own `HON-62089.01` is headed
  &quot;INDOOR OMNI CEILING ANTENNA&quot; &mdash; a BDA is the four-figure amplifier
  this $19.50 antenna plugs into. Eighth: `P2WLED-P` was titled a **strobe** and typed
  **Strobes**, while `AVDS916-01`'s ordering table reads
  *&quot;P2WLED-P &mdash; 2-Wire, Horn Strobe, Wall, White, Plain&quot;*; it has an
  eight-position tone switch and a UL 464 listing, and the strobe-only part is a
  different number, `SWLED-P`. **In both cases the type field agreed with the wrong
  title and so raised nothing.** That is the rule working as stated, not failing: the
  field is a signal on disagreement and no evidence at all on agreement.
- **The SIGA-HRS supersession claim is settled, and what settled it was a
  consequence, not a citation.** Two agents in different batches searched independently
  &mdash; `E85001-0647` in **both** its revisions (Issue 2.1, 2018 and Issue 2.2, 2020)
  and the legacy `85001-0243` Issue 6 &mdash; for HRS, HFS, replac, supersed,
  discontinu and legacy, in both directions, and found nothing; every claim traces to
  resellers. That alone was only a bounded negative and the title was left alone for a
  batch. What decided it: **the two generations carry different UL listed spacing,
  70 ft for HFS/HRS against 50 ft for HFD/HRD.** A successor with *shorter* listed
  spacing is not a drop-in &mdash; a layout drawn on 70 ft needs more devices when
  re-equipped &mdash; so an unqualified &quot;Replaced by&quot; in a feed title was not
  merely unsourced but misleading in a way that costs the buyer. Claim moved to the
  body with the spacing difference stated. **Generalises: when a supersession claim
  cannot be sourced, look for a spec that would have to be equal if it were true.**
- **Ninth product-class error, and the first where the store contradicts itself.**
  Gentex `STRR` was titled &quot;Multi-Criteria Smoke **Detector**&quot; and typed
  &quot;Multi Criteria Detectors&quot;, so the type agreed and raised nothing. Gentex's
  own document calls the whole family a **&quot;Smoke Alarm&quot;** and lists it under
  **ANSI/UL 217 9th Edition**: a self-contained 120 VAC dwelling-unit alarm with its own
  horn and a 9V battery, which is a materially different purchase from a UL 268 system
  detector on an SLC. **The store's own sibling page for the SR was already titled
  &quot;Smoke Alarm&quot;**, so the catalogue disagreed with itself and nobody noticed.
  When two pages in one family use different class nouns, one of them is wrong.
- **The appliance-only trap: a part that is merchandised as a finished product but
  ships as bare electronics.** Autocall `A49CMT-APPLW` was titled &quot;Conventional
  Mount Appliance&quot;, which contains no class noun at all and names a mounting style
  that does not exist. `AC49CMT-0001` Rev. 7 heads Table 2 *&quot;Separate mounting
  plate, **required** when ordering model A49CMT-APPLW&quot;* and Table 3 the same for
  covers; the finished horns `49CMT-WRF` and `49CMT-WWF` *&quot;include cover and
  matching mounting plate&quot;*. So the buyer receives a horn with no cover, no plate
  and no lettering. This is the `4099-9015` shape one step worse, and it is the second
  time in three batches. **Check the ordering table for the word &quot;required&quot;
  before assuming a catalogue number is a complete product.**
  **A trap avoided inside it:** the trailing `W` does **not** mean white. Word
  coordinates show that row's Cover-colour and Wording cells are **empty**, with
  &quot;Select cover and mounting plate separately&quot; spanning both, while the rows
  above do carry Red and White. Colour is set by the cover ordered separately, so
  titling it white would assert what the manufacturer deliberately leaves open.
- **A part can be merchandised as its general family when it is the special case, and
  that is worse than a wrong class noun.** Simplex `4099-9015` was titled *&quot;Double
  Action Addressable Manual Pull Station&quot;* &mdash; not false, but it is documented
  in its own datasheet, `S4099-0006`, as a station **for releasing applications**, and
  it **ships with a blank front panel**: the buyer must separately order label kit
  `4099-9802` to mark it clean agent, CO&#8322;, foam, sprinkler or manual release.
  Someone shopping for an ordinary Simplex double-action station received an unmarked
  agent-release station and a part number they did not know to order. Corrected.
  **The agent found it only by continuing past three negative results** &mdash; the part
  is in none of `S4099-0005`, `S14099-0001` or `S4099-0008`, the three obvious
  manual-station datasheets. **Wrong document family, for the third time.**
- **A lossy slice file silently disarms the catalogue's best cross-check, and both
  agents will report the loss as a fact about the catalogue.** Building v2b13 from the
  revenue CSV, the coordinator wrote `'type': ''` into every `aN_in.json` because that
  CSV did not carry the field. Two agents then reported, as a finding, that all their
  products had an empty Shopify `type`. **Only 1 of the 264 is actually empty, and
  catalogue-wide only 52 of 16,031 (0.3%).** The agents were reporting the input file,
  faithfully. This is the hand-transcribed-id failure in a new shape: **a briefing that
  is wrong in a *blank* is harder to catch than one wrong in a value**, because nobody
  disputes a blank.
  It cost real signal. Restoring the field and re-reading the 18 products against the
  agents' own class conclusions immediately produced **two disagreements, both real**
  &mdash; `HONBDA-7S27B-IB-10` and `OSE-HPW` below. **The rule: any slice file must be
  built from `catalogo_full.json`, carrying `type` and `handle` verbatim; never
  default a field the agents are asked to reason about.**
- **The product-class error has a signature, and it has now fired three times:
  the type field names a *subcomponent* or a *role*, not the product.** `CPU2-3030D`
  was typed Annunciators and is the panel CPU; `4100-9701` was typed Annunciators and
  is the 4100ES master controller; **`HONBDA-7S27B-IB-10` is typed Annunciators and is
  an $8,948 all-in-one public-safety BDA that happens to contain an annunciator.** Its
  three siblings in the same family are all typed BDA. So: **&quot;Annunciators&quot;
  on a part that costs more than an annunciator is a class question every time**, and
  a family whose members disagree on type is a defect, not a nuance.
- **Two structured fields wrong the same way corroborate each other.** `OSE-HPW` has
  vendor `Vesda` and type `Aspirating Smoke Detectors`. VESDA is Xtralis's aspirating
  line; **OSID (Open-area Smoke Imaging Detection) is a separate Xtralis line**, and
  every manufacturer document says &quot;OSID by Xtralis&quot;. An OSID emitter is
  open-area optical imaging, not aspiration. The agent found the brand error from the
  documents and the restored type field confirmed it from a second direction. Honeywell
  owns both lines, which is presumably how they merged. **Decide vendor and type
  together when they are wrong together.**
- **The pack count IS manufacturer-stated &mdash; in a document nobody had opened.
  Four searches across two batches concluded &quot;unsourceable&quot; and all four were
  bounded wrong.** System Sensor document **`9021-62013-E`** (L-Series Low Frequency)
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
  family's* sheet. Second, and new: **`AVDS910-02` (2020) is the earlier revision of
  the very same product and does NOT carry the footnote &mdash; it was added in the
  later `9021-` numbered revision.** So on this brand, **prefer the `9021-xxxxx-E`
  document over the `AVDS` one**, and a negative in an old revision says nothing about
  the current one. Scope and per-SKU basis in `/tmp/tfas/PACKCOUNT_decisao.csv`.
- **The pack-count negative is now a rule with a boundary: Honeywell states bulk packs
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
  outright, and `9021-62013-E` states the LF sounders. So the split is not by brand and
  not by document age: **Honeywell states a carton quantity for bases and LF sounders
  and declines to for strobes, horn strobes and speakers.** That converts
  &quot;six documents checked&quot; from a bounded negative into a positive finding
  about how this manufacturer documents, which is the bar the `SPCWL` case set &mdash;
  *a mechanism beats a missing row.* The remaining titles rest on convention, and
  **the cheapest authoritative fix is still a purchase order or a carton label**, not a
  tenth document.
- **The boundary is now proved on a single page, which is as clean as this gets.**
  Notifier `DN-62046:C` lists the 951 self-test detectors in its Product Line
  Information block with **no `-BP` variant of any kind**, and immediately beneath, in
  the Intelligent Bases sub-block on the same page, states
  **&quot;B300-6-BP: Bulk pack of B300-6, package contains 10&quot;** and
  &quot;B501-WHITE-BP: Bulk pack of B501-WHITE contains 10&quot;. Not two documents
  disagreeing, not two revisions, not two brands &mdash; **one page, one author, one
  date, stating the carton quantity for the base and declining to for the detector
  sitting above it.** So the rule is: **Honeywell states a carton quantity for bases,
  and for the low-frequency sounders via the `9021-62013-E` footnote, and for nothing
  else.** Detectors and notification appliances both fall outside it.
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
- **The pack-count audit itself had the wrong document family &mdash; sixth instance.**
  Two of the 22 open rows are **Gamewell-FCI**, not System Sensor: `AOM-2RF-BP` and
  `MS-7AF-BP`. Both were recorded as &quot;six documents checked&quot; where all six
  were System Sensor L-Series appliance sheets that could not mention a Gamewell relay
  module or pull station under any circumstances. Checked properly now:
  `9020-0625` Rev I 04/19 lists only `AOM-2RF` in Ordering Information with zero
  occurrences of BP/bulk/pack, and `9020-0616` Rev F 11/17 lists twelve MS-7 variants
  and no `-BP`. Both are still negatives &mdash; but they are *now* negatives, and were
  not before. **A negative result is only worth what the document family is worth; an
  audit that carries one brand's citation list across a vendor boundary is asserting
  something it never checked.**
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
- **The Sucuri fingerprint has a second host, and a blocked site is not an undocumented
  one.** `trilogycoax.com` answers **HTTP 202, 169&ndash;193 bytes, with a
  `/.well-known/sgcaptcha/` meta-refresh** on `/`, `/products/`, `/robots.txt` and
  `/sitemap.xml` alike &mdash; the exact protectowire.com shape. The part behind it,
  `BDA-NMP01250`, is a Trilogy product sold under a Honeywell SKU, and the Honeywell
  **Fiplex Document Center requires sign-in**. That is a **bounded** negative: one
  owner login would settle it. Recorded as a retry, not a permanent skip.
- **Identical third-party listing files prove a single manufacturer.** The MR-relay
  brand tangle &mdash; one family under four store vendors &mdash; was settled not by
  any website's claim but by APC's and Space Age's documents citing the **same** UL
  `S3403`, MEA `73-92-E` and CSFM `7300-1004` files. One listee, one manufacturer,
  two catalogue numbers. Use this whenever a brand question looks unanswerable.
- **A part's own name can misdescribe its product class, and the store title will
  inherit the error.** `EOLR-1` was briefed &mdash; by this file's coordinator, as a
  stated fact &mdash; as an end-of-line resistor, and the store title read "System
  Sensor EOLR-1 End-Of-Line". System Sensor manual I56-2185-004 calls it an *epoxy
  encapsulated SPST normally open relay activated by 9 to 40 VDC*. It has **no
  resistance and no wattage at all**. A buyer searching for an EOL resistor was
  landing on a relay. Note the Shopify `type` field said "Relays" and was right while
  the title was wrong: **when a structured field disagrees with the title, that is
  a signal, not noise.**

## Conventions

- Battery capacity, pack counts, and fiber mode (single vs multi) in titles are
  the highest-risk fields. Verify them against a manufacturer document every time.
- Do **not** add "Non-Fire", "(Security)", or "Not Fire Rated" to product titles.
  Owner's decision. Such warnings belong in the description body only. Using a
  manufacturer's own product name is fine even when it contains such a word.
- Scratch scripts and datasheet PDFs produced during research are gitignored.

## Catalog state (21 Sep 2026)

19,442 products total: **16,031 active, 3,411 archived**. The archive wave
completed: 701 ROHN plus 2,708 mature candidates imported via Matrixify.

## Demand data: the full Ahrefs sweep

Every SKU in the catalog (19,438 distinct) was measured against Ahrefs US search
volume. **1,522 SKUs carry demand of ≥20/month, totalling 120,600 searches.**
Results live in `/tmp/tfas/demanda_ahrefs_COMPLETO.csv`.

Top vendors by demand: Resideo 290 SKUs / 20,400 per month; Honeywell Home 53 /
18,360; System Sensor 162 / 13,010; BRK Electronics 41 / 9,710; Notifier 121 /
7,070; Fire-Lite 65 / 6,000; Simplex 100 / 4,550; Aiphone 63 / 4,160.

### Method traps proven by this sweep

- **Selection effect.** An earlier sweep covered only 8,763 SKUs and found a 2%
  hit rate. That population was *defined* as zero-impression and zero-stock, so
  the low rate was built in. The live catalog hits 36%. Never infer catalog-wide
  demand from the archive-screening population.
- **Catalog SKU suffixes.** Resideo and Honeywell SKUs carry `/u`, `/b`, `/e`,
  `/a`. Querying them literally returns nothing. Strip the suffix first — doing so
  uncovered the entire Resideo hydronic and thermostat line.
- **Numeric part numbers are not uniformly dead.** Simplex, Notifier and
  Fire-Lite numerics have real volume (`4098-9714` at 350/month). Kidde Fenwal,
  Hochiki, Apollo and Det-Tronics numerics return essentially zero — 1 hit across
  ~1,900 Det-Tronics part numbers.
- **The 100-row cap.** `keywords-explorer-overview` silently truncates at the
  `limit`. When a batch returns exactly 100 rows, re-run ascending and, if still
  capped, with a raised threshold. Five of thirteen batches capped.
- **Short SKUs are noise.** Bare acronyms (`spc` 78k, `bcm` 60k, `csb` 24k, `l1`
  6.5k, `rome` 234k) return real volume for unrelated subjects. Exclude SKUs under
  4 characters and keep a noise list.

## Collections

204 collections exist. Only ~50 rank for anything, together drawing roughly
1,000 visits per month. Analysis in `/tmp/tfas/oportunidade_colecoes.csv`.

**Generic category terms are the wrong target.** "covers" (34,000/month) is
noise; the page actually ranks #5 for **"fire alarm cover"** (350/month). The
qualifier carries the commercial intent.

**But the qualified terms do not convert into a collection-page opportunity
either.** Three SERPs were read before writing any copy, and all three killed the
premise:

- **"duct smoke detector"** (800/month, KD 0, collection at position 23). Page one
  is YouTube, a Honeywell PDF, a People Also Ask box, Google Shopping carousels
  and two code/informational articles. The only retailer category pages are
  Ferguson at #5 and Jackson Systems at #7.
- **"fire alarm battery"** (3,000/month, KD 0). Intent is a homeowner with a
  chirping smoke alarm: First Alert's "How to Replace 9V Batteries" article pulls
  2,859 visits, then Shopping carousels, PAA, Amazon, Reddit and Quora. One
  commercial category page in the whole top ten, at #8. TFAS sells SLA panel
  batteries to contractors — wrong audience.
- **"fire alarm annunciator"** (900/month). Page one is YouTube, PAA ("What is an
  annunciator", "Is it required"), Honeywell's Australian site, two eBay listings
  and three forum threads. **No e-commerce category page at all.**

Three lessons, all costly if missed:

1. **KD does not measure SERP features.** A KD 0 term whose page one is video,
   PAA and Shopping has almost no organic real estate. Read the SERP before
   valuing a keyword.
2. **Where commercial results appear, they are individual product listings** —
   Google Shopping, eBay, Amazon — not category pages. Positions 3 to 5 on these
   terms draw only 30 to 60 visits per month.
3. **This validates the product-page pipeline over a collection frontier.** The
   1,522 SKUs with part-number demand are the real asset, because part-number
   searchers are qualified buyers and product pages are what rank for them.

The collection work worth doing is therefore narrow: the pages already ranking
3–7 for qualified long-tail ("fire alarm cover" #5, "commercial smoke detector"
#3, "pull down fire alarm" #7) earn 80–100 visits each and can be nudged. The
implied redirect is **Google Merchant Center**, since Shopping owns the
commercial slots — which ties directly to the structured fields already flagged
for the owner (vendor/brand, product type, pack counts).

`/collections/simplex?page=12` ranks #2 for "simplex fire alarm" (900/month) and
is the single biggest collection traffic source at 212 visits. A paginated page
holding a head term is fragile — any catalog reorder moves it.

## The priority list was defective — rebuilt as ranked_v2.json

Found 21 Sep 2026 while checking whether the ERP revenue data should reorder
the queue. It should not, but looking for the answer exposed something worse.

`ranked.json` was built with **two undocumented filters**: a description of
**50 characters or less**, and **stock greater than zero**. Every entry obeys
both (max desc 50 chars, min qty 1). Anything in the 51-700 character band was
therefore never a candidate, however thin and however much traffic it drew.
That band holds the most valuable thin pages in the catalogue.

The whole catalogue was then pulled with `bulkOperationRunQuery` (16,031 active
products, 19 seconds, output in `/tmp/tfas/catalogo_full.json`). **The median
active product carries 68 visible characters of description; 13,867 of 16,031
are under 700.**

### ranked_v2.json

Rule: **active, impressions > 0, visible description under 700 characters**,
sorted by impressions descending, stock as a tiebreaker and never a filter.
The 555 pages already published are excluded.

**5,074 candidates carrying 1,537,073 impressions and $39.8M of revenue** —
against the old list's 165,818 impressions. **9.3x larger.** 4,975 of them
were never in the old list at all. The top 100 alone hold 402,142 impressions,
2.4x the entire old project.

| band | products | impressions | revenue |
|---|---|---|---|
| A, under 120 chars | 3,274 | 867,989 | $23.9M |
| B, 120-349 chars | 1,322 | 369,054 | $12.1M |
| C, 350-699 chars | 478 | 300,030 | $3.8M |

Work it by `ranked_v2_byscore.json`, which sorts by `impressions x (1 - chars/700)`
so effort lands where both traffic and the text deficit are largest. Batches are
named `v2bNN/`.

Worked examples of what the old filters hid: Notifier AFP-100 (15 chars, 10,211
impressions, excluded by the stock rule), Lenel LNL-1320-S3B (56 chars, 8,201),
Gamewell-FCI MS-7LOB (544 chars, 13,627), Napco SLE-MAX2-FIRE (164 chars, 6,123,
$201,628), Fire-Lite MDF-300 (190 chars, 2,633, $215,312 — its impressions alone
would have ranked it position 3 of the old list).

**The remaining 100 products of the old queue carried 2,888 impressions between
them, 29 each. The first v2 batch of 18 products carries 112,189** — 68% of the
old project's entire impression base in one batch.

**The lesson generalises: never inherit a candidate list without measuring the
filters that built it.** This one was worked for 33 batches before anyone asked
what defined membership.

## Where this queue stops paying — measured at batch 10 (21 Sep 2026)

281 batches of 18 is the whole v2 queue. **179 products are done, capturing 487,458
of the 1,537,073 impressions &mdash; 32% of the value in 3.5% of the work**, which is
what a steep long tail looks like from the good end. The curve from here:

| band | products | impressions | per batch | ERP revenue | rev/impr |
|---|---|---|---|---|---|
| next 14 batches (to 50% of v2) | 252 | 278,061 | **19,861** | $7.0M | $25 |
| batches 25&ndash;67 (to 75%) | 774 | 385,637 | **8,968** | $12.5M | $32 |
| batches 68&ndash;135 (to 90%) | 1,224 | 230,230 | **3,385** | $8.6M | $38 |
| batches 136&ndash;281 (last 10%) | 2,645 | 155,687 | **1,066** | $4.6M | $30 |

**The last 146 batches are 52% of the remaining work for 10% of the remaining
impressions**, at 59 impressions per product. The old queue's abandoned tail was 29
per product, and abandoning it was right; this tail is twice that, which is marginal
rather than obviously worthless.

**Three things this settles:**

1. **There is a natural stopping point around batch 135**, where per-batch value
   falls to ~3,385 and then to ~1,066. Plan for it rather than drifting into it.
   Even band 3 alone (230,230 impressions) still exceeds the *entire* old project's
   165,818, so nothing before batch 135 is hard to justify.
2. **Revenue per impression stays healthy across every band ($25&ndash;38).** The
   tail is thin by traffic, not junk by value &mdash; so the stopping argument is
   about cost per batch, not about reaching worthless products.
3. **The thermostat problem has solved itself.** Honeywell Home and Resideo are now
   **328 products, 5% of remaining impressions and 0.0% of remaining revenue**. The
   $0.23-per-impression concentration was in the first 100 positions and the queue
   has passed it. The bounded experiment is no longer needed to protect the queue,
   though the 30-day measurement still answers whether enrichment works at all.

**What follows batch 135, when it comes:** the second frontier already identified
&mdash; the 86 products that sell *and* have Ahrefs demand *and* few impressions
($672,002, 4,430 searches/month, 81 of them outside this queue), in
`/tmp/tfas/ALVO_enriquecimento_vendas.csv` &mdash; then the narrow collection work,
then Merchant Center. Per-batch projection in `/tmp/tfas/CURVA_DA_FILA.csv`.

## The thermostat problem: high traffic, almost no revenue

Measured 21 Sep 2026 after noticing six Honeywell Home thermostats in one v2
slice. The pattern is real and it cuts against a pure impressions sort.

| vendor in the v2 queue | products | impressions | revenue | revenue per impression |
|---|---|---|---|---|
| Honeywell Home | 41 | 114,498 | $26,900 | **$0.23** |
| Resideo | 307 | 36,208 | $6,848 | **$0.19** |
| System Sensor | 322 | 127,744 | $6,231,749 | $48.78 |
| Simplex | 467 | 141,783 | $2,983,612 | $21.04 |
| Vesda | 146 | 42,139 | $5,653,956 | $134.17 |

Honeywell Home draws **2,793 impressions per product**, nine times the queue
average of 303, and converts at **1/200th** of the fire alarm core per
impression. Resideo and Honeywell Home together are 348 products and 150,706
impressions against **$33,748 of total revenue**.

They are not a rounding error in the queue: **13 of the first 100 positions and
75,312 of the first 100 positions' 361,237 impressions** are thermostats and
HVAC accessories.

**Two readings, and the available data cannot separate them:**

1. **Wrong audience.** A homeowner searching a thermostat model will not buy
   from a fire alarm distributor. This is the same shape as the "fire alarm
   battery" SERP finding above, where the intent was a homeowner with a chirping
   smoke alarm and TFAS sells SLA panel batteries to contractors.
2. **The pages are too thin to convert**, and enrichment is exactly the fix.

A 200x gap is too large to be explained by page quality alone, but reading 1
cannot be proven from this data either.

**Recommended treatment: a bounded experiment rather than a drift.** These pages
have thousands of impressions each, so unlike the old queue they *can* show an
effect. Do one batch of thermostats, measure at 30 days against the baseline,
and continue only if they convert. Do not let them consume a fifth of the next
five batches by default.

Note this is **not** the earlier rejected idea of sorting by absolute revenue,
which would have surfaced BDA gear nobody searches for. This is revenue *per
impression* on traffic the pages already earn, which is a different test.

## Google Ads: the ROAS collapse is mostly a duplicated conversion action

Measured 21 Sep 2026 over the full 180 days (`google_ads`, account 151-468-5549),
after the owner asked why ROAS was falling. Series in
`/tmp/tfas/ROAS_180d_diagnostico.csv`.

**Two conversion actions were counting the same purchase.** Alongside the site tag
`www.thefirealarmsupplier.com (web) purchase` (id 6910639875), a second action
**`Google Shopping App Purchase (1)` (id 7700459405) ran from 29 Jun to 10 Aug 2026**
and added **1,121 conversions and $464,272** of value. It is provably a duplicate:
in the weeks of 27 Jul and 3 Aug the Ads account reported **1,153 and 1,097
conversions against 843 and 818 orders taken by the entire store, all channels**.
The ratio of Ads conversions to Shopify orders sits at **0.68&ndash;0.89 for every
other week of the 180 days** and jumped to **1.37 and 1.34** in exactly those two.

So **the ROAS peak never existed.** Reported 15.26 and 13.11; web-tag-only **9.11 and
7.53**. The true baseline is **~9.5**, not 15, and the real fall is 9.5 &rarr; 3.8,
beginning **20 July** rather than mid-August.

**What the fall is not:** CPC moved $2.45 &rarr; $2.66, +8%. It explains nothing.

**What it is, in two parts:**
1. **Scaling past the qualified audience.** PMax impressions went 2.70M (Jul) &rarr;
   **4.05M** (Aug), +50%, on +31% spend; CTR fell, conversion rate fell 7.36% &rarr;
   5.90% &rarr; 3.38%.
2. **Attribution loss, not lost sales.** The Ads-conversions-to-Shopify-orders ratio
   decayed 0.77, 0.68, 0.66, 0.57, 0.56, **0.38**, while the store's own AOV held at
   ~$420 and the Ads-reported AOV fell to $307. Ads is failing to see orders the
   store is recording.

**The attribution-free check settles it.** MER (Shopify net sales &divide; Ads spend)
averaged 13.3 in Mar&ndash;Jul, fell to 10.2 in August and 9.1, and was **back to 13.0**
in the week of 14 Sep. A ~25% dip that has already recovered, against a *reported*
ROAS down 60%.

**And the business is not collapsing &mdash; it returned to baseline.** The &minus;43%
figure is measured against an abnormal peak:

| | net sales/week | orders/week | AOV |
|---|---|---|---|
| baseline Mar&ndash;Jun (14 wk) | $239,053 | 493 | $485 |
| peak Jul&ndash;Aug (7 wk) | $352,002 | 766 | $460 |
| September (2 full wk) | $208,320 | **506** | **$412** |

September versus the spring baseline: **orders +2.6%**, net sales &minus;12.9%. The
one real problem is **AOV, &minus;15% against baseline** &mdash; the same order count
with smaller baskets, which is a product-mix question in the feed and therefore
inside this project's scope.

**Two things only the Ads UI can answer** (Windsor returns the bidding-strategy
fields as `null`): who added and removed conversion action 7700459405 &mdash; Smart
Bidding optimised for six weeks against ~$464k of inflated value, so part of the
September fall is the model relearning &mdash; and what changed around 10 Sep, when
spend halved **and** budget-lost impression share fell from ~37% to ~0%, which is the
signature of a raised tROAS or tightened bid, not of weak demand.

**Three method lessons worth keeping:**
1. **Never read a ROAS trend without listing the conversion actions behind it.** One
   `conversion_action_name` breakdown turned a "collapse from 15" into "return to 9.5".
2. **Cross-check platform conversions against the store's own order count.** The ratio
   is stable enough to be a control chart; >1 is impossible and instantly diagnostic.
3. **Keep one attribution-free number.** MER needed no tags to work and disagreed with
   the reported ROAS by more than half.

## The second frontier is open: 264 products that sell and never got an ad

Measured 21 Sep 2026 from 12 months of `google_ads` item-level data joined to the
catalogue. **This is now the live enrichment queue, ahead of `ranked_v2_byscore.json`.**

### What the 12 months actually say

$985,765 spend, $9,114,601 conversion value, **blended ROAS 9.25**, CPC $2.39.
**97.4% of spend sits in one campaign**, Performance Max 9-11-2024 (Product Only).

**The obvious lever is not there.** Products with spend and zero conversions total
**$39,886, 5.1% of spend**; high-spend products under ROAS 4 add $25,817. Together ~8%.
And ROAS is nearly flat across spend bands &mdash; 9.54 for the top 50 products,
10.14, 9.60, 9.47, and **8.52 for the bottom 4,701**. There is no fat to cut, so
"pause the losers" would recover almost nothing. Test that before recommending it.

### Where the money actually leaks: price band and coverage

| price | % of catalogue | % of spend | ROAS |
|---|---|---|---|
| under $50 | 22.5% | 16.5% | 8.51 |
| **$50-150** | 27.5% | **47.2%** | 9.39 |
| $150-400 | 17.9% | 15.5% | 8.82 |
| $400-1000 | 12.8% | 11.1% | **10.90** |
| **over $1000** | **19.3%** | **9.6%** | **12.79** |

Nearly half the budget sits in the band that returns 9.39 while the band returning
**12.79** gets 9.6%. That is the same fact as the AOV decline: PMax concentrates on
cheap, fast-moving items and the basket follows. **Caveat that must travel with this
table: average ROAS per band is partly selection** &mdash; PMax already bids where it
converts, so it is not the marginal ROAS of new spend.

**The argument without that caveat is coverage. 10,359 of 16,031 active products
(65%) received zero ad spend in twelve months.** Those never lost an auction; they
never entered one. Filtered to what is actionable &mdash; sells in the ERP at
&ge;$5,000, has stock, zero spend &mdash; that is **264 products carrying $10.3M**,
and their **median description is 112 characters**. The products that sell best
through other channels and have never been advertised are also the thinnest pages.
List in `/tmp/tfas/ADS_sem_verba_mas_vende.csv`.

### What was done

- **All 264 carry `custom_label_0 = high_revenue_no_ad_spend`** in the
  `mm-google-shopping` metafield namespace, written 21 Sep 2026, zero errors. That
  namespace is what the Shopify Google &amp; YouTube channel reads. **Confirmed written
  in Shopify; not confirmable from here that the channel has mapped it into the
  Merchant Center feed** &mdash; that takes up to 24 h and must be checked there.
  It is reversible: delete the metafield. `custom_label` is a filter and reporting
  dimension only and does not affect query matching or product approval.
- **The campaign itself could not be created from here, and this is a hard limit worth
  recording: Windsor's `create_campaign` accepts only `channel_type: search` or
  `display`. There is no Performance Max, no Shopping, and no asset-group action at
  all.** A Search campaign would not serve these as Shopping listings. Configuration
  handed to the owner in `/tmp/tfas/ADS_configuracao_para_o_painel.md`, budget $500/day
  at the owner's instruction.
- **The enrichment queue is re-sorted.** Of the 264: 25 already published, 3 frozen in
  the hold-out, 66 already carry good descriptions. **170 remain, 10 batches, $4.45M of
  ERP revenue, median 94 characters**, in `/tmp/tfas/enrich/FRONTEIRA_receita.json`.
  v2b13 alone carries **$1,813,474** against roughly zero for an impression-sorted
  batch.

**The measurement consequence, recorded because it was declined:** the owner chose to
enrich all 264 rather than split them into enriched and control arms. The feed
refreshes daily, so a split would have answered "does enrichment work" in about two
weeks on the channel that moves $1.2M a year. Without it, opening coverage and
enriching happen together and cannot be separated, and **the organic hold-out frozen
until 20 Nov is once again the only route to evidence.**

## The paid channel nobody had looked at

Checked 21 Sep 2026, after 591 pages of enrichment, via the Windsor connectors
(`google_merchant`, `google_ads`, `searchconsole` are all connected and were
never queried). Last 30 days:

| channel | impressions | clicks | spend | conv. | conv. value |
|---|---|---|---|---|---|
| Google Ads Performance Max | 2,838,637 | 36,674 | $101,108 | 1,366 | $552,797 |
| Google Ads Search | 7,300 | 344 | $1,631 | 21 | $10,909 |
| **Organic (Search Console)** | **371,907** | **6,537** | **$0** | &mdash; | &mdash; |

**ROAS 5.49x on $102,739 of monthly spend, roughly $1.2M a year.** Paid buys
37,018 clicks at **$2.78 each**; organic earns 6,537 clicks free, 18% of the
paid volume.

**A correction worth recording:** the Merchant Center product-performance report
returns 2,900,556 impressions for the same period, which reads as a free-listing
channel eight times the size of organic. It is not &mdash; it is almost entirely
the same Performance Max traffic. Do not present that figure as earned.

### Why this matters to the enrichment pipeline

**Product title and description are Merchant Center feed attributes, pulled from
Shopify.** Performance Max matches queries against feed content. So every page
this pipeline has rewritten &mdash; and especially the ~350 corrected titles
&mdash; is already feeding a $1.2M-a-year ad channel, not only the organic pages
the project has been measuring.

That makes title accuracy the highest-leverage output of the work, and it means
the errors found so far were costing money in both channels: `FSP1004G` sold as
a 4-zone panel when it is 10-zone, `EOL-4.7` carrying the 47K text, `NP7-12`
claiming a flame-retardant case it does not have.

### The measurement consequence

The feed refreshes about daily, against 30 to 60 days for an organic recrawl.
**The Shopping channel can answer "does enrichment work" in a week or two
instead of two months.** To do that the enriched products have to be separable
in Performance Max reporting &mdash; a `custom_label` on the feed is the normal
mechanism. Per-product performance did **not** come back through the Windsor
`google_merchant` connector (joins on `product_id` returned empty), so the
segmentation has to be set up on the feed side.

### What this does NOT support

The feed is healthy: **16,039 active, 74 disapproved (0.46%), 4 pending.** The
accumulated vendor/brand and product-type decisions are therefore **not blocking
the feed**, which earlier notes implied they might be. They still matter for
relevance matching, but they are not an outage.

## Measurement: there is no evidence yet, by design

Checked 21 Sep 2026: **the entire pipeline is three days old.** The first batch
published 18 Sep, batch 33 on 21 Sep. Google has not recrawled, so **nothing is
yet known about whether enrichment lifts these pages** — neither for nor against.

This is a reason to work high-traffic pages, not low ones. A page with 29
impressions can never demonstrate an effect; the variance swamps it. Pages with
thousands of impressions can.

Baseline captured in `/tmp/tfas/BASELINE_555_publicadas.csv`: all 555 published
pages with their pre-publication six-month impressions (162,930), clicks (2,629)
and average position, plus batch number and publication date.

**Re-measure at 2026-10-21 (30 days) and 2026-11-20 (60 days)** against
`BASELINE_555_publicadas.csv`, which holds per-page six-month impressions, clicks
and average position and is the only durable copy of that data. Until then the
pipeline is running on an untested premise, which is acceptable at three days and
would not be at sixty.

### RESOLVED: the Windsor `searchconsole` connector is back (21 Sep 2026)

Tested a month early, deliberately, rather than discovering it on the checkpoint
date &mdash; and that was the right call, because both routes were dead at the time.

- **The Ahrefs GSC tools return `No GSC data available for the requested date range`**
  for project 7227233 on every window tried (Mar&ndash;Sep, Jun&ndash;Sep,
  Aug&ndash;Sep), via both `gsc-performance-history` and `gsc-pages`. The project
  itself is fine &mdash; verified, 308 tracked keywords &mdash; so **Search Console is
  simply not connected inside Ahrefs for it.** Still broken; do not plan around it.
- **The Windsor `searchconsole` connector was re-authorised by the owner and now
  returns daily rows** for `sc-domain:thefirealarmsupplier.com` (clicks, impressions,
  position, plus `page`, `query` and a `branded_vs_nonbranded` flag). **This is the
  measurement instrument.** The 30-day and 60-day checkpoints are unblocked.
- **Ahrefs Site Explorer is not a substitute** &mdash; it returns Ahrefs' own
  *estimated* organic traffic, not GSC impressions, and at these per-page volumes it
  is far too coarse to measure a lift.

**The generalisable lesson survives the fix: test the measurement instrument long
before the measurement date.** The plan had been written down for three days and
named a tool that returns nothing. Had this gone unchecked until 21 October, the
30-day window would have closed unmeasured and unrecoverable.

### The before/after comparison is already contaminated &mdash; a control group is required

The first thing the restored connector showed is a problem with the measurement
design, not with the pipeline. Site-wide average position over the 30 days to
19 Sep 2026, weekdays only:

| week | avg position |
|---|---|
| 24&ndash;28 Aug | 10.19 |
| 31 Aug&ndash;4 Sep | 9.91 |
| 8&ndash;11 Sep | 9.80 |
| 14&ndash;18 Sep | **8.90** |

**The site gained roughly 1.3 positions before enrichment began.** The first batch
published 18 Sep; this trend runs from late August. Whatever is causing it &mdash;
seasonality, an algorithm update, the archive wave, the 80 title-encoding fixes
&mdash; it is not the descriptions.

**So a naive before/after on `BASELINE_555_publicadas.csv` will credit the pipeline
with a lift that was already happening.** The fix is a control group, and it is cheap
because the queue is already sorted: take the next N unenriched products from
`ranked_v2_byscore.json` immediately below the published cut, which match the
published set on impressions and description length by construction, and measure the
**difference in differences**. Without that, the 21 Oct checkpoint produces a number
that cannot distinguish enrichment from drift.

This is the same failure shape as the priority list: a measurement whose defining
filter nobody checked.

### A matched control is impossible, so the design is a randomised hold-out

The obvious control &mdash; the next N unenriched products in the queue &mdash; does
not work, and the reason is structural. The treated set averages **2,643 impressions
per product**; the next 198 in the queue average **1,105**. Matching treated products
to remaining ones on impression band and description length recovered **18 of 197**.
**The queue is sorted by score, so the treated set *is* the top of the distribution
and there is nothing left that looks like it.** Any before/after against a
lower-traffic control compares two different populations.

What works instead, and costs nothing: **randomise the order of work.** Draw the next
72 products by score, randomly assign 36 to enrich now and **freeze 36 as a hold-out**
until the 60-day checkpoint. Both arms are drawn from the same band, so they match by
construction rather than by search:

| arm | n | mean impressions | mean description chars |
|---|---|---|---|
| treated | 36 | 1,098 | 107 |
| hold-out | 36 | 1,168 | 108 |

The frozen ids are in `/tmp/tfas/enrich/holdout_frozen_ids.json`, the paired list in
`/tmp/tfas/EXPERIMENTO_holdout.csv`. **Every future batch must exclude those ids until
20 Nov 2026.** The hold-out products are delayed, not abandoned &mdash; against a
4,859-deep queue the delay costs nothing, and it buys the only clean answer to
whether enrichment works at all.

**The wider point: define the control before the treatment, not at the checkpoint.**
The 555 old-list pages and v2b01&ndash;v2b12 have no valid control and never will;
the best they can support is a site-wide-trend adjustment, which the position drift
above shows is worth little. This experiment is the evidence base.

## Sales data: the ERP export (Jan 2025 to Sep 2026)

The owner supplied `MOST_SOLD_ITEMS_FROM_2025_TO_TODAY.xlsx`, a
sales-by-item export covering **all channels, including the email, phone and
chat orders Shopify never sees**. Saved as `/tmp/tfas/sales_joined.json`.

7,578 items, **$137.7M revenue, 1.6M units**. Joined to the catalogue on a
normalised SKU (strip non-alphanumerics; strip the `/u` `/b` `/e` `/a`
suffixes; strip the Autocall `A` prefix, e.g. `A4098-9714` to `4098-9714`):
**5,406 items matched, carrying 95.6% of the revenue.**

Revenue is concentrated: the top 100 items are 45.7% of it, the top 500 are
76.8%. Top vendors differ sharply from the search-demand ranking &mdash; Vesda
$25.4M, System Sensor $20.9M, Simplex $13.8M, Fire-Lite $11.3M, Notifier
$11.0M.

### What it changes for archiving: the question is closed

Added as a fourth filter after no-stock, no-impressions, no-Ahrefs-demand:

| filter | remaining |
|---|---|
| no stock | 12,977 |
| + no GSC impressions | 9,496 |
| + no Ahrefs demand | 8,604 |
| + **no sale since Jan 2025** | 8,235 |

**369 products worth $1,018,601 were rescued by the fourth filter alone** &mdash;
they would have been archived on the old three-filter rule. The list is in
`/tmp/tfas/RESGATADOS_do_arquivamento.csv`; it is dominated by Fiplex, Westell
and Comba public-safety BDA gear, exactly the relationship-sold categories the
Det-Tronics lesson already warned about.

Of the 8,235 that survive all four filters, only **4 are mature** (created
before April 2026). All four were then checked directly against Shopify
analytics and **all four have transacted**, so **zero products in the catalogue
currently qualify for archiving**.

That includes a correction: Honeywell CPR14 (id 7758172979424), previously
named here as the single archivable product in the catalogue, **sold 2 units
for $122** through a non-Shopify channel. It was only ever a candidate because
the Shopify-only view could not see that order.

**Never run the archive filter without the ERP sales export.** Shopify
analytics alone systematically over-flags the categories that sell offline.

### What it changes for enrichment: less than the headline suggests

The naive read is that the 655-product queue covers only **3.0%** of matched
revenue and should be re-sorted by revenue. That is wrong. 1,438 active
products sell while carrying under 50 impressions, but most have no search
demand either &mdash; they are BDA, flame-detection and Det-Tronics gear bought
through relationships, not Google. Enriching them buys no organic traffic.

The defensible target is the **intersection** of the three signals: sells, has
Ahrefs US search demand, and has few impressions. That is **86 products,
$672,002 in revenue and 4,430 searches per month**, of which **81 sit outside
the current queue**. List in `/tmp/tfas/ALVO_enriquecimento_vendas.csv`.

So sales data is a **second frontier after position 654, not a reordering of
the existing one**. Impressions stay the primary sort inside the current scope,
because a page that already earns impressions is the one enrichment can lift.

## Archiving: the wave is finished

Applying the full filter to the live catalog — no stock, no GSC impressions, no
Ahrefs demand — yields 8,599 candidates, but **8,568 of them were created in
June–August 2026** and are one to three months old.

The maturation curve says that is far too early to judge:

| Age | Share with impressions |
|---|---|
| 1 month | 30% |
| 2 months | 5% |
| 3 months | 8% |
| 6–10 months | 90% |
| 13 months | 97% |
| 36+ months | 94% |

Only **31 candidates are mature, and 30 of them have sold** — including a
Det-Tronics X3301S4N15W1 at $8,062 gross. Exactly one product in the entire
catalog qualifies: Honeywell CPR14 (id 7758172979424), created July 2022, never
sold, no stock, no impressions, no demand.

**Do not archive by search demand alone.** Det-Tronics has ~3,158 products, zero
search demand, and $340,063 in sales across 143 items. That business arrives
through channels other than organic search. The same holds for Space Age
($183,915) and Amerex ($90,825).

Revisit the June–August 2026 cohort around **March 2027**, when it reaches the
6–10 month mark where the impression rate jumps to 90%.
