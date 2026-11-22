"""Indice Gulpease: la formula di leggibilità standard per l'italiano.

    G = 89 + (300 * frasi - 10 * lettere) / parole

Più è alto, più il testo è facile: sotto 80 è difficile per chi ha la licenza elementare,
sotto 60 per chi ha la licenza media, sotto 40 per chi ha un diploma superiore.

Regole di conteggio, fissate nel protocollo:
- lettere: i soli caratteri alfabetici, accentate comprese;
- parole: le sequenze separate da spazi o da apostrofi («l'ipotesi» sono due parole);
  anche un numero è una parola, senza lettere;
- frasi: le chiude un `.`, `!`, `?` o `…` seguito da uno spazio o dalla fine del testo,
  tranne il punto dopo una sola lettera («A. Weil») o dopo un'abbreviazione della lista
  `ABBREVIAZIONI`; i numeri con il punto o la virgola («19.344») non chiudono niente.
  Un testo che non finisce con un segno di chiusura conta la sua ultima frase.
"""
from __future__ import annotations

import re
from dataclasses import dataclass

ABBREVIAZIONI = frozenset({"p", "pp", "ecc", "es", "n", "cfr", "vol", "cap", "sez", "fig"})

_WORD = re.compile(r"[^\s'’]+")
_END = re.compile(r"([.!?…]+)(?=\s|$)")


@dataclass(frozen=True)
class Counts:
    letters: int
    words: int
    sentences: int


def _sentences(text: str) -> int:
    n = 0
    last_end = 0
    for m in _END.finditer(text):
        token = text[:m.start()].split()[-1] if text[:m.start()].split() else ""
        token = re.split(r"['’]", token)[-1]
        if m.group(1) == ".":
            word = token.lower()
            if len(word) == 1 and word.isalpha():
                continue
            if word in ABBREVIAZIONI:
                continue
        n += 1
        last_end = m.end()
    if text[last_end:].strip():
        n += 1
    return n


def counts(text: str) -> Counts:
    words = _WORD.findall(text)
    words = [w for w in words if any(ch.isalnum() for ch in w)]
    letters = sum(1 for ch in text if ch.isalpha())
    return Counts(letters=letters, words=len(words), sentences=_sentences(text))


def gulpease(text: str) -> float:
    c = counts(text)
    if c.words == 0:
        raise ValueError("testo senza parole")
    return 89 + (300 * c.sentences - 10 * c.letters) / c.words
