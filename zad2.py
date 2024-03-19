def make_multiplier(a):
    def multiplier(b):
        return a * b
    return multiplier

result = make_multiplier(10)

print(result(20))