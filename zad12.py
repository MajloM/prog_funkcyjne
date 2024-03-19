from functools import partial
def multiplication(a,b):
    return a * b

multi3 = partial(multiplication,3)

print(multi3(6))
