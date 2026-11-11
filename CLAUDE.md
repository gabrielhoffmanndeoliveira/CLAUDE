# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

A working repository for SEO and catalog maintenance of the TFAS Shopify store. It holds no application code: there is no build, lint, or test step. The deliverables are CSV files that a person imports into Shopify, mostly through the Matrixify app.

## Layout

- `tfas-seo/` — all TFAS deliverables (CSV).
- `ths-seo/` — SEO deliverables for The House Supplier, in the same import / ROLLBACK / REVIEW trio used for TFAS. Not applied until approved.
- `ths-ops/` — change logs for The House Supplier (THS, a separate Shopify store). Each row records a change applied directly through the Shopify API, with the previous value and how to roll it back. TFAS product IDs and CSVs do not apply to THS.
- `.mcp.json` — Chrome DevTools MCP server, run headless against the container's preinstalled Chromium (`/opt/pw-browsers/chromium`).
- `.claude/settings.json` — Claude Code project settings.

## Files in `tfas-seo/`

### Product description rewrites

Three batches, each with the same trio of files:

| Batch | Selection | Import file | Rollback file | Review file |
|---|---|---|---|---|
| 1 | 60 priority products | `Products_new_descriptions_matrixify.csv` | `Products_ROLLBACK_original_descriptions_matrixify.csv` | `REVIEW_descriptions_verify_notes.csv` |
| 2 | Next 100 products by revenue | `Products_batch2_new_descriptions_matrixify.csv` | `Products_batch2_ROLLBACK_original_descriptions_matrixify.csv` | `REVIEW_batch2_descriptions_verify_notes.csv` |
| 3 | Top 100 products by GSC impressions | `Products_batch3_new_descriptions_matrixify.csv` | `Products_batch3_ROLLBACK_original_descriptions_matrixify.csv` | `REVIEW_batch3_descriptions_verify_notes.csv` |

- Import and rollback files use the Matrixify columns `ID, Handle, Command, Body HTML` with `Command = UPDATE`, so an import changes only the description.
- Review files list, per product, the word count, the sources used (manufacturer datasheets), and `Verify notes`: claims that could not be confirmed and need a human check before import. Batch 3 marks the most important ones with `PRIORITY:`.

### Resideo archive

- `resideo_archived_products_backup.csv` — the Resideo products with no sales that were archived, with their previous status and a redirect target.
- `Products_resideo_UNARCHIVE_rollback_matrixify.csv` — Matrixify file (`ID, Handle, Command, Status`) that sets them back to `Active`.

### Redirects

- `shopify_redirects_404.csv` — 301 redirects (`Redirect from, Redirect to`) for 363 archived product URLs that returned 404, each pointing to its category collection, or to the brand collection as a fallback.

## Conventions

- **Every change ships with its rollback.** Any file that modifies store data is committed together with a file that restores the previous state.
- **Change only what is needed.** Matrixify files carry the identifying columns plus the single field being changed.
- **Description format.** An opening `<p>` paragraph, then `<h3>` sections (starting with `Key Features`) with `<ul>` lists. Product facts come from manufacturer documentation; anything unconfirmed goes into the review file instead of the description.
- **Redirect targets must exist.** Check that each target collection returns 200 before adding a redirect.
- **File naming.** `Products_<scope>_<what>_matrixify.csv` for imports, `ROLLBACK` in the name for rollbacks, `REVIEW_` prefix for human-review notes.
- Nothing in this repository is applied to the store automatically; a person runs the imports.
