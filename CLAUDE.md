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
for approval to continue. The owner restated this on 22 Sep 2026 as
**&quot;segue sempre&quot;** &mdash; keep going, always &mdash; and **said it again
later the same day, unprompted, after six batches had already run**. Treat it as a
standing order that does not expire and does not need re-confirming: **never end a turn
asking whether to continue.**

**What it looks like in practice, measured on the day it was restated.** Six batches
(v2b20&ndash;v2b25), 108 products sliced, 90 published, four live title corrections
outside any batch, a catalogue-wide verification sweep, 29 rows consolidated into the
owner's decision file, and the Google Ads target changed and its baseline frozen. The
shape that made that possible is **three research agents always in flight while the
coordinator does something else** &mdash; validating the previous batch, running a sweep,
fetching a document to check an agent's strongest claim, or writing up what the last
batch proved. **Idle coordinator time is the only waste in this loop**, because the
agents are the long pole and nothing the coordinator does is on their critical path.

**One thing the owner does NOT want interrupted for: findings.** Report them as they
land, in the same turn as the work. The exception in the next paragraph &mdash; structured
data that feeds Merchant Center &mdash; is a *flag*, not a *pause*: write it to
`DECISOES_DO_DONO.csv` and keep going.

### How &quot;continuously&quot; actually works, and the one way it breaks

Learned by breaking it on 22 Sep 2026. **A research agent finishing wakes this
session automatically** &mdash; that is the mechanism the whole batch loop runs on,
and it is why v2b16 and v2b17 advanced through validate, publish and re-launch with
no user message in between. What does *not* happen is a timer: nothing wakes the
session on a schedule unless one is deliberately armed.

**So the loop has exactly one failure mode: ending a turn with no agent in flight.**
That turn's last words become the last words, because there is nothing left to
trigger the next one.

It failed that way once, and the shape is worth keeping because it is this project's
own recurring error wearing different clothes. The coordinator wrote
*&quot;Sigo para v2b18 agora&quot;* as closing text **without having launched the
agents**. The sentence occupied the position where the action belonged &mdash; a
statement that reads like a result and is not, which is the same defect as a title
asserting a spec nobody sourced.

**The rule: launch before you write.** Build the slice and start the agents as the
first act of the turn, then report. A turn that reports progress while holding no
running work has stopped the pipeline, whatever its prose says. If a batch genuinely
cannot start &mdash; a blocked host, an exhausted queue &mdash; say that plainly
instead, because an explicit stop is recoverable and a silent one is not.

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

**Progress: 1,047 pages published** — 555 from the old list plus v2b01 through
v2b27, plus seven from the first photo batch (`foto01`), plus two queued title defects (`4-NET-SM`, `ZH-MC-W`) and four Thermotech
title corrections — plus 80 title-encoding fixes applied
catalogue-wide. **The revenue frontier is exhausted**: all 170 of the
`FRONTEIRA_receita.json` products are published, v2b22 was the transitional batch
(8 frontier plus 10 by score) and **v2b23 is the first drawn entirely from
`ranked_v2_byscore.json` again** &mdash; 19,975 impressions and $885,277 in one slice,
which is a better batch on both axes than most of the frontier run. One product,
`SM7100-L8`, was deliberately skipped as unverifiable rather than written from
reseller data; the deliberate-skip list is now `SM7100-L8`, `90521`, `BDA-NMP01250`
and `BDA-TP10-L2`, all four blocked by a host or a login rather than by absent
documentation.

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

**The same failure has a second form, and v2b20 produced four instances of it in
one batch: the briefing was wrong about what the product IS.** Not the id &mdash;
the brand and the class. In **every one of the four the slice file was right and
the coordinator's prose was wrong**:

| part | the briefing said | the document says |
|---|---|---|
| `MPS-100` | Mircom power supply; establish output current and battery charging | **Eaton Wheelock single-action manual pull station** (`TD450082EN`) |
| `NIC-C` | Mircom; route to mircom.com | **Siemens** FireFinder XLS network interface card (`500-033240`) |
| `TC840C3206` | Honeywell commercial controls, not fire &mdash; maybe a thermostat | **addressable multi-criteria fire/CO detector** on the XLS FlashScan SLC |
| `2099-` series | Simplex releasing / agent-release modules | Simplex **non-coded manual pull stations**; releasing is one sheet inside it |

`MPS-100` is the one that shows the cost. Had the agent trusted the prose it would
have researched and published **a power supply that does not exist** &mdash; output
current, battery charging capacity, enclosure, all of it invented off a premise,
on a page that would have looked entirely normal. The `2099-` error is subtler and
would have been worse to catch: releasing stations use **break rods**, ordinary
stations **breakglass**, so the wrong premise points at the wrong sibling and the
copy comes back plausible.

**So the rule generalises past ids: the slice file is the authority on vendor,
type, title and id together, and the briefing prose is a hypothesis.** State
routing guesses as guesses (&quot;this looks like X, verify before using it&quot;),
never as fact, and **when the prose disagrees with `aN_in.json`, the file wins
without argument**. Three of these four were catchable for free &mdash; the input
file already said Eaton Wheelock / Pull Stations, Siemens, and a fire detector
type &mdash; which is the same lesson the lossy-`type` incident taught from the
other direction: **the structured fields in the slice are evidence, and the
coordinator is the least reliable source in the loop.**

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
ASCII**, because titles are Merchant Center feed attributes.
**Clarified 22 Sep 2026, because the old wording was pushing agents to mangle real brand
names.** &quot;Plain ASCII&quot; is a rule about *characters*, not about *entities*, and
the two were being conflated. **`&` is ASCII (0x26) and a title is plain text, not
HTML** &mdash; so **`AT&T` is a perfectly legal title** and so is `Air Products & Controls`.
What is wrong is writing the literal six characters `&amp;` into a title, which is exactly
the defect this file already records for the two titles containing a literal `&nbsp;`.
So: **in a title write `&`; in a description write `&amp;`.** A briefing that told an
agent &quot;`AT&amp;T` is not writable in a title&quot; was wrong, and the agent caught
it. The earlier decision to
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

**Re-run at batch 19 (896 pages, 22 Sep 2026): clean again, and the sweep has now
found nothing three times running.** All 896 tracked ids are present in the active
catalogue &mdash; **zero missing** &mdash; and exactly **four** pages sit under 400
visible characters, all four being the deliberate skips (`SM7100-L8`, `90521`,
`BDA-TP10-L2`, `BDA-NMP01250`). The ASCII title check over the same live pull:
**56 of 16,031 titles carry non-ASCII characters and every one is `&deg;`, `&reg;`
or `&trade;`** &mdash; 26, 25 and 5 respectively, **zero outside that set**, unchanged
from the batch-14 count across roughly 220 further titles written since. **Worth
noting what the clean run costs: one bulk query, 16,031 products, under a minute
end to end.** At that price the argument for running it every ten batches is weak;
run it every five.
**And a flag of the coordinator's own died in it.** `PAD100-6DB` was noted as a
non-ASCII title defect while building the v2b21 slice, from the curly `6&rdquo;` in
`FRONTEIRA_receita.json`. The live title carries a **plain** `6&quot;`; the curly
form survives only in the description body and in a working file built before the
80-title normalisation pass. **That is the snapshot rule firing on a file nobody
thinks of as a snapshot** &mdash; `FRONTEIRA_receita.json` is derived data, frozen at
the moment it was built, and a title defect read out of it is a defect that may
already be fixed.

**Re-run at batch 24 (986 pages, 22 Sep 2026): clean a fourth time, and the non-ASCII
title count is falling on its own.** All 986 tracked ids present &mdash; **zero
missing** &mdash; and exactly **four** pages under 400 visible characters, all four the
deliberate skips. Non-ASCII titles: **50 of 16,031, every one `&deg;`, `&reg;` or
`&trade;`, zero outside that set**, and a **new check added this session returns zero
titles containing a literal HTML entity** (`&amp;`, `&nbsp;`, `&quot;`), confirming the
two `&nbsp;` titles stayed fixed and none have reappeared.
**The count went 56 &rarr; 50 without anyone churning a title for cosmetics**, which is
worth understanding rather than celebrating: the rule says *do not rewrite an old title
purely to remove a degree sign*, and that does not stop the number falling, because
enrichment rewrites titles for **substantive** reasons and the replacement is written
under the plain-ASCII rule. Six Thermotech titles carrying `135&deg;F` became `135F` as a
side effect of the rate-compensation correction. **So the deliberate-leave-alone set
drains as the queue advances, and needs no separate project.**

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
- **SUPERSEDED 22 Sep 2026: Edwards IS first-party, and the LifeLines library is
  found.** This file said for four days that &quot;Edwards documents are not on
  edwardsfiresafety.com&quot; and that PDFs had to come from verbatim mirrors. That is
  wrong, and it was wrong because nobody had looked for the library the file itself
  flagged as worth finding. An agent found it; the coordinator verified all three
  claims directly, because it overturned a recorded rule.
  **Route 1: `https://www.edwardsfiresafety.com/lifelines/<category>`** &mdash; e.g.
  `/lifelines/speakers-strobes-horns-bells-and-chimes`. Plain HTML, HTTP 200, no bot
  protection, ~108 KB, and it embeds direct links to roughly 35 catalogue sheets per
  category. **Route 2: those PDFs live on
  `https://myeddie.edwardsfiresafety.com/PublicMedia/Catalog%20Sheets/`** with the slug
  form `E85001-NNNN -- <Descriptive Title>.pdf`, mime-clean `application/pdf`.
  **The old `myeddie` shell fingerprint was right about the wrong path, and the
  distinction is the whole finding.** A control with a bogus filename returns:
  **`/PublicMedia/Catalog Sheets/` &rarr; a clean HTTP 404 at 1,245 bytes**, while
  **`/Media/Catalog Sheets/` &rarr; HTTP 200 with an 8,909-byte shell.** So `/Media/`
  is the poisoned path and `/PublicMedia/` is the real library. **The mirrors &mdash;
  lsicloud, unilogcorp, steelfire, qdigital, savemoreonfirealarmparts &mdash; are no
  longer needed for Edwards catalogue sheets.** This unblocks the SIGA parts still in
  the queue. `est.net` and `edwardsfiresafety.com/files/import/` remain shells.
  **Kidde has the same library and it is machine-readable**: `kidde-esfire.com`'s own
  JavaScript discloses `POST /LiteratureLibrary/GetCategoryNavigation` with
  `categoryName=<name>`, returning JSON with every PDF URL for that category. Its JS
  namespace is literally `EdwardsPublic` &mdash; one codebase, two brands, which is the
  thread that led to the Edwards library in the first place.
  **The lesson is about this file, not about Edwards. A recorded negative decays.**
  &quot;Not on their site&quot; was true when tested and stayed in force as fact long
  after; the note even carried its own to-do and nobody ran it. **Re-test a
  host-level negative before building a batch around the workaround.**
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
  `/tmp/tfas/DECISOES_DO_DONO.csv`** &mdash; **190 rows as of 22 Sep 2026** (29 when this note was written), each with
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
- **Widening that scan taught the same lesson a fourth time, and then a new one.**
  Loosening the stem to &quot;drop the last hyphen segment&quot; took the flag count
  from 18 to **203** &mdash; the over-firing signature, immediately. The fix was a
  mechanism, not a threshold: **a short trailing segment is a variant suffix, a long
  one is model identity**, so only drop a final segment of two characters or fewer.
  That gives 106 families and **52 outliers**, and inspecting all 52 rather than
  reporting the number is what made it useful.
  **The new lesson is a reframing, and it matters more than the count. In a large
  share of these families the MAJORITY is wrong and the minority is right** &mdash;
  `ELMTSR-N` and `ELMTSW-NA` are correctly typed Horn Strobes inside a family typed
  Strobes; `P2WLED-SP` likewise; `VSR-CR-3` is correctly typed Switches in a family
  typed &quot;Fire Alarms&quot;; `AFAWS-BX` is correctly typed Backboxes in a family
  typed Doors; and **`HONBDA-7S27B-IB-18` is correctly typed BDA inside the family
  typed Annunciators**, which is the already-confirmed `-IB-10` defect found from the
  other direction. So &quot;outlier&quot; is the wrong word for what this scan
  returns: **it finds a broken family by its one healthy member.** Counting outliers
  therefore *understates* the defect, which is the opposite of every previous scan on
  this catalogue and worth remembering before anyone sizes the work from the flag
  count. A good part of the rest are mere taxonomy-granularity differences &mdash;
  Kits against Bezel Kits, Relays against Relay Modules, Surface Boxes against
  Backboxes &mdash; real inconsistencies but not worth a write.
- **Two title defects the scan surfaced that no keyword search would have, both
  queued for agent research rather than acted on.** First: **`4-NET-SM` is titled
  &quot;Dual Line Dialer&quot; inside a family that is uniformly SFP network
  controllers** &mdash; `4-NET-CAT` copper, `4-NET-MM` multimode, `4-NET-SMD`/`-SMU`
  single-mode single-fiber, `4-NET-SMH` single-mode dual-fiber. **`SM` means
  single-mode everywhere else in the family**, a dialer is a DACT, and the part is
  $1,522. That is the adjacent-row trap, and **fiber mode is one of the three
  highest-risk title fields in this catalogue**, so it needs the Edwards EST4 ordering
  table and not a pattern. Note the type field was **no help at all** &mdash;
  `4-NET-SM` and `4-NET-CAT` are both the generic &quot;Fire Alarms&quot;, agreeing
  with the wrong title; **the entire signal came from the siblings.** Second:
  **`ZH-MC-W`'s complete title is &quot;Siemens ZH-MC-W (Replaced by SLHSWW-F)&quot;**
  &mdash; a part number and a parenthetical, with **no class noun and no descriptive
  name at all**, whose one substantive claim is an unsourced supersession sitting in a
  Merchant Center feed attribute, on the brand where exactly that claim has already
  been wrong twice. Its family also splits on class and on price ($272.15 against
  $101.40 for three siblings). Both are in `pending_fixes.md`.
- **The coordinator predicted a live claim was wrong and the live claim was right.
  Worth recording because the scepticism, not the page, was the error.** The
  `ATD-L3R-IV` page said the `-IV` models run both Velociti and CLIP while the
  suffix-free part is Velociti only, and the briefing told the agent *&quot;that is a
  strong, specific, falsifiable claim and it is the kind that is usually wrong &mdash;
  a finish suffix does not normally change a communication protocol.&quot;* It does
  here. Gamewell-FCI `9020-0620 Rev G` lists all six members with the protocol against
  each finish, and its Description paragraph gives the mechanism outright: *&quot;For
  legacy installations, service detectors are available in the classic ivory color
  that will operate in both Velociti and CLIP protocol for backwards compatibility.
  Service models are designated by the -IV part number.&quot;* **Ivory is a
  service-stock designation that carries a dual-protocol build, not a colour option**
  &mdash; two independent places in one document agreeing. The general lesson is not
  &quot;trust the live page&quot;; it is that **&quot;that kind of claim is usually
  wrong&quot; is a prior, not evidence**, and it has to lose to a document like any
  other prior. The same confirmation cleared the held `ASD-PTL3` page, whose closing
  makes the identical claim on the parallel photoelectric line.
- **Every distributor can be wrong together, and the mechanism was visible on the
  page.** `BDA-NM-RG8-13-NM` is **51 inches** per Honeywell `HON-62084.02`
  (11/29/2021); every reseller says 48. The mechanism: **page 1 of that same brochure
  tabulates a different part, `BDA-NM-RG58-12-NF`, at 48 inches**, and page 5 is the
  only page carrying the part in question. Distributors read the first table in a file
  named for the part they wanted. The numeric field is also **not a length** &mdash;
  `-08-NM` is 24 in., `RG58-10` is 37 in., `RN4P-03` is 10 in. &mdash; so the
  briefing's &quot;inches or feet, a factor of twelve&quot; framing was wrong in a
  third way. **The 51 in. figure went in the body and deliberately not in the title**:
  a length contradicting every distributor and possibly the stock on the shelf is a
  feed claim the owner should confirm against a carton first.
- **`fiplex.com` is a new blocked-host fingerprint, and it cost a page.**
  `/Datasheets/` paths return **HTTP 400 with an Akamai &quot;Access Denied&quot; body
  of 456 bytes `text/html`** to curl on both HTTP versions, to curl with full Safari
  headers, to `urllib` through the proxy and to WebFetch; `/wp-content/` paths time out
  at **0 bytes** after 60 and 90 seconds. No Wayback capture, and the Document Center
  needs sign-in. `BDA-TP10-L2` was therefore **left unwritten by decision** rather than
  built from reseller copy &mdash; three sources give three different frequency ranges
  for it, which is exactly why. The document is named and findable: Fiplex
  `BD500-High_Power_Tapper_138-960MHz`. **One owner login to the Fiplex Document Center
  would settle both this and `BDA-NMP01250`; ask for BD500.**
  Mapped in the process, and useful next time: the Fiplex passive-device series on
  EDAM is `HON-62073` (DC-W2), `HON-62074` (DC-L2), `HON-62075` (HC3-L2), `HON-62079`
  (PSx-L2 splitters) and `HON-62084` (jumpers), with **`-L2` low band and `-W2`
  wideband, manufacturer-stated.**
- **`alldataresource.com` cuts both ways, so the mime check decides which.** It served
  a **verbatim 382,945-byte mirror** of `HON-62084.02` whose footer, template and
  imprint match two sheets pulled directly from `prod-edam` &mdash; and it returns a
  **313,459-byte HTML shell** for a PDF it does not have. Same host, same request
  shape, one good and one poisonous. This is the `systemsensor.com` lesson again on a
  host the project already distrusted: **`file -b --mime-type` is what separates them,
  not the host's reputation.**
- **DITEK reissued its whole `SPS-` datasheet series in 04/26, so any DITEK figure
  quoted from an earlier revision needs rechecking.** `DTK-MRJPOEX` is the worked
  example: every reseller and all older literature say 802.3af/at and &quot;PoE Plus,
  HiPoE ready&quot;, while `SPS-100042-010` **Rev 11** carries a four-row IEEE table
  adding **802.3bt Type 3 (60 W) and Type 4 (100 W)**. Also corrected: **DITEK's site
  is `diteksurgeprotection.com`**, not `ditekcorp.com`, which only survives inside
  older install sheets. And the ordering syntax is settled from the manufacturer's own
  tables: **`B` = fails short to ground and 5 A max continuous, `F` = fails open
  circuit and 1 A, `WB` = includes the single-position mounting base.** Two agents
  reached that independently from opposite ends of the pair and every shared figure
  agreed &mdash; 20,000 A, UL 497B, 30&ndash;12 AWG, &minus;40 to 158 &deg;F,
  3.25 &times; 1.5 &times; 2.65 in. **Pair-splitting paid again.**
- **Two revisions of one Honeywell datasheet disagree on the number a battery
  calculation depends on.** Silent Knight `350098` **Rev K (02/22)** gives the 5815XL
  &quot;Standby &amp; Alarm Current: 55 mA&quot;; **Rev J (01/18)** gives &quot;55 mA
  minimum &ndash; 125 mA max&quot;. No current figure was published. Rev J also lists
  5820XL and 5820XL-EVS IntelliKnight compatibility that Rev K drops, and **no document
  says support was withdrawn**, so the copy states the current list and mentions the
  older one as a relationship rather than asserting a discontinuation either way.
- **The `-IV` suffix encodes a PROTOCOL, not a colour, and it is a Honeywell-wide
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
- **The `GW` prefix hides the real manufacturer catalogue number, and it has now fired
  twice in two batches.** `GWPID-95` is `PID-95` in `CS-2044` Rev B; `GWRCE-95` is
  `RCE-95` throughout `CS-2045` Rev C including its Ordering table. **In both cases the
  `GW` form appears in no Gamewell-FCI document at all** &mdash; recorded as a bounded
  negative both times, with the real number added in parentheses rather than the SKU
  being touched. **There are 30 Gamewell-FCI `GW*` SKUs and only one already names a
  catalogue number in its title.** So the routing rule for this brand is: **search the
  part number with the `GW` stripped**, and expect the documents to be filed under the
  bare form. Beware the false friends &mdash; of 83 `GW*` SKUs, **50 are Gentex**, where
  `GWHS…` is a genuine Gentex weatherproof horn-strobe family and nothing is hidden.
- **The conditional-headline rule paid on its first reuse, one batch after it was
  written.** It was recorded from `D1xB2XH1…`, where the datasheet headlines
  &quot;86.37cd&quot; flat and only the instruction sheet reveals that is the 1 Hz
  value. The next E2S part, `D1XS2FDC024CS1A1R`, was briefed with it and **the same
  shape fired**: the datasheet's headline **123 dB(A)** turns out, in instruction
  manual `D190-00-101-IS Issue 6`, to be the **maximum at high power on tone 4**, with
  **118 dB(A) nominal on tone 44** and 120/115 at default power. The copy quotes the
  figures with their conditions. **A written-down trap that catches its next instance
  is the whole return on writing traps down**; this one now has two independent
  confirmations on one brand, so treat any single headline acoustic, candela or current
  figure on a configurable device as conditional until the instruction sheet's table
  says otherwise.
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
- **When two Honeywell documents disagree, prefer the part-specific manual over a
  sibling brand's catalogue sheet.** Fire-Lite `DF-60059:G` (a 2015 catalogue sheet)
  and System Sensor `I56-3737` (the part's own manual) disagree on **five** `B224RB`
  figures at once &mdash; diameter (6.1 in. against 6.85 in.), standby current
  (&lt;500 &micro;A against 170 &micro;A), relay set times, AC contact rating (0.9 A
  against 0.5 A at 125 VAC) and single-gang box compatibility. **Only the intersection
  was published.** The diameter split may be an old-style/new-style generation
  difference &mdash; resellers list both &mdash; but no document says so, so nothing
  was claimed. Five disagreements in one pair is not a typo; it is two generations or
  two sources, and neither is resolvable from the documents alone.
- **Tenth coordinator premise wrong: `WG4RF-HVMHC` is not a residential Kidde number.**
  The briefing warned it &quot;looks like a residential/consumer Kidde number&quot; and
  told the agent to establish the UL standard first. It is an **85001-series commercial
  Genesis WG4 outdoor horn strobe**, and the suffix reads straight off the ordering
  table: **H horn, VM visual multi-candela, HC high candela.** The warning was still
  worth giving &mdash; it forced the check &mdash; but the guess inside it was wrong.
  **And the E/K prefix-swap rule is confirmed for a third time:** Kidde `K85001-0628`
  Issue 1.1 (2020) and Edwards `85001-0628` Issue 2.2 (2013) agree **exactly** on every
  candela, current, dB, dimension and temperature figure, seven years apart.
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
- **`RSG` is a Potter Electric Signal Company brand**, and Potter serves the document
  first-party (`8820099 REV A`), so no mirror is needed. Its model-number syntax block
  decodes `DH24120FB` completely: `DH` door holder, `24120` dual 24 V and 120 V, `F`
  flush, `B` brass. **Note the four mount styles it lists are Surface, Flush, Ground
  and Recessed &mdash; there is no &quot;semi-flush&quot;**, which is distributor
  wording that had reached the store title.
- **The `-IV` protocol finding was confirmed a second time inside the same batch, by a
  different agent on a different product line.** Agent 2 had `H365R-IV` and agent 3
  `SD365T-IV`; both found the note independently, and `DF-61010:C`'s ordering block
  carries it in the same words as `DF-61011:C` &mdash; *&quot;'-IV' suffix indicates
  CLIP and LiteSpeed device&quot;*, against white heads listed **&quot;LiteSpeed
  only.&quot;** Two brands, three product lines, four documents. The routing note above
  stands, and **any collection logic or copy treating `-IV` as a colour variant is
  wrong.**
- **EDAM has BOTH slug orders, so try both before searching.** The briefing gave
  `<Model>_<DocNum>.pdf` from `SD365_DF-61010.pdf`; an agent found
  **`DF-61012_ANN-100.pdf`** resolves too &mdash; `<DocNum>_<Model>.pdf`, the reverse.
  Eight other guesses for that document returned the 8,047-byte fingerprint. And **the
  bare `<docnum>.pdf` route is stronger than recorded for Gamewell-FCI**:
  `9021-60758.pdf`, `9020-0649.pdf` and `9020-0541.pdf` all resolved first try, three in
  a row. For that brand it is the cheapest route, not a long shot.
- **Two more first-party hosts mapped.** `support.westell.com/documents/<slug>-DS.pdf`
  serves Westell datasheets directly, no bot protection, mime-clean &mdash; **so the
  &quot;relationship-sold means undocumented&quot; premise fails for a third category**,
  after Fiplex and Det-Tronics. And **STI's real document host is
  `cdn.sanity.io/files/4ikv42xc/production/<hash>.pdf`**, linked from `sti-global.com`
  product pages; `sti-usa.com` is only the footer address, so paths cannot be
  constructed &mdash; read the product page. STI publishes three documents per product,
  and the **sales data sheet carries a Build-Your-Model ordering-syntax block** that
  decodes the number character by character, the same class of decoder as Edwards
  catalogue page 5 and Eaton `TD450158EN` Table 3.
- **Two more self-contradicting documents, both resolved by publishing nothing.**
  Siemens Data Sheet **6306** says *&quot;Durable metal design&quot;* in its A&amp;E
  bullets and *&quot;constructed of durable, molded polycarbonate material&quot;*
  in the Specifications paragraph **immediately below, on the same page**; the
  installation sheet states no material, and the reseller pages repeat the
  polycarbonate line, which is the datasheet prose rather than a third source. No
  material claim published. Two **STI** documents disagree on the polycarbonate
  temperature range &mdash; sales sheet &minus;40 to 250 &deg;F, installation sheet
  &minus;40 to 284 &deg;F. No temperature published. **That is now five documents in two
  batches contradicting themselves on a spec**, which makes it ordinary rather than
  remarkable: budget for it, and treat &quot;the document says so&quot; as needing a
  second reading of the same document.
- **The series-wide spec block is a new shape of the adjacent-row trap.**
  `DF-61010:C`'s System Specifications prints one thermal line for the whole SD365
  family &mdash; fixed 135 &deg;F, rate-of-rise 15 &deg;F/min, high-temperature
  190 &deg;F &mdash; **with no model attribution**, while the Product Line entry for
  `SD365T-IV` names only a fixed-temperature device. Reading the series block as if it
  described the part would have published a rate-of-rise claim on a fixed-temperature
  detector. **A spec block that covers a family is not a spec for any member of it.**
- **A load-bearing restriction can live in an asterisk footnote hanging off the
  ordering table, where grepping the body returns a false negative.** The live
  `WAV-CWL` page claims the wall bases fit only L-Series devices *&quot;manufactured
  after 26 April 2019, date code 9045 and later&quot;* while the ceiling bases are
  unrestricted. **Confirmed in three documents** &mdash; `SPDS902-04` (3/10/2022, a
  revision newer than the `SPDS902-01` the sibling page used), `SPDS902-01` and
  Gamewell-FCI `9021-61070:C` &mdash; in almost the page's own words. **But the note is
  a footnote on the table, not prose.** Anyone checking that claim by searching the
  datasheet text would have found nothing and called it unsourced, which is the
  wrong-document-family failure in miniature: right document, wrong part of it.
  **Read ordering-table footnotes before declaring a compatibility claim unsupported.**
- **Eleventh product-class error, and the giveaway was a new one.** `3-SDC1` was titled
  *&quot;Signature Driver Controller Module&quot;*. Edwards heads its Ordering
  Information **&quot;3-SDC1: Signature Device Card &ndash; upgrades a 3-SSDC1 to a
  3-SDDC1&quot;**, and lists the controllers separately: *&quot;3-SSDC1: Single
  Signature Driver Controller. **Comes with one 3-SDC1 Device Card**&quot;* and
  *&quot;3-SDDC1: Dual … **Comes with two 3-SDC1s**&quot;*. A buyer ordering a loop
  controller received a plug-in card that does nothing without a controller already in
  the cabinet. That is the `4099-9015` / `A49CMT-APPLW` incomplete-product shape, but
  **the tell here is not the word &quot;required&quot;** &mdash; it is **the sibling
  rows stating what they come with**. Add that to the checklist: when a catalogue
  number appears inside another product's &quot;comes with&quot; clause, it is a
  component, not the product. The `type` field said Modules and agreed with the wrong
  title, so it raised nothing again.
- **The E/K prefix rule reaches down into part numbers, not just document numbers.**
  Same document number, different brand: `K85001-0667` is titled *&quot;Genesis LED
  **EG1** Series&quot;* and `E85001-0667` *&quot;Genesis LED **G1** Series&quot;*, with
  every spec matching (16&ndash;33 VDC/VFWR, 15/30/75 cd, 20 &#937; sync,
  3 &times; 4-5/8 &times; 1-1/8 in., &minus;0.71 in. box offset, 32&ndash;122 &deg;F).
  Trim rings follow it too: `EG1TR`/`EG1TW` against `G1TR`/`G1TW`. **So a Kidde
  catalogue number on this line is the Edwards number with an `E` prefix** &mdash;
  search both forms, and reach for Kidde's first-party host rather than an Edwards
  mirror. An MD5 check also proved verbatim mirroring the cheap way again: `K85001-0640`
  came back byte-identical from two unrelated mirrors.
- **Every distributor wrong together, for the second time in three batches.**
  `ELSPKBB-R` is a **wall** back box: Eaton `TD450158EN`'s backbox table, confirmed on
  one y-line by word coordinates, reads `ELSPKBB-R` &rarr; Wall, `ELSPKBB-W` &rarr;
  Wall, `LSPKBB-CR`/`LSPKBB-CW` &rarr; Ceiling &mdash; **the `C` in the sibling number
  is the ceiling marker.** ADI and Telcom-Data both list it as ceiling. After the
  51-inch Fiplex jumper this is a pattern worth naming: **distributor consensus is not
  evidence, and it fails in a correlated way**, because they copy each other rather
  than the datasheet.
- **A corroborating diagram can argue for the wrong reading, and only the render
  settles it.** On `E85001-0640` p6 plain text gives *&quot;Base height from box:
  0.8 in. | 1.4 in.&quot;* across three model columns. Word coordinates put both at
  cell-centre, and a 200 dpi render shows **0.8 in. spans the AB4G *and* AB4GT columns
  while 1.4 in. is AB4G-LF alone.** The page-3 exploded diagram groups
  &quot;SIGA-AB4GT(-LF)&quot; together, **which argues the other way** &mdash; so the
  one piece of apparent corroboration was the trap. Same merged structure on the
  Listings and Resonant-frequency rows. **When a merged cell and a diagram disagree,
  the render of the table wins.**
- **`RFP`'s &quot;5-Pack&quot; is unsourced, and this is the pack-count mechanism from
  the other side.** `AVDS870-03` (10/10/2023) **states pack quantities when it means
  to, on the same page, in the same Ordering Information block** &mdash; `TR-2`,
  `TRC-2`, `TR-2W`, `TRC-2W` each marked &quot;(5-pack)&quot;, `TRCWLA-10` and
  `TCRLA-10` &quot;(10-pack)&quot;, plus a footnote about bezel packs &mdash; and the
  two retrofit-plate rows carry **nothing**. `AVDS882-03` (2020) and `AVDS4004` (2015)
  do the same. **Three revisions across ten years, numbering RFP's neighbours and
  declining to number RFP.** That is exactly the `DN-62046:C` proof inverted, and it
  makes the negative positive. Title left untouched; flagged to the owner.
- **Correction: the Eaton `urllib` workaround is alive again.** This file records it as
  having worked on 21 Sep and failed later the same day. On 22 Sep `curl` still failed
  with an empty reply on both HTTP versions, and **Python `urllib` through
  `HTTPS_PROXY` with a Safari user-agent pulled both Eaton PDFs first try.** So it is
  intermittent rather than dead: **still worth one attempt, and now worth it before
  falling back to alarmax.**
- **A document defect can persist across revisions and across brands, which tells you
  it is the source and not your extraction.** `E85001-0640` and its Kidde twin
  `K85001-0640` both print the CAN/ULC-S525 row with **low dBA louder than high**
  (Temporal 24 VDC: 95 low, 91 high) &mdash; the same inversion, 2.5 years apart, under
  two brands. Nothing published from that row. Likewise all three SWIFT AV base
  datasheets print &quot;RF Operating Voltage Range 3.3 VDC&quot; and, two rows later,
  &quot;RF Operating Voltage 12 VDC&quot;. **Reproducing across revisions rules out
  extraction error and rules in a real document defect &mdash; which is a reason to
  publish nothing, not a reason to pick one.**
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
- **Ninth coordinator premise wrong, and the agent's handling of it is the model.**
  The briefing called `FSL-E3` a &quot;fiber SLC/loop module&quot;. `9021-60783` Rev F
  makes it an **ARCNET network module** &mdash; one transmit or receive channel for the
  `RPT-E3-UTP` repeater and INI-VG voice gateways, not an SLC device-loop card. But the
  agent did **not** rewrite the class noun out of the title, because
  **the document is itself titled &quot;FML-E3/FSL-E3 Fiber Loop Modules&quot;** &mdash;
  that *is* the manufacturer's product name, which house convention explicitly permits.
  It kept the name in the title, put *&quot;This is a network card, not an SLC device
  loop card&quot;* as the second sentence of the body, and flagged the `type` to the
  owner. **That is the right shape for every case where the manufacturer's own name is
  the confusing thing** &mdash; the opposite handling from `CPU2-3030D`, where the
  manufacturer's &quot;Primary Display&quot; wording was allowed to set the title and
  misled. Fiber mode settled positively for the exact part: single-mode, 9/125 &micro;m,
  LC, 30 dB, 0.079 A, against FML-E3's multi-mode, 62.5/125, ST, 8 dB, 0.053 A.
- **A stale model list can sit in a PDF's text layer without ever being rendered, and a
  grep alone reads it as a generation conflict.** Gamewell-FCI `9020-0617`'s text layer
  opens with `ASD-PL2F/ASD-PTL2F ASD-PL2FR` &mdash; **Series 2** codes &mdash; while a
  150 dpi render of page 1 shows only *&quot;Velociti Series 3 Detectors /
  Photoelectric Detectors&quot;*. The Series 2 strings are invisible leftovers. This is
  the **inverse of the invisible-dimension trap**: there the text layer was missing data
  that the page showed, here it carries data the page does not. Same remedy both ways.
  **Render before calling a generation conflict**, not only when a figure seems absent.
- **Word coordinates are necessary but were not sufficient, for the first time.** On
  Simplex `S49AVC-0001` Table 1, plain text put `579-1242` after &quot;Blue&quot; and
  word coordinates put it at y=250.6 next to &quot;Clear&quot; &mdash; but neither
  settled the *merged* Installation-Instructions cell. A 200 dpi render did
  (`579-1242` spans rows 1&ndash;6, `579-1279` the last two). So the escalation is three
  steps, not two: plain text, then `get_text(&quot;words&quot;)` with coordinates, then
  **render and read**. Also from that sheet: **`-BA` on a Simplex appliance code means
  &quot;assembled in the USA&quot;**, not a functional variant.
- **Tenth product-class error, and the type agreed with the wrong title again.**
  `ASD-PTL3` was titled *&quot;Thermal Sensor&quot;* and typed **Heat Detectors**, while
  `9020-0617` Rev K's ordering block reads *&quot;ASD-PTL3: **Photoelectric smoke
  detector** with thermal sensing&quot;* under a heading of &quot;Photoelectric
  Detectors&quot;, listed to **UL 268 7th Edition**. A buyer filtering for heat detectors
  gets a smoke detector, and one filtering for smoke detectors never sees it.
  **Its thermal class is separately contested inside that one document** &mdash; page 1
  prose says *135 &deg;F **fixed temperature*** and the page 3 spec block says
  ***Rate-of-Rise**: greater than 15 &deg;F/minute or 135 &deg;F*. Both give 135 &deg;F,
  so 135 &deg;F is published and neither class word is asserted. It is **not** rate
  compensation.
- **Three independent structural reasons can settle a self-contradicting datasheet, and
  that is stronger than preferring the table by rule.** Gentex's S-Series sheet lists
  `SHRR` among the models that *&quot;feature electrochemical CO sensing&quot;* in its
  Standard Features prose, while the ordering table gives the SHRR row **no CO bullet**
  (word coordinates: bullets at Smoke x=222.7 and Heat x=314.9, nothing at CO x=268.8).
  Three things side with the table, and none of them is &quot;tables beat prose&quot;:
  SHRR is a **917-** S-Series number where every CO model is **918-**; the Product
  Listings give the S Series **ANSI/UL 217 only**, UL 2034 being reserved for SC/C; and
  the SHRR harness diagram is labelled **HEAT ALARM CONTACTS** where STRR/SCRR says
  &quot;CO or HEAT&quot;. No CO claim was published either way. **When a document
  contradicts itself, look for a third and fourth signal rather than applying the
  table-over-prose rule mechanically** &mdash; the rule tells you which to bet on, the
  corroboration tells you whether to publish at all.
- **Gentex path construction failed for the S-Series, so the direct-serve rule has a
  boundary.** `SHRR-Series1`, `S-Series1`, `STRR-Series1`, `SR-Series1` and `S-Series2`
  all 404 at 7,264&ndash;7,273 bytes of `text/html`. The real file is
  **`GN600_S-C-SC-H_Series_FINAL_R1.pdf`** (doc code SCSCH-01), found by search. The
  `fireprotection.gentex.com/files/<Model>-Series<n>.pdf` pattern works for some
  families and not this one &mdash; **find the filename, do not build it**, same as EDAM
  slugs and `qdigital.mx`.
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
  bounded wrong.** System Sensor document **`9021-62013:C`, 9/25/2020** (L-Series Low Frequency)
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
  family's* sheet. Second, the document families differ: **`AVDS910-02` covers
  the same product and does NOT carry the footnote**, so on this brand **prefer the
  `9021-` document family over the `AVDS` one**.
  **CORRECTED 22 Sep 2026, twice over, and both corrections came from an agent
  contradicting this file.** (a) The document number is **`9021-62013`, with no `-E`
  suffix** &mdash; verified by the coordinator directly, where the bare name returns a
  206 KB PDF and `9021-62013-E.pdf` returns the 8,047-byte fingerprint. The `E` was
  never a revision letter; the revision is **`:C`**. (b) **The old/new framing was
  wrong on the dates.** `AVDS910-02` is **11/02/2020** and `9021-62013:C` is
  **9/25/2020**, so the `AVDS` sheet is the *later* document and still lacks the
  footnote. **The difference is between document families published weeks apart, not
  between an old revision and a new one** &mdash; which makes the rule stronger, not
  weaker: it is not that System Sensor added carton quantities over time, it is that
  one family states them and the other does not. Scope and per-SKU basis in `/tmp/tfas/PACKCOUNT_decisao.csv`.
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
  outright, and `9021-62013:C` states the LF sounders. So the split is not by brand and
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
  and for the low-frequency sounders via the `9021-62013:C` footnote, and for nothing
  else.** Detectors and notification appliances both fall outside it.
- **CORRECTION, 22 Sep 2026: that boundary was wrong. BATTERIES are a third category,
  and the quantities are not 10.** An agent found it and the coordinator verified it
  directly rather than taking the report on trust, because the claim overturned a rule
  this file states twice. Fire-Lite **`DF-52397:C1`** and its Notifier twin
  **`DN-6933:D`** each state five carton quantities verbatim in Ordering Information:
  `BAT-1250-BP: 10-unit bulk pack`, `BAT-1270-BP: 5-unit`, `BAT-12120-BP: 4-unit`,
  `BAT-12180-BP: 2-unit`, `BAT-12260-BP: 2-unit`. **So the rule becomes: Honeywell
  states carton quantities for bases, low-frequency sounders and batteries, and not for
  detectors or notification appliances.**
  **The sharper half of the finding is the one the agent did not draw: the quantity
  varies inversely with capacity &mdash; 10, 5, 4, 2, 2.** This catalogue's whole
  working assumption has been that `-BP` means ten, which is why the census phrase was
  *&quot;Bulk Pack with 10 Units&quot;*. On batteries that assumption is wrong four
  times out of five. **Checked against the live catalogue immediately: 18 `BAT-*` SKUs,
  two of them `-BP`, and neither asserts any quantity in its title** &mdash; so there is
  no live error, only an unclaimed documentary basis. Nothing was changed; both went to
  the owner's file.
  **The method lesson is the transferable one.** The rule was built from a genuinely
  strong proof &mdash; `DN-62046:C` stating a base's carton quantity and declining to
  state a detector's **on one page** &mdash; and it was still too broad, because the
  evidence covered bases against detectors and the conclusion said *&quot;and nothing
  else&quot;*. **A mechanism confirmed on two categories does not license a claim about
  every category.** The same over-reach the Protectowire spacing rule made when it
  broke at 220 &deg;F.
- **EDAM paths are case-sensitive, and this cost the verification a round trip.**
  `.../datasheets/DF-52397.pdf` returns the 8,047-byte fingerprint; **`df-52397.pdf`,
  lowercase, returns a 261 KB PDF.** An agent separately found the same for separators:
  **`DF_52004.pdf` (underscore) resolves where `df-52004.pdf` (hyphen) 404s.** So the
  path shapes to try, each one fetch, are now: bare `<docnum>.pdf`, **lowercased**,
  **underscore-for-hyphen**, `<Model>_<DocNum>.pdf` and `<DocNum>_<Model>.pdf`. Also
  recorded: `9020-0616.pdf` 404s under the flat directory while
  `datasheets/MS-7AF-Datasheet.pdf` serves that exact document, so **the bare-docnum
  route is strong for Gamewell-FCI but not universal &mdash; a model slug can be the
  filing key instead.**
- **&quot;Find the slug, do not build it&quot; has a boundary worth using.** EDAM holds
  two subdirectories this file had not recorded &mdash; `datasheets/flexbda-050526/`
  and `datasheets/fiplex-02022026/` &mdash; whose Fiplex passive-device slugs are long
  and descriptive. An agent found `HON-62071` by search and then **constructed the
  `HON-62072` sibling slug from it, and it resolved.** So: **within one document family
  in one dated subdirectory, the slug IS derivable from a sibling you already hold.**
  Eight guesses made without such a sibling all returned the fingerprint. Build from a
  known neighbour; never build from the document number alone.
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
- **`DACT-UD2` was typed &quot;Cellular Communicators&quot; and reports over telephone
  lines.** Manual `53037:B` &sect;1: *&quot;transmits system status to UL listed Central
  Station Receivers via the public switched telephone network&quot;*; two modular phone
  jacks, RJ31X, REN 0.0B, FCC Part 68, **no radio in the product at all**. DACT stands
  for Digital Alarm Communicator/Transmitter. The briefing predicted this from the
  acronym alone and the document confirmed it &mdash; **an expansion of the part's own
  initialism is a free class check worth running before any fetch.**
- **Two agents described the same E/K fact and one of them explained it wrongly; the
  sharper version wins.** Agent 2 reported *&quot;the Kidde catalogue number is the
  Edwards number with an `E` prefix&quot;* from `K85001-0667` (&quot;EG1 Series&quot;)
  against `E85001-0667` (&quot;G1 Series&quot;). Agent 1, reading each document's own
  syntax block, found the mechanism: **Edwards' series code is `GC` and Kidde's is
  `EGC`** &mdash; the `E` is *inside the series code*, not a prefix bolted onto a part
  number. Descriptively the two agree; mechanistically only one is right, and the wrong
  framing would mispredict any part whose series letters differ some other way.
  **Also found: a real product difference under one document number** &mdash; Kidde
  lists the GP10 wiring plate as *&quot;required, included with device&quot;* and
  Edwards as *&quot;required, ordered separately&quot;*, and Kidde's sheet drops the
  FEU/FUEGO and ALERT variants Edwards carries. **So the prefix-swap rule means the
  same hardware, not necessarily the same carton.**
- **Distributor consensus fails in a correlated way, which is why it is not evidence.**
  Third instance in four batches. `ELSPKBB-R` is a **wall** box (Eaton's backbox table,
  confirmed on one y-line by coordinates: the `C` in `LSPKBB-CR` is the ceiling marker)
  and ADI and Telcom-Data both call it ceiling. `BDA-NM-RG8-13-NM` is 51 in. and every
  reseller says 48. And **every reseller copy of the DITEK `120S` sheet is stale on four
  figures at once** &mdash; UL 1449 4th against the current **5th** Edition,
  &minus;40 to 185 &deg;F against **&minus;31 to 104 &deg;F**, the wrong depth, and
  40&ndash;400 Hz against **50/60 Hz**. They copy each other, not the datasheet, so
  agreement among them carries no independent weight at all.
- **The incumbent PMax's tROAS went 650% &rarr; 500% on 22 Sep 2026, and the diagnosis
  behind it is worth more than the number.** The campaign had **not** been throttled by a
  raised target &mdash; Windsor reports one tROAS value per campaign with no time
  variation, which is the signature of the *current* setting stamped on every historical
  row, so the connector cannot tell you when a target changed. The Ads UI screenshot
  confirmed 650% as the live value and $5,000/day as the budget, and nothing more.
  **What actually changed is what Ads can see.** Ads-conversions-to-Shopify-orders went
  0,77 (June) &rarr; 0,56 (4 wk) &rarr; **0,39** (week of 14 Sep) while **MER held at
  10&ndash;13**. Reported ROAS fell 10,18 &rarr; 4,69; the business did not. With the same
  6,5 target and predicted values halved, the bidder must bid down to reach it &mdash; and
  it did: rank-lost impression share 57,9% &rarr; **75,6%**, budget-lost 18,6% &rarr;
  **0,1%**, and **budget utilisation 101% (10 Aug) &rarr; 42%**, leaving **$20,347 a week
  of authorised budget unspent**.
  **Two independent routes gave the same target**, which is why 500 was defensible:
  rescaling the old target by the visibility loss (6,5 &times; 0,56/0,77 = 4,7; &times;
  0,48/0,77 = 4,05) and the trailing achieved reported ROAS (5,55 over 4 weeks, 4,69 over
  2). Both land at 4,0&ndash;4,7.
  **The method notes worth reusing.** (1) **A hard budget cap bounds the downside of a
  target cut**, which is what justified moving in one 23% step and reviewing in a week
  rather than two &mdash; worst case is a return to August's spend at August's efficiency,
  which was not a disaster. (2) **Review the budget utilisation, not the reported ROAS.**
  The reported number is depressed by attribution and will mislead. (3) **Lowering a
  target treats the symptom**; the cure is restoring conversion visibility, after which
  the original target becomes reachable again. Baseline frozen in
  `/tmp/tfas/ADS_configuracao_para_o_painel.md` so the 29 Sep read compares against
  numbers rather than memory.
- **The Windsor `google_ads` connector serves TWO businesses, and a query without an
  account filter silently blends them.** `151-468-5549` is **TFAS SHOPIFY**;
  `192-200-0533` is **The House Supplier**, a heating-supplies business. Earlier work
  in this file correctly scoped to `151-468-5549`; a query on 22 Sep dropped the filter
  and returned both, and the coordinator read a House Supplier Shopping campaign
  (`SHOPPING GABRIEL 8-3-2026`) as if it were TFAS's, complete with a recommendation
  built on it. **The owner caught it.** It is the same shape as auditing against the
  stale snapshot: measuring the wrong artefact, confidently, and reporting a
  conclusion from it. **Always pass `accounts: [&quot;151-468-5549&quot;]`.**
- **TFAS has no Standard Shopping campaign running, and its own history says not to
  start one.** Active in `151-468-5549`: the Performance Max 9-11-2024 (Product Only)
  campaign and a small `TFAS - Search`. Every Shopping campaign in the account is
  paused or removed. **Three of them did run over the last two years and together lost
  money:**

  | campaign | spend | clicks | CPC | conv | CVR | value | ROAS |
  |---|---|---|---|---|---|---|---|
  | US SHOPPING GABRIEL OCT 24 | $33,280 | 28,541 | $1.17 | 108 | 0.38% | $30,546 | **0.92** |
  | INTER SHOPPING OCT 24 | $15,057 | 77,829 | $0.19 | 21 | **0.027%** | $7,792 | **0.52** |
  | GABRIEL CPC MAY 2025 | $5,881 | 7,265 | $0.81 | 34 | 0.47% | $14,823 | **2.52** |
  | **total** | **$54,218** | 113,635 | $0.48 | 163 | 0.14% | **$53,161** | **0.98** |

  **$54,218 spent to recover $53,161**, against PMax's blended 9.25 over twelve months.
  The international campaign is the clearest case: 77,829 clicks at $0.19 and twenty-one
  conversions &mdash; cheap clicks that are not buyers.
- **So the 264 go into a dedicated PMax, and the coordinator's own argument against
  that was wrong.** The objection recorded earlier was *&quot;a second PMax asks the
  same algorithm the same question&quot;*. **It is not the same question.** The
  incumbent campaign was asked *&quot;where do I spend $100k across 16,031
  products?&quot;* and with 16,000 better-signal alternatives it never reached these
  264 &mdash; which is precisely why they show zero spend in twelve months. A campaign
  filtered to those 264 and nothing else asks *&quot;spend this budget here&quot;*, and
  **with no alternative inventory the algorithm has nowhere else to go.** That is the
  mechanism the `custom_label_0` asset group exists to create.
  Still required: **exclude the same 264 from the incumbent PMax** by listing group, so
  the measurement stays clean if it ever does start bidding on them. And the
  **$500/day the owner chose is defensible for PMax** in a way it would not be for
  Shopping &mdash; PMax needs conversion volume to leave learning, and starving the
  budget is its own failure mode. Two to three weeks with no tROAS, then set one.
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
- **A stale figure can be proved stale by the PREVIOUS revision, which is a third
  signal rather than a coin flip.** Eaton `TD450158EN` (May 2025) prose says the Eluxa
  speaker has a &quot;listed sound output of up to **87 dB** at 10 feet&quot; while its
  own Table 2 runs to **90 dBA**. 87 dBA is *exactly* the maximum of the September 2021
  revision, whose taps stopped at 2 W where the 2025 taps run to 8 W. So this is not
  prefer-the-table-by-rule: the prose is a **carry-over from the superseded revision**,
  and knowing that is what settles it. **When a document contradicts itself, pull the
  previous revision &mdash; the stale side often matches it exactly.**
  The same sheet has a **row-label defect**: the 2025 Table 2 labels its rows
  &quot;(Wall) **ELSPT**&quot; and &quot;(Ceiling) **ELSPTC**&quot;, neither of which is
  a model in the document.
  **CORRECTION, same day, and it is the &quot;a correction can introduce a new error&quot;
  rule firing on this file's own newest entry.** The first version of this note said the
  2021 revision prints the same table with `ELSPK/ELSPKC` and `ELSPST/ELSPSTC` rows
  carrying **identical values**, and called that the licence for quoting a 2025 wall row.
  The next agent was briefed with it, checked, and **it is not true**: the 2021 Table 2
  has **five** tap columns reading 75/79/82/85/87 and separates neither wall from ceiling
  nor 25 from 70.7 VRMS, while the 2025 table runs seven columns and separates both.
  What actually licenses the row is a **third document**: installation sheet
  **`P85967A` (2025)**, whose Table 2A is **explicitly headed for models
  &quot;ELSPK (Speaker), ELSPST (Speaker-Strobe), ELSPST-A (Amber)&quot;** and reproduces
  the 2025 wall values cell for cell. The 2021 revision corroborates only the weaker
  claim &mdash; that speaker and speaker strobe carry identical numbers as separate rows.
  **So the instruction sheet is model-attributed where the datasheet is not**, which is
  the conditional-headline rule pointing across documents for the third time.
  The speaker-equals-speaker-strobe result still stands and is still the **opposite** of
  the System Sensor `SPWL`/`SPSWL` case, where the two differ by 2 dBA at every tap. Two
  brands, opposite behaviour, neither assumable. **And the System Sensor figures have a
  generation boundary this file did not state:** 77/80/83/86 is the **xenon** `SPSWL`;
  `AVDS-62174:A` gives the **LED** line 76/79/82/83 for speaker strobes against
  79/82/85/88 for speakers, a 3 dBA gap. Do not reuse the xenon row on an LED part.
  Also recorded: the filename this file carried for that document is dead, the live one
  is `eaton-eluxa-speaker-and-speaker-strobe-clear-and-amber-lens-td450158en-us.pdf`
  under `/lsmns/eluxa/`, and **`web.eaton.com` returns HTTP 200 with 86,227 bytes of
  `text/html`** for the old name &mdash; another host that pymupdf opens happily and only
  the mime check catches.
- **Bosch is a blocked brand with a 128-byte fingerprint, and the sitemap route does not
  reach it.** `resources.boschsecurity.com` and the Azure CDN are **refused at the proxy
  gateway with 502 to CONNECT**; `resource.boschsecurity.com` (singular) 301s every
  `/documents/` path to the site root; and `cdn.commerce.boschsecurity.com`,
  `cdn2.commerce...`, `commerce...` and `catalog.boschbuildingtechnologies.com` all answer
  **HTTP 200 with a 128-byte `text/html` body** for every path, including URLs taken
  straight from search results. **128 bytes joins EDAM's 8,047, steelfire's 48,687,
  autocall's 103 and lenel's 371 on the fingerprint list.** The robots/sitemap route this
  file recommends *does* resolve (`catalog.boschbuildingtechnologies.com/sitemap-products.xml`,
  10.7 MB) but carries only the &quot;lifesafetysystems&quot; storefront with **no US fire
  products at all** &mdash; so that route has a boundary, and this brand is outside it.
  `D296` was written from two Bosch-authored documents reached through mirrors three
  years apart, agreeing exactly on every figure quoted.
- **A carton-contents change between revisions is a real product change, and the older
  document is the trap.** Bosch's 2014 `D296` manual says a **D306** remote indicator
  plate ships with each detector and that the **D308 test kit is not supplied**; the 2017
  data sheet's Parts Included list gives a **D344-RL** plate **and** the D308 kit, and
  never mentions the D306. Anyone reading only the manual would tell a buyer to order a
  test kit they already have. **Prefer the newer revision for carton contents
  specifically** &mdash; it is the field most likely to change without any spec changing.
- **The type field's silence has an inverse case worth naming.** `ELFHNW-N` is typed
  **Horn Strobes** and has **no strobe** &mdash; `TD450159EN` Table 5 lists it under
  Sounders with an empty Strobe Candela column and draws its current from the
  &quot;Horn Only&quot; table. But the **title was already correct**, so the type agreed
  with nothing and still raised nothing; the mismatch surfaced only from the ordering
  table. The recorded rule is &quot;the type field is a signal when it disagrees with the
  title and no evidence when it agrees&quot;; this is the case where it disagrees with a
  *correct* title, which is the same defect pointing the other way. **Check the type
  against the document, not against the title.**
- **Det-Tronics is first-party and unprotected, which breaks the relationship-sold
  premise for a fourth category.** `det-tronics.com/wp-content/uploads/sites/8/2025/04/`
  serves current documents directly; the older `det-tronics.com/content/documents/` path
  now 404s. Its model matrix decodes a SKU completely, the Edwards-page-5 class of
  decoder: `UD10S5N28W2C` = **S** 316 stainless, **5N** five 3/4 in. NPT ports, **28**
  EQP/DCU emulator, **W** FM/CSA/ATEX/CE/IECEx, **2** Ex d flameproof, **C** CGS board.
  After Fiplex, Westell and STI that is four categories where &quot;nobody searches for
  it&quot; was mistaken for &quot;nobody documents it&quot;.
  Two flags from it: `010254-008` is typed **Annunciators** and is a $4,294 Ex d gas
  display/controller &mdash; the CPU2-3030D signature, where the type names a role rather
  than the product &mdash; and its title was the **raw ERP string &quot;DISPLAY,
  DCU&quot;** with no class noun. **Worth a sweep for other Det-Tronics SKUs carrying raw
  ERP descriptions as titles.** Also a bounded negative recorded rather than acted on:
  the string `010254` appears in neither `95-8656` nor `90-1209`, so the
  `010254-008` &harr; `UD10S5N28W2C` pairing rests on resellers &mdash; but the ordering
  code decodes correctly against the manufacturer's own matrix, which is what the copy
  rests on, so **neither number was touched**.
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
- **The pack-count boundary is a fact about HONEYWELL, not about manufacturers, and
  Xtralis proves it by stating carton quantities routinely.** `PIP-018`'s title asserts
  **PK10**, and unlike every Honeywell `-BP` case that claim is **manufacturer-stated**:
  Xtralis's own *VESDA Pipes and Fittings &mdash; Europe* catalogue (`xtralis.com/file/495`,
  p. 11) lists **&quot;PIP-018 &mdash; 25mm Air Sampling Test Point, Pack of 10, Red&quot;**,
  and `PIP-007`, `PIP-004`, `144-013`, `222-059` and many others carry &quot;Pack of
  10&quot; in the same catalogue. **This is the first documented pack count in the project
  outside Honeywell bases, LF sounders and batteries.**
  The correction that matters is to how the rule was phrased. This file worked toward
  &quot;bases, low-frequency sounders and batteries, and nothing else&quot; as though it
  were a fact about how *manufacturers* document. It is a fact about **Honeywell**. A
  different vendor states carton quantities as a matter of course, so **the convention
  question has to be asked per brand**, and a Honeywell-derived negative says nothing
  about Xtralis, STI, Potter or anyone else. That is the same over-reach as the battery
  correction &mdash; evidence covering two categories, conclusion covering all of them
  &mdash; one level further out, at the vendor boundary instead of the category boundary.
  Two more results on that part, both from deliberately checking rather than assuming:
  it is **VESDA, not OSID** (it sits in Xtralis's own VESDA pipe range, so the vendor
  field is right and this is not the `OSE-HPW` case), and although it appears **inside an
  End-of-Life bulletin** it is there as the **surviving alternative** to a discontinued
  PVC adapter, not as a discontinued product. A part named in an EOL bulletin is not
  thereby end-of-life &mdash; read which side of the table it is on.
  **The title's PK10 was left exactly as it was** and went to the owner's file anyway,
  because a pack count in a title is a feed attribute and the decision is the owner's
  even when the documentation supports it. Route recorded: `xtralis.com/file/<id>` serves
  PDFs directly with no bot protection, and **the metric 25 mm range is in the Europe
  edition only** &mdash; the Americas sheet (`file/623`) does not list `PIP-018` at all,
  which is worth knowing before writing off any other `PIP-*` part as undocumented.
- **A private-mode appliance sold as an ordinary one: the class error at the listing
  level rather than the noun level.** `SPSWLED-ALERT` is titled and typed as a speaker
  strobe, and it is one &mdash; but `I56-0024-000` (4/15/2024) &sect;1.4 says in the
  manufacturer's own words that the **amber lens ALERT** models are *&quot;**private
  mode** notification appliances intended to alert **trained personnel**&quot;*, with the
  speaker listed to ANSI/UL 1480 (public mode) and the strobe to **ANSI/UL 1638 (private
  mode)**, where the clear-lens models in the same manual are public mode throughout.
  Nothing in the title is false, so this is not one of the fourteen product-class errors;
  it is a **materially different purchase hiding behind a correct class noun**. Per house
  rules it went in the body and not the title, and to the owner as a possible Merchant
  Center category question.
  Consequence for the copy, worth stating because it is easy to get wrong in the other
  direction: the candela values were published as **switch settings** rather than as a
  rated output, because UL 1638 private mode is not the UL 1971 basis on which a
  clear-lens candela is rated, and neither current document states UL 1971 for any model.
- **The coordinator typed product ids from memory into a live query, one batch after
  writing the rule against it.** Building v2b22, the slice file was already on disk with
  every id in it, and the ids that went into the Shopify query were **invented** &mdash;
  seven of eight returned `null` and the eighth returned a completely unrelated product
  (`G1TW`, a trim ring). Nothing was written, because it was a read.
  **The near-miss is the point.** Had that been a publish rather than a query, one real
  product would have received another product's copy, silently, exactly as in the v2b03
  briefing incident. The existing rule says *never hand-transcribe an id into a
  briefing*; this shows the rule is too narrow. **Never type an id anywhere &mdash;
  briefing, query, mutation or note. Read it from the file, every time, even when the
  file is open and the id feels familiar.** The cost of reading it is one command.
- **A proposed scan died on its own worked example, before it was built. Worth keeping
  because the reasoning failed in the way this file warns about, one paragraph after
  citing that warning.** The coordinator saw that `A050-9101`'s page described a
  &quot;**2050FS**&quot; panel and never named `A050-9101`, called it a third instance of
  the wrong-product shape after `4-NET-SM` and `PAD200-DD`, and proposed a catalogue-wide
  scan for **descriptions whose body never contains their own SKU**.
  **`A050-9101` IS the 2050FS.** Autocall `AC4098-0060` Rev. 4, 05/2025, Table 1, read
  directly by the coordinator after the agent contradicted the briefing: *&quot;A050-9101
  | Red | 2050FS FACU with 4 x 40 LCD display, single MX addressable initiating loop with
  50 devices maximum and 2 conventional NAC circuits | 175 mA | 215 mA&quot;*. The
  catalogue number appears **once** in its own datasheet and `2050FS` appears **23
  times**, because the ordering number and the marketing model name are different strings
  and the datasheet is written around the latter. The live copy was substantively right.
  **So the scan is a shape, not a mechanism, and would have over-fired exactly as every
  keyword scan on this catalogue has.** &quot;The body does not contain the SKU&quot;
  fires on every page correctly written around a model name &mdash; which is most panel,
  appliance and series pages in the store. Sharpening it to &quot;the body names a
  *different* model number&quot; does not save it either: this page names 2050FS and is
  correct. What separates `4-NET-SM` from `A050-9101` is whether the named thing **is the
  same product**, and no scan can know that. **Do not build it.**
  The two real cases stand on their own and were both found by an agent reading the page
  against the ordering table, which is the method this file already records as the one
  that works for cross-references.
- **EDAM has a SECOND datasheets root, and a document declared gone may simply be in the
  other tree.** The System Sensor 5600 series is not under the known
  `content/dam/hon/hbt-fire/en-us/products/literature-and-specs/datasheets/` &mdash;
  `5600.pdf`, `5624.pdf` and `A05-1004.pdf` all return the 8,047-byte fingerprint there.
  It lives under **`content/dam/honeywell-edam/hbt/en-us/documents/literature-and-specs/datasheets/`**
  as `5600-Series_DataSheet_SPDS3001.pdf`. **Try the second root before concluding a
  Honeywell document has been dropped** &mdash; this file already records `DN-7045` as
  &quot;dropped entirely&quot;, and that conclusion was reached without it.
  (`SPDS300.pdf` in the same directory is byte-for-byte the same text as `SPDS3001.pdf`:
  two filenames, one document, not two revisions.)
- **The Kidde literature API's category names are enumerable, which removes its one silent
  failure.** A wrong `categoryName` returns the top-level nav in `Markup` with `Content`
  **empty** rather than an error, so a bare category looks identical to a typo. The fix:
  any request returns that nav, and `re.findall(r'>([^<>]+)</a>', Markup)` yields the 20
  real names. Note SuperDuct sits under &quot;Intelligent Initiating Devices&quot; and
  &quot;Conventional Initiating Devices&quot; &mdash; **not** under any name containing
  &quot;Duct&quot;. Also: `myeddie.edwardsfiresafety.com/**PrivateMedia**/Catalog Sheets/`
  serves real PDFs too, so `/PublicMedia/` is not the only live path and only `/Media/` is
  poisoned.
- **&quot;Check the other regional edition&quot; runs in both directions.** Last batch
  `PIP-018` was documented in the Xtralis **Europe** catalogue and absent from the
  Americas sheet; this batch `E700-SP-DCL-PNT` is in the **Americas** sheet
  (`xtralis.com/file/623`, Doc. 17748_12, June 2024) and absent from Europe. Neither
  edition is the superset, so a miss in one is not a negative until the other is checked.
  And a second **positive** pack count from that source: *&quot;50 per roll&quot;* is
  manufacturer-stated verbatim for `E700-SP-DCL-PNT` &mdash; it is **not** currently in
  the title, so unlike the Honeywell cases this is a claim the owner could now add rather
  than one resting on convention. The colour &quot;White&quot; in the live body has no
  basis: the only stated label colours are red and grey, and the &quot;ABS white
  colour&quot; phrase in the EOL notice attaches to the sampling point, not the label.
- **A spec that belongs to the parent, not the accessory, and differs by parent family.**
  Duct air velocity is a property of the **detector**, not of the sampling tube: 100 to
  4,000 ft/min for SuperDuct and Optica but **300 to 4,000 ft/min for the KI-SDH
  housing**. A tube page serves several families, so one velocity figure on it would be
  wrong for one of them. This inverts the recorded rule that *accessory specs often live
  in the parent's data sheet* &mdash; they do, and that is exactly why they may not be
  the accessory's specs at all. Check whether the figure varies across the parents the
  accessory fits before carrying it over.
- **A cross-BRAND adjacent-row trap: a live page asserted a candela value its
  manufacturer does not make.** `ELSTWC-ALA` claimed **15/30/75/95/150/177 cd**. Eaton's
  ceiling set is 15/30/75/**110**/150/177, consistent in five places in `TD450157EN`.
  **95 cd is not an Eluxa setting at all, wall or ceiling &mdash; it is a System Sensor
  L-Series ceiling setting.** Every previous instance of this trap in this file is a row
  copied from a *sibling* or an *adjacent row in the same table*; this one crossed a
  vendor boundary, which no amount of reading Eaton documents would have caught. It was
  found by checking the one number that looked out of pattern.
  **A precision worth keeping about where such errors live.** Both this and the bogus
  &quot;S3000&quot; on `4-24L24S` sat in the description `<h2>`, **not** in the Shopify
  `title` field, which was clean in both cases. Titles are Merchant Center feed
  attributes and descriptions are not, so an error in the body costs one channel and an
  error in the title costs two. **Say which field a defect is in before sizing it** &mdash;
  the coordinator briefed both as title defects and both were not.
- **Amber lens is a listing class, not a colour option, and it is now proven on two
  brands.** Note 5 of Eaton ceiling installation sheet `P85756F`, word for word in the
  wall sheet `P85750D`: *&quot;Amber strobes are not to be used as a Visual Public Mode
  alarm notification appliance.&quot;* Last batch System Sensor documented its amber
  ALERT models as **private mode**, UL 1638 rather than UL 1971. Two manufacturers, same
  idea, so treat an amber lens as a class question every time.
  **Three things about how that one was handled are the reusable part.** (1) The note is
  item 5 of a **sheet-level `NOTES:` list**, not a footnote on a table row &mdash;
  confirmed by render &mdash; so it is a class statement; but the class it names is
  &quot;amber strobes&quot;, and `TD450157EN` Table 4 assigns **Strobe Color: Amber** to
  this part by name. That is what distinguishes it from the `SD365T-IV` series-block trap,
  where the family statement named no property that could be assigned to the member.
  (2) **The complement is not documented.** &quot;Private&quot; appears **zero times** in
  all three Eaton documents. The agent's first draft wrote *&quot;so this is private mode
  signalling&quot;* and, challenged, traced it to a **web-search snippet about the ELSA
  speaker-strobe line** &mdash; a different product family. Wrong document family for the
  eighth time, and the first caused by an agent inside its own copy. The published
  sentence now states the prohibition and adds that neither document says what amber may
  be used for instead. (3) **The sheet grants the amber model the same UL 1638/1971/ULC
  listing line as the clear one and then forbids the public-mode use**, which is odd and
  unresolved; the copy reports the listing as a family line and the prohibition as the
  part-level fact.
  **The general rule this sharpens: when a restriction is found, look for its complement
  before writing the sentence.** A prohibition without a permitted use is hard to phrase
  without inventing one.
- **The coordinator compressed a nuanced agent finding into a flat rule, and the flat
  rule was wrong for the very next instance. This is the lossy-slice-file failure moved
  into prose.** A v2b20 agent reported, correctly and completely, that the Simplex
  `2099-` series is the **non-coded manual station line** and that releasing stations are
  **one data sheet inside it**, `S2099-0010`. Writing the next briefing, the coordinator
  compressed that to *&quot;`2099-` is the non-coded manual pull station line, **not** a
  releasing line&quot;* &mdash; dropping the exception. The next `2099-` part to come
  through, `2099-9149`, **is in `S2099-0010`**: *&quot;Non-Coded Manual Stations for
  Releasing Applications&quot;*, Table 1, UL 38 listed for releasing service, and absent
  from `S2099-0007` entirely.
  **So it is a product-class error in a feed title** &mdash; a release station sold as a
  pull station &mdash; and the `type` field said **Pull Stations** and agreed with the
  wrong title, raising nothing. That is the recurring signature again.
  **And it is the incomplete-product trap for the eighth time:** the sheet says *&quot;a
  blank area on the front of the station allows the selection of a label&hellip; (label
  kit is ordered separately)&quot;* and Table 1 notes **&quot;requires label kit
  4099-9802&quot;** &mdash; six labels covering clean agent, extinguishing, CO&#8322;, foam,
  sprinkler and manual. At $38 the buyer receives an unmarked releasing station. This is
  the `4099-9015` case almost exactly, one series over.
  A third thing the compression would have cost: the coordinator asked the agent to diff
  against `2099-9803`, the replacement **breakglass** published the day before. Wrong
  accessory &mdash; `2099-9149` is a **break-rod** station and takes `2099-9804`. Acting
  on the briefing would have cross-sold the wrong part.
  **The rule: when an agent's finding carries an exception, carry the exception.** A
  summary that drops the &quot;except&quot; is not a shorter version of the finding, it is
  a different and false one &mdash; and it is harder to catch than a wrong value, because
  it reads as a clean general rule.
- **Gentex is a third manufacturer that states carton quantities, which further confines
  the pack-count rule to Honeywell.** The S/C/SC/H series sheet prints **&quot;24 units
  per carton, 28 pounds per carton&quot;**. With Xtralis already established as stating
  them routinely, that is two vendors outside Honeywell documenting what Honeywell
  documents only for bases, LF sounders and batteries. **The open pack-count rows in
  `PACKCOUNT_decisao.csv` are a question about Honeywell's documentation habits and must
  not be generalised to any other brand** &mdash; and for a non-Honeywell part, the
  carton quantity is probably findable rather than unsourceable.
- **A summarising fetch can shift a table by one row, and the shift is invisible because
  the output looks tidy.** WebFetch on the Space Age category page returned a clean model
  table giving `SSU00651` **32** termination points. The manufacturer's own `LT10221
  Rev. J` says **64**, as does the product URL slug. The summary had not hallucinated a
  number &mdash; it had **misaligned the rows**, so every value was some other model's.
  This is the SWIFT lifecycle-label lesson one layer over: that one warned against taking
  a *lifecycle claim* from a summarising fetch, and this shows the same tool failing on
  *numeric table data*, where the result reads as authoritative because it is
  well-formatted. **A summarising fetch is not evidence about a table. Download the
  document.**
- **A new extraction shape: a genuine PDF whose text layer is unusable.** Space Age
  install sheet `LT10322` downloads as real `application/pdf`, opens in pymupdf, and
  `get_text()` returns **custom-encoded punctuation soup** &mdash; not navigation chrome,
  just garbage. **This is distinct from the EDAM and systemsensor.com traps, where
  `file -b --mime-type` is the tell.** Here the mime check *passes* and the document is
  still unreadable without a render. So the check separates a fake PDF from a real one and
  says nothing about whether the real one can be read; **if extracted text looks like
  noise rather than prose, render, do not conclude the document is wrong.**
- **On the JCI hub an accessory may appear in NO index entry at all.** `2975-9206` is in
  no filename and no title across the 961-entry Simplex index; grepping `2975` returns
  one unrelated Canadian bells-and-chimes sheet from 11/00 that does not contain the part.
  It was found by grepping the **downloaded text of the parent annunciator data sheets**.
  **So the rule &quot;grep the `filename` field, not the title&quot; has a boundary: it
  works for documents, and an accessory is usually not a document.** For an accessory,
  identify the parent product and grep its PDF text. Two smaller notes from the same work:
  the index `metadata` is a **list of `{key,label,values}` dicts, not a dict**, so
  `.get()` on it raises; and filtering `ft:locale` to `en-US` collapsed one family's hits
  from 11 to 7.
- **`sid.siemens.com/go/` resolves A6V ASSET numbers only, never part numbers.**
  `/go/FC901-U3` 303s to an `unresolved` deeplink. Web-search the A6V number first, then
  call `/go/<A6V>`; that worked first try on two documents. Also confirmed, and worth
  knowing before spending the fetch: `/api/khub/maps` contains the string `FC901`
  **zero times** &mdash; its Cerberus entries are DMS, PACE and PRO Modular only &mdash;
  and `file -b --mime-type` reports **`text/plain`** for that 8.5 MB JSON.
- **The robots-and-sitemap route has now paid on a third brand, and the host was wrong in
  the catalogue.** `www.spaceagelectronics.com` fails at the proxy with
  **`CONNECT tunnel failed, response 502`, zero bytes**, on `/robots.txt` and
  `/sitemap.xml` alike &mdash; a new fingerprint. The real host is **`www.1sae.com`**,
  whose product pages are a Magento JS shell with **zero PDF links in the HTML** and whose
  `robots.txt` is a **1-byte file** &mdash; but `/sitemap.xml` is a live 260 KB index that
  led to the category page and three documents under `/media/assets/product/documents/`.
  After Functional Devices and HyperSpike that is three brands recovered this way.
- **Ninth incomplete-product case, and the priciest yet in proportion: `FC901-U3` is
  panel electronics with nothing to mount them in.** Siemens Data Sheet `9813`'s
  Electronics Package block lists the kit as exactly two items &mdash; `FCM901-U3` main
  board and `FP2011-U1` 170 W supply &mdash; while the Specifications paragraph on the
  same sheet says the FC901 FACP *&quot;consists of a main board, a 170-Watt power supply,
  **and a Model FH901-U3 / R3 system enclosure**&quot;*. Three components; the kit is two
  of them. **At $911.90 the buyer receives no enclosure**, and separately no battery
  bracket (required for seismic certification), no trim kit, no batteries.
  The `type` field said **Boards** and agreed with the raw-ERP title, raising nothing
  &mdash; fifth instance. It is not a board: a buyer filtering for boards gets a two-part
  kit, and a buyer filtering for control panels never sees it. Note the sibling
  `FCM901-U3` genuinely *is* a board, which is presumably how the field was set.
- **The coordinator's scepticism was the error again, for the second time.** A briefing
  flagged the live `TH4210U2002/U` stage claim &mdash; *&quot;up to 2 Heat/1 Cool heat
  pumps; up to 1 Heat/1 Cool conventional&quot;* &mdash; as the kind of claim that is
  usually wrong. **Two independent Resideo documents confirm it**, submittal
  `33-00285----04` and the `03-00306` comparison chart, and the only thing the live copy
  had omitted was the qualifier *with electric aux heat*. That is the `ATD-L3R-IV` shape
  exactly: **&quot;that kind of claim is usually wrong&quot; is a prior, not evidence, and
  it has to lose to a document like any other prior.** Worth stating as a count now: twice
  the coordinator has predicted a live claim was wrong and twice the page was right.
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
- **The Eaton route's intermittency is PER CONNECTION, not per host per day, and the
  evidence is two processes disagreeing within the same hour.** On 22 Sep a v2b23 agent
  pulled `TD450157EN` **first try**, 519,514 bytes, mime-clean, from
  `www.eaton.com/content/dam/eaton/products/safety-security-emergency-communications/lsmns/eluxa/eaton-eluxa-horn-strobe-and-strobe-clear-and-amber-data-sheet-td450157en-us.pdf`
  &mdash; while the coordinator, using **that same URL** in the same hour, got
  `RemoteDisconnected` **50 times in a row** across two files, and `curl` failed to
  connect at all. Same host, same path, same proxy, opposite outcomes.
  **Two consequences.** First, this file's advice to &quot;keep hammering&quot; is right
  but has a limit: 25 attempts per file is enough to establish that *this* process is not
  getting through, and the next move is to have a different one fetch it, not to keep
  going. Second, **distinguish the failure modes before diagnosing** &mdash; the agent
  separately burned 25 attempts on clean **HTTP 404s** from a wrong slug, which is a
  *connected* failure and reads nothing like `RemoteDisconnected`. A 404 means find the
  slug; a disconnect means try another route or another process.
  Also recorded from that success: **the working slug puts the document number lowercase
  and at the end**, so it cannot be built from `TD450157EN`.
  **And one verification is still owed.** The `ELSTWC-ALA` copy published in v2b22 cites
  Note 5 of installation sheet `P85756F`. It rests on one agent reading it, quoting it
  verbatim, confirming its placement on a 170 dpi render, and re-checking the surrounding
  word counts when challenged &mdash; but **the coordinator has not read it directly**, and
  the attempt failed on the route above. The published sentence is deliberately weaker
  than the finding (it states the prohibition and that no document states the complement),
  so the exposure is small. **Re-check `P85756F` when the Eaton route next answers.**
- **Fourteenth product-class error, and the first where a listing code explained an
  apparent nonsense in the title.** `49AV-WWFO-BA` asserts **15/75/WP75/WP185 cd**, which
  reads as a broken candela ladder with 75 appearing twice. It is not: **15 and 75 cd are
  the UL 1971 settings and WP75 and WP185 are the UL 1638 settings**, two listings on one
  appliance with **different temperature ranges** (32 to 120 &deg;F against &minus;31 to
  150 &deg;F) and different humidity limits. 75 cd appears twice because it is rated twice.
  **Every element of that title checked out.** Generalises: a candela set that looks
  malformed may be two listings concatenated, and the temperature ranges are the tell.
  Two routing corrections came with it. The part is **not** in `S49AV-0001` and **not** in
  the `S4906-0001` family the briefing pointed at; the weatherproof wall models are in
  **`S49WP-0001-5`**, and `S49WP-0002` is the parallel **ULC** document with a *different*
  candela set (20/30/75) &mdash; so mixing the two would attribute a ULC figure to a UL
  model. Wrong document family again, and the `-BA` suffix is confirmed a second time as
  **assembled in the USA**.
- **A live page can be right and the catalogue still wrong, when a suffix is unsourceable.**
  `SIGA-OSD-IN` carried *&quot;Note: Manufactured in India&quot;* in its body. The `-IN`
  suffix appears in **none** of five Edwards documents &mdash; `E85001-1001` Issue 1.5
  (which lists `SIGA-OSD` and `SIGA-OSD-NL` only), installation sheet `3102595-EN`,
  `E85001-1002`, `E85001-1004` or the Signature Factbook `E85000-0371` &mdash; and
  &quot;India&quot; appears zero times in all five. **The suffix was not called invented
  and the SKU was not touched**, which is the `THM04R3000` lesson holding; the country
  claim was removed because it is unsourced and is not a spec; and the page now says
  plainly that no Edwards document read defines `-IN`. One reseller says it means a
  built-in isolator, which is correlated distributor consensus and was neither repeated
  nor contradicted. **Flagged to the owner, because an unsourceable suffix is still a
  Merchant Center title attribute.**
- **A number inside a model number can look like a spec and be denied by the
  manufacturer in the same document. New shape, and the strongest title defect yet.**
  `AS-75-R-WP` was titled *&quot;AS Horn 75CD Red Weatherproof&quot;*. Siemens Data Sheet
  2578 (Rev. 5, Sept 2015), read directly by the coordinator, carries **Note 1 verbatim:
  &quot;Models AS-75-WP and AS-75-R-WP do not provide a 75cd setting.&quot;** Note 2 gives
  the real ratings &mdash; **115 cd per UL 1638 outdoor and 30 cd per UL 1971 indoor**
  &mdash; and the ratings table row agrees (115 | 30/180 | 30).
  **The document contradicts itself and the note wins**: the ordering row does read
  &quot;AS Horn | Strobe: 75CD Weatherproof, Red&quot;, which is the shorthand the store
  title inherited, while the note on the same page denies it and the ratings table
  corroborates the note. Two signals against one piece of shorthand.
  **So the `75` is a series designator, not a candela value**, and the live title was
  asserting a setting that does not exist, in a Merchant Center feed attribute, on a
  product where candela is exactly what a specifier filters by.
  **Fifteenth product-class error came free with it:** the sheet is headed *&quot;AS &amp;
  AH &mdash; **Audible Horn | Strobe** / Audible Horn Appliances&quot;*, so **AS is the
  horn-strobe line and AH is the horn-only line**. The title said Horn and the `type` says
  Horns, agreeing with the wrong title and raising nothing &mdash; the signature again.
  **Generalises: when a title's number matches a fragment of the model number, check
  whether it is a spec at all.** The briefing had already flagged &quot;a horn has no
  candela&quot; as a class question; the answer turned out to be both that *and* a
  phantom figure.
- **Plain extraction can emit two tables in the wrong order, so the CAPTIONS attach to
  the wrong bodies.** On `TD450157EN` page 3, `get_text()` hands back &quot;Table 2.
  Strobe Ratings&quot; joined to the ELHS/ELHNC body and &quot;Table 3. Horn-Strobe,
  Current Ratings&quot; joined to the ELST/ELSTC body &mdash; the two swapped. Word
  coordinates show the ELST table physically **above** the ELHS one, and a 220 dpi render
  settles it. **Anyone trusting plain text would have read strobe currents out of the
  horn-strobe table**, and would have concluded the briefing's warning about that table
  was wrong.
  This is the caption-below-its-table trap (`9021-60930`) one level up: there a caption
  attached to the wrong table *within* reading order, here two whole tables are
  interleaved. Same remedy, same rule &mdash; **never take a caption-to-body assignment
  from reading order alone.**
- **EDAM case and root are independent axes, and the underscore rule is per-document.**
  Measured this batch: `DF_52004.pdf` (underscore) resolves while `DF-52004.pdf` and
  `df-52004.pdf` both return the 8,047-byte fingerprint under **both** roots; meanwhile
  `AVDS870-03.pdf` resolves **bare and correctly cased under the `honeywell-edam` root
  only**, with the `hon/hbt-fire` root, the lowercased form and the underscore form all
  failing for that same document. So the shapes do not compose into a rule &mdash; try
  bare, lowercased and underscore **against each root separately**, and accept that it is
  per-document.
- **A wrong dBA figure in a live title, verified by the coordinator, and the document
  never contained the wrong number at all.** `GB6-24` was titled *&quot;85 Dba at 10
  Feet&quot;*. Gentex `551-0042-04`, fetched and read directly: the model table row reads
  `GB6-24 | 904-1278-002 | 24 VDC | 6&quot; | 100 mA | **95 dBA**`, and the A&amp;E
  paragraph independently specifies *&quot;peak sound output of **95 dBA** or
  greater&quot;*. **`85 dBA` occurs zero times in the document.** Not a
  prose-against-table conflict and not an extraction artefact &mdash; the figure was
  simply never there, which is the cheapest kind of defect to confirm and the easiest to
  miss, because 85 dBA is the plausible number a reader expects on a notification
  appliance.
  Two things came with it. **Gentex path construction worked first try here**
  (`fireprotection.gentex.com/files/GB-Series1.pdf`, 538 KB, mime-clean) where it failed
  for the S-Series &mdash; so that route is family-by-family, not broken. And **Gentex
  states a carton quantity for a notification appliance** &mdash; *&quot;20 units per
  carton&quot;* on the datasheet face &mdash; which is the category Honeywell declines to
  state. Third vendor outside Honeywell doing so.
- **The page-chrome lifecycle trap has now fired three times, on three pages, and the
  mime check caught the hosts.** `SRK`'s live copy said &quot;(Discontinued)&quot;. Both
  `buildings.honeywell.com` and `systemsensor.com` return **`application/javascript`**
  shells (225 KB and 112 KB), and the only occurrences of the word are the JS UI label
  `&quot;discontinuedText&quot;:&quot;Discontinued&quot;` and a nav entry &mdash; attached
  to nothing, as in the two earlier cases. **Positive evidence pointed the other way:**
  the 23 Feb 2022 outdoor brochure lists SRK, SRK-R and SRK-P as current wall-mount
  strobes. Nothing published; flagged as a lifecycle/feed decision.
  **And the `K` suffix IS decoded here**, unlike `PC2WKLED-P` where no document defined
  it: the same brochure states *&quot;model numbers with a 'K' suffix are outdoor-rated
  products listed to **UL 1638** and rated from &minus;40 &deg;F to 151 &deg;F, with a
  NEMA 4X or 3R rating&quot;*. So the convention is real and documented on System Sensor;
  it simply was not stated in the document family the other part sat in. **A bounded
  negative in one document family says nothing about the convention.**
- **A merged cell that changes whether a device may be installed at all.** `A05-0456`'s
  Candela Derating table merges *&quot;Do not use below 32 &deg;F&quot;* across the
  **15, 15/75 and 30 cd** rows &mdash; confirmed by word coordinates at y=618.9 and a
  300 dpi render. `SRK` is a standard-candela device, so it falls inside that cell. **A
  designer laying out on 15 cd in an unheated space would be specifying a device the
  manufacturer says must not be used there**, and no plain-text read of that table would
  show it. Published for exactly that reason. (75 derates to 44 cd and 95 to 70 cd at
  &minus;40 &deg;F; 110 and 115 unchanged.)
- **`trilogyrf.com` is the same Sucuri block as `trilogycoax.com`, so the whole brand is
  walled.** HTTP 202, **221 bytes**, `/.well-known/sgcaptcha/` meta-refresh, on every
  path; the `urllib`-plus-Safari-UA workaround returns the same 221-byte block, confirming
  it does not defeat Sucuri. `trilogycoax.com` still 202s at 190 bytes.
  `trilogycomms.com` 301s to a different company entirely. **Wayback is no help this week
  &mdash; `archive.org` is returning a site-wide &quot;temporarily offline&quot; page to
  both the availability API and CDX.**
  The page was still written, from Trilogy's own AirCell product specification served
  intact by a mirror, **read entirely off a 260 dpi render because its text layer is
  scrambled** &mdash; the genuine-PDF-unusable-text-layer shape for the second time.
  **What could not be sourced was the ordering unit.** The title's *&quot;1 ft (0.304m),
  Reel&quot;* is Honeywell catalogue-feed wording repeated verbatim by every distributor:
  correlated repetition, not evidence. Dropped from the title and flagged &mdash; a price
  list or a purchase order settles it, not another search.
- **An import truncated titles at 150 characters, and the cliff in the histogram proves
  it. Second mechanism-based scan on this catalogue that did not over-fire, and the
  cleanest yet.** Run 22 Sep 2026 against a live pull while agents were working.
  **The mechanism: a title with unbalanced parentheses cannot be correct.** Not a shape,
  not a keyword &mdash; there is no legitimate title that opens a bracket and never closes
  it. **102 of 16,031 titles qualify, and inspecting all 102 found no false positive**,
  against 1&ndash;8% precision for every keyword scan in this file and 67% for the
  family-disagreement scan. **Precision only &mdash; its recall was measured seven
  batches later and is about 25&ndash;30%; see the re-measurement in the batch-25 sweep.**
  They split into two different defects:
  - **79 with an unclosed `(`** &mdash; cut off mid-phrase: *&quot;&hellip;Temporal 4
    Capabilities Plain (no&quot;*, *&quot;&hellip;(Availability Limited to Quantity&quot;*,
    *&quot;&hellip;(Notifier Marketing PN:&quot;*.
  - **23 with a stray `)`** &mdash; a different mechanism, where the opener and part of its
    content were lost: `Potter PE-LFHNW 4871013) Low Frequency Sounder`,
    `Resideo 900748 BP10) Seal Ring`, `Simplex 4098-9784 discountinued)true Alarm Base`.
  **The proof of the cause is the length histogram, not the sample.** Across the newest
  product-id blocks, title lengths climb to a plateau at 145&ndash;149 characters
  (107, 97, 88, 88, 76) and then go to **17 at exactly 150 and ZERO at 151 and above**.
  A natural distribution does not end in a cliff. **Titles in the new blocks land at
  145&ndash;150 at 5.51%, against 0.51% in the older blocks** &mdash; an 11x difference,
  and every one of the 79 broken titles sits in a new block, none in an old one. This is
  the same shape as the Aiphone non-ASCII finding: **the defect clusters in one import,
  so it is fixable at the source rather than one product at a time.**
  **The 79 are the detectable tail, not the whole problem.** Roughly **456 new-block
  titles sit in the truncation band**; the 79 are merely the ones whose cut happened to
  fall inside a bracket. The rest were cut too and end at a word boundary, so they look
  fine and are invisible to any scan.
  **Not fixed, and deliberately so.** The truncated text is *missing*, so reconstructing
  79 endings would be inventing them &mdash; the one thing this project never does. This
  is a data question for the owner: re-import the affected block with the full titles.
  Ids saved in `/tmp/tfas/TITULOS_TRUNCADOS_ids.json`. Titles are Merchant Center feed
  attributes, so a title ending mid-word costs money in two channels.
  **Two mechanism flaws found and fixed while building this scan, worth keeping because
  they are the general failure mode of such rules.** A first pass flagged
  &quot;comma with no following space&quot; as an ERP field separator &mdash; it fires on
  every **thousands separator** (`1,000'`, `4,064 Points`, `3,000 Hz`), including a title
  written the same day. And it flagged `EA` as an ERP abbreviation &mdash; it fires inside
  **model numbers** (`IX-EA`, `ATJ-EA`, `GWBDA-EA-AU-MDA`). Both fixes were mechanisms,
  not thresholds: require a non-digit after the comma, and require the token not be inside
  a hyphenated run.
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
- **Coloured lens is a listing class on a THIRD brand, and it is not just amber.** Gentex
  lists the GE3 Colored Lens Series to **ANSI/UL 1638 and ANSI/UL 464, CAN/ULC S525/S526,
  and explicitly NOT UL 1971**, with the note that *&quot;ANSI/UL 1971 is not applicable to
  emergency communications devices, but readings were obtained using the measurement
  procedure specified under ANSI/UL 1971.&quot;* So the candela are rated output with no
  derating, but **the appliance is an emergency-communications device, not a fire
  strobe** &mdash; Gentex names severe weather and emergency response as the applications.
  After Eaton (amber forbidden as a public-mode fire appliance) and System Sensor (amber
  ALERT is private mode, UL 1638), that is **three brands and the finding now extends
  from amber to blue, green and red**. Treat any non-clear lens as a listing question.
- **The E/K carton split is confirmed on a second document number, so it is a rule and
  not a one-off.** `E85001-1021` Issue 1.2 marks the GP10 wiring plate *&quot;required,
  ordered separately&quot;* while `K85001-1021` Issue 1 marks it *&quot;required, INCLUDED
  WITH DEVICE&quot;* &mdash; same two places in the document, same hardware on every
  figure (candela set, 20 &#937; sync, 6.8 &times; 1.82 in., UL files S218/S5389).
  Identical to the `85001-0667` finding on a different number. **A prefix swap means the
  same hardware and not necessarily the same carton**, and Edwards again carries `-FR`
  and `-SP` variants Kidde drops.
  Route note worth keeping: **Kidde uses the Edwards slug form**, so the Kidde URL builds
  from the Edwards LifeLines filename with the `E` swapped for `K` &mdash;
  `kidde-esfire.com/Content/Documents/K85001-1021%20--%20Genesis%20LED%20GC%20Series...pdf`
  resolves where the bare `K85001-1021.pdf` 404s at 1,245 bytes.
- **`NCM-F` is MULTIMODE, and there is no single-mode NCM at all.** `DN-6861:D` (3/5/19):
  62.5/125 or 50/125 &micro;m multimode, **ST connectors**, 820 nm, 8 dB budget on 62.5 and
  4.2 dB on 50. That is the **opposite** of `FSL-E3` (single-mode, 9/125, LC), so the
  fibre-mode field cannot be guessed from the brand or the letter.
  **And the 3,000 ft figure on that same data sheet belongs to the NCM-W twisted-pair
  board** &mdash; the adjacent-row trap, avoided. `DN-6861` publishes an optical loss
  budget and no distance for the fibre part, so no distance was published.
  The live page also said the NCM-F *&quot;connects FACPs to Network Control
  Annunciators&quot;*. It does not: the NCM is **each node's own interface to a peer
  network**, and panels and NCA annunciators alike carry one.
- **A scan suggested by an agent, run, and mostly negative &mdash; recorded because the
  negative is the useful part.** An agent noticed `GCAVWF-CVR` is a replacement cover and
  asked whether any `-CVR` SKU is merchandised as a device. **Ten `-CVR` titles exist and
  all ten say &quot;Cover&quot;**, so the dangerous form &mdash; a bare cover sold as an
  appliance &mdash; does not occur. Two carry the wrong `type`: `G4AVRF-CVR` is typed
  **Horn Strobes** and `G4VRF-CVR` **Strobes**, where the other eight are typed Covers.
  Titles right, structured field wrong, which is the milder half of the usual signature.
- **Sixteenth product-class error, and it is the releasing-gear shape for the THIRD time
  in six batches.** `RP-2002` was titled *&quot;Fire Alarm Control Panel&quot;*. Notifier's
  own title is **&quot;Agent Release Control Panel&quot;**. That follows `4099-9015` (a
  releasing station sold as an ordinary double-action pull station) and `2099-9149` (a
  manual release station typed Pull Stations). **Releasing equipment is consistently
  merchandised in this catalogue as ordinary fire equipment**, which is now a pattern
  rather than three coincidences, and it is the kind that costs a buyer the most: someone
  specifying a fire alarm panel receives a panel that discharges an agent.
  Everything else on that page verified, six zones included, and the panel **is** complete
  &mdash; but the IBC seismic claim it makes is only realisable with `SEISKIT-COMMENC`,
  *&quot;required for seismic-certified installations&quot;*, which is not supplied.
- **The coordinator offered a cross-family import and the agent refused it. First time
  the wrong-document-family rule has fired PREVENTIVELY.** The briefing offered a System
  Sensor outdoor brochure sentence defining the `K` suffix (*&quot;models with a 'K'
  suffix are outdoor-rated products listed to UL 1638&quot;*) as a possible answer for
  `PC2WKLED`, whose own L-Series documents do not define it. The agent checked
  `AVDS-62173:A`, `I56-0040-000` and `A05-0456`, found that **none defines the letter**,
  observed that every outdoor-table model carries `K` and no indoor-table model does
  &mdash; *an inference from two ordering tables, not a manufacturer statement* &mdash;
  and **put nothing about the letter in the copy.** Recorded because every previous
  instance of this rule in this file is a post-mortem; this is the first where the import
  was offered and declined before it reached a page. A convention documented on one
  product line is not documented on another.
- **A table can carry the WRONG HEADER INSIDE ITSELF, which defeats caption-matching
  entirely.** `AVDS-62173:A` p2: the left table is captioned *&quot;UL/ULC Maximum
  **Strobe** Current Draw&quot;* above it, while its own blue in-table header reads
  *&quot;UL/ULC Maximum **Horn** Current Draw and Sound Output&quot;* &mdash; on a body
  that is candela against current. So the caption above and the header inside disagree,
  and plain extraction additionally emits three captions in an order that attaches each
  to the wrong body. **Render was the only resolution.** Add it to the ladder: caption
  below its table (`9021-60930`), two tables emitted in swapped order (`TD450157EN`), and
  now a header that contradicts its own caption.
- **&quot;Platinum&quot; is a colour, and a merged cell hid it.** `4007-9102` was a
  three-way question &mdash; finish, feature tier or model designation. `S4007-0001`
  Rev. 22 Table 3 lists `4007-9101` **Red** and `4007-9102` **Platinum** against one
  vertically merged Description cell, confirmed at 250 dpi. Also settled: the panel is a
  **complete enclosed unit** including one `4007-9801` zone/relay card, and the two 12 V
  batteries are not in it.
  By contrast `FCI2016-U1` is a **bare board**: installation instructions `A6V10356958`
  show the FC922 built from **eleven separately located items**, and the box holds none
  of the back box, doors, operating unit, supply, trim kit, battery bracket or batteries.
  **Two Siemens panel-family parts in one batch, opposite answers** &mdash; which is why
  the complete-product question has to be asked per part and never inferred from the
  family.
- **Two more index and path facts.** The JCI Simplex hub has a **`product_code` metadata
  field**, and grepping `filename` alone missed `4100-5451` entirely &mdash; the four
  documents carrying it expose it only there, so grep `filename`, `prodname` **and**
  `product_code`. And on EDAM, **prefix and case are independent axes**:
  `BA-Fire-AVDS-62173-A.pdf` works while `ba-fire-DN-60240.pdf` 404s and
  **`hon-ba-fire-dn-60240.pdf`** serves the PDF. Try the `hon-ba-fire-` prefix lowercased.
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
- **The `-IV` protocol convention is now documented outright on a THIRD brand, in the
  manufacturer's own words.** Notifier `DN-62004:B` (7/15/2019) Ordering block:
  ***&quot;'-IV' suffix indicates support of FlashScan and CLIP.&quot;*** That follows
  Gamewell-FCI (`9020-0620 Rev G`, Velociti-or-CLIP) and Fire-Lite (`DF-61011:C` and
  `DF-61010:C`, LiteSpeed-or-CLIP). **Three brands, five documents, one convention:
  ivory is legacy service stock carrying the dual-protocol build.** The `FPTI-951-IV`
  live title already said &quot;(FlashScan and CLIP)&quot; and was right. Also
  manufacturer-stated on the same sheet, and unusually: the FPTI-951 Series **replaces
  the FAPT-851 Series** &mdash; a sourced supersession, which is rare enough to note.
- **Amber is encoded by POSITION on the Eluxa line, and that is why `-A` does not mean
  amber.** `ELHSR-A` is **AGENT lettering**, confirmed in `TD450157EN` Table 4 by word
  coordinates and a 200 dpi render. On this line amber is a **trailing** A *after* the
  lettering code: `-N` unlettered, `-NA` unlettered amber, `-AL` ALERT, `-ALA` ALERT
  amber. So `ELHSR-A` and `ELHSR-NA` are one character apart and are AGENT-clear against
  unlettered-amber. **A suffix letter means nothing without its position in the syntax.**
  **A new document defect on that sheet, and it is the conditional-headline rule a fourth
  time on this brand.** `TD450157EN` p2 Features prints *&quot;Sound pressure (Anechoic)
  dBA &mdash; Low 78, High 91&quot;*, **pairing a reverberant low with an anechoic high**:
  installation sheet `P85750D` Table 2A, model-attributed and coordinate-verified, gives
  **reverberant 80 H / 78 L per UL 464** and **anechoic 91 H / 86 L per ULC S525**. The
  anechoic low is 86, not 78. Anyone quoting the datasheet bullet publishes a wrong
  number. Also on that sheet, Table 3's second body is labelled **ELHNC**, a ceiling
  *horn*, while carrying ceiling *strobe* candela and currents &mdash; nothing published
  from it.
- **The owed `P85756F` verification is NOT discharged, and saying so is the point.**
  A v2b27 agent reported it as discharged, having read the **wall** sheet `P85750D` and
  found Note 5 verbatim. But the published `ELSTWC-ALA` sentence cites the **ceiling**
  sheet `P85756F`, and this file already recorded that the note appears word for word in
  the wall sheet &mdash; so the agent independently re-confirmed a fact already on record
  rather than the one outstanding. **That is genuine corroboration** (two independent
  readers now on `P85750D`, and &quot;private&quot; still appears zero times in it) and it
  raises confidence, but the document the copy cites remains unread by anyone but its
  original agent. The coordinator's own attempt failed: four constructed
  `eaton.com/.../eluxa/` paths for `P85756F` all returned HTTP 404 &mdash; **find the
  slug, do not build it**, again. Debt stands.
- **A supersession that the manufacturer does state, and a battery-box colour that it
  does not: two claims, opposite handling, same batch.** See the `FPTI-951-IV` and
  `BB-55F` entries above. The pair is worth keeping together because it shows the rule is
  not scepticism &mdash; it is the source. A sourced claim goes in the title; an unsourced
  one goes in the body or nowhere.
- **A Simplex title lost a slash in the same import that truncated the others, and only
  the title.** `4100-5113` read `220240V` while its own description `<h2>` still read
  `220/240V`. **The defect was in the Shopify title field alone**, which is the Merchant
  Center attribute, so it cost the feed channel and not the page. Same shape as
  `3-ZA40A`, whose 150-character title ends mid-sentence at *&quot;Has Built in
  Class&quot;* while the description carries the full text. **When a defect appears in one
  field and not the other, say which** &mdash; it decides whether it costs one channel or
  two.
- **The micro-sign trap: a cousin of the Omega trap, and the first one found.**
  Notifier `DN-2243:B` prints the ISO-X standby current as **&quot;450 A&quot;** &mdash;
  the `&micro;` is dropped in extraction exactly as `&#937;` becomes `W`. 450 amperes on
  an SLC isolator module is absurd, which is the tell, and two independent documents
  settle it: installation sheet `I56-3624-001` prints **450 &micro;A** and `DN-60844:A`
  prints **&quot;450 &micro;A per circuit&quot;**. **So the Omega rule generalises to any
  prefix symbol** &mdash; &micro;, &#937;, &deg; &mdash; and the check is the same one:
  ask whether the bare number is physically possible for that quantity before writing it.
- **A search-engine result is not evidence about the catalogue, and it cost one query to
  prove.** A v2b26 agent flagged what looked like **duplicate product pages** &mdash;
  `/products/bb-55f` alongside `/products/fire-lite-bb-55f-battery-box`, and
  `/products/notifier-dp-disp2` alongside `/products/notifier-dp-disp2-dress-plate`
  &mdash; and correctly told the coordinator to verify live rather than against a
  snapshot. **Both short handles return `null`**: `productByIdentifier` finds neither,
  and a product search returns exactly one active SKU each. The URLs exist only in a
  search index. **That is the snapshot rule with a new artefact in the slot**: a search
  result is a cache of something that may never have been current, and it is one degree
  staler than the snapshot this file already warns about. The agent's handling was right
  &mdash; flag it, do not act on it &mdash; and the check cost one query.
- **`DP-DISP` and `DP-DISP2` are different parts for different panels, and the store
  carries both correctly.** `DN-7111:O`: *&quot;DP-DISP2: Dress panel for top row in
  cabinet with CPU2-640/640E installed&quot;*; `DP-DISP` (no 2) serves a CPU2-3030D top
  row (`DN-7070:S`) and an NCA-2 on a CHS-M3 chassis (`DN-7047:H`), and **`DP-DISP2`
  appears zero times in `DN-7047:H`**. A one-character sibling pair separated by which
  CPU sits in the cabinet, both real. Both also require **two BMP-1 blanks** alongside
  them, which is the useful thing on a sheet-metal page.
- **Tenth incomplete-product case, and the `CM` suffix is the whole warning.**
  `HPFF8CM` ships as a **bare chassis**: Honeywell Power `53499 Rev B4` &sect;1 reads
  *&quot;The HPFF8CM is a chassis-mount model &hellip; These separately sold cabinets are
  also referred to as the large equipment enclosure&quot;*, and `DH-60541:C1` marks the
  enclosure **&quot;Order separately.&quot;** At $819.90 a buyer expecting a boxed supply
  like the plain `HPFF8` receives a chassis with no backbox, no door and no batteries.
  **`CM` = chassis mount and `HPFF` = Honeywell Power FireForce**, both manufacturer-
  stated. The live copy named &quot;SBBD4 or EQBBB4&quot; where Table 2.1 lists **eight**
  cabinets across one-, two-, three- and four-unit sizes &mdash; an arbitrary pair, and
  **Honeywell hyphenates them** (`SBB-D4`, `EQBB-B4`), so the unhyphenated forms in the
  live copy would not match a search either.
- **A ULC suffix can shift every figure in a table, which is the sibling trap across
  listings rather than across parts.** Simplex `S4902-0003` Rev 11: `4902-9716` is
  **80/83/85/88 dBA at 25 VRMS** and **79/82/85/88 at 70.7 VRMS**, while `4902-9716CA`,
  the **ULC** variant, is **77/80/83/86** &mdash; two to three dBA lower at every tap.
  **`CA` is the only suffix on this series; `-BA` appears nowhere in it**, so the
  assembled-in-the-USA reading recorded from `S49AVC-0001` does not transfer here.
  Two further points from the same table. **The merged-cell trap fired as briefed and
  needed the render**: the Model cell holding `4902-9716` and `4902-9717` is merged
  across two Input-voltage rows, so y-coordinates alone assign 25 VRMS to one and 70.7 to
  the other &mdash; wrong, both are dual-voltage and carry both rows, confirmed at
  300 dpi. And **the two voltage rows are not identical**: 25 V is 1 dBA louder at the
  two lower taps and converges at 1 W and 2 W, so **quoting one set of four figures
  quotes one voltage only.**
  Also a document defect published from: Table 3's general-signalling frequency response
  reads **&quot;125 kHz to 12 kHz&quot;**, not a coherent range. Nothing quoted from it.
- **A colour claim with no positive source, handled by naming the sibling instead of
  asserting or denying.** The live `BB-55F` copy said **Red**. Fire-Lite `DF-52220:A1`
  reads *&quot;**BB-55FR**: Same as BB-55F above but painted red&quot;*, and Notifier runs
  the identical convention cross-brand in `DN-7111:O` (*&quot;NFS-LBB &hellip; NFS-LBBR:
  Same as above but red&quot;*) &mdash; so the `R` is the red marker and the plain part is
  something else. **But no document states what the plain part's finish is**, and every
  distributor says red, which is correlated consensus for the fifth time. **Nothing was
  asserted either way**: the closing paragraph names `BB-55FR` and tells the buyer to
  confirm the finish. Note the defect is in the **description**, not the Shopify title,
  so it costs one channel.
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
- **THE `P85756F` DEBT IS DISCHARGED, and the coordinator read it directly.** This file
  has carried an outstanding verification since v2b22: the `ELSTWC-ALA` copy cites Note 5
  of Eaton ceiling installation sheet `P85756F`, and no one but its original agent had
  read that document. **A v2b27 agent found the slug by search** &mdash;
  `eaton.com/content/dam/.../eluxa/eaton-eluxa-installation-instructions-p85756f-elhsc-clear-amber-lens.pdf`
  &mdash; and the coordinator then fetched it independently: **859,067 bytes,
  `application/pdf`, 2 pages.** Item 5 of its sheet-level `NOTES:` block reads verbatim
  ***&quot;Amber strobes are not to be used as a Visual Public Mode alarm notification
  appliance.&quot;*** and **&quot;private&quot; and &quot;Private&quot; each appear zero
  times**, so the published sentence &mdash; which states the prohibition and adds that
  no document states the complement &mdash; stands exactly as written.
  **Note what closed it: a search, not a construction.** The coordinator's four attempts
  to build the path all returned HTTP 404. This is the fifth or sixth time on this project
  that *find the slug, do not build it* has been the difference between a document and a
  dead end.
- **An agent reported a document defect as a &quot;typo&quot;, and it is really two
  separate facts.** `TD450157EN` Table 3's second body is labelled **ELHNC** while
  carrying ceiling *strobe* candela and currents. The agent called the label a typo for
  ELHSC, which is right about the datasheet &mdash; but **`ELHNC` is a real and distinct
  product**, and `P85756F` says so in its own General paragraph: *&quot;The Wheelock Eluxa
  **ELHNC horn**, ELSTC multi-candela strobe, and ELHSC horn/strobe appliances&hellip;&quot;*,
  with **ELHNC also for 12 V operation** and **ELHNC the only one of the three that may be
  wall or ceiling mounted**, and its own **Table 5: ELHNC Horn, Current Ratings**. So the
  datasheet mislabelled an ELHSC row; it did not invent a part. Two things that read as
  one, and worth separating before anyone concludes a catalogue number does not exist.
  **The dB pairing is now confirmed by the coordinator with word coordinates**, on
  `P85756F` Table 2: row (H) reads 80 | 80 | 85 | **91** and row (L) reads 78 | 78 | 79 |
  **86**, across the columns ELHNC@12V and ELHNC/ELHSC@24V for reverberant then anechoic.
  **Reverberant 80 H / 78 L per UL 464; anechoic 91 H / 86 L per ULC-S525.** The
  datasheet's Features bullet *&quot;Sound pressure (Anechoic) dBA &mdash; Low 78, High
  91&quot;* really does pair a reverberant low with an anechoic high.
  **And a supersession sat underneath it that would have poisoned the page.** `P85756E`
  (2022) gives the same model **0.037 / 0.046 / 0.077 / 0.109 / 0.146 / 0.208 A** DC where
  `P85756F` (2025) gives **0.035 / 0.042 / 0.069 / 0.096 / 0.124 / 0.177** &mdash; Eaton
  lowered every DC current in the newer revision. Reading the 2022 install sheet against
  the 2025 datasheet produces a two-document contradiction and the correct response of
  publishing nothing; **only the 2025 install sheet resolves it.** Pull the current
  revision of the *installation* sheet before concluding a datasheet contradicts itself.
- **Coloured lens is a listing class on a FOURTH brand, and Siemens treats amber the
  opposite way to Eaton.** Siemens Data Sheet 2625 states the blue, green and red lens
  strobes are *&quot;solely used for visual **Private Mode** alarm notification&quot;*,
  each with its own candela ladder (blue 15/30/75/95/135/150, green 15/30/60/75/115/125,
  red 10/20/40/50/75/80), while **amber is 15/30/75/95/150/177 and is &quot;certified as
  an Emergency Warning Visual Signal&quot;**. Eaton forbids amber as a public-mode fire
  appliance; Siemens certifies amber for emergency warning and puts blue, green and red
  in private mode. **Same underlying Wheelock hardware** &mdash; the Siemens installation
  sheet is `P85827-001A`, a Wheelock P-number. So after Eaton, System Sensor, Gentex and
  now Siemens: **a non-clear lens is a listing question on every brand, and the answer is
  not the same on every brand.**
  Eaton's own document pair shows it internally too: the coloured-lens ceiling sheet
  `P85756-002F` lists the strobe agency as **UL1638 and ULC526 only**, where the
  clear/amber `P85756F` lists **UL1638, UL1971 and ULC526**.
- **A part number that does not match itself, in a feed attribute, for the second time.**
  The live `ZR-MC-R` title rendered the Siemens catalogue number as **`Part 500636169`**
  with the hyphen stripped, while its own description body had it correctly as
  `(500-636169)`. Siemens prints `500-636169`. That is the `868STRC-AQ` shape in
  miniature &mdash; a part number in a title that cannot match a search for itself &mdash;
  and it is the same punctuation-stripping mechanism as the 185 frequency ranges, showing
  up one product at a time. Corrected in the title.
- **The queued `ZH-MC-W` title defect now has its missing class noun, from a sibling's
  research.** That title is a part number plus an unsourced supersession parenthetical
  with **no class noun at all**. Data Sheet 2584 describes `ZH-MC-W | 500-636162` as
  *&quot;Z Horn: Multi Candela (Wall), White&quot;* and `P84860-001C` Table 1 gives
  `ZH-MC` an **X in the Horn column plus a 15/30/75/110 cd strobe** &mdash; so
  **`ZH-MC-W` is a horn strobe**, and **`ZR` is the strobe-only half of the Z Series while
  `ZH` is the half with a horn**. Siemens' own &quot;Z Horn&quot; wording is itself the
  misleading part, which is the `FSL-E3` situation: keep the manufacturer's name and put
  the class in the body.
- **Eighteenth product-class error, and it is a fire extinguisher sold as the wrong
  AGENT.** Ansul `429022` was titled *&quot;FE13 Cleanguard 13 lb **ABC** Fire
  Extinguisher&quot;*. It is a **clean agent** extinguisher &mdash; Ansul's own class noun
  in `F-96111-17` is *Clean Agent Hand Portable Extinguishers*, the agent is **HFC-236fa**,
  and the UL rating is **2-A:10-B:C**. So the rating genuinely covers A, B and C, which is
  presumably how &quot;ABC&quot; got written &mdash; but **&quot;ABC&quot; in the trade
  means ABC dry chemical**, the corrosive-residue agent that is the exact opposite of what
  a clean-agent buyer is paying $1,750 to avoid. A data room or a switchgear cabinet
  specified for clean agent and given dry chemical is a real mis-sale in both directions.
  **The `type` field said Fire Extinguishers, agreed with the wrong title, and raised
  nothing &mdash; the signature for the sixth time.** Airgas repeats the same
  &quot;ABC&quot; wording, which is correlated distributor copy and not a second source.
  Two more from that sheet. **`FE13` is Ansul's own model designation**, not a mangled
  &quot;FE-36&quot;: the part-number row runs FE02VB / FE05S / FE09 / **FE13** against
  429107 / 442255 / 429021 / **429022**. And **&quot;DuPont FE-36&quot; is not Ansul's
  wording at all** &mdash; `FE-36`, `FE36`, `DuPont` and `Chemours` appear **zero times**
  in both revisions, which Ansul writes as HFC-236fa throughout.
  **The incomplete-product trap fired on the bracket, and only a render found it.** The
  bracket row reads `24610 (Included) | 429146 | 422737 | 30937`, and word coordinates
  plus a 250 dpi render put the **`(Included)` marker in the FE02VB column alone**. The
  FE13's bracket `30937` carries no included marker in either revision, while the live
  copy asserted *&quot;with bracket&quot;*. Claim removed, flagged to the owner &mdash;
  if TFAS assembles the bracket itself that is a stock fact and belongs in the copy said
  that way.
- **A pack count that IS manufacturer-stated, in two independent places, and it further
  confines the Honeywell rule.** `VP-ELB-90`'s live title claims *&quot;Box with 20
  Units&quot;*. Xtralis `Doc. 17748_12` (Part No. 29813, June 2024) ordering block reads
  **`VP-ELB-90 | 90&deg; Elbow - 3/4&quot;, 20 per box`**, and independently the product
  bulletin's discontinued-alternative table gives `P-ELB-90 &quot;QTY 20&quot;` &rarr;
  `VP-ELB-90 &quot;20 PER PK&quot;` &mdash; which is also a **manufacturer-stated
  supersession**, rare enough to note. Second documented pack count outside Honeywell
  after `PIP-018`.
  **But the same block shows why a sourced count cannot be generalised:** within this one
  range the 45&deg; elbow and union are **10**, the coupling and tee **15**, the end cap
  **25**. A pack count is a per-SKU fact even inside one family from one vendor.
  The regional rule fired both ways a third time: `VP-ELB-90` is **Americas-only**, and
  the Europe edition has no `VP-*` parts at all &mdash; its 90&deg; elbow is the 25 mm ABS
  `PIP-017` at ten per pack.
- **Three live defects in one batch that all sit in the DESCRIPTION and not the title,
  and one that sits in the title alone.** `FSL100-IR3-W`'s certification string
  (`Div2EN54-10` is two approvals joined at a lost bullet &mdash; substantively correct,
  just unreadable), `DVP-120M`'s *&quot;120V&quot;* (it is a **90&ndash;250 VAC universal
  input** panel, stated identically in a 2016 manual and a 2025 data sheet), and
  `FN-PS776`'s *&quot;220V&quot;* (Hochiki documents **120 or 240 VAC selected by jumper
  R72** &mdash; fitted is 120, removed is 240, and **there is no 220 V setting**). Against
  those, `429022`'s wrong agent class sits in the **title**. **Saying which field each one
  is in is what sizes it**: three cost the page, one costs the page and the Merchant
  Center feed.
  `FN-PS776`'s *&quot;9th Edition&quot;* was **confirmed** as UL 864 9th Edition rather
  than a product revision, by a replacement-parts table listing `FN-PS4` as 8th Edition
  against `FN-PS402` as 9th &mdash; **one character changes the UL edition on this brand**,
  which is a sibling trap worth keeping.
- **Three more first-party hosts, and a new failure fingerprint.**
  `honeywellanalytics.com/~/media/honeywell-analytics/products/<line>/documents/` serves
  Honeywell gas and flame PDFs directly with no bot protection &mdash; the FSL100 needed
  no EDAM probing at all. `docs.johnsoncontrols.com/specialhazards` reaches **Ansul hand
  portable extinguishers** cleanly (`F-96111` is the CLEANGUARD family sheet). And
  `altronix.com/library/pdf/data_sheets/DS_<MODEL>.pdf` is **fully derivable inside the
  library**, so pulling five siblings to find a separator costs five fetches &mdash; its
  404 is a stable **13,828-byte `text/html`**, confirmed against a control.
  Also: `macurco.com` links a first-party `docs.macurco.com`, a bubble.io app whose
  `/file/<id>` route returns a **~15,548-byte `text/html` JS shell**, while the underlying
  `*.cdn.bubble.io/<fileid>/<name>.pdf` serves real PDFs on **searched** paths.
- **Twelfth coordinator premise wrong, and it breaks a signature this file had been
  treating as reliable.** The `4100-9706` briefing flagged its live sentence &mdash;
  *&quot;Same as 4100-9701 above except with Color ES Touchscreen Display user
  interface&quot;* &mdash; as **copy borrowed from an adjacent catalogue row**, the tell
  recorded three times here (`PAD200-DD`, `4-NET-SM`, `INX-10A`). It is not borrowed.
  **It is Simplex's own Table 8 row for this exact model**, almost word for word, in
  `S4100-1031 Rev. 22`.
  **So the borrowed-copy signature has a false positive, and it is a common one: a
  manufacturer catalogue that itself writes rows as &quot;same as the one above,
  except&quot;.** Every previous instance was a store page carrying a *sibling's* text;
  here the store faithfully carried the *manufacturer's* text about the right part. The
  discriminator is not the phrasing &mdash; it is **whose row it is**, which only the
  ordering table answers. The real defect left is small and different in kind: **the word
  &quot;above&quot; dangles** on a product page where `4100-9701` does not appear.
  Worth pairing with the outcome on the class question: `4100-9706` **is** the 4100ES
  Master Controller, and its `type` of Control Panels is correct &mdash; so this page
  does *not* repeat the `4100-9701` error where the same controller was typed
  &quot;Annunciators&quot;. The premise was wrong twice over.
- **The photo work was sorted by the wrong metric, and the owner's second screenshot
  proved it. 22 Sep 2026.** After the first photo batch the owner sent **the same admin
  screenshot again** and asked whether it had been fixed. It had not, and none of the
  eleven products on it would have been fixed for a very long time. The reason is the
  sort: the photo queue was ranked by `impressions x 30 + revenue / 50`, the same shape
  as the text queue. **7,384 of the 7,900 products without a photograph have ZERO
  impressions**, and every product on the owner's screen was one of them. So **93% of the
  problem was ranked below everything else** and the visible catalogue never moved.
  **Impressions are the right sort for text and a circular one for photographs.** A thin
  page with traffic is one that copy can lift &mdash; that is why the text queue is built
  that way. A photograph is not competing for an organic ranking: it is a Merchant Center
  feed attribute and the thing a buyer sees after they arrive. Ranking it by the traffic
  the page already earns asks the wrong question, and it systematically protects the
  products that look worst.
  **The second error was rate.** Eight products per agent run against 7,900 is roughly a
  thousand agent runs. That was never going to finish, and it should have been obvious
  from the first batch rather than from the owner asking twice.
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
- **The bulk match needs a token-boundary rule, and the test that proved it also caught
  the trap.** A naive substring match of SKU against filename scored 6 hits in 12 on the
  Rath sample &mdash; **and one of the six was wrong**: `8100-V4G` matched a file named
  `16x9-Training-Image-8100-V4G**S**.png`, which is the **successor model**, exactly the
  trap an agent had flagged on that same part a batch earlier. Substring matching
  publishes the successor's photograph onto the predecessor's page.
  **The fix is a mechanism: the SKU must be followed by a non-alphanumeric character or
  end of token.** On a 14-SKU sample it **rejected 32 near-matches** and dropped the hit
  rate from 50% to 36%. It also rejected some legitimate files (`2500-205FM.png` for SKU
  `2500-205`), which is the correct direction to err: **a missing photograph is a
  placeholder, and a wrong photograph is a lie that looks convincing.** Any brand whose
  part numbers carry option suffixes &mdash; batteries, BDA gear, notification appliances
  &mdash; needs this rule, and the naive match must never be used to publish.
- **The photo pipeline's first batch: 5 real photographs of 8, and the verification
  chain is the reusable part.** `foto01`, 22 Sep 2026. Rule applied: manufacturer-hosted
  images only, the source must name the exact part number, and **the coordinator measures
  the file rather than trusting the agent's numbers.** All five re-fetched independently:
  mime and pixel dimensions matched the agent's report exactly, and all five were then
  **looked at**.
  **Four of the five are self-evidencing, which is the strongest form this can take:**
  the Power-Sonic labels read `MODEL PS-1290 F2 / 12 Volt 9.0 Amp. Hr.` and
  `PSL-SC-1270 / 12.8V 7.2AH / 92.16WH` in the photograph, and the RATH unit's front
  panel reads `BOSS CONTROLLER / AREA OF REFUGE`. **A part number printed on the product
  in the picture cannot be a sibling's photo.** The fifth, a plain grey enclosure showing
  nothing, rested on an agent's claim that it is the same photograph the datasheet
  embeds &mdash; so the coordinator **checked it**: the PDF headed `2500-PWR24U` embeds a
  520 &times; 520 JPEG that is the identical pose, latch position, cable gland and
  lighting. Verified, published.
  **Three nulls, each for a stated reason, and accepting them is the point.** A series
  image showing the wrong role and the wrong cabinet size; a correct captioned datasheet
  photo that extracts at **243 &times; 374**, under the 600 px floor; and a brand that
  publishes no photograph at all (line drawings and page furniture only). **`null` is a
  correct answer and it was accepted three times out of eight.**
  **Two mechanical facts for the next batch.** `productCreateMedia` **appends**, so the
  placeholder stays `featuredMedia` until `productReorderMedia` moves the new image to
  position 0 &mdash; without that step the work is invisible. And **the placeholder must
  not be deleted**: the same `MediaImage` id is referenced by 7,738 products, so a
  delete could strip it from all of them. Reorder, never delete.
- **The coordinator fed an agent a placeholder in a field it was asked to reason about,
  and the agent caught it. Third instance of the lossy-slice-file failure.** Building
  `foto01`, `2500-PWR24U` already had good published copy, so its `live_desc` was written
  as the literal string *&quot;[ja enriquecida no v2b25 - copia completa presente. FALTA
  SO A FOTO.]&quot;*. The agent echoed it back verbatim, **flagged it, and told the
  coordinator not to publish that description** &mdash; which is exactly right and is what
  stopped a live page being overwritten with a note to self. The recorded rule was
  *never default a field the agents are asked to reason about*; this adds that **a
  human-readable note is a default too**, and a more dangerous one than a blank, because
  it looks deliberate.
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
- **A vendor's own product page can describe the successor, which makes it the worst
  place to take a photo from.** `avire-global.com/.../8100-v4g/` now describes the
  **8100-V4GS**, a newer model, and every image on it is named `8100-4gvs`. Taking the
  photo from the URL carrying the part number would have published the successor's
  picture. The images used are the dated upload files whose **filenames** carry
  `8100-V4G`. **A URL containing a part number is not evidence that its contents are that
  part** &mdash; the same lesson as the wrong-document-family rule, applied to a web page.
- **CORRECTION: this file's own &quot;bogus `S3000`&quot; note is unsourced and may be
  wrong.** It is recorded above as a defect found on `4-24L24S`. A v2b27 agent reports
  **`S3000` appears on page 1 of Edwards `E85010-0057` as a listing mark**, alongside a
  CSFM file number &mdash; i.e. a UL file number, not an invented string. The coordinator
  could not retrieve that document to settle it (the constructed `myeddie` path returned
  the clean 1,245-byte 404 and the catalogue's audio-amplifier sheets are a different
  family). **Nothing live depends on it**: the `4-24L24S` page was rewritten wholesale and
  the current copy asserts nothing about S3000 either way. But the note stands as written
  in violation of this file's own rule &mdash; *never conclude a part number is invented
  from a negative search result* &mdash; and &quot;bogus&quot; was the coordinator's word,
  not a finding. **Treat S3000 as unresolved, and do not call it invented anywhere on an
  Edwards part.**
- **Half the catalogue has no product photograph, and the first scan for it returned
  zero. 22 Sep 2026, and the owner found it before any scan did.** He sent a screenshot
  of an admin list showing grey placeholder icons and asked for photos. A bulk pull of
  `featuredMedia` and `media` over all 16,031 active products reported **zero products
  with no image** &mdash; true, and useless. **Every product has a media record; three
  of them are TFAS placeholder images shared across the catalogue.** Counting products
  per `MediaImage` id is what finds it:
  `43649142325472` on **7,738** products, `38254642888928` on 127, `41631160795360` on 35.
  **7,900 of 16,031 active products (49%) carry no real photograph** &mdash; 30,608
  six-month impressions and **$1,520,466 of ERP revenue**. Of those, **7,113 also have a
  description under 120 characters** and **1,376 have all three defects at once**
  (placeholder, thin description, bare `Brand PartNumber` title). Top vendors: Kidde
  Fenwal 1,508, Hochiki 798, Rath 708, Amerex 629, Space Age 480. Ranked list in
  `/tmp/tfas/SEM_FOTO_REAL_ranked.json`; the top 200 carry 21,300 of the 30,608
  impressions and $703,245.
  **The method lesson is the sharp one, and it is a new shape for this file.** Every
  previous scan here failed by **over-firing** &mdash; matching a shape and returning
  hundreds of correct products. This one failed by **measuring the wrong property**:
  it asked *is there an image* when the question was *is the image of this product*.
  A presence check cannot see a wrong value, and a placeholder is a wrong value that
  passes every presence check there is. **Before running a scan, say out loud what a
  defective product would look like in the data &mdash; not what a defective product
  looks like on the page.** Here the signature is not a null, it is a **shared id**,
  and nothing about "no photo" suggests looking for duplicates.
  **The working rule for the photo pipeline: a wrong photo is worse than a placeholder.**
  A grey box tells a buyer nothing; the adjacent catalogue row's photo tells them
  something false, looks entirely convincing, and is discoverable only by accident. That
  is the sibling-part failure mode with no textual trace at all, so it gets the strictest
  handling in the project: the image must be served by the manufacturer's own domain, the
  source page or document must name the **exact** part number, the agent must measure the
  real mime type and pixel dimensions of the downloaded file rather than trust the page,
  and **`image_url: null` is an accepted answer**. No reseller, Amazon, eBay or
  image-search asset &mdash; that is a rights rule as well as a correctness one, since a
  manufacturer image on a distributor page is ordinary channel practice and a scraped
  reseller photo is not. Batches live in `/tmp/tfas/foto/fotoNN/`.
- **Verification sweep at batch 25 (1,004 pages, 22 Sep 2026): clean for the fourth
  time running, and the non-ASCII title count is now FALLING.** All 1,004 tracked ids
  present in the active catalogue, **zero missing**. Exactly **four** pages under 400
  visible characters and all four are the deliberate skips (`SM7100-L8`, `90521`,
  `BDA-TP10-L2`, `BDA-NMP01250`). The ASCII title check: **50 of 16,031**, down from 56
  at batches 14 and 19, and **every one is still `&deg;`, `&reg;` or `&trade;`** &mdash;
  25, 23 and 5, zero outside that set. **The drop is the rule working twice over:** six
  of those 56 came through the queue and were rewritten in ASCII, so the count falls as
  the pipeline touches them, and no new one has been introduced across roughly 330
  titles written since batch 14. Cost: one bulk query, 16,031 products, about 40 seconds.
- **The truncation scan re-measured on a second pull, seven batches later, and the
  numbers hold &mdash; but the recall estimate is now measured rather than argued.**
  102 unbalanced-parenthesis titles, unchanged. The 150-character ceiling is confirmed
  catalogue-wide: **749 titles sit at 140&ndash;150, exactly 0 at 151&ndash;155**, and
  the six above 150 are Resideo and Aiphone products from a different import entirely.
  Against a background of ~85&ndash;105 titles per 5-character band from 125 to 139, the
  140&ndash;149 bands hold **238 and 493** &mdash; a 3.6x pile-up against the cap.
  A random sample of 30 from the band, read one by one, found **roughly half clearly cut
  mid-sentence** (*&quot;&hellip;Space for Up to 12Ah Batteries. H:355mm W:436mm&quot;*,
  *&quot;&hellip;Has Built in Class&quot;*, *&quot;&hellip;Replacement Detector Only, Does
  NOT&quot;*). So the real count is **300&ndash;400, and the parenthesis scan's recall is
  about 25&ndash;30% at 100% precision.** Worth stating plainly: **that scan is recorded
  in this file as the cleanest ever run here, and it is &mdash; on precision. Its recall
  was never measured and is poor.** A scan is two numbers, and this project has only ever
  reported one of them.
  **The upstream cause is visible in the same band: 350 of the 749 contain a sentence
  break.** Marketing prose was written into the `title` field, which is why titles reach
  a 150-character cap at all. Fixing the cap without fixing that produces 749 long titles
  instead of 749 truncated ones.
- **Third mechanism-based scan that did not over-fire, and the first one whose defect is
  RECONSTRUCTABLE: 185 titles lost the hyphen inside a frequency range.** Mechanism:
  **a digit run of five or more immediately before `MHz` is not a frequency** &mdash;
  `450512MHz` is 450&ndash;512 MHz with the separator gone, `136174MHz` is
  136&ndash;174 MHz, `758869MHz` is 758&ndash;869 MHz. 185 products, **179 of them
  Fiplex by Honeywell**, plus RFS Technologies, Comprod and Polyphaser: 482 six-month
  impressions and **$317,378 of ERP revenue**.
  **The striking part is the closed set: 185 titles carry only TWELVE distinct broken
  values**, and eleven of the twelve are recognisable US public-safety bands
  (`450512`&times;135, `136174`&times;124, `470512`, `450470`, `758869`, `350600`,
  `470490`, `150175`, `136960`, `5556000`, `1251000`, `460462465467`). So unlike the
  truncated titles, **the text is not missing &mdash; only the separator is** &mdash; and
  twelve substitutions would fix all 185.
  **It still went to the owner unapplied, and the reason is one row.** `136960 MHz`
  disagrees with the Fiplex document this file already names, `BD500-High_Power_Tapper_
  **138**-960MHz`. One of the twelve is not obvious, which is exactly the punctuation-scan
  precedent: *reading `34 NPT` as `3/4 NPT` is a claim about a thread size and needs a
  document.* A split point is a claim about a frequency band and needs the same bar.
  List in `/tmp/tfas/FREQ_hifen_perdido.csv`; the readings are marked unverified on
  purpose.
  **And the first attempt at this scan over-fired 30x, which is worth keeping.** Widening
  it to voltage, current and candela with a 3-digit threshold returned **570 hits, almost
  all correct values** &mdash; `120 VAC`, `177 cd`, `185 cd` are real. The threshold was
  domain knowledge pretending to be a mechanism. Only the frequency case is a true
  impossibility, because no real value has six digits before `MHz`. **Narrowing to the one
  genuinely impossible shape is what took it from 570 noisy to 185 clean.**
- **Addressing method can split a model line, and it changes the current draw.**
  `KIR-OSD` is the **rotary-addressed** Optica detector at 43 &micro;A standby and
  70 &micro;A alarm; the electronically-addressed twin draws 32 and 45 &micro;A. Two
  parts under one family name, differing in how the address is set, with a ~50%
  current difference that lands straight in a battery calculation. **The rotary /
  electronic split is a real separator on this brand** &mdash; do not read a shared
  family name as a shared spec sheet row.
- **A brand word in a store title that the manufacturer has never written.**
  A Simplex page carried &quot;Digitalflex&quot;. The manufacturer's name for that
  line is **Flex-50**; &quot;Digitalflex&quot; appears in no Simplex document. This is
  a different failure from a wrong class noun &mdash; the noun was right and the
  *proper name* was invented &mdash; and it is invisible to every scan this project
  runs, because a made-up brand word has no shape and no sibling to disagree with. The
  only thing that catches it is an agent reading the live title against the ordering
  block.
- **A trailing numeral can be a count, not a model distinction.** `PCVS-2`'s `2`
  records **how many switches the unit contains**, not which model it is. So the
  sibling-part rule has a third form alongside &quot;one character apart&quot; and
  &quot;suffix encodes a protocol&quot;: **the number may be a quantity inside the
  product**, and a title that reads it as a generation number asserts something the
  manufacturer does not.
- **Three supersession claims in one batch, and the split was two to one again.**
  `SCWLED-CLR-ALERT`'s &quot;replaced by&quot; **is** manufacturer-stated &mdash;
  bulletin `M23.2SS`'s REPLACES table &mdash; so it stayed in the title. `KIR-OSD`'s
  and `GCSVWN`'s are unsourced and were moved to the body. That is now the settled
  handling and it has held across four batches: **the bulletin is the source, the
  datasheet almost never is, and an unsourced claim costs money in two channels if it
  sits in a feed attribute.**
- **A required accessory sold only in a carton of ten is a purchasing fact, not a
  spec.** Edwards states the **GRSW** wiring plate is required for `GCSVWN` and sells
  it **only as a 10-pack**. A buyer ordering one appliance cannot order one plate. That
  belongs in the closing paragraph next to the sibling parts, because it is the thing
  the buyer gets wrong &mdash; and it is the `4099-9015` / `A49CMT-APPLW` incomplete-
  product trap with a quantity attached.

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
