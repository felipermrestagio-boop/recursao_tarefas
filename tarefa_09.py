def eh_palindromo(palavra):
    palavra = palavra.lower()
    if(len(palavra) <= 1):
        return True
   
    if(palavra[0] != palavra[len(palavra) - 1]):
        return False

    return eh_palindromo(palavra[len(palavra) - 1])

print(eh_palindromo("radar"))
   