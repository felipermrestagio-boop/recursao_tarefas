def contagem_regressiva(n):
    if(n < 0):
        return print("FIM!")

    print(n, end=" ")
    return contagem_regressiva(n - 1)

contagem_regressiva(3)