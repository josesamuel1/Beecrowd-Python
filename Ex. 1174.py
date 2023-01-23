from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

vetor = []
# Atribuição de valor.

def fnc1 ():
    for _ in range (100):
        x = float (input ())
        # Atribuição de valores.
        
        vetor.append (x)
        # Insere o valor no vetor.
        
    fnc2 (vetor)
    # Chama a função para ser executada.
    
def fnc2 (vetor):
    for i in range (100):
        if vetor[i] <= 10:
            print (f'A[{i}] = {vetor[i]}')
    
    # Função que irá imprimir todos os números
    # menores que 10 e suas posições no vetor.

fnc1 ()
# Chama a função para ser executada.

# # # # # # # # # # # # # # #

# vetor = []
# i = j = 0
#
# while i < 100:
#
#     x = float (input ())
#     vetor.append (x)
#
#     i += 1
#
# while j < 100:
#
#     if vetor[j] <= 10:
#         print (f'A[{j}] = {vetor[j]}')
#
#     j += 1