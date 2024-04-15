from itertools import product

lista1 = ['A', 'B']
lista2 = ['C', 'D']

for kombinacja in product(lista1, lista2):
    print(kombinacja)