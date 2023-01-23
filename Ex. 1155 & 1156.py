from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

# EXEMPLO 1155:
s = 0
divs = 1
# Atribuição de valores.

while divs <= 100:
    s += (1/divs)
    divs += 1
    # Condição que irá somar 's' com
    # ele mesmo, mas sempre com 1 elevado
    # à 'divs' até que o mesmo chegue a 100.

print (f'{s:.2f}')
# Impressão do valor.

# # # # # # # # # # # # # # #

# EXEMPLO 1156:
# s = 0
# divs = x = 1
# # Atribuição de valor.
#
# while x <= 39:
#     s += (x/divs)
#     x += 2
#     divs += divs
#     # Condição que, a cada ciclo, irá somar o
#     # numerador com 2, o denominador com ele mesmo e
#     # depois tudo junto, até que o numerador atinja 39.
#
# print (f'{s:.2f}')
# # Impressão do valor.