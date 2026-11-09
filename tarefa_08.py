def existe_na_lista(lista, alvo):
    if(not lista):
        return False

    if(lista[0] == alvo):
        return True
    else:
        return existe_na_lista(lista[1:], alvo)


print(existe_na_lista([10, 20, 30], 40))
        