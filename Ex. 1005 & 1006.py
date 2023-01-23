from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

# EXEMPLO 1005:
def fnc1 ():
    x = float (input ())
    y = float (input ())
    # Atribuição de valores.
    
    print (f'MEDIA = {media (x, y):.5f}')
    # Comando função e impressão que
    # retorna a média dos valores.

def media (x, y):
    return (x * 3.5 + y * 7.5) / 11
# Função que retorna a média dos
# números inseridos pelo usuário
# com base nos pesos da questão.

fnc1 ()
# Chama a função para ser executada.

# # # # # # # # # # # # # # #

# A = float (input ())
# B = float (input ())
#
# print (f'MEDIA = {(((A * 3.5) + (B * 7.5)) / 11):.5f}')

# EXEMPLO 1006:
# def media (x, y, z):
#     return ((A * 2) + (B * 3) + (C * 5)) / 10
#     # Função que retornará a
#     # média total do aluno.
#
# def fnc1 ():
#     x = float (input ())
#     y = float (input ())
#     z = float (input ())
#     # Atribuição de valores.
#
#     print (f'MEDIA = {media (x, y, z):.5f}')
#     # Impressão de valores.
# 
# fnc1 ()
# # Chama a função para ser executada.