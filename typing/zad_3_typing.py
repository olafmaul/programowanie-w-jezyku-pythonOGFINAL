# zad 3

def steven_even(x):
    return x % 2 == 0


wybrana_liczba = 10

czy_even = steven_even(wybrana_liczba)

if czy_even:
    print(f"Liczba {wybrana_liczba}: jest parzysta")
else:
    print(f"Liczba {wybrana_liczba}: jest nieparzysta")
