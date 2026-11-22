"""Le fonti dell'esperimento: URL, SHA-256 e copia locale (mai nel repository).

F1 è la nota di Alpöge, F2 la nota di Zhang, F3a la dichiarazione di Lean e Mathlib,
F3b la pagina dei controlli di Sutherland. `data/sources.json` ne tiene URL e hash;
`scripts/fetch_sources.py` le scarica in `sources/`, che git ignora.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


class SourceMismatch(Exception):
    """La copia locale manca o non ha l'hash registrato."""


@dataclass(frozen=True)
class Source:
    id: str
    url: str
    sha256: str
    local: Path


def load_sources(path: Path | str = ROOT / "data" / "sources.json",
                 root: Path | str = ROOT / "sources") -> dict[str, Source]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return {
        s["id"]: Source(id=s["id"], url=s["url"], sha256=s["sha256"], local=Path(root) / s["file"])
        for s in data["sources"]
    }


def sha256_of(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def verify(source: Source) -> None:
    if not source.local.is_file():
        raise SourceMismatch(f"{source.id}: manca la copia locale {source.local}")
    got = sha256_of(source.local)
    if got != source.sha256:
        raise SourceMismatch(f"{source.id}: SHA-256 {got}, atteso {source.sha256}")


def pdf_text(pdf: Path, first_page: int | None = None, last_page: int | None = None) -> str:
    cmd = ["pdftotext", "-layout"]
    if first_page is not None:
        cmd += ["-f", str(first_page)]
    if last_page is not None:
        cmd += ["-l", str(last_page)]
    cmd += [str(pdf), "-"]
    return subprocess.run(cmd, check=True, capture_output=True, text=True).stdout


def overview_text(pdf: Path, first_page: int = 3, last_page: int = 14,
                  stop_marker: str | None = "2. Detecting zeros") -> str:
    """Il testo della panoramica di F2: le pagine indicate, fino al titolo della sezione 2."""
    text = pdf_text(pdf, first_page, last_page)
    if stop_marker:
        cut = text.find(stop_marker)
        if cut >= 0:
            text = text[:cut]
    return text.rstrip() + "\n"
