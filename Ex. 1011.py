from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

pi = 3.14159
# Valor do pi da atual questão.

def calculo (pi, raio):
    return (4.0/3.0) * pi * raio**3
    # Função que retorna o valor do volume
    # de acorco com o raio informado.

def fnc1 ():
    raio = float (input ())
    # Atrtibuição de valor.
    
    print (f'VOLUME = {calculo (pi, raio):.3f}')
    # Comando função e impressão que
    # retorna o volume total.

fnc1 ()
# Chama a função para ser executada.