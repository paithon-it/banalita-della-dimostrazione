"""Scarica le fonti in `sources/` (se mancano) e ne controlla lo SHA-256.

Uso: uv run python scripts/fetch_sources.py

Le fonti non si ridistribuiscono: restano dei loro autori. Se una pagina viva è cambiata
dopo il 22/11/2026, l'hash non torna e lo script lo dice: per rifare le prove serve la
copia con l'hash registrato in `data/sources.json`.
"""
import sys
import urllib.request

from banalita.sources import SourceMismatch, load_sources, verify


def main() -> int:
    bad = 0
    for src in load_sources().values():
        if not src.local.exists():
            src.local.parent.mkdir(parents=True, exist_ok=True)
            req = urllib.request.Request(src.url, headers={"User-Agent": "Mozilla/5.0 (research)"})
            with urllib.request.urlopen(req, timeout=60) as r:
                src.local.write_bytes(r.read())
        try:
            verify(src)
            print(f"ok  {src.id}  {src.local.name}")
        except SourceMismatch as e:
            bad += 1
            print(f"NO  {e}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
