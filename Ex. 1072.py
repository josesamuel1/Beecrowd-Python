from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

dentro = fora = 0
rep = int (input ())
# Atribuição de valores.

while rep > 0:
    x = int (input ())
    # Atribuição de valor
    
    if x >= 10 and x <= 20:
        dentro += 1
        # Caso 'x' esteja dentro dos valores
        # predeterminados da questão.
    else:
        fora += 1
        # Caso contrário.

    rep -= 1

print (f'{dentro} in')
print (f'{fora} out')
# Impressão de valores.

# # # # # # # # # # # # # # #

# dentro = fora = 0
# rep = int (input ())
#
# for _ in range (rep):
#     x = int (input ())
#
#     if x >= 10 and x <= 20:
#         dentro += 1
#     else:
#         fora += 1
#
# print (f'{dentro} in')
# print (f'{fora} out')