from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

def verifica (x, y, z):
    if x > y and x > z:
        d = x
        if y > z:
            e = y
            f = z
        else:
            e = z
            f = y
    if y > x and y > z:
        d = y
        if x > z:
            e = x
            f = z
        else:
            e = z
            f = x
    if z > x and z > y:
        d = z
        if x > y:
            e = x
            f = y
        else:
            e = y
            f = x
    # Casos para ordenar os valores
    # inseridos de forma crescente.
    
    print (f)
    print (e)
    print (d)
    print ()
    print (x)
    print (y)
    print (z)
    # Impressão de valores.

def fnc1 ():
    x, y, z = map (int, input().split())
    # Atribuição de valores.
    
    verifica (x, y, z)
    # Chama a função para ser executada.

fnc1 ()
# Chama a função para ser executada.