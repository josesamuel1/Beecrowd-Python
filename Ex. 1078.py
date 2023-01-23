from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

def tabuada (num):
    for tab in range (1, 11):
        print (f'{tab} x {num} = {tab * num}')
        # Condição que irá imprimir o valor de 'num'
        # de acordo com a tabuada de 1 à 10.

def fnc1 ():
    num = int (input ())
    # Atribuição de valor.
    
    tabuada (num)
    # Chama a função para ser executada.

fnc1 ()
# Chama a função para ser executada.

# # # # # # # # # # # # # # #

# num = int (input ())
# tab = 1
#
# while tab < 11:
#     print (f'{tab} x {num} = {tab * num}')
#     tab += 1