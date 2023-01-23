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
    soma = 0
    # Atribuição de valor.

    for i in range (x, y + 1):
        if i % 13 != 0:
            soma += i
            # Condição que irá somar todos os números de
            # 'x' à 'y' que não são divisíveis por 13.

    print (soma)
    # Impressão de valor.

fnc1 ()
# Chama a função para ser executada.

# # # # # # # # # # # # # # #

# soma = 0
# x = int (input ())
# y = int (input ())
#
# if x > y:
#     aux = x
#     x = y
#     y = aux
#
# for i in range (x, y + 1):
#     if i % 13 != 0:
#         soma += i
#
# print (soma)