import pytest
import json

from banalita.batch import Result
from banalita.claude_code import ENV_KEYS, build_command, build_stdin, minimal_env, parse_output, run_claude_code
from banalita.costs import Ledger

PARAMS = {
    "model": "claude-opus-5-5", "max_tokens": 32000,
    "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object"}}},
    "system": [{"type": "text", "text": "Sei un revisore."}],
    "messages": [{"role": "user", "content": [
        {"type": "document", "title": "F1", "source": {"type": "base64", "media_type": "application/pdf", "data": "QUJD"},
         "cache_control": {"type": "ephemeral", "ttl": "1h"}},
        {"type": "text", "text": "Giudica."}]}],
}


def _result_line(**over):
    base = {"type": "result", "subtype": "success", "is_error": False, "result": "{\"a\":1}",
            "structured_output": {"a": 1}, "stop_reason": "end_turn", "total_cost_usd": 0.5,
            "usage": {"input_tokens": 3, "output_tokens": 100, "cache_read_input_tokens": 1000,
                      "cache_creation_input_tokens": 0}}
    base.update(over)
    return json.dumps({"type": "system", "subtype": "init"}) + "\n" + json.dumps(base) + "\n"


def test_command_has_isolation_flags_and_no_bare():
    cmd = build_command(PARAMS)
    assert cmd[:2] == ["claude", "-p"]
    for flag in ("--tools", "--setting-sources", "--strict-mcp-config", "--no-session-persistence",
                 "--disable-slash-commands"):
        assert flag in cmd
    assert "--bare" not in cmd  # --bare autentica solo con la chiave API, cioè a pagamento
    assert cmd[cmd.index("--model") + 1] == "claude-opus-5-5"
    assert cmd[cmd.index("--effort") + 1] == "high"
    assert cmd[cmd.index("--system-prompt") + 1] == "Sei un revisore."
    assert cmd[cmd.index("--tools") + 1] == ""


def test_command_adds_json_schema_only_with_format():
    assert json.loads(build_command(PARAMS)[build_command(PARAMS).index("--json-schema") + 1]) == {"type": "object"}
    plain = {**PARAMS, "output_config": {"effort": "high"}}
    assert "--json-schema" not in build_command(plain)


def test_stdin_keeps_cache_control_and_documents():
    """Claude Code mette da solo il punto di cache in fondo al messaggio: senza il cache_control
    sulle fonti, i giudizi (diversi solo nell'ultimo blocco) non riusano mai la cache (provato
    il 22/11/2026: 220.000 token riscritti per giudizio)."""
    msg = json.loads(build_stdin(PARAMS))
    blocks = msg["message"]["content"]
    assert msg["type"] == "user" and blocks[0]["type"] == "document"
    assert blocks[0]["cache_control"] == {"type": "ephemeral", "ttl": "1h"}
    assert blocks[0]["source"]["data"] == "QUJD"


def test_minimal_env_has_only_basic_keys():
    env = minimal_env()
    assert set(env) <= set(ENV_KEYS)
    assert "ANTHROPIC_API_KEY" not in env


def test_parse_output_success_with_structured_output():
    r = parse_output("c1", _result_line())
    assert r.status == "succeeded" and r.parsed == {"a": 1}
    assert r.usage["cache_read_input_tokens"] == 1000


def test_parse_output_plain_text_and_error():
    r = parse_output("c1", _result_line(result="Una spiegazione.", structured_output=None))
    assert r.status == "succeeded" and r.text == "Una spiegazione." and r.parsed is None
    e = parse_output("c2", _result_line(is_error=True, subtype="error_during_execution", result="boom"))
    assert e.status == "errored"
    assert parse_output("c3", "").status == "errored"


def test_contamination_flagged():
    r = parse_output("c1", _result_line(result="Come dice il file CLAUDE.md del progetto...", structured_output=None))
    assert r.status == "contaminated"


def test_resume_skips_done_and_records_spend(tmp_path):
    out = tmp_path / "out.jsonl"
    out.write_text(Result("a", "succeeded", "x", None, {}, "end_turn").to_json() + "\n")
    seen = []

    def fake(cid, params, timeout):
        seen.append(cid)
        return Result(cid, "succeeded", "y", None, {"input_tokens": 1_000_000, "output_tokens": 0}, "end_turn")

    led = Ledger(tmp_path / "s.jsonl", cap=1000)
    res = run_claude_code({"a": PARAMS, "b": PARAMS}, "explain", led, out, workers=1, runner=fake)
    assert seen == ["b"]
    assert set(res) == {"a", "b"}
    assert led.spent() == 4.0  # costo a listino, senza sconto batch
    assert len(out.read_text().splitlines()) == 2


def test_first_call_of_each_prefix_runs_alone(tmp_path):
    """La prima chiamata di ogni gruppo con lo stesso prefisso scrive la cache da sola; le altre
    del gruppo partono solo dopo, per leggerla."""
    import threading
    import time
    from banalita.claude_code import prefix_key
    events, lock = [], threading.Lock()

    def fake(cid, params, timeout):
        with lock:
            events.append(("start", cid))
        time.sleep(0.05)
        with lock:
            events.append(("end", cid))
        return Result(cid, "succeeded", "y", None, {}, "end_turn")

    other = {**PARAMS, "system": [{"type": "text", "text": "Altro sistema."}]}
    reqs = {"a1": PARAMS, "a2": PARAMS, "a3": PARAMS, "b1": other, "b2": other}
    run_claude_code(reqs, "x", Ledger(tmp_path / "s.jsonl", cap=1000), tmp_path / "o.jsonl", workers=3, runner=fake)
    for first, rest in (("a1", ("a2", "a3")), ("b1", ("b2",))):
        end_first = events.index(("end", first))
        assert all(events.index(("start", r)) > end_first for r in rest)
    assert prefix_key(PARAMS) != prefix_key(other)
    last_block_changed = {**PARAMS, "messages": [{"role": "user", "content": PARAMS["messages"][0]["content"][:-1]
                                                 + [{"type": "text", "text": "Diverso."}]}]}
    assert prefix_key(PARAMS) == prefix_key(last_block_changed)


def _init_line(**over):
    base = {"type": "system", "subtype": "init", "tools": [], "mcp_servers": [], "skills": [],
            "plugins": [{"name": "cc-plugin-telemetry", "path": "builtin", "source": "cc-plugin-telemetry@builtin"}]}
    base.update(over)
    return json.dumps(base) + "\n"


def test_isolated_init_passes():
    """La prova del 23/11/2026: niente strumenti, server MCP né skill, solo plugin interni."""
    stdout = _init_line() + _result_line().split("\n", 1)[1]
    assert parse_output("c1", stdout).status == "succeeded"


@pytest.mark.parametrize("over", [{"tools": ["Bash"]}, {"mcp_servers": [{"name": "paithon"}]},
                                  {"skills": ["superpowers:brainstorming"]},
                                  {"plugins": [{"name": "superpowers", "path": "/home/x/.claude/plugins/sp"}]}])
def test_init_with_tools_or_user_plugins_is_contaminated(over):
    stdout = _init_line(**over) + _result_line().split("\n", 1)[1]
    assert parse_output("c1", stdout).status == "contaminated"
