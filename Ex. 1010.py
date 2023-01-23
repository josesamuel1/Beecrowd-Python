from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

def calculo (n1, v1, n2, v2):
    return n1 * v1 + n2 * v2
# Função que retorna o valor total dos
# números inseridos pelo usuário.

def fnc1 ():
    _, n1, v1 = input().split()
    _, n2, v2 = input().split()
    # Atribuição de valores.
    
    n1 = int (n1)
    n2 = int (n2)
    v1 = float (v1)
    v2 = float (v2)
    # Casting nas variáveis.
    
    print (f'VALOR A PAGAR: R$ {float (calculo (n1, v1, n2, v2)):.2f}')
    # Função que retorna o valor total do
    # produto inserido pelo usuário.

fnc1 ()
# Chama a função para ser executada.

# # # # # # # # # # # # # # #

# _, qtda_1, vlr_1 = input().split()
# _, qtda_2, vlr_2 = input().split()
#
# qtda_1 = int (qtda_1)
# qtda_2 = int (qtda_2)
# vlr_1 = float (vlr_1)
# vlr_2 = float (vlr_2)
#
# print (f'VALOR A PAGAR: R$ {(qtda_1 * vlr_1 + qtda_2 * vlr_2):.2f}')