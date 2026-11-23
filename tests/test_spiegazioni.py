from pathlib import Path

import pytest

from analysis.spiegazioni import to_html, write_markdown


def test_paragraphs_bold_italic_and_escaping():
    t = "Sulla striscia 0 < Re(s) < 1 vale **questo**.\n\nE *quello* & altro."
    assert to_html(t) == ("<p>Sulla striscia 0 &lt; Re(s) &lt; 1 vale <strong>questo</strong>.</p>\n"
                          "<p>E <em>quello</em> &amp; altro.</p>")


def test_bullets_and_numbered_lists_inside_a_block():
    t = "I passi sono due:\n- il primo\n- il secondo\n\n1. uno\n2. due"
    assert to_html(t) == ("<p>I passi sono due:</p>\n<ul>\n<li>il primo</li>\n<li>il secondo</li>\n</ul>\n"
                          "<ol>\n<li>uno</li>\n<li>due</li>\n</ol>")


def test_single_newline_inside_a_paragraph_is_a_space():
    assert to_html("una riga\naltra riga") == "<p>una riga altra riga</p>"


@pytest.mark.skipif(not Path("results/explanations_claude.jsonl").exists(), reason="risultati assenti")
def test_markdown_file_has_all_64_explanations(tmp_path):
    out = write_markdown(Path("results"), tmp_path / "spiegazioni.md")
    text = out.read_text()
    assert text.count("\n### ") == 64
    assert "claude_full-L1-s04" in text
