lista_slow = ["romek", "tomek", "atomek", "arek", "kasia"]

slowa_na_a = list(filter(lambda  slowo: slowo.startswith('a'), lista_slow))

print(slowa_na_a)


lista_liczb = [4, 5, 9, 12, 25]

kwadraty = list(map(lambda x: x**2, lista_liczb))

print(kwadraty)