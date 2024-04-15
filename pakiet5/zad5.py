def parzyste(lista):
    return [liczba for liczba in lista if liczba % 2 == 0 ]

liczby = [1,2,3,4,5,6,7,8,9,10]
wynik = parzyste(liczby)
print(wynik)

pole_prostokata = lambda a, b: a * b

dlugosc = float(input("Podaj dlugosc: "))
szerokosc = float(input("Podaj szerokoscc: "))
wynik = pole_prostokata(dlugosc, szerokosc)
print("Pole prostokąta: ", wynik)
