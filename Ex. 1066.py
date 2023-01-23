from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

par = impar = pos = neg = 0

def fnc1 ():
    for _ in range (5):
        num = int (input ())
    
    if num % 2 == 0:
        par += 1
        
    if num % 2 == 1:
        impar += 1
    
    if num > 0:
        pos += 1
    
    if num < 0:
        neg += 1
    # Casos onde será analisado
    # cada valor de 'num'.

    print (f'{par} valor(es) par(es)')
    print (f'{impar} valor(es) impar(es)')
    print (f'{pos} valor(es) positivo(s)')
    print (f'{neg} valor(es) negativo(s)')
    # Impressão de valores.