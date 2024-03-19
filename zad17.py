from functools import partial

def five_funs(a,b):
    return a+b

five_jej = partial(five_funs, 5)

print(five_jej(9))