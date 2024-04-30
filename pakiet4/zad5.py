def podziel_liste(lista, maks_dlugosc):
    podzielone_czesci = []
    for i in range(0, len(lista), maks_dlugosc):
        podzielone_czesci.append(lista[i:i+maks_dlugosc])
    return podzielone_czesci

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

podzielone = podziel_liste(lista, 3)
print(podzielone)