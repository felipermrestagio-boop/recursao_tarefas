def tamanho_lista(lista):
    if not lista:
        return 0

    return 1 + tamanho_lista(lista[1:])


print(tamanho_lista(['a', 'b', 'c', 'd']))