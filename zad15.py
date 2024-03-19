def add(a):
    def currying(b):
        return a + b

    return currying

print(add(5)(4))