import pytest

"""ZADANIE 1"""
def is_palindrome(text: str) -> bool:

    cleaned_text = "".join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]

"""ZADANIE 2"""
def fibonacci(n: int) -> int:

    if n < 0:
        raise ValueError("UJEMNA!!!")
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

"""ZADANIE 3"""
def count_vowels(text: str) -> int:
    vowels = "aeiouyAEIOUYąćęłńóśźżĄĆĘŁŃÓŚŹŻ"
    count = sum(1 for char in text if char in vowels)
    return count

"""ZADANIE 4"""
def calculate_discount(price: float, discount: float) -> float:
    if not (0 <= discount <= 1):
        raise ValueError("UJEMNA ALBO 0")
    return price * (1 - discount)

"""ZADANIE 5"""
def flatten_list(nested_list: list) -> list:
    flattened = []
    for item in nested_list:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)
    return flattened

"""ZADANIE 6"""
import string

def word_frequencies(text: str) -> dict:
    text = text.lower()
    for char in string.punctuation:
        text = text.replace(char, "")
    words = text.split()
    frequencies = {}
    for word in words:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1
    return frequencies

"""ZADANIE 7"""
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

