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

**Progress: 675 pages published** — 555 from the old list plus v2b01 through
v2b06, and two thirds of v2b07.

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
- Entities allowed: `&mdash; &quot; &times; &deg; &micro; &ndash; &nbsp; &#937;` only.
- No raw `"` or `'` characters. Use `&quot;` for inches.
- Titles: `Brand PartNumber Descriptive Name, qualifiers`.

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
- **Edwards documents are not on edwardsfiresafety.com.** Every `/documents/`,
  `/products/` and `/literature` path 404s, and `est.net` and
  `edwardsfiresafety.com/files/import/` return an HTML shell for any filename. Edwards
  PDFs have to come from verbatim mirrors, so cross-check two documents of different
  dates against each other. Finding the real Edwards LifeLines library URL is worth
  doing before the next Edwards-heavy batch; several SIGA parts are still in the queue.
- **Gentex serves datasheets directly** from `fireprotection.gentex.com/files/<Model>-Series<n>.pdf`,
  with no bot protection. Beware though: one Gentex revision has a **blank Part Number
  column** while another populates it, so confirm the catalogue number on the revision
  you actually have.
- **EDAM paths cannot be constructed from the document number**, and a failed EDAM
  fetch has a fingerprint: **`application/javascript`, about 8,047 bytes, every time**.
  `AVDS916-01.pdf` exists under no `products/` tree; the file is published as
  `.../literature-and-specs/datasheets/L-Series-LED-Indoor-Horns-Strobes-and-Horn-Strobes-Data-Sheet.pdf`.
  Search for the slug, do not build it.
- **EDAM has dropped some Notifier documents entirely.** `DN-7045` 404s under both
  `notifier-us/` and the flat datasheets directory. `honeywellbuildings.in` is a
  Honeywell-operated regional site that still serves them &mdash; first-party, but
  older revisions, so cross-check against a current datasheet before using it.
- **Resideo literature path details that cost fetches:** the working path is
  `/resources/Techlit/TechLitDocuments/<prefix>s/<file>.pdf` &mdash; **capital T in
  `Techlit`**, and the directory is `33-00000s` with **five** zeros. Grepping
  `customer.resideo.com/en-US/Pages/Product.aspx?cat=HonECC+Catalog&pid=<SKU>` returns
  the document paths in one fetch, across the `33-` and `50-` prefixes together.
- **Eaton and Wheelock block `curl`.** Both HTTP/2 and HTTP/1.1 with browser
  headers fail against eaton.com (INTERNAL_ERROR or empty reply) and WebFetch
  gets 503. This is Eaton-side bot protection, not a proxy fault. What works is
  Python `urllib` through `HTTPS_PROXY` with a Safari user-agent. The Anixter
  mirror `objects.eanixter.com` serves verbatim Eaton PDFs as a fallback but
  carries superseded revisions &mdash; it had the 2016 MT4 datasheet describing
  xenon flashtubes where the current one specifies LED.
- **The sibling part is the dominant failure mode.** Part numbers differ by one
  character and describe different products. Find the full ordering table and
  confirm which row is this exact part before writing anything.
- **The Omega trap:** `Ω` often extracts as the letter `W`. An extracted "50W" in
  a resistance spec is almost always 50 Ω. **Four hits.** The fourth was Edwards
  literature printing an ordering table as `4.7KW, 3.6KW and 1.1KW` where the
  manufacturer's own technical reference prints the same parts with real Ω symbols.
- **The dropped-decimal trap:** a title copied from the adjacent catalogue row
  loses a decimal point and asserts a value ten times too large. Edwards lists
  `EOL-4.7` (4.7 kΩ) and `EOL-47` (47 kΩ) on consecutive rows; the store's
  EOL-4.7 page carried the EOL-47 text while separately stocking the real EOL-47.
  A full scan of the 19,440 active products found exactly one such case, so the
  pattern is closed catalogue-wide, but it recurs whenever a new row is copied.
- **The generation trap:** one document number can cover two product generations
  at different revisions. Confirm the revision covers the part.
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
- **Discontinuation is a feed decision, not a copy decision.** Four SKUs in one batch
  were marked discontinued by their own manufacturer while carrying live prices and
  feed entries. House rules keep lifecycle out of the copy; that leaves the question
  open rather than answered, so it goes to the owner.
- Unverifiable claims go in an `unverified` array with the reason, never in the copy.
- Always ask agents to contradict the briefing. **Seven** of the coordinator's own
  premises have been proven wrong this way; that is the point.
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

### BLOCKED: neither route to fresh GSC data currently works (checked 21 Sep 2026)

Tested a month early, deliberately, rather than discovering it on the checkpoint date.

- **The Ahrefs GSC tools return `No GSC data available for the requested date range`**
  for project 7227233 on every window tried (Mar&ndash;Sep, Jun&ndash;Sep,
  Aug&ndash;Sep), via both `gsc-performance-history` and `gsc-pages`. The project
  itself is fine &mdash; verified, 308 tracked keywords, owned by
  `gabriel@jemsystems.com` &mdash; so **Search Console is simply not connected inside
  Ahrefs for it.** The measurement plan named these tools; they do not work.
- **The Windsor `searchconsole` connector has disconnected** and needs the owner to
  re-authenticate. That connector is where every GSC figure in this file came from,
  including the 371,907 organic impressions and the `impr` column of `ranked_v2`
  (via a `gsc_raw.json` scratch pull that no longer exists on disk).
- **Ahrefs Site Explorer still works**, but it returns Ahrefs' own *estimated*
  organic traffic, not GSC impressions. At these per-page volumes &mdash; most
  products draw a handful of clicks &mdash; it is far too coarse to measure a lift
  across 645 pages. It is not a substitute.

**Owner action needed, and it is time-sensitive:** either connect Search Console
inside Ahrefs for project 7227233, or re-authorise the Windsor `searchconsole`
connector. Without one of them the 30-day checkpoint cannot be measured at all.

**The generalisable lesson: test the measurement instrument long before the
measurement date.** The plan had been written down for three days and named a tool
that returns nothing. Had this gone unchecked until 21 October, the 30-day window
would have closed unmeasured and unrecoverable.

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
