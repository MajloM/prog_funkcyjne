Cena_global = 10
def Test():
    Banan = 5
    global Cena_global
    Cena_global +=20
    print("Lokalny produkt: ", Banan)
    print("Globalna cena: ", Cena_global)

Test()

