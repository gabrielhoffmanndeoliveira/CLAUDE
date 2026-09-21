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

**Scope ends at position 654 of `ranked.json`**, the last product with any
Search Console impressions. The list nominally holds 805 candidates, but
positions 655–804 recorded zero impressions over six months, so the owner cut
them: writing pages nobody searches for does not pay for itself in organic
search. Finishing position 654 covers 100% of the priority group's 165,818
impressions.

Working files live outside the repo, in `/tmp/tfas/enrich/`:

- `ranked.json` — the 805 candidates in priority order. Record shape:
  `{"id","handle","title","vendor","type","desc","qty","sku","price","pn","impr","clicks","pos"}`
- `bN/slice.json` — the 18-product slice for batch N
- `bN/agent{1,2,3}.json` — per-agent research output
- `bN/varsA.json`, `bN/varsB.json` — validated publish payloads, 9 products each
- `pending_fixes.md` — corrections queued against already-published pages

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
- **The sibling part is the dominant failure mode.** Part numbers differ by one
  character and describe different products. Find the full ordering table and
  confirm which row is this exact part before writing anything.
- **The Omega trap:** `Ω` often extracts as the letter `W`. An extracted "50W" in
  a resistance spec is almost always 50 Ω. Hit three times so far.
- **The dropped-decimal trap:** a title copied from the adjacent catalogue row
  loses a decimal point and asserts a value ten times too large. Edwards lists
  `EOL-4.7` (4.7 kΩ) and `EOL-47` (47 kΩ) on consecutive rows; the store's
  EOL-4.7 page carried the EOL-47 text while separately stocking the real EOL-47.
  A full scan of the 19,440 active products found exactly one such case, so the
  pattern is closed catalogue-wide, but it recurs whenever a new row is copied.
- **The generation trap:** one document number can cover two product generations
  at different revisions. Confirm the revision covers the part.
- Never state stock, lead time, or condition.
- Unverifiable claims go in an `unverified` array with the reason, never in the copy.
- Always ask agents to contradict the briefing. Six of the coordinator's own
  premises have been proven wrong this way; that is the point.

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
