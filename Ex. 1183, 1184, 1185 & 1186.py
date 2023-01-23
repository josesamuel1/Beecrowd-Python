from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

# EXEMPLO 1183:
matriz = []
# Atribuição de valor.

def monta_matriz ():
    op = str (input ())
    # Atribuição de valores.
    
    for i in range (12):
        array = []
        # Atribuição de valor.
        
        for j in range (12):
            array.append (float (input ()))
            # Insere o valor no vetor.
        
        matriz.append (array)
        # Insere o valor no vetor.
    
    # Condição de repetição que irá montar uma matriz
    # 12x12 com os valores inseridos pelo usuário.
        
    soma_ou_media (matriz, op)
    # Chama a função para ser executada.
    
def soma_ou_media (matriz, op):
    soma = cont = 0
    # Atribuição de valor.
    
    for linha in range (12):
        for coluna in range (12):
            if linha < coluna:
                soma += matriz[linha][coluna]
                # Cálculo para a soma total do volume
                # acima da diagonal principal na matriz.
                cont += 1

    if op == 'S':
        print (f'{soma:.1f}')
        # Caso que irá imprimir a soma total do volume
        # acima da diagonal principal na matriz.

    elif op == 'M':
        print (f'{soma / cont:.1f}')
        # Caso que irá imprimir a média total do volume
        # acima da diagonal principal na matriz.
    
    # Função que irá imprimir a soma total ou a média
    # de valores acima da diagonal principal.
        
monta_matriz ()
# Chama a função para ser executada.

# # # # # # # # # # # # # # #

# EXEMPLO 1184:
# matriz = []
# # Atribuição de valor.
#
# def monta_matriz ():
#     op = str (input ())
#     # Atribuição de valores.
#
#     for i in range (12):
#         array = []
#         # Atribuição de valor.
#
#         for j in range (12):
#             array.append (float (input ()))
#             # Insere o valor no vetor.
#
#         matriz.append (array)
#         # Insere o valor no vetor.
#
#     # Condição de repetição que irá montar uma matriz
#     # 12x12 com os valores inseridos pelo usuário.
#
#     soma_ou_media (matriz, op)
#     # Chama a função para ser executada.
#
# def soma_ou_media (matriz, op):
#     soma = cont = 0
#     # Atribuição de valor.
#
#     for linha in range (12):
#         for coluna in range (12):
#             if linha > coluna:
#                 soma += matriz[linha][coluna]
#                 # Cálculo para a soma total do volume
#                 # abaixo da diagonal principal na matriz.
#                 cont += 1
#
#     if op == 'S':
#         print (f'{soma:.1f}')
#         # Caso que irá imprimir a soma total do volume
#         # abaixo da diagonal principal na matriz.
#
#     elif op == 'M':
#         print (f'{soma / cont:.1f}')
#         # Caso que irá imprimir a média total do volume
#         # abaixo da diagonal principal na matriz.
#
#    # Função que irá imprimir a soma total ou a média
#    # de valores abaixo da diagonal principal.
#
# monta_matriz ()
# # Chama a função para ser executada.

# EXEMPLO 1185:
# matriz = []
# # Atribuição de valor.
#
# def monta_matriz ():
#     op = str (input ())
#     # Atribuição de valores.
#
#     for i in range (12):
#         array = []
#         # Atribuição de valor.
#
#         for j in range (12):
#             array.append (float (input ()))
#             # Insere o valor no vetor.
#
#         matriz.append (array)
#         # Insere o valor no vetor.
#
#     # Condição de repetição que irá montar uma matriz
#     # 12x12 com os valores inseridos pelo usuário.
#
#     soma_ou_media (matriz, op)
#     # Chama a função para ser executada.
#
# def soma_ou_media (matriz, op):
#     soma = cont = 0
#     cont2 = 12
#     # Atribuição de valor.
#
#     for linha in range (12):
#         cont2 -= 1
#         for coluna in range (12):
#             if coluna < cont2:
#                 soma += matriz[linha][coluna]
#                 # Cálculo para a soma total do volume
#                 # acima da diagonal secundária na matriz.
#                 cont += 1
#
#     if op == 'S':
#         print (f'{soma:.1f}')
#         # Caso que irá imprimir a soma total do volume
#         # acima da diagonal secundária na matriz.
#
#     elif op == 'M':
#         print (f'{soma / cont:.1f}')
#         # Caso que irá imprimir a média total do volume
#         # acima da diagonal secundária na matriz.
#
#     # Função que irá imprimir a soma total ou a média
#     # de valores acima da diagonal secundária na matriz.
#
# monta_matriz ()
# # Chama a função para ser executada.

# EXEMPLO 1186:
# matriz = []
# # Atribuição de valor.
#
# def monta_matriz ():
#     op = str (input ())
#     # Atribuição de valores.
#
#     for i in range (12):
#         array = []
#         # Atribuição de valor.
#
#         for j in range (12):
#             array.append (float (input ()))
#             # Insere o valor no vetor.
#
#         matriz.append (array)
#         # Insere o valor no vetor.
#
#     # Condição de repetição que irá montar uma matriz
#     # 12x12 com os valores inseridos pelo usuário.
#
#     soma_ou_media (matriz, op)
#     # Chama a função para ser executada.
#
# def soma_ou_media (matriz, op):
#     soma = cont = 0
#     cont2 = 12
#     # Atribuição de valor.
#
#     for linha in range (12):
#         cont2 -= 1
#         for coluna in range (12):
#             if coluna > cont2:
#                 soma += matriz[linha][coluna]
#                 # Cálculo para a soma total do volume
#                 # abaixo da diagonal secundária na matriz.
#                 cont += 1
#
#     if op == 'S':
#         print (f'{soma:.1f}')
#         # Caso que irá imprimir a soma total do volume
#         # abaixo da diagonal secundária na matriz.
#
#     elif op == 'M':
#         print (f'{soma / cont:.1f}')
#         # Caso que irá imprimir a média total do volume
#         # abaixo da diagonal secundária na matriz.
#
#     # Função que irá imprimir a soma total ou a média
#     # de valores abaixo da diagonal secundária na matriz.
#
# monta_matriz ()
# # Chama a função para ser executada.