from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

vetor = []
# Atribuição de valor.

def fnc1 ():
    x = int (input ())
    # Atribuição de valor.
    
    fnc2 (x)
    # Chama a função para ser executada.

def fnc2 (x):
    for i in range (10):
        vetor.append (x)
        # Insere o valor no vetor.
        
        if vetor[i] <= 0:
            vetor[i] = 1
            # Condição que verifica se o valor inserido é
            # menor ou igual à 0, para que o substitua por 1.
        
        print (f'X[{i}] = {vetor[i]}')
        # Impressão de valores.

fnc1 ()
# Chama a função para ser executada.

# # # # # # # # # # # # # # #

# vetor = []
# # Atribuição de valor.
#
# for i in range (10):
#     vetor.append (int (input ()))
#     # Atribuição de valor.
#
#     if vetor[i] <= 0:
#         vetor[i] = 1
#     # Condição que verifica se o valor inserido é
#     # menor ou igual à 0, para que o substitua por 1.
#
#     print (f'X[{i}] = {vetor[i]}')
#     # Impressão de valores.

# # # # # # # # # # # # # # #

# i = 0
# vetor = []
#
# while len (vetor) < 10:
#     vetor.append (int (input ()))
#
#     if vetor[i] <= 0:
#         vetor[i] = 1
#
#     print (f'X[{i}] = {vetor[i]}')
#
#     i += 1