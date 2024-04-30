def filtrowanie_parzystych(slowo):
    return {klucz: wartosc for klucz, wartosc in slowo.items() if isinstance(wartosc, int) and wartosc % 2 == 0}

slownik = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

print(filtrowanie_parzystych(slownik))