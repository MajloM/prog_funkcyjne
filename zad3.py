def filter_even_numbers(liczba):
    return list(filter(lambda x: x % 2 == 0, liczba))


print("Liczby parzyste z tej listy to: ", filter_even_numbers([1, 2, 3, 4, 5, 6, 78, 333, 3534, 22, 77, 53, 90]))
