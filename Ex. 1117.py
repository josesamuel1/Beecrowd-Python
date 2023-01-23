from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

def fnc1 ():
    n1 = float (input ())
    # Atribuição de valor.
    
    while n1 < 0 or n1 > 10:
        print ('nota invalida')
        n1 = float (input ())
        # Condição onde somente aceitará
        # notas inseridas entre 0 e 10.
    
    n2 = float (input ())
    # Atribuição de valor.
    
    while n2 < 0 or n2 > 10:
        print ('nota invalida')
        n1 = float (input ())
        # Condição onde somente aceitará
        # notas inseridas entre 0 e 10.
    
    calculo (n1, n2)
    # Chama a função para ser executada.

def calculo (n1, n2):
    print (f'media = {(n1 + n2) / 2:.2f}')
    # Função que irá imprimir a média do aluno
    # com base nos dados inseridos pelo usuário.

# # # # # # # # # # # # # # #

# nota1 = float (input ())
#
# while nota1 < 0 or nota1 > 10:
#     print ('nota invalida')
#     nota1 = float (input ())
#
# nota2 = float (input ())
#
# while nota2 < 0 or nota2 > 10:
#     print ('nota invalida')
#     nota2 = float (input ())
#
# print (f'media = {(nota1 + nota2) / 2:.2f}')