import pytest

from banalita.readability import counts, gulpease


def test_gulpease_known_value():
    # 6 parole, 23 lettere, 2 frasi: 89 + (300*2 - 10*23) / 6
    assert gulpease("Il gatto dorme. Il cane corre.") == pytest.approx(150.6667, abs=1e-3)


def test_apostrophe_splits_words():
    c = counts("L'ipotesi è vera.")
    assert c.words == 4  # L, ipotesi, è, vera
    assert c.letters == 13
    assert c.sentences == 1


def test_abbreviation_does_not_end_sentence():
    assert counts("Vedi p. 495 del testo.").sentences == 1
    assert counts("Vedi pp. 495 e seguenti, ecc. e poi basta.").sentences == 1


def test_single_letter_initial_does_not_end_sentence():
    assert counts("Lo dimostra A. Weil nel 1948.").sentences == 1


def test_decimal_does_not_end_sentence():
    assert counts("Fa 19.344 contro 19,237 circa.").sentences == 1


def test_ellipsis_ends_sentence():
    assert counts("Poi… Si vede dopo.").sentences == 2


def test_question_and_exclamation_end_sentences():
    assert counts("Davvero? Sì! Bene.").sentences == 3


def test_last_sentence_without_period_counts():
    assert counts("Una frase. Un'altra senza punto").sentences == 2


def test_numbers_are_words_without_letters():
    c = counts("Sono 17 milioni.")
    assert c.words == 3
    assert c.letters == 11


def test_empty_text_raises_value_error():
    with pytest.raises(ValueError):
        gulpease("   ")


def test_single_letter_can_count_as_sentence_end():
    """Analisi di sensibilità del 23/11/2026: nei testi tecnici «fino a x.» chiude la frase."""
    assert counts("Vale fino a x. Poi basta.").sentences == 1
    assert counts("Vale fino a x. Poi basta.", letter_ends_sentence=True).sentences == 2
    assert gulpease("Vale fino a x. Poi basta.", letter_ends_sentence=True) > gulpease("Vale fino a x. Poi basta.")
