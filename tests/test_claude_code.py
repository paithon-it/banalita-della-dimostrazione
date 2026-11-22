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


def test_stdin_strips_cache_control_keeps_documents():
    msg = json.loads(build_stdin(PARAMS))
    blocks = msg["message"]["content"]
    assert msg["type"] == "user" and blocks[0]["type"] == "document"
    assert all("cache_control" not in b for b in blocks)
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
