def multiplicar(a, b):
    if(b == 1):
        return a

    return a + multiplicar(a, b - 1)

print(multiplicar(4, 3))