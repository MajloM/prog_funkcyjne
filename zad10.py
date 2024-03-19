def generate():
    x = 0
    while True:
        yield x
        x+= 2

for i in generate():
    print(i)