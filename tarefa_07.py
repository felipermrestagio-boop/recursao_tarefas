def contar_letra(palavra, letra):
    
    if(len(palavra ) > 1):
        if(palavra[0] == letra or len(palavra) == 1 and palavra[0] == letra ):
            return 1 + contar_letra(palavra[1:], letra)
        else: 
            return 0 + contar_letra(palavra[1:], letra)
    elif(len(palavra) == 1):
        if(palavra == letra):
            return 1
        else:
            return 0

