def soma_ate(n):
    if n <= 1:
        return 1

    return n + soma_ate(n - 1)

print(soma_ate(4))