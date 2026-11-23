# Le 64 spiegazioni di Claude

Il testo esatto di ogni spiegazione, raggruppato per lettore e per condizione, con la misura che ne danno il giudice, il critico e il verificatore. Generato da `analysis/spiegazioni.py` a partire da `results/`: i file JSONL restano la fonte.

## Livello 1: un bambino di dieci anni (al più 300 parole)

### claude_full-L1-s00

*nota intera, spiegazione 1 di 8.* Fatti del livello: 3 sì, 1 in parte, 1 no (copertura 0,70) · errori 0 su 19 · analogie dichiarate 1 · segnalazioni del critico 1, errori introdotti 1 · 329 parole (limite 300) · Gulpease 61,5

I numeri primi (2, 3, 5, 7, 11…) sembrano comparire a caso. Da 150 anni i matematici sospettano che il loro disordine abbia un limite preciso: è l'ipotesi di Riemann. Levent Alpöge, lavorando con l'intelligenza artificiale Claude, ha annunciato di averne dimostrato una versione più grande, che vale anche per i primi divisi in famiglie, come "quelli che finiscono per 1" o "quelli che finiscono per 3".

La dimostrazione fa tre mosse.

Prima mossa: si tiene un conteggio speciale dei primi fino a un numero x. Se l'ipotesi fosse falsa, questo conteggio a volte supererebbe di parecchio la radice quadrata di x, cioè √x. Basta quindi trovare tratti di numeri, sempre più lontani, in cui non la supera, o la supera solo di pochissimo.

Seconda mossa: con oggetti matematici molto complicati si costruiscono dei numeri speciali. Più il conteggio è grande, più questi numeri sono divisibili per tanti primi. Ma un numero diverso da zero che si può dividere per 2, 3, 5 e 7 vale almeno 210: avere tanti divisori obbliga un numero a essere grande. Qui semplifico, perché quei numeri sono un po' più strani degli interi, ma l'idea è questa. Un'altra stima dice invece che quei numeri non possono essere troppo grandi. Stretto fra queste due regole, il conteggio non può esagerare.

Terza mossa: la costruzione si ripete m volte di fila, e ogni ripetizione aggiunge divisibilità. Però porta anche due errori: uno che diventa più piccolo quando m cresce (come x diviso m) e uno che diventa più grande (come m). Come in un'altalena, ed è solo un paragone, l'equilibrio si trova quando m è circa √x. Da lì nasce proprio il "½" che l'ipotesi chiede, perché √x è x elevato a ½.

Una cosa onesta da sapere: la dimostrazione è gigantesca, circa 17 milioni di righe scritte per Lean, un programma che controlla ogni passaggio. Nessuna persona l'ha letta tutta. Alpöge stesso dice di non padroneggiarla ancora e si aspetta versioni molto più corte.

### claude_full-L1-s01

*nota intera, spiegazione 2 di 8.* Fatti del livello: 4 sì, 1 in parte, 0 no (copertura 0,90) · errori 0 su 22 · analogie dichiarate 2 · segnalazioni del critico 1, errori introdotti 0 · 315 parole (limite 300) · Gulpease 62,5

I numeri primi sono quelli che si dividono solo per 1 e per sé stessi: 2, 3, 5, 7, 11… Da più di 150 anni i matematici si chiedono se, contandoli, si sbagli sempre di poco. L'ipotesi di Riemann dice di sì. La versione "generalizzata" vale anche per i primi che cadono in file come 1, 4, 7, 10, 13… Il 20 novembre 2026 Levent Alpöge ha annunciato di averla dimostrata insieme a Claude, un'intelligenza artificiale.

La dimostrazione procede in tre passi. Primo: basta far vedere che un certo conteggio dei primi fino a un numero x non supera mai di molto la radice quadrata di x, almeno su tratti di numeri lunghi quanto si vuole. Se è così, l'ipotesi è vera.

Secondo: per controllare il conteggio si costruiscono numeri speciali, usando strumenti matematici molto avanzati. Più primi ci sono, più volte questi numeri si possono dividere. Ma un numero che si divide tantissime volte dev'essere grande: pensa a 1024, che si divide per 2 dieci volte. (È solo un esempio per darti l'idea.) Si sa però che questi numeri non possono essere troppo grandi, quindi i primi non possono essere troppi.

Terzo: per ottenere tanta divisibilità si ripete m volte un'operazione chiamata "sollevamento theta". È come salire m gradini. Ogni gradino aumenta la divisibilità, ma restano due errori: uno grande come x diviso m, l'altro grande come m. Il punto di equilibrio è scegliere m uguale alla radice di x. Per esempio, con x = 100 si prende m = 10, e i due errori valgono entrambi 10. Secondo Alpöge, l'idea di questa scelta l'ha suggerita Claude.

La dimostrazione è lunghissima: circa 17 milioni di righe scritte per Lean, un programma che controlla ogni passaggio come un correttore instancabile. La comunità di Lean ha verificato che la dimostrazione funziona. Nemmeno Alpöge, però, dice di capirla ancora tutta, e ora i matematici dovranno studiarla davvero.

### claude_full-L1-s02

*nota intera, spiegazione 3 di 8.* Fatti del livello: 4 sì, 1 in parte, 0 no (copertura 0,90) · errori 0 su 19 · analogie dichiarate 2 · segnalazioni del critico 1, errori introdotti 0 · 308 parole (limite 300) · Gulpease 60,9

I numeri primi (2, 3, 5, 7, 11…) sono i mattoncini con cui si costruiscono tutti gli altri numeri. I matematici vogliono sapere quanti primi ci sono fra numeri di una certa grandezza, anche dentro file come 1, 4, 7, 10, 13… (sempre +3). L'ipotesi di Riemann generalizzata dice che questi conteggi sono prevedibili nel modo migliore possibile: l'errore resta vicino alla radice quadrata. Detto da matematici, certe funzioni speciali hanno tutti i loro "zeri" su una sola linea.

Levent Alpöge, lavorando con l'intelligenza artificiale Claude, dice di averlo dimostrato. La dimostrazione ha due passi.

**Primo passo.** Si costruisce una somma fatta con i numeri primi. Se questa somma resta piccola, cioè circa la radice quadrata di x, su intervalli lunghi, allora nessuno zero può stare fuori dalla linea.

**Secondo passo.** Per tenere piccola quella somma si usano numeri speciali chiamati "periodi". Un'analogia: un numero intero diverso da zero che si può dividere per 2 cento volte di fila deve essere enorme. Quindi, se un numero non è troppo grande, non può essere diviso troppe volte. Nella dimostrazione, quante volte i periodi si lasciano dividere dipende proprio dalla somma sui primi. Siccome i periodi non sono troppo grandi, anche la somma non può esserlo.

Per rendere i periodi molto divisibili si ripete m volte un'operazione chiamata "sollevamento theta". Alla fine restano due errori: uno grande circa x diviso m, l'altro circa m. Se x vale 10 000 e si sceglie m = 100, entrambi valgono 100, cioè la radice quadrata di x. Questa scelta l'aveva suggerita Claude, e da qui nasce la linea dell'1/2.

La dimostrazione è lunghissima: circa 17 milioni di righe scritte in Lean, un programma che controlla ogni passaggio. Nessuna persona l'ha letta tutta, ma in un giorno la comunità di Lean l'ha verificata. Alpöge pensa che presto se ne troveranno versioni molto più corte.

### claude_full-L1-s03

*nota intera, spiegazione 4 di 8.* Fatti del livello: 2 sì, 3 in parte, 0 no (copertura 0,70) · errori 1 su 21 · analogie dichiarate 1 · segnalazioni del critico 3, errori introdotti 2 · 317 parole (limite 300) · Gulpease 68,9

I numeri primi sono quelli che si dividono solo per 1 e per se stessi: 2, 3, 5, 7, 11… Sembrano sparsi a caso. Da più di 150 anni i matematici cercano di dimostrare che in realtà sono distribuiti in modo molto ordinato. Questa idea si chiama ipotesi di Riemann. La versione dimostrata qui è più grande, la versione “generalizzata”. Riguarda anche i primi che cadono in file regolari, per esempio 3, 7, 11, 15, 19… (cioè contando di 4 in 4).

Il trucco principale si basa su un fatto semplice. Se un numero intero, diverso da zero, si può dividere per 2 dieci volte di seguito, allora deve valere almeno 1024. Più è divisibile, più è grande.

Alpöge e Claude hanno costruito dei numeri speciali, chiamati “periodi”. Li hanno costruiti in modo che i primi lascino dentro di loro tante divisibilità. Poi hanno dimostrato che questi numeri non possono essere troppo grandi. Quindi non possono essere troppo divisibili. Questo pone un tetto: il conteggio dei primi non può “sbandare” troppo. E se lo sbandamento resta piccolo, l'ipotesi è vera.

Per ottenere tanta divisibilità ripetono più volte un'operazione, detta “sollevamento theta”. È un po' come piegare un foglio tante volte: ogni piega aggiunge un po' di divisibilità (questa è solo un'analogia). Ripeterla troppe volte però produce anche errori. Il numero giusto di ripetizioni è circa la radice quadrata del numero fino a cui si contano i primi. Proprio da lì nasce il “1/2” dell'ipotesi.

Per tenere sotto controllo i pezzi più difficili servono moltissimi strumenti di quasi tutta la teoria dei numeri. La dimostrazione è stata scritta per il computer, in un linguaggio chiamato Lean, che controlla ogni passaggio. Sono circa 17 milioni di righe. In un giorno è stata verificata in modo indipendente da altri esperti. Però nessuna persona l'ha ancora letta e capita tutta. Neppure Alpöge dice di padroneggiarla. Capirla davvero è il prossimo lavoro.

### claude_full-L1-s04

*nota intera, spiegazione 5 di 8.* Fatti del livello: 5 sì, 0 in parte, 0 no (copertura 1,00) · errori 0 su 20 · analogie dichiarate 2 · segnalazioni del critico 1, errori introdotti 0 · 322 parole (limite 300) · Gulpease 64,1

I numeri primi sono quelli divisibili solo per 1 e per sé stessi: 2, 3, 5, 7, 11… Sembrano sparsi a caso. Da 150 anni i matematici si chiedono quanto bene si possa prevedere quanti ce ne sono fino a un certo numero. La risposta dipende da dove si trovano gli "zeri" di certe funzioni speciali, le funzioni L. L'ipotesi di Riemann generalizzata dice che stanno tutti su una stessa linea, quella del "1/2". Levent Alpöge, lavorando con l'intelligenza artificiale Claude, dice di averla dimostrata.

La dimostrazione procede in due passi.

Nel primo si costruisce un "conto" che somma contributi dai numeri primi, togliendo la parte prevedibile. Se uno zero stesse fuori dalla linea, questo conto prima o poi diventerebbe troppo grande. Basta quindi dimostrare che resta piccolo, all'incirca come la radice quadrata di x, almeno su certi tratti lunghi.

Il secondo passo è il più difficile. Si usano numeri speciali chiamati "periodi". Un numero di questo tipo, se non è zero e si può dividere per tantissimi primi, non può essere piccolo. Un'analogia: un numero divisibile per 2, 3, 5 e 7 deve valere almeno 210. I primi rendono i periodi molto divisibili, ma si dimostra che i periodi non sono troppo grandi. Così i primi non possono far crescere troppo il conto.

Per ottenere abbastanza divisibilità si ripete m volte un'operazione chiamata "sollevamento theta". Ripeterla aiuta, ma crea due errori, uno grande circa x diviso m e l'altro circa m. È come un'altalena da tenere in equilibrio (anche questa è un'analogia). L'equilibrio si trova quando m è la radice quadrata di x, ed è da qui che viene il "1/2". Questa scelta l'ha suggerita Claude.

La dimostrazione è enorme: circa 17 milioni di righe in Lean, un linguaggio in cui un computer controlla ogni passaggio. La comunità di Lean l'ha verificata in un giorno. Però nessuna persona l'ha ancora letta tutta, e Alpöge spera che presto diventi molto più semplice.

### claude_full-L1-s05

*nota intera, spiegazione 6 di 8.* Fatti del livello: 4 sì, 1 in parte, 0 no (copertura 0,90) · errori 0 su 21 · analogie dichiarate 1 · segnalazioni del critico 1, errori introdotti 1 · 305 parole (limite 300) · Gulpease 64,9

I numeri primi sono i "mattoncini" della moltiplicazione: 2, 3, 5, 7, 11... Da più di 150 anni i matematici cercano di capire esattamente come sono sparsi. Esistono funzioni speciali, le "funzioni L", che fanno da mappa dei primi, anche di quelli in file come 1, 5, 9, 13... L'ipotesi dice che certi punti speciali di queste mappe, gli "zeri", stanno tutti su una stessa linea. Levent Alpöge dice di averlo dimostrato insieme all'intelligenza artificiale Claude.

La dimostrazione ha due parti. Nella prima si fa un conteggio pesato dei primi. Se uno zero stesse fuori dalla linea, questo conteggio crescerebbe troppo in fretta. Quindi basta mostrare che resta piccolo, più o meno come la radice quadrata del numero fino a cui si conta (fino a 100 la radice è 10, perché 10 × 10 = 100). E basta controllarlo solo su certi tratti lunghi, scelti apposta.

Nella seconda parte, per tenere piccolo il conteggio, si usano numeri speciali chiamati "periodi". L'idea è semplice: un numero intero che contiene tante volte il fattore 2, come 64 = 2×2×2×2×2×2, non può essere piccolo. I primi del conteggio diventano fattori dei periodi. Ma si sa che i periodi non sono troppo grandi, quindi nemmeno il conteggio può esserlo.

Per avere tanti fattori si ripete m volte un'operazione chiamata "sollevamento theta". È un po' come impilare strati, ma questa è solo un'analogia. Più strati danno più fattori, ma anche più errori. Un errore è circa "numero diviso m", l'altro è circa m. Il compromesso migliore è scegliere m vicino alla radice quadrata: per questo compare proprio "un mezzo".

Il ragionamento è lunghissimo: circa 17 milioni di righe scritte in Lean, un programma che controlla ogni passaggio. La comunità di Lean l'ha già verificato. Però Alpöge stesso ammette di non padroneggiarlo ancora del tutto. Ci vorrà tempo per spiegarlo bene.

### claude_full-L1-s06

*nota intera, spiegazione 7 di 8.* Fatti del livello: 4 sì, 1 in parte, 0 no (copertura 0,90) · errori 0 su 18 · analogie dichiarate 1 · segnalazioni del critico 2, errori introdotti 1 · 312 parole (limite 300) · Gulpease 60,7

I numeri primi (2, 3, 5, 7, 11…) sembrano sparsi a caso. Da più di un secolo i matematici sospettano che seguano invece una regola molto ordinata: si possono contare con un errore piccolissimo, circa la radice quadrata di quanto si conta. È l'ipotesi di Riemann. La versione "generalizzata" vale anche per i primi divisi in famiglie, per esempio quelli che finiscono per 1, 3, 7 o 9. Ogni famiglia ha una sua formula, chiamata funzione L, e la regola dice che certi suoi punti speciali, gli "zeri", stanno tutti su una stessa linea.

Levent Alpöge, lavorando con l'intelligenza artificiale Claude, dice di averlo dimostrato. L'idea ha tre passi.

Primo: se uno zero uscisse dalla linea, un certo conteggio dei primi diventerebbe troppo grande. Quindi basta dimostrare che quel conteggio resta piccolo.

Secondo: per tenerlo piccolo si costruiscono numeri speciali, presi da oggetti matematici molto avanzati. Ogni primo contato rende questi numeri divisibili una volta in più, ma si sa anche che i numeri non possono essere troppo grandi. Pensa a un numero divisibile per 2 dieci volte: vale almeno 1024. Un numero molto divisibile ma piccolo è impossibile, quindi i primi contati non possono essere troppi.

Terzo: il trucco si ripete molte volte. Con un'analogia mia, è come costruire una torre: ogni piano aggiunge divisibilità, ma anche un po' di errore. Il numero di piani più conveniente è la radice quadrata di quanto si conta, e da lì viene proprio la "radice quadrata" della regola.

La dimostrazione è lunghissima: circa 17 milioni di righe scritte per Lean, un programma che controlla ogni passaggio. Nessuna persona l'ha letta tutta. In un giorno, però, la comunità di Lean l'ha ricontrollata con versioni indipendenti del programma e ha verificato che le definizioni usate siano quelle giuste. Le spiegazioni a parole sono ancora provvisorie. Alpöge stesso pensa che presto la dimostrazione diventerà molto più corta.

### claude_full-L1-s07

*nota intera, spiegazione 8 di 8.* Fatti del livello: 3 sì, 2 in parte, 0 no (copertura 0,80) · errori 0 su 17 · analogie dichiarate 2 · segnalazioni del critico 0, errori introdotti 0 · 305 parole (limite 300) · Gulpease 61,1

I numeri primi, come 2, 3, 5, 7 e 11, sono, per fare un paragone, i mattoncini da cui si ottengono tutti gli altri numeri moltiplicando. L'ipotesi di Riemann generalizzata dice, in sostanza, che i primi sono distribuiti nel modo più ordinato possibile, anche dentro file come 1, 4, 7, 10, 13… A ogni fila corrisponde una funzione speciale, e la domanda diventa: i suoi "zeri" stanno tutti su una certa linea, quella chiamata "un mezzo"?

Levent Alpöge, lavorando con un'intelligenza artificiale chiamata Claude, dice di averlo dimostrato. L'idea si può raccontare in tre passi.

Primo: si fa una somma che conta i primi dando a ciascuno un peso. Se, su intervalli lunghi scelti con cura, questa somma non supera di molto la radice quadrata di x, allora nessuno zero può stare fuori dalla linea.

Secondo: per tenere a freno la somma si usano numeri speciali, chiamati "periodi". Il trucco è questo: un numero intero diverso da zero che si può dividere tante volte non può essere piccolo. Per esempio, se si divide dieci volte per 2, vale almeno 1024. Più la somma dei primi è grande, più il periodo risulta divisibile; ma il periodo non può essere troppo grande, e quindi nemmeno la somma.

Terzo: per ottenere ancora più divisibilità si ripete m volte un'operazione chiamata "sollevamento theta". Ripeterla però crea due errori: uno grande come x diviso m, l'altro grande come m. Come su un'altalena da tenere in equilibrio (è un'analogia), conviene scegliere m vicino alla radice di x. Con x = 100 e m = 10, i due errori valgono entrambi 10. Ecco da dove viene il "mezzo".

Servono moltissimi altri pezzi di matematica. Il programma Lean ha controllato la dimostrazione, che però è lunghissima: circa 17 milioni di righe. Per ora nessuna persona è riuscita a leggerla e a capirla tutta.

### claude_overview-L1-s00

*panoramica, spiegazione 1 di 8.* Fatti del livello: 3 sì, 1 in parte, 1 no (copertura 0,70) · errori 0 su 13 · analogie dichiarate 2 · segnalazioni del critico 1, errori introdotti 1 · 303 parole (limite 300) · Gulpease 64,1

I numeri primi, come 2, 3, 5, 7 e 11, sono i mattoncini con cui si costruiscono tutti gli altri numeri. Sembrano sparpagliati a caso. Per studiarli i matematici usano delle formule speciali, le funzioni L di Dirichlet, che contano i primi anche dentro file regolari come 1, 4, 7, 10, 13… Ogni formula ha dei "punti zero". Da più di cent'anni si pensa che stiano tutti allineati su una stessa riga: è l'ipotesi di Riemann generalizzata. Se fosse vera, sapremmo contare i primi quasi alla perfezione.

Levent Alpöge, lavorando con un'intelligenza artificiale, Claude, dice di averla dimostrata. L'idea di partenza è questa: se un punto zero uscisse dalla riga, una certa somma fatta sui numeri primi diventerebbe troppo grande. Quindi basta mostrare che quella somma resta piccola, circa come la radice quadrata di quanto si è contato (la radice quadrata di 100 è 10).

Per riuscirci si costruiscono numeri speciali che hanno due facce. Da una parte sono divisibili per moltissimo, e la somma sui primi entra in quel "moltissimo". Dall'altra si dimostra che non sono troppo grandi. Te lo spiego con un esempio più semplice, che è solo un paragone: un numero intero, diverso da zero e divisibile per 2, 3, 5 e 7, vale almeno 210. Non può essere molto divisibile e anche minuscolo. Questo tira e molla tiene la somma sotto controllo.

La divisibilità si guadagna ripetendo tante volte un'operazione chiamata "sollevamento theta". Anche qui uso un paragone: è come una bilancia. Con pochi passi resta grande un errore, con troppi ne cresce un altro. Il punto di equilibrio sta proprio alla radice quadrata.

La dimostrazione è lunghissima. Per questo è stata scritta per Lean, un programma che controlla ogni passaggio. Alpöge però resta prudente: dice di "credere" di averla trovata, e ora le persone devono capirla e semplificarla.

### claude_overview-L1-s01

*panoramica, spiegazione 2 di 8.* Fatti del livello: 2 sì, 3 in parte, 0 no (copertura 0,70) · errori 0 su 16 · analogie dichiarate 1 · segnalazioni del critico 1, errori introdotti 1 · 294 parole (limite 300) · Gulpease 61,4

I numeri primi, come 2, 3, 5, 7, 11, sono i mattoncini da cui si ottengono tutti gli altri numeri moltiplicando. Quasi duecento anni fa Dirichlet inventò delle funzioni speciali, le funzioni L, per studiare i primi che cadono in file come 1, 4, 7, 10, 13… Ogni funzione L ha dei punti in cui vale zero. La congettura che Levent Alpöge dice di aver dimostrato insieme a Claude afferma che, in una certa zona, tutti questi zeri stanno su un'unica linea retta.

Come ci si arriva? Alpöge guarda una somma che raccoglie i primi fino a un numero x. Se uno zero stesse fuori dalla linea, questa somma prima o poi diventerebbe troppo grande. Basta quindi mostrare che resta piccola, più o meno quanto la radice quadrata di x: così lo zero fuori posto non può esistere.

Per tenere a bada la somma usa dei numeri speciali, chiamati periodi, che vengono da oggetti matematici molto simmetrici. Vale una regola: un numero intero divisibile per tantissimi primi non può essere anche piccolo. La somma sui primi dice quanto i periodi sono divisibili, mentre altri strumenti dicono quanto sono grandi. Confrontando le due cose, la somma resta sotto controllo.

Per guadagnare divisibilità, quegli oggetti vengono «sollevati» più volte da un posto all'altro. Per fare un'analogia, è come salire una scala. Con m gradini restano due errori, grandi circa x diviso m e m. Se x vale 100 e scegli 10 gradini, entrambi gli errori valgono 10, cioè la radice quadrata di 100. Da qui viene il «mezzo» della linea.

La dimostrazione è lunghissima e usa moltissima matematica. Per ora esiste soprattutto come testo controllato dal computer con il programma Lean. Alpöge stesso dice di non padroneggiarne ancora ogni parte e vuole riscriverla in modo leggibile.

### claude_overview-L1-s02

*panoramica, spiegazione 3 di 8.* Fatti del livello: 2 sì, 2 in parte, 1 no (copertura 0,60) · errori 0 su 17 · analogie dichiarate 1 · segnalazioni del critico 0, errori introdotti 0 · 307 parole (limite 300) · Gulpease 58,6

I numeri primi, come 2, 3, 5, 7, 11, sono i mattoncini con cui si costruiscono tutti gli altri numeri. Quasi due secoli fa Dirichlet inventò delle "macchine" matematiche, le funzioni L, per studiare i primi che compaiono in file come 1, 4, 7, 10, 13… Ogni macchina ha dei punti speciali, chiamati zeri. L'ipotesi di Riemann generalizzata dice che tutti gli zeri interessanti stanno su una sola retta. Se è vera, sappiamo contare i primi di quelle file nel modo più preciso possibile.

Il 20 novembre 2026 il matematico Levent Alpöge ha annunciato di averla dimostrata insieme a Claude, un'intelligenza artificiale. La dimostrazione è scritta in Lean, un programma che controlla ogni passaggio. Puoi immaginarlo come un maestro severissimo che non lascia passare nessun errore.

Il primo passo è questo: se uno zero stesse fuori dalla retta, una certa somma che "conta" i primi diventerebbe ogni tanto troppo grande. Quindi basta mostrare che quella somma resta piccola, più o meno quanto la radice quadrata di x.

Nel secondo passo Alpöge usa dei numeri speciali, costruiti da oggetti molto simmetrici. Vale una regola: un numero intero diverso da zero, se è divisibile per tantissimi primi, non può essere piccolo. La somma dei primi decide quanto sono divisibili questi numeri. Si sa però che non sono troppo grandi, e così anche la somma resta sotto controllo.

Per aumentare la divisibilità si ripete molte volte una trasformazione chiamata "sollevamento theta". Se la si ripete m volte, restano due errori: uno grande come x diviso m, l'altro grande come m. Per esempio, con x = 100 e m = 10 valgono tutti e due 10. Per questo si sceglie m vicino alla radice quadrata di x.

La dimostrazione è lunghissima e usa moltissima matematica. Alpöge ammette di non padroneggiarne ancora tutte le parti e spera che presto qualcuno la semplifichi.

### claude_overview-L1-s03

*panoramica, spiegazione 4 di 8.* Fatti del livello: 3 sì, 2 in parte, 0 no (copertura 0,80) · errori 0 su 18 · analogie dichiarate 1 · segnalazioni del critico 1, errori introdotti 0 · 306 parole (limite 300) · Gulpease 60,0

I numeri primi sono numeri come 2, 3, 5, 7, 11, divisibili solo per 1 e per sé stessi. Quasi duecento anni fa Dirichlet voleva capire se una fila come 1, 5, 9, 13, 17… (si aggiunge sempre 4) contiene infiniti primi. Per studiarla inventò delle funzioni speciali, le funzioni L. Queste funzioni in certi punti valgono zero, e quei punti decidono quanto ordinatamente sono sparsi i primi. L'ipotesi di Riemann generalizzata dice che tutti quegli zeri importanti stanno su una stessa linea. Levent Alpöge, lavorando con l'intelligenza artificiale Claude, dice di averlo dimostrato.

La dimostrazione ha due tappe. Nella prima basta mostrare che una certa somma fatta con i numeri primi, contati fino a un numero x, non diventa mai troppo grande: al massimo poco più della radice quadrata di x. Ragionamenti di matematici di molti anni fa trasformano questo controllo nel fatto che gli zeri stanno sulla linea.

La seconda tappa, la più difficile, serve a controllare la somma. Usa un fatto semplice: un numero intero diverso da zero che si può dividere per 2 cento volte è almeno 2 elevato alla 100, cioè enorme. Alpöge costruisce dei numeri speciali, chiamati periodi. Quante volte si possono dividere dipende dalla somma sui primi. Se si sa che questi numeri non sono troppo grandi, allora nemmeno la somma può esserlo. Per renderli sempre più divisibili, Alpöge ripete m volte un'operazione chiamata sollevamento theta.

Però restano due errori: uno diminuisce quando m cresce, l'altro aumenta. Per fare un'analogia, è come tenere in equilibrio un'altalena. Si sceglie m vicino alla radice quadrata di x, e così entrambi gli errori restano vicini a quella radice. Per questo nel risultato compare proprio «un mezzo».

La dimostrazione è lunghissima e usa moltissima matematica. Un programma, Lean, ne ha controllato ogni passaggio, ma i matematici la stanno ancora studiando per capirla davvero.

### claude_overview-L1-s04

*panoramica, spiegazione 5 di 8.* Fatti del livello: 2 sì, 3 in parte, 0 no (copertura 0,70) · errori 0 su 17 · analogie dichiarate 0 · segnalazioni del critico 1, errori introdotti 0 · 302 parole (limite 300) · Gulpease 61,4

I numeri primi, come 2, 3, 5, 7 e 11, sono i mattoncini con cui si costruiscono tutti gli altri numeri. Da quasi due secoli si sa che per capire come i primi si distribuiscono, anche in file come 1, 4, 7, 10, 13…, bisogna studiare certe funzioni speciali, le funzioni L. Ognuna ha dei "punti zero". L'ipotesi di Riemann generalizzata dice che tutti quelli importanti stanno su un'unica linea, quella del "mezzo". Il 20 novembre 2026 Levent Alpöge ha annunciato di averlo dimostrato insieme a Claude, un'intelligenza artificiale.

Come funziona la dimostrazione? Se uno zero stesse fuori dalla linea, una certa somma costruita con i primi diventerebbe troppo grande. Alpöge dimostra che quella somma resta sotto un "soffitto" (è un'immagine, non un termine tecnico), almeno su tratti lunghi a piacere. Questo basta per escludere zeri fuori posto.

Per costruire il soffitto usa un'idea semplice. Un numero intero diverso da zero che si può dividere per 2 dieci volte vale almeno 1024: tanta divisibilità significa che il numero non è piccolo. Alpöge costruisce numeri speciali, chiamati "periodi". Da un lato sono molto divisibili, e quanto lo sono dipende dai primi. Dall'altro non possono essere troppo grandi. Confrontando le due cose ottiene il soffitto. Per avere tanta divisibilità ripete m volte un'operazione chiamata "sollevamento theta", e ogni ripetizione ne aggiunge un po'.

C'è però un prezzo: restano due errori, uno grande circa x diviso m e l'altro circa m. Se x è un milione e si sceglie m uguale a mille, valgono entrambi mille, cioè la radice quadrata di x. Da qui viene quel "mezzo".

La dimostrazione è lunghissima e usa tantissima matematica. È stata controllata da un programma chiamato Lean. Alpöge pensa che verrà semplificata presto. Il matematico Robin Zhang ne ha scritto un primo riassunto e la chiama ancora "dimostrazione proposta".

### claude_overview-L1-s05

*panoramica, spiegazione 6 di 8.* Fatti del livello: 3 sì, 1 in parte, 1 no (copertura 0,70) · errori 0 su 17 · analogie dichiarate 1 · segnalazioni del critico 0, errori introdotti 0 · 306 parole (limite 300) · Gulpease 60,1

I numeri primi, come 2, 3, 5, 7 e 11, sono i mattoncini con cui si costruiscono tutti gli altri numeri. Sembrano sparsi a caso, e da 150 anni i matematici cercano di capire quanto possano essere disordinati. Esistono delle formule speciali, le funzioni L, che servono a studiare i primi, anche a gruppi: per esempio solo quelli che finiscono per 3. L'ipotesi di Riemann generalizzata dice che certi punti di queste formule, chiamati zeri, stanno tutti su una stessa linea, quella del numero un mezzo. Se è vera, i primi sono ordinati nel modo migliore possibile.

Levent Alpöge, lavorando con un'intelligenza artificiale, Claude, annuncia di averla dimostrata. L'idea di partenza è semplice: un numero intero diverso da zero che è divisibile per 2, 3, 5 e 7 vale almeno 210. Più un numero è divisibile, più deve essere grande. Alpöge costruisce numeri speciali, ricavati da oggetti molto simmetrici, la cui divisibilità dipende da conti sui primi. Se mostri che quei numeri non sono troppo grandi, allora nemmeno quei conti sui primi possono sbagliare di molto. E conti abbastanza precisi bastano a tenere gli zeri sulla linea.

Per rendere i numeri più divisibili, Alpöge li trasforma molte volte di seguito, con un passaggio chiamato sollevamento theta. Qui serve un equilibrio: con poche ripetizioni resta un errore grande, con troppe ne nasce un altro. È un po' come cercare il punto giusto su un'altalena a bilico (è solo un paragone). Claude ha suggerito il numero giusto di ripetizioni: la radice quadrata della lunghezza del conto. È da questa radice quadrata che spunta l'un mezzo.

La dimostrazione è lunghissima e usa moltissima matematica diversa. È stata scritta per Lean, un programma che controlla ogni passaggio. Il matematico Robin Zhang ne ha scritto un primo riassunto e la chiama ancora «dimostrazione proposta». Alpöge stesso vuole capirla meglio e semplificarla.

### claude_overview-L1-s06

*panoramica, spiegazione 7 di 8.* Fatti del livello: 2 sì, 3 in parte, 0 no (copertura 0,70) · errori 0 su 14 · analogie dichiarate 2 · segnalazioni del critico 1, errori introdotti 1 · 328 parole (limite 300) · Gulpease 64,1

Sai che cosa sono i numeri primi: 2, 3, 5, 7, 11… sono i mattoncini con cui si costruiscono tutti gli altri numeri. Prendi ora una fila come 1, 4, 7, 10, 13…, in cui si va avanti sempre di 3. Quasi duecento anni fa Dirichlet dimostrò che in file come questa i primi non finiscono mai. Per studiarle inventò delle funzioni speciali, le funzioni L. Ognuna ha dei «punti zero». Da quasi 150 anni si sospetta che tutti gli zeri importanti stiano su un'unica linea retta. Se è così, i primi sono distribuiti nel modo più ordinato possibile. È questo che Levent Alpöge, lavorando con l'intelligenza artificiale Claude, dice di aver dimostrato.

La dimostrazione ha due parti. La prima è conosciuta da tempo: se conti i primi in un modo speciale e il conto non supera mai «circa la radice quadrata» di quanto sei arrivato lontano, nessuno zero può stare fuori dalla linea.

La seconda parte, quella nuova, serve a tenere basso quel conto. Si basa su un fatto vero: un numero intero, diverso da zero, che si può dividere per 2 dieci volte di fila vale almeno 1024. Quindi un numero molto divisibile non può essere piccolo. Alpöge costruisce numeri speciali, ricavati da oggetti matematici difficilissimi, la cui divisibilità dipende dal conto dei primi. Sapendo che questi numeri non sono troppo grandi, ottiene che il conto dei primi resta basso. Per renderli più divisibili ripete molte volte un passaggio chiamato «sollevamento theta».

Ripeterlo ha però un prezzo: compaiono due errori. Uno cala se ripeti di più, l'altro cresce. Come per i due piatti di una bilancia (è solo un paragone), conviene scegliere il punto di mezzo. Da quella scelta viene proprio la «radice quadrata».

La dimostrazione è lunghissima. Un programma, Lean, ne ha controllato ogni passo, come un arbitro severissimo (anche questo è un paragone). Lo stesso Alpöge però dice di non capirne ancora bene tutte le parti, e gli altri matematici la stanno ancora studiando.

### claude_overview-L1-s07

*panoramica, spiegazione 8 di 8.* Fatti del livello: 1 sì, 4 in parte, 0 no (copertura 0,60) · errori 0 su 18 · analogie dichiarate 1 · segnalazioni del critico 1, errori introdotti 1 · 302 parole (limite 300) · Gulpease 62,7

I numeri primi (2, 3, 5, 7, 11…) sembrano sparsi a caso. Esistono però delle «macchine» matematiche, le funzioni L di Dirichlet, che aiutano a contarli, anche divisi in file come 1, 11, 21, 31… Ogni macchina ha dei punti speciali, gli «zeri». L'ipotesi dice che gli zeri importanti stanno tutti su un'unica linea. Levent Alpöge, lavorando con l'intelligenza artificiale Claude, dice di averlo dimostrato.

Il primo passo è questo. Si sommano i primi fino a un numero grande x, ognuno con un suo peso, e si toglie il risultato atteso. Se l'avanzo resta più piccolo di circa la radice quadrata di x (per un milione, circa mille), nessuno zero può stare fuori dalla linea. Basta mostrarlo su certi intervalli, purché se ne trovino di sempre più lontani.

Il secondo passo è il trucco: un numero intero che si divide tante volte per tanti primi non può essere piccolo. Con strumenti molto avanzati si costruiscono numeri speciali, detti «periodi». Quante volte si dividono per i primi dipende proprio da quella somma. Poi si dimostra che questi numeri non sono troppo grandi. Mettendo insieme le due cose, l'avanzo resta sotto controllo.

Per avere più divisibilità si ripete m volte un'operazione chiamata «sollevamento theta». Restano due errori: uno grande circa x/m, l'altro circa m. Un'analogia: è come tagliare una torta, dove poche fette sono troppo grosse e troppe fette fanno troppe briciole. Il punto giusto è m vicino alla radice di x, ed ecco da dove viene la radice quadrata.

La dimostrazione è lunghissima ed è stata controllata da Lean, un programma che verifica ogni passaggio. Però Alpöge stesso dice di non padroneggiare ancora tutta la matematica che contiene e di doverla ancora scrivere bene per le persone. Il matematico Robin Zhang la chiama «dimostrazione proposta». Gli esperti avranno bisogno di tempo per capirla.

## Livello 2: uno studente di liceo (al più 600 parole)

### claude_full-L2-s00

*nota intera, spiegazione 1 di 8.* Fatti del livello: 9 sì, 5 in parte, 0 no (copertura 0,82) · errori 0 su 38 · analogie dichiarate 0 · segnalazioni del critico 1, errori introdotti 1 · 619 parole (limite 600) · Gulpease 57,1

Nel 1859 Riemann collegò la distribuzione dei numeri primi agli zeri di una funzione, la zeta, e ipotizzò che quelli "interessanti" stessero tutti su una retta: quella dei numeri con parte reale 1/2. Le funzioni L di Dirichlet sono una famiglia di funzioni simili, che servono a studiare i primi nelle progressioni aritmetiche. L'ipotesi di Riemann generalizzata afferma che anche i loro zeri stanno su quella retta. Levent Alpöge sostiene di averla dimostrata lavorando con Claude, e il caso classico della zeta ne è un caso particolare.

La dimostrazione procede in tre passi.

Il primo passo collega gli zeri ai primi. Alpöge studia una somma "pesata" sui primi e sulle loro potenze fino a x, alla quale toglie la parte prevedibile. Se esistesse uno zero fuori posto, a destra della retta, questa somma prima o poi crescerebbe troppo in fretta. Basta quindi mostrare che resta sotto x^(1/2+η), con η piccolo a piacere. Serve anche poco: un limite solo dall'alto, e solo su certi intervalli arbitrariamente lontani. Combinando le somme di più funzioni L con coefficienti positivi, gli zeri non possono cancellarsi a vicenda. Le derivate di ordine altissimo permettono poi di concentrarsi su un solo intervallo. Gli zeri a sinistra della retta si escludono per simmetria.

Il secondo passo limita la somma usando la divisibilità. Un esempio semplice: un intero non nullo divisibile per 2¹⁰ vale almeno 1024. Una versione molto più raffinata di questa idea vale per i numeri algebrici: se un numero è molto divisibile, non può essere piccolo. Alpöge costruisce numeri speciali, i "periodi automorfi", che sono integrali di funzioni con enormi simmetrie. Dimostra che la loro divisibilità per i primi è controllata proprio dalla somma sui primi, e stima separatamente quanto questi numeri possono essere grandi. Se la somma fosse troppo grande, i periodi risulterebbero troppo divisibili rispetto alla loro grandezza. Da qui si ricava il limite superiore cercato.

Il terzo passo consiste nel ripetere la costruzione per guadagnare divisibilità. Si usano i "sollevamenti theta", che trasportano una funzione simmetrica da un gruppo a un altro, e li si ripete m volte. Alpöge propone un'analogia con il metodo di Stepanov per le curve sui campi finiti, dove si costruisce un polinomio che si annulla "molte volte" in certi punti. Qui ogni sollevamento corrisponde a un ordine di annullamento in più. Però più sollevamenti portano anche più errori. Gli errori principali hanno grandezza circa x/m e m: il primo cala al crescere di m, il secondo aumenta. Il compromesso migliore è m vicino a √x, e allora entrambi gli errori valgono circa √x. Da qui viene l'esponente 1/2. Alpöge racconta che fu Claude a suggerire questa lunghezza della catena.

Perché tutto funzioni, i termini principali devono cancellarsi esattamente. Per verificarlo servono risultati classici come la formula di Chowla–Selberg, la formula di Weyl e la formula di massa di Siegel. Altre parti usano geometria aritmetica, rappresentazioni di Galois, teoria di Iwasawa e perfino insiemi di interi senza progressioni aritmetiche di tre termini (Behrend).

Quanto è affidabile il risultato? La dimostrazione esiste soprattutto come codice Lean, un linguaggio in cui un computer controlla ogni passaggio logico, e conta circa 17 milioni di righe. Alpöge ha scelto di non pubblicare un testo di oltre 250.000 pagine generato dall'IA, perché lo giudica illeggibile. Secondo la nota di Robin Zhang, in un solo giorno le comunità Lean e Mathlib hanno verificato il codice con implementazioni indipendenti e hanno controllato che le definizioni coincidano con quelle standard. La comprensione umana, però, è appena iniziata. Zhang avverte che il suo riassunto è stato scritto in gran parte con l'IA e potrebbe non rispecchiare fedelmente il codice. Lo stesso Alpöge ammette di non padroneggiare ancora tutto l'argomento e si aspetta che venga molto semplificato.

### claude_full-L2-s01

*nota intera, spiegazione 2 di 8.* Fatti del livello: 8 sì, 6 in parte, 0 no (copertura 0,79) · errori 0 su 37 · analogie dichiarate 0 · segnalazioni del critico 0, errori introdotti 0 · 618 parole (limite 600) · Gulpease 52,7

Le funzioni L di Dirichlet sono una famiglia di funzioni legate ai numeri primi, che comprende la celebre funzione zeta di Riemann. L'ipotesi di Riemann generalizzata afferma che tutti i loro zeri "interessanti", cioè quelli nella striscia in cui la parte reale è compresa tra 0 e 1, stanno esattamente sulla retta di parte reale 1/2. Alpöge dichiara di averla dimostrata insieme a Claude. La dimostrazione include anche il caso della zeta, cioè l'ipotesi di Riemann classica.

Il primo passo consiste nel passare dagli zeri ai primi. Invece di cercare direttamente gli zeri, la dimostrazione studia somme pesate sulle potenze dei numeri primi, dalle quali si sottrae un "termine principale". Un passaggio classico, la trasformata di Mellin, fa sì che uno zero fuori posto si traduca in una crescita troppo rapida di queste somme. Basta allora provare che la somma resta sotto circa √x, cioè sotto x^(1/2+η) per ogni η>0. Non serve nemmeno che valga ovunque: bastano intervalli arbitrariamente lontani. Le somme di più funzioni L vengono combinate con coefficienti positivi, così gli zeri non possono cancellarsi a vicenda. Derivando molte volte si isola un eventuale zero fuori posto e si arriva a una contraddizione. Per la metà sinistra della striscia basta la simmetria data dall'equazione funzionale.

L'idea centrale viene da un principio della teoria dei numeri: un numero algebrico non nullo, molto divisibile per i primi, non può essere piccolo in tutte le sue "misure di grandezza". Un esempio semplificato, che non è l'argomento vero: un intero non nullo divisibile per 2¹⁰ vale almeno 1024 in valore assoluto. La dimostrazione costruisce numeri speciali, detti periodi automorfi, che sono integrali di oggetti molto simmetrici chiamati forme automorfe. La loro divisibilità per i primi è controllata proprio dalle somme sui primi. Se si sa che questi periodi non sono troppo grandi, allora nemmeno le somme possono esserlo.

Per ottenere abbastanza divisibilità, l'argomento ripete m volte un'operazione chiamata sollevamento theta, che trasporta una forma automorfa da un gruppo di simmetrie a un altro. Alpöge propone un'analogia con il metodo di Stepanov per contare i punti di una curva su un campo finito. Lì si costruisce un polinomio che si annulla con "molteplicità" alta nei punti da contare; qui il numero di sollevamenti fa la parte della molteplicità. Ogni sollevamento però ha un costo: gli errori finali hanno dimensioni circa x/m e m. Il compromesso migliore è m vicino a √x, ed è proprio da qui che nasce l'esponente 1/2. Secondo Alpöge, fu Claude a suggerire questa lunghezza della catena.

Il resto della dimostrazione serve a controllare gli errori e richiede moltissima matematica: geometria aritmetica per misurare i "reticoli" di forme automorfe, rappresentazioni di Galois e coomologia per tenere a bada i denominatori, teoria di Iwasawa, e persino una costruzione di Behrend di insiemi di interi senza progressioni aritmetiche di tre termini. Un dettaglio notevole è che le costanti ricavate dai periodi coincidono esattamente con il termine principale sottratto all'inizio.

Quanto allo stato della dimostrazione, oggi esiste solo come codice per l'assistente di dimostrazione Lean, circa 17 milioni di righe. Alpöge ha scelto di non pubblicare un testo di oltre 250.000 pagine generato dall'IA, giudicandolo illeggibile. Secondo la nota di Robin Zhang, in un giorno le comunità di Lean e Mathlib hanno verificato la prova con implementazioni indipendenti del verificatore. Hanno anche controllato che le definizioni usate corrispondano a quelle matematiche standard.

Nessuno, però, ha ancora letto e compreso l'argomento per intero. La ricostruzione di Zhang, da cui proviene la descrizione qui sopra, è stata scritta in gran parte con un'IA, e lui stesso avverte che potrebbe non rispecchiare fedelmente il codice. Alpöge ammette di non padroneggiare ancora tutte le parti e si aspetta che la dimostrazione venga presto molto semplificata.

### claude_full-L2-s02

*nota intera, spiegazione 3 di 8.* Fatti del livello: 8 sì, 6 in parte, 0 no (copertura 0,79) · errori 1 su 41 · analogie dichiarate 1 · segnalazioni del critico 0, errori introdotti 0 · 657 parole (limite 600) · Gulpease 57,0

Si tratta di una dimostrazione annunciata il 20 novembre 2026 da Levent Alpöge, costruita insieme a Claude. Riguarda l'ipotesi di Riemann generalizzata per le funzioni L di Dirichlet. Queste funzioni nascono dallo studio dei numeri primi nelle progressioni aritmetiche, come 1, 5, 9, 13, …. L'enunciato dice che, per ogni carattere di Dirichlet primitivo χ, tutti gli zeri di L(s, χ) nella striscia 0 < Re(s) < 1 stanno sulla retta Re(s) = 1/2. Il caso più semplice di queste funzioni è la zeta di Riemann, quindi la dimostrazione comprende anche l'ipotesi di Riemann classica. Il senso concreto è questo: gli zeri controllano quanto il conteggio dei primi può sbagliare rispetto alla previsione, e stare su quella retta significa che l'errore è il più piccolo possibile.

Alpöge ha diffuso soltanto il codice Lean, un linguaggio in cui un computer controlla ogni passaggio logico. Sono circa 17 milioni di righe. Secondo la nota di Robin Zhang, in un solo giorno le comunità Lean e Mathlib hanno verificato la dimostrazione con implementazioni indipendenti del controllore. Hanno anche controllato che le definizioni usate coincidano con quelle standard. Nessun essere umano ha però letto l'argomento per intero. Il riassunto leggibile è quello di Zhang, scritto in gran parte da un'IA, e lui stesso avverte che potrebbe non tradurre fedelmente il codice.

La dimostrazione ha due parti. Nella prima il problema degli zeri diventa un problema di primi. Si considera una somma pesata sulle potenze dei primi, indicata con 𝒢_ψ(x). Se esistesse uno zero a destra della retta critica, questa somma crescerebbe più in fretta di circa √x. Basta quindi dimostrare che 𝒢_ψ(x) ≤ x^{1/2+η}, per η piccolo a piacere. Non serve dimostrarlo per ogni x: bastano intervalli arbitrariamente lontani, del tipo [Y, Y^{3/2}]. Due accorgimenti rendono il passaggio possibile. La somma combina più funzioni L con coefficienti positivi, quindi zeri diversi non possono cancellarsi a vicenda. Inoltre si deriva molte volte una trasformata della somma, così da concentrare l'attenzione su un solo intervallo. Gli zeri a sinistra della retta si escludono per simmetria, grazie all'equazione funzionale.

La seconda parte, molto più lunga, dimostra quella disuguaglianza. Il punto di partenza è un fatto aritmetico: un intero algebrico non nullo che è molto divisibile per molti primi non può avere tutte le sue "grandezze" piccole. Un'analogia con gli interi ordinari: un numero non nullo divisibile per 2¹⁰·3⁵ vale almeno 2¹⁰·3⁵ in valore assoluto. Alpöge costruisce numeri speciali, chiamati periodi automorfi, la cui divisibilità per i primi codifica proprio la somma sui primi. Se si riesce a limitare dall'alto la loro grandezza, si limita anche la somma.

Per ottenere abbastanza divisibilità si ripete m volte un'operazione chiamata sollevamento theta, che trasporta funzioni da un gruppo di simmetrie a un altro. Ogni ripetizione aggiunge divisibilità. Le fonti stesse propongono un'analogia con il metodo di Stepanov per le curve sui campi finiti, dove si usa un polinomio che si annulla con molteplicità alta. Qui il numero m di sollevamenti fa la parte della molteplicità. Ripetere ha però un costo: i due errori principali hanno taglia circa x/m e m. La loro somma è minima per m ≈ √x, e da qui nasce l'esponente 1/2. Alpöge racconta che fu Claude a suggerire una catena di lunghezza √X.

Il resto serve a tenere sotto controllo ogni costante. I termini principali devono cancellarsi esattamente. Per questo entrano la formula di Chowla–Selberg sui periodi delle varietà abeliane, la formula delle dimensioni di Weyl e la formula di massa di Siegel. I "denominatori" che rovinerebbero la divisibilità si controllano con la coomologia di Galois, la teoria di Iwasawa e il sistema di Eulero di Kato. Servono poi la geometria dei reticoli e perfino una costruzione di Behrend di insiemi di interi privi di progressioni aritmetiche di tre termini.

Alpöge stesso ritiene che l'argomento contenga scelte poco ottimali e che verrà presto molto semplificato. Oggi è una dimostrazione verificata dalla macchina, ma ancora in attesa di essere davvero capita dagli esseri umani.

### claude_full-L2-s03

*nota intera, spiegazione 4 di 8.* Fatti del livello: 6 sì, 8 in parte, 0 no (copertura 0,71) · errori 0 su 36 · analogie dichiarate 0 · segnalazioni del critico 0, errori introdotti 0 · 599 parole (limite 600) · Gulpease 57,5

Dirichlet, nell'Ottocento, introdusse delle funzioni L(s, χ), una per ogni "carattere" χ, per studiare i numeri primi nelle progressioni aritmetiche (come 1, 5, 9, 13, …). L'ipotesi di Riemann generalizzata afferma che tutti gli zeri di queste funzioni nella striscia 0 < Re(s) < 1 stanno sulla retta Re(s) = 1/2. Il caso più semplice è la funzione zeta, quindi l'ipotesi di Riemann classica è inclusa. Sapere dove stanno questi zeri dà un controllo ottimale sul conteggio dei primi.

Prima, un avvertimento. Alpöge ha pubblicato solo il codice Lean, circa 17 milioni di righe. Non ha diffuso un'esposizione di oltre 250.000 pagine generata dall'IA. Secondo la nota preliminare di Robin Zhang, in un giorno le comunità Lean e Mathlib hanno verificato la dimostrazione con implementazioni indipendenti e hanno controllato che le definizioni coincidano con quelle standard. Nessun essere umano ha però letto l'argomento per intero. Zhang avverte inoltre che il suo riassunto, scritto in buona parte da un'IA, potrebbe non rispecchiare fedelmente il codice. Quello che segue è lo schema di quel riassunto.

Primo passo: dagli zeri ai primi. Si considera una somma pesata sulle potenze dei primi fino a x, in cui ogni pᵏ conta log p, e se ne toglie il "termine principale" prevedibile. Uno zero fuori dalla retta critica farebbe crescere questa somma troppo in fretta. Basta quindi dimostrare che resta sotto circa x^(1/2), anche solo dall'alto e solo su certi intervalli arbitrariamente lontani. I coefficienti positivi della combinazione impediscono agli zeri di funzioni diverse di cancellarsi a vicenda. Derivando molte volte una trasformata della somma si isola un singolo intervallo. Gli zeri a sinistra della retta si escludono per simmetria, con l'equazione funzionale.

Secondo passo: il cuore. Si parte da un fatto elementare: un intero non nullo divisibile per molti primi non può essere piccolo. Se è divisibile per 2¹⁰, per esempio, vale almeno 1024 in valore assoluto. La dimostrazione costruisce dei numeri detti "periodi", integrali di forme automorfe (funzioni con moltissime simmetrie). Mostra poi che la loro divisibilità per i primi contiene proprio la somma del primo passo, mentre la loro grandezza si stima con altri strumenti. Confrontando "quanto sono divisibili" con "quanto sono grandi" si ottiene un limite superiore alla somma.

Per accumulare abbastanza divisibilità si applica m volte di fila il "sollevamento theta", che trasporta una forma da un gruppo di simmetrie a un altro più grande. Ogni sollevamento aggiunge divisibilità. Alpöge propone un'analogia con il metodo di Stepanov per contare i punti di una curva su un campo finito. Lì si costruisce un polinomio che si annulla con molteplicità alta; qui il numero di sollevamenti fa la parte della molteplicità. Le costanti di formule classiche (Chowla–Selberg, Weyl, formula di massa di Siegel) riproducono esattamente il termine principale sottratto all'inizio.

Perché proprio 1/2? Gli errori principali valgono circa x/m e m. Aumentare i sollevamenti riduce il primo errore ma fa crescere il secondo. La somma x/m + m è minima per m ≈ √x, e allora entrambi gli errori valgono circa √x = x^(1/2). Così il valore della retta critica nasce da un bilanciamento elementare. Alpöge racconta che fu Claude a suggerire una catena di lunghezza √X.

Il resto è controllo degli errori, e richiede moltissima matematica. Servono la coomologia di Galois e la teoria di Iwasawa per i "denominatori" che compaiono lungo il percorso, e la geometria di Arakelov per le stime di grandezza. Serve perfino la costruzione di Behrend di insiemi senza progressioni aritmetiche di tre termini, usata per scegliere certi parametri. Alpöge stesso pensa di aver fatto scelte poco ottimali e si aspetta che l'argomento venga presto molto semplificato.

### claude_full-L2-s04

*nota intera, spiegazione 5 di 8.* Fatti del livello: 6 sì, 6 in parte, 2 no (copertura 0,64) · errori 0 su 35 · analogie dichiarate 0 · segnalazioni del critico 0, errori introdotti 0 · 586 parole (limite 600) · Gulpease 53,2

Le funzioni L di Dirichlet sono parenti della funzione zeta di Riemann: ognuna aiuta a contare i numeri primi dentro una progressione aritmetica come 1, 5, 9, 13… L'ipotesi di Riemann generalizzata afferma che tutti i loro zeri "interessanti", cioè quelli nella striscia 0 < Re(s) < 1, stanno esattamente sulla retta Re(s) = 1/2.

Il 20 novembre 2026 Levent Alpöge ha annunciato una dimostrazione costruita insieme a Claude. L'ha presentata solo nel linguaggio di verifica Lean: circa 17 milioni di righe di codice. Secondo la nota di Robin Zhang, già il giorno dopo le comunità Lean e Mathlib l'avevano verificata con implementazioni indipendenti del verificatore. Avevano anche controllato che le definizioni usate coincidessero con quelle standard. Nessun essere umano però l'ha ancora letta per intero. La ricostruzione a parole che segue viene dalla nota di Zhang, scritta in gran parte con l'aiuto di un'IA, e Zhang stesso avverte che potrebbe non essere una traduzione fedele del codice.

**Primo passo: dai primi agli zeri.** Si considera una somma pesata sulle potenze dei primi fino a x, da cui si toglie il suo "termine principale" prevedibile. Una trasformazione, la trasformata di Mellin, converte questa somma in una funzione i cui poli corrispondono proprio agli zeri delle funzioni L. Se uno zero stesse a destra della retta critica, la somma dovrebbe crescere troppo in fretta. Basta quindi dimostrare un tetto: la somma non supera x^(1/2+η), con η piccolo quanto si vuole. Curiosamente il tetto serve solo dall'alto, e solo su certi intervalli [Y, Y^(3/2)] arbitrariamente lontani. Derivando la trasformata moltissime volte si concentra l'informazione su un singolo intervallo. La simmetria data dall'equazione funzionale sistema poi l'altra metà della striscia.

**Secondo passo, il cuore: ottenere il tetto.** Si parte da un fatto elementare: se un intero non nullo è divisibile per 2¹⁰⁰, allora vale almeno 2¹⁰⁰ in valore assoluto. Essere molto divisibili ed essere piccoli non vanno d'accordo. La dimostrazione costruisce numeri algebrici speciali, i "periodi automorfi", che sono integrali di funzioni molto simmetriche dette forme automorfe. Su questi numeri dimostra due cose:
- sono divisibili per potenze di primi in quantità legata proprio alla somma sui primi;
- non possono essere troppo grandi.

Mettendo insieme le due cose, la somma sui primi non può essere troppo grande.

Per ottenere abbastanza divisibilità si ripete m volte un'operazione chiamata sollevamento theta, che trasporta una forma automorfa da un gruppo di simmetrie a un altro. Ogni ripetizione aggiunge divisibilità. Alpöge propone un'analogia, che è appunto solo un'analogia: nella dimostrazione di Stepanov per il caso dei "campi di funzioni" si usa un polinomio che si annulla con molteplicità alta, e qui il numero m di sollevamenti fa la parte della molteplicità.

Ogni sollevamento però ha un costo, perché gli spazi crescono e con loro gli errori. Alla fine restano due errori principali, grandi circa x/m e m. Se m è piccolo domina il primo, se è grande domina il secondo. L'equilibrio si ottiene con m vicino a √x, e allora entrambi valgono circa √x. Ecco da dove viene l'esponente 1/2.

Il resto è un enorme lavoro di contabilità:
- misurare i "volumi" di certi reticoli con la geometria aritmetica;
- evitare che, scomponendo, compaiano denominatori che cancellino la divisibilità guadagnata, usando la coomologia di Galois e tecniche della scuola di Wiles;
- scegliere con cura campi numerici e parametri, sfruttando perfino la costruzione di Behrend di insiemi di interi senza progressioni aritmetiche di tre termini.

Alpöge scrive di aspettarsi semplificazioni drastiche. Ammette anche di non padroneggiare ancora alcune parti trovate da Claude.

### claude_full-L2-s05

*nota intera, spiegazione 6 di 8.* Fatti del livello: 6 sì, 7 in parte, 1 no (copertura 0,68) · errori 0 su 37 · analogie dichiarate 0 · segnalazioni del critico 0, errori introdotti 0 · 653 parole (limite 600) · Gulpease 58,7

L'annuncio di Levent Alpöge riguarda le funzioni L di Dirichlet. Dirichlet le inventò per studiare i numeri primi nelle progressioni aritmetiche, come 1, 5, 9, 13, … Ognuna è costruita a partire da un "carattere", cioè una funzione periodica che distingue una progressione dall'altra. L'ipotesi di Riemann generalizzata afferma che tutti gli zeri di queste funzioni nella "striscia critica" (parte reale tra 0 e 1) stanno esattamente sulla retta di parte reale 1/2. Il caso più semplice è l'ipotesi di Riemann originale, che quindi è inclusa. Questi zeri determinano di quanto i primi possono deviare dalla loro distribuzione media.

Il primo passo traduce gli zeri in somme sui primi. Si prende una somma pesata sulle potenze dei primi fino a x e le si sottrae il suo "termine principale". Uno zero fuori dalla retta farebbe crescere questa somma corretta più di √x. Basta quindi dimostrare che resta sotto x^(1/2+η), per ogni η positivo piccolo. Il compito è facilitato da due fatti. Serve solo una stima dall'alto. E serve solo su certi intervalli [Y, Y^(3/2)], scelti arbitrariamente lontani: un argomento classico di analisi complessa, che deriva molte volte una trasformata, basta comunque a scovare uno zero. Le somme di più caratteri vengono combinate con coefficienti positivi, così zeri in comune non possono cancellarsi tra loro. Gli zeri a sinistra della retta si escludono per simmetria, grazie all'equazione funzionale.

Il cuore della dimostrazione parte da un'idea elementare. Un intero diverso da zero e divisibile per 2¹⁰ e per 3⁵ vale almeno 2¹⁰·3⁵ in valore assoluto. Per i numeri algebrici vale una versione generale, la "formula del prodotto": un numero molto divisibile per i primi non può essere piccolo in tutti i modi in cui lo si misura. Alpöge usa numeri speciali, i periodi automorfi. Sono integrali di "forme automorfe", funzioni dotate di enormi simmetrie. La loro divisibilità per i primi contiene proprio la somma sui primi che ci interessa, mentre la loro grandezza si sa stimare dall'alto. Confrontando divisibilità e grandezza si ottiene un limite superiore per la somma.

Per accumulare divisibilità si ripete m volte un'operazione chiamata sollevamento theta, che trasporta una forma automorfa da un gruppo di simmetrie a un altro. Alpöge propone un'analogia con un metodo di Stepanov, nato per contare i punti di curve su campi finiti, in cui si costruisce un polinomio che si annulla "molte volte" in certi punti. Il numero di sollevamenti m fa la parte di quel numero di annullamenti. Ogni sollevamento però ha un costo. I due errori principali valgono circa x/m e m. Qui c'è un esercizio da liceo: x/m + m è minimo per m = √x, e allora vale 2√x. Ecco da dove viene l'esponente 1/2. Alpöge racconta che fu proprio Claude a suggerire una catena di sollevamenti lunga √X.

Far tornare i conti richiede moltissima matematica. Il termine principale deve ricomparire con le costanti esatte, e qui entrano i periodi di varietà abeliane speciali (formula di Chowla–Selberg). I volumi dei reticoli di forme si stimano con la geometria aritmetica. I "denominatori" che nascono strada facendo si controllano con le rappresentazioni di Galois, usando anche gli strumenti della dimostrazione di Wiles dell'ultimo teorema di Fermat e la teoria di Iwasawa. Serve persino una costruzione di Behrend di insiemi di interi privi di progressioni aritmetiche di tre termini.

Bisogna però essere onesti su cosa sappiamo. La dimostrazione esiste come codice Lean di circa 17 milioni di righe. Secondo la nota di Robin Zhang, le comunità Lean e Mathlib l'hanno verificata in un giorno, con implementazioni indipendenti, controllando anche che le definizioni coincidano con quelle standard. Nessun essere umano, però, l'ha letta per intero. Alpöge non ha diffuso la versione in linguaggio naturale, oltre 250.000 pagine generate dall'IA. Il riassunto di Zhang, su cui si basa questa spiegazione, è in gran parte scritto da un'IA, e Zhang stesso non garantisce che rispecchi fedelmente il codice. Alpöge si aspetta che arrivino presto dimostrazioni molto più brevi.

### claude_full-L2-s06

*nota intera, spiegazione 7 di 8.* Fatti del livello: 9 sì, 4 in parte, 1 no (copertura 0,79) · errori 0 su 36 · analogie dichiarate 1 · segnalazioni del critico 0, errori introdotti 0 · 627 parole (limite 600) · Gulpease 57,5

I numeri primi sembrano sparsi a caso, ma la loro distribuzione è governata da certe funzioni dette *funzioni L*. Già Dirichlet, nell'Ottocento, le usò per studiare i primi nelle progressioni aritmetiche, come 1, 5, 9, 13, … L'ipotesi di Riemann generalizzata afferma che tutti gli zeri "interessanti" di queste funzioni, cioè quelli nella striscia 0 < Re(s) < 1, stanno esattamente sulla retta Re(s) = 1/2. Levent Alpöge sostiene di averla dimostrata insieme a Claude.

Il primo passo collega gli zeri ai primi. Si costruisce una somma pesata sulle potenze dei numeri primi fino a x, a cui si sottrae un "termine principale" prevedibile. Ogni zero lascia un'impronta in questa somma. Per analogia, si può pensarlo come un'eco: uno zero a destra della retta critica farebbe crescere la somma più del dovuto. Basta quindi dimostrare che la somma non supera all'incirca √x (precisamente x^(1/2+η), per ogni η > 0). La stima non serve nemmeno ovunque: bastano intervalli arbitrariamente grandi, e solo dall'alto. Le somme relative a funzioni L diverse vengono combinate con coefficienti positivi, così i loro zeri non possono cancellarsi a vicenda. La metà sinistra della striscia si sistema con una simmetria che le funzioni L già possiedono, l'equazione funzionale. Questa parte usa idee classiche, come quelle di Landau e di Turán.

Il secondo passo mette a confronto divisibilità e grandezza. L'idea chiave è semplice: un intero diverso da zero e divisibile per 2¹⁰⁰ vale almeno 2¹⁰⁰. La versione raffinata di questo fatto, la "formula del prodotto", dice che un numero algebrico non nullo molto divisibile per i primi non può essere piccolo sotto tutte le sue misure di grandezza. La dimostrazione costruisce numeri speciali, detti *periodi automorfi*: sono integrali di forme automorfe, oggetti dotati di enormi simmetrie. La loro divisibilità contiene proprio la somma sui primi. Quindi, se si sa che questi numeri non sono troppo grandi, si ottiene un limite superiore per la somma.

Il terzo passo consiste nel ripetere la costruzione per guadagnare divisibilità. Si usa il "sollevamento theta", che trasporta una forma automorfa da un gruppo di simmetrie a un altro, e lo si ripete m volte: ogni passaggio aggiunge divisibilità. Alpöge lo paragona al metodo di Stepanov per contare i punti di una curva su un campo finito. Lì si costruisce un polinomio che si annulla con alta molteplicità; qui il numero m di sollevamenti fa la parte della molteplicità. Alpöge osserva che ottenere qualcosa di simile sugli interi è come "derivare i numeri interi". Più passaggi, però, ingrandiscono gli spazi e gli errori. Restano due errori principali, di grandezza x/m e m: il primo cala al crescere di m, il secondo cresce. Scegliendo m vicino a √x si bilanciano, ed entrambi valgono circa √x. È da qui che nasce l'esponente 1/2.

Attorno a questo nucleo c'è moltissima altra matematica. Per misurare le grandezze serve la geometria aritmetica (altezze, reticoli). Per controllare certi "denominatori" che rovinerebbero la divisibilità servono la coomologia di Galois, la teoria di Iwasawa e metodi alla Wiles. Perfino un'idea di combinatoria, gli insiemi di Behrend senza progressioni aritmetiche di tre termini, serve a scegliere bene alcuni parametri.

Resta da dire a che punto siamo. Alpöge ha pubblicato solo la formalizzazione in Lean, circa 17 milioni di righe, perché un testo generato dall'AI superava le 250.000 pagine illeggibili. Secondo Robin Zhang, in un giorno le comunità Lean e Mathlib hanno controllato la dimostrazione con implementazioni indipendenti del verificatore. Hanno anche controllato che le definizioni coincidano con quelle matematiche standard. Però non esiste ancora una dimostrazione leggibile da un essere umano. La ricostruzione che ho seguito, quella di Zhang, è scritta in gran parte con l'AI, e Zhang stesso non garantisce che sia fedele al codice. Alpöge ammette di non padroneggiare tutte le parti e si aspetta semplificazioni presto.

### claude_full-L2-s07

*nota intera, spiegazione 8 di 8.* Fatti del livello: 8 sì, 6 in parte, 0 no (copertura 0,79) · errori 0 su 39 · analogie dichiarate 1 · segnalazioni del critico 1, errori introdotti 0 · 645 parole (limite 600) · Gulpease 56,4

Le funzioni L di Dirichlet sono parenti della funzione zeta di Riemann. Dirichlet le introdusse nell'Ottocento per dimostrare che progressioni come 3, 7, 11, 15… contengono infiniti numeri primi. L'ipotesi di Riemann generalizzata afferma che tutti i loro zeri nella striscia 0 < Re(s) < 1 stanno esattamente sulla retta Re(s) = 1/2. Il caso più semplice è proprio l'ipotesi di Riemann classica.

Levent Alpöge, lavorando con Claude, ha scritto la dimostrazione in Lean, un linguaggio in cui il computer controlla ogni passaggio logico. Sono circa 17 milioni di righe di codice. In un giorno le comunità Lean e Mathlib le hanno riverificate con implementazioni indipendenti e hanno controllato che le definizioni coincidano con quelle standard. Una versione leggibile da un essere umano però non esiste ancora. Ciò che segue viene dalla nota preliminare di Robin Zhang, scritta in buona parte con l'aiuto di un'IA: lo stesso Zhang avverte che non può garantire che sia una traduzione fedele del codice.

**Primo passo: dagli zeri ai numeri primi.** Si considera una somma su tutte le potenze di primi fino a x, pesata con log p, alla quale si sottrae un "termine principale" prevedibile. Uno zero a destra di 1/2 costringerebbe questa somma a essere troppo grande. Basta allora dimostrare che resta sotto x^(1/2+η), per ogni η positivo. Due dettagli rendono il compito più leggero: serve solo un limite dall'alto, e basta che valga su intervalli arbitrariamente grandi, non per ogni x. Si sommano più funzioni L con coefficienti positivi, così i loro zeri non possono annullarsi a vicenda. La metà sinistra della striscia si tratta poi per simmetria, grazie all'equazione funzionale.

**Secondo passo: divisibilità contro grandezza.** Un'analogia aiuta: un intero diverso da zero e divisibile per 2^100 deve valere almeno 2^100. La dimostrazione usa una versione di questo principio per i numeri algebrici, applicata ai "periodi automorfi". Si tratta di integrali di forme automorfe, funzioni dotate di moltissime simmetrie, normalizzati in modo da diventare numeri algebrici. Da un lato si dimostra che questi numeri sono divisibili per potenze di primi, in una quantità che contiene proprio la somma sui primi del primo passo. Dall'altro si dimostra che non sono troppo grandi. Confrontando le due cose si ottiene che la somma non può crescere troppo.

**Il cuore: ripetere e bilanciare.** Per ottenere abbastanza divisibilità si applica m volte il "sollevamento theta". È un'operazione che trasporta una forma automorfa da un gruppo di simmetrie a un altro, e ogni ripetizione aggiunge divisibilità. Alpöge propone un'analogia con il metodo di Stepanov, che contava i punti di una curva su un campo finito costruendo un polinomio che si annulla "molte volte" in quei punti: qui m gioca il ruolo di quel numero di annullamenti. Ma ogni sollevamento ingrandisce anche gli spazi in gioco e quindi gli errori. Alla fine restano due errori, uno di grandezza x/m e uno di grandezza m. Il primo diminuisce e il secondo cresce al crescere di m, e si bilanciano quando m è circa √x. Così entrambi diventano circa √x = x^(1/2): ecco da dove viene l'1/2. Alpöge racconta che fu Claude a suggerire questa lunghezza √x, e commenta: «che altro potrebbe essere?».

**Il resto del lavoro.** Il grosso della fatica tecnica sta nel far tornare i conti. Le costanti devono riprodurre esattamente il termine principale, e qui entrano la formula di Chowla–Selberg e le formule di Weyl e di Siegel. Il volume dei reticoli di forme si controlla con la geometria di Arakelov. I denominatori che compaiono si tengono a bada con le rappresentazioni di Galois e la teoria di Iwasawa. Perfino gli insiemi di Behrend, cioè interi senza progressioni aritmetiche di tre termini, servono a scegliere certi parametri. Nella dimostrazione confluisce più di un secolo di matematica.

Si tratta di una dimostrazione *proposta*. Alpöge stesso la definisce lunghissima, ammette di avervi forse inserito scelte poco ottimali e si aspetta che venga presto semplificata.

### claude_overview-L2-s00

*panoramica, spiegazione 1 di 8.* Fatti del livello: 5 sì, 5 in parte, 4 no (copertura 0,54) · errori 0 su 32 · analogie dichiarate 1 · segnalazioni del critico 1, errori introdotti 0 · 601 parole (limite 600) · Gulpease 57,2

Il 20 novembre 2026 Levent Alpöge ha annunciato di aver dimostrato, insieme all'intelligenza artificiale Claude, l'ipotesi di Riemann generalizzata per le funzioni L di Dirichlet. Per ora la dimostrazione esiste soprattutto come codice per Lean, un programma che controlla ogni passaggio logico. Alpöge ha scelto di non pubblicare un testo leggibile e ammette di non padroneggiare ancora tutta la matematica coinvolta. Quello che segue si basa sulla sua nota e su una nota preliminare del matematico Robin Zhang.

Che cosa si dimostra? Dirichlet voleva capire i numeri primi dentro progressioni come 1, 5, 9, 13, … Per distinguere le progressioni usò certe funzioni periodiche, i caratteri χ, e costruì le funzioni L(s,χ). Queste funzioni si possono estendere a tutti i numeri complessi s. L'enunciato dice che ogni zero di L(s,χ) con parte reale compresa fra 0 e 1 ha parte reale esattamente 1/2. Nel caso più semplice si ritrova l'ipotesi di Riemann originale del 1859, che riguarda la funzione zeta. In sostanza, significa avere il controllo migliore possibile su quanti primi ci sono di una certa grandezza.

Il primo passo collega gli zeri ai primi. Si sommano, fino a un numero x, i termini Λ(n)χ(n)(x/n − 1), dove Λ(n) vale log p se n è una potenza del primo p, e 0 altrimenti. Da questa somma si toglie un "termine principale" prevedibile. Con una trasformazione classica, gli zeri di L diventano punti speciali di un'altra funzione, e più la somma corretta resta piccola, più gli zeri sono costretti verso la retta 1/2. Alpöge combina, con pesi positivi, le somme di un carattere ψ e di tutte le sue potenze, così che gli zeri di funzioni diverse non possano compensarsi a vicenda. Il cuore della dimostrazione diventa allora una stima: la somma combinata non supera x^(1/2+η), per ogni η>0, su intervalli [Y, Y^(3/2)] lontani quanto si vuole. Basta una stima dall'alto, e non serve che valga per ogni x: argomenti classici (Landau, Guinand, Turán, Weil) la trasformano nell'assenza di zeri fuori dalla retta.

Il secondo passo sfrutta la divisibilità. Un'analogia aiuta: un intero diverso da zero e divisibile per 2^10 non può valere meno di 1024 in valore assoluto. Un principio simile vale per numeri algebrici più generali. Alpöge usa dei numeri chiamati "periodi automorfi", cioè integrali di oggetti molto simmetrici, le forme automorfe. Questi periodi sono divisibili per molte potenze di primi, e le somme sui primi compaiono proprio nella misura di quanto lo sono. Se si dimostra anche che i periodi sono "piccoli", si ottiene un limite superiore per le somme.

Come si ottiene tanta divisibilità? Esiste un mondo analogo, quello dei "campi di funzioni", dove l'ipotesi di Riemann era già nota. Lì l'argomento di Stepanov usa la molteplicità, cioè zeri ripetuti, che si studiano con le derivate. Ma sugli interi, scrive Alpöge, sarebbe come "derivare i numeri interi". Il sostituto è una catena di "sollevamenti theta", trasformazioni che portano una forma automorfa da un gruppo di simmetrie a un altro, e ogni passo imita un grado di molteplicità. Con m passi, i due errori principali sono di ordine x/m e m. Scegliendo m vicino a √x, come aveva suggerito Claude, entrambi diventano circa √x: ecco da dove viene l'esponente 1/2.

Tenere sotto controllo tutti gli errori richiede una quantità enorme di matematica. Servono la geometria aritmetica per misurare la grandezza dei periodi, le rappresentazioni di Galois per gestire i denominatori e la teoria di Iwasawa. Serve perfino una costruzione di Behrend di grandi insiemi di numeri senza progressioni aritmetiche di tre termini. Alpöge pensa che molte di queste scelte siano superflue e che arriveranno presto dimostrazioni molto più brevi.

### claude_overview-L2-s01

*panoramica, spiegazione 2 di 8.* Fatti del livello: 6 sì, 8 in parte, 0 no (copertura 0,71) · errori 1 su 35 · analogie dichiarate 1 · segnalazioni del critico 1, errori introdotti 1 · 589 parole (limite 600) · Gulpease 57,2

Nell'Ottocento Dirichlet voleva dimostrare che progressioni come 3, 7, 11, 15, … (primo termine e passo senza fattori comuni) contengono infiniti numeri primi. Per riuscirci introdusse certe funzioni periodiche, i «caratteri», e a ciascuno associò una funzione L(s, χ), parente della funzione zeta di Riemann. Come per la zeta, gli zeri di queste funzioni governano la distribuzione dei primi. L'ipotesi di Riemann generalizzata, nella versione affrontata qui, afferma questo: per ogni carattere primitivo, tutti gli zeri di L(s, χ) nella striscia 0 < Re(s) < 1 stanno sulla retta Re(s) = 1/2.

Il 20 novembre 2026 Levent Alpöge ha annunciato di aver trovato una dimostrazione lavorando con Claude, e di averla formalizzata in Lean, un programma che controlla ogni passaggio logico. Per ora ha pubblicato solo il codice Lean. Un testo leggibile non esiste ancora, e l'argomento è, parole sue, «incredibilmente lungo». La ricostruzione che segue viene soprattutto dalla nota preliminare di Robin Zhang, che parla di dimostrazione «proposta».

Il primo passo traduce gli zeri in un conteggio di primi. Si considera una somma pesata sulle potenze dei primi fino a x e se ne sottrae il termine principale atteso. Il peso è dato dalla funzione di von Mangoldt, che vale log p sulle potenze del primo p e zero altrove. Uno zero fuori dalla retta lascerebbe un'impronta nella crescita di questa somma. Basta allora mostrare che una certa combinazione di queste somme resta sotto x^(1/2+η), per ogni η > 0, su intervalli [Y, Y^(3/2)] arbitrariamente lontani. La combinazione usa tutte le potenze di un carattere con pesi positivi, così gli zeri di funzioni diverse non possono cancellarsi a vicenda. Risultati classici di Landau, Guinand, Turán e Weil trasformano poi questa stima nell'assenza di zeri fuori dalla retta.

Il secondo passo è il cuore: ottenere la stima. Un'analogia semplificata aiuta: un intero non nullo divisibile per 2¹⁰ vale almeno 1024. Nella dimostrazione si usa una versione per i numeri algebrici, la «formula del prodotto»: molta divisibilità impedisce a un numero di essere piccolo in tutte le sue misure di grandezza. Alpöge costruisce dei «periodi automorfi», cioè integrali di funzioni con enormi simmetrie, normalizzati per diventare numeri algebrici. La loro divisibilità per i vari primi dipende proprio dalle somme sui primi, e la loro grandezza si può stimare dall'alto. Confrontando le due informazioni si limita la somma.

Per accrescere la divisibilità si ripete m volte il «sollevamento theta», che trasporta queste funzioni da un gruppo di simmetrie a un altro. Alpöge lo collega a un argomento di Stepanov per la versione dell'ipotesi sui campi di funzioni. Lì serve una «molteplicità» che sugli interi è difficile da trovare, «come derivare i numeri interi». Qui ogni sollevamento imita un grado di molteplicità. Alla fine restano due errori, di grandezza circa x/m e m. Scegliendo m vicino a √x, entrambi diventano circa √x: ecco da dove viene l'esponente 1/2. Alpöge racconta che fu Claude a suggerire che la catena di sollevamenti fosse lunga √X.

Servono pezzi da quasi tutta la teoria dei numeri. La geometria aritmetica misura i reticoli di queste funzioni. Le rappresentazioni di Galois controllano certe congruenze. Interviene la teoria di Iwasawa. C'è perfino la costruzione di Behrend di grandi insiemi di interi senza progressioni aritmetiche di tre termini, usata per scegliere alcuni parametri. Alpöge pensa di aver inserito scelte strane e non ottimali, e si aspetta presto argomenti molto più corti. Ammette di non padroneggiare ancora le parti in cui l'esperto era Claude. Per ora la garanzia sta nella verifica di Lean, mentre la comprensione umana dell'argomento è appena cominciata.

### claude_overview-L2-s02

*panoramica, spiegazione 3 di 8.* Fatti del livello: 6 sì, 5 in parte, 3 no (copertura 0,61) · errori 1 su 30 · analogie dichiarate 0 · segnalazioni del critico 1, errori introdotti 0 · 596 parole (limite 600) · Gulpease 57,1

Nell'Ottocento Dirichlet voleva dimostrare che progressioni aritmetiche come 3, 7, 11, 15, … (con primo termine e passo senza fattori comuni) contengono infiniti numeri primi. Per farlo introdusse le funzioni L(s,χ), oggi dette funzioni L di Dirichlet. Ciascuna è legata a un "carattere" χ, cioè una funzione periodica che serve a distinguere le progressioni. Riemann aveva fatto qualcosa di simile con la funzione zeta: la distribuzione dei primi dipende dai punti in cui la funzione si annulla, i suoi "zeri". L'ipotesi di Riemann generalizzata, già presente in Piltz nel 1884, afferma che per ogni carattere primitivo tutti gli zeri di L(s,χ) nella striscia 0 < Re(s) < 1 stanno sulla retta Re(s) = 1/2. È questo che Alpöge, lavorando con Claude, annuncia di aver dimostrato.

La dimostrazione ha due metà. La prima traduce la domanda sugli zeri in una domanda sui primi. Si usa una somma pesata dei logaritmi delle potenze di primi fino a x, ciascuno moltiplicato per χ e per un peso. Uno strumento chiamato trasformata di Mellin collega la crescita di questa somma agli zeri della funzione L: uno zero a destra della retta critica la farebbe crescere troppo. Prima si sottrae un termine principale noto. Poi si sommano, con pesi positivi, le somme relative a tutte le potenze di un carattere ψ, così che zeri di funzioni diverse non possano cancellarsi a vicenda. A quel punto basta una stima: la somma combinata non supera x^(1/2+η), per ogni η > 0, su intervalli [Y, Y^(3/2)] arbitrariamente lontani. Non serve controllarla per ogni x né dal basso: risultati classici di Landau, Guinand, Turán e Weil permettono di concludere.

La seconda metà, nuova e lunghissima, dimostra questa stima. Il caso più semplice dell'idea di partenza è questo: un intero diverso da zero e divisibile per 2^10 vale almeno 1024 in valore assoluto. Un principio dello stesso tipo, la "formula del prodotto", vale per i numeri algebrici: se un numero è molto divisibile, non può essere piccolo. Alpöge costruisce numeri di questo genere, i "periodi automorfi". Sono integrali di oggetti molto simmetrici, le forme automorfe, normalizzati in modo da appartenere a un campo di numeri. Quanto sono divisibili per i vari primi dipende proprio dalle somme sulle potenze di primi. Confrontando questa divisibilità con una stima della loro grandezza, si ottiene un limite per quelle somme.

Per rendere i periodi molto divisibili si applica ripetutamente il "sollevamento theta", che trasporta una forma automorfa da un gruppo di simmetrie a un altro. Qui riecheggia un'idea di Stepanov. Sui campi di funzioni l'ipotesi di Riemann si dimostra sfruttando zeri "con molteplicità", come le radici doppie di un polinomio. Sugli interi però, scrive Alpöge, sarebbe come derivare i numeri interi. Nella nuova dimostrazione ogni sollevamento theta imita un grado di molteplicità. Con m sollevamenti restano due errori, grandi circa x/m e m. Scegliendo m vicino a √x, come suggerito da Claude, entrambi diventano circa √x: ecco da dove viene l'esponente 1/2.

Per tenere tutto sotto controllo servono teoremi da quasi ogni angolo della teoria dei numeri: geometria di Arakelov, teoria di Hodge p-adica, rappresentazioni di Galois, teoria di Iwasawa. Serve perfino una costruzione di Behrend di insiemi grandi senza progressioni aritmetiche di tre termini.

Va detto onestamente a che punto siamo. Alpöge scrive di "credere" di avere una dimostrazione. L'argomento è enorme e lui stesso non ne padroneggia ancora tutte le parti. Per questo ha pubblicato solo la versione formalizzata in Lean, un programma che verifica ogni passaggio logico. Robin Zhang, nella sua nota preliminare, parla di "dimostrazione proposta". Alpöge si aspetta semplificazioni rapide e promette una stesura leggibile.

### claude_overview-L2-s03

*panoramica, spiegazione 4 di 8.* Fatti del livello: 3 sì, 8 in parte, 3 no (copertura 0,50) · errori 1 su 31 · analogie dichiarate 1 · segnalazioni del critico 1, errori introdotti 0 · 615 parole (limite 600) · Gulpease 58,1

Dirichlet voleva dimostrare che ogni progressione aritmetica come 3, 7, 11, 15, … (con primo termine e passo senza divisori comuni) contiene infiniti numeri primi. Per farlo usò certe funzioni periodiche, i caratteri χ, che servono a distinguere le progressioni. A ciascun carattere associò una funzione L(s, χ) di variabile complessa. L'ipotesi di Riemann generalizzata, nella forma annunciata da Levent Alpöge il 20 novembre 2026, afferma che gli zeri di queste funzioni con parte reale fra 0 e 1 stanno tutti sulla retta di parte reale 1/2. Sapere dove stanno gli zeri significa controllare nel modo migliore possibile quanti primi di una certa grandezza cadono in ogni progressione.

La dimostrazione proposta procede in due grandi passi.

Il primo passo trasforma gli zeri in somme sui primi. La funzione Λ(n) vale log p quando n è una potenza del primo p, e 0 altrimenti. Alpöge studia una somma pesata dei valori Λ(n)χ(n) per n fino a x, da cui toglie un "termine principale" prevedibile. Una formula classica (la trasformata di Mellin) lega la crescita di questa somma agli zeri: uno zero a destra della retta critica la farebbe crescere troppo. Basta quindi dimostrare che una certa combinazione di queste somme resta sotto x^(1/2+η), per ogni η positivo piccolo a piacere. La combinazione usa tutte le potenze di un carattere ψ, ed è costruita in modo che zeri di funzioni diverse non possano compensarsi a vicenda. La stima non serve per ogni x: bastano intervalli [Y, Y^(3/2)] lontani quanto si vuole.

Il secondo passo, il cuore della dimostrazione, consiste nel provare quella stima. L'idea di partenza è semplice. Un'analogia: un intero non nullo divisibile per 2^10 vale almeno 1024. Più un numero è divisibile, più deve essere grande. Per i numeri algebrici vale una versione di questo principio, la formula del prodotto. Alpöge costruisce numeri di questo tipo, i periodi automorfi, che sono integrali di oggetti molto simmetrici chiamati forme automorfe. Poi mostra che la divisibilità di questi periodi per i primi è legata proprio alle somme sui primi. Se i periodi non possono essere troppo grandi, allora nemmeno le somme possono esserlo.

Resta da capire come ottenere tanta divisibilità. Qui entra l'idea che Alpöge attribuisce a Claude. Nel caso "giocattolo" dei campi di funzioni, l'ipotesi di Riemann era già stata dimostrata con l'argomento di Stepanov, che sfrutta la molteplicità: zeri contati più volte, cosa che richiede di derivare. Sugli interi, scrive Alpöge, sarebbe come "derivare i numeri interi". Il sostituto trovato sono i sollevamenti theta (theta lifts), operazioni che trasportano una forma automorfa da un gruppo di simmetrie a un altro. Ogni sollevamento aggiunge divisibilità, come uno strato in più di molteplicità, e se ne eseguono m di fila. Alla fine restano due errori, di dimensioni circa x/m e m. Se m è piccolo pesa il primo, se m è grande pesa il secondo. Scegliendo m vicino a √x, entrambi valgono circa √x: ecco da dove viene l'esponente 1/2.

Per rendere tutto rigoroso servono moltissimi strumenti. La geometria aritmetica serve a misurare quanto sono "grandi" i reticoli di forme automorfe. Le rappresentazioni di Galois e la coomologia controllano denominatori indesiderati. Intervengono anche la teoria di Iwasawa e una costruzione di Behrend di insiemi di interi senza progressioni aritmetiche di tre termini.

Sullo stato del risultato bisogna essere onesti. Alpöge dice di "credere" di aver trovato una dimostrazione. Afferma di averla formalizzata con Claude in Lean, un programma che verifica ogni passaggio, e per ora ha pubblicato solo il codice Lean, non un articolo leggibile. Ammette di non padroneggiare ancora tutta la matematica coinvolta e si aspetta semplificazioni. La nota di Robin Zhang, su cui si basa questa ricostruzione, si definisce preliminare e parla di "dimostrazione proposta".

### claude_overview-L2-s04

*panoramica, spiegazione 5 di 8.* Fatti del livello: 8 sì, 4 in parte, 2 no (copertura 0,71) · errori 0 su 31 · analogie dichiarate 1 · segnalazioni del critico 0, errori introdotti 0 · 577 parole (limite 600) · Gulpease 58,1

Nella prima metà dell'Ottocento Dirichlet voleva dimostrare che una progressione come 1, 5, 9, 13…, con primo termine e passo senza divisori comuni, contiene infiniti numeri primi. Per farlo introdusse delle funzioni, oggi chiamate funzioni L di Dirichlet. Ognuna è legata a un "carattere" χ, una funzione periodica sugli interi che serve a distinguere le progressioni. La più semplice di queste funzioni è la zeta di Riemann. L'ipotesi di Riemann generalizzata, già formulata da Piltz nel 1884, afferma che tutti gli zeri di queste funzioni nella "striscia critica" (parte reale tra 0 e 1) stanno esattamente sulla retta di parte reale 1/2. Levent Alpöge, il 20 novembre 2026, ha annunciato di averla dimostrata lavorando con Claude.

Il risultato va presentato con prudenza. Alpöge non ha pubblicato un articolo leggibile. Ha reso pubblica soltanto la versione in Lean, un linguaggio in cui un computer controlla ogni passaggio, e afferma che la formalizzazione è completa. Ammette però che il ragionamento è lunghissimo e che non lo padroneggia ancora del tutto. Il matematico Robin Zhang, in una nota preliminare che ne riassume la struttura, parla di "dimostrazione proposta".

Il primo passo traduce gli zeri in un problema sui primi. Si usa la funzione di von Mangoldt, che vale log p se n è una potenza del primo p e zero altrimenti. Se ne sommano i valori fino a x, pesati con χ(n) e con il fattore x/n − 1. Una trasformazione integrale, detta di Mellin, collega questa somma alla funzione L: ogni zero diventa un punto in cui l'espressione esplode. Come analogia, uno zero fuori dalla retta critica sarebbe un'eco che fa crescere la somma troppo in fretta. Dopo aver tolto un "termine principale" prevedibile, basta mostrare che una certa combinazione di queste somme resta sotto x elevato a "1/2 più un pochino". Non serve che valga per ogni x: bastano intervalli della forma [Y, Y^(3/2)], scelti arbitrariamente lontani.

Il secondo passo, il cuore della dimostrazione, ottiene questa stima da un principio semplice. Un intero algebrico non nullo, divisibile per molte potenze di primi, non può essere piccolo in tutte le sue misure di grandezza. Con gli interi comuni l'idea è questa: un numero diverso da zero divisibile per 2^10 vale almeno 1024. Alpöge costruisce dei "periodi automorfi", cioè integrali di funzioni estremamente simmetriche, normalizzati in modo da essere numeri algebrici. Quanto sono divisibili per i primi dipende proprio dalle somme di prima. Quanto sono grandi si può invece limitare dall'alto. Confrontando le due informazioni si ottiene il controllo cercato.

Per aumentare la divisibilità si usano i "sollevamenti theta", che trasportano una forma automorfa da un gruppo di simmetrie a un altro, ripetuti m volte. L'idea discende da un argomento di Stepanov, che dimostra un analogo dell'ipotesi di Riemann in un altro contesto sfruttando la "molteplicità" degli zeri. Sugli interi la molteplicità è difficile da ottenere: Alpöge la paragona a "derivare i numeri interi". Ogni sollevamento ne imita un pezzo. Da qui nasce l'1/2: i due errori principali hanno grandezza circa x/m e m. Prendendo m vicino a √x, entrambi diventano circa √x. Secondo Alpöge, fu Claude a suggerire una catena di lunghezza √x.

Per far tornare i conti serve moltissima matematica. La geometria di Arakelov misura i reticoli di forme. Rappresentazioni di Galois e coomologia controllano i denominatori. Intervengono anche la teoria di Iwasawa e perfino una costruzione di Behrend di insiemi di interi senza progressioni aritmetiche di tre termini. Alpöge stesso si aspetta che l'argomento venga presto semplificato.

### claude_overview-L2-s05

*panoramica, spiegazione 6 di 8.* Fatti del livello: 4 sì, 7 in parte, 3 no (copertura 0,54) · errori 0 su 36 · analogie dichiarate 1 · segnalazioni del critico 2, errori introdotti 2 · 592 parole (limite 600) · Gulpease 59,3

I numeri primi sembrano sparsi a caso. Già nell'Ottocento Dirichlet voleva dimostrare che ogni progressione aritmetica come 1, 5, 9, 13… contiene infiniti primi. Per distinguere le progressioni usò certe funzioni periodiche, i caratteri χ, e costruì le funzioni L(s,χ), parenti della funzione zeta di Riemann. I punti in cui queste funzioni si annullano, i loro «zeri», regolano quanto è ordinata la distribuzione dei primi. L'ipotesi di Riemann generalizzata afferma che, per ogni carattere primitivo, gli zeri nella striscia 0 < Re(s) < 1 stanno tutti sulla retta Re(s) = 1/2. Levent Alpöge sostiene di averla dimostrata lavorando con Claude.

Il primo passo traduce gli zeri in una domanda sui primi. Si considera una somma pesata: per ogni potenza di primo pᵏ fino a x si aggiunge log p, moltiplicato per χ(pᵏ) e per il peso x/pᵏ − 1. Uno zero produce un'irregolarità in questa somma, quindi controllarne la crescita vincola la posizione degli zeri. Alpöge sottrae la parte prevedibile, il «termine principale». Poi somma con pesi positivi i contributi di tutte le potenze di un carattere ψ: così gli zeri di funzioni diverse non possono compensarsi a vicenda. Il cuore della dimostrazione è la Proposizione 1.2: questa somma combinata resta sotto x^(1/2+η), per ogni η > 0, su intervalli [Y, Y^(3/2)] che si trovano arbitrariamente lontano. Bastano una stima solo dall'alto e solo su certi intervalli. Un ragionamento classico, legato ai nomi di Landau, Guinand, Turán e Weil, la trasforma poi nell'assenza di zeri fuori dalla retta.

Come si ottiene la stima? L'idea guida è elementare. Un intero diverso da zero e divisibile per 2¹⁰ vale almeno 1024. Per i numeri algebrici esiste una versione di questo fatto, la «formula del prodotto»: un numero molto divisibile non può essere troppo piccolo ovunque. Alpöge costruisce numeri speciali, i periodi automorfi. Sono integrali di funzioni con enormi simmetrie, le forme automorfe, e la loro divisibilità dipende proprio dalle somme sui primi. Se si dimostra che questi numeri non sono troppo grandi, neppure la loro divisibilità può essere troppo alta, e questo frena le somme.

Per aumentare la divisibilità si usa il sollevamento theta, che trasporta una forma automorfa da un gruppo di simmetrie a un altro, e lo si ripete m volte. L'ispirazione viene da un caso più semplice. Nella dimostrazione di Stepanov dell'analoga ipotesi per i «campi di funzioni» serve una «molteplicità», legata al derivare. Ma, osserva Alpöge, derivare i numeri interi non ha senso. Qui ogni sollevamento theta imita un grado di molteplicità. Alla fine restano due errori, uno di grandezza circa x/m e l'altro circa m. Scegliendo m vicino a √x entrambi diventano circa √x: da qui viene l'esponente 1/2. Secondo Alpöge, l'idea di una catena lunga √x è stata un suggerimento di Claude.

Per far tornare tutte le costanti servono moltissimi altri strumenti. La geometria aritmetica misura i reticoli di forme automorfe. Le rappresentazioni di Galois e la teoria di Iwasawa controllano i denominatori. C'è perfino una costruzione di Behrend di insiemi di interi senza progressioni aritmetiche di tre termini. Per usare un'analogia, è come pesare qualcosa con una bilancia di precisione: ogni pezzo va tarato al millesimo, altrimenti l'errore supera √x.

Resta da dire a che punto siamo. L'argomento è stato formalizzato in Lean, un programma che controlla ogni passaggio logico, e Alpöge ha pubblicato soltanto quella versione. Un testo leggibile per esseri umani non esiste ancora: quello generato superava le 250.000 pagine. Alpöge ammette di non padroneggiare ancora tutte le parti e si aspetta forti semplificazioni. La nota preliminare di Robin Zhang parla infatti di «dimostrazione proposta».

### claude_overview-L2-s06

*panoramica, spiegazione 7 di 8.* Fatti del livello: 5 sì, 5 in parte, 4 no (copertura 0,54) · errori 0 su 24 · analogie dichiarate 1 · segnalazioni del critico 2, errori introdotti 2 · 534 parole (limite 600) · Gulpease 55,1

Nel 1837 Dirichlet voleva dimostrare che ogni progressione aritmetica come 3, 7, 11, 15, … (con primo termine e passo senza fattori comuni) contiene infiniti numeri primi. Per farlo inventò delle funzioni, oggi chiamate funzioni L di Dirichlet, che separano i primi a seconda della progressione in cui cadono. Queste funzioni hanno degli zeri, cioè punti del piano complesso in cui valgono zero, e la posizione di questi zeri controlla quanto regolarmente si distribuiscono i primi. L'ipotesi di Riemann generalizzata, formulata già nel 1884, afferma che tutti gli zeri della striscia con parte reale tra 0 e 1 stanno esattamente sulla retta di parte reale 1/2. Levent Alpöge afferma di aver dimostrato proprio questo enunciato, lavorando con Claude.

Il primo passo è un ponte tra zeri e primi. Si prende una somma sui primi e sulle loro potenze fino a x, con peso x/n − 1, e le si sottrae il termine principale atteso. Un'identità classica mostra che uno zero fuori dalla retta lascerebbe una traccia in questa somma, facendola crescere troppo. Basta quindi dimostrare che la somma, combinata su più funzioni L, resta sotto x elevato a "1/2 più un pochino". Non serve controllarla per ogni x: bastano intervalli [Y, Y^(3/2)] che si spingono arbitrariamente lontano, e basta una stima dall'alto.

Il cuore della dimostrazione è ottenere questa stima. Il punto di partenza si capisce con un'analogia, che resta solo un'analogia: un intero diverso da zero e divisibile per 1000 vale almeno 1000, perché essere molto divisibile costringe a essere grande. Alpöge usa una versione raffinata di questo principio, la formula del prodotto, applicata ai "periodi automorfi". Sono integrali di oggetti con moltissime simmetrie, le forme automorfe. Quanto questi periodi siano divisibili dipende proprio dalle somme sui primi, mentre la loro grandezza si può limitare dall'alto. Confrontando le due informazioni si ricava il limite superiore cercato.

Per ottenere abbastanza divisibilità si ripete m volte un'operazione chiamata sollevamento theta, che trasporta una forma automorfa da un gruppo di simmetrie a un altro. Alpöge collega l'idea a un argomento di Stepanov, che risolse l'analogo dell'ipotesi di Riemann in un mondo più semplice, quello dei campi di funzioni, usando una nozione di "molteplicità". Sugli interi la molteplicità è difficile da trovare: è un po' come voler derivare i numeri interi. Ogni sollevamento theta ne imita un grado.

Qui arriva il punto più elegante. Alla fine restano due errori principali: uno è circa x/m, l'altro circa m. Aumentando i sollevamenti il primo cala e il secondo cresce. Il compromesso migliore è scegliere m vicino a √x. Così entrambi gli errori diventano circa √x, e compare esattamente l'esponente 1/2 della retta critica.

Rendere rigoroso tutto questo richiede moltissimi strumenti: geometria aritmetica, rappresentazioni di Galois, teoria di Iwasawa. Serve perfino una costruzione di Behrend, cioè insiemi di interi senza tre termini in progressione aritmetica, che Alpöge stesso ritiene probabilmente superflua.

Restano due avvertenze oneste. L'argomento è lunghissimo e non esiste ancora una versione leggibile da un essere umano: Alpöge ha pubblicato solo il codice in Lean, un programma che controlla meccanicamente ogni passaggio, e dice che la formalizzazione è completa. La nota di Robin Zhang parla infatti di "dimostrazione proposta". Alpöge, inoltre, si aspetta che venga presto semplificata parecchio.

### claude_overview-L2-s07

*panoramica, spiegazione 8 di 8.* Fatti del livello: 7 sì, 7 in parte, 0 no (copertura 0,75) · errori 0 su 33 · analogie dichiarate 0 · segnalazioni del critico 1, errori introdotti 1 · 622 parole (limite 600) · Gulpease 55,6

I numeri primi sembrano sparsi a caso, eppure si possono contare con grande precisione se si sa dove stanno gli "zeri" di certe funzioni. Il 20 novembre 2026 il matematico Levent Alpöge ha annunciato di aver dimostrato, lavorando con l'intelligenza artificiale Claude, l'ipotesi di Riemann generalizzata per le funzioni L di Dirichlet.

Nell'Ottocento Dirichlet voleva sapere se progressioni come 1, 5, 9, 13, … contengono infiniti primi. Per distinguerle usò i "caratteri", funzioni periodiche che rispettano la moltiplicazione, e con essi costruì le funzioni L(s, χ). La più famosa è la zeta di Riemann. L'enunciato dimostrato è questo: per ogni carattere primitivo, tutti gli zeri di L(s, χ) nella striscia 0 < Re(s) < 1 stanno esattamente sulla retta Re(s) = 1/2.

Il primo passo traduce gli zeri in un problema sui primi. Si prende una somma pesata sulle potenze dei primi fino a x, costruita con la funzione di von Mangoldt (vale log p sulle potenze del primo p e zero altrove), e le si sottrae il "termine principale" atteso. Una trasformazione di Mellin fa comparire ogni zero come un "polo", cioè un punto in cui la funzione trasformata esplode. Se la somma corretta non cresce più di x elevato a 1/2 più un pizzico, non possono esserci zeri a destra della retta critica. Alpöge somma insieme tutte le potenze di un carattere con pesi positivi, così gli zeri di funzioni diverse non possono cancellarsi a vicenda. Basta una stima solo dall'alto, e solo su intervalli [Y, Y^(3/2)] arbitrariamente lontani.

Il secondo passo, il cuore, è ottenere quella stima. Il principio guida, nel caso dei normali numeri interi, è questo: un intero diverso da zero e divisibile per 2¹⁰ vale almeno 1024. La versione generale, la "formula del prodotto", vale per i numeri algebrici. Alpöge costruisce numeri di questo tipo, chiamati "periodi": sono integrali di forme automorfe, oggetti dotati di moltissime simmetrie. La somma sui primi compare nella stima di quanto questi numeri sono divisibili, mentre la loro grandezza si può limitare dall'alto. Mettendo a confronto i due lati si tiene sotto controllo la somma.

Per aumentare la divisibilità si applica m volte di fila un "sollevamento theta", che trasporta una forma automorfa da un gruppo di simmetrie a un altro. Secondo Alpöge, ogni passaggio imita la "molteplicità" usata da Stepanov nel caso analogo dei campi di funzioni. Sugli interi questa idea è difficile da realizzare: sarebbe, dice lui, come "derivare i numeri interi". Alla fine restano due errori, grandi circa x/m e m. Per renderli piccoli entrambi conviene scegliere m vicino a √x, e allora valgono tutti e due circa √x: ecco da dove viene l'1/2. Proprio questa lunghezza della catena, √X, è stata suggerita da Claude. Alpöge racconta di aver guidato il lavoro fino all'impostazione giusta e che poi, vicino al traguardo, Claude lo ha superato.

Per far funzionare tutto servono strumenti presi da quasi ogni ramo della teoria dei numeri: geometria di Arakelov, teoria di Hodge p-adica, rappresentazioni di Galois, teoria di Iwasawa. C'è perfino una costruzione di Behrend, che produce grandi insiemi di numeri senza progressioni aritmetiche di tre termini.

Quanto è affidabile il risultato? La dimostrazione è scritta in Lean, un programma che controlla ogni passaggio logico, e Alpöge dichiara di averla formalizzata "senza ipotesi aggiuntive". Ha pubblicato solo il codice Lean: una versione completa per lettori umani sarebbe un documento enorme e illeggibile, e quella generata in automatico superava le 250.000 pagine. Ammette di non padroneggiare ancora alcune parti, alcune sue descrizioni sono parafrasi di riassunti prodotti da Claude, e si aspetta semplificazioni. Anche la nota di Robin Zhang che riassume l'argomento si definisce "preliminare" e parla di una dimostrazione "proposta". Il controllo della macchina c'è già; il lavoro per capirla davvero è appena cominciato.

## Livello 3: un laureato in matematica che non si occupa di teoria dei numeri (al più 1000 parole)

### claude_full-L3-s00

*nota intera, spiegazione 1 di 8.* Fatti del livello: 17 sì, 6 in parte, 2 no (copertura 0,80) · errori 0 su 60 · analogie dichiarate 0 · segnalazioni del critico 0, errori introdotti 0 · 1117 parole (limite 1000) · Gulpease 51,4

Il risultato annunciato è l'ipotesi di Riemann generalizzata per le funzioni L di Dirichlet. Per ogni carattere di Dirichlet primitivo χ, tutti gli zeri di L(s,χ) nella striscia 0 < Re(s) < 1 starebbero sulla retta Re(s) = 1/2. Il caso χ banale, cioè la funzione zeta, è l'ipotesi di Riemann classica.

Prima di tutto lo stato dei fatti. Alpöge, lavorando con Claude, ha pubblicato soltanto una formalizzazione in Lean di circa 17 milioni di righe. Non ha rilasciato un testo leggibile: ne esiste uno generato automaticamente di oltre 250.000 pagine, che ha scelto di non diffondere. Secondo Robin Zhang, le comunità Lean e Mathlib hanno verificato la dimostrazione con implementazioni indipendenti del kernel e hanno controllato che le definizioni coincidano con quelle standard. La ricostruzione matematica che segue viene dalla nota preliminare di Zhang. Zhang stesso avverte che gran parte di quel testo è stata scritta con un'IA e che non può garantire che traduca fedelmente il codice Lean. Lo stesso Alpöge dice di non padroneggiare ancora tutte le parti e si aspetta semplificazioni drastiche.

**Primo passo: ridurre tutto a una stima sui primi.** L'oggetto centrale è una somma pesata sulle potenze dei primi:

Sχ(x) = Σ_{n≤x} Λ(n)χ(n)(x/n − 1),

dove Λ è la funzione di von Mangoldt. Il peso (x/n − 1) rende semplice la trasformata di Mellin, che risulta −L′(s,χ)/(s(s−1)L(s,χ)). Ogni zero di L nella striscia critica diventa quindi un polo della trasformata. Si sottrae un termine principale per eliminare il polo in s = 1, ottenendo funzioni corrette Gχ(x). Poi si forma una combinazione Gψ a coefficienti positivi, che coinvolge le potenze di un carattere ψ.

Basta dimostrare che Gψ(x) ≤ x^{1/2+η} su intervalli [Y, Y^{3/2}] arbitrariamente lontani (Proposizione 1.2). Che una stima solo dall'alto, e solo su certi intervalli, sia sufficiente è un fatto di analisi complessa che non richiede l'ipotesi di Riemann. Si ragiona così:

- I coefficienti positivi fanno sommare, invece di cancellarsi, i contributi di uno zero comune a più funzioni L.
- Si deriva k volte la trasformata (in coordinate logaritmiche è una trasformata di Laplace). Il nucleo diventa una densità gamma che, per k proporzionale a log Y, concentra la massa proprio sull'intervallo dove vale la stima.
- Un polo con parte reale maggiore di 1/2 + η forzerebbe le derivate a crescere più in fretta di quanto la stima consenta: contraddizione.

Il metodo ricorda quello delle somme di potenze di Turán. L'equazione funzionale sistema poi la metà sinistra della striscia.

**Secondo passo: dai primi alla divisibilità.** Qui entra l'idea portante, che si basa sulla formula del prodotto. Un esempio elementare dà l'intuizione: un intero non nullo divisibile per 2^100 ha valore assoluto almeno 2^100. In generale, un intero algebrico non nullo molto divisibile ai primi finiti non può essere piccolo in tutti i posti archimedei.

La dimostrazione costruisce numeri algebrici, i "periodi automorfi": integrali normalizzati di forme automorfe su gruppi unitari, del tipo detto di Bessel e studiato da Gan, Gross e Prasad. Le loro valutazioni p-adiche ammettono minorazioni in cui compaiono esattamente i termini della somma sui primi. Il legame passa per condizioni sul Frobenius tradotte, con l'ortogonalità dei caratteri, in somme di valori di caratteri di Dirichlet, come faceva Dirichlet per le progressioni aritmetiche.

Le maggiorazioni archimedee dei periodi diventano così maggiorazioni della somma sui primi. Il punto delicato è che le costanti devono riprodurre esattamente il termine principale sottratto. Questo avviene grazie a un legame classico: secondo Chowla–Selberg e Anderson, i periodi di varietà abeliane a moltiplicazione complessa sono collegati alle derivate logaritmiche delle funzioni L di Dirichlet. Le costanti si cancellano esattamente (equazione 4.5 di Zhang).

**Terzo passo: moltiplicare la divisibilità.** Un solo periodo non basta. La dimostrazione applica m volte la corrispondenza theta, che trasporta forme automorfe da un gruppo unitario a uno più grande. Ogni sollevamento aggiunge un contributo alla divisibilità.

Alpöge propone un'analogia esplicita con il metodo di Stepanov per contare i punti di curve su campi finiti. Lì si costruisce un polinomio ausiliario che si annulla con alta molteplicità nei punti da contare. Qui il numero m di sollevamenti fa la parte della molteplicità. Alpöge osserva che sugli interi la molteplicità è difficile da trovare: sarebbe come "derivare i numeri interi".

Più sollevamenti però ingrandiscono gli spazi coinvolti, e alla fine restano due errori di ordine x/m e m. Scegliendo m ≈ √x entrambi diventano circa √x, ed è da qui che nasce l'esponente 1/2. Alpöge racconta che fu Claude a proporre questa lunghezza √X per la catena di sollevamenti.

**Quarto passo: il controllo degli errori.** È la parte di gran lunga più lunga, e qui posso solo indicare gli strumenti.

- **Le forme come reticoli.** Per confrontare valutazioni finite e norme archimedee, le forme automorfe vengono organizzate in reticoli su anelli di interi, con norme hermitiane. Il loro covolume si controlla con la geometria di Arakelov: formule di Hilbert–Samuel aritmetiche (Gillet–Soulé, Zhang, Moriwaki), altezze su compattificazioni di spazi di moduli di varietà abeliane, teoria p-adica di Hodge integrale.
- **Le immagini devono coprire tutto lo spazio.** La disuguaglianza delle pendenze di Bost e la filtrazione di Harder–Narasimhan trasferiscono le stime attraverso le mappe definite dai periodi. Un lemma di algebra lineare, nello spirito dei "tight frames", garantisce che le immagini non si concentrino in un sottospazio piccolo.
- **I denominatori.** Proiettare sugli autospazi di Hecke può introdurre denominatori, che misurano congruenze tra forme automorfe. Queste si controllano passando alle rappresentazioni di Galois associate, fino a stimare gruppi di coomologia di Galois "localmente banali". Gli strumenti sono elementi di Stickelberger, il metodo di Kolyvagin, la teoria delle deformazioni alla Taylor–Wiles, il sistema di Eulero di Kato e la teoria di Iwasawa con il teorema di Ferrero–Washington.
- **Il ruolo della libertà sugli intervalli.** È qui che serve poter scegliere gli intervalli [Y, Y^{3/2}]. Alcuni indici "eccezionali", per i quali si dispone solo di stime grossolane, vengono confinati sotto una piccola potenza di x.
- **La scelta dei posti complessi.** I posti complessi su cui distribuire i pesi devono essere molti, ma poco addensati nelle orbite del Frobenius. Per sceglierli si usa una variante della costruzione di Behrend di insiemi privi di progressioni aritmetiche di tre termini.

Il quadro complessivo, in sintesi:
- un'equivalenza analitica classica tra la stima Gψ(x) ≲ x^{1/2+η} e l'assenza di zeri fuori dalla retta critica;
- un meccanismo nuovo che ottiene quella stima confrontando divisibilità finita e grandezza archimedea di periodi automorfi;
- la ripetizione dei sollevamenti theta, che imita la molteplicità di Stepanov;
- un enorme apparato per tenere tutti gli errori entro x^{1/2+η}.

Zhang segnala che lo stesso giorno è stata annunciata anche una dimostrazione indipendente di Alessandro Masullo, svolta senza IA. La comprensione umana di entrambe, per ora, è appena cominciata.

### claude_full-L3-s01

*nota intera, spiegazione 2 di 8.* Fatti del livello: 18 sì, 5 in parte, 2 no (copertura 0,82) · errori 0 su 53 · analogie dichiarate 1 · segnalazioni del critico 1, errori introdotti 1 · 1087 parole (limite 1000) · Gulpease 55,0

Il teorema annunciato è l'ipotesi di Riemann generalizzata per le funzioni L di Dirichlet. Un carattere di Dirichlet χ è una funzione periodica e moltiplicativa sugli interi, quella che Dirichlet usò per separare le progressioni aritmetiche. A esso si associa L(s,χ) = Σ χ(n) n^(−s), prolungata meromorficamente a tutto il piano. L'enunciato è che ogni zero di L(s,χ) nella striscia 0 < Re(s) < 1 sta sulla retta Re(s) = 1/2. Con χ banale si ritrova l'ipotesi di Riemann classica.

Prima del contenuto conviene chiarire lo stato delle cose. Alpöge ha pubblicato soltanto una formalizzazione in Lean, di circa 17 milioni di righe. Ha deciso di non diffondere un'esposizione di oltre 250.000 pagine generata dall'IA. Secondo la nota di Robin Zhang, nel giro di un giorno le comunità Lean e Mathlib hanno verificato la dimostrazione con implementazioni indipendenti del kernel. Hanno anche controllato che le definizioni in Lean coincidano con quelle matematiche standard. Una versione leggibile da un essere umano però non esiste ancora. Quello che segue si basa sulla ricostruzione di Zhang, scritta in larga parte da un'IA a partire dal codice Lean, che lo stesso Zhang non garantisce fedele. Alpöge dichiara di non padroneggiare ancora alcune parti dell'argomento e si aspetta semplificazioni drastiche.

**Primo passo: ridurre tutto a una disuguaglianza sui primi.** Sia Λ(n) = log p se n è una potenza del primo p, e 0 altrimenti. Si considerano le somme pesate S_χ(x) = Σ_{n≤x} Λ(n)χ(n)(x/n − 1). Il peso è scelto perché la trasformata di Mellin sia semplice: vale −L′(s,χ)/(s(s−1)L(s,χ)). Gli zeri di L diventano così poli, e la crescita di S_χ controlla dove possono trovarsi. Si sottrae poi un termine principale per eliminare il polo in s = 1 e si ottengono funzioni corrette G_χ. Infine, per un carattere ψ, si forma una combinazione 𝒢_ψ a coefficienti positivi dei G_χ associati alle potenze di ψ.

Il cuore analitico è la Proposizione 1.2: per ogni η > 0 esistono intervalli [Y, Y^(3/2)] con Y arbitrariamente grande su cui 𝒢_ψ(x) ≤ x^(1/2+η). È solo una maggiorazione, e vale solo su alcuni intervalli, ma basta per due ragioni.

- I coefficienti sono positivi, quindi i residui nei poli si sommano e non possono cancellarsi.
- Derivando molte volte la trasformata, il nucleo d'integrazione diventa una densità gamma concentrata proprio sull'intervallo in cui vale la stima. Il polo più vicino al punto scelto domina allora le derivate di ordine alto, un'idea affine al metodo di Turán.

Ne segue che non ci sono zeri con Re(s) > 1/2. L'equazione funzionale esclude poi quelli a sinistra della retta critica.

**Secondo passo: dall'aritmetica alle forme automorfe.** Il principio guida è la formula del prodotto: un intero algebrico non nullo molto divisibile per molti primi non può essere piccolo in tutte le sue immagini complesse. Un'analogia elementare: un intero non nullo divisibile per 2^100 vale almeno 2^100 in valore assoluto.

Gli oggetti a cui si applica il principio sono i periodi automorfi P_α(f,g). Sono integrali di forme automorfe su gruppi unitari, normalizzati in modo da prendere valori in un campo di numeri K. Alpöge mostra due cose:

- le valutazioni p-adiche di questi periodi sono limitate dal basso da somme sulle potenze dei primi, tramite condizioni sul Frobenius tradotte in caratteri con l'ortogonalità;
- le loro dimensioni archimedee sono limitate dall'alto.

Confrontando le due stime si ottiene una maggiorazione delle somme sui primi.

Il punto delicato è che il confronto deve riprodurre esattamente il termine principale già sottratto in G_χ. Ci riesce perché la normalizzazione usa periodi di varietà abeliane a moltiplicazione complessa. Questi periodi sono legati, tramite Chowla–Selberg e Anderson, alle derivate logaritmiche delle funzioni L di Dirichlet. Insieme alla formula delle dimensioni di Weyl e alla formula di massa di Siegel, le costanti si cancellano esattamente.

**Terzo passo: iterare i theta-lift.** Un solo confronto non è abbastanza preciso. La corrispondenza theta, che ha origine nella rappresentazione di Weil nata dalla meccanica quantistica, trasporta forme automorfe da un gruppo unitario a un altro. Alpöge la applica m volte in catena, e ogni lift aggiunge divisibilità ai periodi. Le identità "seesaw" di Kudla collegano il periodo iniziale a quello finale.

Alpöge propone un'analogia esplicita con il metodo di Stepanov per contare i punti di curve su campi finiti. Lì si costruisce un polinomio ausiliario che si annulla con molteplicità alta in quei punti. Qui il numero m di lift svolge il ruolo della molteplicità, che sugli interi è difficile da imitare: Alpöge lo paragona a «derivare i numeri interi».

Aumentare m ha però un costo. I due errori principali hanno grandezza x/m e m, e il compromesso ottimale è m ≈ √x. È di qui che nasce l'esponente 1/2. Alpöge racconta che fu proprio Claude a suggerire una catena di lunghezza √X.

**Il macchinario tecnico.** Per rendere quantitativo il confronto servono tre ordini di strumenti, che si possono solo nominare.

Geometria di Arakelov. Si lavora con reticoli di forme automorfe muniti di norme e si stimano i loro covolumi, o "pendenze". Gli strumenti sono la filtrazione di Harder–Narasimhan, la disuguaglianza delle pendenze di Bost e un lemma di algebra lineare. Il lemma garantisce che le immagini delle mappe definite dai periodi riempiano quasi tutto lo spazio. I covolumi si controllano tramite altezze su spazi di moduli di varietà abeliane, con la formula di Hilbert–Samuel aritmetica (Gillet–Soulé, Zhang, Moriwaki) e con la teoria di Hodge p-adica (Fargues, teoria di Dieudonné prismatica).

Coomologia di Galois. Proiettare sugli autospazi di Hecke può introdurre denominatori. Questi misurano congruenze tra forme automorfe, che si traducono in classi di estensione di rappresentazioni di Galois. Gli ordini dei gruppi di coomologia coinvolti si stimano con:
- elementi di Stickelberger e operatori di Kolyvagin;
- teoria delle deformazioni e metodo di Taylor–Wiles;
- il sistema di Eulero di Kato;
- la teoria di Iwasawa, con l'annullamento dell'invariante μ (Ferrero–Washington).

Per alcuni "twist eccezionali" la stima disponibile è più grossolana. Qui interviene la libertà di scegliere l'intervallo [Y, Y^(3/2)]: lo si sceglie in modo che gli indici eccezionali restino piccoli rispetto a x.

Combinatoria additiva. Per selezionare i posti complessi rilevanti si adatta la costruzione di Behrend di insiemi privi di progressioni aritmetiche di tre termini.

**Valutazione onesta.** La struttura logica è chiara: una riduzione analitica relativamente classica e un'enorme stima aritmetica ottenuta confrontando valutazioni p-adiche e norme archimedee di periodi automorfi. Lo stesso Alpöge sospetta però di aver incorporato «scelte strane e subottimali» e definisce la costruzione di Behrend probabilmente superflua. La certezza della correttezza oggi poggia sulla verifica in Lean. La comprensione umana dell'argomento è appena cominciata.

### claude_full-L3-s02

*nota intera, spiegazione 3 di 8.* Fatti del livello: 13 sì, 10 in parte, 2 no (copertura 0,72) · errori 0 su 50 · analogie dichiarate 1 · segnalazioni del critico 0, errori introdotti 0 · 1132 parole (limite 1000) · Gulpease 54,7

L'enunciato riguarda le funzioni L di Dirichlet, L(s,χ)=Σχ(n)n⁻ˢ. Qui χ è un carattere di Dirichlet, cioè una funzione periodica e moltiplicativa sugli interi. Con χ banale si ritrova la zeta di Riemann. Il teorema afferma che, per ogni carattere primitivo χ, ogni zero di L(s,χ) nella striscia 0<Re(s)<1 sta sulla retta Re(s)=1/2. È l'ipotesi di Riemann generalizzata (GRH) per le funzioni L di Dirichlet, e contiene come caso particolare l'ipotesi classica.

Prima del contenuto, lo stato delle cose. Alpöge non ha diffuso una dimostrazione scritta. Ha pubblicato soltanto una formalizzazione in Lean di circa 17 milioni di righe, e ha scelto di non rilasciare un'esposizione generata dall'IA di oltre 250.000 pagine. Secondo Robin Zhang, in un giorno le comunità Lean e Mathlib hanno ricontrollato la prova con implementazioni indipendenti del kernel. Hanno anche verificato che le definizioni formali coincidono con quelle matematiche standard. Quel che segue riprende la ricostruzione di Zhang, che lui stesso dichiara scritta in gran parte da un'IA e non garantita come traduzione fedele del codice. Va presa come una mappa, non come la dimostrazione.

Il primo passo è classico: tradurre gli zeri in informazione sui primi. Si usa la funzione di von Mangoldt, Λ(n)=log p se n è una potenza di un primo p e 0 altrimenti, e la somma pesata S_χ(x)=Σ_{n≤x} Λ(n)χ(n)(x/n−1). La sua trasformata di Mellin è −L′(s,χ)/(s(s−1)L(s,χ)). Ogni zero di L diventa quindi un polo, e la crescita di S_χ controlla dove possono stare gli zeri. Si sottrae un termine principale, ottenendo somme corrette G_χ, e se ne prende una combinazione 𝒢_ψ a coefficienti positivi su tutte le potenze di un carattere ψ. La positività garantisce che zeri comuni a più funzioni L non si cancellino: il residuo in uno zero è una somma pesata positiva di molteplicità.

L'obiettivo diventa la Proposizione 1.2: per ogni η>0 esistono intervalli [Y,Y^{3/2}], con Y grande a piacere, su cui 𝒢_ψ(x)≤x^{1/2+η}. È una stima debole in due sensi: vale solo dall'alto e solo su certi intervalli. Basta lo stesso. Derivando molte volte la trasformata di Mellin, il nucleo d'integrazione diventa una densità gamma concentrata proprio sull'intervallo buono, e fuori basta una stima grossolana. Un eventuale polo con parte reale maggiore di 1/2 farebbe crescere le derivate troppo in fretta, in contraddizione con la stima. Le idee risalgono a Landau, Turán, Guinand e Weil. L'equazione funzionale sistema poi la metà sinistra della striscia.

Il cuore della prova, e la parte nuova, è come ottenere la stima per 𝒢_ψ. L'idea guida è la formula del prodotto: un intero algebrico non nullo molto divisibile ai primi finiti non può essere piccolo in tutti i valori assoluti archimedei. Alpöge costruisce numeri di questo tipo, cioè *periodi automorfi*: integrali di forme automorfe su gruppi unitari definiti su un campo CM ausiliario E, normalizzati in modo da stare in un campo di numeri K. Sono periodi di Bessel del tipo studiato da Gan, Gross e Prasad.

Ci sono poi due stime contrapposte. La prima è una stima dal basso delle valutazioni p-adiche di questi periodi. Tramite l'ortogonalità dei caratteri, che esprime le condizioni di Frobenius come somme di valori di caratteri, questa stima contiene proprio le somme sulle potenze dei primi. La seconda è una stima dall'alto delle grandezze archimedee, ottenuta dalle norme di Petersson (formule di Rallis e di Gan–Qiu–Takeda). Confrontandole si ricava un limite superiore per le somme sui primi.

Per avere abbastanza divisibilità si itera la corrispondenza theta di Weil e Howe: una forma viene sollevata m volte, tra gruppi unitari sempre più grandi, e ogni sollevamento aggiunge un contributo di divisibilità. Le identità «seesaw» di Kudla permettono di seguire il periodo lungo la catena.

Alpöge e Zhang propongono un'analogia con il metodo di Stepanov per contare i punti di una curva su un campo finito. Lì si costruisce un polinomio ausiliario che si annulla con alta molteplicità nei punti da contare, e si confronta il grado con l'ordine di annullamento. Qui il numero m di sollevamenti theta fa la parte della molteplicità, che sugli interi è difficile da produrre direttamente. Più sollevamenti danno più divisibilità, ma allargano gli spazi di forme e quindi gli errori. I due errori principali hanno grandezza circa x/m e m: scegliendo m≈√x si bilanciano, ed è da qui che esce l'esponente 1/2. Alpöge racconta che fu Claude a suggerire una catena di lunghezza √X.

Perché il confronto funzioni, il termine principale sottratto all'inizio deve ricomparire *esattamente* dal lato automorfo. Ricompare per via di un legame classico, dovuto a Chowla–Selberg e Anderson, tra i periodi delle varietà abeliane CM e le derivate logaritmiche delle funzioni L di Dirichlet. A questo si aggiungono le formule di dimensione di Weyl e quella di massa di Siegel. Zhang scrive esplicitamente l'identità che fa cancellare i termini principali. Si usano solo derivate logaritmiche nel punto 1, dove la non annullabilità è già nota, e Zhang osserva che questo evita la circolarità.

Il resto del lavoro, che è la maggior parte, serve a rendere rigoroso il confronto tra valutazioni finite e norme archimedee. Sul piano della geometria aritmetica, i periodi diventano mappe tra reticoli hermitiani, e serve stimarne il covolume. Per questo entrano la geometria di Arakelov sugli spazi di moduli di varietà abeliane (formule di Hilbert–Samuel aritmetiche, Zhang, Moriwaki), la teoria di Hodge p-adica integrale (Fargues, teoria di Dieudonné prismatica), le filtrazioni di Harder–Narasimhan e la disuguaglianza delle pendenze di Bost.

C'è poi il problema dei denominatori. Proiettare sugli autospazi di Hecke può introdurre denominatori, che dipendono dalle congruenze tra forme automorfe. Le congruenze si misurano attraverso le rappresentazioni di Galois associate, e alla fine attraverso certi gruppi di coomologia di Galois. Questi gruppi vanno limitati con strumenti come i numeri di Bernoulli e gli elementi di Stickelberger, la teoria delle deformazioni alla Wiles e Taylor–Wiles, il sistema di Eulero di Kato e la teoria di Iwasawa (l'annullamento dell'invariante μ di Ferrero–Washington). Alcuni «twist» eccezionali ammettono solo stime grossolane, ed è per questo che la stima vale soltanto su intervalli scelti con cura.

Infine, per scegliere i posti complessi di E in modo che non si addensino lungo le orbite di Frobenius, si adatta la costruzione di Behrend di insiemi grandi senza progressioni aritmetiche di tre termini.

Un'immagine riassuntiva, da prendere come analogia: la prova è una bilancia. Su un piatto c'è quanto un numero algebrico è divisibile per i primi, sull'altro quanto è grande, e la formula del prodotto impedisce che il primo piatto pesi troppo. La quantità di architettura serve a tarare la bilancia con un errore di ordine √x.

Lo stesso Alpöge dice di non padroneggiare ancora gran parte dell'argomento, in particolare le forme automorfe su gruppi di rango alto. Si aspetta semplificazioni rapide, e ritiene per esempio che il trucco di Behrend sia quasi certamente superfluo. Una comprensione umana completa della dimostrazione, insomma, è ancora da costruire.

### claude_full-L3-s03

*nota intera, spiegazione 4 di 8.* Fatti del livello: 14 sì, 9 in parte, 2 no (copertura 0,74) · errori 1 su 57 · analogie dichiarate 1 · segnalazioni del critico 0, errori introdotti 0 · 1011 parole (limite 1000) · Gulpease 55,3

Il risultato annunciato il 20 novembre 2026 da Levent Alpöge, ottenuto lavorando con Claude, è l'ipotesi di Riemann generalizzata per le funzioni L di Dirichlet. Per ogni carattere di Dirichlet primitivo χ, tutti gli zeri di L(s,χ) = Σ χ(n)n⁻ˢ nella striscia 0 < Re(s) < 1 stanno sulla retta Re(s) = 1/2. Con χ banale si ottiene l'ipotesi di Riemann classica.

Prima una premessa sullo stato delle cose. La dimostrazione esiste come formalizzazione in Lean di circa 17 milioni di righe. Alpöge ha scelto di non diffondere un'esposizione di oltre 250.000 pagine generata dall'IA. Secondo Robin Zhang, le comunità Lean e Mathlib hanno verificato la dimostrazione in un giorno, usando kernel indipendenti. Hanno anche controllato che le definizioni coincidano con quelle standard. Ciò che segue si basa però sulla ricostruzione di Zhang, scritta in larga parte con un'IA a partire dal codice. Zhang stesso avverte che non può garantirne la fedeltà.

**Primo passo: ridurre tutto a una stima sui primi.** La funzione di von Mangoldt Λ vale log p sulle potenze di un primo p e zero altrove. Con essa si considera

S_χ(x) = Σ_{n≤x} Λ(n)χ(n)(x/n − 1).

Il peso x/n − 1 rende semplice la trasformata di Mellin, che vale −L′(s,χ)/(s(s−1)L(s,χ)). Gli zeri di L diventano quindi poli, e stime sulla crescita di S_χ vincolano la posizione degli zeri. Una correzione lineare in x elimina il polo in s = 1. Si prende poi una combinazione 𝒢_ψ, a coefficienti positivi, di queste somme corrette per le potenze di un carattere ψ. La positività conta: se più funzioni L si annullano nello stesso punto, le molteplicità si sommano invece di cancellarsi.

L'obiettivo diventa questo: per ogni η > 0 esistono intervalli [Y, Y^{3/2}], con Y arbitrariamente grande, su cui 𝒢_ψ(x) ≤ x^{1/2+η}. È una stima debole, perché vale solo dall'alto e solo su certi intervalli, ma basta. In coordinate logaritmiche la trasformata diventa una trasformata di Laplace. Derivandola k volte, con k proporzionale a log Y, il nucleo diventa una densità gamma concentrata sull'intervallo buono; fuori basta una stima grossolana. Un polo con parte reale maggiore di 1/2 + η farebbe crescere le derivate più di quanto la stima consente. L'idea ricorda metodi di Landau e Turán. L'equazione funzionale esclude poi gli zeri a sinistra della retta critica.

**Secondo passo, il cuore: stimare dall'alto una somma sui primi.** Il principio è la formula del prodotto. Un intero algebrico non nullo molto divisibile ai primi finiti non può essere piccolo in tutti i valori assoluti archimedei. (Un'analogia: un intero non nullo divisibile per 2¹⁰⁰ vale almeno 2¹⁰⁰ in modulo.)

L'argomento costruisce dei numeri algebrici di questo tipo: i *periodi automorfi*. Sono integrali di forme automorfe su gruppi unitari, definiti su un campo CM ausiliario, normalizzati in modo da stare in un campo di numeri. Le loro valutazioni p-adiche sono stimate dal basso da espressioni che contengono proprio i termini della somma sui primi. Il collegamento passa per l'ortogonalità dei caratteri, che traduce condizioni sugli elementi di Frobenius in somme di valori di caratteri. Una stima dall'alto delle norme archimedee mette allora un tetto alla somma.

Per ottenere abbastanza divisibilità, si ripete m volte la corrispondenza theta di Weil e Howe, che trasporta forme automorfe da un gruppo unitario a un altro. Le identità "seesaw" di Kudla collegano il periodo iniziale a quello finale, e ogni sollevamento aggiunge divisibilità.

Qui entra un'analogia proposta dallo stesso Alpöge: il metodo di Stepanov per contare i punti di una curva su un campo finito. Stepanov usa un polinomio ausiliario che si annulla con alta molteplicità in quei punti. Sugli interi la molteplicità è difficile da trovare, perché corrisponderebbe a qualcosa come «derivare numeri interi». Il numero m di sollevamenti theta ne fa le veci.

Più sollevamenti, però, significano anche spazi più grandi e più errori. I due errori principali hanno taglia x/m e m. Scegliendo m vicino a √x, entrambi valgono circa √x: è da qui che nasce l'esponente 1/2. Alpöge racconta che fu Claude a suggerire per la catena di sollevamenti proprio questa lunghezza, √X.

Non basta però una stima di grandezza: bisogna recuperare *esattamente* il termine principale sottratto all'inizio. Le costanti tornano perché i periodi delle varietà abeliane CM sono legati alle derivate logaritmiche delle funzioni L di Dirichlet (Chowla–Selberg, Anderson). Combinandoli con la formula delle dimensioni di Weyl e con la formula di massa di Siegel si ottiene un'identità esatta, che cancella il termine principale.

**Il resto è macchinario, imponente.**
- **Valutazioni contro norme.** Per confrontare valutazioni finite e norme archimedee si usano reticoli di forme automorfe e geometria di Arakelov: pendenze di reticoli hermitiani, filtrazione di Harder–Narasimhan e disuguaglianza delle pendenze di Bost. Servono anche teoremi di Hilbert–Samuel aritmetici (Gillet–Soulé, Zhang, Moriwaki) su spazi di moduli di varietà abeliane, e la teoria di Hodge p-adica integrale.
- **Algebra lineare.** Un lemma garantisce che le immagini delle mappe definite dai periodi riempiano quasi tutto lo spazio duale.
- **Combinatoria additiva.** Alcuni posti complessi vanno scelti in modo che pochi cadano in un breve tratto di un'orbita di Frobenius. Per questo si adatta la costruzione di Behrend di insiemi senza progressioni aritmetiche di tre termini.
- **Coomologia di Galois.** Proiettare sugli autospazi di Hecke può introdurre denominatori che consumano la divisibilità guadagnata. Questi si controllano con le congruenze tra forme automorfe, tradotte in coomologia di Galois. Si stimano gruppi di Tate–Shafarevich con elementi di Stickelberger, metodi alla Kolyvagin, deformazioni alla Taylor–Wiles, il sistema di Eulero di Kato e la teoria di Iwasawa (annullarsi dell'invariante μ, Ferrero–Washington).

La libertà di scegliere gli intervalli [Y, Y^{3/2}] serve proprio qui, per tenere piccoli certi indici eccezionali.

**In sintesi, la catena logica è questa:**
1. Uno zero fuori dalla retta critica forzerebbe una crescita troppo rapida di somme pesate sui primi.
2. Queste somme controllano la divisibilità di numeri algebrici costruiti da periodi automorfi.
3. Il confronto tra divisibilità e grandezza archimedea, con circa √x sollevamenti theta, dà l'esponente 1/2 + η.

Alpöge stesso la considera una prima versione, lunghissima, che si aspetta venga semplificata presto. La comunità deve ancora capire che cosa contenga di davvero nuovo.

### claude_full-L3-s04

*nota intera, spiegazione 5 di 8.* Fatti del livello: 16 sì, 7 in parte, 2 no (copertura 0,78) · errori 0 su 48 · analogie dichiarate 0 · segnalazioni del critico 0, errori introdotti 0 · 1088 parole (limite 1000) · Gulpease 50,4

Il 20 novembre 2026 Levent Alpöge ha annunciato una dimostrazione dell'ipotesi di Riemann generalizzata per le funzioni L di Dirichlet, ottenuta lavorando con Claude. L'enunciato è questo: per ogni carattere di Dirichlet primitivo χ, ogni zero di L(s,χ) = Σ χ(n)n^(−s), prolungata meromorficamente, che cade nella striscia 0 < Re s < 1 sta sulla retta Re s = 1/2. Quando χ è il carattere banale si ottiene l'ipotesi di Riemann classica.

La dimostrazione esiste soprattutto come formalizzazione in Lean, di circa 17 milioni di righe. Dopo un giorno le comunità Lean e Mathlib riferivano di averla verificata con implementazioni indipendenti del kernel e di aver controllato che le definizioni usate coincidano con quelle standard. Un testo leggibile da un essere umano ancora non c'è. Alpöge ha scelto di non diffondere un'esposizione generata dall'IA di oltre 250.000 pagine e si aspetta forti semplificazioni. Quello che segue si basa sulla nota preliminare di Robin Zhang, scritta in gran parte da un'IA a partire dal codice; Zhang stesso avverte che non può garantirne la fedeltà.

**Primo passo: dagli zeri a somme sui primi.** Si considera la somma pesata S_χ(x) = Σ_{n≤x} Λ(n)χ(n)(x/n − 1), dove Λ è la funzione di von Mangoldt: vale log p sulle potenze del primo p e zero altrove. La sua trasformata di Mellin è −L′(s,χ)/(s(s−1)L(s,χ)), quindi ogni zero di L diventa un polo. Si sottrae un termine correttivo per eliminare l'eventuale polo in s = 1 e si ottiene G_χ. Poi si forma una combinazione 𝒢_ψ a coefficienti positivi delle G_χ, relative ai caratteri che inducono le potenze di un carattere ψ. La positività dei coefficienti è essenziale: i residui di uno zero comune a più funzioni L si sommano invece di cancellarsi.

Il risultato centrale è un enunciato debole in apparenza. Per ogni η > 0 esistono intervalli [Y, Y^(3/2)] arbitrariamente lontani su cui 𝒢_ψ(x) ≤ x^(1/2+η). Si ha dunque solo una maggiorazione, e solo su certi intervalli. Basta lo stesso, perché derivando k volte la trasformata, con k proporzionale a log Y, il nucleo u^k e^(−σu)/k! diventa una densità gamma concentrata proprio sull'intervallo buono. Un polo con parte reale maggiore di 1/2 imporrebbe a queste derivate una crescita incompatibile con la maggiorazione; la nota collega l'idea ai metodi di Landau e di Turán. L'equazione funzionale esclude poi gli zeri a sinistra della retta critica.

**Il cuore: divisibilità contro grandezza.** Per ottenere la maggiorazione si usa la formula del prodotto: un intero algebrico non nullo molto divisibile ai primi finiti non può essere piccolo in tutti i valori assoluti archimedei. Gli oggetti a cui si applica sono i *periodi automorfi*, cioè integrali di forme automorfe su gruppi unitari, del tipo dei periodi di Bessel di Gan–Gross–Prasad, normalizzati in modo da prendere valori in un campo di numeri K. Le minorazioni delle loro valutazioni p-adiche contengono, tramite l'ortogonalità dei caratteri, esattamente le somme sulle potenze dei primi. Le maggiorazioni archimedee vengono invece dalle norme di Petersson, calcolate con le formule di Rallis e di Gan–Qiu–Takeda. Più divisibilità obbliga a più grandezza, e questo limita le somme sui primi.

**Sollevamenti theta ripetuti e l'esponente 1/2.** Il sollevamento theta, di Weil e Howe, trasporta una forma automorfa da un gruppo unitario a un altro integrandola contro un nucleo theta. Ogni sollevamento aggiunge divisibilità, e la costruzione ne concatena m. L'analogia proposta dagli autori è con il metodo di Stepanov per contare i punti di una curva su un campo finito: lì si costruisce un polinomio ausiliario che si annulla con alta molteplicità nei punti, e qui m svolge il ruolo dell'ordine di annullamento. Alpöge osserva che sugli interi «la molteplicità è difficile da trovare», perché corrisponderebbe a derivare numeri interi; la catena di sollevamenti la imita. I due errori principali hanno grandezza x/m e m, quindi la scelta ottimale è m ≈ √x, che rende entrambi circa √x. Da qui viene l'esponente 1/2. Alpöge racconta che fu Claude a proporre catene di lunghezza √X.

**Il termine principale deve tornare esattamente.** Dalle G_χ è già stato sottratto un termine principale, quindi le costanti del confronto devono riprodurlo identicamente. Lo fanno grazie a tre ingredienti: i periodi delle varietà abeliane a moltiplicazione complessa, che Chowla–Selberg e Anderson collegano alle derivate logaritmiche delle funzioni L di Dirichlet; la formula delle dimensioni di Weyl; la formula di massa di Siegel. Un'identità esplicita mostra che i contributi delle valutazioni e delle norme danno proprio il termine principale.

**Reticoli e geometria di Arakelov.** In concreto non si confrontano singoli numeri ma reticoli. I periodi definiscono mappe b_α da reticoli di forme automorfe verso un reticolo duale C, e l'obiettivo è minorarne la pendenza media, cioè maggiorarne il covolume. Per questo servono tre cose. La prima sono stime sui covolumi dei reticoli di partenza, ottenute come sezioni di fibrati su compattificazioni di spazi di moduli di varietà abeliane, con la formula di Hilbert–Samuel aritmetica, i risultati di Zhang, Yuan e Moriwaki e la teoria di Hodge p-adica integrale. La seconda sono la filtrazione di Harder–Narasimhan e la disuguaglianza delle pendenze di Bost. La terza è un lemma di algebra lineare che garantisce che le immagini delle b_α riempiano quasi tutto lo spazio. Zhang lo paragona ai *tight frame* finiti, e anche questo è dichiarato come analogia.

**Denominatori e coomologia di Galois.** Proiettare sugli autospazi di Hecke può introdurre denominatori e quindi distruggere parte della divisibilità guadagnata. Questi denominatori misurano congruenze tra forme automorfe, e vengono controllati attraverso le rappresentazioni di Galois associate (Clozel–Harris–Labesse, Shin, Chenevier–Harris) e certi gruppi di coomologia di Galois localmente banali. Gli strumenti sono la dualità di Tate–Poitou, i metodi di Stickelberger e Kolyvagin per uno degli autospazi, la teoria delle deformazioni alla Taylor–Wiles e il sistema di Eulero di Kato per l'altro, la teoria di Iwasawa e il teorema di Ferrero–Washington. La libertà di scegliere l'intervallo [Y, Y^(3/2)] serve qui a evitare alcuni "twist" eccezionali. Un'idea di combinatoria additiva, la costruzione di Behrend di insiemi senza progressioni aritmetiche di tre termini, serve invece a scegliere i posti complessi in modo che pochi cadano in segmenti brevi delle orbite di Frobenius.

In sintesi, l'architettura combina tre parti: un argomento analitico classico, che trasforma maggiorazioni unilaterali sui primi in assenza di zeri; un meccanismo aritmetico alla Stepanov, in cui la divisibilità accumulata con √x sollevamenti theta si scontra con la grandezza; e un apparato tecnico vastissimo che tiene sotto controllo ogni costante. Alpöge stesso considera la propria comprensione parziale e prevede che l'argomento verrà presto molto semplificato. La garanzia di correttezza oggi viene dalla verifica in Lean, non da una lettura umana.

### claude_full-L3-s05

*nota intera, spiegazione 6 di 8.* Fatti del livello: 16 sì, 7 in parte, 2 no (copertura 0,78) · errori 0 su 61 · analogie dichiarate 1 · segnalazioni del critico 1, errori introdotti 0 · 1164 parole (limite 1000) · Gulpease 53,8

Il risultato annunciato da Levent Alpöge il 20 novembre 2026 è l'ipotesi di Riemann generalizzata per le funzioni L di Dirichlet. Per ogni carattere di Dirichlet primitivo χ, ogni zero di L(s,χ) nella striscia 0 < Re(s) < 1 sta sulla retta Re(s) = 1/2. Il caso del carattere banale è l'ipotesi di Riemann classica per ζ(s). L'argomento è stato sviluppato insieme a Claude e pubblicato solo come formalizzazione in Lean, di circa 17 milioni di righe. Secondo la nota preliminare di Robin Zhang, in un giorno le comunità Lean e Mathlib hanno verificato la dimostrazione con implementazioni indipendenti del kernel di Lean, e hanno controllato che le definizioni formali coincidano con quelle matematiche standard. Una dimostrazione leggibile da un essere umano invece non esiste ancora. La ricostruzione che segue viene dalla nota di Zhang, che è in gran parte scritta da un'IA a partire dal codice. Zhang stesso avverte di non poterne garantire la fedeltà al codice Lean.

**Primo passo: dagli zeri a una disuguaglianza sui primi.** Si considera la somma pesata

S_χ(x) = Σ_{n≤x} Λ(n)χ(n)(x/n − 1),

dove Λ(n) vale log p sulle potenze del primo p e 0 altrove. La sua trasformata di Mellin è −L′(s,χ)/(s(s−1)L(s,χ)). Uno zero di L nella striscia diventa quindi un polo della trasformata. Si sottrae un termine principale, per eliminare il polo in s = 1, e si ottiene una funzione corretta G_χ. Le G_χ relative alle potenze di un carattere ψ si combinano poi con coefficienti positivi in una funzione 𝒢_ψ.

La positività è cruciale: se più funzioni L si annullano nello stesso punto, le molteplicità si sommano e non possono cancellarsi. Il cuore analitico è la Proposizione 1.2. Per ogni η > 0 esistono intervalli [Y, Y^{3/2}], con Y arbitrariamente grande, sui quali 𝒢_ψ(x) ≤ x^{1/2+η}.

Colpisce quanto poco si chieda: solo una maggiorazione, e solo su certi intervalli. Basta lo stesso, per questa ragione. Si passa a coordinate logaritmiche e si deriva k volte la trasformata. Il peso che compare nell'integrale diventa una densità di tipo gamma, che per k proporzionale a log Y si concentra proprio sull'intervallo dove vale la stima. Spostando il punto di derivazione, il polo più vicino domina le derivate di ordine alto, in uno spirito vicino al metodo di Turán. Un polo con parte reale maggiore di 1/2 + η produrrebbe una crescita incompatibile con la stima. L'altra metà della striscia segue dall'equazione funzionale. Questo passo è elementare, e la nota lo dimostra per esteso.

**Secondo passo: maggiorare somme di primi con la divisibilità.** L'idea guida è la formula del prodotto: un intero algebrico non nullo molto divisibile ai primi finiti non può essere piccolo in tutte le valutazioni archimedee. Un'analogia elementare è che un intero non nullo divisibile per p^N ha valore assoluto almeno p^N.

I numeri algebrici in gioco sono *periodi automorfi*. Si tratta di integrali di forme automorfe su gruppi unitari definiti su un campo CM ausiliario E, normalizzati in modo da prendere valori in un campo di numeri K. Le valutazioni p-adiche di questi periodi si stimano dal basso con quantità che contengono proprio le somme sulle potenze dei primi. Le potenze di p che contribuiscono sono selezionate da condizioni sul Frobenius, che l'ortogonalità dei caratteri, come in Dirichlet, ritraduce in combinazioni di G_χ. Le dimensioni archimedee si stimano invece dall'alto tramite le norme di Petersson. Confrontando le due stime si ottiene una maggiorazione della somma aritmetica.

Perché il confronto funzioni, i termini principali devono cancellarsi *esattamente*. Le costanti arrivano da fonti classiche: la formula di Chowla–Selberg e i risultati di Anderson, che legano i periodi delle varietà abeliane CM alle derivate logaritmiche delle L di Dirichlet; la formula delle dimensioni di Weyl; la formula di massa di Siegel. L'identità (4.5) della nota mostra che queste costanti riproducono proprio il termine principale sottratto.

**Terzo passo: iterare il sollevamento theta.** Per ottenere abbastanza divisibilità si applica m volte la corrispondenza theta di Weil e Howe, che trasporta forme automorfe da un gruppo unitario a un altro. Le identità "seesaw" di Kudla permettono di seguire il periodo attraverso tutta la catena. Ogni sollevamento aggiunge un contributo alla divisibilità.

Alpöge propone qui un'analogia con il metodo di Stepanov per contare i punti delle curve sui campi finiti. Lì si costruisce un polinomio ausiliario che si annulla con molteplicità alta nei punti da contare. Qui il numero m di sollevamenti fa la parte della molteplicità, cioè dell'ordine di annullamento, che sugli interi è difficile da ottenere direttamente.

Più sollevamenti però ingrandiscono gli spazi di forme automorfe e quindi gli errori. Alla fine i due errori principali hanno dimensione x/m e m. Scegliendo m ≈ √x si bilanciano, e da qui nasce l'esponente 1/2. Alpöge racconta che fu Claude a suggerire una catena di lunghezza √X.

**La macchina che regge tutto.** Rendere rigorosi questi confronti richiede moltissima matematica, e la nota la censisce con cura.

- **Geometria di Arakelov.** I periodi definiscono mappe tra reticoli di forme automorfe. Il loro covolume si controlla con le pendenze di Arakelov, la filtrazione di Harder–Narasimhan, la disuguaglianza delle pendenze di Bost, e le altezze su compattificazioni di spazi di moduli di varietà abeliane (Zhang, Moriwaki, Yuan). Al controllo dei contributi ai primi finiti contribuisce anche la teoria di Hodge p-adica integrale (Fargues, Anschütz–Le Bras).
- **Coomologia di Galois.** Proiettare sugli autospazi di Hecke può introdurre denominatori, che misurano congruenze tra forme automorfe. Questi si controllano attaccando rappresentazioni di Galois alle forme automorfe e stimando gruppi di coomologia di Galois "localmente banali". Gli strumenti sono la dualità di Tate–Poitou, gli elementi di Stickelberger, la teoria delle deformazioni alla Wiles e Taylor–Wiles, il sistema di Eulero di Kato, la teoria di Iwasawa e l'annullarsi dell'invariante μ (Ferrero–Washington).
- **Combinatoria additiva.** Gli insiemi di Behrend, privi di progressioni aritmetiche di tre termini, servono a scegliere i posti complessi di E in modo che pochi cadano in brevi segmenti di orbite di Frobenius.

La libertà di scegliere l'intervallo [Y, Y^{3/2}] serve proprio a evitare alcuni "twist" di Tate eccezionali, per i quali si ha solo una stima grossolana. È per questo che la stima principale vale solo su intervalli.

**Lo stato delle cose.** Alpöge sottolinea di non padroneggiare ancora alcune parti, in particolare le forme automorfe su gruppi di rango alto. Ritiene che l'argomento contenga scelte subottimali e si aspetta presto dimostrazioni molto più brevi. Considera alcuni trucchi, come l'uso di Behrend, intuitivamente non necessari. Ha generato un'esposizione automatica di oltre 250.000 pagine e ha scelto di non diffonderla. Va segnalato anche che lo stesso giorno Ravi Vakil ha annunciato una dimostrazione indipendente, attribuita ad Alessandro Masullo e ottenuta senza IA; le fonti non ne descrivono il contenuto.

In sintesi: l'enunciato risulta verificato formalmente, e la strategia è chiara a grandi linee. Si riduce GRH a una maggiorazione per somme sui primi, e la si ottiene confrontando divisibilità e grandezza di periodi automorfi resi via via più divisibili da catene di sollevamenti theta di lunghezza circa √x. La comprensione umana dei dettagli, invece, è appena cominciata.

### claude_full-L3-s06

*nota intera, spiegazione 7 di 8.* Fatti del livello: 16 sì, 7 in parte, 2 no (copertura 0,78) · errori 0 su 53 · analogie dichiarate 1 · segnalazioni del critico 0, errori introdotti 0 · 1055 parole (limite 1000) · Gulpease 56,9

Il teorema annunciato riguarda le funzioni L di Dirichlet. Un carattere di Dirichlet χ è una funzione periodica e moltiplicativa sugli interi, e L(s,χ) = Σ χ(n)n^{-s} si estende meromorficamente a tutto il piano complesso. L'enunciato dimostrato è questo: per ogni carattere primitivo χ, ogni zero di L(s,χ) nella striscia 0 < Re(s) < 1 ha parte reale 1/2. Il caso χ = 1 è la funzione zeta, quindi l'ipotesi di Riemann classica è inclusa.

Prima del contenuto, lo stato delle cose. Alpöge ha pubblicato soltanto una formalizzazione in Lean, di circa 17 milioni di righe. Non ha diffuso un'esposizione generata dall'IA di oltre 250.000 pagine, che lui stesso giudica illeggibile. Il resoconto leggibile che seguo è una nota di Robin Zhang, scritta in gran parte con l'aiuto di un'altra IA. Zhang avverte esplicitamente di non poter garantire che sia una traduzione fedele del codice. Riferisce però che le comunità di Lean e Mathlib hanno verificato la dimostrazione con implementazioni indipendenti del kernel di Lean, e che le definizioni in Lean coincidono con quelle standard. Quello che segue è quindi l'architettura dell'argomento così come è stata ricostruita.

Il primo passo è classico: trasformare gli zeri in una stima su somme sui primi. Si usa la funzione di von Mangoldt Λ(n), che vale log p se n è una potenza di un primo p e 0 altrimenti. Si considera la somma pesata S_χ(x) = Σ_{n≤x} Λ(n)χ(n)(x/n − 1). La sua trasformata di Mellin è −L'(s,χ)/(s(s−1)L(s,χ)), per cui ogni zero di L diventa un polo. Dopo aver corretto il polo spurio in s = 1, l'argomento costruisce una combinazione 𝒢_ψ a coefficienti positivi delle somme associate alle potenze di un carattere ψ. Il cuore analitico è la Proposizione 1.2: per ogni η > 0 esistono Y arbitrariamente grandi tali che 𝒢_ψ(x) ≤ x^{1/2+η} su tutto l'intervallo [Y, Y^{3/2}].

È una stima debole sotto due aspetti. È solo dall'alto e vale solo su certi intervalli. Basta comunque, per due ragioni. La prima è la positività dei coefficienti: le molteplicità di uno zero comune a più funzioni L si sommano, quindi i residui non possono cancellarsi. La seconda è un trucco di derivazione. Se si deriva k volte la trasformata, con k proporzionale a log Y, il peso u^k e^{-σu}/k! diventa una densità gamma concentrata proprio sull'intervallo in cui vale la stima. Un polo con parte reale maggiore di 1/2 + η forzerebbe invece una crescita incompatibile con la stima. Zhang collega questo passo alle idee di Landau e di Turán. L'equazione funzionale esclude poi gli zeri a sinistra della retta critica.

Il secondo passo è la parte nuova: ottenere quella stima dall'aritmetica di oggetti automorfi. Il principio guida è la formula del prodotto. Un intero algebrico non nullo molto divisibile ai primi finiti non può essere piccolo in tutti i valori assoluti archimedei. L'argomento costruisce allora dei "periodi" P_α(f,g). Sono integrali di forme automorfe su gruppi unitari definiti su un campo CM ausiliario E, normalizzati in modo da assumere valori in un campo di numeri. Attraverso l'ortogonalità dei caratteri, le loro valutazioni p-adiche sono limitate dal basso da termini del tipo (a/p^ν − w)_+, cioè proprio dagli addendi delle somme sui primi. Le loro dimensioni archimedee sono invece limitate dall'alto tramite le norme di Petersson, calcolate con la formula del prodotto interno di Rallis. Confrontando le due stime si ottiene un limite superiore per le somme sui primi.

C'è un punto delicato: il termine principale deve risultare identico, costante compresa. Questo succede grazie a relazioni classiche. I periodi delle varietà abeliane CM sono legati alle derivate logaritmiche delle funzioni L di Dirichlet (Chowla–Selberg, Anderson). A queste si aggiungono la formula delle dimensioni di Weyl e la formula di massa di Siegel. Il risultato è un'identità esatta, D_div − A·L_w = M_tot, che cancella il termine principale e lascia solo l'errore.

L'idea chiave è la ripetizione della corrispondenza theta. Ogni sollevamento theta trasporta una forma automorfa da un gruppo unitario a uno più grande e aggiunge divisibilità ai periodi. Le identità "seesaw" di Kudla permettono di seguire il periodo lungo tutta la catena. Alpöge propone un'analogia, e va presa come tale: il metodo di Stepanov per contare i punti di una curva su un campo finito. Lì si costruisce un polinomio ausiliario che si annulla con alta molteplicità nei punti da contare. Sugli interi la molteplicità è difficile da ottenere, perché sarebbe come "derivare i numeri interi". In questa analogia, il numero m di sollevamenti fa la parte dell'ordine di annullamento.

Più sollevamenti significano più divisibilità, ma anche spazi più grandi e stime più costose. I due errori principali hanno taglia x/m e m. Scegliere m ≈ √x li bilancia entrambi a circa √x. Secondo Zhang, è da qui che viene l'esponente 1/2.

Il resto è un'impalcatura imponente, che il lettore può immaginare come un controllo di "volumi" di reticoli. Per confrontare valutazioni finite e norme archimedee servono reticoli interi di forme automorfe. I loro covolumi si stimano con la geometria di Arakelov: formula di Hilbert–Samuel aritmetica (Gillet–Soulé, Zhang, Moriwaki), spazi di moduli di varietà abeliane, teoria di Hodge p-adica integrale, fino alla teoria di Dieudonné prismatica. Le "pendenze" dei reticoli si trasferiscono con la disuguaglianza di Bost e con la filtrazione di Harder–Narasimhan. Un lemma di algebra lineare, vicino ai tight frame, garantisce che i funzionali-periodo ricoprano quasi tutto lo spazio duale. Una variante della costruzione di Behrend, quella degli insiemi senza progressioni aritmetiche di tre termini, sceglie i posti complessi di E senza troppe concentrazioni lungo le orbite di Frobenius.

Infine, proiettare sugli autospazi di Hecke può introdurre denominatori che mangiano la divisibilità guadagnata. Questi denominatori riflettono congruenze tra forme automorfe. Si misurano tramite rappresentazioni di Galois e gruppi di coomologia di Galois, controllati a loro volta con elementi di Stickelberger, sistemi di Eulero di Kato, metodi alla Taylor–Wiles e teoria di Iwasawa (annullamento dell'invariante μ di Ferrero–Washington). Qui torna utile la libertà di scegliere l'intervallo [Y, Y^{3/2}]: lo si sceglie in modo da evitare certi indici "eccezionali".

Un'ultima avvertenza onesta. Alpöge stesso dichiara di non padroneggiare ancora tutta la matematica coinvolta. Ritiene di aver fatto scelte subottimali e si aspetta semplificazioni rapide. Secondo lui, alcune descrizioni nella sua cronologia "potrebbero non avere alcun senso" e andranno corrette. Allo stato attuale, la garanzia di correttezza viene dalla verifica in Lean, non da una comprensione umana completa dell'argomento.

### claude_full-L3-s07

*nota intera, spiegazione 8 di 8.* Fatti del livello: 16 sì, 7 in parte, 2 no (copertura 0,78) · errori 0 su 55 · analogie dichiarate 1 · segnalazioni del critico 0, errori introdotti 0 · 1057 parole (limite 1000) · Gulpease 54,9

Levent Alpöge ha annunciato il 20 novembre 2026 una dimostrazione dell'ipotesi di Riemann generalizzata per le funzioni L di Dirichlet. L'enunciato è questo: per ogni carattere di Dirichlet primitivo χ, tutti gli zeri di L(s,χ) nella striscia 0 < Re(s) < 1 stanno sulla retta Re(s) = 1/2. Il caso del carattere banale è l'ipotesi di Riemann classica per ζ.

Prima della matematica, conviene chiarire lo stato dei fatti. Alpöge ha pubblicato solo una formalizzazione in Lean, di circa 17 milioni di righe. Un'esposizione generata da Claude, di oltre 250.000 pagine, non è stata diffusa. Secondo Robin Zhang, in un giorno le comunità Lean e Mathlib hanno verificato la dimostrazione con implementazioni indipendenti del kernel. Hanno anche controllato che le definizioni usate coincidano con quelle standard. La descrizione che segue viene però dalla nota di Zhang, che è una ricostruzione: un'IA ha estratto dal codice una dimostrazione leggibile, poi riscritta da Zhang, il quale avverte di non poterne garantire la fedeltà al codice. Lo stesso Alpöge dice di non padroneggiare ancora alcune parti dell'argomento e si aspetta semplificazioni.

Il primo passo porta dagli zeri alle somme sui primi. Si usano le somme pesate S_χ(x) = Σ_{n≤x} Λ(n)χ(n)(x/n − 1), dove Λ(n) vale log p sulle potenze del primo p e 0 altrove. La loro trasformata di Mellin è −L'(s,χ)/(s(s−1)L(s,χ)), quindi ogni zero di L diventa un polo. Si corregge il polo in s = 1 e si combinano, con coefficienti positivi, le somme corrette relative alle potenze di un carattere ψ. Il cuore tecnico è allora una sola stima: questa combinazione è al più x^{1/2+η} per ogni x in intervalli [Y, Y^{3/2}], con Y arbitrariamente grande.

La stima è debole in due sensi, perché vale solo dall'alto e solo su certi intervalli, ma basta comunque. Grazie alla positività dei coefficienti, i residui di uno zero comune a più funzioni L si sommano invece di cancellarsi. Derivando molte volte la trasformata, il peso si concentra su un singolo intervallo. Il polo più vicino al punto scelto domina allora le derivate, e questo contraddice la stima se esiste uno zero con parte reale maggiore di 1/2. L'equazione funzionale esclude poi gli zeri a sinistra della retta critica. Questa parte è analisi classica, nello spirito di Landau, Turán, Guinand e Weil.

Il secondo passo contiene l'idea aritmetica. Il principio guida è la formula del prodotto: un intero algebrico non nullo, molto divisibile ai primi finiti, non può essere piccolo in tutti i valori assoluti archimedei. Un'analogia mia, solo per orientarsi: un intero non nullo divisibile per 2¹⁰⁰ ha valore assoluto almeno 2¹⁰⁰.

Gli oggetti a cui si applica il principio sono periodi automorfi. Si tratta di integrali di forme automorfe su gruppi unitari, normalizzati in modo da prendere valori in un campo di numeri K. Le stime dal basso delle loro valutazioni p-adiche contengono proprio le somme sulle potenze dei primi. Le stime dall'alto archimedee limitano quindi quelle somme.

In pratica il confronto non si fa su un singolo numero ma su reticoli. I periodi definiscono mappe integrali da reticoli di forme automorfe verso un reticolo duale C. La disuguaglianza diventa così una stima della pendenza media di C, cioè del suo covolume, nel linguaggio della geometria di Arakelov.

Il terzo passo consiste nell'iterare il sollevamento theta. La divisibilità di un solo periodo non basta. La dimostrazione applica m volte la corrispondenza theta di Weil e Howe, trasportando forme fra gruppi unitari di dimensione crescente. Le identità "seesaw" di Kudla collegano il periodo iniziale ai successivi, e ogni sollevamento aggiunge divisibilità.

L'analogia indicata dalle fonti è il metodo di Stepanov per contare i punti di una curva su un campo finito. Lì si costruisce un polinomio ausiliario che si annulla con alta molteplicità in quei punti, e si confronta il grado con l'ordine di annullamento. Qui il numero m di sollevamenti fa la parte della molteplicità. Sugli interi, scrive Alpöge, la molteplicità è difficile da trovare: è "come derivare numeri interi".

Più sollevamenti, però, ingrandiscono anche gli spazi di forme. I due errori principali hanno ordine x/m e m. Scegliendo m vicino a √x, entrambi restano vicini a √x: è da qui che nasce l'esponente 1/2. Alpöge racconta che fu Claude a suggerire per la catena la lunghezza √X.

Un punto delicato è che le somme sono già private del loro termine principale. I confronti devono quindi riprodurre esattamente le costanti. Ci riescono grazie a formule classiche. Chowla–Selberg e Anderson legano i periodi di varietà abeliane a moltiplicazione complessa (CM) alle derivate logaritmiche delle funzioni L di Dirichlet. La formula di Rallis dà le norme dei sollevamenti. La formula di Weyl e la formula di massa di Siegel forniscono le dimensioni degli spazi. Un'identità esplicita mostra infine che il termine principale si cancella esattamente.

Il resto della dimostrazione serve a controllare gli errori, ed è qui che compare una quantità enorme di matematica:

- **Covolumi dei reticoli.** Si usano spazi di moduli di varietà abeliane, la formula di Hilbert–Samuel aritmetica (Gillet–Soulé, Zhang, Moriwaki) e la teoria di Hodge p-adica integrale.
- **Pendenze.** Un lemma di algebra lineare garantisce che le immagini delle mappe dei periodi riempiano quasi tutto lo spazio. La filtrazione di Harder–Narasimhan e la disuguaglianza di Bost trasferiscono poi le stime di pendenza.
- **Scelta dei posti complessi.** Bisogna che pochi posti cadano in brevi segmenti di orbite di Frobenius. Per questo si adatta la costruzione di Behrend di insiemi senza progressioni aritmetiche di tre termini.
- **Denominatori.** Proiettare sugli autospazi di Hecke può introdurre denominatori che consumano la divisibilità. Per controllarli si passa alle rappresentazioni di Galois e si stimano gruppi di coomologia di Galois. Gli strumenti sono la dualità di Tate–Poitou, gli elementi di Stickelberger, le deformazioni alla Wiles e Taylor–Wiles, il sistema di Eulero di Kato e la teoria di Iwasawa con il teorema di Ferrero–Washington.

Alcuni casi eccezionali ammettono solo stime grossolane, valide quando un certo indice è piccolo rispetto a x. Per questo la stima vale solo su intervalli scelti con cura, ed è per questo che il primo passo è costruito per accontentarsi di intervalli.

In sintesi, la strategia riduce l'ipotesi di Riemann a una disuguaglianza fra divisibilità p-adica e grandezza archimedea di periodi automorfi, amplificata da circa √x sollevamenti theta. La correttezza è garantita dalla verifica in Lean. Una comprensione umana dell'argomento, per ammissione degli stessi protagonisti, è ancora da costruire.

### claude_overview-L3-s00

*panoramica, spiegazione 1 di 8.* Fatti del livello: 13 sì, 7 in parte, 5 no (copertura 0,66) · errori 2 su 49 · analogie dichiarate 1 · segnalazioni del critico 1, errori introdotti 1 · 1031 parole (limite 1000) · Gulpease 54,3

Alpöge annuncia una dimostrazione dell'ipotesi di Riemann generalizzata (GRH) per le funzioni L di Dirichlet. Un carattere di Dirichlet χ è una funzione periodica e moltiplicativa da ℤ a ℂ. Dirichlet li introdusse per distinguere le progressioni aritmetiche e dimostrare che ognuna, se primo termine e ragione sono coprimi, contiene infiniti primi. La funzione L(s,χ) = Σ χ(n) n^(−s), definita per Re s > 1, si estende meromorficamente a tutto ℂ. L'enunciato dimostrato, formulato già da Piltz nel 1884, è questo: per ogni carattere primitivo χ, ogni zero di L(s,χ) nella striscia 0 < Re s < 1 sta sulla retta Re s = 1/2. Per il carattere banale L è la zeta di Riemann, quindi il risultato comprende l'ipotesi di Riemann classica. Alpöge si aspetta che il metodo arrivi anche all'ipotesi "estesa", ma questo non fa parte dell'annuncio.

Il primo passo traduce gli zeri in somme sui primi. Si usa la funzione di von Mangoldt Λ(n), che vale log p se n = p^k ed è nulla altrimenti. Vale −L′/L(s,χ) = Σ Λ(n)χ(n) n^(−s), quindi uno zero di L diventa un polo della derivata logaritmica. La dimostrazione lavora con la media pesata S_χ(x) = Σ_{n≤x} Λ(n)χ(n)(x/n − 1). Il peso è scelto perché la trasformata di Mellin sia semplice, cioè −L′/(s(s−1)L). Uno zero nella striscia critica produce un polo di questa trasformata, e stime sulla crescita di S_χ(x) vincolano dove possono stare i poli. Prima si sottrae un termine principale. Per la zeta, per esempio, si definisce G(x) = Σ Λ(n)(x/n − 1) − x log x + (1+γ)x, che elimina il polo in s = 1, dove non ci sono zeri. Poi, fissato un carattere ψ di ordine r, si sommano con pesi positivi le funzioni corrette relative a tutte le potenze di ψ. Uno zero di una qualunque di queste L dà allora un polo con residuo positivo, e gli zeri di funzioni diverse non possono cancellarsi.

Il risultato analitico centrale (Proposizione 1.2 nella nota di Zhang) è sorprendentemente debole. Per ogni η > 0 esistono intervalli [Y, Y^(3/2)], con Y arbitrariamente grande, su cui la somma combinata G_ψ(x) è al più x^(1/2+η). È solo una maggiorazione, non un controllo del valore assoluto, e vale solo su certi intervalli. Un argomento che Zhang collega a Landau, Guinand, Turán e Weil mostra che basta comunque a escludere zeri fuori dalla retta critica.

La novità sta nel modo di ottenere quella maggiorazione. L'idea guida è la formula del prodotto: se un intero algebrico non nullo è molto divisibile ai primi finiti, i suoi valori assoluti archimedei non possono essere tutti piccoli. Come analogia, un intero non nullo divisibile per p^k ha modulo almeno p^k. Gli oggetti a cui si applica questa idea sono i *periodi automorfi*, cioè integrali di forme automorfe su gruppi unitari, normalizzati in modo da prendere valori in un campo di numeri. Le stime dal basso della loro divisibilità contengono potenze di primi soggette a condizioni di Frobenius. L'ortogonalità dei caratteri riscrive queste condizioni proprio come le somme G_χ. Una stima dall'alto della grandezza archimedea dei periodi diventa così una stima dall'alto delle somme sui primi, e serve un errore vicino a √x.

Qui entra il legame con Stepanov, che Alpöge sottolinea. Nella dimostrazione dell'ipotesi di Riemann sui campi di funzioni, l'argomento di Stepanov usa una molteplicità: si costruiscono oggetti che si annullano con ordine elevato. Sugli interi la molteplicità è difficile da ottenere, perché equivarrebbe, dice Alpöge, a "derivare i numeri interi". Il sostituto è una catena di *sollevamenti theta*. La corrispondenza theta (Weil, Howe) trasporta una forma automorfa da un gruppo unitario a un altro, integrandola contro un nucleo theta. Si parte da un periodo di Bessel, nel senso di Gan–Gross–Prasad, che accoppia due forme, e si sollevano m volte entrambi gli argomenti: U(X₀) → U(X₁) → … → U(X_m). Le identità "seesaw" di Kudla collegano il periodo iniziale all'accoppiamento finale. Ogni sollevamento aggiunge divisibilità e imita un grado di molteplicità. L'esponente 1/2 nasce da un bilanciamento: i due errori principali hanno grandezza x/m e m, e scegliendo m vicino a √x entrambi diventano circa √x. Secondo Alpöge, proprio questa lunghezza della catena, √X, è stata suggerita da Claude.

Far funzionare il bilancio richiede un apparato enorme, che la nota di Zhang descrive per sommi capi. Le norme dei sollevamenti si calcolano con le formule di Rallis e di Gan–Qiu–Takeda, che le esprimono tramite valori speciali di funzioni L. Le dimensioni degli spazi si ottengono con la formula di Weyl e con conteggi di reticoli hermitiani del tipo della formula di massa di Siegel. I periodi di varietà abeliane CM, collegati da Chowla–Selberg alle derivate logaritmiche delle L di Dirichlet, servono a ritrovare esattamente il termine principale sottratto all'inizio. Per confrontare divisibilità e grandezza si lavora con reticoli di forme automorfe e se ne stimano i covolumi con la geometria di Arakelov. Gli strumenti sono le formule di Hilbert–Samuel aritmetiche, la filtrazione di Harder–Narasimhan, la disuguaglianza di pendenza di Bost e risultati di teoria di Hodge p-adica integrale (Fargues, Anschütz–Le Bras). Proiettare sugli autospazi di Hecke può introdurre denominatori che mangiano divisibilità. Questi si controllano con rappresentazioni di Galois, congruenze tra forme e argomenti di deformazione alla Wiles e Taylor–Wiles, insieme al sistema di Eulero di Kato e alla teoria di Iwasawa (con il teorema di Ferrero–Washington). Perfino la combinatoria additiva compare: una variante della costruzione di Behrend di insiemi grandi senza progressioni aritmetiche di tre termini serve a scegliere bene certi posti complessi. Alpöge stesso la considera intuitivamente superflua.

Lo stato attuale va descritto con cautela. Secondo Alpöge, la dimostrazione è stata trovata con Claude tra ottobre e il 16 novembre 2026 e formalizzata interamente in Lean "senza assunzioni". Al momento è pubblica solo sotto forma di codice Lean, distribuito in quattordici archivi. Un testo leggibile da esseri umani non esiste ancora, e Alpöge ha scelto di non pubblicare una versione automatica illeggibile di oltre 250 000 pagine. Ammette di non padroneggiare ancora tutte le parti del ragionamento, in particolare quelle sulle forme automorfe di rango alto, e si aspetta semplificazioni drastiche a breve. La nota di Zhang, che è una prima ricostruzione umana della struttura, si definisce "preliminare" e parla di "dimostrazione proposta".

### claude_overview-L3-s01

*panoramica, spiegazione 2 di 8.* Fatti del livello: 13 sì, 9 in parte, 3 no (copertura 0,70) · errori 0 su 56 · analogie dichiarate 2 · segnalazioni del critico 0, errori introdotti 0 · 1088 parole (limite 1000) · Gulpease 53,7

Il risultato annunciato da Levent Alpöge il 20 novembre 2026 riguarda le funzioni L di Dirichlet. Un carattere di Dirichlet χ è una funzione periodica e moltiplicativa sugli interi, che Dirichlet introdusse per distinguere tra loro le progressioni aritmetiche. A χ si associa la serie L(s,χ) = Σ χ(n)/nˢ, che converge per Re(s) > 1 e si estende in modo meromorfo a tutto il piano complesso. Per il carattere banale si ottiene la funzione zeta di Riemann. L'ipotesi di Riemann generalizzata, in questa forma già presente in Piltz nel 1884, afferma che per ogni carattere primitivo tutti gli zeri di L(s,χ) nella striscia 0 < Re(s) < 1 stanno sulla retta Re(s) = 1/2. È questo che si dichiara dimostrato. Alpöge si aspetta che il metodo arrivi, con più tempo, anche all'ipotesi di Riemann "estesa", ma questa non fa parte dell'annuncio.

Sullo stato della dimostrazione conviene essere precisi. Alpöge dice di averla trovata lavorando con Claude e di averla formalizzata con Claude nell'assistente di dimostrazione Lean, senza ipotesi aggiuntive. Ha reso pubblico soltanto il codice Lean. Un testo leggibile non esiste ancora: la versione estesa generata automaticamente superava le 250.000 pagine. Lui stesso ammette di non padroneggiare ancora gran parte della matematica coinvolta e prevede semplificazioni rapide. La nota di Robin Zhang, su cui si basa quasi tutto ciò che segue, si presenta come «preliminare» e parla di dimostrazione «proposta».

**La riduzione a una stima sui primi.** Il punto di partenza è classico. Per Re(s) > 1 la derivata logaritmica −L′/L è la serie Σ Λ(n)χ(n)n⁻ˢ, dove Λ è la funzione di von Mangoldt: vale log p se n è una potenza del primo p, e 0 altrimenti. Gli zeri di L diventano poli di −L′/L.

La dimostrazione usa una media pesata, S_χ(x) = Σ_{n≤x} Λ(n)χ(n)(x/n − 1). Il peso è scelto perché la trasformata di Mellin di S_χ sia esattamente −L′(s,χ)/(s(s−1)L(s,χ)). In questo modo una stima sulla crescita di S_χ(x) si traduce in informazioni sui poli, cioè sugli zeri. Si sottrae poi un termine principale, ottenendo G_χ, così da eliminare il polo spurio in s = 1.

C'è però un rischio: zeri di funzioni L diverse potrebbero cancellarsi a vicenda. Per evitarlo, dato un carattere ψ di ordine r, si combinano con coefficienti positivi le G_χ di tutti i caratteri che inducono le potenze di ψ, ottenendo una funzione G_ψ. In ogni zero ρ fuori dalla retta critica, il residuo è allora 1/(ρ(1−ρ)) per una somma positiva di molteplicità. Nessuna cancellazione è possibile.

Tutto si riduce così alla Proposizione 1.2: per ogni η > 0 esistono intervalli [Y, Y^{3/2}], con Y arbitrariamente grande, su cui G_ψ(x) ≤ x^{1/2+η}. La stima è solo dall'alto e vale solo su certi intervalli. Basta comunque a escludere gli zeri fuori dalla retta, grazie ad argomenti che risalgono a Landau, Guinand, Turán e Weil. Il lavoro nuovo sta tutto nel dimostrare questa disuguaglianza.

**L'idea centrale: divisibilità contro grandezza.** Il motore è la formula del prodotto: se un intero algebrico non nullo è molto divisibile ai primi finiti, i suoi valori assoluti archimedei non possono essere tutti piccoli. Per fare un'analogia nel caso più semplice: un intero non nullo divisibile per p^k ha valore assoluto almeno p^k.

Alpöge costruisce numeri algebrici, i "periodi automorfi", cioè integrali di forme automorfe normalizzati in modo da cadere in un campo di numeri. Mostra poi due cose:
- le valutazioni p-adiche di questi periodi sono limitate dal basso da espressioni che contengono proprio le somme sui primi;
- le loro grandezze archimedee sono limitate dall'alto.

Confrontando le due stime si ottiene un controllo su G_ψ. La difficoltà è mantenere un errore vicino a √x.

L'ispirazione dichiarata è il metodo di Stepanov, che dimostra l'analogo dell'ipotesi di Riemann sui campi di funzioni usando polinomi con zeri di alta molteplicità. Sugli interi la molteplicità è difficile da imitare: sarebbe come «derivare i numeri interi». La soluzione trovata è sostituire la molteplicità con lifting theta ripetuti. Ogni lifting fa guadagnare divisibilità, come se aggiungesse un grado di molteplicità.

**La macchina.** Si lavora con gruppi unitari definiti su un campo totalmente reale, legato a un campo CM abeliano che contiene il campo di ψ. Il periodo iniziale è un periodo di Bessel del tipo studiato da Gan, Gross e Prasad. Lo si trasporta con m lifting successivi della corrispondenza theta di Weil e Howe. Le identità "seesaw" di Kudla collegano il periodo iniziale a quelli finali.

Molte costanti vanno controllate con precisione, perché il termine principale è già stato sottratto e deve riapparire esattamente:
- le norme dei lifting, tramite valori speciali di funzioni L (formule di Rallis e di Gan–Qiu–Takeda);
- le dimensioni degli spazi di forme, tramite la formula di Weyl e conteggi alla Siegel;
- i periodi delle varietà abeliane CM, legati da Chowla–Selberg alle derivate logaritmiche delle funzioni L di Dirichlet.

Per confrontare il lato p-adico con quello archimedeo si usano reticoli di forme automorfe e se ne stimano i covolumi. Qui entrano la geometria di Arakelov sugli spazi di moduli di varietà abeliane (teoremi di Hilbert–Samuel aritmetici, Zhang, Moriwaki), la teoria di Hodge p-adica integrale (Fargues, teoria di Dieudonné prismatica), le filtrazioni di Harder–Narasimhan e la disuguaglianza delle pendenze di Bost. Un'altra difficoltà nasce dalla proiezione sugli autospazi di Hecke, che può introdurre denominatori e quindi far perdere divisibilità. Per controllarli servono le rappresentazioni di Galois associate alle forme automorfe, la coomologia di Galois (dualità di Tate–Poitou, metodi di Taylor–Wiles, il sistema di Eulero di Kato) e la teoria di Iwasawa, inclusa l'annullamento dell'invariante μ di Ferrero–Washington. Alpöge descrive questa parte come una forma molto indebolita della congettura di Vandiver. Compare perfino la costruzione di Behrend di grandi insiemi di interi senza progressioni aritmetiche di tre termini, usata per scegliere certi posti complessi; Alpöge la ritiene quasi certamente eliminabile.

**Perché proprio 1/2.** L'esponente esce da un bilanciamento. Messi insieme tutti i contributi, i due errori principali nella stima di G_ψ(x) hanno ordine x/m e m, a meno di fattori piccoli. Con m dell'ordine di √x entrambi diventano circa √x, cioè esattamente la precisione richiesta dall'ipotesi di Riemann. Alpöge racconta che fu proprio Claude a suggerire che la catena di lifting dovesse avere lunghezza √X, e aggiunge: «e cos'altro potrebbe essere?».

In sintesi, la dimostrazione è una strategia alla Stepanov trapiantata nel mondo automorfo: divisibilità crescente grazie ai lifting theta, contro limiti archimedei, con il numero di lifting scelto per far coincidere i due errori. Al momento la sua correttezza si appoggia sulla formalizzazione in Lean, mentre una versione scritta per lettori umani è ancora da fare.

### claude_overview-L3-s02

*panoramica, spiegazione 3 di 8.* Fatti del livello: 13 sì, 7 in parte, 5 no (copertura 0,66) · errori 1 su 55 · analogie dichiarate 1 · segnalazioni del critico 0, errori introdotti 0 · 1070 parole (limite 1000) · Gulpease 55,5

L'enunciato è l'ipotesi di Riemann generalizzata per le funzioni L di Dirichlet. Un carattere di Dirichlet χ è una funzione periodica e moltiplicativa sugli interi. Dirichlet la introdusse per distinguere le progressioni aritmetiche e dimostrare che ciascuna, se primo termine e ragione sono coprimi, contiene infiniti primi. La funzione L(s,χ) = Σ χ(n) n^(−s) si estende meromorficamente a tutto il piano complesso. La congettura afferma che, per ogni χ primitivo, tutti gli zeri nella striscia 0 < Re(s) < 1 stanno sulla retta Re(s) = 1/2. Il caso χ = 1 è l'ipotesi di Riemann classica per ζ(s).

Prima di tutto lo stato delle cose. Alpöge dichiara di aver trovato la dimostrazione lavorando con Claude e di averla formalizzata in Lean «senza assunzioni». Ha però deciso di pubblicare soltanto il codice Lean: la versione completa leggibile prodotta con Claude supera le 250.000 pagine, e una stesura umana ancora non c'è. Scrive di non padroneggiare ancora tutte le parti e di aspettarsi semplificazioni rapide. La nota di Robin Zhang, da cui viene quasi tutta la ricostruzione che segue, si presenta come «preliminare» e parla di dimostrazione «proposta».

**Dagli zeri alle somme sui primi.** Il punto di partenza è classico. La derivata logaritmica −L′/L(s,χ) è uguale a Σ Λ(n)χ(n)n^(−s), dove Λ, la funzione di von Mangoldt, vale log p sulle potenze del primo p e 0 altrove. Gli zeri di L diventano poli della derivata logaritmica. Alpöge usa una media pesata, S_χ(x) = Σ_{n≤x} Λ(n)χ(n)(x/n − 1). Il peso x/n − 1 è scelto perché la trasformata di Mellin di S_χ sia semplice: vale −L′/(s(s−1)L). Così le stime sulla crescita di S_χ(x) diventano informazioni sui poli, cioè sugli zeri.

Poi si sottrae un termine principale per eliminare il polo spurio in s = 1, ottenendo funzioni corrette G_χ. Fissato un carattere ψ di ordine r, si combinano le G_χ dei caratteri che inducono tutte le potenze di ψ, con coefficienti positivi. La positività conta: in uno zero comune a più funzioni L, i contributi si sommano e non possono cancellarsi.

Il cuore della dimostrazione è la Proposizione 1.2. Per ogni η > 0 esistono intervalli [Y, Y^(3/2)], con Y arbitrariamente grande, su cui G_ψ(x) ≤ x^(1/2+η). È soltanto una stima dall'alto e vale solo su questi intervalli. La nota spiega che basta comunque a escludere zeri fuori dalla retta critica, con argomenti che risalgono a Landau, Guinand, Turán e Weil.

**Come si stima G_ψ: divisibilità contro grandezza.** L'idea motrice viene dalla formula del prodotto. Un intero algebrico non nullo molto divisibile ai primi finiti non può avere tutti i valori assoluti archimedei piccoli. Il caso più semplice, che vale come analogia, è un intero non nullo divisibile per 2^10: in valore assoluto è almeno 1024.

Alpöge costruisce numeri algebrici, i periodi automorfi, cioè integrali di forme automorfe normalizzati in modo da prendere valori in un campo di numeri. La loro divisibilità ai primi finiti si stima dal basso con somme sulle potenze dei primi. Se si stima dall'alto la loro grandezza archimedea, si ottiene un vincolo su quelle somme. La difficoltà è ottenere un errore vicino a √x.

I periodi vivono su gruppi unitari definiti su un campo CM abeliano E che contiene il campo associato a ψ. Il periodo di partenza è un periodo di Bessel nel senso di Gan–Gross–Prasad. Per aumentarne la divisibilità, Alpöge applica ripetutamente la corrispondenza theta di Weil e Howe, che trasporta forme automorfe da un gruppo unitario a un altro: si fanno m sollevamenti consecutivi. Le identità «seesaw» di Kudla collegano il periodo iniziale a quello finale.

Qui c'è il legame con la storia del problema. Sui campi di funzioni l'ipotesi di Riemann fu dimostrata, tra l'altro, con il metodo di Stepanov, che usa un oggetto ausiliario con zeri di molteplicità elevata. Sugli interi la molteplicità è difficile da imitare, perché sarebbe come «derivare i numeri interi». Secondo Alpöge, ogni sollevamento theta fa le veci di un ordine di molteplicità.

Per tenere sotto controllo le costanti servono molti strumenti classici. Le norme dei sollevamenti si calcolano con le formule di Rallis e di Gan–Qiu–Takeda, le dimensioni con la formula di Weyl e con conteggi di reticoli alla Siegel. I periodi delle varietà abeliane CM, legati alle derivate logaritmiche delle L di Dirichlet tramite Chowla–Selberg, servono a ricostruire esattamente il termine principale sottratto.

**Reticoli e geometria aritmetica.** Per confrontare divisibilità e grandezza, Alpöge lavora con reticoli di forme automorfe a coefficienti interi. I periodi definiscono mappe tra questi reticoli. Serve poi stimare il covolume di un reticolo duale, o equivalentemente la sua «pendenza media».

Gli strumenti vengono dalla teoria di Arakelov: la filtrazione di Harder–Narasimhan per reticoli hermitiani, la disuguaglianza di Bost, le formule di Hilbert–Samuel aritmetiche (Gillet–Soulé, Zhang) e i risultati di Moriwaki. Il tutto è applicato su spazi di moduli di varietà abeliane. Per i contributi dei primi finiti entra la teoria di Hodge p-adica integrale, con Fargues e Anschütz–Le Bras.

**Denominatori e coomologia di Galois.** Proiettare sugli autospazi di Hecke può introdurre denominatori, che mangiano parte della divisibilità guadagnata. Per controllarli si studiano le congruenze tra autovalori di Hecke attraverso le rappresentazioni di Galois associate alle forme automorfe.

Ne nascono gruppi di coomologia di Galois S_ℓ(E,j), che vanno stimati. Per farlo si usano la dualità di Tate–Poitou, argomenti di deformazione alla Wiles e Taylor–Wiles, il sistema di Eulero di Kato e la teoria di Iwasawa lungo torri ciclotomiche, con il teorema di Ferrero–Washington. Alpöge descrive questo passaggio come la conquista di un forte indebolimento della congettura di Vandiver.

C'è anche un ingrediente combinatorio. Per scegliere i posti complessi di E si adatta la costruzione di Behrend di insiemi grandi senza progressioni aritmetiche di tre termini. Alpöge stesso ritiene che questo passaggio sia probabilmente evitabile.

**Perché proprio 1/2.** Messe insieme tutte le stime, restano due errori principali, di ordine x/m e m, a meno di fattori piccoli. Scegliendo m ≈ √x entrambi valgono circa √x, ed è da qui che viene l'esponente 1/2 della retta critica. Alpöge racconta che fu Claude a proporre una catena di sollevamenti di lunghezza √X: «e del resto, che altro potrebbe essere?».

Per un laureato non specialista il messaggio è questo: il problema analitico viene trasformato in una gara tra divisibilità e grandezza di numeri algebrici di origine automorfa. La dimostrazione impiega una parte enorme della teoria dei numeri contemporanea. Per ora esistono il codice Lean e resoconti preliminari, non ancora un testo che i matematici possano leggere per intero.

### claude_overview-L3-s03

*panoramica, spiegazione 4 di 8.* Fatti del livello: 13 sì, 6 in parte, 6 no (copertura 0,64) · errori 1 su 40 · analogie dichiarate 2 · segnalazioni del critico 0, errori introdotti 0 · 890 parole (limite 1000) · Gulpease 55,7

Il risultato annunciato il 20 novembre 2026 da Levent Alpöge riguarda le funzioni L di Dirichlet. Un carattere di Dirichlet χ è una funzione periodica e moltiplicativa sugli interi, a valori complessi. La serie L(s,χ) = Σ χ(n)n^{-s} converge per Re s > 1 e si prolunga in modo meromorfo a tutto il piano. L'enunciato è questo: per ogni carattere primitivo χ, ogni zero di L(s,χ) nella striscia 0 < Re s < 1 sta sulla retta Re s = 1/2. Per il carattere banale si ritrova la funzione zeta, e quindi l'ipotesi di Riemann classica. Il lavoro, svolto insieme a Claude, è formalizzato in Lean «senza assunzioni». Per ora Alpöge ha diffuso solo il codice Lean, non un testo leggibile. Ciò che segue viene dalla sua nota e da una nota preliminare di Robin Zhang, che parla di dimostrazione «proposta».

Il primo passo è classico. Per Re s > 1, −L'/L(s,χ) = Σ Λ(n)χ(n)n^{-s}, dove la funzione di von Mangoldt Λ(n) vale log p se n è una potenza del primo p, e 0 altrimenti. Gli zeri di L diventano poli di questa funzione. Alpöge usa la somma pesata S_χ(x) = Σ_{n≤x} Λ(n)χ(n)(x/n − 1). La sua trasformata di Mellin è −L'(s,χ)/(s(s−1)L(s,χ)), quindi controllare la crescita di S_χ(x) dice dove possono stare i poli, cioè gli zeri. Si sottrae un termine principale per togliere il polo in s = 1. Poi si sommano con pesi positivi le versioni corrette relative a tutte le potenze di un carattere ψ, ottenendo una funzione G_ψ. I pesi positivi impediscono che zeri di funzioni L diverse si compensino. Il cuore è una proposizione: per ogni η > 0 esistono intervalli [Y, Y^{3/2}] arbitrariamente lontani su cui G_ψ(x) ≤ x^{1/2+η}. È solo una maggiorazione, e solo su certi intervalli. Argomenti classici, legati a Landau, Guinand, Turán e Weil, mostrano che basta a escludere zeri fuori dalla retta critica. Tutta la difficoltà sta nel dimostrare quella stima.

L'idea guida viene dai campi di funzioni. Lì l'analogo dell'ipotesi di Riemann ha una dimostrazione dovuta a Stepanov, che costruisce un oggetto ausiliario con zeri di molteplicità alta. Sugli interi la molteplicità è difficile da trovare: secondo Alpöge corrisponderebbe a qualcosa come «derivare i numeri interi». Al suo posto entra un principio aritmetico, conseguenza della formula del prodotto: un intero algebrico non nullo molto divisibile ai primi finiti non può avere tutti i valori assoluti archimedei piccoli. Come analogia elementare, un intero non nullo divisibile per 2¹⁰ ha valore assoluto almeno 1024. La divisibilità fa le veci della molteplicità.

Gli interi algebrici in gioco sono periodi automorfi: integrali di forme automorfe su gruppi unitari, costruiti a partire da un campo CM E che contiene il campo associato a ψ, e normalizzati in modo da prendere valori in un campo di numeri K. Si parte da un periodo di Bessel nel senso di Gan–Gross–Prasad. Poi si applica ripetutamente la corrispondenza theta di Weil e Howe, che trasporta forme automorfe da un gruppo unitario a un altro. Le identità «seesaw» di Kudla collegano il periodo iniziale a quelli ottenuti dopo m sollevamenti, e ogni sollevamento contribuisce alla divisibilità. Le stime dal basso delle valutazioni p-adiche contengono somme su potenze di primi soggette a condizioni di Frobenius. Per ortogonalità dei caratteri, queste somme si traducono nelle funzioni G_χ.

Dall'altro lato servono maggiorazioni archimedee. Le norme dei sollevamenti si esprimono con le formule di Rallis e di Gan–Qiu–Takeda, tramite valori speciali di funzioni L. Le dimensioni si contano con la formula di Weyl e con conteggi di reticoli hermitiani alla Siegel. La normalizzazione usa periodi di varietà abeliane CM, che per il teorema di Chowla–Selberg sono legati alle derivate logaritmiche delle funzioni L di Dirichlet: così riappare esattamente il termine principale sottratto all'inizio.

Per confrontare le due parti si lavora con reticoli di forme automorfe e con le loro «pendenze», usando la filtrazione di Harder–Narasimhan e la disuguaglianza di Bost: una sorta di geometria dei numeri in dimensione crescente. I covolumi si controllano con la geometria di Arakelov su spazi di moduli di varietà abeliane (Gillet–Soulé, Zhang, Moriwaki) e con la teoria di Hodge p-adica intera (Fargues, Anschütz–Le Bras).

C'è poi un'insidia: proiettare sugli autospazi di Hecke può introdurre denominatori che consumano la divisibilità guadagnata. Questi denominatori si controllano tramite congruenze fra autovalori di Hecke. Entrano così le rappresentazioni di Galois, la coomologia di Galois, i metodi di deformazione alla Taylor–Wiles, il sistema di Eulero di Kato e la teoria di Iwasawa. Serve perfino la combinatoria: una variante della costruzione di Behrend di insiemi senza progressioni aritmetiche di tre termini, usata per scegliere i posti complessi di E.

E l'esponente 1/2? Alla fine i due errori principali hanno taglie circa x/m e m, dove m è il numero di sollevamenti theta. Con m dell'ordine di √x i due errori si bilanciano, ed entrambi valgono circa √x. Alpöge racconta che fu Claude a suggerire una catena di sollevamenti di lunghezza √X, ciascuno a imitare un grado di molteplicità.

Restano due avvertenze. Alpöge scrive che l'argomento è per ora lunghissimo, contiene probabilmente scelte subottimali e parti che lui stesso non padroneggia ancora. Si aspetta forti semplificazioni, e la sua cronologia è in parte una parafrasi di un riassunto di Claude. Le fonti, inoltre, non dicono che la comunità abbia già esaminato la formalizzazione: per ora la garanzia di correttezza poggia sul controllo di Lean.

### claude_overview-L3-s04

*panoramica, spiegazione 5 di 8.* Fatti del livello: 14 sì, 6 in parte, 5 no (copertura 0,68) · errori 1 su 49 · analogie dichiarate 1 · segnalazioni del critico 2, errori introdotti 2 · 1033 parole (limite 1000) · Gulpease 57,9

Il risultato annunciato da Levent Alpöge il 20 novembre 2026 riguarda le funzioni L di Dirichlet. Un carattere di Dirichlet χ è una funzione periodica e moltiplicativa dagli interi ai complessi. Dirichlet la introdusse per distinguere tra loro le progressioni aritmetiche e mostrare che ciascuna contiene infiniti primi. A χ si associa la serie L(s,χ) = Σ χ(n) n^(−s), che si estende meromorficamente a tutto il piano complesso. L'enunciato è che, per ogni carattere primitivo χ, tutti gli zeri di L(s,χ) nella striscia 0 < Re(s) < 1 stanno sulla retta Re(s) = 1/2. Nel caso χ = 1 si ottiene la funzione zeta, e quindi l'ipotesi di Riemann classica. Alpöge scrive che il metodo dovrebbe estendersi anche all'ipotesi di Riemann "estesa", ma per ora lo dichiara solo come aspettativa.

Lo stato della dimostrazione va detto con precisione. Alpöge dichiara di averla trovata lavorando con Claude e di averla formalizzata in Lean "senza assunzioni". Ha pubblicato soltanto il codice Lean: un testo leggibile non esiste ancora, perché l'argomento è lunghissimo e la versione completa prodotta automaticamente superava le 250.000 pagine. La fonte di Robin Zhang è una "nota preliminare" su quella che chiama una dimostrazione *proposta*. Lo stesso Alpöge avverte che alcune sue descrizioni sono parafrasi di riassunti di parti che non padroneggia ancora.

Il primo passo è classico: tradurre il problema dagli zeri ai numeri primi. La derivata logaritmica −L′/L si scrive come serie Σ Λ(n)χ(n)n^(−s). Qui Λ è la funzione di von Mangoldt, che vale log p sulle potenze di un primo p e zero altrove. Gli zeri di L diventano poli di −L′/L. Alpöge usa una media pesata, S_χ(x) = Σ_{n≤x} Λ(n)χ(n)(x/n − 1). Questa scelta ha un vantaggio: la trasformata di Mellin di S_χ è esattamente −L′/(s(s−1)L). Se si controlla la crescita di S_χ(x), si esclude che quella trasformata abbia poli lontano dalla retta critica, e quindi che L abbia zeri fuori da essa.

Restano due accorgimenti. Il primo: si sottrae un termine principale per eliminare il polo in s = 1, che non viene da alcuno zero. Per la zeta il termine corretto è −x log x + (1+γ)x. Il secondo: per un carattere ψ di ordine r si combinano con coefficienti positivi le somme corrette relative a tutte le potenze di ψ, ottenendo una funzione G_ψ. I coefficienti sono positivi, quindi gli zeri di funzioni L diverse non possono cancellarsi a vicenda. Il cuore analitico è la Proposizione 1.2: per ogni η > 0 esistono Y arbitrariamente grandi tali che G_ψ(x) ≤ x^(1/2+η) su tutto l'intervallo [Y, Y^(3/2)]. È solo una maggiorazione, e vale solo su intervalli. Che basti a escludere gli zeri fuori dalla retta è il contenuto della Sezione 2 della nota, che si appoggia a Landau, Guinand, Turán e Weil. Le fonti non dettagliano questo passaggio.

Tutta la novità sta nel dimostrare quella maggiorazione. L'idea di fondo è la formula del prodotto. Se un intero algebrico non nullo è divisibile per una potenza elevata dei primi finiti, i suoi valori assoluti archimedei non possono essere tutti piccoli. Un'analogia elementare: un intero non nullo divisibile per 2^100 ha valore assoluto almeno 2^100. Alpöge costruisce numeri di questo tipo, i "periodi automorfi". Sono integrali di forme automorfe su gruppi unitari, normalizzati in modo da cadere in un campo di numeri. Due stime vengono poi confrontate. Dal lato aritmetico, la divisibilità di questi periodi per i vari primi è controllata dal basso proprio da somme di Λ su potenze di primi. Dal lato analitico, le loro dimensioni archimedee sono controllate dall'alto. Il confronto fornisce la maggiorazione di G_ψ. La difficoltà è ottenerla con un errore vicino a √x.

Qui entra l'ispirazione di Alpöge. Sui campi di funzioni (l'analogo "geometrico" degli interi) l'ipotesi di Riemann fu dimostrata anche con il metodo di Stepanov. Quel metodo usa un oggetto ausiliario che si annulla con *alta molteplicità*. Sugli interi la molteplicità è difficile da trovare: sarebbe, dice Alpöge, come derivare i numeri interi. Il surrogato proposto sono i *sollevamenti theta*. Integrando contro un nucleo theta si trasporta una forma automorfa da un gruppo unitario a un altro. Alpöge costruisce catene di m sollevamenti, e ogni anello imita un ordine di molteplicità, cioè aggiunge divisibilità ai periodi. Le identità "seesaw" di Kudla permettono di collegare il periodo iniziale, di tipo Gan–Gross–Prasad, a quello finale. Facendo i conti, i due errori principali hanno grandezza x/m e m. Si bilanciano scegliendo m dell'ordine di √x, e l'errore risultante è proprio √x: da qui viene l'esponente 1/2. Alpöge racconta che fu Claude a proporre una catena di lunghezza √X.

Il resto dell'argomento serve a tenere esatte le costanti, ed è qui che la dimostrazione diventa enorme. Le costanti contano perché il termine principale è già stato sottratto. Le norme dei sollevamenti si esprimono tramite valori speciali di funzioni L (Rallis; Gan–Qiu–Takeda). Le dimensioni degli spazi si calcolano con la formula di Weyl e con conteggi alla Siegel di reticoli hermitiani. La normalizzazione usa periodi di varietà abeliane a moltiplicazione complessa, legati da Chowla–Selberg proprio a L′/L(1,χ). Così il termine principale ricompare e si cancella esattamente.

Per confrontare divisibilità e norme si lavora con reticoli di forme automorfe, cioè in geometria di Arakelov. Si stimano covolumi e "pendenze" usando le filtrazioni di Harder–Narasimhan e la disuguaglianza di Bost. Si usano altezze su compattificazioni di spazi di moduli di varietà abeliane e strumenti di teoria di Hodge p-adica integrale (Fargues, teoria di Dieudonné prismatica). C'è poi un'insidia: proiettare sugli autospazi di Hecke può introdurre denominatori che mangiano la divisibilità guadagnata. Per controllarli servono rappresentazioni di Galois, coomologia di Galois, gli argomenti di deformazione alla Wiles e Taylor–Wiles, il sistema di Eulero di Kato e la teoria di Iwasawa lungo torri ciclotomiche. Infine, i posti complessi su cui lavorare vengono scelti adattando la costruzione di Behrend di insiemi senza progressioni aritmetiche di tre termini. Alpöge giudica questo trucco quasi certamente superfluo.

Riassumendo, lo scheletro è classico: dagli zeri a una stima di somme sui primi. L'idea nuova è ottenere quella stima imitando la molteplicità di Stepanov con catene di sollevamenti theta lunghe circa √x, e confrontando divisibilità aritmetica e grandezza analitica di periodi automorfi. Lo stesso Alpöge prevede che l'argomento verrà semplificato in modo drastico, e presto.

### claude_overview-L3-s05

*panoramica, spiegazione 6 di 8.* Fatti del livello: 13 sì, 8 in parte, 4 no (copertura 0,68) · errori 0 su 45 · analogie dichiarate 1 · segnalazioni del critico 1, errori introdotti 0 · 1027 parole (limite 1000) · Gulpease 57,0

Alpöge, insieme a Claude, afferma di aver dimostrato l'ipotesi di Riemann generalizzata per le funzioni L di Dirichlet. Un carattere di Dirichlet χ è una funzione periodica e moltiplicativa dagli interi ai complessi. Dirichlet li introdusse per contare i primi nelle progressioni aritmetiche. A ogni χ si associa L(s,χ) = Σ χ(n) n^(−s), che converge per Re s > 1 e si prolunga meromorficamente a tutto il piano. Per il carattere banale si ritrova la zeta di Riemann. L'enunciato, già presente in Piltz nel 1884, dice che per ogni χ primitivo tutti gli zeri di L(s,χ) nella striscia 0 < Re s < 1 stanno sulla retta Re s = 1/2. L'ipotesi "estesa", più generale, Alpöge la indica come un obiettivo futuro.

Il primo passo traduce gli zeri in un problema sui primi. Vale l'identità classica −L′/L(s,χ) = Σ Λ(n)χ(n) n^(−s). Qui Λ è la funzione di von Mangoldt: vale log p sulle potenze di un primo p e 0 altrove. Gli zeri di L diventano poli del membro sinistro. Alpöge usa la somma pesata S_χ(x) = Σ_{n≤x} Λ(n)χ(n)(x/n − 1), la cui trasformata di Mellin è semplicemente −L′/(s(s−1)L). L'integrale di Mellin converte informazioni sulla crescita di S_χ in informazioni sulla posizione dei poli. Se S_χ cresce poco, non possono esserci zeri troppo a destra.

Prima di applicare questo principio servono due accorgimenti. Si sottrae a S_χ un termine principale, così da eliminare il polo spurio in s = 1; si ottiene una funzione G_χ. Poi, fissato un carattere ψ di ordine r, si sommano con pesi positivi le G_χ di tutte le sue potenze, ottenendo G_ψ. In uno zero ρ il residuo di G_ψ è una combinazione a coefficienti positivi delle molteplicità di ρ nelle varie L, quindi non può annullarsi per cancellazione.

L'intero problema si riduce allora alla Proposizione 1.2 della nota di Zhang. Per ogni η > 0 e ogni A ≥ 2 esiste Y ≥ A tale che G_ψ(x) ≤ x^(1/2+η) per ogni x in [Y, Y^(3/2)]. La stima è solo dall'alto e vale solo su intervalli arbitrariamente lontani. La nota di Zhang spiega, con strumenti risalenti a Landau, Guinand, Turán e Weil, perché questo basta a escludere zeri fuori dalla retta critica.

Il cuore della dimostrazione è un principio che segue dalla formula del prodotto. Se un intero algebrico non nullo è molto divisibile ai primi finiti, i suoi valori assoluti archimedei non possono essere tutti piccoli. Un'analogia nel caso più elementare: un intero non nullo divisibile per 2^20 ha valore assoluto almeno 2^20. Alpöge costruisce numeri di questo tipo, i "periodi automorfi": integrali di forme automorfe, normalizzati in modo da cadere in un campo di numeri K. Le loro valutazioni p-adiche sono limitate dal basso da espressioni che contengono proprio somme sulle potenze dei primi come G_ψ. Una stima dall'alto della loro grandezza archimedea dà quindi una stima dall'alto di G_ψ. La difficoltà è ottenere una precisione vicina a √x.

Da dove viene la divisibilità? Alpöge presenta l'argomento come un discendente di quello di Stepanov per l'ipotesi di Riemann sui campi di funzioni. In quell'argomento si usa un divisore con molteplicità, cioè qualcosa che si annulla a un ordine elevato. Sugli interi la molteplicità è difficile da trovare: lui la paragona a "derivare i numeri interi". La sua proposta è che ogni sollevamento theta (theta lift) imiti un ordine di molteplicità.

La corrispondenza theta di Weil e Howe trasporta una forma automorfa da un gruppo unitario a un altro, integrandola contro un nucleo theta. I gruppi sono definiti sul sottocampo totalmente reale di un campo CM E che contiene il campo associato a ψ. Si parte da un periodo di Bessel, del tipo studiato da Gan, Gross e Prasad, e si applicano m sollevamenti successivi. Le identità "seesaw" di Kudla collegano il periodo iniziale all'accoppiamento finale, e ogni sollevamento aggiunge divisibilità.

Qui si vede perché compare l'esponente 1/2. I due errori principali nella stima di G_ψ(x) hanno ordine x/m e m. Scegliendo m vicino a √x entrambi diventano vicini a √x. Alpöge racconta che fu Claude a suggerire una catena di lunghezza √X, e commenta: "e che altro potrebbe essere?".

Il prezzo di questa idea è enorme. Ogni sollevamento cambia le norme di Petersson e le dimensioni degli spazi, e queste costanti vanno controllate esattamente, perché il termine principale è già stato sottratto. Gli strumenti usati sono i seguenti.

- **Norme dei sollevamenti:** formule di Rallis e di Gan–Qiu–Takeda, che le esprimono tramite valori speciali di funzioni L.
- **Dimensioni:** formula di Weyl e conteggi di reticoli hermitiani alla Siegel.
- **Termine principale:** periodi di varietà abeliane CM, legati da Chowla–Selberg e Anderson alle derivate logaritmiche delle L di Dirichlet, che lo ricostruiscono esattamente.
- **Confronto tra grandezza e divisibilità:** geometria di Arakelov. Si lavora con reticoli di forme automorfe sugli interi di K, se ne stimano covolumi e pendenze (filtrazione di Harder–Narasimhan, disuguaglianza di Bost) e si dimostra che i funzionali periodo generano quasi tutto lo spazio duale.
- **Covolumi:** altezze su spazi di moduli di varietà abeliane, controllate con la teoria di Hodge p-adica integrale (Fargues, Anschütz–Le Bras).
- **Denominatori:** proiettare sugli autospazi di Hecke può introdurre denominatori che mangiano divisibilità. Si controllano con congruenze tra forme e rappresentazioni di Galois, dualità di Tate–Poitou, teoria delle deformazioni alla Taylor–Wiles, il sistema di Eulero di Kato e la teoria di Iwasawa lungo torri ciclotomiche.
- **Combinatoria:** i posti complessi di E sono scelti adattando la costruzione di Behrend di insiemi senza progressioni aritmetiche di tre termini. Alpöge stesso ritiene che questo trucco sia quasi certamente superfluo.

Infine, lo stato del lavoro, con onestà. Alpöge ha diffuso soltanto il codice Lean e dichiara che la formalizzazione è completa e "senza assunzioni". Un testo leggibile per esseri umani non esiste ancora: un tentativo automatico aveva superato le 250.000 pagine. Alpöge ammette di non padroneggiare tutta la matematica coinvolta, in particolare le forme automorfe sui gruppi di rango alto. Ammette anche che parte della sua cronologia parafrasa riassunti di Claude che "potrebbero non avere senso". Si aspetta semplificazioni rapide. La nota di Zhang si presenta come "preliminare" e parla di dimostrazione "proposta". Quanto sopra è quindi una ricostruzione dell'architettura dell'argomento, non una verifica.

### claude_overview-L3-s06

*panoramica, spiegazione 7 di 8.* Fatti del livello: 16 sì, 4 in parte, 5 no (copertura 0,72) · errori 1 su 45 · analogie dichiarate 1 · segnalazioni del critico 0, errori introdotti 0 · 1007 parole (limite 1000) · Gulpease 56,7

Il teorema annunciato da Levent Alpöge riguarda le funzioni L di Dirichlet. Un carattere di Dirichlet χ è una funzione periodica e moltiplicativa sugli interi. Dirichlet la introdusse per separare i primi nelle diverse progressioni aritmetiche. A χ si associa la serie L(s,χ) = Σ χ(n)/nˢ, che si prolunga meromorficamente a tutto il piano complesso. L'enunciato dimostrato è l'ipotesi di Riemann generalizzata in questa forma: per ogni carattere primitivo χ, ogni zero di L(s,χ) nella striscia 0 < Re(s) < 1 sta sulla retta Re(s) = 1/2. Il caso χ = 1 è la funzione zeta, quindi l'ipotesi di Riemann classica è compresa. Alpöge scrive di aspettarsi che, con più tempo, il metodo raggiunga anche l'ipotesi di Riemann "estesa".

Sullo stato del risultato le fonti dicono questo. Alpöge afferma di aver formalizzato l'intera dimostrazione in Lean insieme a Claude, "senza assunzioni", e di aver reso pubblico solo il codice Lean. Un testo leggibile ancora non esiste: la versione estesa generata supera le 250.000 pagine, e lui stesso la considera illeggibile. Ammette anche di non padroneggiare ancora diverse parti dell'argomento, in particolare quelle sulle forme automorfe di rango alto, dove a suo dire Claude "lo ha lasciato indietro". La nota di Robin Zhang, su cui si basa quasi tutto ciò che segue, si definisce "preliminare" e parla di una dimostrazione "proposta". Le fonti non riportano verifiche indipendenti della formalizzazione.

Il primo passo è classico. La derivata logaritmica −L′/L(s,χ) è uguale a Σ Λ(n)χ(n)n⁻ˢ, dove Λ è la funzione di von Mangoldt: vale log p sulle potenze del primo p e zero altrove. Ogni zero di L diventa così un polo di una serie sui primi. Alpöge usa una media pesata, la media di Riesz S_χ(x) = Σ_{n≤x} Λ(n)χ(n)(x/n − 1). La sua trasformata di Mellin è esattamente −L′/(s(s−1)L). Se S_χ(x) cresce lentamente, la trasformata converge più a sinistra, e lì non possono esserci poli, cioè zeri. Si sottrae poi un termine principale per eliminare il polo spurio in s = 1, ottenendo funzioni corrette G_χ. Infine si sommano con coefficienti positivi le G_χ di tutte le potenze di un carattere ψ, ottenendo una funzione G_ψ. La positività dei pesi garantisce che zeri di funzioni L diverse non si cancellino a vicenda.

Il cuore analitico è la Proposizione 1.2: per ogni η > 0 esistono Y arbitrariamente grandi tali che G_ψ(x) ≤ x^{1/2+η} per tutti gli x in [Y, Y^{3/2}]. La stima è solo dall'alto e vale solo su intervalli sparsi. Un argomento nello spirito di Landau, Guinand, Turán e Weil mostra però che basta a escludere zeri a destra della retta critica. Per simmetria, li esclude anche a sinistra.

La parte nuova è il modo di ottenere questa stima, e qui entra l'aritmetica. Il principio di fondo è la formula del prodotto: un intero algebrico non nullo molto divisibile per i primi finiti non può essere piccolo in tutti i suoi valori assoluti archimedei. Un'analogia elementare: un intero ordinario non nullo divisibile per 2¹⁰ ha modulo almeno 1024. Alpöge costruisce numeri di questo tipo, i "periodi automorfi". Sono integrali di forme automorfe su gruppi unitari, normalizzati in modo da prendere valori in un campo di numeri. Le loro valutazioni p-adiche sono stimate dal basso da somme sulle potenze dei primi, cioè da quantità come G_ψ. La loro grandezza archimedea si stima invece dall'alto. Il confronto tra le due stime controlla G_ψ.

L'idea guida, racconta Alpöge, viene dal metodo di Stepanov, che dimostra l'ipotesi di Riemann sui campi di funzioni usando polinomi che si annullano con molteplicità alta, cioè sfruttando le derivate. Sugli interi manca un analogo naturale della molteplicità: sarebbe come "derivare i numeri interi". Il sostituto trovato è la corrispondenza theta di Weil e Howe. Integrare contro un nucleo theta trasporta una forma automorfa da un gruppo unitario a un altro, e ogni sollevamento aumenta la divisibilità del periodo, come se aggiungesse un'unità di molteplicità. Si costruisce allora una catena di m sollevamenti theta U(X₀) → U(X₁) → … → U(X_m). Le identità "seesaw" di Kudla collegano il periodo iniziale, di tipo Gan–Gross–Prasad, a quello finale. Le due fonti principali di errore hanno ordine x/m e m. Scegliendo m vicino a √x entrambe diventano circa √x, ed è da qui che viene l'esponente 1/2. Alpöge cita come momento chiave la proposta di Claude di usare una catena di lunghezza √X.

Far funzionare lo schema richiede un'enorme quantità di matematica, e le fonti la elencano. Le norme dei sollevamenti si calcolano con le formule di Rallis e di Gan–Qiu–Takeda. Le dimensioni degli spazi di forme si ottengono dalla formula di Weyl e da conteggi di reticoli alla Siegel. Il termine principale si ritrova grazie ai periodi di varietà abeliane a moltiplicazione complessa, legati a L′/L da Chowla–Selberg. Le forme automorfe vengono organizzate in reticoli. Per stimarne i covolumi intervengono la geometria di Arakelov sugli spazi di moduli (Gillet–Soulé, Zhang, Moriwaki), la teoria di Hodge p-adica integrale (Fargues, Anschütz–Le Bras), la filtrazione di Harder–Narasimhan e la disuguaglianza delle pendenze di Bost. Serve anche mostrare che i funzionali periodo generano quasi tutto lo spazio duale. Proiettare sugli autospazi di Hecke può introdurre denominatori che mangiano la divisibilità guadagnata. Per controllarli si usano le rappresentazioni di Galois associate alle forme automorfe, la coomologia di Galois, gli argomenti di deformazione alla Wiles e Taylor–Wiles, il sistema di Eulero di Kato e la teoria di Iwasawa con il teorema di Ferrero–Washington. Infine, per scegliere i posti complessi del campo ausiliario si adatta la costruzione di Behrend di insiemi grandi senza progressioni aritmetiche di tre termini.

Lo stesso Alpöge ritiene che molte di queste scelte siano subottimali. Considera Behrend "ovviamente non necessario" e si aspetta semplificazioni drastiche, probabilmente a breve. In sintesi, la dimostrazione riduce l'ipotesi di Riemann generalizzata a una stima dall'alto per somme sui primi. Ottiene poi quella stima confrontando la divisibilità e la grandezza di periodi automorfi, e la divisibilità è amplificata da una catena di circa √x sollevamenti theta che imita la molteplicità del metodo di Stepanov. Che l'argomento regga nella sua interezza è affidato, per ora, al codice Lean.

### claude_overview-L3-s07

*panoramica, spiegazione 8 di 8.* Fatti del livello: 14 sì, 6 in parte, 5 no (copertura 0,68) · errori 4 su 47 · analogie dichiarate 1 · segnalazioni del critico 0, errori introdotti 0 · 950 parole (limite 1000) · Gulpease 56,6

Il 20 novembre 2026 Levent Alpöge ha annunciato di aver trovato, lavorando con Claude, una dimostrazione dell'ipotesi di Riemann generalizzata per le funzioni L di Dirichlet. Dice che anche la formalizzazione in Lean è completa e senza ipotesi aggiuntive. Per ora non esiste un articolo leggibile. Alpöge ha pubblicato solo il codice Lean: un testo umano completo sarebbe enorme e illeggibile, e lui stesso ammette di non padroneggiare ancora gran parte della matematica coinvolta. Ciò che segue si basa sulla sua nota e su una «nota preliminare» di Robin Zhang che riassume l'argomento. Va quindi letto come la descrizione di una dimostrazione proposta.

L'enunciato è questo. Un carattere di Dirichlet χ è una funzione periodica e moltiplicativa sugli interi. La sua funzione L, L(s,χ) = Σ χ(n) n^(−s), si estende meromorficamente al piano complesso. La congettura afferma che, per ogni χ primitivo, tutti gli zeri nella striscia 0 < Re s < 1 stanno sulla retta Re s = 1/2. Per χ banale si ritrova l'ipotesi di Riemann classica sulla funzione zeta.

Il primo passo traduce gli zeri in somme sui primi. La derivata logaritmica −L′/L è uguale a Σ Λ(n)χ(n)n^(−s), dove Λ(n) vale log p se n è una potenza del primo p e zero altrimenti; gli zeri di L diventano poli. Alpöge usa la somma pesata S_χ(x) = Σ_{n≤x} Λ(n)χ(n)(x/n − 1). La sua trasformata di Mellin è semplicemente −L′/(s(s−1)L), quindi informazioni sulla crescita di S_χ si traducono in vincoli sulla posizione dei poli, cioè degli zeri. A S_χ si sottrae un termine principale, ottenendo G_χ, per eliminare un eventuale polo in s = 1 che non viene da zeri. Fissato un carattere ψ, le G_χ relative alle sue potenze si combinano poi con pesi positivi in una funzione G_ψ. La positività garantisce che zeri di funzioni L diverse non si cancellino a vicenda.

Il cuore analitico è un'unica stima, la Proposizione 1.2. Per ogni η > 0 esistono Y arbitrariamente grandi tali che G_ψ(x) ≤ x^(1/2+η) per ogni x in [Y, Y^(3/2)]. La stima è solo dall'alto e vale solo su intervalli, non per ogni x grande. Secondo Zhang, risultati classici di Landau, Guinand, Turán e Weil bastano comunque per escludere zeri fuori dalla retta critica. La sua panoramica non entra nei dettagli di questo passaggio.

Come si ottiene la stima? L'idea guida è la formula del prodotto. Un intero algebrico non nullo molto divisibile per i primi finiti non può avere tutti i valori assoluti archimedei piccoli. Un'analogia: un intero diviso da 2^100 è almeno 2^100 in valore assoluto. Gli interi algebrici in questione sono «periodi automorfi», cioè integrali di forme automorfe su gruppi unitari costruiti a partire da un campo CM che contiene il campo associato a ψ. Questi integrali vengono normalizzati in modo da prendere valori in un campo di numeri K. La loro divisibilità per i primi si esprime con somme su potenze di primi soggette a condizioni di Frobenius. Per ortogonalità dei caratteri, queste somme diventano proprio i termini G_χ. Una stima dall'alto della grandezza archimedea dei periodi diventa così una stima dall'alto di G_ψ, con un errore vicino a √x.

Da dove viene tanta divisibilità? Qui entra l'idea che Alpöge considera decisiva. Nei campi di funzioni, l'ipotesi di Riemann fu dimostrata anche da Stepanov, con un divisore ausiliario che si annulla con alta molteplicità. Sugli interi la molteplicità è difficile da trovare: corrisponderebbe, scrive Alpöge, a «derivare i numeri interi». Il sostituto proposto è una catena di sollevamenti theta. La corrispondenza theta di Weil e Howe porta una forma automorfa da un gruppo unitario a un altro integrandola contro un nucleo theta. Ogni sollevamento imita un ordine di molteplicità e aumenta la divisibilità dei periodi. Dopo m sollevamenti, le identità «seesaw» di Kudla collegano il periodo iniziale, un periodo di Bessel nel senso di Gan–Gross–Prasad, all'accoppiamento finale.

Sul lato archimedeo bisogna tenere conto delle norme e delle dimensioni con grande precisione, perché il termine principale è già stato sottratto. Le formule di Rallis e di Gan–Qiu–Takeda esprimono le norme di Petersson dei sollevamenti tramite valori speciali di funzioni L. La formula di Weyl e conteggi alla Siegel danno le dimensioni. La normalizzazione usa periodi di varietà abeliane CM, che per Chowla–Selberg sono legati a derivate logaritmiche di funzioni L di Dirichlet. In questo modo il termine principale ricompare esattamente e si cancella.

Per confrontare divisibilità e grandezza servono reticoli di forme automorfe sull'anello degli interi di K, e quindi la geometria di Arakelov. I covolumi si stimano con formule di Hilbert–Samuel aritmetiche e con la teoria di Hodge p-adica integrale. La filtrazione di Harder–Narasimhan e la disuguaglianza delle pendenze di Bost mostrano che i funzionali periodo coprono quasi tutto lo spazio duale. Proiettare sugli autospazi di Hecke può introdurre denominatori che mangiano la divisibilità. Per controllarli servono rappresentazioni di Galois associate alle forme automorfe, coomologia di Galois, argomenti di deformazione alla Taylor–Wiles, il sistema di Eulero di Kato e la teoria di Iwasawa. Infine, per scegliere le posizioni complesse rilevanti, si adatta la costruzione di Behrend di grandi insiemi di interi senza progressioni aritmetiche di tre termini. Alpöge pensa che quest'ultimo ingrediente sia quasi certamente evitabile.

Il bilancio finale spiega l'esponente 1/2. Secondo Zhang, i due errori principali nella stima di G_ψ(x) hanno ordine x/m e m, a meno di potenze arbitrariamente piccole di x. Scegliendo m vicino a √x entrambi diventano vicini a √x. Alpöge racconta che la lunghezza √X della catena fu suggerita da Claude, e commenta: «che altro potrebbe essere?».

Restano alcune avvertenze. L'argomento è, parole dell'autore, «incredibilmente lungo» e probabilmente pieno di scelte non ottimali. Alpöge si aspetta semplificazioni drastiche, forse a breve. Le fonti non dicono quale verifica indipendente del codice Lean sia stata fatta finora.

## Livello 4: un teorico dei numeri (al più 1500 parole)

### claude_full-L4-s00

*nota intera, spiegazione 1 di 8.* Fatti del livello: 21 sì, 7 in parte, 2 no (copertura 0,82) · errori 0 su 76 · analogie dichiarate 0 · segnalazioni del critico 2, errori introdotti 0 · 1537 parole (limite 1500) · Gulpease 55,6

Ciò che viene dimostrato è l'ipotesi di Riemann generalizzata per le funzioni L di Dirichlet: per ogni carattere primitivo χ, ogni zero di L(s,χ) nella striscia 0 < Re(s) < 1 ha parte reale 1/2. Il caso χ = 1 è l'ipotesi di Riemann classica. Prima del come, conviene dire in che forma esiste la dimostrazione. Alpöge ha pubblicato soltanto una formalizzazione in Lean, di circa 17 milioni di righe, scritta insieme a Claude. Ha tenuto per sé un'esposizione generata dall'IA di oltre 250.000 pagine. Secondo la nota di Robin Zhang, le comunità Lean e Mathlib hanno verificato la dimostrazione in un giorno con implementazioni indipendenti del kernel, e hanno controllato che le definizioni in Lean coincidano con quelle matematiche standard. La ricostruzione leggibile che riassumo qui è però quella di Zhang, che dalla sezione 2 in poi è in gran parte scritta da un'IA (GPT 6 Pro) a partire dal codice. Zhang stesso dichiara di non poter garantire che sia una traduzione fedele del Lean. Prendete quindi la struttura descritta qui sotto come la mappa migliore disponibile, non come un testo verificato riga per riga.

**Riduzione a una stima unilaterale.** Il punto di partenza è la media di Riesz del primo ordine

S_χ(x) = Σ_{n≤x} Λ(n)χ(n)(x/n − 1).

La sua trasformata di Mellin è −L′(s,χ)/(s(s−1)L(s,χ)). Si corregge il polo in s = 1 in due modi. Per χ ≠ 1 si pone G_χ(x) = S_χ(x) + x L′(1,χ)/L(1,χ). Per χ = 1 si pone G_1(x) = S_1(x) − x log x + (1+γ)x. Fissato ψ primitivo di ordine r, si considera la combinazione

𝒢_ψ = G_1 + (3r+1)^{−1} Σ Re G_χ,

dove χ percorre i caratteri primitivi che inducono le potenze di ψ. Il risultato centrale è la Proposizione 1.2: per ogni η > 0 esistono Y arbitrariamente grandi tali che 𝒢_ψ(x) ≤ x^{1/2+η} su tutto l'intervallo [Y, Y^{3/2}].

Questa stima ha due debolezze: è solo dall'alto e vale solo su certi intervalli. Basta lo stesso, perché i coefficienti della combinazione sono positivi. Il residuo della trasformata in uno zero ρ vale ν_ρ/(ρ(1−ρ)), dove ν_ρ è una somma pesata positiva di molteplicità, quindi zeri comuni a più funzioni L non possono cancellarsi.

Il passaggio dalla stima agli zeri ricorda Landau e Turán. Si passa a coordinate logaritmiche e si deriva la trasformata di Laplace k volte, con k ≍ log Y. Il nucleo u^k e^{−σu}/k! è una densità gamma, che concentra la massa sull'intervallo buono (Lemma 2.2); fuori basta la stima grossolana |g(u)| ≪ e^{2u}. Combinando |A_k(t)| + A_k(0) si usa solo la parte positiva di g. Scegliendo il punto di derivazione in modo che un unico polo sia il più vicino, il suo contributo d^{−k−1} contraddice la maggiorazione. La metà sinistra della striscia si ottiene poi dall'equazione funzionale, e i caratteri imprimitivi dai fattori euleriani.

**Dalla stima ai fattori di Frobenius.** Si lavora in un campo CM abeliano ausiliario E che contiene il campo tagliato da ψ. Per ortogonalità dei caratteri, la quantità

A(a,t,w) = Σ_p log p Σ_j (2/|I_p|) Σ_g (a/p^j − w_{ρ_t(g)})_+,

ristretta a una condizione di Frobenius, è non negativa. La Proposizione 3.1 mostra che A − M si scrive esattamente come una combinazione dei w·G_χ(a/w). Il termine principale M contiene log a − 1 − γ + L′/L(1,κ) e la media dei log w, e usa solo derivate logaritmiche in s = 1, quindi non presuppone nulla sugli zeri.

I pesi w si scelgono su due scale. Nei posti complessi di un insieme T₂ si ha a/w ≈ x. Negli altri posti a/w è enorme, e lì bastano le regioni libere da zeri. Una media su un sottogruppo H₀ del gruppo di Galois conserva proprio i caratteri che servono per 𝒢_ψ. Resta quindi da maggiorare A − M.

**Il cuore: divisibilità di periodi automorfi.** L'idea viene dalla formula del prodotto: un intero algebrico non nullo molto divisibile ai primi finiti non può essere piccolo in tutti i posti archimedei. Gli oggetti sono periodi di Bessel alla Gan–Gross–Prasad P_α(f,g), con f forma cuspidale su U(X₀), X₀ totalmente definito, e g su U(Y₀), per gruppi unitari su E⁺. I periodi sono normalizzati in modo da avere valori in un campo di numeri K. Le minorazioni delle loro valutazioni ai primi di K contengono esattamente gli addendi (a/p^ν − w)_+ di A.

Per avere abbastanza divisibilità si applica il sollevamento theta m volte, su entrambi i lati. Ogni sollevamento U(X_j) → U(X_{j+1}) aggiunge un blocco di parametri di Harish-Chandra centrato in −w_{j+1,τ}. Le identità seesaw di Kudla trasportano il periodo iniziale fino a un periodo di restrizione U(Y_m) ⊂ U(X_m), passando per periodi alternativamente di Bessel e di Fourier–Jacobi. I contributi favorevoli si sommano sugli m sollevamenti e producono un fattore m.

L'analogia, proposta dallo stesso Alpöge, è con il metodo di Stepanov per le curve sui campi finiti, dove si costruisce un polinomio ausiliario che si annulla con alta molteplicità nei punti. Qui il numero m di sollevamenti fa la parte della molteplicità, che sugli interi è difficile da realizzare direttamente. È un'analogia, non un'identità tra i due metodi. Alpöge racconta che fu Claude a proporre una catena di lunghezza √X per una somma di von Mangoldt di lunghezza X.

Il confronto tra la parte finita e quella archimedea è formulato in geometria di Arakelov. Dalla divisibilità, codificata da ideali frazionari a_α, si ottengono mappe intere b_α : N_α → C = Hom(M_W, O_K). L'obiettivo è minorare la pendenza media di C, e servono tre ingredienti:

1. **La disuguaglianza delle pendenze di Bost**, applicata ai pezzi di Harder–Narasimhan dei domini N_α.
2. **Un lemma di algebra lineare (Lemma 4.2).** Se le mappe normalizzate sono quasi isometrie e l'operatore Q = Σ γ_i B_i B_i* è quasi scalare, le immagini coprono quasi tutto W^∨ anche dopo aver ristretto i domini. Zhang lo paragona ai tight frame, come analogia. Le stime necessarie, sui prodotti di Hilbert–Schmidt tra mappe diverse, vengono dall'ortogonalità di Schur.
3. **Le stime di covolume per i reticoli iniziali M_α.** Si ottengono realizzando le forme come sezioni di fibrati automorfi su varietà di Shimura unitarie compattificate. Gli strumenti sono la formula di Hilbert–Samuel aritmetica (Gillet–Soulé, Zhang, Moriwaki, Yuan), un controllo della metrica di Hodge vicino al bordo e la teoria di Hodge p-adica intera (Fargues, Dieudonné prismatico di Anschütz–Le Bras).

Le norme dei sollevamenti sono date dalla formula del prodotto interno di Rallis (Gan–Qiu–Takeda): Θ_μΘ_μ* agisce su ogni autospazio di Hecke come κ₀ moltiplicato per un prodotto di valori L parziali in (h+1)/2.

Il punto delicato è che le costanti devono riprodurre esattamente M. Ciò avviene tramite i periodi CM, legati alle derivate logaritmiche di funzioni L di Dirichlet (Chowla–Selberg, Anderson), la formula delle dimensioni di Weyl e la formula di massa di Siegel. Il risultato è l'identità D_div − A·L_w = M_tot (eq. 4.5), che dà la stima (4.11) per A_tot − M_tot.

C'è anche un ingrediente combinatorio. T₂ deve essere grande ma incontrare ogni breve segmento di orbita di Frobenius in al più due posti, e lo si costruisce adattando l'insieme di Behrend privo di progressioni aritmetiche di tre termini. Alpöge scrive che questo trucco gli sembra «ovviamente» destinato a sparire.

**Denominatori e coomologia di Galois.** Proiettare sugli autospazi di Hecke può introdurre denominatori, misurati da ideali di congruenza. Questi si controllano con le rappresentazioni di Galois associate tramite il cambio di base al GL_n (Clozel–Harris–Labesse, Shin, Chenevier–Harris). Tutto si riduce a stimare un gruppo di Selmer e i gruppi S_ℓ(E,j), cioè le classi in H¹(G_{E,S_ℓ}, Q_ℓ/Z_ℓ(−j)) localmente banali, uniformemente in ℓ, in j < x^{401} e in E. Le due parti per la coniugazione complessa si trattano in modo diverso:

- **la parte "−"** con numeri di Bernoulli generalizzati, elementi di Stickelberger e operatori derivati di Kolyvagin;
- **la parte "+"** con teoria delle deformazioni e sollevamento di automorfia per U(3) e GSp₄, più l'annullamento dei gruppi di Selmer di Bloch–Kato per forme modulari, via il sistema di Eulero di Kato.

Alpöge descrive questo passo come un «indebolimento significativo di Vandiver». Il campo E si fa variare in torri ciclotomiche, usando la teoria di Iwasawa e l'annullamento dell'invariante μ (Ferrero–Washington). Restano finitamente molti twist eccezionali, per i quali si ha solo una stima grossolana. Un argomento di pigeonhole sulle scale (Lemma 5.5) sceglie un intervallo di x in cui tutti questi indici sono piccoli. È qui che nasce la restrizione a intervalli [Y, Y^{3/2}], che la parte analitica sa poi assorbire.

**Il bilanciamento.** Dopo aver diviso per il coefficiente di 𝒢_ψ, i due errori principali hanno taglia x/m e m, a meno di potenze x^{O(ε)}. Scegliendo m ≈ √x si ottiene l'esponente 1/2 + O(ε) (Lemma 6.1, Proposizione 6.3). La costante C è fissata prima di ε, per cui l'esponente può avvicinarsi a 1/2 quanto si vuole.

**Cautele.** Alpöge ammette di non padroneggiare ancora gran parte dell'argomento, soprattutto le forme automorfe di rango alto. Prevede semplificazioni drastiche e la sua cronologia riassume in parte materiale prodotto da Claude, che potrebbe «non avere senso». La garanzia di correttezza sta quindi nella verifica in Lean, non nell'esposizione in linguaggio naturale, che è ancora da scrivere. Zhang segnala infine che lo stesso giorno è stata annunciata un'altra dimostrazione, indipendente e senza IA, di Alessandro Masullo; le fonti non ne descrivono il contenuto.

### claude_full-L4-s01

*nota intera, spiegazione 2 di 8.* Fatti del livello: 21 sì, 7 in parte, 2 no (copertura 0,82) · errori 1 su 81 · analogie dichiarate 0 · segnalazioni del critico 1, errori introdotti 0 · 1555 parole (limite 1500) · Gulpease 55,8

Il risultato annunciato da Levent Alpöge il 20 novembre 2026 è l'ipotesi di Riemann generalizzata per le funzioni L di Dirichlet. Per ogni carattere primitivo χ, ogni zero di L(s,χ) nella striscia 0 < Re s < 1 ha parte reale 1/2. Il caso del conduttore 1 dà l'ipotesi di Riemann classica. La dimostrazione esiste come formalizzazione in Lean, di circa 17 milioni di righe, sviluppata con Claude. Alpöge ha scelto di non pubblicare l'esposizione in linguaggio naturale generata dall'IA, oltre 250.000 pagine. Secondo Robin Zhang, le comunità Lean e Mathlib hanno controllato la dimostrazione in un giorno, con implementazioni indipendenti del kernel, e hanno verificato che le definizioni coincidono con quelle standard. Il resoconto leggibile su cui mi baso è la nota preliminare di Zhang, scritta in gran parte da un'IA a partire dal codice Lean. Zhang stesso avverte che non può garantire che sia una traduzione fedele. Quello che segue è quindi la struttura dell'argomento secondo quella nota.

**La riduzione a una stima unilaterale.** L'oggetto aritmetico è la media di Riesz del primo ordine

S_χ(x) = Σ_{n≤x} Λ(n)χ(n)(x/n − 1),

la cui trasformata di Mellin è −L′/L(s,χ)/(s(s−1)). Si sottrae il polo in s = 1:

- per χ non principale si pone G_χ(x) = S_χ(x) + x·L′/L(1,χ);
- per il carattere banale si pone G_𝟙(x) = S_𝟙(x) − x log x + (1+γ)x.

Dato un carattere primitivo ψ di ordine r, si forma la combinazione a coefficienti positivi

𝒢_ψ = G_𝟙 + (3r+1)^{-1} Σ Re G_χ,

dove la somma corre sui caratteri primitivi che inducono le potenze di ψ. Il cuore è la Proposizione 1.2: per ogni η > 0 e ogni A esiste Y ≥ A tale che 𝒢_ψ(x) ≤ x^{1/2+η} per ogni x in [Y, Y^{3/2}].

È solo una maggiorazione, e solo su intervalli arbitrariamente lontani. Perché basta? La positività dei coefficienti fa sì che, in uno zero ρ comune a più funzioni L, il residuo della trasformata sia ν_ρ/(ρ(1−ρ)) con ν_ρ > 0, cioè una somma pesata di molteplicità che non può cancellarsi. Il passaggio successivo ricorda Landau, ma non si applica direttamente. In coordinate logaritmiche si deriva la trasformata di Laplace k volte, con k ≍ log Y. Il fattore u^k/k! è una densità gamma che concentra la massa sull'intervallo dove vale la stima, mentre fuori basta la stima banale O(x log²x). Si sceglie poi un punto σ + it in modo che un solo polo sia il più vicino, in uno spirito vicino a Turán. Il suo contributo c/(z−ρ)^{k+1} contraddice la maggiorazione, che usa solo la parte positiva di g. Questo esclude gli zeri con Re s > 1/2, e l'equazione funzionale esclude quelli a sinistra.

**Dai primi alla divisibilità di periodi.** Si sceglie un campo CM abeliano E che contiene il campo tagliato da ψ, con Gal(E/Q) = Γ. L'ortogonalità dei caratteri trasforma una condizione sul Frobenius in una somma di valori di caratteri. Ne nasce la quantità

A(a,t,w) = Σ_p log p Σ_j (pesi di Frobenius) · (a/p^j − w)_+,

che è non negativa. L'identità della Proposizione 3.1 esprime A − M come combinazione dei G_χ(a/w). Il termine principale M(a,w) contiene log a, γ, L′/L(1,κ) e i log w, cioè solo derivate logaritmiche in s = 1, senza bisogno di non annullamento nella striscia.

I parametri w si scelgono su due scale. Su un insieme T₂ di posti complessi sono vicini a b = exp(x^ε), così che a/w ≈ x. Altrove sono molto più piccoli: gli argomenti diventano enormi e bastano le regioni libere da zeri. Una media su un sottogruppo H₀ conserva esattamente i caratteri che servono per ricostruire 𝒢_ψ.

Il collegamento con le forme automorfe passa per la formula del prodotto. Se un intero algebrico non nullo è molto divisibile ai primi finiti, i suoi valori assoluti archimedei non possono essere tutti piccoli. Gli oggetti sono periodi di Bessel, alla Gan–Gross–Prasad, tra forme su gruppi unitari U(X₀) ⊂ U(Y₀) su E⁺, normalizzati in modo da avere valori in un campo di numeri K. Le minorazioni delle loro valutazioni finite contengono esattamente gli addendi (a/p^ν − w)_+ di A.

Per ottenere abbastanza divisibilità si iterano m sollevamenti theta (Weil–Howe) lungo due catene di spazi hermitiani. Gli X_j sono totalmente definiti. Le segnature degli Y_j variano finché anche Y_m diventa definito. Le identità seesaw di Kudla collegano il periodo iniziale, attraverso periodi di Bessel e di Fourier–Jacobi alternati, a un periodo di restrizione per U(Y_m) ⊂ U(X_m). Il j-esimo sollevamento aggiunge un blocco di parametri di Harish-Chandra centrato in −w_{j,ρ}. I termini favorevoli si sommano sugli m sollevamenti.

L'analogia, dichiarata da Alpöge e ripresa da Zhang, è con il metodo di Stepanov per le curve su campi finiti. Lì un polinomio ausiliario si annulla con alta molteplicità nei punti da contare. Qui m fa la parte dell'ordine di annullamento. Alpöge la descrive come una "molteplicità" difficile da trovare sugli interi, qualcosa come "derivare i numeri interi", e ottenuta in modo nativamente automorfo concatenando sollevamenti theta.

**Il confronto archimedeo, in geometria di Arakelov.** I periodi definiscono mappe integrali b_α: N_α → C = Hom(M_W, O_K). Qui M_W è un reticolo di forme test costruito dai sollevamenti theta discendenti. N_α = 𝔞_α^{-1}M′_α è il reticolo delle forme algebriche alla Gross, riscalato proprio grazie alla divisibilità dei periodi. L'obiettivo è minorare la pendenza media μ(C). Servono quattro ingredienti:

1. **Pendenze delle immagini.** La disuguaglianza delle pendenze di Bost, applicata alle filtrazioni di Harder–Narasimhan (nella versione di Stuhler–Grayson), controlla le pendenze delle immagini.
2. **Le immagini coprono quasi tutto W^∨.** Un lemma di algebra lineare, simile in spirito ai *tight frames*, garantisce che le immagini non si concentrino in un sottospazio piccolo, anche dopo aver ristretto i domini. Le ipotesi del lemma si verificano tramite stime di ortogonalità di Schur.
3. **Covolumi dei reticoli M_α.** Si ottengono realizzando le forme come sezioni di fibrati su compattificazioni di varietà di Shimura unitarie. Gli strumenti sono le formule di Hilbert–Samuel aritmetiche (Gillet–Soulé, Zhang, Moriwaki, Yuan), le stime di Fargues sulle mappe di Hodge–Tate e la teoria di Dieudonné prismatica.
4. **Norme dei sollevamenti.** Vengono dalla formula del prodotto interno di Rallis (Gan–Qiu–Takeda), che le esprime tramite valori L^S((h+1)/2, B⊗μ_j^{-1}).

Il punto delicato è che le costanti devono riprodurre esattamente il termine principale M. Accade perché la normalizzazione usa periodi di varietà abeliane CM, che per Chowla–Selberg e Anderson sono legati alle derivate logaritmiche delle L di Dirichlet. Insieme alla formula delle dimensioni di Weyl e alle formule di massa di Siegel si ottiene un'identità esatta, D_div − A·L_w = M_tot. Il risultato è la stima (4.11) per A_tot − M_tot.

Resta un problema combinatorio. Troppi posti di T₂ in un breve segmento di un'orbita di Frobenius fanno perdere precisione. Per evitarlo T₂ si costruisce adattando la costruzione di Behrend degli insiemi privi di progressioni aritmetiche di tre termini: ogni segmento rilevante contiene al più due posti.

**Denominatori e coomologia di Galois.** Le formule per le norme richiedono di proiettare sugli autospazi di Hecke. Una decomposizione non spezza necessariamente un reticolo, quindi compaiono denominatori, misurati da ideali di congruenza. Questi si controllano con le rappresentazioni di Galois associate (Clozel–Harris–Labesse, Shin, Chenevier–Harris). I gruppi da limitare sono essenzialmente i gruppi di Tate–Shafarevich S_ℓ(E,j) per Q_ℓ/Z_ℓ(−j), con j < h, e si trattano separando i due autospazi della coniugazione complessa:

- **Parte "−".** Si limita con numeri di Bernoulli generalizzati, elementi di Stickelberger e derivate di Kolyvagin.
- **Parte "+".** Serve teoria delle deformazioni alla Wiles, Taylor–Wiles e Clozel–Harris–Taylor, con forme su U(3) e GSp₄. Il sistema di Eulero di Kato dà l'annullamento dei gruppi di Selmer di Bloch–Kato di forme modulari a un twist critico non centrale.

L'uniformità al crescere del campo, lungo torri ciclotomiche, viene dalla teoria di Iwasawa e dal μ = 0 di Ferrero–Washington. Ci sono però pochi twist "eccezionali", per i quali si dispone solo di stime grossolane. Si sceglie allora l'intervallo [Y, Y²] in modo che questi indici siano piccoli rispetto a x (Lemma 5.5). È questa scelta che spiega perché la stima finale vale solo su intervalli scelti. Alpöge parla di una "significativa indebolimento di Vandiver" e ipotizza conseguenze sui K-gruppi di Z: è una sua congettura, non un risultato.

**Perché 1/2.** Dopo aver diviso per il coefficiente di 𝒢_ψ, i due errori principali hanno dimensione x/m e m, a meno di potenze x^{O(ε)}. Scegliere m ≍ √x li bilancia entrambi attorno a √x (Lemma 6.1). È la scelta che Alpöge attribuisce a Claude: una catena di sollevamenti theta lunga √X per una somma di von Mangoldt di lunghezza X, "e del resto, che altro potrebbe essere?". La Proposizione 6.3 sceglie insieme gli spazi, i pesi e i posti, in modo che le ipotesi valgano su tutto [Y, Y^{3/2}]. Da qui segue la Proposizione 1.2 e quindi la GRH.

**Cautele.** Lo stesso Alpöge dice di poter aver introdotto molte scelte subottimali e si aspetta semplificazioni drastiche; considera per esempio "ovviamente superfluo" il trucco di Behrend. La sua cronologia e alcune descrizioni sono parafrasi di riassunti dell'IA che, ammette, "potrebbero non avere alcun senso". In questo momento la garanzia di correttezza sta nella verifica Lean, non in una comprensione umana dell'argomento, che resta in gran parte da costruire. Zhang segnala infine che lo stesso giorno è stata annunciata, tramite Ravi Vakil, un'altra dimostrazione proposta della GRH, di Alessandro Masullo, ottenuta senza IA. Le fonti non ne descrivono il contenuto.

### claude_full-L4-s02

*nota intera, spiegazione 3 di 8.* Fatti del livello: 21 sì, 7 in parte, 2 no (copertura 0,82) · errori 0 su 79 · analogie dichiarate 0 · segnalazioni del critico 3, errori introdotti 0 · 1523 parole (limite 1500) · Gulpease 57,6

Il teorema annunciato da Levent Alpöge il 20 novembre 2026 è l'ipotesi di Riemann generalizzata per le funzioni L di Dirichlet: per ogni carattere primitivo χ, ogni zero di L(s,χ) nella striscia 0 < Re(s) < 1 sta sulla retta Re(s) = 1/2. Il caso χ = 1 dà l'ipotesi di Riemann classica. Prima di entrare nel merito, conviene chiarire lo statuto del testo. Alpöge ha pubblicato soltanto una formalizzazione in Lean, di circa 17 milioni di righe, e non l'esposizione di oltre 250.000 pagine generata con Claude. Secondo la nota di Robin Zhang, le comunità Lean e Mathlib hanno verificato la dimostrazione con implementazioni indipendenti del kernel e hanno controllato che le definizioni in Lean coincidano con quelle standard. Il resoconto leggibile su cui si basa quanto segue è però quello di Zhang, scritto in gran parte da un'IA a partire dal codice Lean. Zhang stesso avverte di non poterne garantire la fedeltà. Alpöge, da parte sua, dice che la sua cronologia potrebbe in alcuni punti «non avere alcun senso» e prevede semplificazioni drastiche.

**La riduzione analitica.** Al posto di ψ(x), Alpöge usa la media di Riesz del primo ordine S_χ(x) = Σ_{n≤x} Λ(n)χ(n)(x/n − 1). La sua trasformata di Mellin è semplicemente −L′/L(s,χ)/(s(s−1)). Si aggiunge poi una correzione che rende la trasformata regolare in s = 1:

- per χ non principale, G_χ(x) = S_χ(x) + x·L′(1,χ)/L(1,χ);
- per ζ, G_1(x) = Σ Λ(n)(x/n − 1) − x log x + (1+γ)x.

Per un carattere primitivo ψ di ordine r si considera la combinazione a coefficienti positivi 𝒢_ψ = G_1 + (3r+1)^{-1} Σ Re G_χ, dove χ percorre i caratteri primitivi che inducono le potenze di ψ. La positività dei coefficienti è il punto essenziale. In uno zero ρ, il residuo della trasformata è una somma pesata e positiva di molteplicità, quindi zeri comuni a più funzioni L non possono cancellarsi.

Il cuore della dimostrazione è la Proposizione 1.2: per ogni η > 0 e ogni A esiste Y ≥ A tale che 𝒢_ψ(x) ≤ x^{1/2+η} su tutto [Y, Y^{3/2}]. Si tratta di una stima unilaterale, valida solo su intervalli arbitrariamente lontani. Per ricavarne l'assenza di zeri con Re(s) > 1/2 si procede in tre passi.

1. Si passa a coordinate logaritmiche e si deriva k volte la trasformata di Laplace, con k ≍ log Y. Il peso u^k/k! è una densità gamma concentrata sull'intervallo buono, e fuori basta la stima banale O(x log² x).
2. Si combina |F^{(k)}(σ+it)| con (−1)^k F^{(k)}(σ), così che serva solo la parte positiva di g.
3. Si sceglie un centro in cui un polo sia strettamente il più vicino, nello spirito di Landau e Turán. Il suo contributo c/d^{k+1} contraddice allora la stima superiore.

La metà sinistra della striscia segue dall'equazione funzionale. Il passaggio ai caratteri non primitivi è immediato.

**Dalle somme sui primi alla divisibilità dei periodi.** L'idea guida è la formula del prodotto: un intero algebrico non nullo molto divisibile ai primi finiti non può essere piccolo a tutti i posti archimedei. Le somme sui primi devono quindi comparire come limiti inferiori per le valutazioni di periodi automorfi, e una stima archimedea dall'alto dei periodi le controlla.

Si lavora con un campo CM abeliano E che contiene il campo di ψ, e Γ = Gal(E/ℚ). Per ortogonalità dei caratteri, la condizione su Frobenius «g − jF_p ∈ I_p» si scrive come somma di valori di caratteri. Si ottiene così una quantità visibilmente non negativa, A(a,t,w) = Σ_p log p Σ_j (2/|I_p|) Σ (a/p^j − w_{ρ_t(g)})_+. La Proposizione 3.1 mostra che A − M, con un termine principale esplicito M(a,w) = a(log a − 1 − γ + ℓ_κ − f^{-1} Σ log w_ρ), è esattamente una combinazione di valori G_χ(a/w_ρ).

I pesi w_ρ si scelgono su due scale.
- Su un insieme T₂ di posti complessi si ha a/w ≈ x.
- Altrove a/w ≫ exp(x^{ε/3}), e lì bastano le regioni libere da zeri note.

Una media su un sottogruppo H₀ di Galois conserva infine proprio i caratteri che inducono le potenze di ψ.

**I periodi e i sollevamenti theta iterati.** I gruppi in gioco sono gruppi unitari su E⁺. Il periodo iniziale è un periodo di Bessel nel senso di Gan–Gross–Prasad per U(X₀) ⊂ U(Y₀), con X₀ totalmente definito. Ai due argomenti si applicano m sollevamenti theta successivi, X₀ → X₁ → … → X_m e Y₀ → … → Y_m, fino a una semplice restrizione U(Y_m) ⊂ U(X_m) in codimensione uno. Le identità seesaw di Kudla collegano i periodi intermedi, che alternano tra periodi di Bessel e di Fourier–Jacobi. A ogni passo si aggiunge un blocco di parametri di Harish-Chandra centrato in −w_{j,ρ}: è così che i pesi w della sezione precedente entrano nella teoria delle rappresentazioni.

I termini favorevoli nelle stime di valutazione si sommano sugli m sollevamenti. Alpöge propone qui un'analogia, da prendere come tale, con il metodo di Stepanov per le curve su campi finiti. Lì un polinomio ausiliario che si annulla con alta molteplicità nei punti razionali ne limita il numero. Sugli interi la «molteplicità» è difficile da trovare: sarebbe come derivare i numeri interi. Ogni sollevamento theta ne fa le veci, e m svolge il ruolo dell'ordine di annullamento. Alpöge racconta che fu Claude a suggerire, per una somma di von Mangoldt di lunghezza X, una catena di lunghezza √X.

**Il confronto aritmetico.** La divisibilità si formalizza come un'inclusione P_α(M′_α, M_W) ⊆ 𝔞_α, dove M′_α e M_W sono reticoli su O_K di forme automorfe algebriche nel senso di Gross. Riscalando si ottengono mappe intere b_α : N_α → C = Hom(M_W, O_K). L'obiettivo è stimare dal basso la pendenza media di Arakelov di C. Gli strumenti sono quattro.

- **Disuguaglianza delle pendenze di Bost**, applicata alle parti di Harder–Narasimhan (Stuhler, Grayson) dei domini.
- **Un lemma di algebra lineare**, in spirito vicino ai «tight frame». Garantisce che le immagini delle b_α ricoprano quasi tutto W^∨ anche dopo aver tolto piccole porzioni di dimensione.
- **Formule di Rallis e di Gan–Qiu–Takeda** per le norme dei sollevamenti, nella forma ΘΘ* = κ₀ Π_j L^S((h+1)/2, B ⊗ μ_j^{-1}) su ogni autospazio di Hecke.
- **Stime di covolume dei reticoli iniziali.** Si ottengono con l'aritmetica alla Hilbert–Samuel (Gillet–Soulé, Zhang, Yuan, Moriwaki) su compattificazioni di schemi di moduli unitari e con altezze di fibrati di Hodge. Il controllo ai primi finiti passa per Fargues e per la teoria di Dieudonné prismatica di Anschütz–Le Bras.

Il punto più notevole è che i termini principali si cancellano esattamente. I periodi vengono normalizzati con periodi di varietà abeliane CM, che Chowla–Selberg e Anderson legano a derivate logaritmiche di funzioni L di Dirichlet. Insieme alla formula di Weyl e alla formula di massa di Siegel, che servono a scegliere un primo ausiliario T_α, si ottiene l'identità D_div − A·L_w = M_tot. In altre parole, valutazioni finite e norme archimedee riproducono proprio il termine principale sottratto nella Proposizione 3.1, e resta solo l'eccesso A_tot − M_tot.

Serve ancora che l'insieme T₂ sia grande ma incontri ogni breve segmento di un'orbita di Frobenius in al più due punti. Per questo si adatta la costruzione di Behrend di insiemi senza progressioni aritmetiche di tre termini. Alpöge la considera un trucco «ovviamente non necessario».

**I denominatori e la coomologia di Galois.** Proiettare sugli autospazi di Hecke può introdurre denominatori, misurati dalle congruenze tra autovalori di Hecke. Queste congruenze si traducono in classi di estensione di rappresentazioni di Galois, costruite con i risultati di Clozel–Harris–Labesse, Shin e Chenevier–Harris. Ne nascono i gruppi S_ℓ(E,j), cioè classi in H¹ con coefficienti in ℚ_ℓ/ℤ_ℓ(−j) che sono localmente banali. Bisogna mostrare che la loro «taglia» complessiva V(E,h) è al più exp(x^ε/2).

Le due autoparti rispetto al coniugio complesso si trattano in modo diverso.
- **Parte «meno»:** numeri di Bernoulli generalizzati, elementi di Stickelberger e derivate di Kolyvagin.
- **Parte «più»:** deformazioni e sollevamento di automorfia, alla Wiles, Taylor–Wiles e Clozel–Harris–Taylor, su U(3) e GSp₄. Interviene anche l'annullamento dei gruppi di Selmer di Bloch–Kato tramite il sistema di Eulero di Kato.

Il campo E varia lungo torri ciclotomiche, controllate dall'annullamento dell'invariante μ (Ferrero–Washington). Restano pochi twist «eccezionali». Il Lemma 5.5 sceglie l'intervallo [Y, Y²] in modo che tutti cadano sotto x^η, ed è questo il motivo per cui la stima principale vale solo su intervalli. Alpöge osserva che serve un indebolimento significativo della congettura di Vandiver, e che ne seguirebbero l'annullamento di vari K-gruppi di ℤ.

**Perché proprio 1/2.** Messo tutto insieme, i due errori dominanti nella stima di 𝒢_ψ(x) hanno ordine x/m e m, a meno di potenze arbitrariamente piccole di x. Scegliendo m ≈ √x entrambi sono circa √x. Il Lemma 6.1 e la Proposizione 6.3 regolano simultaneamente il numero di sollevamenti, la dimensione k di X₀, i posti scelti e i campi, e danno 𝒢_ψ(x) ≤ x^{1/2+η}. A quel punto la Sezione 2 chiude la dimostrazione.

**Lo stato delle cose.** La verifica formale, secondo le fonti, è completa. La comprensione umana, invece, è appena all'inizio: nessuno ha letto l'argomento per intero, e la mappa qui descritta è una ricostruzione mediata da IA. Zhang segnala inoltre che lo stesso giorno è stata annunciata una dimostrazione indipendente, senza uso di IA, di Alessandro Masullo.

### claude_full-L4-s03

*nota intera, spiegazione 4 di 8.* Fatti del livello: 22 sì, 6 in parte, 2 no (copertura 0,83) · errori 0 su 75 · analogie dichiarate 0 · segnalazioni del critico 0, errori introdotti 0 · 1348 parole (limite 1500) · Gulpease 53,5

Il risultato annunciato da Levent Alpöge il 20 novembre 2026 è l'ipotesi di Riemann generalizzata per le funzioni L di Dirichlet. Per ogni carattere primitivo χ, ogni zero di L(s,χ) nella striscia 0 < Re(s) < 1 sta sulla retta Re(s) = 1/2. Il passaggio ai caratteri imprimitivi è immediato, e il caso del conduttore 1 dà l'ipotesi di Riemann classica.

Sullo stato del risultato va detto subito questo. Alpöge ha pubblicato soltanto una formalizzazione in Lean di circa 17 milioni di righe. Ha scelto di non diffondere l'esposizione generata dall'IA, che supera le 250.000 pagine. Secondo la nota di Robin Zhang (IHES, 21 novembre), le comunità di Lean e Mathlib hanno già verificato la dimostrazione con implementazioni indipendenti del kernel. Hanno anche controllato che le definizioni in Lean coincidano con quelle matematiche standard. Una dimostrazione leggibile da un essere umano però non esiste ancora. Quanto segue ricostruisce l'argomento dalla nota di Zhang, che lui stesso dichiara scritta in gran parte da un'IA a partire dal codice Lean e di cui non garantisce la fedeltà. Uso anche la cronologia di Alpöge, che però l'autore descrive come una parafrasi in parte poco familiare anche a lui.

**La riduzione analitica.** Si lavora con la media di Riesz del primo ordine, corretta in modo da eliminare la singolarità in s = 1:

G_χ(x) = Σ_{n≤x} Λ(n)χ(n)(x/n − 1) + x·L′(1,χ)/L(1,χ),

e, per il carattere principale, G_1(x) = Σ Λ(n)(x/n − 1) − x log x + (1+γ)x. La trasformata di Mellin di G_χ è −L′/L(s,χ)/(s(s−1)) più termini correttivi, ed è olomorfa in s = 1. Fissato ψ primitivo di ordine r, si considera la combinazione a coefficienti positivi

𝒢_ψ = G_1 + (3r+1)^{−1} Σ Re G_χ,

dove χ percorre i caratteri primitivi che inducono le potenze di ψ. Il cuore della dimostrazione è la Proposizione 1.2: per ogni η > 0 esistono Y arbitrariamente grandi tali che 𝒢_ψ(x) ≤ x^{1/2+η} per ogni x ∈ [Y, Y^{3/2}].

È una stima molto debole in apparenza: unilaterale e valida solo su intervalli sparsi. Basta comunque, per un argomento di tipo Landau–Turán. Si scrive la trasformata in coordinate logaritmiche come trasformata di Laplace F(s). Grazie alla positività dei coefficienti, il residuo in uno zero ρ vale ν_ρ/(ρ(1−ρ)), con ν_ρ somma pesata e positiva delle molteplicità: zeri comuni a più L-funzioni non possono cancellarsi. Si deriva F circa log Y volte. Il nucleo u^k/k!·e^{−σu} è allora una densità gamma concentrata sull'intervallo in cui vale la stima, mentre fuori basta la stima banale |G_χ(x)| ≪ x log²x. Si sceglie un punto σ+it in cui un solo polo è il più vicino. Con le stime di Cauchy, questo polo domina |F^{(k)}| e contraddice la maggiorazione. Quindi non ci sono zeri con Re(s) > 1/2 + η, e l'equazione funzionale sistema l'altra metà della striscia.

**L'idea centrale: la formula del prodotto.** Se un intero algebrico non nullo è molto divisibile ai primi finiti, i suoi valori assoluti archimedei non possono essere tutti piccoli. Alpöge costruisce periodi automorfi normalizzati P_α(f,g), a valori in un campo di numeri K, che si comportano così:

- le minorazioni delle loro valutazioni p-adiche contengono proprio termini del tipo (a/p^ν − w)_+, con p soggetto a condizioni di Frobenius;
- le maggiorazioni archimedee vengono dalle norme di Petersson.

L'ortogonalità dei caratteri (Proposizione 3.1) traduce le condizioni di Frobenius in una somma su χ di w·G_χ(a/w), meno un termine principale esplicito M(a,w). Questo termine contiene log a, γ, L′/L(1,κ) per un carattere quadratico κ e i logaritmi dei pesi w. Una media su un sottogruppo del gruppo di Galois isola poi i caratteri che inducono le potenze di ψ.

**Sollevamenti theta iterati.** Si prende un campo CM abeliano E che contiene il campo tagliato da ψ, e si lavora con gruppi unitari su E⁺. Il periodo iniziale è un periodo di Bessel, nel senso di Gan–Gross–Prasad, per U(X₀) ⊂ U(Y₀), con X₀ totalmente definito.

Si applica poi m volte la corrispondenza theta di Weil–Howe su entrambi i lati, ottenendo due catene di gruppi U(X_j) e U(Y_j). Le identità seesaw di Kudla collegano il periodo iniziale alla coppia di restrizione finale U(Y_m) ⊂ U(X_m), passando per periodi di Fourier–Jacobi negli stadi dispari. Ogni sollevamento aggiunge un blocco di parametri di Harish-Chandra centrato in −w_{j,ρ} e un contributo alla divisibilità del periodo. Dunque il guadagno di divisibilità cresce linearmente in m.

Alpöge e Zhang propongono un'analogia, che va presa come tale: il metodo di Stepanov per le curve su campi finiti. Lì un polinomio ausiliario si annulla con alta molteplicità nei punti razionali. Alpöge osserva che sugli interi la molteplicità è difficile da trovare, perché «corrisponde a qualcosa come derivare i numeri interi». Ogni sollevamento theta ne fa le veci: m gioca il ruolo dell'ordine di annullamento.

**Il lato archimedeo e il termine principale.** Per le norme si usa la formula di Rallis (Gan–Qiu–Takeda). Sugli autospazi di Hecke, ΘΘ* agisce come κ₀ volte il prodotto per j da 1 a m di L^S((h+1)/2, B⊗μ_j^{−1}). Il punto sorprendente è che le costanti tornano esattamente:

- i periodi delle varietà abeliane CM che servono a normalizzare, tramite Chowla–Selberg e Anderson, sono legati alle derivate logaritmiche delle L di Dirichlet;
- le dimensioni vengono dalla formula di Weyl e dalla formula di massa di Siegel.

Combinando i due contributi si ottiene un'identità che ricostruisce esattamente il termine principale M_tot (l'equazione 4.5). Resta così da stimare solo l'eccesso.

**Geometria di Arakelov.** Il confronto non avviene sui singoli valori ma tra reticoli. Si hanno applicazioni intere b_α : N_α → C = Hom(M_W, O_K), dove N_α è un reticolo di forme automorfe algebriche riscalato secondo la divisibilità. Serve una minorazione della pendenza media μ(C).

Per i covolumi di N_α si usano:

- le forme automorfe come sezioni di fibrati sulle varietà di Shimura unitarie compattificate;
- l'Hilbert–Samuel aritmetico (Gillet–Soulé, Zhang, Moriwaki, Yuan);
- per le strutture intere ai primi finiti, Fargues e la teoria di Dieudonné prismatica di Anschütz–Le Bras.

Bisogna poi garantire che le immagini delle b_α riempiano quasi tutto lo spazio W^∨. Questo lo fa un lemma di algebra lineare di tipo «frame quasi stretto» (Lemma 4.2), combinato con la filtrazione di Harder–Narasimhan e la disuguaglianza delle pendenze di Bost (Proposizione 4.3).

**Denominatori e coomologia di Galois.** Proiettare sugli autospazi di Hecke può introdurre denominatori, che misurano le congruenze tra autosistemi. Per controllarli si attaccano rappresentazioni di Galois (Clozel–Harris–Labesse, Shin, Chenevier–Harris) e ci si riduce a stimare gruppi di classi localmente banali S_ℓ(E,j) in H¹ a coefficienti in Q_ℓ/Z_ℓ(−j). Le due parti si trattano diversamente:

- la parte «meno» si stima con numeri di Bernoulli generalizzati, elementi di Stickelberger e derivate di Kolyvagin;
- la parte «più» si stima con deformazioni alla Wiles, Taylor–Wiles e Clozel–Harris–Taylor su U(3) e GSp₄, più il sistema di Eulero di Kato.

L'uniformità al variare di E lungo torri ciclotomiche viene da Iwasawa e dal teorema di Ferrero–Washington (μ = 0). Restano alcune torsioni eccezionali che si sanno stimare solo grossolanamente. Per renderle innocue si sceglie un intervallo di x opportuno, ed è questa la ragione per cui la Proposizione 1.2 vale solo su intervalli scelti. Una variante della costruzione di Behrend degli insiemi senza progressioni aritmetiche di tre termini serve a scegliere molte posizioni complesse senza che troppe cadano in un breve tratto di orbita di Frobenius. Alpöge stesso ritiene questo trucco quasi certamente superfluo.

**Perché proprio 1/2.** Raccogliendo tutto, i due errori principali nella stima di 𝒢_ψ(x) hanno dimensione x/m e m, a meno di potenze piccole di x. La scelta ottimale è m ≈ √x, e l'esponente 1/2 nasce da questo bilanciamento (Lemma 6.1). Alpöge racconta che la lunghezza √X della catena di sollevamenti è stata suggerita da Claude, e aggiunge: «e del resto, cos'altro potrebbe essere?».

**Cautele.** Alpöge stesso dice di aver probabilmente introdotto molte scelte subottimali e si aspetta semplificazioni drastiche. Ha annunciato l'intenzione di scrivere una versione leggibile. Zhang sottolinea che nessun essere umano può oggi confrontare un riassunto in linguaggio naturale con 17 milioni di righe di Lean. La correttezza formale è certificata dalla verifica in Lean. La comprensione matematica dell'argomento, invece, è ancora in gran parte da costruire.

### claude_full-L4-s04

*nota intera, spiegazione 5 di 8.* Fatti del livello: 23 sì, 5 in parte, 2 no (copertura 0,85) · errori 1 su 73 · analogie dichiarate 0 · segnalazioni del critico 1, errori introdotti 0 · 1526 parole (limite 1500) · Gulpease 55,2

L'enunciato è l'ipotesi di Riemann generalizzata per le funzioni L di Dirichlet: per ogni carattere primitivo χ, ogni zero di L(s,χ) nella striscia 0 < Re(s) < 1 ha parte reale 1/2. Il caso del conduttore 1 dà l'ipotesi di Riemann classica. Il passaggio ai caratteri non primitivi è immediato, perché i fattori di Eulero aggiunti non si annullano per Re(s) > 0.

Prima di entrare nel merito conviene chiarire lo stato delle fonti. Alpöge ha pubblicato soltanto una formalizzazione in Lean, di circa 17 milioni di righe. Ha scelto di non diffondere un'esposizione generata dall'IA di oltre 250.000 pagine. Secondo Robin Zhang, le comunità Lean e Mathlib hanno verificato in un giorno la dimostrazione con implementazioni indipendenti del kernel e hanno controllato che le definizioni in Lean coincidano con quelle standard. Quello che segue ricalca però la nota di Zhang, che è una ricostruzione scritta in gran parte da un'IA a partire dal codice. Zhang stesso avverte di non poter garantire che sia una traduzione fedele. Alpöge, dal canto suo, dice di non padroneggiare ancora diverse parti dell'argomento e si aspetta semplificazioni drastiche.

**La riduzione analitica**

L'oggetto di partenza è la media di Riesz del primo ordine

S_χ(x) = Σ_{n≤x} Λ(n)χ(n)(x/n − 1).

La sua trasformata di Mellin è esattamente −L′(s,χ)/(s(s−1)L(s,χ)). Si corregge poi il polo in s = 1. Per χ non principale si pone G_χ = S_χ + x·L′(1,χ)/L(1,χ); per ζ si pone G_1 = S_1 − x log x + (1+γ)x. Fissato ψ primitivo di ordine r, si costruisce la combinazione a coefficienti positivi

𝒢_ψ = G_1 + (3r+1)^{−1} Σ_χ Re G_χ,

dove la somma corre sui caratteri primitivi che inducono le potenze di ψ. La positività dei coefficienti fa sì che il residuo in uno zero ρ sia ν_ρ/(ρ(1−ρ)), con ν_ρ > 0: uno zero condiviso da più L-funzioni non può cancellarsi.

Il cuore analitico è la Proposizione 1.2. Per ogni η > 0 esistono Y arbitrariamente grandi tali che 𝒢_ψ(x) ≤ x^{1/2+η} su tutto l'intervallo [Y, Y^{3/2}]. Si tratta di una stima solo dall'alto e solo su intervalli sparsi. Per vedere che basta, si passa in coordinate logaritmiche e si deriva la trasformata di Laplace k volte, con k ≍ log Y. Il nucleo u^k e^{−σu}/k! è una densità gamma che concentra la massa sull'intervallo buono; fuori dall'intervallo basta la stima banale |g(u)| ≪ e^{2u}. Combinando |F^{(k)}(σ+it)| con (−1)^k F^{(k)}(σ) si usa solo la parte positiva di g. Se ci fosse un polo con parte reale maggiore di ϑ, scegliendo il centro in modo che quel polo sia il più vicino, le stime di Cauchy darebbero una crescita incompatibile. Zhang collega questo passo al teorema di Landau sulle serie a coefficienti non negativi e al metodo di Turán. L'equazione funzionale esclude poi gli zeri a sinistra della retta critica.

**Il cuore aritmetico: divisibilità contro grandezza archimedea**

L'idea guida è la formula del prodotto: un intero algebrico non nullo molto divisibile ai primi finiti non può essere piccolo in tutte le norme archimedee.

Si sceglie un campo CM abeliano E che contiene il campo tagliato da ψ, e si considerano gruppi unitari definiti su E⁺. Su di essi si definiscono periodi automorfi P_α(f,g): periodi di Bessel nel senso di Gan–Gross–Prasad, normalizzati in modo da prendere valori in un campo di numeri K. Le minorazioni delle valutazioni di questi periodi ai primi di K contengono somme del tipo Σ log p · (a/p^ν − w)_+, ristrette a primi con una condizione di Frobenius.

Per ortogonalità dei caratteri, la Proposizione 3.1 riscrive queste somme come combinazioni di G_χ(a/w), più un termine principale esplicito M(a,w). Questo termine contiene log a, γ, L′(1,κ)/L(1,κ) per un carattere quadratico dispari κ, e i log w. I parametri w sono i centri dei blocchi di parametri di Harish-Chandra aggiunti a ogni sollevamento. Vengono scelti su due scale: vicino a x su un insieme T₂ di posti complessi, molto più grandi altrove, dove bastano regioni prive di zeri. Mediando su un sottogruppo di Gal(E/Q) restano proprio i caratteri che compaiono in 𝒢_ψ.

Per scegliere T₂ abbastanza grande, ma tale che ogni breve segmento di un'orbita di Frobenius lo intersechi in al più due posti, si usa una variante della costruzione di Behrend di insiemi senza progressioni aritmetiche di tre termini.

**Sollevamenti theta iterati e analogia con Stepanov**

La divisibilità si accumula applicando m volte la corrispondenza theta, lungo due catene di spazi hermitiani X_j e Y_j. Gli X_j sono definiti; le segnature degli Y_j variano finché anche Y_m diventa definito. Le identità seesaw di Kudla collegano il periodo di Bessel iniziale a una restrizione finale U(Y_m) ⊂ U(X_m), passando per periodi alternativamente di Bessel e di Fourier–Jacobi.

L'analogia è dichiarata dagli autori stessi ed è con il metodo di Stepanov sulle curve sui campi finiti. Lì si costruisce un polinomio ausiliario che si annulla con alta molteplicità nei punti, e si confronta il grado con l'ordine di annullamento. Sugli interi, scrive Alpöge, la molteplicità è difficile da trovare, perché corrisponderebbe a "derivare i numeri interi". Ogni sollevamento theta fa da surrogato di un'unità di molteplicità, e m svolge il ruolo dell'ordine di annullamento.

L'aneddoto che Alpöge presenta come decisivo è che Claude abbia proposto una catena di lunghezza √X. Nella ricostruzione di Zhang l'esponente 1/2 nasce proprio così: i due errori principali hanno taglia x/m e m (a meno di potenze x^ε), e m ≈ √x li bilancia.

**Il lato archimedeo: reticoli, pendenze, termine principale**

Per tradurre la divisibilità in una disuguaglianza servono stime archimedee molto precise. Si lavora con O_K-reticoli di forme automorfe algebriche nel senso di Gross. I periodi definiscono mappe intere b_α: N_α → C, dove C è il duale di un reticolo M_W di forme test ottenuto da sollevamenti theta "verso il basso".

Le norme si controllano con la formula del prodotto interno di Rallis (Gan–Qiu–Takeda): ΘΘ* agisce su un autospazio di Hecke come κ₀ ∏_j L^S((h+1)/2, B ⊗ μ_j^{−1}).

La pendenza media di C viene minorata con un argomento di Arakelov. Si usano la filtrazione di Harder–Narasimhan per i reticoli hermitiani, la disuguaglianza delle pendenze di Bost e un lemma di algebra lineare. Il lemma dice che, se le mappe normalizzate sono quasi isometrie e Σ γ_i B_i B_i* è quasi scalare (una sorta di "frame stretto" approssimato), restringere i domini fa perdere solo una frazione controllata del bersaglio.

I covolumi dei reticoli iniziali si stimano realizzando le forme come sezioni di fibrati automorfi su schemi di moduli unitari compattificati. Gli strumenti sono la formula di Hilbert–Samuel aritmetica (Gillet–Soulé, Zhang, Moriwaki), il criterio di Yuan e il controllo delle strutture intere ai primi finiti tramite le mappe di Hodge–Tate di Fargues e la teoria di Dieudonné prismatica di Anschütz–Le Bras.

Il punto cruciale è che le costanti coincidano. I periodi CM, tramite Chowla–Selberg e Anderson, producono le derivate logaritmiche di L-funzioni di Dirichlet. La formula di Weyl e le formule di massa di Siegel danno le dimensioni. L'identità D_div − A·L_w = M_tot mostra che i contributi finiti e archimedei ricostruiscono esattamente il termine principale sottratto nei G_χ. Senza questa cancellazione esatta, una stima di A(a,t,w) da sola non servirebbe a nulla.

**I denominatori e la coomologia di Galois**

Proiettare su autospazi di Hecke può introdurre denominatori nei reticoli, controllati dagli ideali di congruenza. Questi si misurano tramite le rappresentazioni di Galois associate (Clozel–Harris–Labesse, Shin, Chenevier–Harris). Il contributo critico sono i gruppi S_ℓ(E,j): classi di H¹ non ramificate fuori da ℓ, a coefficienti in Q_ℓ/Z_ℓ(−j), che si annullano localmente. Va stimata la loro lunghezza totale V(E,h), pesata con log ℓ, per tutti i j < x^{401}.

La parte "−" per la coniugazione complessa si controlla con numeri di Bernoulli generalizzati, elementi di Stickelberger e derivate di Kolyvagin. La parte "+" si controlla con la teoria delle deformazioni e i sollevamenti di automorfia su U(3) e GSp₄. Il sistema di Eulero di Kato serve qui ad annullare certi gruppi di Selmer di Bloch–Kato. Alpöge descrive questo passo come una "significativa indebolitura di Vandiver".

Per far variare E lungo torri ciclotomiche si usano Iwasawa e l'annullamento dell'invariante μ (Ferrero–Washington). Restano finitamente molte torsioni eccezionali, per cui esiste solo una stima grossolana. È qui che serve la libertà di scegliere l'intervallo: un lemma elementare trova [Y, Y²] in cui tutti gli indici eccezionali sono sotto x^η. Questo spiega perché la stima su 𝒢_ψ vale solo su intervalli sparsi.

**Assemblaggio e cautele**

La stima finale (4.11), divisa per il coefficiente di 𝒢_ψ e con i parametri scelti nei range del Lemma 6.1 (m tra x^{1/2−ε} e x^{1/2+ε/2}, dim X₀ tra xm e n²x^{1/2−ε}), dà 𝒢_ψ(x) ≤ x^{1/2+(C+4)ε}. La costante C è fissata prima di ε, e la Sezione 2 conclude.

Resta l'avvertenza più importante. Il lettore umano oggi dispone di una prova verificata dalla macchina e di una mappa ricostruita in larga parte da un'IA, non di un testo leggibile da cima a fondo. Alpöge stesso avverte che le sue descrizioni delle parti più tecniche sono parafrasi che "potrebbero non avere alcun senso" e che potrebbe aver incorporato molte scelte subottimali. Uno studio umano dell'argomento è appena cominciato. Zhang ricorda inoltre che lo stesso giorno è stata annunciata, in modo indipendente, una dimostrazione di Masullo ottenuta senza IA.

### claude_full-L4-s05

*nota intera, spiegazione 6 di 8.* Fatti del livello: 19 sì, 9 in parte, 2 no (copertura 0,78) · errori 1 su 80 · analogie dichiarate 0 · segnalazioni del critico 1, errori introdotti 1 · 1436 parole (limite 1500) · Gulpease 54,7

Le fonti vanno inquadrate prima di entrare nel merito. Alpöge non ha pubblicato un testo matematico leggibile. Ha rilasciato solo una formalizzazione in Lean, di circa 17 milioni di righe secondo Zhang, e ha rinunciato a diffondere un'esposizione generata dall'IA di oltre 250.000 pagine. Zhang riferisce che in un giorno le comunità Lean e Mathlib hanno verificato la dimostrazione con implementazioni indipendenti del kernel e hanno controllato che le definizioni coincidano con quelle standard.

L'architettura descritta qui sotto è quella ricostruita da Zhang. Lui stesso è partito da un riassunto del codice prodotto da GPT 6 Pro e dichiara di non poter garantire che sia una traduzione fedele. Alpöge, a sua volta, avverte che alcune descrizioni potrebbero «non avere senso» e si aspetta semplificazioni drastiche.

**L'enunciato.** Per ogni carattere di Dirichlet primitivo χ, ogni zero di L(s,χ) con 0 < Re s < 1 ha parte reale 1/2. Il caso dei caratteri non primitivi, ζ compresa, segue subito perché i fattori di Eulero aggiunti non si annullano per Re s > 0.

**La riduzione analitica.** L'oggetto centrale è la media di Riesz del primo ordine S_χ(x) = Σ_{n≤x} Λ(n)χ(n)(x/n − 1). La sua trasformata di Mellin è −L′(s,χ)/(s(s−1)L(s,χ)). Per eliminare il polo in s = 1 si corregge:
- G_χ(x) = S_χ(x) + x·L′(1,χ)/L(1,χ) per χ non principale;
- G_𝟙(x) = Σ Λ(n)(x/n − 1) − x log x + (1+γ)x per il carattere principale.

Fissato ψ primitivo di ordine r, si forma 𝒢_ψ = G_𝟙 + (3r+1)⁻¹ Σ Re G_χ, dove χ percorre i caratteri primitivi non banali che inducono le potenze di ψ. Il risultato chiave (Proposizione 1.2) è il seguente: per ogni η > 0 e ogni A esiste Y ≥ A tale che 𝒢_ψ(x) ≤ x^{1/2+η} per ogni x ∈ [Y, Y^{3/2}].

La stima ha due debolezze: è solo una maggiorazione e vale solo su intervalli. Basta comunque, per tre ragioni.
- **Nessuna cancellazione.** Poiché i coefficienti sono positivi, in uno zero ρ comune a più L-funzioni il residuo della trasformata vale ν_ρ/(ρ(1−ρ)) con ν_ρ > 0.
- **Concentrazione sull'intervallo.** In coordinate logaritmiche si deriva la trasformata di Laplace k volte, con k ≍ log Y. Dopo la divisione per k!, il nucleo u^k e^{−σu}/k! è una densità gamma che concentra la massa sull'intervallo dove vale la stima. Fuori basta la stima banale |g(u)| ≪ e^{2u}.
- **Uso della sola maggiorazione.** Si combina |A_k(t)| + A_k(0) ≤ 2∫(u^k/k!) g(u)₊ e^{−σu} du. Scegliendo poi il centro σ+it in modo che un solo polo sia il più vicino, in spirito vicino a Turán, il termine c/(z−ρ)^{k+1} domina e contraddice la stima. Se il polo più vicino è reale, serve la positività del residuo.

Zhang cita Landau come precedente. L'equazione funzionale esclude infine la metà sinistra della striscia.

**Il lato aritmetico.** Si sceglie un campo CM abeliano E che contiene il campo tagliato da ψ. L'ortogonalità dei caratteri in Gal(E/ℚ) trasforma una condizione sul Frobenius in somme di caratteri. Ne esce una quantità non negativa

A(a,t,w) = Σ_p log p Σ_j (2/|I_p|) Σ_{g ∉ Φ, g − jF_p ∈ I_p} (a/p^j − w_{ρ_t(g)})₊,

e l'identità della Proposizione 3.1 la scrive come M(a,w) più una combinazione dei G_χ(a/w). Il termine principale è

M(a,w) = a(log a − 1 − γ + ℓ_κ − f⁻¹ Σ log w_ρ), con ℓ_κ = L′(1,κ)/L(1,κ).

Compaiono solo derivate logaritmiche in 1, quindi l'argomento non è circolare.

I pesi w sono scelti su due scale:
- su un insieme T₂ di posti complessi si ha a/w ≈ x;
- altrove l'argomento è ≫ exp(x^{ε/3}), e bastano le regioni libere da zeri note.

Una media su un sottogruppo H₀ conserva i caratteri che servono per 𝒢_ψ.

**Il ponte automorfo.** L'idea guida è la formula del prodotto: un intero algebrico non nullo molto divisibile nei primi finiti non può essere piccolo in tutti i posti archimedei. Si costruiscono periodi automorfi P_α(f,g), normalizzati a valori in un campo di numeri K.
- Le loro valutazioni finite sono minorate da espressioni che contengono esattamente i sommandi (a_t/p^ν − w)₊ di A.
- Le loro norme archimedee sono maggiorate.

Ne segue una maggiorazione per A − M.

Il periodo iniziale è un periodo di Bessel, alla Gan–Gross–Prasad, per l'inclusione U(X₀) ⊂ U(Y₀) di gruppi unitari su E⁺, con X₀ totalmente definito. Si applica poi la corrispondenza theta (Weil, Howe) m volte su entrambi gli argomenti, fino ad avere Y_m definito. Le identità seesaw di Kudla collegano il periodo iniziale a un accoppiamento di restrizione U(Y_m) ⊂ U(X_m), passando per periodi alternativamente di Bessel e di Fourier–Jacobi.

Ogni lift su U(X_j) aggiunge un blocco di parametri di Harish-Chandra centrato in −w_{j,ρ}: è qui che entrano i pesi della parte aritmetica. I contributi favorevoli alle valutazioni si sommano sugli m lift, e questo produce un fattore m.

**Un'analogia (dichiarata come tale nelle fonti).** È il metodo di Stepanov per contare punti di curve su campi finiti, che usa un polinomio ausiliario che si annulla con alta molteplicità. Sugli interi, scrive Alpöge, la molteplicità è difficile da trovare: è «qualcosa come derivare numeri interi». Ogni lift theta ne imita un grado, e m fa le veci dell'ordine di annullamento. Alpöge racconta che per una somma di von Mangoldt di lunghezza X fu Claude a proporre una catena di lunghezza √X.

**Le costanti.** I G_χ hanno già il termine principale sottratto, quindi le costanti devono tornare esattamente. Gli strumenti sono:
- per le norme dei lift, la formula del prodotto interno di Rallis (Gan–Qiu–Takeda): ΘΘ*|_{W[B]} = κ₀ Π_j L^S((h+1)/2, B ⊗ μ_j⁻¹);
- per dimensioni e molteplicità, la formula di Weyl e conteggi di reticoli hermitiani alla Siegel;
- per la normalizzazione, i periodi di varietà abeliane CM, legati alle derivate logaritmiche di L di Dirichlet (Chowla–Selberg, Anderson);
- per le valutazioni finite dei fattori algebrici, la reciprocità di Shimura–Taniyama e l'integralità di Deligne–Ribet.

L'esito è l'identità D_div − A·L_w = M_tot: i contributi dei posti finiti e di quelli archimedei riproducono esattamente il termine principale.

**La geometria di Arakelov.** Per confrontare valutazioni finite e norme archimedee si lavora con reticoli. Si fissano:
- un reticolo M_α di forme automorfe algebriche (nel senso di Gross) su U(X₀);
- un sottoreticolo M′_α e un ideale 𝔞_α tali che P_α(M′_α, M_W) ⊆ 𝔞_α;
- N_α = 𝔞_α⁻¹M′_α e le mappe integrali b_α : N_α → C = Hom(M_W, 𝒪_K).

L'obiettivo è minorare la pendenza media di C. Per farlo servono:
- i covolumi di M_α, ottenuti realizzando forme olomorfe come sezioni di fibrati di Hodge su schemi di moduli unitari compattificati (Faltings–Chai);
- il teorema di Hilbert–Samuel aritmetico (Gillet–Soulé, Zhang, Moriwaki, Yuan);
- il controllo delle strutture intere p-adiche (Fargues, Anschütz–Le Bras);
- la filtrazione di Harder–Narasimhan e la disuguaglianza delle pendenze di Bost;
- un lemma di algebra lineare (Lemma 4.2, affine ai «tight frame»), che garantisce che le immagini delle b_α ricoprano quasi tutto W^∨ anche dopo la restrizione ai sottoreticoli di pendenza alta.

**I denominatori.** Proiettare sugli autospazi di Hecke può introdurre denominatori, misurati da congruenze tra autovalori. Per controllarle si passa alle rappresentazioni di Galois associate (Clozel–Harris–Labesse, Shin, Chenevier–Harris). Ci si riduce così a gruppi di Selmer e ai gruppi S_ℓ(E,j) di classi in H¹ a coefficienti ℚ_ℓ/ℤ_ℓ(−j) che sono banali localmente.
- **Parte «meno».** Si tratta con numeri di Bernoulli generalizzati, elementi di Stickelberger e derivate di Kolyvagin.
- **Parte «più».** Si tratta con deformazioni e metodi alla Taylor–Wiles / Clozel–Harris–Taylor su U(3) e GSp₄ (Weissauer). Il sistema di Euler di Kato serve ad annullare i Selmer di Bloch–Kato che compaiono.
- **Torri ciclotomiche.** Il campo E varia in torri ciclotomiche e si usa μ = 0 di Ferrero–Washington.

Per pochi twist eccezionali si dispone solo di una stima grossolana. Lì si sfrutta la libertà di scegliere l'intervallo (Lemma 5.5), ed è per questo che la Proposizione 1.2 è formulata su intervalli. Alpöge chiama questo passo «un indebolimento significativo di Vandiver».

**Il bilanciamento.** I due errori principali hanno taglia x/m e m, a meno di fattori x^{O(ε)}. Scegliere m ≈ √x dà l'esponente 1/2.

L'insieme T₂ deve soddisfare due esigenze opposte:
- essere grande, per avere abbastanza divisibilità;
- intersecare ogni breve segmento di orbita di Frobenius in al più due punti.

Lo si costruisce adattando gli insiemi di Behrend privi di progressioni aritmetiche di tre termini. Alpöge giudica questo trucco quasi certamente superfluo. Chiude l'argomento il fatto che la costante dell'errore non dipenda da ε.

In sintesi, la verifica formale, stando a Zhang, è avvenuta. La comprensione umana della dimostrazione invece è appena cominciata: l'unica esposizione in prosa disponibile è in larga parte scritta dall'IA, e lo stesso autore pensa di aver inserito molte scelte subottimali.

### claude_full-L4-s06

*nota intera, spiegazione 7 di 8.* Fatti del livello: 21 sì, 6 in parte, 3 no (copertura 0,80) · errori 0 su 75 · analogie dichiarate 0 · segnalazioni del critico 0, errori introdotti 0 · 1483 parole (limite 1500) · Gulpease 53,5

Il 20 novembre 2026 Levent Alpöge ha annunciato una dimostrazione dell'ipotesi di Riemann generalizzata per le funzioni L di Dirichlet, trovata lavorando con Claude. L'ha pubblicata solo come formalizzazione in Lean, di circa 17 milioni di righe, e ha scelto di non diffondere un'esposizione generata dall'IA di oltre 250.000 pagine. Secondo la nota preliminare di Robin Zhang, in un giorno le comunità Lean e Mathlib hanno verificato la prova con implementazioni indipendenti del kernel e hanno controllato che le definizioni coincidano con quelle standard.

Ricostruisco l'architettura dalla nota di Zhang. Zhang stesso avverte che il suo testo è in larga parte scritto da un'IA a partire dal codice e che non può garantire che sia una traduzione fedele del Lean. Alpöge, da parte sua, dichiara di non padroneggiare ancora molte parti e si aspetta forti semplificazioni.

**L'enunciato e la riduzione.** Si dimostra che, per ogni carattere di Dirichlet primitivo χ, gli zeri di L(s,χ) con 0 < Re s < 1 stanno su Re s = 1/2. Tutto si riduce a una stima unilaterale su somme sulle potenze di primi.

Si parte dalla media di Riesz del primo ordine S_χ(x) = Σ_{n≤x} Λ(n)χ(n)(x/n − 1). La sua trasformata di Mellin è −L′(s,χ)/(s(s−1)L(s,χ)). Si elimina il polo in s = 1 con una correzione:
- per χ non principale si aggiunge xL′(1,χ)/L(1,χ);
- per ζ si sottrae x log x − (1+γ)x.

Si ottengono così le funzioni G_χ. Fissato ψ primitivo di ordine r, si forma la combinazione a coefficienti positivi 𝒢_ψ = G_1 + (3r+1)^{−1} Σ Re G_χ, dove la somma corre sui caratteri primitivi che inducono le potenze di ψ. Il cuore della prova è la Proposizione 1.2: per ogni η > 0 esistono Y arbitrariamente grandi tali che 𝒢_ψ(x) ≤ x^{1/2+η} su tutto l'intervallo [Y, Y^{3/2}].

**Primo passo: dalla stima agli zeri.** Una maggiorazione solo dall'alto e solo su intervalli basta per due ragioni.
- I coefficienti sono positivi. In uno zero comune a più funzioni L i residui della trasformata si sommano con pesi positivi, quindi nulla si cancella. In un polo reale il residuo è positivo.
- La derivazione ripetuta concentra l'integrale. In coordinate logaritmiche la trasformata diventa una Laplace F(s) = ∫ g(u)e^{−su} du. Derivando k volte in un punto reale σ, con k proporzionale a log Y, il nucleo u^k e^{−σu}/k! è una densità gamma concentrata sull'intervallo dove vale la stima. Fuori basta la stima banale |g(u)| ≪ e^{2u}.

Combinando |F^{(k)}(σ+it)| con (−1)^k F^{(k)}(σ) interviene solo la parte positiva di g. Un polo con parte reale > ϑ, scelto come unico polo più vicino al centro, forza una crescita incompatibile con la stima. Zhang indica Landau e il metodo di Turán come precedenti. L'equazione funzionale tratta la metà sinistra della striscia.

**Secondo passo: caratteri e Frobenius.** Si lavora in un campo CM abeliano E che contiene il campo di ψ. L'ortogonalità dei caratteri trasforma una somma manifestamente non negativa,

A(a,t,w) = Σ_p log p Σ_j (peso)·(a/p^j − w)_+,

ristretta ai p^j con Frobenius in una classe prescritta, in una combinazione di valori G_χ(a/w). A questa si aggiunge un termine principale esplicito:

M(a,w) = a(log a − 1 − γ + L′/L(1,κ) − media dei log w).

Compaiono solo derivate logaritmiche in s = 1, dunque non serve nessuna informazione sugli zeri. I pesi w si scelgono su due scale:
- su un insieme selezionato T₂ di posti complessi, a/w ≈ x;
- altrove a/w ≫ exp(x^{ε/3}), e lì bastano le regioni libere da zeri.

Una media su un sottogruppo del gruppo di Galois isola i caratteri che compongono 𝒢_ψ. Resta da maggiorare l'eccesso A − M.

**Terzo passo, il cuore: divisibilità di periodi automorfi.** L'idea guida è la formula del prodotto: un intero algebrico non nullo molto divisibile ai primi finiti non può essere piccolo a tutti i posti archimedei.

I periodi usati sono periodi di Bessel, alla Gan–Gross–Prasad, tra forme cuspidali su gruppi unitari U(X₀) ⊂ U(Y₀) definiti su E⁺, con X₀ totalmente definito. Sono normalizzati in modo da prendere valori in un campo di numeri K. Le loro valutazioni finite sono minorate da somme che riproducono esattamente i termini (a_t/p^ν − w)_+, con ν dispari e la condizione di Frobenius.

Per avere abbastanza divisibilità si itera la corrispondenza theta di Weil–Howe, con m sollevamenti su ciascun lato:
- dal lato X, U(X₀) → … → U(X_m), tutti gruppi totalmente definiti;
- dal lato Y, gruppi U(Y_j) la cui segnatura cambia finché U(Y_m) diventa definito.

Ogni sollevamento aggiunge alla parte archimedea un blocco di parametri di Harish-Chandra centrato in −w_{j,ρ}: è così che i pesi w entrano nell'aritmetica. Le identità seesaw di Kudla portano il periodo iniziale, attraverso periodi di Fourier–Jacobi intermedi, a un periodo di restrizione finale U(Y_m) ⊂ U(X_m). I contributi favorevoli si sommano sugli m sollevamenti e producono un fattore m.

Alpöge propone un'analogia, da prendere come tale. Nel metodo di Stepanov per le curve sui campi finiti, un polinomio ausiliario si annulla con molteplicità alta nei punti. Sugli interi la molteplicità è difficile da trovare: sarebbe come "derivare i numeri interi". Qui ogni sollevamento theta ne fa le veci, e m gioca il ruolo dell'ordine di annullamento.

Il lato archimedeo è il più pesante e si articola in tre parti.
- **Norme.** Le norme di Petersson dei sollevamenti sono controllate dalla formula di Rallis (nella versione di Gan–Qiu–Takeda). Su un autospazio di Hecke vale Θ_μΘ_μ* = κ₀ Π_j L^S((h+1)/2, B⊗μ_j^{−1}).
- **Pendenze.** Si costruiscono reticoli interi di forme automorfe algebriche, alla Gross, e mappe di periodo intere b_α: N_α → C. Poi si minora la pendenza media di C usando la disuguaglianza di Bost e la filtrazione di Harder–Narasimhan per reticoli (Stuhler, Grayson). Serve anche un lemma di algebra lineare: le immagini dei periodi coprono quasi tutto lo spazio duale anche dopo aver ristretto i domini. Zhang lo accosta, per analogia, ai tight frame finiti.
- **Covolumi.** I covolumi dei reticoli iniziali vengono dalla geometria di Arakelov sugli schemi di moduli unitari: Hilbert–Samuel aritmetico (Gillet–Soulé, Zhang), sezioni piccole (Yuan, Moriwaki), confronti di altezze. Le strutture intere sono controllate con le stime di Fargues sulle mappe di Hodge–Tate e con la teoria di Dieudonné prismatica di Anschütz–Le Bras.

Il punto delicato è che le costanti devono riprodurre *esattamente* il termine principale M. Succede perché la normalizzazione usa periodi di varietà abeliane CM, che Chowla–Selberg e Anderson legano a derivate logaritmiche di funzioni L di Dirichlet. Insieme alle formule di dimensione di Weyl e di massa di Siegel, questo dà l'identità esplicita D_div − A·L_w = M_tot. La reciprocità di Shimura–Taniyama e l'integralità di Deligne–Ribet controllano i fattori algebrici ai posti finiti.

**Quarto passo: denominatori e coomologia di Galois.** Proiettare su autospazi di Hecke può introdurre denominatori nei reticoli, e questi mangerebbero la divisibilità. Le congruenze tra autovalori si misurano con le rappresentazioni di Galois associate (Clozel–Harris–Labesse, Shin, Chenevier–Harris). Il costo si riduce agli ordini di gruppi di tipo Tate–Shafarevich S_ℓ(E,j) ⊂ H¹(G_{E,S_ℓ}, Q_ℓ/Z_ℓ(−j)).

Tramite la dualità di Poitou–Tate si separano i due autospazi della coniugazione complessa:
- un autospazio si controlla con numeri di Bernoulli generalizzati, elementi di Stickelberger e derivate di Kolyvagin;
- l'altro con teoria delle deformazioni, congruenze su U(3) e GSp₄, sollevamento di automorfia (Wiles, Taylor–Wiles, Clozel–Harris–Taylor) e l'annullamento dei Selmer di Bloch–Kato via il sistema di Eulero di Kato.

Il campo E varia in torri ciclotomiche, usando la teoria di Iwasawa e l'annullamento dell'invariante μ (Ferrero–Washington). Per pochi twist "eccezionali" è disponibile solo una stima grossolana, valida quando j è piccolo rispetto a x. Un argomento di piccionaia sceglie allora intervalli che evitano le scale critiche. È questa la ragione per cui la stima finale vale solo su intervalli. Alpöge dice che qui ha dovuto ottenere una forma significativamente indebolita della congettura di Vandiver, e crede che ne segua l'annullamento di vari K-gruppi di Z.

C'è anche un ingrediente combinatorio. I posti di T₂ devono essere molti, ma non devono affollarsi in brevi segmenti di orbite di Frobenius. Per questo si usa una variante della costruzione di Behrend di insiemi privi di progressioni aritmetiche di tre termini. Alpöge la considera intuitivamente superflua.

**Quinto passo: l'esponente 1/2.** Messi insieme i pezzi, i due errori principali hanno dimensioni x/m e m, a meno di fattori x^{O(ε)} con costante indipendente da ε. Scegliendo m ≈ √x entrambi diventano ≈ √x, e si ottiene 𝒢_ψ(x) ≤ x^{1/2+η}. È la riga che Alpöge cita: per una somma di von Mangoldt di lunghezza X, la lunghezza della catena di sollevamenti theta suggerita da Claude era √X. "E del resto, che altro potrebbe essere?"

Lo schema globale è concettualmente lineare: una stima unilaterale a coefficienti positivi, poi il confronto tra valutazioni finite e norme archimedee di periodi algebrici. Il costo enorme sta nel rendere tutto uniforme rispetto a campi, pesi e livelli che crescono con x. Le fonti non dicono ancora quali parti siano davvero essenziali, e Alpöge scrive di aver forse introdotto molte scelte subottimali.

### claude_full-L4-s07

*nota intera, spiegazione 8 di 8.* Fatti del livello: 23 sì, 4 in parte, 3 no (copertura 0,83) · errori 0 su 80 · analogie dichiarate 0 · segnalazioni del critico 1, errori introdotti 0 · 1513 parole (limite 1500) · Gulpease 55,9

Che cosa si afferma? Per ogni carattere di Dirichlet primitivo χ, tutti gli zeri di L(s, χ) nella striscia 0 < Re(s) < 1 stanno sulla retta Re(s) = 1/2. Il caso dei caratteri non primitivi segue subito, e il caso di conduttore 1 è l'ipotesi di Riemann classica. Alpöge, che ha sviluppato l'argomento con Claude, ha pubblicato soltanto la formalizzazione in Lean, circa 17 milioni di righe. Ha scelto di non diffondere un'esposizione generata dall'IA di oltre 250.000 pagine. Quello che segue ricostruisce la struttura dalla nota preliminare di Robin Zhang (21 novembre 2026). Zhang stesso avverte che gran parte del suo testo dalla Sezione 2 in poi è stata scritta da un'IA (GPT 6 Pro) leggendo il codice Lean, e che non può garantire che sia una traduzione fedele. Riferisce però che le comunità Lean e Mathlib hanno verificato la dimostrazione con implementazioni indipendenti del kernel, e che le definizioni in Lean coincidono con quelle matematiche standard.

**La riduzione analitica.** Il punto di partenza è la media di Riesz del primo ordine

S_χ(x) = Σ_{n≤x} Λ(n)χ(n)(x/n − 1),

la cui trasformata di Mellin è −L′(s,χ)/(s(s−1)L(s,χ)). Si corregge il polo in s = 1. Per χ non principale si pone G_χ(x) = S_χ(x) + x·L′(1,χ)/L(1,χ). Per ζ si pone G_1(x) = S_1(x) − x log x + (1+γ)x. Fissato ψ primitivo di ordine r, si forma una combinazione a coefficienti positivi:

𝒢_ψ = G_1 + (3r+1)⁻¹ Σ Re G_χ,

dove la somma corre sui caratteri primitivi che inducono le potenze di ψ. La positività serve a questo: in uno zero comune a più funzioni L, il residuo della trasformata è ν_ρ/(ρ(1−ρ)) con ν_ρ > 0, quindi gli zeri non possono cancellarsi tra loro.

L'obiettivo analitico (Proposizione 1.2) è più debole di una stima puntuale. Per ogni η > 0 esistono Y arbitrariamente grandi tali che 𝒢_ψ(x) ≤ x^{1/2+η} su tutto [Y, Y^{3/2}]. La stima è solo dall'alto, e vale solo su intervalli. Per mostrare che basta, si scrive la trasformata in coordinate logaritmiche come trasformata di Laplace F(s) e la si deriva k volte in un punto reale σ, con k ≍ log Y. Dopo divisione per k!, il peso u^k e^{−σu}/k! è una densità gamma concentrata sull'intervallo buono (Lemma 2.2). Fuori dall'intervallo basta la stima banale |g(u)| ≪ e^{2u}. Dentro l'intervallo, combinando |F^{(k)}(σ+it)| con (−1)^k F^{(k)}(σ), si usa solo la parte positiva di g. Un polo con parte reale > ϑ, scelto come polo più vicino al centro con un argomento alla Turán, forza una crescita incompatibile. L'equazione funzionale sistema poi la metà sinistra della striscia. Questa parte è classica nello spirito (Landau, Guinand–Weil, Turán) e non usa RH.

**Dai primi alla divisibilità di periodi.** L'idea centrale viene dalla formula del prodotto. Un intero algebrico non nullo molto divisibile ai primi finiti non può essere piccolo a tutti i posti archimedei. Le somme sulle potenze di primi compaiono come minoranti delle valutazioni di periodi automorfi normalizzati P_α(f, g), che sono numeri in un campo K. Una maggiorazione archimedea di questi periodi limita quindi le somme sui primi.

Il collegamento passa per l'ortogonalità dei caratteri (Proposizione 3.1). In un gruppo abeliano Γ = Gal(E/ℚ) si considera la quantità

A(a, t, w) = Σ_p log p Σ_j (2/|I_p|) Σ (a/p^j − w_{ρ_t(g)})_+,

dove la somma interna corre sui g con g − jF_p ∈ I_p. È manifestamente ≥ 0, e differisce da una combinazione esplicita dei G_χ(a/w) per un termine principale

M(a, w) = a(log a − 1 − γ + ℓ_κ − f⁻¹ Σ log w_ρ).

L'identità usa solo L′/L in s = 1, dove la non nullità è nota. Mediando su un sottogruppo H_0 e scegliendo i parametri w su due scale si isolano i caratteri che compongono 𝒢_ψ con argomenti vicini a x. Sui posti "lontani" gli argomenti sono enormi e bastano le regioni senza zeri note.

**Il motore: lift theta iterati.** Si fissa un campo CM abeliano E che contiene il campo di ψ e si lavora con gruppi unitari su E⁺. Il periodo iniziale è un periodo di Bessel alla Gan–Gross–Prasad per U(X_0) ⊂ U(Y_0), con X_0 totalmente definito. Si applicano poi m lift theta (Weil–Howe) a entrambi gli argomenti. Le identità seesaw di Kudla trasportano il periodo, alternando periodi di Bessel e di Fourier–Jacobi, fino a un semplice accoppiamento di restrizione U(Y_m) ⊂ U(X_m). Ogni lift aggiunge un blocco di parametri di Harish-Chandra centrato in −w_{j,ρ}, e i contributi favorevoli alle valutazioni si sommano sugli m lift.

Alpöge propone un'analogia, che va presa come tale: il metodo di Stepanov per le curve su campi finiti usa un polinomio ausiliario che si annulla con alta molteplicità. Sugli interi la molteplicità sarebbe "come derivare i numeri interi", e la catena di lift theta ne fa le veci: m gioca il ruolo dell'ordine di annullamento. Racconta anche che fu Claude a suggerire una catena di lunghezza √X.

**Il lato archimedeo: geometria di Arakelov.** Si lavora con reticoli di forme automorfe algebriche alla Gross, costruiti da moduli di Weyl interi. Si costruiscono un sottoreticolo M′_α e un ideale frazionario 𝔞_α con P_α(M′_α, M_W) ⊆ 𝔞_α. Riscalando si ottengono mappe intere b_α: N_α → C = Hom(M_W, O_K), e da queste si deduce una minorazione della pendenza media di C. Gli strumenti sono quattro:

1. **Disuguaglianza delle pendenze di Bost**, che controlla quanto scende la pendenza minima sotto una mappa di norma limitata.
2. **Filtrazione di Harder–Narasimhan** (Stuhler, Grayson), per tenere solo le parti di pendenza alta.
3. **Un lemma di algebra lineare** (Lemma 4.2) che garantisce che le immagini, quasi un "tight frame" secondo l'analogia della nota, ricoprano quasi tutto W^∨ anche dopo le restrizioni.
4. **Maggiorazioni dei covolumi** dei reticoli di partenza, ottenute dal teorema di Hilbert–Samuel aritmetico (Gillet–Soulé, Zhang, con l'estensione di Moriwaki e le idee di Yuan per fibrati solo nef) su compattificazioni aritmetiche dei moduli unitari (Faltings–Chai). I contributi finiti delle altezze sono controllati con le stime di Fargues sulle mappe di Hodge–Tate e con la teoria di Dieudonné prismatica di Anschütz–Le Bras.

Le norme dei lift si calcolano con la formula del prodotto interno di Rallis (Gan–Qiu–Takeda). Θ_μΘ_μ* agisce sugli autospazi di Hecke come κ_0 ∏_j L^S((h+1)/2, B ⊗ μ_j⁻¹).

Il punto più delicato è che le costanti tornino esattamente, perché M(a, w) è già stato sottratto. Il ponte è la relazione classica tra periodi di varietà abeliane CM e derivate logaritmiche di funzioni L di Dirichlet (Chowla–Selberg, Anderson). A questa si aggiungono la reciprocità di Shimura–Taniyama e l'integralità di Deligne–Ribet per i fattori algebrici, e le formule di Weyl e di massa di Siegel per dimensioni e molteplicità. L'identità D_div − A·L_w = M_tot (eq. 4.5) mostra che valutazioni finite e norme archimedee ricostruiscono esattamente il termine principale. Resta una stima d'errore esplicita (eq. 4.11).

**I denominatori: coomologia di Galois.** Proiettare sugli autospazi di Hecke può introdurre denominatori che mangiano la divisibilità, e questi sono misurati dalle congruenze tra autosistemi. Tramite le rappresentazioni di Galois attaccate (Clozel–Harris–Labesse, Shin, Chenevier–Harris), il problema si riduce a limitare gruppi di Tate–Shafarevich 𝒮_ℓ(E, j) a coefficienti ℚ_ℓ/ℤ_ℓ(−j), uniformemente in ℓ, j ed E. Le due parti si trattano diversamente:

- **Parte "−"**: si usano numeri di Bernoulli generalizzati, elementi di Stickelberger e derivate di Kolyvagin.
- **Parte "+"**: si usano deformazioni e sollevamento di automorfia su U(3) e GSp₄ (Wiles, Taylor–Wiles, Clozel–Harris–Taylor), con l'annullamento di Selmer di Bloch–Kato tramite il sistema di Eulero di Kato.

Si fa poi variare E lungo torri ciclotomiche usando μ = 0 (Ferrero–Washington). Per alcuni twist "eccezionali" c'è solo una stima grossolana, valida quando j è piccolo rispetto a x. È qui che serve la libertà di scegliere l'intervallo [Y, Y²] (Lemma 5.5), ed è uno dei motivi per cui l'enunciato analitico vale solo su intervalli. Alpöge descrive questa parte come la conquista di "un indebolimento significativo di Vandiver". In nota aggiunge una sua convinzione, non dimostrata nelle fonti: ne seguirebbe l'annullamento di vari K-gruppi di ℤ.

**Scelte combinatorie e l'esponente 1/2.** L'insieme T_2 dei posti complessi scelti deve essere grande, ma deve incontrare in pochi punti i segmenti corti delle orbite di Frobenius. Si ottiene adattando la costruzione di Behrend di insiemi senza progressioni aritmetiche di tre termini: ogni segmento rilevante contiene al più due posti.

Alla fine i due errori principali hanno dimensioni x/m e m, a meno di potenze x^{O(ε)}. Scegliere m ≍ √x li bilancia e dà 𝒢_ψ(x) ≤ x^{1/2+(C+4)ε}, con C fissato prima di ε. L'esponente 1/2 nasce quindi da un bilanciamento, non da una simmetria imposta.

**Cautele.** Alpöge dichiara di non padroneggiare ancora l'intorno matematico dell'argomento, in particolare le forme automorfe su gruppi di rango alto. Scrive di aver forse incorporato scelte subottimali e si aspetta semplificazioni rapide; ritiene per esempio "ovviamente non necessario" il trucco di Behrend. La sua cronologia parafrasa un riassunto di Claude che, dice lui stesso, "potrebbe non avere senso". La garanzia di correttezza poggia dunque sulla verifica Lean riportata, non sulle esposizioni in linguaggio naturale. Zhang segnala infine che lo stesso giorno è stata annunciata una dimostrazione indipendente di GRH, interamente umana, di Alessandro Masullo. Le fonti non dicono nulla sui suoi contenuti.

### claude_overview-L4-s00

*panoramica, spiegazione 1 di 8.* Fatti del livello: 16 sì, 8 in parte, 6 no (copertura 0,67) · errori 2 su 58 · analogie dichiarate 0 · segnalazioni del critico 2, errori introdotti 0 · 1512 parole (limite 1500) · Gulpease 54,5

Il risultato annunciato da Levent Alpöge il 20 novembre 2026 è l'ipotesi di Riemann generalizzata per le funzioni L di Dirichlet. Nella forma della nota preliminare di Robin Zhang, l'enunciato è questo: per ogni carattere di Dirichlet primitivo χ, ogni zero di L(s, χ) nella striscia 0 < Re(s) < 1 sta sulla retta Re(s) = 1/2. Il carattere principale dà ζ, quindi l'ipotesi di Riemann classica è inclusa. Alpöge scrive di aver trovato la dimostrazione lavorando con Claude e che entrambi l'hanno formalizzata in Lean «senza assunzioni». Per ora l'unico testo pubblicato è il codice Lean: un documento leggibile non c'è. Alpöge aggiunge di non padroneggiare ancora una parte ampia della matematica coinvolta e si aspetta semplificazioni rapide. Zhang parla di «proposed proof» e presenta la sua sintesi come un tentativo. Le fonti non riferiscono altre verifiche indipendenti, quindi quello che segue descrive l'architettura dell'argomento proposto.

**La riduzione analitica.** Il punto di partenza è classico. Si usa la media di Riesz del primo ordine

Sχ(x) = Σ_{n≤x} Λ(n)χ(n)(x/n − 1),

scelta perché la sua trasformata di Mellin è particolarmente semplice: ∫₁^∞ Sχ(x)x^{−s−1}dx = −L′(s,χ)/(s(s−1)L(s,χ)) per Re(s) > 1. Uno zero nella striscia critica diventa un polo, quindi una crescita controllata di Sχ esclude zeri.

Per eliminare il possibile polo in s = 1 si corregge il termine principale. Per χ non principale si pone Gχ(x) = Sχ(x) + xL′(1,χ)/L(1,χ). Per ζ si pone

G₁(x) = Σ_{n≤x} Λ(n)(x/n − 1) − x log x + (1+γ)x.

Poi, per ψ primitivo di ordine r, si prende la combinazione positiva

Gψ = G₁ + (3r+1)⁻¹ Σ Re(Gχ),

dove la somma corre sui caratteri primitivi χ ≠ 1 che inducono le potenze di ψ. Le potenze compaiono tutte perché l'ortogonalità dei caratteri serve a imporre condizioni sui Frobenius. Poiché l'insieme di questi caratteri è chiuso per coniugio, il residuo in uno zero ρ è 1/(ρ(1−ρ)) per una somma di molteplicità con pesi positivi. Quindi ρ resta un polo anche se più funzioni L si annullano lì: niente cancellazioni.

Il cuore quantitativo è la Proposizione 1.2. Per ogni η > 0 e ogni A ≥ 2 esiste Y ≥ A tale che

Gψ(x) ≤ x^{1/2+η} per ogni x ∈ [Y, Y^{3/2}].

La stima è solo dall'alto e vale solo su intervalli arbitrariamente lontani. Zhang rinvia alla sua Sezione 2, che si appoggia a Landau, Guinand, Turán e Weil, per spiegare perché questo basta a escludere zeri fuori dalla retta critica. Il dettaglio di quel passaggio non è nell'estratto che ho, quindi non lo ricostruisco.

**Il principio: divisibilità contro grandezza.** Tutta la parte nuova serve a dimostrare la Proposizione 1.2, e poggia sulla formula del prodotto: un intero algebrico non nullo molto divisibile ai primi finiti non può essere piccolo a tutti i posti archimedei.

Alpöge colloca l'idea in una genealogia precisa. Il metodo di Stepanov per l'ipotesi di Riemann sui campi di funzioni usa un divisore ausiliario con molteplicità. Sugli interi la molteplicità è difficile da trovare: corrisponderebbe, dice lui, a «derivare i numeri interi». Il suo surrogato sono le catene di theta lift, dove ogni lift imita un ordine di molteplicità. È un'analogia di Alpöge stesso, non un enunciato formale. In questo quadro le somme sui primi compaiono come minoranti delle valutazioni di periodi automorfi normalizzati, mentre la geometria aritmetica fornisce maggioranti per le loro grandezze archimedee.

**Periodi e theta lift.** Si fissa un campo CM abeliano E che contiene il campo tagliato da ψ, e si lavora con gruppi unitari U(V) sul sottocampo totalmente reale massimale E₊. Il periodo iniziale è un periodo di Bessel alla Gan–Gross–Prasad tra forme cuspidali f su U(X₀) e g su U(Y₀), con X₀ ⊂ Y₀ e X₀ totalmente definito. Il periodo è normalizzato in modo da dare un accoppiamento K-bilineare su un campo di numeri K.

Si applica poi m volte la corrispondenza theta di Weil–Howe a entrambi gli argomenti. Gli Xⱼ restano totalmente definiti, mentre le segnature degli Yⱼ variano finché anche Y_m è totalmente definito. Le identità seesaw di Kudla legano il periodo di Bessel iniziale all'accoppiamento finale di restrizione U(Y_m) ⊂ U(X_m). Ogni lift aggiunge termini al minorante delle valutazioni finite.

Il prezzo è tenere sotto controllo tre cose:
- le norme di Petersson dei lift, tramite le formule di Rallis e di Gan–Qiu–Takeda;
- le dimensioni e le molteplicità, tramite la formula di Weyl e conteggi pesati di reticoli hermitiani alla Siegel;
- le costanti di normalizzazione, che usano periodi di varietà abeliane CM, legati da Chowla–Selberg e Anderson alle derivate logaritmiche delle funzioni L di Dirichlet.

Le costanti contano davvero, perché in Gχ il termine principale è già stato sottratto. È proprio da questi periodi CM che l'argomento ricostruisce il termine principale (Proposizione 3.1).

**Reticoli e pendenze.** Il confronto tra posti finiti e archimedei avviene nel linguaggio di Arakelov. Per ogni peso massimo α c'è un O_K-reticolo M_α di forme automorfe algebriche alla Gross su U(X₀). Dall'altro lato, i lift discendenti da U(Y_m) danno un reticolo M_W in uno spazio di forme test W.

«Divisibilità» ha qui un senso esatto. Si costruiscono un sottoreticolo M′_α di indice finito e un ideale frazionario a_α tali che P_α(M′_α, M_W) ⊆ a_α. Riscalando a N_α = a_α⁻¹M′_α si ottengono mappe intere b_α: N_α → C = Hom(M_W, O_K). Le loro norme minorano la pendenza media μ(C).

Servono però due ingredienti in più. Il primo sono i covolumi degli M_α. Per stimarli si vedono le forme automorfe come sezioni di fibrati su uno spazio di moduli di varietà abeliane principalmente polarizzate con azione di O_E. Si usano:
- le compattificazioni aritmetiche di Faltings–Chai;
- la formula di Hilbert–Samuel aritmetica di Gillet–Soulé e Zhang;
- i minimi successivi di Zhang e il criterio di Moriwaki;
- ai primi finiti, le stime di Fargues sulle mappe di Hodge–Tate e la teoria di Dieudonné prismatica di Anschütz–Le Bras.

Il secondo ingrediente serve a evitare che le immagini dei b_α giacciano tutte in una direzione. Bisogna mostrare che i funzionali periodo generano quasi tutto W^∨, anche dopo aver tolto piccole parti dei domini. A questo servono la filtrazione di Harder–Narasimhan per reticoli hermitiani (Stuhler, Grayson), la disuguaglianza delle pendenze di Bost e il Lemma 4.2, che stima la codimensione. Il risultato è la Proposizione 4.3.

**Scelta dei posti complessi.** Le condizioni di Frobenius, tradotte con l'ortogonalità dei caratteri, producono termini Gχ(a_t/w_{j,ρ}). Qui ρ è un posto complesso di E, e gli interi w_{j,ρ} fissano i blocchi di parametri di Harish-Chandra aggiunti dal j-esimo lift. Scegliendo i w_{j,ρ} e mediando su sottogruppi di Gal(E/Q) si recupera Gψ(x).

L'insieme T₂ dei posti usati deve essere grande. Però si perde precisione se troppi suoi posti cadono in un segmento corto di un'orbita di Frobenius. Per conciliare le due richieste si adatta la costruzione di Behrend di insiemi grandi senza progressioni aritmetiche di tre termini, così che ogni intersezione rilevante contenga al più due posti. Gli altri posti si trattano con regioni libere da zeri. Alpöge stesso ritiene questo trucco quasi certamente non necessario.

**Denominatori di Hecke e coomologia di Galois.** Per applicare le formule delle norme bisogna proiettare sugli autospazi di Hecke. Queste proiezioni possono introdurre denominatori che mangiano la divisibilità guadagnata. I denominatori si controllano studiando le congruenze tra autovalori di Hecke attraverso rappresentazioni di Galois: cambio di base a GL_n su E, poi i risultati di Clozel–Harris–Labesse, Shin e Chenevier–Harris.

Gli addendi unidimensionali prodotti dai lift danno gruppi Sℓ(E, j). Sono nuclei di restrizione in H¹ non ramificata fuori da ℓ, verso i completamenti di E sopra ℓ, a coefficienti in Qℓ/Zℓ(−j). Per stimarli si usano:
- la dualità di Tate–Poitou;
- argomenti di deformazione alla Wiles, Taylor–Wiles e Clozel–Harris–Taylor;
- l'Euler system di Kato, per l'annullamento di certi gruppi di Selmer di rappresentazioni modulari bidimensionali;
- la teoria di Iwasawa lungo torri ciclotomiche, con l'annullamento dell'invariante μ di Ferrero–Washington.

Qui entra la libertà nella scelta dell'intervallo [Y, Y^{3/2}]: lo si sceglie in modo che gli indici «eccezionali» siano piccoli rispetto a x. Alpöge descrive questa parte come la conquista di un «indebolimento significativo di Vandiver», e aggiunge che è comunque un'affermazione forte.

**Perché proprio 1/2.** Dopo aver combinato tutto, i due errori principali nella stima di Gψ(x) hanno taglia x/m e m, a meno di fattori arbitrariamente piccoli in potenze di x. Bilanciarli impone m ≍ √x, e l'esponente 1/2 nasce da qui (Lemma 6.1). Alpöge racconta che fu proprio Claude a suggerire che la lunghezza della catena di theta lift dovesse essere √X. I campi di numeri, i pesi e i posti complessi vanno poi scelti insieme a m (Proposizione 6.3).

In sintesi, l'architettura proposta ha due livelli. Il livello analitico è classico: una media di Riesz, una combinazione positiva sui caratteri, una stima unilaterale su intervalli lontani. Il motore è nuovo: un argomento alla Stepanov in cui la molteplicità è sostituita da √x lift theta iterati, con la formula del prodotto a fare da ponte. Il controllo delle costanti mobilita CM, Arakelov, teoria di Hodge p-adica e deformazioni di Galois. Quanto alla verifica, oggi esiste soltanto la formalizzazione dichiarata da Alpöge, insieme a una lettura umana ancora dichiaratamente preliminare.

### claude_overview-L4-s01

*panoramica, spiegazione 2 di 8.* Fatti del livello: 16 sì, 10 in parte, 4 no (copertura 0,70) · errori 1 su 64 · analogie dichiarate 0 · segnalazioni del critico 1, errori introdotti 0 · 1545 parole (limite 1500) · Gulpease 53,4

Il risultato annunciato da Levent Alpöge il 20 novembre 2026 è l'ipotesi di Riemann generalizzata per le funzioni L di Dirichlet: per ogni carattere di Dirichlet primitivo χ, ogni zero di L(s, χ) nella striscia 0 < Re(s) < 1 sta sulla retta Re(s) = 1/2. Il carattere principale, di conduttore 1, è incluso e dà ζ(s), quindi il risultato contiene l'ipotesi di Riemann classica. Alpöge scrive di aver trovato la dimostrazione lavorando con Claude e che l'argomento è stato formalizzato in Lean «senza assunzioni». Per ora esiste solo la formalizzazione: non c'è ancora un testo leggibile. Alpöge ha scelto di non diffondere un documento generato automaticamente che supera le 250.000 pagine, ammette di non padroneggiare ancora gran parte della matematica coinvolta e si aspetta semplificazioni importanti. La ricostruzione che segue si basa soprattutto sulla «nota preliminare» di Robin Zhang, che parla di «proposed proof» e presenta il proprio riassunto come un tentativo.

Il primo passo è una riduzione classica. Si considera la media di Riesz del primo ordine

S_χ(x) = Σ_{n≤x} Λ(n)χ(n)(x/n − 1),

la cui trasformata di Mellin, ∫_1^∞ S_χ(x) x^{−s−1} dx, vale −L′(s, χ)/(s(s−1)L(s, χ)) per Re(s) > 1. Uno zero nella striscia critica produce quindi un polo, e una maggiorazione su S_χ vincola la posizione degli zeri. Per eliminare il polo eventuale in s = 1 si corregge il termine principale. Per χ non principale si pone G_χ(x) = S_χ(x) + x L′(1, χ)/L(1, χ). Per ζ si pone G_1(x) = Σ_{n≤x} Λ(n)(x/n − 1) − x log x + (1 + γ)x.

Non si lavora però con un carattere alla volta. Dato ψ primitivo di ordine r, si somma G_1 con (1/(3r+1)) Σ Re(G_χ), dove la somma corre sui caratteri primitivi χ ≠ 1 che inducono le potenze di ψ. Si ottiene così una funzione G_ψ. Poiché l'insieme di questi caratteri è chiuso per coniugazione, il residuo in uno zero ρ è 1/(ρ(1−ρ)) per una somma di molteplicità con pesi positivi. Gli zeri di funzioni L diverse quindi non possono cancellarsi tra loro. La ragione per includere tutte le potenze di ψ è l'ortogonalità dei caratteri, che serve più avanti per imporre condizioni sui Frobenius.

Il cuore del lavoro è la Proposizione 1.2: per ogni η > 0 e ogni A ≥ 2 esiste Y ≥ A tale che G_ψ(x) ≤ x^{1/2+η} per ogni x in [Y, Y^{3/2}]. La stima è unilaterale e vale solo su intervalli arbitrariamente lontani, non per ogni x grande. La Sezione 2 di Zhang spiega perché basta comunque a escludere zeri fuori dalla retta critica, con riferimenti a Landau, Guinand, Turán e Weil. Le fonti non riportano i dettagli di questo passaggio. Nella cronologia di Alpöge compaiono soltanto accenni: «Guinand–Weil had the sign», un trucco con una funzione test di varianza, la domanda su come applicare Turán.

Per dimostrare la Proposizione 1.2, l'idea guida è la formula del prodotto. Un intero algebrico non nullo molto divisibile ai primi finiti non può essere piccolo a tutti i posti archimedei. Le somme sui primi compaiono nelle minorazioni delle valutazioni di certi periodi automorfi, normalizzati in modo da assumere valori in un campo di numeri K. Una maggiorazione archimedea di questi periodi vincola quindi le somme, e la difficoltà è farlo con un errore vicino a √x. Alpöge colloca l'argomento nella discendenza del metodo di Stepanov per l'ipotesi di Riemann sui campi di funzioni, dove si usa un divisore con molteplicità. Sugli interi la molteplicità è difficile da ottenere: sarebbe come «derivare i numeri interi». Per analogia, nel nuovo argomento la divisibilità dei periodi fa la parte della molteplicità, e ogni sollevamento theta ne aggiunge un po'.

Ecco la costruzione, per come la descrive Zhang. Si fissa un campo CM abeliano E che contiene il campo tagliato da ψ, e si considerano gruppi unitari su E⁺, il suo sottocampo totalmente reale massimale. Il periodo iniziale è un periodo di Bessel alla Gan–Gross–Prasad. Accoppia forme cuspidali f su [U(X_0)] e g su [U(Y_0)], con X_0 ⊂ Y_0 e X_0 totalmente definito: si prende un coefficiente di Fourier di g lungo un sottogruppo unipotente e lo si accoppia con f ristretta. Si applica poi m volte la corrispondenza theta di Weil e Howe su entrambi gli argomenti, con catene U(X_j) e U(Y_j) per 0 ≤ j ≤ m. Tutti gli X_j sono totalmente definiti, e le segnature degli Y_j variano finché anche Y_m lo diventa. Le identità seesaw di Kudla collegano il periodo di Bessel iniziale agli accoppiamenti dopo i sollevamenti, attraverso periodi di Fourier–Jacobi, fino a un accoppiamento di restrizione per U(Y_m) ⊂ U(X_m). Ogni sollevamento contribuisce alle minorazioni delle valutazioni finite. Queste minorazioni coinvolgono potenze di primi razionali soggette a condizioni di Frobenius, e l'ortogonalità dei caratteri le trasforma in termini del tipo G_χ(a_t/w_{j,ρ}) (Proposizione 3.1).

I sollevamenti cambiano le norme di Petersson e le dimensioni degli spazi, e le costanti contano perché nei G_χ il termine principale è già stato sottratto. Per le norme si usano le formule di Rallis e di Gan–Qiu–Takeda, che esprimono la norma di un sollevamento theta tramite valori speciali di funzioni L e integrali locali. Per le dimensioni si usano la formula di Weyl e conteggi pesati di reticoli hermitiani alla Siegel. La normalizzazione usa periodi di varietà abeliane CM, che Chowla–Selberg e Anderson legano alle derivate logaritmiche delle L di Dirichlet. Così il termine principale viene ricostruito esattamente (identità della Sezione 4.5), ed è questo il punto in cui riappare L′(1, χ)/L(1, χ).

Il lato archimedeo è geometria di Arakelov. Si considerano reticoli M_α su O_K di forme automorfe algebriche alla Gross su U(X_0), indicizzati dai pesi massimi α, e un reticolo M_W in uno spazio W di forme test su U(Y_0), ottenuto con sollevamenti theta discendenti. La «divisibilità» ha un significato preciso: esistono un sottoreticolo di indice finito M′_α e un ideale frazionario a_α tali che P_α(M′_α, M_W) ⊆ a_α. Riscalando si ottengono mappe intere b_α da N_α = a_α^{−1} M′_α verso C = Hom(M_W, O_K), e con queste si minora la pendenza media di C.

Servono allora maggiorazioni dei covolumi dei domini. Per ottenerle si vedono le forme olomorfe come sezioni di fibrati su compattificazioni aritmetiche alla Faltings–Chai di spazi di moduli di varietà abeliane con azione di O_E. Si usano poi:
- le formule di Hilbert–Samuel aritmetiche di Gillet–Soulé e di Zhang;
- le disuguaglianze di Zhang sui minimi successivi e il criterio di Moriwaki;
- ai primi finiti, le stime di Fargues sulle mappe di Hodge–Tate e la teoria di Dieudonné prismatica di Anschütz–Le Bras.

Le norme da sole non bastano, perché le immagini potrebbero concentrarsi in poche direzioni di W^∨. Bisogna mostrare che i funzionali periodo generano quasi tutto W^∨, anche dopo piccole restrizioni dei domini. Le restrizioni vengono dalla filtrazione di Harder–Narasimhan per reticoli hermitiani (Stuhler, Grayson), e la disuguaglianza delle pendenze di Bost controlla le immagini (Lemma 4.2 e Proposizione 4.3).

Restano tre ingredienti tecnici.

Il primo è la scelta di Behrend. Ogni sollevamento aggiunge un blocco di parametri di Harish-Chandra centrato in −w_{j,ρ} ai posti complessi ρ di E. L'insieme di posti T_2 su cui si fa questa scelta deve essere grande, ma le stime peggiorano se troppi suoi posti cadono in un breve segmento di un'orbita di Frobenius. Un adattamento della costruzione di Behrend di insiemi senza progressioni aritmetiche di tre termini limita ogni intersezione a due posti. Ai posti rimanenti si usano regioni libere da zeri. Alpöge ritiene che questo trucco sia quasi certamente superfluo.

Il secondo sono i denominatori di Hecke. Proiettare su autospazi di Hecke può introdurre denominatori e mangiare divisibilità. Per controllarli si usano le rappresentazioni di Galois associate tramite cambiamento di base (Clozel–Harris–Labesse, Shin, Chenevier–Harris) e si stimano i gruppi S_ℓ(E, j), nuclei di restrizione in H¹ a coefficienti Q_ℓ/Z_ℓ(−j). Gli strumenti sono la dualità di Poitou–Tate, l'argomento di deformazione alla Wiles e Taylor–Wiles, il sistema di Eulero di Kato per annullare certi gruppi di Selmer bidimensionali e torri ciclotomiche con la teoria di Iwasawa e l'annullamento dell'invariante μ di Ferrero–Washington. La libertà nella scelta dell'intervallo [Y, Y^{3/2}] serve a rendere piccoli gli indici eccezionali. Alpöge descrive questa parte come una forma «significativamente indebolita» della congettura di Vandiver, e congettura che ne seguano annullamenti di alcuni K-gruppi di Z.

Il terzo spiega l'esponente 1/2. I due errori principali hanno taglia x/m e m, a meno di potenze arbitrariamente piccole di x. Scegliendo m ≍ √x entrambi diventano circa √x (Lemma 6.1), con campi, pesi e posti scelti insieme a m (Proposizione 6.3). Alpöge indica proprio questo come il suggerimento di Claude che dovrebbe far «cadere dalla sedia»: una catena di √X sollevamenti theta per una somma di von Mangoldt di lunghezza X.

Sulla genesi, Alpöge racconta che la strada è partita da un modello giocattolo sui campi di funzioni: una dimostrazione «di solo segno» di Weil e Deligne tramite un'identità qN = M^k + R. Il passaggio decisivo è stato trovare un determinante «nativamente automorfo» che dava molteplicità 2 su O(2, n), con la prospettiva di ottenerne di più iterando i sollevamenti theta. La sua cronologia va dal 6 ottobre al 16 novembre 2026. Alpöge avverte però che quella cronologia, per le parti più tecniche, parafrasa un riassunto prodotto da Claude e «potrebbe non avere alcun senso», e che il riferimento autorevole è la formalizzazione in Lean.

### claude_overview-L4-s02

*panoramica, spiegazione 3 di 8.* Fatti del livello: 18 sì, 6 in parte, 6 no (copertura 0,70) · errori 1 su 67 · analogie dichiarate 1 · segnalazioni del critico 0, errori introdotti 0 · 1545 parole (limite 1500) · Gulpease 51,0

Il 20 novembre 2026 Levent Alpöge ha annunciato di aver dimostrato, lavorando con Claude, l'ipotesi di Riemann generalizzata per le funzioni L di Dirichlet. L'enunciato è quello classico: per ogni carattere di Dirichlet primitivo χ, ogni zero di L(s, χ) nella striscia 0 < Re(s) < 1 giace sulla retta Re(s) = 1/2. Il caso χ = 1 è l'ipotesi di Riemann per ζ. Alpöge si aspetta che il metodo arrivi, con più tempo, anche all'ipotesi di Riemann "estesa".

Sullo stato del lavoro va detta subito una cosa. Secondo Alpöge, l'argomento è stato formalizzato in Lean "senza assunzioni", e per ora è pubblicato soltanto il codice Lean. Lui stesso scrive che l'argomento è "incredibilmente lungo", che non padroneggia ancora alcune parti (in particolare le forme automorfe su gruppi di rango alto) e che la sua cronologia parafrasa in parte riassunti di Claude che "potrebbero non avere senso". La descrizione matematica più leggibile oggi è una "nota preliminare" di Robin Zhang, che parla di "proposed proof". Quello che segue ricostruisce l'architettura del ragionamento a partire da queste due fonti, senza aggiungere dettagli che esse non contengono.

**La riduzione analitica.** Il punto di partenza è la derivata logaritmica, −L′/L(s, χ) = Σ Λ(n)χ(n)n^(−s), tramite la media di Riesz del primo ordine:

S_χ(x) = Σ_{n≤x} Λ(n)χ(n)(x/n − 1).

La sua trasformata di Mellin è −L′(s, χ)/(s(s−1)L(s, χ)), quindi ogni zero nella striscia critica produce un polo. Per eliminare il polo spurio in s = 1 si correggono le somme:

- per χ non principale, G_χ(x) = S_χ(x) + x·L′(1, χ)/L(1, χ);
- per ζ, G_1(x) = Σ Λ(n)(x/n − 1) − x log x + (1 + γ)x.

Dato un carattere primitivo ψ di ordine r, si considera poi la combinazione

G_ψ = G_1 + (1/(3r+1)) Σ Re G_χ,

dove la somma corre sui caratteri primitivi che inducono le potenze non banali di ψ. Le potenze di ψ entrano tutte perché la dimostrazione impone, tramite l'ortogonalità dei caratteri, condizioni sui Frobenius. Poiché i coefficienti sono positivi, in uno zero ρ comune a più di queste L il residuo è una somma pesata positiva di molteplicità, e il polo non può cancellarsi.

Il cuore è la Proposizione 1.2: per ogni η > 0 e ogni A ≥ 2 esiste Y ≥ A tale che G_ψ(x) ≤ x^(1/2+η) per ogni x ∈ [Y, Y^(3/2)]. La stima è soltanto superiore e vale soltanto su intervalli arbitrariamente lontani, non per ogni x grande. Il passaggio da questa stima unilaterale all'assenza di zeri fuori dalla retta (Proposizioni 2.1 e 2.3) si appoggia, secondo la nota di Zhang, a Landau, Guinand, Turán e Weil. Le fonti non danno ulteriori dettagli su questo passaggio. Nella sua cronologia Alpöge ricorda che "Guinand-Weil aveva il segno" e cita un trucco con funzioni test di tipo varianza.

**L'idea guida: Stepanov senza derivate.** Alpöge presenta la dimostrazione come una discendente del metodo di Stepanov per l'ipotesi di Riemann sui campi di funzioni. Lì si costruisce un divisore ausiliario che si annulla con molteplicità alta nei punti da contare. Sugli interi la molteplicità è difficile da ottenere, perché equivarrebbe a "derivare i numeri interi". La sua risposta è sostituire la molteplicità con catene di sollevamenti theta: ogni sollevamento ne imita una. L'aneddoto che secondo lui farà "cadere dalla sedia" i colleghi è che, per una somma di von Mangoldt di lunghezza X, Claude propose una catena di lunghezza √X ("e cos'altro potrebbe essere?").

**Il principio aritmetico.** Il ponte fra primi e forme automorfe è la formula del prodotto: un intero algebrico non nullo molto divisibile ai primi finiti non può avere tutti i valori assoluti archimedei piccoli. Le somme sui primi compaiono nelle stime inferiori delle valutazioni p-adiche di periodi automorfi, cioè integrali di forme automorfe normalizzati in modo da prendere valori in un campo di numeri K. Una stima superiore delle loro dimensioni archimedee vincola quindi le somme sui primi. La difficoltà è mantenere un errore vicino a √x mentre variano campi e forme.

*Analogia mia, da prendere come tale:* è un bilancio contabile. Ogni fattore primo che divide il periodo è un "debito" che va pagato con grandezza archimedea. Se la grandezza disponibile è limitata, i debiti, cioè le somme sui primi, non possono essere troppo grandi.

**Periodi e sollevamenti theta.** Il setting è il seguente:

- si fissa un campo CM abeliano E che contiene il campo tagliato da ψ, con sottocampo totalmente reale massimale E⁺, e si lavora con gruppi unitari U(V) su E⁺;
- il periodo iniziale è un periodo di Bessel nel senso di Gan–Gross–Prasad: accoppia una forma cuspidale f su U(X₀), con X₀ totalmente definito, a una g su U(Y₀), integrando prima g contro un carattere su un sottogruppo unipotente e poi restringendo;
- si applica ripetutamente la corrispondenza theta di Weil–Howe, m volte su entrambi i lati: gli X_j restano totalmente definiti, mentre le segnature degli Y_j variano finché anche Y_m è definito;
- le identità seesaw di Kudla collegano il periodo iniziale agli accoppiamenti dopo i sollevamenti (periodi di Fourier–Jacobi, infine una restrizione U(Y_m) ⊂ U(X_m)).

Ogni sollevamento aggiunge un termine alla stima inferiore delle valutazioni: è la "molteplicità" di Stepanov. I sollevamenti cambiano però le norme di Petersson, controllate con le formule di Rallis e di Gan–Qiu–Takeda tramite valori speciali di funzioni L, e cambiano le dimensioni degli spazi, controllate con la formula di Weyl e con conteggi pesati di reticoli hermitiani alla Siegel.

Le costanti contano, perché G_χ ha già il termine principale sottratto. La normalizzazione usa periodi di varietà abeliane CM, legati alle derivate logaritmiche di L di Dirichlet da Chowla–Selberg e Anderson. Combinando tutto si ritrova esattamente il termine principale (Proposizione 3.1 e identità della Sezione 4.5): ciò che resta sono gli errori.

**Reticoli e geometria di Arakelov.** La divisibilità è resa precisa così. Si prende un O_K-reticolo M_α di forme automorfe algebriche alla Gross su U(X₀), con pesi massimi α, e un reticolo M_W di forme test ottenuto da sollevamenti theta discendenti. Si trovano poi un sottoreticolo M′_α di indice finito e un ideale frazionario a_α con P_α(M′_α, M_W) ⊆ a_α. Riscalando si ottengono mappe intere b_α: N_α → C = Hom(M_W, O_K).

Il confronto tra finito e archimedeo diventa così una stima dal basso della pendenza media di C. Servono due ingredienti:

- *covolumi dei domini.* Le forme si vedono come sezioni di fibrati su schemi di moduli di varietà abeliane principalmente polarizzate con azione di O_E, compattificati alla Faltings–Chai. Si usano le formule di Hilbert–Samuel aritmetiche (Gillet–Soulé, Zhang), le disuguaglianze sui minimi successivi di Zhang e il criterio di Moriwaki. Ai primi finiti, il controllo dei differenziali invarianti passa per le stime di Fargues sulle mappe di Hodge–Tate e per la teoria di Dieudonné prismatica di Anschütz–Le Bras;
- *generazione.* Bisogna mostrare che i funzionali di periodo generano quasi tutto W^∨, anche dopo piccole perdite di dimensione. Altrimenti, se le immagini stessero su una retta, non direbbero nulla sulle altre direzioni. Qui entrano la filtrazione di Harder–Narasimhan per reticoli hermitiani (Stuhler, Grayson) e la disuguaglianza delle pendenze di Bost (Lemma 4.2, Proposizione 4.3).

**Posti complessi e Behrend.** Le condizioni di Frobenius, riscritte con l'ortogonalità dei caratteri, producono termini G_χ(a_t/w_{j,ρ}). Gli interi w_{j,ρ} fissano i blocchi di parametri di Harish-Chandra aggiunti da ciascun sollevamento al posto ρ. Mediando su sottogruppi di Gal(E/Q) si ricostruisce G_ψ(x). L'insieme T₂ di posti scelti deve essere grande, ma senza troppi punti in un segmento corto di un'orbita di Frobenius. Per questo si adatta la costruzione di Behrend di insiemi senza progressioni aritmetiche di tre termini, che limita ogni intersezione rilevante a due posti. Agli altri posti bastano regioni libere da zeri. Alpöge stesso ritiene che questo trucco sia "ovviamente" destinato a sparire.

**Congruenze e coomologia di Galois.** Le formule sulle norme valgono per autoforme di Hecke, ma proiettare un O_K-reticolo sugli autospazi introduce denominatori che possono mangiare la divisibilità. Questi denominatori si controllano attraverso le congruenze tra autovalori di Hecke:

- il cambiamento di base porta ai gruppi lineari, dove si usano le rappresentazioni di Galois di Clozel–Harris–Labesse, Shin e Chenevier–Harris;
- gli addendi unidimensionali prodotti dai sollevamenti generano gruppi S_ℓ(E, j) di coomologia di Galois a coefficienti in Q_ℓ/Z_ℓ(−j), studiati con la dualità di Tate–Poitou;
- servono inoltre argomenti di deformazione alla Wiles, Taylor–Wiles e Clozel–Harris–Taylor, e il sistema di Eulero di Kato per annullare certi gruppi di Selmer;
- E varia lungo torri ciclotomiche (Iwasawa, μ = 0 di Ferrero–Washington).

Ai twist "eccezionali" serve una stima più grossolana. Qui si usa la libertà nella scelta dell'intervallo [Y, Y^(3/2)]: si sceglie un intervallo in cui tutti gli indici eccezionali sono piccoli rispetto a x. Alpöge descrive questo passaggio come "un indebolimento significativo di Vandiver", ancora molto forte.

**Perché proprio 1/2.** Messi insieme valori dei periodi, norme, covolumi e denominatori, i due errori principali in G_ψ(x) hanno ordine x/m e m, a meno di fattori x^ε. Scegliere m ≍ √x li bilancia entrambi a circa √x (Lemma 6.1). Campi, pesi e posti vengono scelti insieme a m (Proposizione 6.3), e da qui seguono la Proposizione 1.2 e quindi la congettura.

Resta che Alpöge considera questa versione piena di scelte "strane e subottimali" e si aspetta semplificazioni rapide. Per una verifica umana completa bisognerà aspettare la stesura che ha promesso. Per ora la garanzia dichiarata è la formalizzazione in Lean.

### claude_overview-L4-s03

*panoramica, spiegazione 4 di 8.* Fatti del livello: 18 sì, 8 in parte, 4 no (copertura 0,73) · errori 1 su 63 · analogie dichiarate 1 · segnalazioni del critico 0, errori introdotti 0 · 1656 parole (limite 1500) · Gulpease 56,4

Il risultato annunciato da Levent Alpöge riguarda la congettura nella forma riportata da Robin Zhang (Congettura 1.1): per ogni carattere di Dirichlet primitivo χ, ogni zero di L(s, χ) nella striscia 0 < Re(s) < 1 sta sulla retta Re(s) = 1/2. Bastano i caratteri primitivi, perché togliere fattori di Eulero non introduce zeri in Re(s) > 0. Alpöge scrive di aspettarsi che il metodo arrivi anche all'ipotesi di Riemann estesa, ma questo non fa parte di ciò che viene annunciato.

Sullo stato della dimostrazione conviene essere precisi fin dall'inizio. Alpöge dichiara di aver formalizzato l'argomento in Lean insieme a Claude, «senza assunzioni», e pubblica soltanto il codice Lean, diviso in quattordici archivi. Non esiste ancora una versione leggibile. Una stesura automatica che aveva prodotto superava le 250.000 pagine, e lui stesso la considera impresentabile. Ammette anche di non padroneggiare ancora molte parti dell'argomento. La nota di Zhang si intitola «nota preliminare» e parla di «proposed proof». Le fonti non riferiscono verifiche indipendenti del codice. Quella che segue è quindi la ricostruzione di Zhang.

Il primo passo è classico: dalle somme sulle potenze di primi agli zeri. Alpöge non lavora direttamente con −L′/L, ma con la media di Riesz del primo ordine
S_χ(x) = Σ_{n≤x} Λ(n)χ(n)(x/n − 1),
che ha una trasformata di Mellin molto semplice:
∫₁^∞ S_χ(x) x^{−s−1} dx = −L′(s, χ) / (s(s−1) L(s, χ)).
Uno zero nella striscia critica produce un polo, quindi stime di crescita su S_χ vincolano la posizione degli zeri. Il polo spurio in s = 1 si elimina con una correzione. Per χ non principale si pone G_χ(x) = S_χ(x) + x L′(1, χ)/L(1, χ). Per ζ si pone G_1(x) = Σ Λ(n)(x/n − 1) − x log x + (1 + γ)x.

Poi, fissato un carattere primitivo ψ di ordine r, Alpöge non stima un singolo G_χ. Stima la combinazione positiva
G_ψ = G_1 + (3r+1)^{−1} Σ_{χ ∈ X_ψ, χ ≠ 1} Re G_χ,
dove X_ψ è l'insieme dei caratteri primitivi che inducono le potenze di ψ. Le potenze compaiono tutte perché l'argomento impone condizioni sui Frobenius tramite l'ortogonalità dei caratteri. Siccome X_ψ è stabile per coniugio, in uno zero ρ il residuo è 1/(ρ(1−ρ)) per una somma pesata e positiva di molteplicità. Gli zeri quindi non possono cancellarsi a vicenda.

Il cuore analitico è la Proposizione 1.2. Per ogni η > 0 e ogni A ≥ 2 esiste Y ≥ A tale che G_ψ(x) ≤ x^{1/2+η} per ogni x in [Y, Y^{3/2}]. La stima è unilaterale e vale solo su intervalli arbitrariamente lontani, non per ogni x grande. La Sezione 2 della nota mostra perché basta comunque a escludere zeri fuori dalla retta critica, appoggiandosi a risultati attribuiti a Landau, Guinand, Turán e Weil. Nella sua cronologia Alpöge accenna a un segno fornito dalla formula esplicita di Guinand–Weil e a un «trucco» con funzioni test di tipo varianza. Le fonti non danno altri dettagli su questo punto.

Tutto il resto della dimostrazione serve a provare la Proposizione 1.2. L'idea guida discende dall'argomento di Stepanov per l'ipotesi di Riemann sui campi di funzioni, ed è un'analogia proposta dallo stesso Alpöge. Lì si costruisce un oggetto che si annulla con alta molteplicità, cioè un divisore con molteplicità, e lo si confronta con il suo grado. Sugli interi la molteplicità è difficile da trovare, perché equivarrebbe a qualcosa come «derivare i numeri interi». Il sostituto è aritmetico e si basa sulla formula del prodotto: un intero algebrico non nullo molto divisibile ai primi finiti non può essere piccolo a tutti i posti archimedei. Le somme sulle potenze di primi compaiono nelle stime dal basso delle valutazioni di certi periodi automorfi normalizzati. Una stima dall'alto della loro taglia archimedea vincola quindi le somme. Il tutto va fatto con un errore vicino a √x, mentre variano campi di numeri e forme automorfe.

Per descrivere questo meccanismo propongo un'immagine mia, da prendere solo come analogia: una tenaglia. Un ganascia è la divisibilità p-adica, che spinge le valutazioni verso l'alto. L'altra sono le norme di Petersson e la geometria di Arakelov, che limitano la taglia. Lo spazio che resta fra le due è la stima su G_ψ.

Vediamo ora i periodi e i sollevamenti theta. Sia E un campo CM abeliano che contiene il campo tagliato da ψ, e sia E⁺ il suo sottocampo totalmente reale massimale. Si lavora con gruppi unitari U(V) di spazi hermitiani su E. Il periodo iniziale accoppia forme cuspidali f su U(X₀) e g su U(Y₀), con X₀ ⊂ Y₀ e X₀ totalmente definito. È un periodo di Bessel nel senso di Gan–Gross–Prasad: si prende un coefficiente di Fourier di g lungo un sottogruppo unipotente e lo si accoppia con f. Poi si applica ripetutamente la corrispondenza theta di Weil e Howe, m volte su entrambi gli argomenti, lungo catene U(X_j) e U(Y_j). Gli X_j restano totalmente definiti, mentre le segnature degli Y_j variano finché anche Y_m diventa definito. Le identità seesaw di Kudla legano il periodo di Bessel iniziale all'accoppiamento di restrizione finale per U(Y_m) ⊂ U(X_m).

Ogni sollevamento aggiunge un contributo alla divisibilità e fa le veci di un ordine di molteplicità alla Stepanov. Questa è la «molteplicità» trovata in modo nativamente automorfo. La contropartita è un costo sul lato delle norme, che si controlla con la formula di Rallis e con Gan–Qiu–Takeda (norme di Petersson tramite valori speciali di funzioni L e integrali locali). Le dimensioni si controllano con la formula di Weyl e con conteggi pesati di reticoli hermitiani alla Siegel.

Le costanti contano, perché G_χ ha già un termine principale sottratto. La normalizzazione usa periodi di varietà abeliane CM, che Chowla–Selberg e Anderson collegano alle derivate logaritmiche delle funzioni L di Dirichlet. È proprio da qui che si ricupera il termine principale x L′(1, χ)/L(1, χ) (Proposizione 3.1, identità della Sezione 4.5).

Il confronto vero e proprio avviene tramite reticoli e pendenze. Sugli O_K-reticoli M_α di forme automorfe algebriche nel senso di Gross, Alpöge costruisce un sottoreticolo M′_α e un ideale frazionario a_α tali che ord_p(P_α(f, g)) ≥ ord_p(a_α) per ogni primo finito. Questo è il significato preciso di «divisibilità» nell'argomento. Riscalando si ottengono mappe intere b_α : N_α → C = Hom(M_W, O_K), dove M_W è un reticolo di forme test ottenute per sollevamento discendente da U(Y_m). Le norme di queste mappe danno un limite inferiore alla pendenza media di C.

Servono però limiti sui covolumi dei domini. Questi vengono dalla geometria di uno schema di moduli di varietà abeliane principalmente polarizzate con azione di O_E, con le relative compattificazioni (Faltings–Chai). Gli ingredienti sono le formule di Hilbert–Samuel aritmetiche di Gillet–Soulé e Zhang, i minimi successivi di Zhang e il criterio di Moriwaki. Ai primi finiti si usano le stime di Fargues sulle mappe di Hodge–Tate e la teoria di Dieudonné prismatica di Anschütz–Le Bras.

Infine bisogna garantire che i funzionali di periodo generino quasi tutto W^∨. Se le immagini stessero su una retta, non direbbero nulla sulle altre direzioni. Per questo si usano la filtrazione di Harder–Narasimhan per reticoli hermitiani (Stuhler, Grayson), la disuguaglianza di pendenza di Bost e il Lemma 4.2. Il risultato è la Proposizione 4.3.

Restano due ingredienti combinatori e aritmetici. Il primo riguarda la scelta dei posti complessi. Al j-esimo sollevamento, a un posto complesso ρ si aggiunge un blocco di parametri di Harish-Chandra centrato in −w_{j,ρ}, e nelle stime compaiono termini G_χ(a_t/w_{j,ρ}). Scegliendo i w_{j,ρ} e mediando su sottogruppi di Gal(E/Q) si ricostruisce G_ψ(x). L'insieme T₂ dei posti usati deve essere grande, ma le stime perdono precisione se troppi suoi posti cadono in un breve segmento di un'orbita di Frobenius. Alpöge adatta allora la costruzione di Behrend di insiemi grandi senza progressioni aritmetiche di tre termini, in modo che ogni intersezione rilevante contenga al più due posti. Gli altri posti si controllano con regioni libere da zeri. Alpöge stesso considera questo trucco quasi certamente eliminabile.

Il secondo ingrediente riguarda i denominatori. Le formule per le norme valgono per autoforme di Hecke, ma proiettare un reticolo sugli autospazi può introdurre denominatori che mangiano divisibilità (Hida). Per controllarli si passa per cambiamento di base a GL_n su E. Alle rappresentazioni algebriche regolari polarizzate si associano rappresentazioni di Galois (Clozel–Harris–Labesse, Shin, Chenevier–Harris), e si studiano i gruppi S_ℓ(E, j). Questi sono nuclei di restrizione in H¹ non ramificata fuori da ℓ, a coefficienti Q_ℓ/Z_ℓ(−j). Gli strumenti sono la dualità di Poitou–Tate e le deformazioni alla Wiles e Taylor–Wiles. Per alcuni gruppi di Selmer di rappresentazioni modulari bidimensionali serve il sistema di Eulero di Kato.

Poiché i pesi devono crescere, E varia lungo torri ciclotomiche, con la teoria di Iwasawa e l'annullamento dell'invariante μ di Ferrero–Washington. Alpöge descrive questa parte come una «significativa versione indebolita» di Vandiver. Ci sono poi alcuni twist eccezionali per cui si ha solo una stima più grossolana. Qui interviene la libertà di scegliere l'intervallo [Y, Y^{3/2}]: lo si prende in modo che quegli indici siano piccoli rispetto a x.

Resta da capire perché l'esponente sia 1/2. Messi insieme tutti i pezzi, i due errori principali nella stima di G_ψ(x) valgono x/m e m, a meno di fattori x^{ε}. Scegliendo m dell'ordine di √x (Lemma 6.1, Proposizione 6.3) entrambi diventano circa √x. Alpöge racconta che fu proprio Claude a suggerire una catena di sollevamenti theta di lunghezza √X, ciascuno a imitare un ordine di molteplicità. In questo senso la retta critica emerge da un bilanciamento: più sollevamenti danno più «molteplicità», ma ciascuno ha un costo. Alpöge nota anche che, contando a priori il costo di ogni sollevamento, ci si sarebbe fermati a 2/3, e che servirono passaggi ulteriori (l'«extra averaging» tra caratteri di Hecke) per arrivare in fondo.

Riassumendo, si tratta di un argomento enorme, che mette insieme forme automorfe su gruppi unitari, geometria di Arakelov, teoria di Hodge p-adica integrale e coomologia di Galois al servizio di una stima di tipo Stepanov. Per ora è disponibile solo come formalizzazione Lean e come la panoramica preliminare di Zhang. Lo stesso Alpöge si aspetta semplificazioni sostanziali a breve.

### claude_overview-L4-s04

*panoramica, spiegazione 5 di 8.* Fatti del livello: 18 sì, 7 in parte, 5 no (copertura 0,72) · errori 3 su 55 · analogie dichiarate 1 · segnalazioni del critico 2, errori introdotti 1 · 1477 parole (limite 1500) · Gulpease 52,1

Il 20 novembre 2026 Levent Alpöge ha annunciato di aver dimostrato, lavorando con Claude, l'ipotesi di Riemann generalizzata per le funzioni L di Dirichlet. L'enunciato, nella forma riportata da Robin Zhang, è questo: per ogni carattere di Dirichlet primitivo χ, ogni zero di L(s,χ) nella striscia 0 < Re(s) < 1 giace sulla retta Re(s) = 1/2. Prima di entrare nel merito conviene chiarire lo stato del risultato. Alpöge non ha diffuso un testo leggibile, ma soltanto una formalizzazione in Lean, distribuita in 14 archivi, e afferma che l'argomento è formalizzato «senza assunzioni». Scrive che l'argomento è per ora «incredibilmente lungo»: una versione dettagliata generata automaticamente supera le 250.000 pagine. Ammette di non padroneggiare ancora tutta la matematica che lo circonda e avverte che parte della cronologia da lui fornita parafrasa riassunti di Claude che «potrebbero non avere alcun senso». La ricostruzione che segue si basa soprattutto sulla nota di Zhang, che si presenta come «preliminare», parla di «proposed proof» e dichiara di «tentare» un riassunto.

**La riduzione a una stima sulle potenze di primi.** Il punto di partenza è classico. Per Re(s) > 1 vale −L′/L(s,χ) = Σ Λ(n)χ(n)n^{−s}. Alpöge ne considera la media di Riesz del primo ordine:

S_χ(x) = Σ_{n≤x} Λ(n)χ(n)(x/n − 1).

La sua trasformata di Mellin ∫₁^∞ S_χ(x)x^{−s−1}dx è uguale a −L′(s,χ)/(s(s−1)L(s,χ)). Uno zero nella striscia critica produce quindi un polo, e stime di crescita su S_χ vincolano la posizione degli zeri. Per eliminare il polo in s = 1 si usano due correzioni:

- per χ non principale, G_χ(x) = S_χ(x) + xL′(1,χ)/L(1,χ);
- per ζ, G₁(x) = Σ_{n≤x} Λ(n)(x/n − 1) − x log x + (1+γ)x.

Fissato ψ primitivo di ordine r, si prende poi una combinazione positiva su tutti i caratteri primitivi che inducono le potenze di ψ:

G_ψ = G₁ + (3r+1)^{−1} Σ Re G_χ.

In uno zero ρ, il residuo della trasformata di G_ψ è 1/(ρ(1−ρ)) moltiplicato per una somma pesata, a coefficienti positivi, delle molteplicità. Non può quindi esserci cancellazione tra le diverse funzioni L. Tutto si riduce alla Proposizione 1.2: per ogni η > 0 e ogni A ≥ 2 esiste Y ≥ A tale che G_ψ(x) ≤ x^{1/2+η} per ogni x in [Y, Y^{3/2}].

Si noti che la stima è solo dall'alto e vale solo su intervalli che non coprono tutti gli x grandi. Che basti lo mostra la Sezione 2 della nota di Zhang, con strumenti di Landau, Guinand, Turán e Weil. Le fonti non dettagliano questo passaggio; Alpöge annota soltanto che «Guinand–Weil aveva il segno».

**L'idea centrale: divisibilità contro grandezza archimedea.** Il motore è la formula del prodotto: un intero algebrico non nullo molto divisibile ai primi finiti non può avere tutti i valori assoluti archimedei piccoli. Le somme sulle potenze di primi compaiono come minoranti delle valutazioni di periodi automorfi, cioè integrali di forme automorfe normalizzati in modo da prendere valori in un campo di numeri K. Una maggiorazione archimedea dei periodi diventa così una maggiorazione delle somme. La difficoltà sta nel mantenere un errore vicino a √x mentre variano i campi e le forme.

Alpöge descrive l'argomento come un discendente di quello di Stepanov per l'ipotesi di Riemann sui campi di funzioni, che usa un divisore con molteplicità. Sugli interi la molteplicità è difficile da ottenere: sarebbe come «derivare i numeri interi». La sua soluzione, presentata da lui stesso come analogia, è che ogni sollevamento theta «imiti» un ordine di molteplicità. Secondo Alpöge, la lunghezza della catena di sollevamenti proposta da Claude, √X per una somma di von Mangoldt di lunghezza X, è il dettaglio che farebbe «cadere dalla sedia» i matematici.

**La costruzione automorfa.** Si lavora con gruppi unitari sul sottocampo totalmente reale massimale E₊ di un campo CM abeliano E che contiene il campo tagliato da ψ. Il periodo iniziale è un periodo di Bessel di tipo Gan–Gross–Prasad. Accoppia una forma cuspidale f su U(X₀) e una forma g su U(Y₀), con X₀ ⊂ Y₀ e X₀ totalmente definito: si prende un coefficiente di Fourier di g lungo un unipotente e lo si accoppia con f.

Si applicano poi m sollevamenti theta (Weil, Howe) su entrambi i lati dell'accoppiamento. Tutti gli X_j restano totalmente definiti, mentre le segnature degli Y_j variano finché anche Y_m è definito. Le identità seesaw di Kudla legano il periodo iniziale agli accoppiamenti successivi, passando per periodi di Fourier–Jacobi, fino a un accoppiamento di restrizione per U(Y_m) ⊂ U(X_m). Ogni sollevamento aggiunge un termine al minorante delle valutazioni.

I sollevamenti alterano però norme e dimensioni, e queste vanno controllate:

- le norme di Petersson dei sollevamenti si esprimono con valori speciali di funzioni L e integrali locali, tramite le formule di Rallis e di Gan–Qiu–Takeda;
- le dimensioni e le molteplicità si controllano con la formula di Weyl e con conteggi pesati di reticoli hermitiani alla Siegel;
- la normalizzazione usa periodi di varietà abeliane CM, legati alle derivate logaritmiche delle funzioni L di Dirichlet (Chowla–Selberg, Anderson).

Le costanti contano, perché nei G_χ è già stato sottratto un termine principale. Il termine principale si ricostruisce infatti esattamente (Proposizione 3.1 e identità della Sezione 4.5), e restano solo gli errori.

**Il lato aritmetico: reticoli e pendenze.** La «divisibilità» ha un senso preciso. Su U(X₀) si usano reticoli M_α di forme automorfe algebriche alla Gross, con pesi più alti α; dall'altro lato, i sollevamenti verso il basso da U(Y_m) forniscono un reticolo M_W. Si costruiscono un sottoreticolo di indice finito M′_α ⊆ M_α e un ideale frazionario a_α tali che P_α(M′_α, M_W) ⊆ a_α. Riscalando, si ottengono mappe intere b_α: N_α → C = Hom(M_W, O_K).

L'obiettivo diventa minorare la pendenza media μ(C). Servono due cose:

- **Maggiorare i covolumi dei domini.** Si usano altezze su compattificazioni aritmetiche dello schema dei moduli di varietà abeliane con azione di O_E (Faltings–Chai), le formule di Hilbert–Samuel aritmetiche (Gillet–Soulé, Zhang) e i minimi successivi (Zhang, Moriwaki). Ai primi finiti entrano le stime di Fargues sulle mappe di Hodge–Tate e la teoria di Dieudonné prismatica di Anschütz–Le Bras.
- **Garantire che i funzionali di periodo generino quasi tutto W^∨.** Se le immagini stessero su una retta, non darebbero informazione sulle altre direzioni. Qui intervengono la filtrazione di Harder–Narasimhan per reticoli hermitiani (Stuhler, Grayson), la disuguaglianza delle pendenze di Bost e il Lemma 4.2. Il risultato è la Proposizione 4.3.

**Frobenius e progressioni aritmetiche.** Le valutazioni coinvolgono potenze di primi soggette a condizioni di Frobenius. Per ortogonalità dei caratteri queste diventano termini G_χ(a_t/w_{j,ρ}), dove gli interi w_{j,ρ} fissano i blocchi di parametri di Harish-Chandra aggiunti a ogni sollevamento. L'insieme T₂ di posti complessi usati deve essere grande, ma senza troppi punti in un segmento corto di un'orbita di Frobenius. Per conciliare le due esigenze si adatta la costruzione di Behrend di insiemi senza progressioni aritmetiche di tre termini, che limita ogni intersezione a due posti. Gli altri posti si trattano con regioni libere da zeri. Alpöge ritiene che questo trucco sia «ovviamente» destinato a sparire.

**Denominatori di Hecke e coomologia di Galois.** Le formule sulle norme valgono per autoforme di Hecke. Proiettare un reticolo sugli autospazi può introdurre denominatori che mangiano divisibilità, e questi denominatori misurano congruenze tra autovalori di Hecke. Per controllarli si passa ai gruppi lineari tramite cambiamento di base e si usano le rappresentazioni di Galois di Clozel–Harris–Labesse, Shin e Chenevier–Harris.

Le parti di dimensione uno producono gruppi S_ℓ(E,j), nuclei della restrizione in H¹ a coefficienti Q_ℓ/Z_ℓ(−j). La dualità di Tate–Poitou li collega all'H². Gli autospazi della coniugazione complessa si trattano in due modi:

- uno con i valori di Bernoulli generalizzati e Stickelberger;
- l'altro con la teoria delle deformazioni alla Wiles, Taylor–Wiles e Clozel–Harris–Taylor, insieme al sistema di Eulero di Kato per annullare certi gruppi di Selmer di rappresentazioni modulari di dimensione 2.

Poiché i pesi crescono, E varia lungo torri ciclotomiche (Iwasawa, con μ = 0 per Ferrero–Washington). Per i twist eccezionali si sfrutta la libertà di scegliere l'intervallo [Y, Y^{3/2}]. Alpöge descrive questo passaggio come una «significativa indebolitura di Vandiver», comunque molto forte.

**Perché proprio l'esponente 1/2.** Messi insieme tutti i pezzi, i due errori principali nella stima di G_ψ(x) hanno ordine x/m e m, a meno di potenze arbitrariamente piccole di x. Scegliendo m ≈ √x, entrambi diventano circa √x (Lemma 6.1, con le scelte simultanee della Proposizione 6.3). Un'analogia mia, non delle fonti: è come scegliere il passo di un metodo numerico che bilanci errore di troncamento ed errore di arrotondamento, dove l'ottimo cade alla media geometrica. Alpöge riporta che il calcolo del «costo» di ogni sollevamento indicava che, senza ulteriori idee, ci si sarebbe fermati a 2/3.

**Cautele.** Alpöge stesso ritiene di aver inserito scelte strane e subottimali e si aspetta semplificazioni rapide. Le fonti non dicono se esperti indipendenti abbiano già verificato la formalizzazione Lean, né se l'enunciato formalizzato sia stato controllato contro la Congettura 1.1. Per ora il riscontro umano più dettagliato è la nota preliminare di Zhang.

### claude_overview-L4-s05

*panoramica, spiegazione 6 di 8.* Fatti del livello: 18 sì, 8 in parte, 4 no (copertura 0,73) · errori 2 su 57 · analogie dichiarate 0 · segnalazioni del critico 0, errori introdotti 0 · 1457 parole (limite 1500) · Gulpease 56,4

Il 20 novembre 2026 Levent Alpöge ha annunciato una dimostrazione dell'ipotesi di Riemann generalizzata per le funzioni L di Dirichlet. L'enunciato è quello di Piltz (1884): per ogni carattere di Dirichlet primitivo χ, ogni zero di L(s, χ) nella striscia 0 < Re(s) < 1 sta sulla retta Re(s) = 1/2. Il caso χ = 1 è l'ipotesi di Riemann classica. Alpöge si aspetta di arrivare, con più tempo, anche all'ipotesi estesa, ma questo non viene rivendicato.

La dimostrazione è stata ottenuta lavorando con Claude. Secondo l'autore è stata formalizzata in Lean «senza assunzioni», e per ora è pubblicata solo come archivio Lean in quattordici parti. Alpöge ha scartato l'idea di diffondere un documento illeggibile (una versione generata arriva a oltre 250.000 pagine). Ammette di non padroneggiare ancora tutta la matematica coinvolta e si aspetta semplificazioni rapide. Quello che segue si basa soprattutto sulla «nota preliminare» di Robin Zhang, che riassume la «dimostrazione proposta». Le fonti non dicono nulla su verifiche indipendenti della formalizzazione.

**La riduzione a una disuguaglianza unilaterale.** Il punto di partenza è classico. Invece di −L′/L si studia la media di Riesz del primo ordine

S_χ(x) = Σ_{n≤x} Λ(n) χ(n) (x/n − 1),

la cui trasformata di Mellin, per Re(s) > 1, è

∫₁^∞ S_χ(x) x^{−s−1} dx = −L′(s, χ) / (s(s−1) L(s, χ)).

Uno zero nella striscia critica produce un polo, quindi una buona stima di crescita su S_χ ne vincola la posizione. Il possibile polo in s = 1 viene eliminato con una correzione:

- per χ non principale, G_χ(x) = S_χ(x) + x L′(1, χ)/L(1, χ);
- per ζ, G_1(x) = Σ Λ(n)(x/n − 1) − x log x + (1 + γ)x.

Non si lavora su un carattere alla volta. Per ψ primitivo di ordine r si considera

G_ψ = G_1 + (1/(3r+1)) Σ Re G_χ,

con χ che percorre i caratteri primitivi che inducono le potenze di ψ. Le potenze compaiono tutte perché, più avanti, l'ortogonalità dei caratteri serve a imporre condizioni sui Frobenius. Poiché l'insieme è stabile per coniugio, il residuo in uno zero ρ è 1/(ρ(1−ρ)) per una somma di molteplicità con pesi positivi. Gli zeri di funzioni L diverse quindi non possono cancellarsi.

Il cuore analitico è la Proposizione 1.2: per ogni η > 0 e ogni A ≥ 2 esiste Y ≥ A tale che

G_ψ(x) ≤ x^{1/2+η} per ogni x ∈ [Y, Y^{3/2}].

È una stima solo dall'alto, e solo su intervalli arbitrariamente lontani che non coprono tutto. Il passaggio da qui alla non-annullazione occupa la Sezione 2 di Zhang, con riferimenti a Landau, Guinand, Turán e Weil. Il testo di quella sezione non è tra le fonti, quindi non ne descrivo il meccanismo. Alpöge accenna soltanto che «Guinand-Weil aveva il segno».

**L'idea guida: Stepanov senza derivate.** Alpöge dichiara la genealogia del metodo. Nel metodo di Stepanov per l'ipotesi di Riemann sui campi di funzioni si usa un divisore con molteplicità. Sugli interi la molteplicità è difficile da trovare, perché richiederebbe qualcosa come «derivare i numeri interi». Partendo da idee di analisi di Fourier in un modello giocattolo, lui e Claude hanno cercato un modo «nativamente automorfo» di far ricomparire la molteplicità, e lo hanno trovato in catene di sollevamenti theta: ogni sollevamento ne imita una. La lunghezza della catena suggerita da Claude per una somma di von Mangoldt di lunghezza X è √X. Alpöge lo presenta come il dettaglio destinato a far «cadere dalla sedia» i colleghi.

Sul piano tecnico, Zhang descrive il meccanismo come una conseguenza della formula del prodotto. Un intero algebrico non nullo molto divisibile ai primi finiti non può essere piccolo a tutti i posti archimedei. Le somme sui primi entrano come minoranti delle valutazioni di certi periodi automorfi normalizzati a valori in un campo di numeri K. Una maggiorazione delle loro taglie archimedee si traduce allora in una maggiorazione di G_ψ. La difficoltà è mantenere un errore vicino a √x mentre campi e forme variano.

**Periodi e sollevamenti theta.** Si fissa un campo CM abeliano E che contiene il campo tagliato da ψ, con sottocampo totalmente reale massimale E⁺, e si considerano gruppi unitari di E-spazi hermitiani. Il periodo iniziale è un periodo di Bessel nel senso di Gan–Gross–Prasad. Accoppia una forma cuspidale f su U(X₀), con X₀ totalmente definito, con una forma g su U(Y₀), dove X₀ ⊂ Y₀. Concretamente si prende un coefficiente di Fourier di g lungo un unipotente e lo si integra contro f.

A entrambi gli argomenti si applicano poi m sollevamenti theta successivi (Weil, Howe). Gli X_j restano totalmente definiti, mentre le segnature degli Y_j variano finché anche Y_m è definito. Le identità seesaw di Kudla legano il periodo iniziale all'accoppiamento finale di restrizione U(Y_m) ⊂ U(X_m). Ogni sollevamento aggiunge termini ai minoranti delle valutazioni finite.

Per controllare le norme di Petersson dei sollevati si usano le formule di Rallis e di Gan–Qiu–Takeda, che le esprimono tramite valori speciali di funzioni L e integrali locali. Per dimensioni e molteplicità si usano la formula di Weyl e conteggi pesati di reticoli hermitiani alla Siegel (massa). Le costanti contano, perché nelle G_χ un termine principale è già stato sottratto. Questo termine viene ricostruito esattamente attraverso i periodi di varietà abeliane CM, legati alle derivate logaritmiche delle L di Dirichlet da Chowla–Selberg e Anderson.

**Il lato aritmetico-geometrico.** La divisibilità è resa precisa con reticoli. Si prende un O_K-reticolo M_α di forme automorfe algebriche alla Gross su U(X₀), con peso più alto α, e un reticolo M_W di forme test ottenute per sollevamento verso il basso da U(Y_m). Si costruiscono un sottoreticolo M′_α e un ideale frazionario a_α con P_α(M′_α, M_W) ⊆ a_α. Ne vengono mappe intere

b_α : N_α → C = Hom(M_W, O_K).

Il confronto diventa un problema di pendenze. Bisogna minorare la pendenza media di C, e per questo servono maggioranti dei covolumi dei domini. Qui entra la geometria di Arakelov sugli spazi di moduli di varietà abeliane con azione di O_E:

- compattificazioni alla Faltings–Chai;
- Hilbert–Samuel aritmetico (Gillet–Soulé, Zhang);
- minimi successivi di Zhang e criterio di Moriwaki, con idee di Yuan;
- al finito, stime di Fargues sulle mappe di Hodge–Tate e la teoria di Dieudonné prismatica di Anschütz–Le Bras.

Serve anche che i funzionali di periodo generino quasi tutto il duale. Questo si ottiene con la filtrazione di Harder–Narasimhan per reticoli hermitiani (Stuhler, Grayson) e con la disuguaglianza delle pendenze di Bost.

**Frobenius e progressioni aritmetiche.** Le condizioni sui Frobenius, tradotte con l'ortogonalità dei caratteri, producono termini G_χ(a_t / w_{j,ρ}). Qui ρ percorre posti complessi di E e i pesi w_{j,ρ} determinano i blocchi di parametri di Harish-Chandra aggiunti da ogni sollevamento. L'insieme di posti usato deve essere grande, ma senza troppi punti in un segmento corto di un'orbita di Frobenius. Per questo si adatta la costruzione di Behrend di insiemi senza progressioni aritmetiche di tre termini. Gli altri posti si controllano con regioni libere da zeri. Alpöge ritiene questo trucco «ovviamente non necessario».

**Denominatori e coomologia di Galois.** Le formule sulle norme valgono per autovettori di Hecke. Proiettare un reticolo sugli autospazi può però introdurre denominatori e mangiarsi parte della divisibilità. Questi denominatori si controllano con le congruenze tra autovalori, studiate attraverso le rappresentazioni di Galois. Il percorso è il seguente:

1. cambiamento di base a GL_n;
2. rappresentazioni di Galois associate (Clozel–Harris–Labesse, Shin, Chenevier–Harris);
3. gruppi S_ℓ(E, j), nuclei di restrizione in H¹ a coefficienti in Q_ℓ/Z_ℓ(−j), controllati con la dualità di Tate–Poitou;
4. argomenti di deformazione alla Wiles, Taylor–Wiles e Clozel–Harris–Taylor;
5. il sistema di Eulero di Kato, per annullare certi gruppi di Selmer.

Poiché i pesi crescono, si fa variare E lungo torri ciclotomiche, usando la teoria di Iwasawa e l'annullamento dell'invariante μ (Ferrero–Washington). La libertà di scegliere l'intervallo [Y, Y^{3/2}] serve a rendere piccoli gli indici eccezionali. Alpöge descrive questa parte come la conquista di un «indebolimento significativo di Vandiver». Crede che ne seguano annullamenti di alcuni K-gruppi di Z, ma lo presenta come una convinzione, non come un risultato.

**Da dove viene 1/2.** Messi insieme tutti i pezzi, i due errori principali nella stima di G_ψ(x) hanno taglia x/m e m, a meno di fattori x^ε. Scegliere m ≍ √x li bilancia entrambi a √x. In questo senso l'esponente 1/2 della retta critica coincide con il numero ottimale di «molteplicità» theta. Campi, pesi e posti vanno scelti insieme a m: è la Proposizione 6.3 citata da Zhang.

**Lo stato delle cose.** Non è ancora una dimostrazione leggibile da un essere umano. È un argomento lunghissimo, formalizzato in Lean secondo l'autore, che attraversa buona parte della teoria dei numeri contemporanea. La sua architettura è nota per ora attraverso una nota preliminare di un terzo e la cronologia di Alpöge, che lui stesso definisce in parte una parafrasi di riassunti che «potrebbero non avere senso».

### claude_overview-L4-s06

*panoramica, spiegazione 7 di 8.* Fatti del livello: 18 sì, 8 in parte, 4 no (copertura 0,73) · errori 2 su 60 · analogie dichiarate 0 · segnalazioni del critico 1, errori introdotti 0 · 1543 parole (limite 1500) · Gulpease 54,1

Il risultato rivendicato è l'ipotesi di Riemann generalizzata per le funzioni L di Dirichlet. Per ogni carattere di Dirichlet primitivo χ, ogni zero di L(s,χ) nella striscia 0 < Re(s) < 1 sta sulla retta Re(s) = 1/2. Limitarsi ai caratteri primitivi non costa nulla, perché togliere fattori di Eulero non introduce zeri in Re(s) > 0. Alpöge scrive di aspettarsi, con più tempo, anche l'ipotesi di Riemann estesa, ma non la rivendica.

Sullo stato del risultato le fonti dicono questo. Alpöge afferma di aver formalizzato l'argomento in Lean insieme a Claude, "senza assunzioni". Pubblica soltanto il codice Lean, perché una versione leggibile non esiste ancora: la versione generata automaticamente supera le 250.000 pagine. La nota di Robin Zhang, su cui si basa quasi tutto ciò che segue, si dichiara "preliminare" e parla di "dimostrazione proposta". Le fonti non riferiscono di controlli indipendenti sul fatto che l'enunciato formalizzato coincida con quello voluto.

Il punto di partenza è classico. La dimostrazione studia la derivata logaritmica, −L'/L(s,χ) = Σ Λ(n)χ(n)n^(−s), attraverso la media di Riesz del primo ordine:

S_χ(x) = Σ_{n≤x} Λ(n)χ(n)(x/n − 1).

La sua trasformata di Mellin, ∫_1^∞ S_χ(x) x^(−s−1) dx, vale −L'(s,χ)/(s(s−1)L(s,χ)) per Re(s) > 1. Uno zero nella striscia critica diventa quindi un polo, e una stima di crescita su S_χ ne vincola la posizione. Il possibile polo in s = 1 si elimina con una correzione:

- per χ non principale, G_χ(x) = S_χ(x) + x·L'(1,χ)/L(1,χ);
- per ζ, G_1(x) = Σ_{n≤x} Λ(n)(x/n − 1) − x log x + (1+γ)x.

Per ψ primitivo di ordine r, sia X_ψ l'insieme dei caratteri primitivi che inducono 1, ψ, …, ψ^(r−1). Si forma la combinazione

G_ψ = G_1 + (1/(3r+1)) Σ_{χ∈X_ψ, χ≠1} Re G_χ.

In uno zero ρ di una qualunque di queste L, il residuo della trasformata di G_ψ è 1/(ρ(1−ρ)) per una somma pesata e positiva di molteplicità. Dunque ρ resta un polo anche se più funzioni L si annullano insieme. Tutte le potenze di ψ compaiono perché, più avanti, l'ortogonalità dei caratteri serve a imporre condizioni sui Frobenius.

Il cuore analitico-aritmetico è la Proposizione 1.2. Per ogni η > 0 e ogni A ≥ 2 esiste Y ≥ A tale che

G_ψ(x) ≤ x^(1/2+η) per ogni x in [Y, Y^(3/2)].

La stima è unilaterale e vale solo su intervalli arbitrariamente lontani, non per ogni x grande. Secondo Zhang, la Sezione 2 della dimostrazione mostra che questo basta a escludere zeri fuori dalla retta critica. Lo schema di Zhang cita qui Landau, Guinand, Turán e Weil, e Alpöge annota che "Guinand-Weil aveva il segno". Il dettaglio di questo passaggio non compare negli estratti che ho a disposizione.

Resta da capire come si ottiene una stima di qualità √x su una somma sulle potenze di primi. L'idea guida è la formula del prodotto: se un intero algebrico non nullo è molto divisibile nei primi finiti, i suoi valori assoluti archimedei non possono essere tutti piccoli. La dimostrazione costruisce dei periodi automorfi, normalizzati per prendere valori in un campo di numeri K, in modo che:

- le loro valutazioni nei primi finiti siano minorate da espressioni che contengono le somme G_χ;
- le loro dimensioni archimedee siano maggiorate.

Il confronto fra i due lati controlla G_ψ. La difficoltà è conservare una precisione vicina a √x mentre variano campi di numeri e forme automorfe.

Il contesto è il seguente. E è un campo CM abeliano che contiene il campo tagliato da ψ, ed E+ è il suo sottocampo totalmente reale massimale; si lavora con gruppi unitari di spazi hermitiani su E. Il periodo iniziale è un periodo di Bessel nel senso di Gan–Gross–Prasad. Si prende una forma cuspidale g su U(Y_0), se ne estrae un coefficiente di Fourier integrando lungo un sottogruppo unipotente, e lo si accoppia con una forma f su U(X_0), dove X_0 ⊂ Y_0 e X_0 è totalmente definito.

Poi si applica ripetutamente la corrispondenza theta di Weil–Howe. Si ottengono due catene di m sollevamenti, su U(X_j) e U(Y_j) per 0 ≤ j ≤ m, con tutti gli X_j totalmente definiti e Y_m totalmente definito alla fine. Le identità seesaw di Kudla collegano il periodo di Bessel iniziale all'accoppiamento finale, che è una restrizione per U(Y_m) ⊂ U(X_m), passando per periodi di Fourier–Jacobi. Ogni sollevamento aggiunge termini alla minorazione delle valutazioni.

Qui Alpöge propone un'analogia esplicita, e va letta come tale. Nella dimostrazione di Stepanov dell'ipotesi di Riemann sui campi di funzioni si usa un divisore con molteplicità. Sugli interi la molteplicità è difficile da trovare: sarebbe qualcosa come "derivare i numeri interi". Nell'argomento ogni sollevamento theta imita un ordine di molteplicità. La frase che Alpöge cita come illuminante è il suggerimento di Claude: per una somma di von Mangoldt di lunghezza X, la catena deve avere lunghezza √X.

I sollevamenti cambiano anche le norme di Petersson e le dimensioni degli spazi, e le costanti contano, perché nei G_χ il termine principale è già stato sottratto. Gli strumenti sono:

- le formule di Rallis e di Gan–Qiu–Takeda, che esprimono le norme dei sollevamenti tramite valori speciali di funzioni L e integrali locali;
- la formula delle dimensioni di Weyl e conteggi pesati di reticoli hermitiani, alla Siegel (formula della massa);
- i periodi di varietà abeliane CM che compaiono nella normalizzazione, legati alle derivate logaritmiche delle L di Dirichlet tramite Chowla–Selberg e Anderson.

Combinando questi ingredienti si ritrova esattamente il termine principale (Proposizione 3.1 e identità della Sezione 4.5), e restano solo gli errori.

Il lato archimedeo usa la geometria di Arakelov. Si considerano:

- reticoli M_α di forme automorfe algebriche alla Gross su U(X_0), indicizzati dai pesi massimi α;
- un reticolo M_W, ottenuto da sollevamenti theta "verso il basso" da U(Y_m), in uno spazio finito-dimensionale W di forme test su U(Y_0).

La divisibilità ha un significato preciso. Esistono un sottoreticolo di indice finito M'_α e un ideale frazionario a_α tali che il periodo normalizzato P_α(M'_α, M_W) è contenuto in a_α. Riscalando, si ottengono mappe intere b_α da N_α = a_α^(−1) M'_α verso C = Hom(M_W, O_K).

Le norme di queste mappe servono a minorare la pendenza media μ(C). Questo però funziona solo se le immagini generano quasi tutto il duale di W, e anche dopo piccole perdite di dimensione nei domini (Lemma 4.2). Per gestirlo si usano la filtrazione di Harder–Narasimhan dei reticoli hermitiani (Stuhler, Grayson) e la disuguaglianza delle pendenze di Bost.

Servono inoltre maggiorazioni dei covolumi di M_α. Qui le forme automorfe olomorfe vengono viste come sezioni di fibrati su compattificazioni aritmetiche (Faltings–Chai) di spazi di moduli di varietà abeliane con azione di O_E. Intervengono:

- le formule di Hilbert–Samuel aritmetiche di Gillet–Soulé e di Zhang;
- i minimi successivi di Zhang e il criterio di Moriwaki;
- al primi finiti, le stime di Fargues sulle mappe di Hodge–Tate e la teoria di Dieudonné prismatica di Anschütz–Le Bras.

C'è poi il problema dei denominatori. Le formule per le norme valgono per autoforme di Hecke. Proiettare su autospazi di Hecke, però, non spezza un reticolo intero: può introdurre denominatori che cancellano parte della divisibilità conquistata. Per controllarli si studiano le congruenze fra autovalori di Hecke tramite rappresentazioni di Galois. Si passa a GL_n per cambiamento di base e si usano le rappresentazioni costruite da Clozel–Harris–Labesse, Shin e Chenevier–Harris.

Gli addendi unidimensionali prodotti dai sollevamenti theta portano a gruppi S_ℓ(E,j). Sono nuclei di restrizione nella H^1 non ramificata fuori da ℓ, con coefficienti in Q_ℓ/Z_ℓ(−j). Per stimarli:

- la dualità di Poitou–Tate li lega alla H^2;
- un argomento di deformazione alla Wiles, Taylor–Wiles e Clozel–Harris–Taylor confronta deformazioni e congruenze;
- il sistema di Eulero di Kato serve a far annullare certi gruppi di Selmer di rappresentazioni modulari bidimensionali;
- la teoria di Iwasawa, insieme all'annullamento dell'invariante μ di Ferrero–Washington, permette di salire lungo torri ciclotomiche quando pesi e twist crescono.

Alpöge descrive questo passaggio come una lotta per "un indebolimento significativo di Vandiver". Restano alcuni twist eccezionali che richiedono stime più grossolane. È qui che serve la libertà di scegliere l'intervallo [Y, Y^(3/2)]: lo si prende in modo che gli indici eccezionali siano piccoli rispetto a x.

Le condizioni di Frobenius che compaiono nelle valutazioni, tradotte con l'ortogonalità dei caratteri, producono termini del tipo G_χ(a_t/w_{j,ρ}), associati a un insieme di posti complessi di E. Questo insieme deve essere grande, ma la precisione peggiora se troppi suoi posti cadono in un breve segmento di un'orbita di Frobenius. Per conciliare le due esigenze si adatta la costruzione di Behrend di insiemi grandi senza progressioni aritmetiche di tre termini, che limita ogni intersezione rilevante ad al più due posti. Ai posti rimanenti si usano regioni senza zeri note. Alpöge stesso considera questo trucco "ovviamente non necessario".

Alla fine, i due errori principali nella stima di G_ψ(x) hanno ordine x/m e m, a meno di potenze arbitrariamente piccole di x. Scegliendo m dell'ordine di √x entrambi diventano circa √x, ed è da qui che nasce l'esponente 1/2. Campi di numeri, pesi massimi e posti complessi vanno scelti insieme a m (Proposizione 6.3 e Lemma 6.1).

Alpöge sottolinea che l'argomento è "incredibilmente lungo", che potrebbe contenere scelte subottimali e che si aspetta semplificazioni rapide. Ammette anche che alcune parti della sua cronologia, dove l'esperto era Claude, sono parafrasi che "potrebbero non avere alcun senso", e rimanda al codice Lean come riferimento definitivo.

### claude_overview-L4-s07

*panoramica, spiegazione 8 di 8.* Fatti del livello: 21 sì, 4 in parte, 5 no (copertura 0,77) · errori 2 su 62 · analogie dichiarate 0 · segnalazioni del critico 0, errori introdotti 0 · 1451 parole (limite 1500) · Gulpease 56,4

Il 20 novembre 2026 Levent Alpöge ha annunciato di aver dimostrato, lavorando con Claude, l'ipotesi di Riemann generalizzata per le funzioni L di Dirichlet. L'enunciato è il seguente: per ogni carattere di Dirichlet primitivo χ, ogni zero di L(s,χ) nella striscia 0 < Re s < 1 sta sulla retta Re s = 1/2. Basta trattare i caratteri primitivi, perché togliere fattori di Euler non introduce zeri in Re s > 0.

Lo stato della dimostrazione è insolito. Non esiste un articolo leggibile. Esiste soltanto una formalizzazione in Lean, distribuita in quattordici archivi, che secondo Alpöge è completa e «senza assunzioni». Alpöge ha scelto di non pubblicare il documento esteso, oltre 250.000 pagine, che si potrebbe generare automaticamente. Quanto segue ricostruisce l'argomento dalla sua nota e da una «nota preliminare» di Robin Zhang, che parla di dimostrazione «proposta». Le fonti non riferiscono verifiche indipendenti al di là di queste. Alpöge stesso avverte che nelle parti più lontane dalla sua competenza la cronologia parafrasa riassunti di Claude e potrebbe essere imprecisa.

Il punto di partenza è classico. Per x ≥ 1 si considera la media di Riesz del primo ordine

Sχ(x) = Σ_{n≤x} Λ(n)χ(n)(x/n − 1),

la cui trasformata di Mellin, ∫₁^∞ Sχ(x)x^{−s−1}dx, vale −L′(s,χ)/(s(s−1)L(s,χ)) per Re s > 1. Ogni zero nella striscia critica diventa un polo, quindi stime di crescita su Sχ vincolano la posizione degli zeri. Per eliminare il polo spurio in s = 1 si corregge la funzione. Per χ non principale si pone Gχ(x) = Sχ(x) + x·L′(1,χ)/L(1,χ). Per ζ si usa

G₁(x) = Σ_{n≤x} Λ(n)(x/n − 1) − x log x + (1+γ)x.

Poi, dato ψ primitivo di ordine r, si prende la combinazione positiva

Gψ(x) = G₁(x) + (1/(3r+1)) Σ Re Gχ(x),

dove la somma corre sui caratteri primitivi χ ≠ 1 che inducono le potenze di ψ. Ci entrano tutte le potenze perché più avanti l'ortogonalità dei caratteri serve a imporre condizioni di Frobenius. Poiché la famiglia è chiusa per coniugio, nel residuo della trasformata di Mellin in uno zero ρ compare la somma pesata, con pesi positivi, delle molteplicità di ρ: non ci possono essere cancellazioni.

Il cuore della dimostrazione è la Proposizione 1.2. Per ogni η > 0 e ogni A ≥ 2 esiste Y ≥ A tale che Gψ(x) ≤ x^{1/2+η} per ogni x ∈ [Y, Y^{3/2}]. La stima è solo dall'alto e vale solo su intervalli arbitrariamente lontani, non per tutti gli x grandi. Che basti comunque a escludere zeri fuori dalla retta critica lo mostra la sezione 2 della nota di Zhang, che rimanda a Landau, Guinand, Turán e Weil. Il testo che ho a disposizione non descrive quel passaggio, quindi non lo ricostruisco.

Per ottenere la stima su Gψ, il meccanismo di fondo è la formula del prodotto: un intero algebrico non nullo molto divisibile ai primi finiti non può essere piccolo a tutti i posti archimedei. Si costruiscono allora numeri algebrici, cioè periodi automorfi normalizzati. Le valutazioni p-adiche di questi periodi sono limitate dal basso da somme su potenze di primi. Le loro taglie archimedee sono limitate dall'alto. Il confronto fra le due stime controlla Gψ, a patto di mantenere un errore vicino a √x.

Alpöge descrive l'idea con un'analogia, che è sua e va presa come tale. Nel metodo di Stepanov per l'ipotesi di Riemann sui campi di funzioni si usa un divisore con molteplicità. Sugli interi la molteplicità è difficile da trovare: sarebbe come «derivare i numeri interi». Qui il ruolo della molteplicità è svolto da sollevamenti theta concatenati, ciascuno dei quali «imita» un ordine di molteplicità.

Concretamente, sia E un campo CM abeliano che contiene il campo tagliato da ψ, e sia E⁺ il suo sottocampo totalmente reale massimale. Si lavora con gruppi unitari su E⁺. Il periodo iniziale è un periodo di Bessel, nel senso di Gan–Gross–Prasad, fra una forma cuspidale f su U(X₀), con X₀ totalmente definito, e una g su U(Y₀) con X₀ ⊂ Y₀. Si applica poi m volte la corrispondenza theta di Weil–Howe su entrambi i lati, fino a gruppi U(X_m) e U(Y_m) entrambi totalmente definiti. Le identità seesaw di Kudla legano il periodo di Bessel iniziale a un accoppiamento di restrizione finale, passando per periodi di Fourier–Jacobi, e ogni sollevamento aggiunge termini alla stima dal basso delle valutazioni.

Le condizioni di Frobenius che compaiono in queste stime vengono tradotte, tramite l'ortogonalità dei caratteri, in termini Gχ(a_t/w_{j,ρ}) (Proposizione 3.1). Poiché Gχ ha già il termine principale sottratto, le costanti devono tornare esattamente. Le norme di Petersson dei sollevamenti si esprimono con valori speciali di funzioni L e integrali locali (Rallis; Gan–Qiu–Takeda). Le dimensioni si calcolano con la formula di Weyl e con conteggi pesati di reticoli hermitiani alla Siegel. La normalizzazione usa i periodi di varietà abeliane CM, che si collegano a L′/L(1,χ) tramite Chowla–Selberg e Anderson. Il termine principale viene così ricostruito in modo esplicito (sezione 4.5).

Sul lato archimedeo l'argomento è arakeloviano. Si costruiscono O_K-reticoli M_α di forme automorfe algebriche alla Gross, un sottoreticolo M′_α e un ideale frazionario a_α tali che P_α(M′_α, M_W) ⊆ a_α. È questo il significato preciso di «divisibilità dei periodi». Ne seguono mappe integrali b_α : N_α → C = Hom(M_W, O_K), con cui si stima dal basso la pendenza media di C. Per questo servono stime di covolume per M_α. Le si ottiene vedendo le forme come sezioni di fibrati su compattificazioni aritmetiche di spazi di moduli di varietà abeliane con azione di O_E (Faltings–Chai), con la formula di Hilbert–Samuel aritmetica (Gillet–Soulé, Zhang), i minimi successivi di Zhang e il criterio di Moriwaki. Ai primi finiti il controllo dei differenziali invarianti passa per le stime di Fargues sulle mappe di Hodge–Tate e per la teoria di Dieudonné prismatica di Anschütz–Le Bras.

Resta un problema: le norme delle b_α non bastano se le immagini sono degeneri. Si dimostra quindi che i funzionali-periodo ricoprono quasi tutto W^∨. Lo strumento è la filtrazione di Harder–Narasimhan per reticoli hermitiani (Stuhler, Grayson), insieme alla disuguaglianza delle pendenze di Bost e al Lemma 4.2 (Proposizione 4.3).

Altri due ingredienti meritano attenzione. Il primo è combinatorio. Le w_{j,ρ} fissano i blocchi di parametri di Harish-Chandra aggiunti da ciascun sollevamento ai posti complessi ρ di E. L'insieme T₂ di posti su cui si fa questa scelta deve essere grande, ma non deve concentrarsi in segmenti brevi di un'orbita di Frobenius. Per questo si adatta la costruzione di Behrend di insiemi senza progressioni aritmetiche di tre termini, così che ogni intersezione rilevante contenga al più due posti. Ai posti rimanenti bastano regioni libere da zeri note. Alpöge ritiene che questo trucco sia quasi certamente superfluo.

Il secondo ingrediente riguarda i denominatori. Proiettare sugli autospazi di Hecke può introdurre denominatori che mangiano divisibilità. Per controllarli si studiano le congruenze fra autovalori di Hecke attraverso le rappresentazioni di Galois associate: cambio di base a GL_n e i risultati di Clozel–Harris–Labesse, Shin e Chenevier–Harris. Compaiono così i gruppi S_ℓ(E,j), nuclei della restrizione locale sopra ℓ nella coomologia H¹ non ramificata fuori da ℓ a coefficienti Q_ℓ/Z_ℓ(−j). Li si stima con la dualità di Poitou–Tate e con argomenti di deformazione alla Wiles, Taylor–Wiles e Clozel–Harris–Taylor. Per certi casi riducibili si usa il sistema di Eulero di Kato. Infine si fa crescere E lungo torri ciclotomiche con la teoria di Iwasawa e con Ferrero–Washington (μ = 0). Alcuni twist eccezionali si gestiscono scegliendo opportunamente l'intervallo [Y, Y^{3/2}], ed è qui che quella libertà diventa essenziale. Alpöge descrive questa parte come una «significativa versione indebolita» della congettura di Vandiver.

Rimane da capire da dove venga l'esponente 1/2. Fatti tutti i conti, i due errori principali nella stima di Gψ(x) sono di ordine x/m e m, a meno di fattori x^ε. Scegliendo m dell'ordine di √x, entrambi sono vicini a √x. Alpöge racconta che fu Claude a proporre una catena di sollevamenti theta di lunghezza √X, e commenta: «e del resto, che altro potrebbe essere?» Campi, pesi e posti vanno scelti insieme a m (Proposizione 6.3). Il Lemma 6.1 dà allora la Proposizione 1.2, e da questa segue la congettura.

Sul processo, Alpöge dice di aver guidato il lavoro verso la situazione analoga a un «modello giocattolo» in cui combinava due idee. Riconosce però di avere poca padronanza delle forme automorfe su gruppi di rango alto e dice che Claude lo ha nettamente superato nella fase finale. La cronologia va dal 6 ottobre 2026, con il «determinante di Stepanov», al 16 novembre, con la conclusione. Alpöge stesso considera l'argomento attuale lunghissimo, pieno probabilmente di scelte subottimali, e destinato a semplificazioni rapide. Si propone di capirlo a fondo e di scriverlo in forma leggibile. Dice inoltre di aspettarsi che il metodo, con più tempo, porti anche all'ipotesi di Riemann «estesa», ma per ora si tratta solo di un'aspettativa.
