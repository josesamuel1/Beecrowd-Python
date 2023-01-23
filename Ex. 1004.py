from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

def prod (x, y):
    return x * y
# Função que retorna o produto dos
# números inseridos pelo usuário.

def fnc1 ():
    x = int (input ())
    y = int (input ())
    # Atribuição de valores.
    
    print (f'PROD = {prod (x, y)}')
    # Comando função e impressão que
    # retorna o produto dos valores.

fnc1 ()
# Chama a função para ser executada.

# # # # # # # # # # # # # # #

# A = int(input())
# B = int(input())
#
# print(f'PROD = {A * B}')