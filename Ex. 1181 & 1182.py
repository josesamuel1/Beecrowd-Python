from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

# EXEMPLO 1181:
matriz = []
# Atribuição de valor.

def monta_matriz ():
    linha = int (input ())
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
        
    soma_ou_media (matriz, linha, op)
    # Chama a função para ser executada.
    
def soma_ou_media (matriz, linha, op):
    soma = 0
    # Atribuição de valor.
    
    for i in range (12):
        soma += matriz[linha][i]
        # Cálculo para a soma total de
        # uma única linha na matriz.

    if op == 'S':
        print (f'{soma:.1f}')
        # Caso que irá imprimir
        # a soma total da linha.

    elif op == 'M':
        print (f'{soma / 12:.1f}')
        # Caso que irá imprimir
        # a média total da linha.
    
    # Função que irá imprimir a soma total ou a média
    # de valores de uma linha informada pelo usuário.
        
monta_matriz ()
# Chama a função para ser executada.

# # # # # # # # # # # # # # #

# EXEMPLO 1182:
# matriz = []
# # Atribuição de valor.
#
# def monta_matriz ():
#     coluna = int (input ())
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
#     soma_ou_media (matriz, coluna, op)
#     # Chama a função para ser executada.
#
# def soma_ou_media (matriz, coluna, op):
#     soma = 0
#     # Atribuição de valor.
#
#     for i in range (12):
#         soma += matriz[i][coluna]
#         # Cálculo para a soma total de
#         # uma única coluna na matriz.
#
#     if op == 'S':
#         print (f'{soma:.1f}')
#         # Caso que irá imprimir
#         # a soma total da coluna.
#
#     elif op == 'M':
#         print (f'{soma / 12:.1f}')
#         # Caso que irá imprimir
#         # a média total da coluna.
#
#     # Função que irá imprimir a soma total ou a média
#     # de valores de uma coluna informada pelo usuário.
#
# monta_matriz ()
# # Chama a função para ser executada.