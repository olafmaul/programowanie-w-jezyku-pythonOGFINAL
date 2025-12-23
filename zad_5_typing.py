# zad 5

def list_checker(zbior_zakres: list, szukana_liczba: int):
    return szukana_liczba in zbior_zakres


uno_lista_zakres = [10, 20, 30, 69, 99, 100]
due_liczba = 100

czy_jest = list_checker(uno_lista_zakres, due_liczba)

if czy_jest:
    print(f"Lista zawiera podaną wartość")
else:
    print(f"Lista nie zawiera podanej wartości")
