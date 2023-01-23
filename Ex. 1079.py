from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

def medias (rep):
    for _ in range (rep):
        x, y, z = map (float, input().split())
        # Atribuição de valor.
    
        media = ((x * 2) + (y * 3) + (z * 5)) / 10
        # Cálculo das médias com
        # os respectivos pesos.
    
        print (f'{media:.1f}')
        # Impressão do valor.

def fnc1 ():
    rep = int (input ())
    # Atribuição de valor.
    
    medias (rep)
    # Chama a função para ser executada.

fnc1 ()
# Chama a função para ser executada.

# # # # # # # # # # # # # # #

# rep = int (input ())
#
# for i in range (rep):
#     x, y, z = map (float, input().split())
#     media = ((x * 2) + (y * 3) + (z * 5)) / 10
#     print (f'{media:.1f}')