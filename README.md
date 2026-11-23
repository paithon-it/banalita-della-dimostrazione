# The banality of the proof

*[Italiano](README.it.md)*

On 20 November 2026 Levent Alpöge announced a proof of the generalized Riemann hypothesis for
Dirichlet L-functions, written with Claude in seventeen million lines of Lean and certified the
next day by the Lean and Mathlib communities. Nobody can read it yet.

This experiment asks an AI to explain it to four readers, from a ten-year-old to a number
theorist, and measures what is lost and what becomes false as the explanation gets simpler.
Then a critic looks for steps that do not hold, and a verifier with the sources decides whether
each problem was introduced by the explanation, was already in the source, or is a false alarm.

- **Protocol**, registered before the runs: [`PROTOCOL.md`](PROTOCOL.md) (original in Italian:
  [`PROTOCOL.it.md`](PROTOCOL.it.md)).
- **Design**: [`docs/design.it.md`](docs/design.it.md) (Italian).
- **Reference facts**: [`data/facts.yaml`](data/facts.yaml), 30 facts with source, page and
  verbatim quote.
- **Results**: `results/report.md` and `results/tables/cells.csv`. The experiment closed on
  23 November 2026 with Claude's arms only: see «Deviations» in the protocol.

The experiment does not decide whether the proof is correct.

## Reproducing it

```bash
uv sync --extra dev
uv run python scripts/fetch_sources.py     # the sources, checked by SHA-256 (not in the repository)
uv run pytest                              # the tests
uv run python scripts/run_phase.py --phase explain --dry-run
```

Calls to Claude go through headless Claude Code (`claude -p`, with a subscription) or the Batch
API (`--backend api`, with `ANTHROPIC_API_KEY`). The open model runs on a GPU with vLLM: see
[`gpu/README.md`](gpu/README.md).

## Licenses

Code: MIT ([`LICENSE`](LICENSE)). Data, facts, explanations and judgments: CC BY-SA 4.0
([`LICENSE-data`](LICENSE-data)). The sources belong to their authors and are not
redistributed.

An experiment by [paithon.it](https://paithon.it).
