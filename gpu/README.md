# Il lavoro sulla L4

La GPU è una NVIDIA L4 da 24 GB, su una macchina che non è dell'esperimento: si lavora solo in
`~/rnd/banalita`, con tutte le cache lì dentro (`gpu/env.sh`), e alla fine si cancella solo
quella cartella (`gpu/clean.sh`). `gpu/run.sh` non parte se la GPU ha già processi al lavoro.

```bash
# dalla macchina di lavoro: copia del repository e delle fonti
rsync -a --exclude .venv --exclude .git ./ gpu-host:rnd/banalita/repo/
# sulla macchina con la GPU
cd ~/rnd/banalita/repo
bash gpu/setup.sh          # ambiente con vLLM e transformers, i due modelli
bash gpu/run.sh explain    # 32 spiegazioni di Qwen3.8-27B (braccio qwen_overview)
bash gpu/run.sh critic     # il secondo critico, dopo le spiegazioni di Claude
bash gpu/run.sh nli        # il controllo NLI, dopo i giudizi
bash gpu/clean.sh          # cancella ~/rnd/banalita, e nient'altro
```

Qwen3.8-27B (`cyankiwi/Qwen3.8-27B-AWQ-INT4`) gira con il ragionamento acceso e i parametri di
campionamento consigliati per Qwen3 (temperatura 0,6, top-p 0,95, top-k 20); il ragionamento si
toglie dall'uscita. Il modello NLI è `MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7`.
