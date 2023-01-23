from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

pi = 3.14159
# Valor do pi da atual questão.

def area (pi, raio):
    return pi * raio**2
# Função que retorna o valor da área
# do círculo de acordo com o raio informado.

def fnc1 ():
    raio = float (input ())
    # Atribuição de valor.
    
    r = area (raio)
    # Chamada da função.
    
    print (f'A={r:.4f}')
    # Impressão do resultado.

fnc1 ()
# Chama a função para ser executada.

# # # # # # # # # # # # # # #

# pi = 3.14159
# raio = float(input())
#
# area = pi * raio**2
#
# print(f'A={area:.4f}')