# La banalità della dimostrazione

*[English](README.md)*

Il 20 novembre 2026 Levent Alpöge ha annunciato una dimostrazione dell'ipotesi di Riemann
generalizzata per le funzioni L di Dirichlet, scritta con Claude in diciassette milioni di righe
di Lean e certificata il giorno dopo dalle comunità di Lean e Mathlib. Nessuno la sa ancora
leggere.

Questo esperimento chiede a un'AI di spiegarla a quattro lettori, da un bambino di dieci anni a
un teorico dei numeri, e misura che cosa si perde e che cosa diventa falso man mano che la
spiegazione si semplifica. Poi un critico cerca i passi che non reggono, e un verificatore con
le fonti decide se l'errore l'ha introdotto la spiegazione, se stava già nella fonte, o se è un
falso allarme.

- **Protocollo** registrato prima delle corse: [`PROTOCOL.it.md`](PROTOCOL.it.md)
  ([English](PROTOCOL.md)).
- **Progetto**: [`docs/design.it.md`](docs/design.it.md).
- **Fatti di riferimento**: [`data/facts.yaml`](data/facts.yaml), 30 fatti con fonte, pagina e
  citazione letterale.
- **Risultati**: `results/report.md` e `results/tables/cells.csv`. L'esperimento si è chiuso il
  23 novembre 2026 con i soli bracci di Claude: vedi «Deviazioni» nel protocollo.

L'esperimento non decide se la dimostrazione è corretta.

## Rifarlo

```bash
uv sync --extra dev
uv run python scripts/fetch_sources.py     # le fonti, controllate con lo SHA-256 (non sono nel repository)
uv run pytest                              # i test
uv run python scripts/run_phase.py --phase explain --dry-run
```

Le chiamate a Claude passano da Claude Code senza interfaccia (`claude -p`, con un abbonamento)
oppure dalla Batch API (`--backend api`, con `ANTHROPIC_API_KEY`). Il modello aperto gira su
una GPU con vLLM: vedi [`gpu/README.md`](gpu/README.md).

## Licenze

Codice: MIT ([`LICENSE`](LICENSE)). Dati, fatti, spiegazioni e giudizi: CC BY-SA 4.0
([`LICENSE-data`](LICENSE-data)). Le fonti restano dei loro autori e non si ridistribuiscono.

Un esperimento di [paithon.it](https://paithon.it).
