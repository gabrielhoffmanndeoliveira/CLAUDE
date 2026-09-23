<!-- Registro de casos do projeto TFAS. Movido VERBATIM de CLAUDE.md em 23 Sep 2026; nada foi reescrito. Nao e carregado automaticamente: leia sob demanda. E cronologico: entradas posteriores corrigem anteriores; em caso de conflito vale a mais recente e o nucleo em CLAUDE.md. -->

# negocio-ads-medicao

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
