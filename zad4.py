import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Zajęło to mu : ", start, " ", end)
        return result
    return wrapper

@timeit
def func():
    result = 10
    for x in range(1, 10):
        result = result * x
    return result

print(func())