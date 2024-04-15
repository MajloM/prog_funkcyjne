def dokwadratu(liczba):
    return liczba * liczba

def dodajjeden(liczba):
    return liczba + 5

def polacz_funkcje(lista_liczb, funkcja1, funkcja2):
    wyniki = []
    for liczba in lista_liczb:
        wynik_funkcji1 = funkcja1(liczba)
        wynik_funkcji2 = funkcja2(wynik_funkcji1)
        wyniki.append(wynik_funkcji2)
    return wyniki

lista_liczb = [1, 2, 3, 4, 5]

wyniki = polacz_funkcje(lista_liczb, dokwadratu, dodajjeden)

print(wyniki)