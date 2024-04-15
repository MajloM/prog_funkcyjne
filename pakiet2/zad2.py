from itertools import combinations

def kombinacje_dwa_elementy(lista):
    kombinacje = list(combinations(lista, 2))
    return kombinacje

lista_elementow = ['C', 'Y', 'F', 'B']
wynik = kombinacje_dwa_elementy(lista_elementow)
print(wynik)