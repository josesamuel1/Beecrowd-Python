from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

num = int (input ())
# Atribuição de valor.

for x in range (num + 1):
    if x % 2 == 0:
        quad = x ** 2
        print (f"{x}^2 = {quad}")
        # Para cada valor de 'x' que o resto
        # da sua divisão por 2 seja igual a 0,
        # dentro da quantidade de 'num' repetições,
        # o seu valor elevado ao quadrado é impresso.