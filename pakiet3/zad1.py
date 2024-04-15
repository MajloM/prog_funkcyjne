def suma_parzystych(lista):
    suma = 0
    for liczba in lista:
        if liczba % 2 == 0:
            suma += liczba
    return suma

lista_liczb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(suma_parzystych(lista_liczb))