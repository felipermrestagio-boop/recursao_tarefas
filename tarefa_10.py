def imprimir_invertido(lista):
    if(not lista):
       return 

    imprimir_invertido(lista[1:])

    print(lista[0])

imprimir_invertido([1,2,3])