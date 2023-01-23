from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

def calculo (a, b):
    return a + b
# Função que retorna a soma dos
# números inseridos pelo usuário.

def fnc1 ():
    a = int (input ())
    b = int (input ())
    # Atribuição de valores.

    print (f'Soma = {calculo (a, b)}')
    # Comando função e impressão que
    # retorna a soma dos valores.

fnc1 ()
# Chama a função para ser executada.

# # # # # # # # # # # # # # #

# a = int(input())
# b = int(input())
#
# soma = a + b
#
# print (f'X = {soma}')