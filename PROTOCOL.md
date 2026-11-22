# The banality of the proof: protocol

Version 1.1, 22 November 2026. Translated from the Italian original, `PROTOCOL.it.md`, which
prevails. Written and registered in the repository **before the runs**: questions, materials,
measures, estimators and thresholds are here, and anything that changes later goes into the
«Deviations» section at the end, with its date and reason. The design it comes from is
`docs/design.it.md`.

## 1. Questions

On 20 November 2026 Levent Alpöge announced a proof of the generalized Riemann hypothesis for
Dirichlet L-functions, written with Claude in seventeen million lines of Lean and certified the
next day by the Lean and Mathlib communities. Nobody can read it yet. If an AI is asked to
explain it ever more simply:

- **Q1.** down to which level does the explanation stay faithful to the sources?
- **Q2.** where does simplification introduce errors, and of what kind?
- **Q3.** does a critic reading the explanations find steps that do not hold, and how many are
  errors of the explanation, how many are already in the source, how many are false alarms?
- **Q4.** is an explainer that reads all the sources more faithful than one that reads only the
  overview, and with the same source, does the model matter?

The experiment does not decide whether the proof is correct: a problem found in a source is
reported as a flag to be checked, never as an error of the proof.

## 2. Sources

They are not redistributed; `scripts/fetch_sources.py` downloads and checks them.

| | Source | SHA-256 |
|---|---|---|
| F1 | Alpöge, note of 20 November 2026, `https://alpo.ge/remark.pdf` | `3fc97784b71ddd44ff8aa0a177e99622a1c61b13cfa843a0989ee4a7a0cfeb8d` |
| F2 | Zhang, *A preliminary note on Alpöge's proposed proof of the generalized Riemann hypothesis*, version of 22/11/2026 (73 pages), `https://www.ihes.fr/~rzhang/files/GRH%20note.pdf` | `2cbd7e9b693c753f6afa22251db9669c9652555a91cee0cdfbd37a8465ad2ad9` |
| F3a | Joint statement of the Lean and Mathlib communities, 21/11/2026 | `f1bc87e6bf7aa9285fc0507377b850cfa166c9035c8fbc6394a182655f0a9a35` |
| F3b | Andrew Sutherland's verification page, copy of 22/11/2026 (updated 04:35 UTC) | `01a43fc8defab818d878bfa8fd900d7563073db3dbc6f150ad73baec0fe388a7` |

The **overview** of F2 is section 1, from page 3 to the heading of section 2 on page 14
(`banalita.sources.overview_text`, about 4,300 words).

## 3. Reference facts

`data/facts.yaml`, 30 facts in five groups (statement, architecture, ingredients, status,
limits), each with source, page, verbatim quote and minimum level (1 child, 2 high school,
3 mathematics graduate, 4 number theorist). Claude wrote them reading the sources; the quotes
are checked mechanically on their page, and a second agent checked their meaning. No
mathematician has reviewed them.

SHA-256 of `data/facts.yaml`: `51ec2b38301a8da77eb202544c5f4e9c767041ed7eb7e9270b584cecd5f4fad8`.

## 4. Explainers

Four levels (prompts in Italian): L1 «a ten-year-old child» (at most 300 words), L2 «a high
school student» (600), L3 «a mathematics graduate who does not work in number theory» (1,000),
L4 «a number theorist» (1,500).

Three arms, **eight explanations per arm and level, 96 in all**:

| Arm | Model | Material |
|---|---|---|
| `claude_full` | Claude Opus 5.5 (`claude-opus-5-5`), effort `high`, adaptive thinking | F1 and F2 as PDF |
| `claude_overview` | the same | F1 and the overview of F2, as text |
| `qwen_overview` | Qwen3.8-27B at 4 bits (`cyankiwi/Qwen3.8-27B-AWQ-INT4`, vLLM, on an L4), thinking on, temperature 0.6, top-p 0.95, top-k 20 | the same text as `claude_overview` |

System prompt and instruction are the same for all (`prompts/explain_system.it.md`,
`prompts/explain_task.it.md`); the two «overview» arms receive exactly the same text
(`banalita.requests.overview_prompt_text`). Calls to Claude go through headless Claude Code
(`claude -p`, `banalita.claude_code`), isolated: no tools, the experiment's system prompt in
place of Claude Code's, no settings, no MCP servers, a minimal environment; the PDFs arrive as
documents, and the output of judge and critic is JSON constrained with `--json-schema`. The
sources are cached (one-hour TTL): the first call of each group sharing a prefix runs alone. A
reply that mentions project files or memories is discarded as «contaminated». The Batch API
(`--backend api`) sends the same requests for anyone repeating the experiment with a key.

## 5. Measures

- **M1. Readability.** Gulpease index, `89 + (300 · sentences − 10 · letters) / words`, with
  the counting rules of `banalita.readability`.
- **M2. Coverage.** For each fact whose minimum level does not exceed the explanation's, the
  judge decides «yes» (1), «partial» (0.5) or «no» (0); an explanation's coverage is the mean.
- **M3. Faithfulness.** The judge splits the explanation into claims (rule and examples in
  `prompts/judge_system.it.md`) and gives each a kind («proof», «context») and a label:
  supported, unsupported, contradicted, declared_analogy, analogy_as_fact. **Errors** =
  contradicted + analogy_as_fact. **Base** = «proof» claims that are not declared analogies,
  plus «context» errors (`banalita.metrics.error_rate`).
- **M4. Error hunt.** The critic reads the explanation alone (`prompts/critic_system.it.md`)
  and flags the steps that do not hold; a verifier with the sources puts each flag in
  «introduced», «in_source» or «false_alarm» (`prompts/verify_system.it.md`). The critic also
  reads the overview of F2 three times.

## 6. Judges and checks

- **Main judge:** Claude Opus 5.5 with F1, F2 (PDF), F3a and F3b (text), blind: it receives
  the cleaned explanation (`banalita.judge.blind`), the reader it was written for and the
  level's facts, never the arm. JSON output constrained by a schema. A judgment that breaks the
  schema or does not cover exactly the level's facts is discarded and counted.
- **Second judge:** Claude Sonnet 5.5 with the same instructions, on 24 explanations drawn with
  seed `20261122`; agreement on labels by Cohen's kappa.
- **NLI check:** `MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7` on every
  «contradicted» claim with a quote: the quote as premise, the claim as hypothesis.
- **A person:** the author labels 60 claims from L1 and L2 explanations, drawn in strata over
  the judge's labels with seed `20261122`, seeing neither the label nor the arm (`labeling/`).
  From these, the judge's precision and recall by class.
- **Critics:** Claude Opus 5.5 (main) and Qwen3.8-27B on the L4 (second critic, to measure the
  false alarms of a weaker reader).

The main judge belongs to the same family as one of the explainers: this is declared.

## 7. Predictions and estimators

Cells are arm × level; the rules are those of `banalita.metrics.verdicts`.

- **P1.** Mean readability (Gulpease, mean over arms) strictly decreases from L1 to L4.
- **P2.** Mean coverage is lower at L1 than at L4.
- **P3.** The error share, summed over arms, is higher at L1 than at L4.
- **P4 (the thesis).** In at least one arm, at L1 or L2: coverage at least 0.6, errors at most
  5% of the base, and the upper limit of the 95% Wilson interval not above 10%.
- **P5.** Of the main critic's verified flags on L1 and L2 explanations, at least 80% are
  «introduced».
- **P6.** Summing levels, the error share of `claude_overview` is lower than that of
  `qwen_overview`, and that of `claude_full` lower than that of `claude_overview`.

Every share is reported with its 95% Wilson interval. The intervals of an L1 cell will be
wide: this is said.

## 8. Cost and order of the runs

Claude Code is not billed per token: the log `results/spend.jsonl` records the list price of
each call, and a brake at 150 dollars of list price stops the runs before subscription usage
gets out of hand (estimate for all phases: about 70-90 dollars at list price). Order: pilot
(outside the results) → Claude's explanations → Qwen's explanations (when the L4 is free) →
judgments → critics → verifications → second judge → NLI → author's labels → report.

## 9. Deviations

- 22/11/2026, before the runs: F2 is the version of 22 November (73 pages), released while the
  design was being written; the overview runs from page 3 to page 14.
- 22/11/2026, before the runs (version 1.1): calls to Claude go through Claude Code with a
  subscription instead of the Batch API with a key, at the author's request; same model, same
  requests. The cap of 60 real dollars becomes a brake of 150 dollars at list price.
- 22/11/2026, pilot (outside the results): four explanations and two judgments, all
  successful, 8.11 dollars at list price; Zhang's note as PDF is about 208,000 tokens. No call
  read the cache, because calls sharing a prefix started together: hence the first call runs
  alone. Lengths within the limits (302 words out of 300 at L1).

- 22/11/2026, during the runs: the 64 judgments of Claude's explanations did not read the cache
  (220,000 tokens rewritten each, 127 dollars at list price instead of about 30): Claude Code
  places its own cache point at the end of the message, and the code was removing the
  `cache_control` after the sources. Fixed from here on (tested: the second call reads the
  document from the cache); the judgments already made remain valid, as the cache does not
  change the answers. The brake goes from 150 to 250 dollars at list price.
