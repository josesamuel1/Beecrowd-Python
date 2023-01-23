from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

def calculo (t):
    h = t // 3600
    t = t - h * 3600

    m = t // 60
    t = t - m * 60

    s = t
    return h, m, s
    # Função que retornará o tempo em h:m:s.
    
def fnc1 ():
    t = int (input ())
    hr, min, seg = calculo (t)
    # Atribuição de valores.
    
    print (f'{hr}:{min}:{seg}')
    # Impressão de valores.

fnc1 ()
# Chama a função para ser executada.

# # # # # # # # # # # # # #

# tempo = int(input())
#
# horas = tempo // 3600
# tempo = tempo - horas * 3600
#
# minutos = tempo // 60
# tempo = tempo - minutos * 60
#
# segundos = tempo
#
# print (f"{horas}:{minutos}:{segundos}")