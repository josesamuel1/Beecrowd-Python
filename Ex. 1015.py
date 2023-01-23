from os import system
from math import sqrt
# Livraria 'os/system' e 'math/sqrt'.
system ('cls')
# Limpa o terminal.

def distancia (x1, x2, y1, y2):
    return sqrt ((x2 - x1)**2 + (y2 - y1)**2)
    # Função que retornará a raiz quadrada
    # dos valores inseridos pelo usuário.

def fnc1 ():
    x1, y1 = map (float, input().split())
    x2, y2 = map (float, input().split())
    # Atribuição de valores.
    
    print (f'{distancia (x1, x2, y1, y2):.4f}')
    # Comando função e impressão que
    # retorna o volume total.
    
fnc1 ()
# Chama a função para ser executada.