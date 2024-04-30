def stworz_potegowanie(exponent):
    def potegowanie(x):
        return x ** exponent
    return potegowanie

podnies_do_kwadratu = stworz_potegowanie(5)
print(podnies_do_kwadratu(10))

podnies_do_szescianu = stworz_potegowanie(4)
print(podnies_do_szescianu(51))