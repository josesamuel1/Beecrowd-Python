from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

def caso (x, y):
    if x == 0:
        if y == 0:
            r = "Origem"
        if y != 0:
            r = "Eixo Y"

    if y == 0:
        if x != 0:
            r = "Eixo X"

    if x > 0:
        if y > 0:
            r = "Q1"
        if y < 0:
            r = "Q4"

    if x < 0:
        if y > 0:
            r = "Q2"
        if y < 0:
            r = "Q3"

    return r
    # Função que irá detectar onde
    # o ponto se encontra de acordo
    # com as coordenadas inseridas.

def fnc1 ():
    x, y = map (float, input().split())
    # Atribuição de valores.
    
    print (caso (x, y))
    # Comando função e impressão que
    # retorna a posição do ponto.

fnc1 ()
# Chama a função para ser executada.

# # # # # # # # # # # # # # #

# x, y = map (float, input().split())
#
# if x == 0:
#     if y == 0:
#         print("Origem")
#     if y != 0:
#         print("Eixo Y")
#
# if y == 0:
#     if x != 0:
#         print("Eixo X")
#
# if x > 0:
#     if y > 0:
#         print("Q1")
#     if y < 0:
#         print("Q4")
#
# if x < 0:
#     if y > 0:
#         print("Q2")
#     if y < 0:
#         print("Q3")