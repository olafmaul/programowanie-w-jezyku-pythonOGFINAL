def list_combiner_no_dup(lista_uno: list, lista_due: list):
    unique_values = list(set(lista_uno + lista_due))
    potegowanie_wartosci = [element ** 3 for element in unique_values]
    return potegowanie_wartosci


pierwsza_lista = [1, 2, 3, 4, 5, 6]
druga_lista = [5, 6, 7, 8, 9]

list_merger = list_combiner_no_dup(pierwsza_lista, druga_lista)

print(list_merger)
