def compose(funA, funB):
    return lambda x: (funA(funB(x)))
def funA(x):
    return x**2
def funB(x):
    return x-10

main_funs = compose(funA, funB)
print(main_funs(50))
