# La banalità della dimostrazione: piano di lavoro

> **Per chi esegue:** sotto-skill richiesta: superpowers:executing-plans (o
> superpowers:subagent-driven-development). I passi usano le caselle (`- [ ]`).

**Obiettivo:** misurare che cosa si perde e che cosa diventa falso quando un'AI spiega a quattro
livelli la dimostrazione dell'ipotesi di Riemann generalizzata annunciata da Alpöge, e cercare gli
errori che la semplificazione introduce o rivela.

**Architettura:** un pacchetto Python (`src/banalita/`) con un modulo per responsabilità
(fonti, leggibilità, spesa, fatti, richieste, batch, giudice, critico, metriche); le chiamate a
Claude passano dalla Batch API con un contatore di spesa; il lavoro sulla L4 sta in `gpu/` e
gira in `~/rnd/banalita`; i risultati sono file JSONL in `results/`; l'analisi in `analysis/`
legge solo i JSONL.

**Stack:** Python ≥ 3.11 con uv, `anthropic` (SDK ufficiale), `pyyaml`, `numpy`, `pytest`;
`pdftotext` (poppler) per il testo della panoramica; sulla L4 vLLM con
`cyankiwi/Qwen3.8-27B-AWQ-INT4` e `transformers` per il modello NLI.

**Progetto:** `docs/design.it.md` (approvato dall'autore il 22/11/2026). Chi esegue legge
entrambi.

## Vincoli globali

- Modelli: `claude-opus-5-5` per spiegatore, giudice e critico; `claude-sonnet-5-5` solo come
  secondo giudice sul campione; nessun altro ID, nessun suffisso di data.
- Spesa API: tetto **60 dollari** in tutto, Batch API per ogni fase che può aspettare.
- Prezzi in dollari per milione di token (Batch: metà di ogni voce):
  Opus 5.5 ingresso 4, uscita 20, lettura cache 0,20, scrittura cache 5 minuti 5, 1 ora 8;
  Sonnet 5.5 ingresso 2, uscita 10, lettura cache 0,10, scrittura 5 minuti 2,5, 1 ora 4.
  Nei batch la cache dei PDF usa il TTL di un'ora.
- Livelli: L1 bambino di dieci anni (300 parole), L2 liceo (600), L3 laureato in matematica non
  specialista (1.000), L4 teorico dei numeri (1.500).
- Bracci: `claude_full` (F1 + F2 in PDF), `claude_overview` (F1 + sezione 1 di F2 in testo),
  `qwen_overview` (stesso materiale, sulla L4). Otto spiegazioni per braccio e livello: 96.
- Etichette delle affermazioni: `supported`, `unsupported`, `contradicted`,
  `declared_analogy`, `analogy_as_fact`; tipi `proof` e `context`. Errori = `contradicted` +
  `analogy_as_fact`.
- Caselle della caccia all'errore: `introduced`, `in_source`, `false_alarm`.
- Fonti: mai nel repository (`sources/` in `.gitignore`); nel repository URL e SHA-256.
- Chiave API solo da `ANTHROPIC_API_KEY` nell'ambiente; nessun link di sessione, nessun dato
  privato, nessun accenno a repository privati nei file pubblici.
- Licenze: codice MIT (`LICENSE`), dati e spiegazioni CC BY-SA 4.0 (`LICENSE-data`).
- L4: solo quando `nvidia-smi` mostra la GPU libera da altri processi; tutto in
  `~/rnd/banalita` (cache comprese); a fine corsa si cancella solo quella cartella.
- Lingua dei prompt, dei testi e del protocollo: italiano; identificatori del codice in
  inglese.

## Punti da guardare in revisione

1. Un batch restituisce i risultati in ordine sparso e alcuni in errore o scaduti: si
   abbinano per `custom_id`, e gli errati si rimettono in coda una volta sola.
2. Il ragionamento adattivo fa uscire molti più token del previsto: il contatore stima il
   costo prima di inviare un batch con un tetto di uscita per richiesta, e si ferma prima di
   superare i 60 dollari.
3. Una risposta con `stop_reason` `refusal` o `max_tokens`: si registra e non entra nelle
   misure, non manda in errore la fase.
4. La cache dei PDF non viene letta (`cache_read_input_tokens` a zero su richieste che
   dovrebbero leggerla): si segnala, perché moltiplica il costo.
5. Il testo italiano con apostrofi («l'ipotesi»), cifre, abbreviazioni («p. 495») e
   puntini di sospensione: il Gulpease deve contare parole, lettere e frasi come la formula
   prevede.

---

### Compito 1: impianto e fonti

**File:**
- Crea: `pyproject.toml`, `LICENSE`, `LICENSE-data`, `.gitignore`, `data/sources.json`,
  `src/banalita/__init__.py`, `src/banalita/sources.py`, `scripts/fetch_sources.py`
- Test: `tests/test_sources.py`

**Interfacce:**
- Produce: `load_sources(path="data/sources.json") -> dict[str, Source]`, con
  `Source(id: str, url: str, sha256: str, local: Path)`;
  `verify(source: Source) -> None` (solleva `SourceMismatch` se l'hash non torna);
  `overview_text(pdf: Path, first_page=2, last_page=14) -> str` (testo della sezione 1 di
  F2 con `pdftotext -layout -f -l`).

- [ ] Test: `test_verify_rejects_wrong_hash` (un file temporaneo con un hash sbagliato
  solleva `SourceMismatch`), `test_verify_accepts_right_hash`,
  `test_overview_text_uses_page_range` (con un PDF di prova di tre pagine generato nel test,
  le pagine 2-3 contengono il testo atteso e non quello della pagina 1).
- [ ] Eseguire `uv run pytest tests/test_sources.py`: falliscono.
- [ ] Scrivere `sources.py`; `data/sources.json` con F1, F2, F3a (dichiarazione Lean), F3b
  (pagina di Sutherland), URL del progetto e SHA-256 delle copie scaricate il 22/11/2026
  (F1 e F2 già presenti nello scratchpad: ricalcolare l'hash, non copiarlo).
- [ ] `scripts/fetch_sources.py` scarica in `sources/` e verifica; `sources/` in
  `.gitignore`.
- [ ] Test verdi; commit `feat: fonti con hash e testo della panoramica`.

### Compito 2: indice Gulpease

**File:** crea `src/banalita/readability.py`; test `tests/test_readability.py`

**Interfacce:** produce `gulpease(text: str) -> float` e `counts(text: str) -> Counts`
(`letters`, `words`, `sentences`).

Formula: `89 + (300 * frasi - 10 * lettere) / parole`. Lettere: solo caratteri alfabetici
(lettere accentate comprese). Parole: sequenze separate da spazi, con l'apostrofo che separa
(«l'ipotesi» = due parole). Frasi: terminate da `.`, `!`, `?`, `…` seguiti da spazio o fine
testo; un punto dopo una sola lettera o dopo un'abbreviazione di una lista fissa (`p`, `pp`,
`ecc`, `es`, `n`) non chiude la frase; i numeri decimali (`19.344`, `0,577`) non chiudono.

- [ ] Test: `test_gulpease_known_value` («Il gatto dorme. Il cane corre.»: 6 parole,
  23 lettere, 2 frasi, 89 + (600 - 230) / 6 = 150,67); `test_apostrophe_splits_words`;
  `test_abbreviation_does_not_end_sentence` («Vedi p. 495 del testo.» è una frase);
  `test_decimal_does_not_end_sentence`; `test_ellipsis_ends_sentence`;
  `test_empty_text_raises_value_error`.
- [ ] Rossi, poi `readability.py`, poi verdi; commit `feat: indice Gulpease`.

### Compito 3: contatore di spesa

**File:** crea `src/banalita/costs.py`; test `tests/test_costs.py`

**Interfacce:** produce `PRICES` (i valori dei vincoli globali), `cost(usage: dict, model: str,
batch: bool, cache_ttl: str = "1h") -> float`, classe `Ledger(path: Path, cap: float = 60.0)`
con `spent() -> float`, `can_afford(estimate: float) -> bool`, `record(phase: str, usage: dict,
model: str, batch: bool) -> float`, eccezione `BudgetExceeded`; il registro è
`results/spend.jsonl`.

- [ ] Test: `test_cost_opus_batch_halves` (1M ingresso + 1M uscita in batch = 12 dollari);
  `test_cache_read_and_write_priced` (1M letti = 0,20, 1M scritti a 1 ora = 8, metà in
  batch); `test_ledger_refuses_over_cap` (speso 55, stima 6: `can_afford` falso);
  `test_ledger_persists_across_instances`; `test_cache_miss_warning` (`record` con
  `cache_read_input_tokens` 0 e `phase` marcata come «a cache» scrive un avviso nel registro).
- [ ] Rossi, `costs.py`, verdi; commit `feat: contatore di spesa con tetto`.

### Compito 4: fatti di riferimento

**File:** crea `data/facts.yaml`, `src/banalita/facts.py`; test `tests/test_facts.py`

**Interfacce:** produce `load_facts(path="data/facts.yaml") -> list[Fact]` con
`Fact(id: str, group: str, text: str, source: str, page: int, quote: str, min_level: int)`;
gruppi ammessi `statement`, `architecture`, `ingredients`, `status`, `limits`;
`facts_for_level(facts, level: int) -> list[Fact]` (quelli con `min_level <= level`).

- [ ] Test: `test_rejects_unknown_group`, `test_rejects_level_out_of_range`,
  `test_rejects_missing_quote`, `test_facts_for_level_filters`, `test_ids_unique`, e
  `test_repository_facts_valid` (il file vero passa la validazione e ha fra 20 e 30 fatti).
- [ ] Rossi, `facts.py`.
- [ ] Scrivere `data/facts.yaml` leggendo F1, F2 e F3 (ogni fatto con pagina e citazione
  letterale). Poi un secondo agente, a contesto pulito, riscontra ogni citazione e pagina
  sulle fonti e propone correzioni; si applicano.
- [ ] Verdi; commit `data: fatti di riferimento riscontrati sulle fonti`.

### Compito 5: richieste degli spiegatori

**File:** crea `prompts/explain.it.md` (un modello con i segnaposto `{lettore}` e
`{parole}`), `src/banalita/requests.py`; test `tests/test_requests.py`

**Interfacce:**
- Consuma: `Source`, `overview_text` (compito 1).
- Produce: `LEVELS = {1: ("un bambino di dieci anni", 300), 2: (...), 3: (...), 4: (...)}`;
  `explain_request(arm: str, level: int, sample: int) -> dict` (parametri per
  `messages.create`: `model`, `max_tokens`, `output_config` con `effort`, `system`,
  `messages`); `custom_id(kind: str, arm: str, level: int, sample: int) -> str`.

Nel braccio `claude_full` i due PDF sono blocchi `document` in base64, prima del testo, con
`cache_control` di un'ora sull'ultimo; in `claude_overview` F1 è PDF e la panoramica è testo.

- [ ] Test: `test_full_arm_has_two_documents_cached`, `test_overview_arm_has_text_overview`,
  `test_prompt_states_reader_and_word_cap` (per ogni livello), `test_custom_id_roundtrip`,
  `test_unknown_arm_raises`.
- [ ] Rossi, `requests.py` e prompt, verdi; commit `feat: richieste degli spiegatori`.

### Compito 6: esecutore dei batch

**File:** crea `src/banalita/batch.py`, `scripts/run_phase.py`; test `tests/test_batch.py`

**Interfacce:**
- Consuma: `Ledger` (compito 3), `custom_id` (compito 5).
- Produce: `run_batch(requests: dict[str, dict], phase: str, ledger: Ledger, client,
  out: Path, poll_seconds: int = 60) -> dict[str, Result]`, con
  `Result(custom_id: str, status: str, text: str | None, parsed: dict | None, usage: dict,
  stop_reason: str | None)`; scrive una riga JSONL per risultato; `scripts/run_phase.py
  --phase explain|judge|critic|verify|judge2 [--dry-run]`.

Prima di inviare stima il costo con il tetto di uscita per richiesta e chiede a
`ledger.can_afford`; i risultati si abbinano per `custom_id`; `errored` e `expired` si
rimettono in coda una volta; `refusal` e `max_tokens` si registrano con quello stato.

- [ ] Test con un client finto: `test_results_matched_by_custom_id_out_of_order`,
  `test_errored_resubmitted_once`, `test_refusal_recorded_not_raised`,
  `test_refuses_when_estimate_exceeds_cap` (nessuna chiamata al client),
  `test_dry_run_sends_nothing`, `test_jsonl_written_one_line_per_result`.
- [ ] Rossi, `batch.py`, verdi; commit `feat: batch con abbinamento e tetto`.

### Compito 7: giudice

**File:** crea `prompts/judge.it.md`, `src/banalita/judge.py`; test `tests/test_judge.py`

**Interfacce:**
- Consuma: `Fact`, `facts_for_level` (compito 4); requests e batch (5, 6).
- Produce: `blind(text: str) -> str` (toglie intestazioni, firme, nomi di modelli e
  formattazione markdown, normalizza gli spazi); `judge_request(explanation_id: str, text: str,
  level: int, model: str = "claude-opus-5-5") -> dict` con output strutturato secondo
  `JUDGE_SCHEMA`: `claims[]` (`text`, `kind`, `label`, `source`, `page`, `quote`) e
  `coverage[]` (`fact_id`, `verdict` in `yes|partial|no`); `parse_judgment(parsed: dict) ->
  Judgment`.

Il prompt contiene la regola delle affermazioni del progetto (§ 6) con tre esempi per
etichetta, la lista dei fatti del livello, e le fonti intere in cache; il giudice non vede il
braccio.

- [ ] Test: `test_blind_removes_model_names_and_markdown`,
  `test_schema_rejects_unknown_label`, `test_coverage_only_for_level_facts`,
  `test_request_has_no_arm_information`, `test_parse_judgment_roundtrip`.
- [ ] Rossi, codice e prompt, verdi; commit `feat: giudice alla cieca`.

### Compito 8: critico e verifica delle segnalazioni

**File:** crea `prompts/critic.it.md`, `prompts/verify.it.md`, `src/banalita/critic.py`; test
`tests/test_critic.py`

**Interfacce:** produce `critic_request(target_id: str, text: str) -> dict` (solo il testo,
nessuna fonte; output `alerts[]` con `passage` e `problem`); `verify_request(target_id: str,
text: str, alerts: list[dict]) -> dict` (fonti in cache; per ogni segnalazione `category` in
`introduced|in_source|false_alarm`, `reason`, `source`, `page`); il bersaglio `F2_overview`
fa leggere al critico la panoramica stessa.

- [ ] Test: `test_critic_request_has_no_sources`, `test_verify_categories_closed_set`,
  `test_source_target_uses_overview`, `test_empty_alert_list_skips_verify`.
- [ ] Rossi, codice e prompt, verdi; commit `feat: caccia all'errore`.

### Compito 9: metriche e verdetti

**File:** crea `src/banalita/metrics.py`, `analysis/report.py`; test `tests/test_metrics.py`

**Interfacce:** produce `wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]`,
`cohen_kappa(a: list[str], b: list[str]) -> float`, `coverage(judgment, facts) -> float`
(`yes` = 1, `partial` = 0,5), `error_rate(judgment) -> tuple[int, int]` (errori, affermazioni
`proof` + errori `context`), `verdicts(table) -> dict[str, str]` per P1-P6 con le soglie del
protocollo; `analysis/report.py` scrive `results/report.md` e `results/tables/*.csv`.

- [ ] Test: `test_wilson_known_values` (k = 5, n = 100: circa 0,0215-0,1118),
  `test_wilson_zero_successes`, `test_kappa_perfect_and_chance`, `test_coverage_partial_half`,
  `test_p4_needs_upper_bound` (errori 4/100, limite superiore 0,098: passa; 1/30, stima
  3,3% ma limite 0,167: non passa).
- [ ] Rossi, codice, verdi; commit `feat: metriche e verdetti`.

### Compito 10: pagina di etichettatura per l'autore

**File:** crea `labeling/sample.py`, `labeling/make_page.py`, `analysis/human.py`; test
`tests/test_labeling.py`

**Interfacce:** produce `sample_claims(judgments, n: int = 60, seed: int = 20261122) ->
list[dict]` (solo L1 e L2, a strati sulle etichette del giudice, l'etichetta del giudice non
esce dal campione); `make_page(sample, sources) -> str` (HTML autonomo, leggibile al telefono:
affermazione, passo della fonte, tre bottoni, esporta un JSON); `human_vs_judge(labels,
judgments) -> dict` (precisione e richiamo per classe).

- [ ] Test: `test_sample_is_stratified_and_deterministic`, `test_page_hides_judge_labels`,
  `test_page_has_three_choices_per_claim`, `test_precision_recall_known_case`.
- [ ] Rossi, codice, verdi; commit `feat: etichettatura dell'autore`.

### Compito 11: lavoro sulla L4

**File:** crea `gpu/env.sh`, `gpu/setup.sh`, `gpu/explain_qwen.py`, `gpu/critic_qwen.py`,
`gpu/nli_check.py`, `gpu/run.sh`, `gpu/clean.sh`, `gpu/README.md`; test `tests/test_gpu.py`

**Interfacce:**
- Consuma: `LEVELS`, il prompt di `prompts/explain.it.md`, `overview_text` (compiti 1, 5).
- Produce: `results/explanations_qwen.jsonl` e `results/critic_qwen.jsonl` nello stesso
  formato di `Result`; `results/nli.jsonl` (`claim_id`, `entailment`, `neutral`,
  `contradiction`).

`env.sh` mette ogni cache sotto `RND=$HOME/rnd/banalita`; `run.sh` si rifiuta di partire se
`nvidia-smi` mostra processi che non sono suoi; `clean.sh` cancella solo un percorso che
finisce in `/rnd/banalita`. Il modello NLI è multilingue, scelto e scritto nel protocollo.

- [ ] Test: `test_clean_refuses_other_paths` (esegue `clean.sh` con `RND=/tmp/x/rnd`
  e con `RND=$HOME/rnd`: rifiuta), `test_qwen_prompt_matches_claude_overview_prompt`
  (stesso testo del braccio `claude_overview`), `test_env_keeps_caches_inside_rnd`.
- [ ] Rossi, codice, verdi; commit `feat: script per la L4`.

### Compito 12: protocollo registrato e repository pubblico

**File:** crea `PROTOCOL.it.md`, `PROTOCOL.md` (traduzione), `README.it.md`, `README.md`

Il protocollo fissa: domande, fonti con hash, fatti con hash di `data/facts.yaml`, prompt con
hash, bracci, livelli, campioni, etichette, estimatori, soglie di P1-P6 (dal progetto § 7,
con P4 come nei vincoli), modello NLI, tetto di spesa, e una sezione «Deviazioni» vuota.

- [ ] `uv run pytest`: tutto verde.
- [ ] Prova pilota a pagamento con un'autorizzazione esplicita: una spiegazione per braccio
  Claude e livello (8 richieste) e il loro giudizio, fuori batch. Controllare la lettura della
  cache e il costo reale; aggiornare le stime nel protocollo. Il pilota non entra nei
  risultati.
- [ ] Commit del protocollo; creare `paithon-it/banalita-della-dimostrazione` pubblico
  (`GH_TOKEN=$(gh auth token --user paithon-it)`) e spingere `main` **prima** di qualunque
  corsa.

### Compito 13: corse

- [ ] `run_phase.py --phase explain` (64 richieste Claude, in batch).
- [ ] Sulla L4, quando è libera: `gpu/run.sh explain` (32 spiegazioni Qwen).
- [ ] `--phase judge` (96), `--phase critic` (96 + panoramica), `--phase verify`,
  `--phase judge2` (Sonnet 5.5 su 24 spiegazioni scelte con il seme del protocollo).
- [ ] Sulla L4: `gpu/run.sh critic` e `gpu/run.sh nli`; poi `gpu/clean.sh`, e `nvidia-smi`
  e `ls ~/rnd` per verificare che di nostro non resti niente.
- [ ] Pagina di etichettatura all'autore; quando torna il JSON, `analysis/human.py`.
- [ ] `analysis/report.py`; risultati, spesa e deviazioni committati e spinti.

### Compito 14: saggio per «Pecore elettriche»

**File:** nel repository di paithon, in un worktree: `content/drafts/NNN-la-banalita-della-
dimostrazione.html` (numero dal massimo di tutti i branch), copertine chiara e scura, PDF.

- [ ] Stesura: `formato: saggio`, firma endjneer, figure SVG in palette con
  `figure-tema.py --apply`, risultati positivi nel corpo e ciò che non ha retto in appendice,
  la spiegazione L1 più fedele con la sua misura accanto, link al repository pubblico.
- [ ] Fact-check sui risultati e sulle fonti, revisione dell'italiano, `valida_bozza`.
- [ ] PR; dopo il merge dell'autore, import, anteprima e pubblicazione su sua decisione.
