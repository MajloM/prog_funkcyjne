lista_liczb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

kwadraty_wieksze_niz_10 = [x ** 2 for x in lista_liczb if (kwadrat := x ** 2) > 10]

print(kwadraty_wieksze_niz_10)