from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

x = 1
# Atribuição de valor para contagem.

y = int (input ())
# Atribuição de valor.

while x <= y:
    if y % x == 0:
        print (x)
        # Condição que irá imprimir
        # todos os números que, quando
        # divididos por 'x', dêem 0.
    x += 1
    # Atribuição de valor para contagem