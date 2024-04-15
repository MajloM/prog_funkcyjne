from itertools import groupby

ciag_liczb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

grupowane = groupby(ciag_liczb, key=lambda x: 'parzysta' if x % 2 == 0 else 'nieparzysta')

for klucz, grupa in grupowane:
    print(klucz, list(grupa))