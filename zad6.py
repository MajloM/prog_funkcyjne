def square(x):
    return x*x

numbers_list = [123,51,21,1,3]
numbers_map = list(map(square, numbers_list))
print(numbers_map)