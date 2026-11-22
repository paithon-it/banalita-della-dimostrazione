# La banalità della dimostrazione: progetto

22 novembre 2026. Documento di progetto, da cui nasceranno il protocollo registrato
(`PROTOCOL.it.md`) e il piano di lavoro. Lingua originale: italiano.

## 1. Perché

Il 20 novembre 2026 Levent Alpöge ha annunciato una dimostrazione dell'ipotesi di Riemann
generalizzata scritta con Claude: diciassette milioni di righe di Lean, certificate il 21
novembre dalle comunità di Lean e Mathlib. Nessuno la sa ancora leggere. La versione in prosa
che Alpöge ha fatto generare supera, scrive, le 250.000 pagine e non è pubblica; Robin Zhang ne
ha ricavato una nota di 65 pagine, scritta in gran parte dall'AI, di cui dice di non poter
garantire che sia «una traduzione fedele» del codice. Alpöge stesso scrive che la sua
intuizione «insiste che sarà semplificata in modo massiccio, probabilmente subito».

La tesi dell'autore di paithon: il passo successivo alla certificazione è chiedere all'AI di
spiegare la dimostrazione, fino a renderla comprensibile a un bambino. L'esperimento la mette
alla prova, e cerca gli errori che una semplificazione estrema introduce o rivela.

## 2. Domande

- **D1.** Fino a che livello di semplicità una spiegazione della dimostrazione resta fedele
  alle fonti? Per ogni livello: quanto si capisce (leggibilità), quanto arriva (copertura),
  quanto è falso (fedeltà).
- **D2.** Dove la semplificazione introduce errori, e di che tipo: un'ipotesi persa, un passo
  saltato, un'analogia presa alla lettera, un'affermazione inventata?
- **D3. La caccia all'errore.** Un critico che legge le spiegazioni trova passi che non
  reggono? Quanti sono errori della spiegazione, quanti stanno già nella fonte, quanti sono
  falsi allarmi?
- **D4.** Uno spiegatore che legge tutte le fonti (Claude) è più fedele di uno che ne legge
  solo la panoramica (modelli aperti sulla L4)?

Fuori dall'esperimento: decidere se la dimostrazione è corretta. È certificata in Lean, e un
errore nel teorema vorrebbe dire un difetto comune al kernel di Lean e ai verificatori
indipendenti, o un enunciato sbagliato: l'esperimento non ha gli strumenti per dirlo. Un
problema trovato in una fonte si riporta come segnalazione da verificare, mai come errore
della dimostrazione.

## 3. Fonti

Non si ridistribuiscono: uno script le scarica e ne controlla lo SHA-256.

- **F1.** Alpöge, nota del 20 novembre 2026, 4 pagine (`https://alpo.ge/remark.pdf`).
- **F2.** Zhang, *A preliminary note on Alpöge's proposed proof of the generalized Riemann
  hypothesis*, 65 pagine, sei sezioni (panoramica, rilevare gli zeri dalle somme sulle potenze
  dei primi, recuperarle dalla divisibilità dei periodi, maggiorarle con i periodi automorfi,
  controllare i denominatori con la coomologia di Galois, scegliere i parametri)
  (`https://www.ihes.fr/~rzhang/files/GRH%20note.pdf`). È una nota preliminare: vale la
  versione con l'hash scritto nel protocollo, e una versione nuova si registra come
  deviazione.
- **F3.** Ciò che è certificato: la dichiarazione congiunta di Lean e Mathlib del 21 novembre
  2026 (`https://leanprover-community.github.io/blog/posts/riemann-hypothesis/`), l'enunciato
  `RiemannHypothesis` di Mathlib, la pagina dei controlli di Andrew Sutherland
  (`https://math.mit.edu/~drew/grh/`, viva: se ne congela una copia locale con l'hash, non
  ridistribuita).

## 4. Fatti di riferimento

Un file `data/facts.yaml` con 20-30 fatti sulla dimostrazione, ciascuno con la fonte, la
pagina e la citazione letterale da cui viene. Cinque gruppi: che cosa si dimostra
(enunciato e portata), l'architettura (i passi della catena, nell'ordine), gli ingredienti
(sollevamenti theta, identità di Kudla, formula di Rallis, periodi di Gan-Gross-Prasad,
coomologia di Galois, l'idea di Stepanov…), lo stato (certificazione, lunghezza, prosa non
pubblicata, avvertenza di Zhang), i limiti. Ogni fatto ha un **livello minimo**: il livello più
semplice al quale una spiegazione dovrebbe trasmetterlo (a un bambino si chiede che cosa si
dimostra e che la dimostrazione è una catena di passi, non la formula di Rallis).

I fatti li scrive un'AI (Claude) leggendo le fonti, e un secondo agente indipendente li
riscontra sulla pagina; il file si congela prima delle prove, con il suo SHA-256 nel
protocollo, livelli minimi compresi. Un'assegnazione diversa dei livelli si può provare dopo,
come lettura esplorativa dichiarata, mai al posto del test. Che nessun matematico li abbia
rivisti si dichiara.

## 5. Spiegatori e livelli

Quattro livelli, con un prompt fisso in italiano per ciascuno e un tetto di parole:

| Livello | Lettore | Tetto |
|---|---|---|
| L1 | un bambino di dieci anni | 300 parole |
| L2 | uno studente di liceo | 600 |
| L3 | un laureato in matematica che non fa teoria dei numeri | 1.000 |
| L4 | un teorico dei numeri | 1.500 |

Spiegatori, tre bracci:

- **Claude, fonti intere**: Claude Opus 5.5 (`claude-opus-5-5`) via API, con F1 e F2 interi
  (i PDF passati come documenti, così le formule restano, e tenuti in cache).
- **Claude, sola panoramica**: lo stesso modello con F1 e la sola sezione 1 di F2, cioè lo
  stesso materiale del modello aperto. È il braccio di controllo che separa l'effetto del
  modello da quello della fonte.
- **Modello aperto sulla L4**: Qwen3.8-27B quantizzato a 4 bit
  (`cyankiwi/Qwen3.8-27B-AWQ-INT4` con vLLM, come nell'esperimento della 554), con F1 e la
  sezione 1 di F2 in testo, perché la nota intera supera la sua finestra. È il caso di chi
  chiede una spiegazione a un modello gratuito; un modello aperto più piccolo aggiungerebbe
  poco e non c'è.

Otto spiegazioni per coppia braccio-livello (96 in tutto), con la temperatura di default.

## 6. Misure

- **M1. Leggibilità**: indice Gulpease, la formula standard per l'italiano, calcolata nel
  codice e provata con test.
- **M2. Copertura**: per ogni fatto con livello minimo non superiore a quello della
  spiegazione, un giudice decide se la spiegazione lo trasmette (sì, in parte, no).
- **M3. Fedeltà**: un giudice scompone la spiegazione in affermazioni sulla dimostrazione e
  classifica ciascuna: sostenuta dalle fonti, non sostenuta, contraddetta, oppure analogia
  dichiarata (figurata, non verificabile). Gli **errori** sono le contraddette, più le
  analogie presentate come fatti.
- **M4. Caccia all'errore**: un critico legge la spiegazione da sola e segnala i passi che non
  reggono. Ogni segnalazione la riscontra poi un giudice con le fonti, in tre caselle:
  introdotta dalla semplificazione, già presente nella fonte, falso allarme. Il critico legge
  anche la panoramica di F2, per cercare problemi nella fonte stessa.

**Che cos'è un'affermazione.** Una proposizione che si può dire vera o falsa: sulla
dimostrazione (enunciato, metodo, passi, stato, storia) oppure di contesto (un fatto di
matematica generale citato per spiegare). Le prime contano per la fedeltà; le seconde, se
false, contano fra gli errori. Le analogie dichiarate come tali non si contano; un'analogia
presentata come un fatto sì. La regola esatta e gli esempi stanno nel prompt del giudice,
congelato nel protocollo.

**Giudici.** Il giudice principale è Claude Opus 5.5 con le fonti intere, alla cieca: non sa
quale braccio ha scritto la spiegazione, e le spiegazioni gli arrivano tutte nello stesso
formato. Tre controlli:

- un secondo giudice di un altro modello Claude (Claude Sonnet 5.5) su un quarto delle
  spiegazioni, estratto a caso, per misurare l'accordo (kappa di Cohen);
- un modello di verifica (NLI) multilingue sulla L4, che controlla ogni affermazione
  classificata «contraddetta» contro il passo della fonte indicato dal giudice: un compito
  testuale, alla portata di un modello piccolo;
- **una persona**: l'autore etichetta circa 60 affermazioni delle spiegazioni L1 e L2,
  scelte a strati sulle etichette del giudice, contro il passo della fonte. Da lì precisione e
  richiamo del giudice per classe.

Il modello aperto non fa da giudice: decidere se un'affermazione sui sollevamenti theta è
sostenuta dalla nota di Zhang chiede una profondità che un 27B quantizzato non garantisce, e
misurerebbe il suo rumore più dell'indulgenza di Claude. Che il giudice sia della stessa
famiglia di uno spiegatore si dichiara.

**Critici.** La caccia all'errore la fa Claude Opus 5.5; il modello aperto la ripete come
secondo critico, per vedere se un lettore più debole trova più «errori» e quanti sono falsi
allarmi.

## 7. Previsioni, da fissare nel protocollo

- **P1.** La leggibilità cresce scendendo di livello.
- **P2.** La copertura cala scendendo di livello.
- **P3.** Gli errori per affermazione crescono scendendo di livello.
- **P4 (la tesi).** Esiste un livello sotto L3 (L1 o L2) con copertura almeno 0,6 ed errori
  al più il 5% delle affermazioni, con il limite superiore dell'intervallo al 95% (Wilson)
  non oltre il 10%: semplice e fedele insieme.
- **P5.** Almeno l'80% delle segnalazioni del critico sulle spiegazioni L1 e L2 riguarda errori
  introdotti dalla semplificazione.
- **P6.** A parità di fonte (sola panoramica), Claude è più fedele del modello aperto; con le
  fonti intere, più fedele che con la sola panoramica.

Ogni stima ha il suo intervallo di confidenza: con otto spiegazioni per cella, le affermazioni
di una cella L1 sono poche, e l'intervallo lo dice. Soglie ed estimatori esatti li fissa il
protocollo, prima delle prove.

## 8. Che cosa ne esce

- Il repository pubblico `paithon-it/banalita-della-dimostrazione`: codice (MIT), dati e
  spiegazioni (CC BY-SA 4.0), protocollo, test. Nessuna chiave, nessun dato privato, nessun
  link di sessione.
- Un saggio per «Pecore elettriche» su paithon.it, firmato endjneer: la domanda, la prova, i
  risultati (positivi nel corpo, ciò che non ha retto in appendice), e la spiegazione per
  bambini più fedele, pubblicata con accanto la sua misura di fedeltà.

## 9. Vincoli

- La chiave API arriva dall'ambiente, mai nel repository.
- **Spesa API: tetto di 60 dollari**, con la Batch API (metà prezzo) per tutte le fasi che
  possono aspettare. Il codice somma il costo dai conteggi d'uso di ogni risposta e si ferma
  prima di superare il tetto; se una fase non ci sta, si decide con l'autore.
- La L4 è della macchina dell'autore: si usa quando è libera, si lavora solo in
  `~/rnd/banalita` con tutte le cache lì dentro, e a fine corsa si cancella solo quella
  cartella.
- Le fonti non si ridistribuiscono: nel repository ci sono gli URL e gli hash.
- Nessuna affermazione di errore nella dimostrazione senza una verifica indipendente.

## 10. Lasciato a chi costruisce

Il testo dei prompt (da congelare nel protocollo), il modello NLI, il livello di effort, il
formato dei file di risultato, la pagina con cui l'autore etichetta le 60 affermazioni.
