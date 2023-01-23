from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

def fnc1 ():
    rep = int (input ())
    # Atribuição de valor para contagem.
    
    fnc2 (rep)
    # Chama a função para ser executada.

def fnc2 (rep):
    while rep > 0:
        soma = 0
        x, y = map (int, input().split())
        # Atribuição de valores.
        
        if x > y:
            aux = x
            x = y
            y = aux
        # Identificação para que sempre o
        # 'x' seja o menor número.
        
        x += 1
        # Atribuição de valor para contagem.
        
        while x < y:
            if x % 2 == 1:
                soma += x
            x += 1
        # Caso onde irá somar todos os números
        # ímpares existentes entre 'x' e 'y'.
        
        rep -= 1
        # Decaimento de valor de contagem.
    
        print (soma)
        # Impressão de valor.

fnc1 ()
# Chama a função para ser executada.

# # # # # # # # # # # # # # #

# rep = int (input ())
#
# while rep > 0:
#     soma = 0
#     x, y = map (int, input().split())
#
#     if x > y:
#         aux = x
#         x = y
#         y = aux
#
#     x += 1
#
#     while x < y:
#         if x % 2 == 1:
#             soma += x
#         x += 1
#
#     rep -= 1
#    
#     print (soma)