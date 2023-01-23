from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

def calculo (n, d):
    return n / d
    # Função que retorna o consumo
    # médio do automóvel.

def fnc1 ():
    n = int (input())
    d = float (input())
    # Atribuição de valores.
    
    print (f'{calculo (n, d):.3f} km/l')
    # Comando função e impressão que
    # retorna o consumo do automóvel.
    
fnc1 ()
# Chama a função para ser executada.

# # # # # # # # # # # # # # #

# X = int (input ())
# Y = float (input ())
#
# print (f'{X / Y:.3f} km/l')