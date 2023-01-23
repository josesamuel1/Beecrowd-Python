from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

pi = 3.14159
# Valor do pi da atual questão.

def calculos (x, y, z):
    a_trin = (x * z) / 2
    a_circ = pi * (z * z)
    a_trap = z * (x + y) / 2
    a_quad = y * y
    a_retn = x * y
    return a_trin, a_circ, a_trap, a_quad, a_retn
    # Função que retorna o valor das áreas.
    
def fnc1 ():
    x, y, z = map (float, input().split())
    a1, a2, a3, a4, a5 = calculos (x, y, z)
    # Atribuição de valores.
    
    print (f'TRIANGULO: {a1:.3f}\nCIRCULO: {a2:.3f}\nTRAPEZIO: {a3:.3f}\nQUADRADO: {a4:.3f}\nRETANGULO: {a5:.3f}')
    # Impressão de valores.
    
fnc1 ()
# Chamada de função para ser executada.