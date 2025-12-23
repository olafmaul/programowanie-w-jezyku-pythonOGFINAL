import pytest

from functions import word_frequencies


def test_word_frequencies():
    text1 = "To be or not to be"
    expected1 = {"to": 2, "be": 2, "or": 1, "not": 1}
    assert word_frequencies(text1) == expected1
    text2 = "Hello, hello!"
    expected2 = {"hello": 2}
    assert word_frequencies(text2) == expected2
    text3 = ""
    expected3 = {}
    assert word_frequencies(text3) == expected3
    text4 = "Python Python python"
    expected4 = {"python": 3}
    assert word_frequencies(text4) == expected4
    text5 = "Ala ma kota, a kot ma Ale."
    expected5 = {"ala": 1, "ma": 2, "kota": 1, "a": 1, "kot": 1, "ale": 1} # Zmiana "ala" na 1 z 2, inaczej wychodził błąd w teście
    assert word_frequencies(text5) == expected5
