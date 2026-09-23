<!-- Registro de casos do projeto TFAS. Movido VERBATIM de CLAUDE.md em 23 Sep 2026; nada foi reescrito. Nao e carregado automaticamente: leia sob demanda. E cronologico: entradas posteriores corrigem anteriores; em caso de conflito vale a mais recente e o nucleo em CLAUDE.md. -->

# pipeline-operacao

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

**Progress: 1,335 enrichment pages published** (555 old list + 768 v2 through v2b50, verified live), plus 260 title-only products — 555 from the old list plus v2b01 through
v2b40 complete (the held `BEAM1224S` released with its supersession moved to the
body), plus fifteen from the photo batches (`foto01`, `foto02`), plus two queued title defects (`4-NET-SM`, `ZH-MC-W`) and four Thermotech
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
- Never state stock, lead time, or condition.
- Unverifiable claims go in an `unverified` array with the reason, never in the copy.
- Always ask agents to contradict the briefing. **Seven** of the coordinator's own
  premises have been proven wrong this way; that is the point.
