import json
from collections import Counter

from analysis.human import human_vs_judge
from banalita.judge import Claim, Judgment
from labeling.make_page import make_page
from labeling.sample import sample_claims


def _judgments():
    """Due spiegazioni per livello 1-4; ognuna con affermazioni di ogni etichetta."""
    out = {}
    labels = ["supported", "unsupported", "contradicted", "analogy_as_fact", "declared_analogy"]
    for level in (1, 2, 3, 4):
        for s in range(2):
            claims = [Claim(text=f"Affermazione L{level} s{s} n{k}-{i}", kind="proof", label=lab, source="F1",
                            page=1, quote="la citazione", note="") for k, lab in enumerate(labels) for i in range(5)]
            out[f"judge-claude_full-L{level}-s{s:02d}"] = Judgment(claims=claims, coverage={})
    return out


def test_sample_is_stratified_and_deterministic():
    j = _judgments()
    a, b = sample_claims(j, n=40), sample_claims(j, n=40)
    assert a == b and len(a) == 40
    assert all(x["level"] in (1, 2) for x in a)
    counts = Counter(x["judge_label"] for x in a)
    # le analogie dichiarate non si etichettano; le altre quattro etichette sono bilanciate
    assert "declared_analogy" not in counts
    assert max(counts.values()) - min(counts.values()) <= 1


def test_page_hides_judge_labels():
    sample = sample_claims(_judgments(), n=8)
    page = make_page(sample)
    for x in sample:
        assert x["text"] in page
    assert "judge_label" not in page and "contradicted" not in page and "analogy_as_fact" not in page
    assert "claude_full" not in page and "judge-" not in page  # nessun indizio sul braccio


def test_page_has_three_choices_per_claim():
    sample = sample_claims(_judgments(), n=8)
    page = make_page(sample)
    assert page.count('data-choice="sostenuta"') == 8
    assert page.count('data-choice="non_sostenuta"') == 8
    assert page.count('data-choice="contraddetta"') == 8


def test_precision_recall_known_case():
    sample = [{"id": f"c{i}", "judge_label": lab} for i, lab in
              enumerate(["contradicted", "contradicted", "supported", "supported", "unsupported"])]
    human = {"c0": "contraddetta", "c1": "sostenuta", "c2": "sostenuta", "c3": "sostenuta", "c4": "non_sostenuta"}
    r = human_vs_judge(human, sample)
    # «errore» del giudice (contradicted o analogy_as_fact) contro «contraddetta» della persona
    assert r["errore"]["precisione"] == 0.5 and r["errore"]["richiamo"] == 1.0
    assert r["sostenuta"]["precisione"] == 1.0 and r["sostenuta"]["richiamo"] == 2 / 3
    assert r["n"] == 5
