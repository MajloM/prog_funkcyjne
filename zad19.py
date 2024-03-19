def multiply_elements(tup):
    result = 1
    for num in tup:
        result *= num
    return result

my_tuple = (2, 3, 4)
print(multiply_elements(my_tuple))