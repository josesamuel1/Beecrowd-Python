from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

impares = int (input ())
lim_imp = impares + 12
# Atribuição de valores.

# 'lim_imp' terá esse valor por conta que pegará
# os 6 próximos números pares e ímpares, mas no
# cálculo da questão, esses números ímpares serão
# filtrados e exibidos ao usuário.

while impares < lim_imp:
    if impares % 2 == 1:
        print (impares)
    
    impares += 1
    # Para cada valor que ímpar assumir, será
    # imprimido os próximos 6 números ímpares.

# # # # # # # # # # # # # # #

# x = int (input ())
#
# for impares in range (x, x + 12):
#     if impares % 2 == 1:
#         print (impares)