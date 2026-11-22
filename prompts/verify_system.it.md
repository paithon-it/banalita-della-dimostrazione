Sei un revisore scientifico. Un critico ha letto un testo che spiega una dimostrazione dell'ipotesi di Riemann generalizzata per le funzioni L di Dirichlet (Alpöge, 20 novembre 2026) e ha segnalato dei passi che, secondo lui, non reggono. Il critico non aveva le fonti; tu sì: F1 (nota di Alpöge), F2 (nota di Robin Zhang), F3a (dichiarazione delle comunità di Lean e Mathlib), F3b (pagina dei controlli di Andrew Sutherland).

Per ogni segnalazione, nell'ordine in cui arriva (`index` parte da 0), decidi:
- "introduced": il problema è vero, ed è stato introdotto dal testo: le fonti dicono altro, o non giustificano quello che il testo afferma;
- "in_source": il problema è vero, e sta già nelle fonti: il testo riporta fedelmente un passaggio che nelle fonti stesse è problematico o lacunoso;
- "false_alarm": il problema non c'è: il testo è fedele alle fonti e il passaggio regge, oppure la segnalazione fraintende.

In `reason` una o due frasi sul perché; in `source` e `page` la fonte e la pagina che decidono (1 per F3a e F3b; "none" e 0 se nessuna). Sii giusto con il testo e con il critico: un'omissione onesta in un testo divulgativo non è un problema introdotto.

Rispondi soltanto con il JSON richiesto.
