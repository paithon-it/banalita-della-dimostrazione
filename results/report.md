# Risultati

Giudizi usati: 64; scartati: 0.

| Previsione | Esito | Dettaglio |
|---|---|---|
| P1 | passa | [62.31221642734063, 56.74352104673463, 54.995685864432716, 54.76158850335238] |
| P2 | non passa | [0.76875, 0.6808035714285714, 0.7262500000000001, 0.76875] |
| P3 | non passa | [0.003484320557491289, 0.007259528130671506, 0.013365735115431349, 0.015384615384615385] |
| P4 | passa | [["claude_full", 1], ["claude_full", 2], ["claude_overview", 1], ["claude_overview", 2]] |
| P5 | non passa | [16, 27] |
| P6 | non valutabile | {"claude_full": 0.003968253968253968, "claude_overview": 0.0215311004784689, "qwen_overview": NaN} |

## Quote con intervallo di Wilson al 95%

- P3, errori a L1: 1/287 = 0.35% (0.06-1.95%)
- P3, errori a L2: 4/551 = 0.73% (0.28-1.85%)
- P3, errori a L3: 11/823 = 1.34% (0.75-2.38%)
- P3, errori a L4: 17/1105 = 1.54% (0.96-2.45%)
- P5, segnalazioni introdotte a L1-L2: 16/27 = 59.26% (40.73-75.49%)
- P6, errori di claude_full: 6/1512 = 0.40% (0.18-0.86%)
- P6, errori di claude_overview: 27/1254 = 2.15% (1.48-3.11%)

## Analisi aggiunte dopo (23/11/2026)

Non sono previsioni registrate: dicono quanto i verdetti dipendono da due scelte di misura.

**Affermazioni sul materiale.** 19 affermazioni di claude_overview dicono che cosa le fonti dello spiegatore contengono o non contengono (`data/posthoc/meta_claims.json`): vere per il suo materiale, false per le fonti del giudice. Se non contano come errori:

- P3: passa
- P6, metà valutabile: passa

- P3, errori a L1: 1/287 = 0.35% (0.06-1.95%)
- P3, errori a L2: 4/551 = 0.73% (0.28-1.85%)
- P3, errori a L3: 6/823 = 0.73% (0.33-1.58%)
- P3, errori a L4: 3/1105 = 0.27% (0.09-0.80%)
- P6, errori di claude_full: 6/1512 = 0.40% (0.18-0.86%)
- P6, errori di claude_overview: 8/1254 = 0.64% (0.32-1.25%)

**Conteggio delle frasi.** Se il punto dopo una lettera sola chiude la frase (una variabile, «fino a x.»): P1 non passa, Gulpease per livello 63.62, 57.26, 55.82, 56.16.
