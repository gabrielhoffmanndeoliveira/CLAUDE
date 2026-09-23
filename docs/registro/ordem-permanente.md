<!-- Registro de casos do projeto TFAS. Movido VERBATIM de CLAUDE.md em 23 Sep 2026; nada foi reescrito. Nao e carregado automaticamente: leia sob demanda. E cronologico: entradas posteriores corrigem anteriores; em caso de conflito vale a mais recente e o nucleo em CLAUDE.md. -->

# ordem-permanente

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

**Restated a THIRD time on 22 Sep 2026, and this time with an instruction attached:
&quot;segue sempre, grava isso no seu claude.md&quot;** &mdash; keep going always, and
*write that down*. It came immediately after a status report, with ten batches, six photo
harvests and 585 photographs already delivered that day, so it is not a nudge to start
&mdash; it is the owner telling the coordinator to stop needing to be told. **The
instruction to record it is the operative part.** A standing order that lives only in a
conversation dies with the context window; the owner has now had to give this one three
times, and the reason it needed repeating is that it was being treated as encouragement
rather than as configuration. It is configuration. **Anyone reading this file starts
already authorised: slice the next batch, launch the agents, publish what validates, flag
what is the owner's to decide, and do not ask.**

**What it looks like in practice, measured on the day it was restated.** Six batches
(v2b20&ndash;v2b25), 108 products sliced, 90 published, four live title corrections
outside any batch, a catalogue-wide verification sweep, 29 rows consolidated into the
owner's decision file, and the Google Ads target changed and its baseline frozen. The
shape that made that possible is **three research agents always in flight while the
coordinator does something else** &mdash; validating the previous batch, running a sweep,
fetching a document to check an agent's strongest claim, or writing up what the last
batch proved. **Idle coordinator time is the only waste in this loop**, because the
agents are the long pole and nothing the coordinator does is on their critical path.

**The agent mix, set by the owner on 22 Sep 2026 after asking whether eight were worth
it: TWO text agents and FOUR photo agents.** The answer came from measuring the nine
agents completed that day &mdash; 2.69M tokens total, and the yield is not comparable
across the two frontiers:

| frontier | tokens | output | per unit |
|---|---|---|---|
| photographs | 844,394 | 583 rows | **1,448 tokens/photo** |
| text | 1,577,392 | 30 pages | **52,580 tokens/page** |

**Photographs are ~36x cheaper per delivered item, which is why the mix tilts that way.**
The text figure looks damning until you count what it bought: those 30 pages produced
**six title-level defects, one in five** &mdash; a $8,595 detector sold as having the
display that distinguishes the model it is not, a $2,657 speaker asserting a line voltage
its manufacturer does not make, a sensing component sold as a finished detector, an
agent-release panel sold as an ordinary one. Measured as pages written it is expensive;
measured as feed errors found it is cheap.

**And the real ceiling is not the agents, it is the coordinator.** Nine agents ran 2.8
hours of work in about 40 minutes of wall clock, because they parallelise and nothing the
coordinator does is on their critical path. But the coordinator is **serial**: every
returning batch costs 10&ndash;15 minutes to validate against the schema, fetch and read
the strongest claim personally, publish, record and commit. **Above about six concurrent
they queue behind the coordinator, and a waiting agent burns tokens at the same rate as a
working one.** Six is the number; the mix is what to tune.
**Batches are therefore 12 products, 2 agents of 6** &mdash; not 18 split 9/9. Six products
per agent is what the quality of this work rests on, so shrink the batch, never the
agent's share.

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

## Conventions

- Battery capacity, pack counts, and fiber mode (single vs multi) in titles are
  the highest-risk fields. Verify them against a manufacturer document every time.
- Do **not** add "Non-Fire", "(Security)", or "Not Fire Rated" to product titles.
  Owner's decision. Such warnings belong in the description body only. Using a
  manufacturer's own product name is fine even when it contains such a word.
- Scratch scripts and datasheet PDFs produced during research are gitignored.

