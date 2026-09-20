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
- **The sibling part is the dominant failure mode.** Part numbers differ by one
  character and describe different products. Find the full ordering table and
  confirm which row is this exact part before writing anything.
- **The Omega trap:** `Ω` often extracts as the letter `W`. An extracted "50W" in
  a resistance spec is almost always 50 Ω. Hit three times so far.
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
