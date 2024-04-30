from collections import Counter

def najczesciej_wystepujacy(lista):
    counter = Counter(lista)
    najczestszy_element, liczba_wystapien = counter.most_common(1)[0]
    return najczestszy_element

lista = [1, 2, 3, 2, 2, 4, 5, 5, 5, 5]

najczestszy = najczesciej_wystepujacy(lista)
print("Najczęściej występujący element:", najczestszy)