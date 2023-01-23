from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

pos = 0
# Atribuição de valor.

for x in range (5):
    num = int (input ())
    # Atribuição de valor.
    
    if num % 2 == 0:
        pos += 1
        # Para cada valor que 'num' assumir e que
        # o resto da sua divisão seja igual a 0,
        # a contagem de números positivos aumentará.

print (f'{pos} valores pares')
# Impressão de valores.