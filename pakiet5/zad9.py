from functools import reduce

liczby = [3, 9, 2, 7, 1, 8, 5]

max_liczba = reduce(lambda x, y: x if x > y else y, liczby)
print("Największa liczba:", max_liczba)

def srednia(lista):
    suma = reduce(lambda x, y: x + y, lista)
    return suma / len(lista)

print("Średnia z listy liczb:", srednia(liczby))