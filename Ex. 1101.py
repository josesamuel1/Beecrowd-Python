from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

def fnc1 ():
    while True:
        x, y = map (int, input().split())
        # Atribuição de valores.
    
        if x <= 0 or y <= 0:
            break
        # Condição de parada caso 'x'
        # ou 'y' sejam iguais a 0.
        
        if x > y:
            aux = x
            x = y
            y = aux
        # Identificação para que sempre o
        # 'x' seja o menor número.
        
        fnc2 (x, y)
        # Chama a função para ser executada.

def fnc2 (x, y):
    soma = 0
    # Atribuição de valor.
    
    while x <= y:
        print (x, end=' ')
        # Impressão de valores que estão
        # entre 'x' e 'y', inclusive os mesmos.
        
        soma += x
        x += 1
        # Atribuição de valores.
        
    # Caso de repetição até que a
    # condição de parada seja verdadeira.

    print (f'Sum={soma}')
    # Impressão de valor.

fnc1 ()
# Chama a função para ser executada.

# # # # # # # # # # # # # # #

# while True:
#     x, y = map(int, input().split())
#
#     if x <= 0 or y <= 0:
#         break
#
#     if x > y:
#         aux = x
#         x = y
#         y = aux
#
#     soma = 0
#     while x <= y:
#         print (x, end=' ')
#         soma += x
#         x += 1
#
#     print (f'Sum={soma}')