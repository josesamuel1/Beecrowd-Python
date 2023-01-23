from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

vetor = []
# Atribuição de valor.

def fnc2 (x):
    for i in range (10):
        
        vetor.append (x)
        # Insere o valor no vetor.
        
        print (f'N[{i}] = {vetor[i]}')
        # Impressão de valor.
        
        x += x
        # Atribuição de valor para contagem.
    
    # Função que irá preencher um vetor com um número
    # inserido pelo usuário e, durante 9 repetições, irá
    # preencher a seguinte casa com o dobro da anterior.

def fnc1 ():
    x = int (input ())
    # Atribuição de valor.
    
    fnc2 (x)
    # Chama a função para ser executada.

fnc1 ()
# Chama a função para ser executada.

# # # # # # # # # # # # # # #

# i = 0
# vetor = []
# x = int (input ())
#
# while i < 10:
#     vetor.append (x)
#
#     print (f'N[{i}] = {vetor[i]}')
#
#     x += x
#     i += 1