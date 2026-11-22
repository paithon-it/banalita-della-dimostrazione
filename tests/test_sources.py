import hashlib
import json

import pytest

from banalita.sources import Source, SourceMismatch, load_sources, overview_text, verify


def _source(tmp_path, content: bytes, sha: str) -> Source:
    local = tmp_path / "f.pdf"
    local.write_bytes(content)
    return Source(id="F1", url="https://example.org/f.pdf", sha256=sha, local=local)


def test_verify_rejects_wrong_hash(tmp_path):
    src = _source(tmp_path, b"contenuto", "0" * 64)
    with pytest.raises(SourceMismatch):
        verify(src)


def test_verify_accepts_right_hash(tmp_path):
    data = b"contenuto"
    src = _source(tmp_path, data, hashlib.sha256(data).hexdigest())
    verify(src)


def test_verify_missing_file_raises(tmp_path):
    src = Source(id="F1", url="u", sha256="0" * 64, local=tmp_path / "manca.pdf")
    with pytest.raises(SourceMismatch):
        verify(src)


def test_load_sources_reads_json(tmp_path):
    path = tmp_path / "sources.json"
    path.write_text(json.dumps({"sources": [
        {"id": "F1", "url": "https://example.org/a.pdf", "sha256": "a" * 64, "file": "a.pdf"},
    ]}))
    srcs = load_sources(path, root=tmp_path / "sources")
    assert srcs["F1"].local == tmp_path / "sources" / "a.pdf"
    assert srcs["F1"].sha256 == "a" * 64


def test_overview_text_uses_page_range(pdf_factory):
    pdf = pdf_factory(["PRIMA PAGINA", "SECONDA PAGINA", "TERZA PAGINA"])
    text = overview_text(pdf, first_page=2, last_page=3)
    assert "SECONDA PAGINA" in text
    assert "TERZA PAGINA" in text
    assert "PRIMA PAGINA" not in text


def test_overview_text_stops_at_marker(pdf_factory):
    pdf = pdf_factory(["indice", "panoramica qui", "fine panoramica 2. Detecting zeros e oltre"])
    text = overview_text(pdf, first_page=2, last_page=3, stop_marker="2. Detecting zeros")
    assert "fine panoramica" in text
    assert "e oltre" not in text
