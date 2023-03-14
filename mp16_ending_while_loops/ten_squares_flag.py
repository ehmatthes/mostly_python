x = 1
active = True
while active:
    square = x**2
    print(square)

    x += 1
    if x > 10:
        active = False