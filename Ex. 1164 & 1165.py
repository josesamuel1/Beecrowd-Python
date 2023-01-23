from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

# EXEMPLO 1164:
rep = int (input ())
# Atribuição de valor para contagem.

for _ in range (rep):
    soma = cont = 0
    x = int (input ())
    # Atribuição de valor.

    while soma < x:
        cont += 1
        soma += cont
        # Condição para somar 'soma' até que
        # o mesmo seja igual ou maior que 'x'.
    
    if soma == x and soma != 1:
        print (f'{x} eh perfeito')
        # Caso soma seja igual à 'x' e diferente de 1.
    else:
        print (f'{x} nao eh perfeito')
        # Caso contrário.

# # # # # # # # # # # # # # #

# EXEMPLO 1165:
# rep = int (input ())
# # Atribuição de valor para contagem.
#
# for _ in range (rep):
#     cont = 0
#     x = int (input ())
#     # Atribuição de valores.
#
#     for i in range (1, x + 1):
#         if x % i == 0:
#             cont += 1
#             # Condição e cálculo para saber
#             # se 'x' é um número primo.
#
#     if cont == 2:
#         print (f'{x} eh primo')
#         # Caso onde 'x' somente é divisível
#         # por 2 números (1 e ele mesmo).
#     else:
#         print (f'{x} nao eh primo')
#         # Caso contrário.