from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

# EXEMPLO 1095:
i = 1
j = 60
# Atribuição de valores.

while j >= 0:
    print (f'I={i} J={j}')
    i = i + 3
    j = j - 5
    # Impressão de valores com base na
    # sequência requerida pela questão.

# # # # # # # # # # # # # # #

# EXEMPLO 1096:
# i = 1
# j = 7
#
# while i <= 9:
#     print (f'I={i} J={j}')
#     j = j - 1
#     if j == 4:
#         i = i + 2
#         j = j + 3

# EXEMPLO 1097:
# i = 1
# j = 7
# k = 4
#
# while i < 10:
#     print (f'I={i} J={j}')
#     j -= 1
#     if j == k:
#         i += 2
#         j += 5
#         k = j - 3

# EXEMPLO 1098:
# i = 0
# j = k = 1
#
# while i <= 2:
#     while k < 4:
#         if i > 2.19:
#             print(f'I={i:.0f} J={j:.0f}')
#         if i == 1.0 or i == 0.0 or i > 1.8:
#             print(f'I={i:.0f} J={j:.0f}')
#         elif i < 2:
#             print(f'I={i:.1f} J={j:.1f}')
#         j += 1
#         k += 1
#     i += 0.2
#     j = 1 + i
#     k = 1