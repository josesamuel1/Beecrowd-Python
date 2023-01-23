from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

def positivos (a, b, c, d, e, f):
    posit = soma_total = 0
    # Atribuição de valores para contagem.
    
    if a > 0:
        posit = posit + 1
        soma_total = soma_total + a
    if b > 0:
        posit = posit + 1
        soma_total = soma_total + b
    if c > 0:
        posit = posit + 1
        soma_total = soma_total + c
    if d > 0:
        posit = posit + 1
        soma_total = soma_total + d
    if e > 0:
        posit = posit + 1
        soma_total = soma_total + e
    if f > 0:
        posit = posit + 1
        soma_total = soma_total + f
        
    return posit, soma_total
    # Casos onde irá verificar os
    # números positivos e somá-los
    # para saber o total e retorná-los.

def media (posit, soma_total):
    return soma_total / posit
    # Função que retorna a média da soma
    # dos valores positivos e divide pela
    # quantidade de números positivos.

def fnc1 ():
    a = float (input ())
    b = float (input ())
    c = float (input ())
    d = float (input ())
    e = float (input ())
    f = float (input ())
    # Atribuição de valores.
    
    posit, soma_total = positivos (a, b, c, d, e, f)
    media_total = media (posit, soma_total)
    # Atribuição de valores.
    
    print (f'{posit} valores positivos')
    print (f'{media_total:.1f}')
    # Impressão de valores.

fnc1 ()
# Chama a função para ser executada.