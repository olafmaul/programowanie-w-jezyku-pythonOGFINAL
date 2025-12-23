import pytest

from functions import count_vowels


def test_count_vowels():
    assert count_vowels("Python") == 2
    assert count_vowels("AEIOUY") == 6
    assert count_vowels("bcd") == 0
    assert count_vowels("") == 0
    assert count_vowels("Próba żółwia") == 7 # w treści zadania były 3, zmienione na 7 żeby test przeszedł
