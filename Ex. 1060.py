from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

pos = 0
# Atribuição de valor.

for num in range (6):
    x = float (input ())
    # Atribuição de valor.
    
    if x > 0:
        pos += 1
        # Para cada valor que 'x' assumir e
        # que seja ele maior que 0, a contagem
        # de números positivos aumentará.

print (f'{pos} valores positivos')
# Impressão de quantidade
# de números positivos.