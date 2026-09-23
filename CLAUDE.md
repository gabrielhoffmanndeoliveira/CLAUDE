# CLAUDE.md

Guidance for Claude Code working in this repository. **This file is the operative
core. The worked cases behind every rule live in `docs/registro/`** — read the index
there (`docs/registro/LEIA-ME.md`) before touching a brand or a workstream.

## How this file and the case log work

- **This file** holds what a coordinator or agent needs on every turn: the standing
  order, the batch mechanics, house style, the research rules, the route table, the
  scan and photo rules, and current state. It is loaded automatically.
- **`docs/registro/`** holds ~640 worked cases moved **verbatim** from the old
  single-file CLAUDE.md on 23 Sep 2026, split by brand and by theme. It is **not**
  loaded automatically (the files are deliberately not named `CLAUDE.md` and are never
  `@`-imported). Read the files for the brands in a batch before briefing, and hand
  their paths to agents.
- **The registro is chronological.** Later entries correct earlier ones. The 19
  overturned rules most likely to mislead carry a `[CORRIGIDO — …]` prefix pointing at
  their correction; the marking is not exhaustive. **On any conflict, this core wins,
  then the most recent registro entry.** The single-file CLAUDE.md as it stood before
  the split is commit `5da4bb6` in git history.
- **Where to write new findings.** A new *case* goes at the end of the matching
  registro file (new brand → new file, and a line in `LEIA-ME.md`). A finding that
  **changes a rule** also gets a one-line edit here, in the rule it changes, citing the
  registro file. This core has a budget of about 35k tokens; the old file reached
  185k and every agent paid it on every turn. Keep it there.

## Repository status

No application source. This is the working root for a consulting engagement on
**thefirealarmsupplier.com** (TFAS), a US Shopify Plus fire-alarm parts distributor.
All product data lives in Shopify and is reached through the Shopify MCP server. Tracked
here: this file, `docs/`, `.gitignore`. Working files live in `/tmp/tfas/` and are not
tracked. They survived a container restart on 23 Sep; `live.jsonl` is a snapshot and
is re-pulled in one bulk query before building a slice or running a sweep.

## Standing instruction

**Run the pipeline continuously until the project is complete. Do not stop between
batches to ask permission and do not sit idle.** The owner restated this three times on
22 Sep 2026 — *&quot;segue sempre&quot;*, the third time with *&quot;grava isso no seu
claude.md&quot;*. It is configuration, not encouragement. **Anyone reading this file
starts already authorised: slice the next batch, launch the agents, publish what
validates, flag what is the owner's to decide, and do not ask. Never end a turn asking
whether to continue.**

**Current capacity setting (owner, 23 Sep 2026): &quot;pode usar só 1 agent agora, vamos
desacelerar um pouco&quot;.** One research agent at a time until the owner changes it.
The standing order still holds inside that cap.

**Usage budget (owner, 23 Sep 2026): &quot;temos q cuidar com o weekly all models&quot;.** One full day of work (12 agent lots + coordination) consumed ~24% of the weekly all-models limit. Pace to **~10–12% per day** (about 6–8 agent lots/day) until the weekly reset (Tuesday 19:00). Prefer title lots (~150–165k tokens) over enrichment lots (~220–260k); fix mechanically, without an agent, any title whose correction decides nothing; keep spot-checks to the strongest claim and reports short. Using a cheaper model for agents requires the owner&#39;s explicit approval.

**Direction change (owner, 23 Sep 2026): enrichment is PAUSED after v2b52.** &quot;vamos
pausar tudo entao e focar na auditoria de titulos e dados estruturados&quot;. No new
`v2bNN` slices. The work is now the title and structured-data audit: mechanism scans on
the live catalogue, title-only research lots for demonstrably wrong titles, and turning
the backlog in `DECISOES_DO_DONO.csv` into owner-approved changes. Rationale: title,
type and vendor errors cost two channels (organic and the Merchant Center feed behind
~$1.2M/yr of PMax) and do not wait on a recrawl, while description value per batch has
fallen to ~6&ndash;8k impressions and is unproven until the 21 Oct / 20 Nov checkpoints. Earlier setting, for reference when the
cap is lifted: two text agents and four photo agents; six concurrent is the ceiling,
because the coordinator is serial (10–15 min to validate, spot-check, publish, record
and commit each returning batch) and a queued agent burns tokens like a working one.
Cheap-to-validate workstreams (photo harvests, title lots) cost the coordinator far less
than enrichment batches, so tune the **mix**, not only the count.

**The loop's one failure mode is ending a turn with no agent in flight.** A finishing
agent wakes the session; nothing else does. So **launch before you write**: start the
work as the first act of the turn, then report. A sentence like &quot;starting v2b18
now&quot; with no agent launched is the loop stopping. If work genuinely cannot start
(blocked host, empty queue, owner pause), say so plainly — an explicit stop is
recoverable, a silent one is not.

**Findings are reported as they land, never as a pause.** The one thing that is a
*flag* rather than an action: structured data feeding Merchant Center (see *Owner
decisions*). Description and title corrections need no approval.

## The batch loop

### Queue and working files (`/tmp/tfas/enrich/`)

- **Live queue: `ranked_v2_byscore.json`** — 5,074 candidates sorted by
  `impressions x (1 - chars/700)`. `ranked.json` is retired; its positions 555–654
  were deliberately abandoned. Do not resume it.
- `_used_ids.json`, every `<dir>/slice.json`, every `_TITULOS_loteNN.json` — ids
  already taken. `_holdout.json` / `holdout_frozen_ids.json` — **36 ids frozen until
  20 Nov 2026**; every batch must exclude them (the builder does).
- `/tmp/tfas/catalogo_full.json` — snapshot of all active products (no
  `descriptionHtml`); `/tmp/tfas/live.jsonl` — the live bulk pull. **Snapshots find
  candidates; every defect must be confirmed live before it is reported or acted on.**
- `pending_fixes.md` — corrections queued against published pages.
- `/tmp/tfas/DECISOES_DO_DONO.csv` — the owner's decision file (see below).

### Batch shape

**12 products, split 6/6** into `v2bNN/a1_in.json` and `a2_in.json`. Six products per
agent is what quality rests on: shrink the batch, never the agent's share. Under the
one-agent cap, run the two halves sequentially. **A batch is a scheduling unit, not a
publishing unit** — publish a validated half as soon as it lands.

### Building (never by hand)

- **Enrichment slice: `python3 build37.py <NN>`** (number only; it normalises `49`,
  `v2b49`, `v2b49/` and prints where it writes). It takes `type` verbatim from the
  snapshot and `handle`, `title`, `vendor` and `live_desc` from `live.jsonl`, excludes
  used, held-out and title-lot ids, **re-reads both input files from disk and refuses
  on a missing file or an empty `id`/`sku`; an empty `type` warns and names the row**
  (52 of 16,031 products genuinely have none — say so in the briefing).
  **The builder is not idempotent**: a second run counts the first run's slice as
  used and produces a different twelve. Never re-run it while agents are working.
- **Title lot: `python3 build_titulos.py <NN>`** (refuses an argument starting with
  `lote`). Joins `type` and `handle` from the live pull and the newest nameless census.
- **Photo input: `/tmp/tfas/foto/build_in.py`** — excludes products not in the
  placeholder census, already adjudicated by a harvest, **and already delivered in a
  CSV lot** (the delivered file is the authority on what is done).
- **Photo CSV: `/tmp/tfas/csv/build_csv.py <OUT.csv> <harvest.json …>`** — output
  first; it refuses a non-`.csv` output and any file that is both source and output.
  A zero-row result is a question about the tool before it is a fact about the data.

### Briefings

- **Build each briefing from its own `aN_in.json`, programmatically.** Never assign
  products to agents by reading a listing, never type an id, a SKU, a filename or a
  figure out of a file by eye — four incidents, four different fields, one cause
  (`registro/coordenacao-e-incidentes.md`).
- **The input file is the authority on id, vendor, type, title and live copy; the
  briefing prose is a hypothesis.** State routing guesses as guesses. When prose and
  file disagree, the file wins without argument. Twenty-plus coordinator premises have
  been wrong; ask agents to contradict the briefing every time.
- **Carry the exception.** When summarising an earlier finding into a briefing, keep
  its &quot;except&quot;. A compressed rule that drops it is a different, false rule
  (`2099-` releasing sheet; `-IV` colour-and-protocol).
- **Say which field a defect is in** (Shopify `title` = feed attribute, two channels;
  description = one) **and which defect it is** (truncation, borrowed copy, unsourced
  claim…). Both have been misbriefed repeatedly.
- **Point agents at the registro files for their brands** by path.
- Tell agents: echo `id` from the input file; put every unverifiable claim in an
  `unverified` array with the reason; `null` is an accepted answer.

### Validation and publishing

- **`v2bNN/verify.py <aN_in.json> <agentN.json>`** — asserts id membership and order,
  SKU present in title, ASCII title ≤150, balanced parentheses, no newlines, entity and
  tag whitelist, no attributes, 4–7 `<li>`, no raw quotes, 700–1230 visible chars.
  Nothing publishes with a failure.
- **Spot-check the batch's strongest claim yourself** — fetch the document and read it,
  especially anything that changes a live title, removes a live claim or overturns a
  recorded rule.
- **Sibling-SKU check before any title change:** does the store already sell something
  under that exact name, or the product the documents describe under another SKU? One
  query. (`PTS-C CABLE` would have been titled as the $280 switch; `SIGA-OSHD-IN` would
  have collided with `SIGA-OSHD`.) An unsourced suffix stays in the title; a sourced
  non-suffix (a reel length) comes out.
- **Publish:** `mcp__Shopify__graphql_mutation`, parameter **`query`**, aliased
  `productUpdate` mutations (`u0:`, `u1:` …), input type **`ProductUpdateInput!`**,
  up to nine per request. **Emit the variables object with a script, `cat` it, paste
  it unmodified.** Check `userErrors` on every alias.
- Record, commit, and move the progress line.

### Title-only lots

Nameless titles (`Brand PartNumber` and nothing else) get a class noun and a
descriptive name, sourced like any other title claim. The census is **re-run, never
decremented** (`/tmp/tfas/TITULOS_SEM_NOME_v3.json` is the latest). **It has a floor of
about twenty deliberate `null`s** — products correctly declined for a named reason
(WAF, wildcard SKU, three incompatible readings, not in the manufacturer's catalogue,
not a product). Track never-sliced / in-flight / declined separately; a queue built by
subtraction cannot see the declined ones. Title-only products are tracked but not
enriched, and must be excluded from the enrichment sweep's population.

## House style for `descriptionHtml`

One single-line string, no newlines.

1. `<p><strong>Brand PartNumber</strong> &mdash; one-line identification.</p>`
2. One context paragraph: what the part does and why it exists.
3. `<ul>` of 4–7 verified specs.
4. Closing paragraph naming the specific sibling parts a buyer could confuse it with.

- **700–1100 visible characters** (tags stripped); hard ceiling 1230. Whole batches
  sitting at 1,135–1,229 means the soft range has stopped binding — say so in briefings.
- Tags: `<p> <ul> <li> <strong> <sub> <em>` only. No headings, links, attributes.
- Entities: `&mdash; &quot; &times; &deg; &micro; &ndash; &nbsp; &#937; &amp;` only.
- No raw `"` or `'`. Use `&quot;` for inches.
- **Titles: `Brand PartNumber Descriptive Name, qualifiers`, plain ASCII, ≤150.** In a
  title write `&` (it is ASCII); in a description write `&amp;`. Never write a literal
  entity into a title. Never introduce a non-ASCII character into a title; do not
  rewrite an old title only to remove `°`, `®` or `™`.
- **Shopify decodes entities and re-inserts newlines on storage.** The entity and
  newline rules are input discipline; never audit published pages for them.
- Do **not** add &quot;Non-Fire&quot;, &quot;(Security)&quot; or &quot;Not Fire
  Rated&quot; to titles (owner's decision); such notes go in the body. A manufacturer's
  own product name containing such a word is fine.
- Never state stock, lead time or condition.
- **The coordinator may tighten or soften agent copy but must not introduce a new
  factual claim** without agent-grade research. Both inline edits that went wrong were
  the two where the coordinator supplied the substance.

## Research rules (give these to every agent)

Case law for every rule: `registro/metodo-geral.md` plus the brand files.

### Evidence

- **Never invent** a number, dimension, current, listing, temperature, compatibility,
  pack count, material, colour or lifecycle state.
- **Manufacturer documents only.** Download the PDF with `curl` (or `urllib` where
  noted) and extract locally with `pymupdf`. Never take a spec from a search snippet,
  a reseller, Amazon, or an AI/summarising fetch — summaries have shifted tables by a
  row, welded two catalogue entries into one, and turned page chrome
  (`discontinuedText`) into a lifecycle claim.
- **Distributor consensus is not evidence.** Resellers copy each other; they have been
  wrong together on at least eight parts (lengths, mountings, stale revisions,
  capacities).
- **`file -b --mime-type` before trusting any extraction.** HTML shells, JS shells and
  CloudFront 403 pages open in pymupdf as clean documents. For **images** mime is not
  enough — several hosts serve a real PNG/JPEG as their 404; use a bogus-SKU control
  measured by MD5 or byte length at download time.
- **Every negative needs two controls: a bogus term and a known-good term.** At least
  ten search endpoints on this project ignore the query, echo it, or return a false
  negative. The test is **whether the response contains what you asked for** — count
  product rows, not string occurrences; byte count, MD5 and status can each be fooled.
- **A negative bounds the search, not the catalogue.** Never conclude a part number is
  invented from an absence; removing a live claim needs positive evidence, the same bar
  as adding one. Check the *document family* (wrong family has fired eleven-plus times)
  and the *product generation* before concluding.
- **Record the path you tested, not the brand.** A host-level negative decays, and six
  recorded ones have (Edwards first-party, Hochiki Europe images, `DN-7045`, the 4%
  Edwards photo ceiling…). Re-test before building a batch on a workaround.
- **Find a filename, do not build it** — unless a search has already given you the
  document number *and* its title, or you hold a sibling slug in the same dated
  subdirectory.
- **A spec finding carries the revision it was measured on.** Revisions change answers
  (Protectowire 220 °F spacing), carton contents, currents and supersession statements.
  A successful fetch is not evidence you have the current revision — read the header line.
- **Normalise whitespace before grepping extracted PDF text** (`re.sub(r'\s+',' ',t)`).
  A phrase-level zero found without it is unmeasured.

### Reading documents

- **Escalation ladder: plain text → `page.get_text("words")` with coordinates → render
  at 200–300 dpi and read.** Each rung has been wrong where the next was right. Render
  whenever a table has merged cells, captions, multi-line headers, rotated headers, or
  text that looks like noise; when an enclosure sheet carries no inch figures (vector
  dimensions); and before calling a generation conflict (stale text layers exist).
- **Caption traps:** caption below its table; two tables emitted swapped; a header
  inside a table contradicting its caption; both halves of a split table under one
  caption; two tables on one page (or two documents of one brand) using different
  column orders. Never take a caption-to-body or row-to-label assignment from reading
  order.
- **Prefer the model-attributed row over prose and over series-wide blocks.** A spec,
  listing or feature block covering a family is not a spec for any member — and can be
  flatly false for one. An A&E paragraph naming a variant is quoting one row of several.
- **When a document contradicts itself, find the mechanism before choosing:** check
  whether the losing figure is correct somewhere else (another model's sheet, the
  previous revision); check whether an adjacent column agrees (a local transposition);
  look for a third and fourth signal. If nothing settles it, publish neither.
- **Conditional headlines:** a single headline dB, candela or current on a configurable
  device is conditional (setting, tone, anechoic vs reverberant, standard) until the
  instruction sheet's table says otherwise. Publish figures with their conditions.
- **Installation instructions beat catalogue sheets** for ratings, carton contents and
  scope; accessory specs often live in the parent's sheet — and the parent's figure may
  be wrong for the child. Accessories are often in no index at all; grep the parent's
  installation/mounting guide and exploded-diagram callouts.
- **Symbol traps:** `Ω` extracts as `W`, `µ` drops (450 A for 450 µA). Ask whether the
  bare number is physically possible. But a real `W` exists (`2W` = two-wire).
  Dropped decimal: a title copied from the adjacent row can assert a value ten times
  too large (`EOL-4.7` carrying `EOL-47` text).
- **A syntax block is the best decoder and is still prose:** cross-check its fields
  against the ordering table (typos, overlapping brackets). A suffix grammar is a
  property of a *generation* and of a *family*, not of a brand; a decode from one member
  is not the family's grammar; a convention on one product line does not transfer to
  another (seven preventive refusals so far — keep refusing).
- **A number inside a model number may not be the spec it resembles** (`AS-75-R-WP` has
  no 75 cd setting; Power-Sonic model numbers match the 20-hour capacity on only about a
  third of models; `KC2-SB4`'s 4 is terminals). **Batteries: state the rate, and both
  rates where they differ; check capacity = stated current × hours.**

### Product-truth checks (the defects that cost buyers)

- **Sibling parts are the dominant failure.** Part numbers one character apart are
  different products; find the full ordering table and confirm the exact row. Pair-split
  obvious sibling pairs across agents and diff shared figures at merge.
- **Product class:** twenty-four title-level class errors so far. **The `type` field is a
  signal when it disagrees with the title and no evidence when it agrees** — and when it
  disagrees it does not say which field is wrong. &quot;Annunciators&quot; or
  &quot;Loop Modules&quot; on something priced like a panel is a class question.
  Expand the part's initialism before fetching (DACT is a telephone communicator).
  Check against the physics of the class (a heat detector has no smoke chamber).
- **Incomplete product:** sixteen-plus cases of a bare head, board, chassis, card,
  appliance, enclosure or licence sold as a finished product. Tells: the word
  &quot;required&quot; or &quot;order separately&quot; in the ordering table; the part
  appearing inside another product's &quot;comes with&quot; clause; copy borrowed from
  a sibling's feature list. It also runs backwards (a complete product described as a
  chassis; a page telling the buyer to buy a cable they do not need). Check whether the
  required part is stocked — that decides whether the copy can help or only warn.
- **Borrowed copy:** a live page carrying a sibling's text end to end. But the
  &quot;same as above, except…&quot; phrasing is often the manufacturer's own row for
  the right part — the discriminator is *whose row it is*.
- **Releasing equipment** has repeatedly been merchandised as ordinary fire equipment;
  check the ordering line, not the page heading. Colour encodes nothing about class.
- **Listing classes hide behind correct nouns:** any non-clear lens (amber, blue, green,
  red) is a listing question on every brand, and the answer differs by brand; `-ALERT`,
  MRI-conditional, private-mode and ULC variants are materially different purchases.
  Put the difference in the body; put it in the title when manufacturer-stated.
- **Supersession (&quot;Replaces&quot;/&quot;Replaced by&quot;) belongs in a title only
  when a manufacturer document states it.** Sources in order: product-announcement
  bulletins (Honeywell `M23.2SS`-style REPLACES tables), sales announcement letters, a
  document renumbered onto the successor (`DN-61092:C`→`:D`), the successor's own sheet.
  A datasheet revision line (&quot;Supersedes sheet dated…&quot;) and a coexistence
  sentence (&quot;may be installed on the same SLC/interconnect with…&quot;) are **not**
  supersession. Search both directions. Then run the mechanism check: a spec that would
  have to be equal if it were a drop-in (listed spacing 70→50 ft refutes; a feature lost
  in a sourced successor becomes a migration warning). Multi-brand Honeywell issues name
  different predecessors per brand imprint — keep those in the body.
- **Pack counts are per-SKU and per-vendor facts.** Honeywell states carton quantities
  for bases, low-frequency sounders and batteries and not for detectors or notification
  appliances (quantities vary: batteries 10/5/4/2/2); Xtralis, Gentex and others state
  them routinely — but not for every item. A pack count in a title is the owner's call
  even when sourced.
- **Lifecycle** is a feed decision, never a copy decision. Curl the page and find what
  &quot;discontinued&quot; is attached to.
- **Brand/vendor:** identical third-party listing files (UL, CSFM, MEA) prove one
  manufacturer; different files prove different ones. Check whose name is on a listing
  document, not whose site served it. Take a brand-vanished finding from a render, not
  a grep. A brand that looks wrong can be right (VESDA Sensepoint XCL).

## Route table

Detailed evidence per brand is in the registro. Fingerprints are measurements and decay
— re-measure before filtering on one.

| brand / host | what works | traps and fingerprints |
|---|---|---|
| **Honeywell EDAM** (`prod-edam.honeywell.com`) | Two roots: `content/dam/honeywell-edam/hbt/en-us/documents/literature-and-specs/datasheets/` and `content/dam/hon/hbt-fire/en-us/products/literature-and-specs/datasheets/`. Per document try: bare docnum, lowercase, `_` for `-`, `<Model>_<DocNum>`, `<DocNum>_<Model>`, `hon-ba-fire-<doc>` (lowercase), `hon-ba-<doc>`, `notifier-us/hon-ba-fire-dn-NNNN.pdf`, `?download=false`, descriptive slugs found by search. Subdirs: `farenhyt/`, `notifier-us/`, `-aus/`, `-uk/`, `-nz/`, `gamewell-101625/`, `flexbda-050526/`, `fiplex-02022026/`; `manuals-and-guides/installation-guides/` and `user-manuals/`. A numeric sweep of `hon-ba-fire-dn-<N>.pdf` finds unknown document numbers. | Miss = **8,047 B `application/javascript`**. `df-52416.pdf` returns **200 with 0 bytes**. Two revisions live under two slugs (`DN-61092`, `DN-60955`, `DN-62113`) — read the header. Case-sensitive. Paths are per-document; the shapes do not compose into a rule. |
| Honeywell bulletins / pages (`buildings.honeywell.com`) | `content/dam/hbtbt/...` bulletins with descriptive slug + bulletin number (search it). Fire-Lite data sheets under `.../document-lists/firelie/data-sheets/` (honest ~610 B 404). | `/products/.../<slug>` discriminates by mime; `by-brand/` and `/search` do not. `discontinuedText` is page chrome. `session-manager.aero.joule.honeywell.com` (product index) is refused at the proxy — unreachable. |
| System Sensor | EDAM. Prefer a document family (`9021-` vs `AVDS`) only after grepping it for a word the part implies (it has failed three times). | `systemsensor.com/en-us/Documents/*.pdf` = JS shell that opens as 7 pages. |
| **JCI hub** (Simplex, Autocall, Ansul/specialhazards, FireClass, Zettler, Tyco Fire) | `https://docs.johnsoncontrols.com/<segment>/api/khub/documents` returns the whole index; grep `filename`, `prodname` **and** `product_code`; download `/<segment>/api/khub/documents/<id>/content`. Segment = business unit, not brand. | `search` is ignored. Metadata is a list of dicts. A metadata hit is not a text hit — grep the served PDF. Service parts lists are not on the hub. Wrong segment 404s at 236 B. |
| **Siemens** | `sid.siemens.com/go/<A6V asset>` → 303 → `/api/khub/documents/<hash>/content`. `/api/khub/maps` index (grep once). `cache.industry.siemens.com/dl/files/...` serves A6V PDFs directly. | `/api/khub/documents` 504s. `/go/` resolves A6V numbers only. Search-result `content` URLs have served the wrong document. `support.industry.siemens.com/cs/attachments` = 403/442 B. |
| **Edwards** | `edwardsfiresafety.com/lifelines/<category>` (and nested platform pages; recover slugs from the index nav JSON). PDFs at `myeddie.edwardsfiresafety.com/PublicMedia/Catalog%20Sheets/<E85001-NNNN -- Title>.pdf` (build only from a searched number + title). Photos: `/PublicMedia/ProductImages/<SKU>.{png,jpg}`. Install/service manuals for legacy accessories. | `/PublicMedia/` miss = **1,245 B 404**; `/Media/` now 302s. `est.net`, `edwards-signals.com` = shells. ProductImages is variant-blind on some G4/lettering families and serves other parts' labels on SIGI modules — look. |
| **Kidde (ES)** | `POST https://www.kidde-esfire.com/LiteratureLibrary/GetCategoryNavigation` with `categoryName=` (names enumerable from the nav). hrefs point to Edwards' myeddie store. `Images` category = five public ZIPs. | Wrong category returns empty `Content`, not an error. E/K prefix = same hardware, **not** the same carton (wiring plate included vs separate); the `E` is inside the series code. |
| Kidde Fenwal | `kiddefenwal.com/wp-json/wp/v2/wpdmpro?per_page=100` (350 docs); `?wpdmdl=<id>` + HEAD gives filename. | `LocalMedia/Data Sheets/*` = 1,279,593 B HTML; `kidde-fenwal.com/Media/Data Sheets/` 301s to root. CARDOX low-pressure CO₂ hardware is in no document. |
| **Eaton / Wheelock** | Python `urllib` + Safari UA through `HTTPS_PROXY`; try `eaton.com` bare host as another draw; `skuPage.<SKU>.html` → `mdmfiles/<contentId>/<ASSET>/<size>` (strip an existing size segment first). `alarmax.com/customer/docs/skudocs/` fallback. Slugs must be searched. | `curl` fails; intermittency is per connection and per route — after ~25 failures use another process. `web.eaton.com` old names = 86 KB HTML. Filenames name wrong products. |
| Gentex | `fireprotection.gentex.com/resources` lists ~90 PDFs; `/files/<name>.pdf`. Sales announcements carry supersessions. PLACE line on `placehomesolutions.com`. | Constructed names 404 at ~7,270 B HTML (size drifts with name). One family render per series; per-SKU photos ~zero. |
| Potter / RSG | `pottersignal.com/sitemap.xml` (625 document URLs); `/product/datasheet/<docnum>_<MODEL>.pdf`; `/product/tool/`; `PotterSecurity_catalog.pdf`. | `/search?q=` ignores the query (80,279 B). 404 = 78,087 B JS. Images are 330 px presets. |
| Mircom / Secutron | `mircom.com/product-documents/` (2,132 PDFs) **and** `/wp-content/uploads/pdf/`; WooCommerce Store API (join on name, not `sku`); media titles are a second field. Apex host; serial at ≥4 s (`Crawl-delay: 10`, 429s). | `?s=` honest but gives false negatives; count result links, not bytes. `wp/v2/media`, posts, pages, search = 401. Doc miss = 146 B. |
| Xtralis / VESDA | `xtralis.com/file/<id>` — enumerate ids and titles from `xtralis.com/product/<id>/<slug>`. Americas (`file/623`) and Europe (`file/495`) catalogues are not supersets of each other. | Miss = `text/html` 226,237–226,241 B. No sitemap. |
| Power-Sonic | Datasheets at `power-sonic.com/wp-content/uploads/datasheets/<slug>.pdf` (slug from sitemap/product page, not the SKU); `wp/v2/product?search=` is honest; `ps_terminal_type` taxonomy lists codes without meanings — the drawing decodes them. | `?s=` non-discriminating. `cdn.power-sonic.com` returns **200 + 0 bytes** for a miss (real files serve when the name was found). Series page 3 is boilerplate. |
| Resideo / Honeywell Home / BRK | `customer.resideo.com/resources/Techlit/TechLitDocuments/<prefix>/<file>.pdf` — capital T; `33-00000s` (five zeros), `63-0000s`/`69-0000s`/`60-0000s` (four), `BRK-First Alert/`. `Product.aspx?pid=` needs `/U` kept and encoded. `03-` sell sheets carry REPLACES tables. | Product pages can list documents they do not serve. `brkelectronics.com`/`firstalert.com` product URLs 404 as JS shells. |
| Napco | `napcosecurity.com/media/pdfs/<DOCNUM>-<slug>.pdf`; tag index `tech.napcosecurity.com/techlibrary/tagresults/tag/<sku>` — try **both** hyphen and underscore, with a control (&quot;of 0 Results&quot;). | 404 ≈ 30,430–30,439 B. `downloadfile/id/<n>` is a constant shell. |
| STI | Sanity: `https://4ikv42xc.api.sanity.io/v2021-10-21/data/query/production?query=` — `sanity.imageAsset` by `originalFilename`, and `product` docs by `modelId`. | Product `featuredImage` names other catalogue numbers — use the filename index. |
| Avire (RATH, JANUS) | `avire-global.com/en-us/wp-json/wp/v2/media` (images and 798 PDFs); `?s=` honest. | Legacy RATH hosts redirect every path to the Avire home page (a 200 that lies). Product URL `8100-v4g` describes the successor. `urllib` 403 where `curl` works. |
| Amerex | Raw markup of `/learning-center/product-brochures/` → 60 PDFs under `/upl/downloads/content-blocks/`. | Product pages 404; category page is a JS shell. Two-line table headers. |
| Macurco | `macurco.com` (no `www.`): WP media API, WP `product` REST, WooCommerce Store API (honest). | `docs.macurco.com` is a bubble.io shell (~15.5 KB). |
| Det-Tronics | `curl -L` on `www.det-tronics.com` WP media API (445 PDFs). | No per-SKU imagery (family assets only). Client behaviour flips between `curl` and `urllib`. |
| Hochiki | America `/products-search?qs=` (honest); datasheets `hochikiamerica.com/img/product/description/`. Europe per-part renders under `hochikieurope.com/casestudies/`; product guide via `/product/<range>` asset links. | `/ecom/productsearch` ignores the query; Europe `?s=` constant 39,632 B; AssetBank constant 14,749 B with varying MD5. |
| Others | Functional Devices: `sitemap-managedcontent-sfdc_cms__document-1.xml` → `/sfsites/c/cms/delivery/media/<MC-key>`. DITEK: `www.diteksurgeprotection.com` series pages. Altronix: `altronix.com/library/pdf/data_sheets/DS_<MODEL>.pdf` or `DS_<series>series.pdf` (404 = 13,828 B). Space Age: `www.1sae.com/sitemap.xml`. Fireray/FFE: `ffeuk.com/resources` (358 PDFs). Apollo: `F00…_0001.pdf` names on product pages. Westell: `support.westell.com/documents/<slug>-DS.pdf`. Honeywell Analytics: `honeywellanalytics.com/~/media/...`. Autronica: `product.autronicafire.com/fileshare/...`. | — |
| Others (2) | APC (Air Products): `apcfire.com/wp-content/uploads/<yyyy>/<mm>/` (dated path; PAM relays). RFS: `rfsworld.com/products_sitemap.xml` (1,514 products, URL = part number). Comba: `combausa.com` WooCommerce Store API + media API. Viking: `vikinggroupinc.com/products?text=` is honest. Aiphone: `know.aiphone.com/search?query=` is honest (documents only). SDi / Detector Testers: `sdifire.com` legacy PDFs under `/wp-content/uploads/2018/08/`; Detector Testers pages carry the product code in four structured places. Mirrors (`qdigital.mx`, `alldataresource.com`, `steelfire.com`, `objects.eanixter.com`): only on **searched** paths, only after the mime check, and prove verbatim by MD5 or imprint. | `rfsworld.com/search`, `aiphone.com/?s=`, `e2s.com/?s=`, `vikinggroupinc.com/?s=`, `safefiredetection.com` search (echoes only) do not discriminate; `detectortesters.com` search = 406, image miss = a real 1,692 B JPEG. `apcfire.com` undated path 404s at 146 B. Mirrors serve HTML shells for guessed names and older revisions (Anixter). `mall.industry.siemens.com` 302s for real and bogus alike (failed reproduction). `digitalassets.resideo.com` route unreachable since BRK shells 404. Bosch sitemap carries no US fire products. |
| **Blocked** | — | `fiplex.com` Akamai (456 B 400); `protectowire.com` and `trilogy*` Sucuri (202 + `sgcaptcha`; EDAM mirrors an older Protectowire revision); `polyphaser.com` Incapsula (~965 B); Bosch CDNs (128 B); `lenel.com` 503; `gamewell-fci.com/CatalogDocuments` (~258 KB JS, 1-byte drift); `autocall.com` (103 B); `web.archive.org` blocked by egress policy; every FCC ID route. **A Fiplex Document Center login is now needed for `DHS40-HG-SCH-1-A` only** (BDA-TP10-L2 settled first-party from BD500 on `flexbda-050526/`; BDA-NMP01250 from the Trilogy sheet; `registro/fiplex-bda.md` x01). |

## Scans and sweeps

Case law: `registro/varreduras-e-auditorias.md`.

- **Scan for a mechanism, not a shape.** Every keyword scan here over-fired by one to
  two orders of magnitude; mechanism scans (unbalanced parentheses, family `type`
  disagreement, brand+SKU repeated, five-plus digits before `MHz`, whitespace-only SKU
  differences, a page spelling its own part number two ways) landed clean. Before
  running a scan, **state what a defective product looks like in the data**, not on the
  page — the placeholder photo was a *shared id*, not a null.
- **A scan is two numbers**, precision and recall; report both or say which is unknown.
  A suspiciously tidy count deserves the same doubt as a huge one (phrase matches
  under-fire).
- **Sharpen by removing named, documented reasons a difference is legitimate**, and stop
  when you run out of explanations — not when the count looks right.
- **A scan reports that a family disagrees, never which member is wrong**; often the
  minority is the healthy one. A near-miss between title and SKU is equally a typo and a
  real sibling — look for a third identifier (catalogue number, stock number, colour
  word, price) before ruling.
- **Run identifier checks on every field** (`title`, `sku`, `vendor`, `productType`,
  `handle`), not only where a defect was first noticed.
- **When a mechanism both applies a fix and verifies it, vary one parameter** (e.g. case)
  in a second check — the 75-title dedup's own verification shared its blind spot.
- **A fix may be applied unilaterally only when it decides nothing** (the new title is a
  literal substring of the old, and postconditions hold: SKU still present verbatim,
  ASCII, ≤150, balanced). Anything that chooses between readings goes to an agent or the
  owner.
- **Verification sweep every five batches**, one bulk query. Population = v2 slice ids +
  `BASELINE_555_publicadas.csv` − the in-flight batch − title-only products. Expected:
  zero missing, exactly two pages under 400 visible characters (`SM7100-L8`, `90521`,
  the deliberate skips; `BDA-TP10-L2` and `BDA-NMP01250` were enriched on 23 Sep). Also report: non-ASCII titles
  (should be only `°`/`®`/`™`, count falling), literal entities in titles (0),
  unbalanced parentheses (102, the unreconstructable truncations), brand+SKU repeats
  (only the known `STI STI EP141207-T`, whose SKU contains the vendor). **Print the
  population in the output line.** A sweep's first job is to prove its denominator
  equals what the project claims to have done.
- **Never apply the frequency-range reconstructions from part numbers**: a digit run
  inside a part number is not evidence about a band (`BDA-YDA763869-14-1` is
  698–869 MHz). Only title-labelled runs are evidence, and the set is still the owner's.

## Photo pipeline

Case law: `registro/fotos.md`.

- **The defect:** 7,900 active products carry a TFAS placeholder (`MediaImage`
  `43649142325472` on 7,738, plus two smaller ones). **Never delete a placeholder
  media object.** Census: `/tmp/tfas/SEM_FOTO_REAL_ranked.json`.
- **A wrong photograph is worse than a placeholder.** Rules: manufacturer-hosted only;
  the source must name the exact part; measure mime and pixel size of the downloaded
  file yourself; 600 px floor measured on the **subject**, not the canvas; `null` is an
  accepted answer; no reseller, marketplace or image-search asset.
- **Token-boundary match:** the SKU must be followed by a non-alphanumeric or the end of
  the token (the successor `8100-V4GS` must not match `8100-V4G`); longest SKU owns the
  file. A filename, a structured `modelId`, a `sku_list` and even a path derived from
  the catalogue number have each served another product. **Only reading the label or
  counting a feature in the photograph is sufficient — build contact sheets and look.**
  Composite PNGs onto white before looking.
- **An asset named for a base model is not evidence for a variant SKU**, even when the
  difference is invisible (owner decision pending on family renders; see below).
- **Delivery-wide checks, over all lots together:** URL reuse, MD5, and dHash at
  Hamming 0 — **with a degeneracy guard** (ignore groups whose hash popcount is below
  ~40 of 256 or whose rows repeat; near-blank white-background shots collide). A
  collision is a question, not a verdict: packs, approval variants (LADBS), retail
  cartons and unbranded shared boards are legitimately one photo. Some hosts re-encode
  per request, so MD5 is a measurement, not an identity.
- **CSV import (Matrixify):** `Handle, Command, Image Src, Image Position, Image Alt
  Text, Image Command`, `MERGE`, position 1 (pushes the placeholder to position 2). The
  handle comes from the census by id, never from the harvest. HEAD every URL before
  delivery; validate every handle against a live pull. A later harvest of the same brand
  is a check on the earlier one — lots are never closed.
- **State (23 Sep):** 1,745 rows delivered across 26 lots; ~6,157 placeholders remain,
  of which ~4,293 sit in brands with a measured ceiling under 4% (Kidde Fenwal, Hochiki,
  Fiplex, Napco, Monaco, Gentex, Resideo…). **Work Amerex, Rath, Edwards, Power Sonic
  and Macurco (~300 obtainable), then stop and ask the manufacturers for dealer image
  packs.** PDF-extracted images (Kidde Fenwal, the Kidde Genesis ZIP) need a
  bytes-upload path that Matrixify cannot provide.
- **Say which ceiling a coverage number hit** (catalogue coverage, image size, or
  matching) and carry its denominator; exclude licences, services and bulk cable first.

## Owner decisions and flags

- **Flag, do not apply:** vendor/brand, `productType`, pack counts in titles, SKUs,
  lifecycle/discontinuation, feed inclusion, regulatory approvals asserted in titles
  (e.g. `LADBS`), a product physically on the shelf that may not match its SKU.
  Write them to **`/tmp/tfas/DECISOES_DO_DONO.csv`** (`prioridade, sku, campo,
  valor_atual, recomendado, por_que, confianca, impressoes_6m, receita_erp`) and keep
  going. Pack-count detail: `/tmp/tfas/PACKCOUNT_decisao.csv`.
- **Open asks that research cannot settle** (phrase them to the owner as the cheapest
  thing that settles them): Fiplex Document Center login (DHS40-HG-SCH-1-A only); Gentex
  cross-reference chart (four pages); Power-Sonic/Potter/Kidde price lists or carton
  labels for the nameless-title floor; whether a family render may stand in for a
  configuration or variant SKU (~20 E2S, Fire-Lite `ES-200XC`/`MS-5UD-3E`, Mircom
  populated-enclosure shots); duplicate listings (U+00A0 SKU twins, 34 RedPipe pairs,
  `868STRC-AQ` SKU corruption); 13 titles with `?`-destroyed characters needing
  re-import; ~300–400 titles truncated at 150 characters by an import.
- The owner's standing rules: no &quot;Non-Fire&quot;/&quot;(Security)&quot; in titles;
  enrich all 264 `custom_label_0 = high_revenue_no_ad_spend` products (done).

## State and measurement

- **Progress (23 Sep 2026): 1,359 enrichment pages published** = 555 old list + 804 v2
  ids across v2b01–v2b52 (v2b50 and v2b51 verified live on 23 Sep), plus 260
  title-only products, 80 catalogue-wide title-encoding fixes and 75+6 brand-and-SKU
  dedups. v2b52 fully published 23 Sep (12 ids). Enrichment paused after v2b52 by the owner. Update this line from a live pull, never by adding.
- **Queue economics:** value per batch falls steeply; a natural stopping point sits
  around batch 135 (see `registro/negocio-ads-medicao.md`). Revenue per impression stays
  $25–38 across bands. Thermostats convert at 1/200th of the fire core per impression.
- **Measurement checkpoints: 2026-10-21 (30 days) and 2026-11-20 (60 days)** against
  `/tmp/tfas/BASELINE_555_publicadas.csv`. The site was already gaining positions before
  enrichment began, so a before/after is contaminated; **the randomised hold-out (36
  frozen ids, `EXPERIMENTO_holdout.csv`) is the evidence base.** Search Console via the
  Windsor `searchconsole` connector (the Ahrefs GSC tools return nothing for this
  project).
- **Google Ads: always pass `accounts: ["151-468-5549"]`** — the connector also serves
  The House Supplier (`192-200-0533`). Windsor cannot create PMax or Shopping campaigns.
  tROAS was cut 650%→500% on 22 Sep; **on 23 Sep the owner switched the Primary purchase action from the GA4 import (`6910639875`, 90-day window) to the Shopify app tag `Google Shopping App Purchase (1)` (`7700459405`, 30-day, enhanced conversions on), GA4 now Secondary — never both Primary (that caused the Jul–Aug double count); both changes read together ~6 Oct;** review **budget utilisation**, not reported ROAS
  (attribution loss; check MER = Shopify net sales ÷ Ads spend). A duplicated conversion
  action inflated Jul–Aug. List conversion actions before reading any ROAS trend. Titles
  and descriptions are Merchant Center feed attributes — errors cost two channels.
- **Daily sales are dominated by single large orders** (one day's lift was two orders,
  38% of the day); do not attribute a day to enrichment.
- **Archiving: closed.** Never run an archive filter without the ERP sales export
  (`/tmp/tfas/sales_joined.json`); zero products currently qualify. Revisit the Jun–Aug
  2026 cohort around March 2027.
- **Demand data:** `/tmp/tfas/demanda_ahrefs_COMPLETO.csv` (1,522 SKUs with ≥20/month).
  Strip Resideo `/u /b /e /a` suffixes before querying; exclude SKUs under 4 characters;
  `keywords-explorer-overview` silently caps at its `limit`.

## Conventions

- Battery capacity, pack counts and fiber mode (single vs multi) in titles are the
  highest-risk fields; verify against a manufacturer document every time. A card can
  carry no optics at all (mode set by a separate transceiver).
- Scratch scripts and datasheet PDFs produced during research are gitignored.
- Catalogue (21 Sep 2026): 19,442 products, 16,031 active, 3,411 archived.
