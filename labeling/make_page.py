"""La pagina con cui l'autore etichetta il campione: un file HTML autonomo, da aprire al telefono.

Per ogni affermazione tre scelte (sostenuta, non sostenuta, contraddetta); le scelte restano
nel browser (localStorage) e un bottone le scarica in JSON. Come materiale c'è l'elenco dei
fatti di riferimento con le loro citazioni. Nessuna traccia dell'etichetta del giudice.

Uso: uv run python -m labeling.make_page  (scrive results/labeling/etichette.html e campione.json)
"""
from __future__ import annotations

import html
import json
import sys
from pathlib import Path

from banalita.facts import facts_for_level, load_facts
from banalita.judge import JudgmentError, parse_judgment
from banalita.phases import RESULTS, load_results
from banalita.requests import parse_custom_id
from labeling.sample import sample_claims

CHOICES = (("sostenuta", "Sostenuta dalle fonti"), ("non_sostenuta", "Le fonti non lo dicono"),
           ("contraddetta", "Sbagliata o contraddetta"))

STYLE = """
body{margin:0;font:17px/1.5 -apple-system,system-ui,sans-serif;background:#F8F5EE;color:#1A1A1A}
main{max-width:680px;margin:0 auto;padding:16px}
h1{font-size:1.3rem}.c{background:#fff;border:1px solid #ddd;border-radius:10px;padding:14px;margin:14px 0}
.t{margin:0 0 10px}.n{color:#5E5852;font-size:.85rem}label{display:block;padding:8px 6px;border-radius:6px}
label:has(input:checked){background:#e6efe9}button{font-size:1rem;padding:10px 16px;border:0;border-radius:8px;
background:#2D5A5C;color:#fff}#stato{position:sticky;top:0;background:#F8F5EE;padding:8px 0;font-weight:600}
details{margin-top:24px}details li{margin-bottom:8px}q{color:#5E5852}
"""

SCRIPT = """
const KEY='banalita-etichette';const s=JSON.parse(localStorage.getItem(KEY)||'{}');
const all=document.querySelectorAll('.c');
function upd(){document.getElementById('stato').textContent=Object.keys(s).length+' di '+all.length+' etichettate';}
document.querySelectorAll('input[type=radio]').forEach(r=>{
  if(s[r.name]===r.dataset.choice)r.checked=true;
  r.addEventListener('change',()=>{s[r.name]=r.dataset.choice;localStorage.setItem(KEY,JSON.stringify(s));upd();});});
document.getElementById('scarica').addEventListener('click',()=>{
  const b=new Blob([JSON.stringify(s,null,1)],{type:'application/json'});
  const a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='etichette.json';a.click();});
upd();
"""


def make_page(sample: list[dict], facts=None) -> str:
    facts = facts if facts is not None else load_facts()
    cards = []
    for i, x in enumerate(sample, 1):
        name = html.escape(x["id"], quote=True)
        opts = "".join(
            f'<label><input type="radio" name="{name}" data-choice="{c}"> {html.escape(lbl)}</label>'
            for c, lbl in CHOICES)
        cards.append(f'<div class="c"><p class="n">{i} · spiegazione per livello {x["level"]}</p>'
                     f'<p class="t">{html.escape(x["text"])}</p>{opts}</div>')
    facts_html = "".join(f'<li><b>{f.id}</b> {html.escape(f.text)}<br><q>{html.escape(f.quote)}</q> '
                         f'({f.source}, p. {f.page})</li>' for f in facts)
    return (
        "<!doctype html><html lang='it'><head><meta charset='utf-8'>"
        "<meta name='viewport' content='width=device-width,initial-scale=1'>"
        f"<title>Etichette</title><style>{STYLE}</style></head><body><main>"
        "<h1>Le affermazioni da etichettare</h1>"
        "<p>Per ciascuna: è sostenuta dalle fonti sulla dimostrazione di Alpöge, le fonti non lo dicono, "
        "o è sbagliata? I fatti di riferimento, con le citazioni, sono in fondo. Le scelte restano in "
        "questo browser; alla fine premi «Scarica».</p>"
        "<div id='stato'></div>" + "".join(cards) +
        "<p><button id='scarica'>Scarica le etichette</button></p>"
        f"<details><summary>Fatti di riferimento</summary><ol>{facts_html}</ol></details>"
        f"</main><script>{SCRIPT}</script></body></html>")


def main(results_dir: Path = RESULTS) -> Path:
    facts = load_facts()
    judgments = {}
    for r in load_results(Path(results_dir) / "judgments.jsonl"):
        level = parse_custom_id(r.custom_id)[2]
        try:
            judgments[r.custom_id] = parse_judgment(r.parsed or {}, [f.id for f in facts_for_level(facts, level)])
        except JudgmentError:
            continue
    sample = sample_claims(judgments)
    out = Path(results_dir) / "labeling"
    out.mkdir(parents=True, exist_ok=True)
    (out / "campione.json").write_text(json.dumps(sample, ensure_ascii=False, indent=1), encoding="utf-8")
    page = out / "etichette.html"
    page.write_text(make_page(sample, facts), encoding="utf-8")
    return page


if __name__ == "__main__":
    print(main())
    sys.exit(0)
