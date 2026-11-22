# La banalità della dimostrazione: protocollo

Versione 1.1, 22 novembre 2026. Scritto e registrato nel repository **prima delle corse**:
domande, materiali, misure, estimatori e soglie stanno qui, e ciò che cambierà dopo va nella
sezione «Deviazioni» in fondo, con la data e il motivo. Lingua originale: italiano. Il progetto
da cui nasce è `docs/design.it.md`.

## 1. Domande

Il 20 novembre 2026 Levent Alpöge ha annunciato una dimostrazione dell'ipotesi di Riemann
generalizzata per le funzioni L di Dirichlet, scritta con Claude in diciassette milioni di
righe di Lean e certificata il giorno dopo dalle comunità di Lean e Mathlib. Nessuno la sa
ancora leggere. Se si chiede a un'AI di spiegarla in modo sempre più semplice:

- **D1.** fino a che livello la spiegazione resta fedele alle fonti?
- **D2.** dove la semplificazione introduce errori, e di che tipo?
- **D3.** un critico che legge le spiegazioni trova passi che non reggono, e quanti sono
  errori della spiegazione, quanti stanno già nella fonte, quanti falsi allarmi?
- **D4.** uno spiegatore che legge tutte le fonti è più fedele di uno che ne legge solo la
  panoramica, e a parità di fonte conta il modello?

L'esperimento non decide se la dimostrazione è corretta: un problema trovato in una fonte si
riporta come segnalazione da verificare, mai come errore della dimostrazione.

## 2. Fonti

Non si ridistribuiscono; `scripts/fetch_sources.py` le scarica e le controlla.

| | Fonte | SHA-256 |
|---|---|---|
| F1 | Alpöge, nota del 20 novembre 2026, `https://alpo.ge/remark.pdf` | `3fc97784b71ddd44ff8aa0a177e99622a1c61b13cfa843a0989ee4a7a0cfeb8d` |
| F2 | Zhang, *A preliminary note on Alpöge's proposed proof of the generalized Riemann hypothesis*, versione del 22/11/2026 (73 pagine), `https://www.ihes.fr/~rzhang/files/GRH%20note.pdf` | `2cbd7e9b693c753f6afa22251db9669c9652555a91cee0cdfbd37a8465ad2ad9` |
| F3a | Dichiarazione congiunta di Lean e Mathlib, 21/11/2026 | `f1bc87e6bf7aa9285fc0507377b850cfa166c9035c8fbc6394a182655f0a9a35` |
| F3b | Pagina dei controlli di Andrew Sutherland, copia del 22/11/2026 (aggiornata alle 04:35 UTC) | `01a43fc8defab818d878bfa8fd900d7563073db3dbc6f150ad73baec0fe388a7` |

La **panoramica** di F2 è la sezione 1, dalla pagina 3 al titolo della sezione 2 a pagina 14
(`banalita.sources.overview_text`, circa 4.300 parole).

## 3. Fatti di riferimento

`data/facts.yaml`, 30 fatti in cinque gruppi (enunciato, architettura, ingredienti, stato,
limiti), ciascuno con fonte, pagina, citazione letterale e livello minimo (1 bambino, 2 liceo,
3 laureato in matematica, 4 teorico dei numeri). Li ha scritti Claude leggendo le fonti; le
citazioni sono controllate in modo meccanico sulla loro pagina, e un secondo agente ne ha
riscontrato il senso. Nessun matematico li ha rivisti.

SHA-256 di `data/facts.yaml`: `51ec2b38301a8da77eb202544c5f4e9c767041ed7eb7e9270b584cecd5f4fad8`.

## 4. Spiegatori

Quattro livelli: L1 «un bambino di dieci anni» (al più 300 parole), L2 «uno studente di liceo»
(600), L3 «un laureato in matematica che non si occupa di teoria dei numeri» (1.000), L4 «un
teorico dei numeri» (1.500).

Tre bracci, **otto spiegazioni per braccio e livello, 96 in tutto**:

| Braccio | Modello | Materiale |
|---|---|---|
| `claude_full` | Claude Opus 5.5 (`claude-opus-5-5`), effort `high`, ragionamento adattivo | F1 e F2 in PDF |
| `claude_overview` | lo stesso | F1 e la panoramica di F2, in testo |
| `qwen_overview` | Qwen3.8-27B a 4 bit (`cyankiwi/Qwen3.8-27B-AWQ-INT4`, vLLM, su una L4), ragionamento acceso, temperatura 0,6, top-p 0,95, top-k 20 | lo stesso testo di `claude_overview` |

Il sistema e l'istruzione sono uguali per tutti (`prompts/explain_system.it.md`,
`prompts/explain_task.it.md`); i due bracci «overview» ricevono lo stesso identico testo
(`banalita.requests.overview_prompt_text`). Le chiamate a Claude passano da Claude Code senza
interfaccia (`claude -p`, `banalita.claude_code`), isolate: nessuno strumento, il prompt di
sistema dell'esperimento al posto di quello di Claude Code, nessuna impostazione, nessun server
MCP, ambiente minimo; i PDF arrivano come documenti, l'uscita del giudice e del critico è JSON
vincolato con `--json-schema`. Le fonti stanno in cache (TTL di un'ora): la prima chiamata di
ogni gruppo con lo stesso prefisso parte da sola. Una risposta che nomina file di progetto o
memorie è scartata come «contaminated». La Batch API (`--backend api`) dà le stesse richieste
a chi rifà l'esperimento con una chiave.

## 5. Misure

- **M1. Leggibilità.** Indice Gulpease, `89 + (300 · frasi − 10 · lettere) / parole`, con le
  regole di conteggio di `banalita.readability`.
- **M2. Copertura.** Per ogni fatto con livello minimo non superiore a quello della
  spiegazione, il giudice decide «yes» (1), «partial» (0,5) o «no» (0); la copertura di una
  spiegazione è la media.
- **M3. Fedeltà.** Il giudice scompone la spiegazione in affermazioni (regola ed esempi in
  `prompts/judge_system.it.md`) e dà a ciascuna un tipo («proof», «context») e un'etichetta:
  supported, unsupported, contradicted, declared_analogy, analogy_as_fact. **Errori** =
  contradicted + analogy_as_fact. **Base** = affermazioni «proof» che non sono analogie
  dichiarate, più gli errori «context» (`banalita.metrics.error_rate`).
- **M4. Caccia all'errore.** Il critico legge la spiegazione da sola (`prompts/critic_system.it.md`)
  e segnala i passi che non reggono; un verificatore con le fonti mette ogni segnalazione in
  «introduced», «in_source» o «false_alarm» (`prompts/verify_system.it.md`). Il critico legge
  anche tre volte la panoramica di F2.

## 6. Giudici e controlli

- **Giudice principale:** Claude Opus 5.5 con F1, F2 (PDF), F3a e F3b (testo), alla cieca:
  riceve la spiegazione ripulita (`banalita.judge.blind`), il lettore a cui era rivolta e i
  fatti del livello, mai il braccio. Uscita JSON vincolata a uno schema. Un giudizio che non
  rispetta lo schema o non copre esattamente i fatti del livello si scarta e si conta.
- **Secondo giudice:** Claude Sonnet 5.5 sulle stesse istruzioni, su 24 spiegazioni estratte
  con il seme `20261122`; accordo sulle etichette con il kappa di Cohen.
- **Controllo NLI:** `MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7` su ogni
  affermazione «contradicted» con citazione: premessa la citazione, ipotesi l'affermazione.
- **Una persona:** l'autore etichetta 60 affermazioni delle spiegazioni L1 e L2, estratte a
  strati sulle etichette del giudice con il seme `20261122`, senza vedere né l'etichetta né il
  braccio (`labeling/`). Da lì precisione e richiamo del giudice per classe.
- **Critici:** Claude Opus 5.5 (principale) e Qwen3.8-27B sulla L4 (secondo critico, per
  misurare i falsi allarmi di un lettore più debole).

Il giudice principale è della stessa famiglia di uno degli spiegatori: si dichiara.

## 7. Previsioni ed estimatori

Le celle sono braccio × livello; le regole sono quelle di `banalita.metrics.verdicts`.

- **P1.** La leggibilità media (Gulpease, media dei bracci) scende strettamente da L1 a L4.
- **P2.** La copertura media è più bassa a L1 che a L4.
- **P3.** La quota di errori, sommata sui bracci, è più alta a L1 che a L4.
- **P4 (la tesi).** In almeno un braccio, a L1 o a L2: copertura almeno 0,6, errori al più il
  5% della base e limite superiore dell'intervallo di Wilson al 95% non oltre il 10%.
- **P5.** Delle segnalazioni del critico principale verificate sulle spiegazioni L1 e L2,
  almeno l'80% è «introduced».
- **P6.** Sommando i livelli, la quota di errori di `claude_overview` è più bassa di quella di
  `qwen_overview`, e quella di `claude_full` più bassa di quella di `claude_overview`.

Ogni quota si riporta con il suo intervallo di Wilson al 95%. Gli intervalli di una cella L1
saranno larghi: si dice.

## 8. Spesa e ordine delle corse

Con Claude Code non si paga a token: il registro `results/spend.jsonl` riporta il costo a
listino di ogni chiamata, e un freno di 150 dollari a listino ferma le corse prima che il
consumo dell'abbonamento esca di misura (stima di tutte le fasi: circa 70-90 dollari a
listino). Ordine: pilota (fuori dai risultati) → spiegazioni di Claude → spiegazioni di Qwen (quando la L4 è libera) → giudizi →
critici → verifiche → secondo giudice → NLI → etichette dell'autore → resoconto.

## 9. Deviazioni

- 22/11/2026, prima delle corse: F2 è la versione del 22 novembre (73 pagine), uscita mentre il
  progetto era in scrittura; la panoramica va da pagina 3 a pagina 14.
- 22/11/2026, prima delle corse (versione 1.1): le chiamate a Claude passano da Claude Code con
  l'abbonamento invece che dalla Batch API con una chiave, su richiesta dell'autore; stesso
  modello, stesse richieste. Il tetto di 60 dollari reali diventa un freno di 150 dollari a
  listino.
- 22/11/2026, prova pilota (fuori dai risultati): quattro spiegazioni e due giudizi, tutti
  riusciti, 8,11 dollari a listino; la nota di Zhang in PDF vale circa 208.000 token. Nessuna
  chiamata ha letto la cache, perché le chiamate con lo stesso prefisso partivano insieme: da
  qui la prima chiamata da sola. Lunghezze entro i limiti (302 parole su 300 a L1).

- 22/11/2026, durante le corse: i 64 giudizi delle spiegazioni di Claude non hanno letto la
  cache (220.000 token riscritti ciascuno, 127 dollari a listino invece di circa 30): Claude
  Code mette da solo il punto di cache in fondo al messaggio, e il codice toglieva il
  `cache_control` dopo le fonti. Corretto da qui in poi (provato: la seconda chiamata legge il
  documento dalla cache); i giudizi già fatti restano validi, la cache non cambia le risposte.
  Il freno passa da 150 a 250 dollari a listino.
