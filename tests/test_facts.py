import pytest
import yaml

from banalita.facts import FactError, facts_for_level, load_facts


def _write(tmp_path, facts):
    path = tmp_path / "facts.yaml"
    path.write_text(yaml.safe_dump({"facts": facts}, allow_unicode=True), encoding="utf-8")
    return path


def _fact(**kw):
    base = {"id": "S1", "group": "statement", "text": "Si dimostra l'ipotesi.",
            "source": "F1", "page": 1, "quote": "a proof", "min_level": 1}
    base.update(kw)
    return base


def test_rejects_unknown_group(tmp_path):
    with pytest.raises(FactError):
        load_facts(_write(tmp_path, [_fact(group="varie")]))


def test_rejects_level_out_of_range(tmp_path):
    with pytest.raises(FactError):
        load_facts(_write(tmp_path, [_fact(min_level=5)]))
    with pytest.raises(FactError):
        load_facts(_write(tmp_path, [_fact(min_level=0)]))


def test_rejects_missing_quote(tmp_path):
    with pytest.raises(FactError):
        load_facts(_write(tmp_path, [_fact(quote="  ")]))


def test_rejects_unknown_source(tmp_path):
    with pytest.raises(FactError):
        load_facts(_write(tmp_path, [_fact(source="F9")]))


def test_ids_unique(tmp_path):
    with pytest.raises(FactError):
        load_facts(_write(tmp_path, [_fact(), _fact()]))


def test_facts_for_level_filters(tmp_path):
    facts = load_facts(_write(tmp_path, [_fact(id="A", min_level=1), _fact(id="B", min_level=3)]))
    assert [f.id for f in facts_for_level(facts, 1)] == ["A"]
    assert [f.id for f in facts_for_level(facts, 3)] == ["A", "B"]


def test_repository_facts_valid():
    facts = load_facts()
    assert 20 <= len(facts) <= 30
    assert {f.group for f in facts} == {"statement", "architecture", "ingredients", "status", "limits"}
    assert any(f.min_level == 1 for f in facts)
    assert any(f.min_level == 4 for f in facts)


def _page_text(source, page: int) -> str:
    import html
    import re
    import subprocess

    if source.local.suffix == ".pdf":
        raw = subprocess.run(["pdftotext", "-f", str(page), "-l", str(page), str(source.local), "-"],
                             check=True, capture_output=True, text=True).stdout
    else:
        raw = html.unescape(re.sub(r"<[^>]+>", " ", source.local.read_text(encoding="utf-8")))
    return " ".join(raw.split())


def test_quotes_found_on_their_page():
    """Ogni citazione sta, lettera per lettera, alla pagina indicata (spazi normalizzati)."""
    from banalita.sources import load_sources

    sources = load_sources()
    if not all(s.local.exists() for s in sources.values()):
        pytest.skip("fonti non scaricate (scripts/fetch_sources.py)")
    missing = []
    for fact in load_facts():
        if " ".join(fact.quote.split()) not in _page_text(sources[fact.source], fact.page):
            missing.append(f"{fact.id} ({fact.source} p. {fact.page})")
    assert not missing, "citazioni non trovate: " + ", ".join(missing)
