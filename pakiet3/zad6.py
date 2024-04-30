def apply_function_to_list(input_list, func):
    return [func(item) for item in input_list]

def square(x):
    return x ** 2

input_list = [1, 2, 3, 4, 5]

result_list = apply_function_to_list(input_list, square)
print(result_list)