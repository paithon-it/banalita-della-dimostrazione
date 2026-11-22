"""Le chiamate a Claude attraverso Claude Code senza interfaccia (`claude -p`), al posto della
Batch API: stesso modello, stesse fonti (i PDF passano come documenti nell'ingresso
stream-json), stesso schema JSON (`--json-schema`), ma con l'abbonamento invece della chiave.

Ogni chiamata è isolata come nell'esperimento della 554: nessuno strumento, prompt di sistema
fisso al posto di quello di Claude Code, nessuna impostazione, nessun server MCP, nessun comando,
nessuna sessione salvata, ambiente minimo e cartella temporanea vuota. Mai `--bare`, che si
autentica solo con la chiave API. Una risposta che nomina file di progetto o memorie è
«contaminated» e non entra nelle misure.

I risultati sono gli stessi `Result` della Batch API; una corsa interrotta riparte saltando i
`custom_id` già riusciti. Il registro della spesa riporta il costo a listino che Claude Code
dichiara a ogni chiamata (con l'abbonamento non si paga a token: misura il consumo).
"""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import tempfile
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from banalita.batch import Result
from banalita.costs import Ledger

ENV_KEYS = ("HOME", "USER", "PATH", "LANG")
SUSPICIOUS = ("claude.md", "memory.md", "paithon", "superpowers", "security-review", "system-reminder")
TIMEOUT = 3600


def minimal_env() -> dict[str, str]:
    env = {k: os.environ[k] for k in ("HOME", "USER", "PATH") if k in os.environ}
    env["LANG"] = "C.UTF-8"
    return env


def build_command(params: dict) -> list[str]:
    cfg = params.get("output_config", {})
    system = "\n\n".join(b["text"] for b in params["system"])
    cmd = ["claude", "-p", "--input-format", "stream-json", "--output-format", "stream-json", "--verbose",
           "--model", params["model"], "--effort", cfg.get("effort", "high"),
           "--tools", "", "--system-prompt", system,
           "--setting-sources", "", "--strict-mcp-config", "--mcp-config", '{"mcpServers":{}}',
           "--disable-slash-commands", "--no-session-persistence", "--permission-mode", "default"]
    fmt = cfg.get("format")
    if fmt and fmt.get("type") == "json_schema":
        cmd += ["--json-schema", json.dumps(fmt["schema"], ensure_ascii=False)]
    return cmd


def build_stdin(params: dict) -> str:
    # I cache_control restano: Claude Code li rispetta, e senza un punto di cache dopo le fonti
    # ogni chiamata con un ultimo blocco diverso riscriverebbe tutto il prefisso.
    content = params["messages"][0]["content"]
    return json.dumps({"type": "user", "message": {"role": "user", "content": content}}, ensure_ascii=False) + "\n"


def parse_output(custom_id: str, stdout: str) -> Result:
    final = None
    for line in stdout.splitlines():
        try:
            d = json.loads(line)
        except json.JSONDecodeError:
            continue
        if d.get("type") == "result":
            final = d
    if final is None or final.get("is_error") or final.get("subtype") != "success":
        text = (final or {}).get("result")
        return Result(custom_id, "errored", text, None, {}, (final or {}).get("stop_reason"))
    u = final.get("usage") or {}
    usage = {k: int(u.get(k) or 0) for k in
             ("input_tokens", "output_tokens", "cache_read_input_tokens", "cache_creation_input_tokens")}
    text = final.get("result") or ""
    parsed = final.get("structured_output")
    status = "contaminated" if any(w in text.lower() for w in SUSPICIOUS) else "succeeded"
    return Result(custom_id, status, text, parsed, usage, final.get("stop_reason"))


def run_one(custom_id: str, params: dict, timeout: int = TIMEOUT) -> Result:
    with tempfile.TemporaryDirectory(prefix="banalita-cc-") as cwd:
        try:
            r = subprocess.run(build_command(params), input=build_stdin(params), cwd=cwd, env=minimal_env(),
                               capture_output=True, text=True, timeout=timeout)
        except subprocess.TimeoutExpired:
            return Result(custom_id, "errored", None, None, {}, "timeout")
    return parse_output(custom_id, r.stdout)


def prefix_key(params: dict) -> str:
    """Che cosa la cache condivide: modello, sistema e tutti i blocchi tranne l'ultimo."""
    head = {"model": params["model"], "system": params["system"],
            "content": params["messages"][0]["content"][:-1]}
    return hashlib.sha256(json.dumps(head, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def _done(out: Path) -> dict[str, Result]:
    if not out.exists():
        return {}
    rows = [Result.from_json(l) for l in out.read_text(encoding="utf-8").splitlines() if l.strip()]
    return {r.custom_id: r for r in rows if r.status == "succeeded"}


def run_claude_code(requests: dict[str, dict], phase: str, ledger: Ledger, out: Path, workers: int = 2,
                    runner=run_one, timeout: int = TIMEOUT, dry_run: bool = False) -> dict[str, Result]:
    out = Path(out)
    results = _done(out)
    todo = {cid: p for cid, p in requests.items() if cid not in results}
    if dry_run:
        print(f"{phase}: {len(todo)} chiamate da fare con Claude Code ({len(results)} già fatte), "
              f"spesi a listino {ledger.spent():.2f} $")
        return {}
    out.parent.mkdir(parents=True, exist_ok=True)
    lock = threading.Lock()

    def work(item):
        cid, params = item
        ledger.require(0.0, phase)
        res = runner(cid, params, timeout)
        with lock:
            if res.usage:
                ledger.record(phase, res.usage, params["model"], batch=False, expect_cache=False,
                              cache_ttl="1h", custom_id=cid)
            with out.open("a", encoding="utf-8") as f:
                f.write(res.to_json() + "\n")
        return res

    # La prima chiamata di ogni prefisso scrive la cache da sola, prima delle altre del gruppo:
    # partite insieme, la scriverebbero tutte (208.000 token ciascuna con la nota di Zhang).
    groups: dict[str, list] = {}
    for item in todo.items():
        groups.setdefault(prefix_key(item[1]), []).append(item)
    with ThreadPoolExecutor(max_workers=workers) as pool:
        for res in pool.map(work, [g[0] for g in groups.values()]):
            results[res.custom_id] = res
        for res in pool.map(work, [it for g in groups.values() for it in g[1:]]):
            results[res.custom_id] = res
    return results
