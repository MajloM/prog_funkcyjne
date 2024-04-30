def apply_function_to_tuples(tuple_list, func):
    return [func(*t) for t in tuple_list]

def sum_tuple(a, b):
    return a + b

tuple_list = [(1, 2), (3, 4), (5, 6)]

result_list = apply_function_to_tuples(tuple_list, sum_tuple)
print(result_list)