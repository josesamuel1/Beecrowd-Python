from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

# EXEMPLO 1177:
vetor = []
# Atribuição de valor.

def preenche_vetor (rep):
    for i in range (1000):
        for j in range (rep):
            vetor.append (j)
            # Insere o valor no vetor.
        
        print (f'N[{i}] = {vetor[i]}')
        # Impressão de valor.
    
    # Função que irá atribuir 'j' valores
    # 'rep' vezes e irá imprimir 'i' vezes.

def fnc1 ():
    rep = int (input ())
    # Atribuição de valor para contagem.
    
    preenche_vetor (rep)
    # Chama a função para ser executada.

fnc1 ()
# Chama a função para ser executada.

# # # # # # # # # # # # # # #

# vetor = []
# i = 0
# rep = int (input ())
#
# while i < 1000:
#     j = 0
#
#     while j < rep:
#         vetor.append (j)
#         j += 1
#
#     print (f'N[{i}] = {vetor[i]}')
#
#     i += 1

# EXEMPLO 1178:
# def preenche_vetor (x):
#     for i in range (100):
#         vetor.append (x)
#         # Insere o valor no vetor.
#
#         print (f'N[{i}] = {vetor[i]:.4f}')
#         # Impressão de valor.
#
#         x /= 2
#         # Cálculo referente à questão.
#
#     # Função que, a cada ciclo, imprimirá
#     # a metade do número inserido pelo
#     # usuário, durante 100 ciclos.
#
# def dados_vetor ():
#     x = float (input ())
#     # Atribuição de valor.
#
#     preenche_vetor (x)
#     # Chama a função para ser executada.
#
# dados_vetor ()
# # Chama a função para ser executada.

# # # # # # # # # # # # # # # #

# # vetor = []
# # x = float (input ())
# # i = 0
# #
# # while i < 100:
# #     vetor.append (x)
# #
# #     print (f'N[{i}] = {vetor[i]:.4f}')
# #
# #     x /= 2
# #     i += 1

# # # # # # # # # # # # # # #

# EXEMPLO 1179:
# vetorpar = []
# vetorimpar = []
# # Atribuição de valores.
#
# for i in range (15):
#     pos = 0
#     # Atribuição de valor para contagem.
#
#     x = int (input ())
#     # Atribuição de valor.
#
#     if x % 2 == 0:
#         vetorpar.append(x)
#         # Caso 'x' seja par.
#     else:
#         vetorimpar.append(x)
#         # Caso 'x' seja ímpar.
#
#     for j in range (5):
#         if len(vetorpar) > 4 or len(vetorimpar) > 4 or i == 14:
#             if len(vetorimpar) > len(vetorpar):
#                 if len(vetorimpar) > 0:
#                     while len(vetorimpar) > 0:
#                         print (f'impar[{pos}] = {vetorimpar[0]}')
#                         pos += 1
#                         vetorimpar.pop(0)
#                     pos = 0
#
#                 elif len(vetorpar):
#                     while len(vetorpar) > 0:
#                         print (f'par[{pos}] = {vetorpar[0]}')
#                         pos += 1
#                         vetorpar.pop(0)
#                     pos = 0
#
#             else:
#                 if len(vetorpar) > 0:
#                     while len(vetorpar) > 0:
#                         print (f'par[{pos}] = {vetorpar[0]}')
#                         pos += 1
#                         vetorpar.pop(0)
#                     pos = 0
#
#                 elif len(vetorimpar):
#                     while len(vetorimpar) > 0:
#                         print (f'impar[{pos}] = {vetorimpar[0]}')
#                         pos += 1
#                         vetorimpar.pop(0)
#                     pos = 0
#
#     # Caso de repetição que irá analisar se 'x' é par ou ímpar, irá
#     # guardar seu valor em um vetor que, ao chegar em um tamanho de
#     # 5 valores, irá imprimir seus valores e suas posições, depois irá
#     # apagar tudo, dentro de um ciclo de no máximo 15 repetições ao total.