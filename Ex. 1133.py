from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

def fnc1 ():
    x = int (input ())
    y = int (input ())
    # Atribuição de valores.

    if x > y:
        aux = x
        x = y
        y = aux
        # Caso onde 'x' deve sempre
        # ser o menor número.

    fnc2 (x, y)
    # Chama a função para ser executada.

def fnc2 (x, y):
    for i in range (x + 1, y):
        if i % 5 == 2 or i % 5 == 3:
            print (i)
            # Função e condição que irá imprimir todos os números
            # que sua divisão por 5 sejam iguais à 2 ou 3.

fnc1 ()
# Chama a função para ser executada.

# # # # # # # # # # # # # # #

# x = int (input ())
# y = int (input ())
#
# if y < x:
#     aux = x
#     x = y
#     y = aux
#
# for i in range (x + 1, y):
#     if i % 5 == 2 or i % 5 == 3:
#             print (i)