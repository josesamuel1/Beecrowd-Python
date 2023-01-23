from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

# EXEMPLO 1043:
def fnc1 ():
    a, b, c = map (float, input().split())
    # Atribuição de valores.
    
    if abs(b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
        per = perimetro(a, b, c)
        print (f"Perimetro = {per:.1f}")
        # Caso os valores inseridos
        # formem um triângulo.
    else:
        ar = area(a, b, c)
        print (f"Area = {ar:.1f}")
        # Caso os valores inseridos
        # não formem um triângulo.

def perimetro (a, b, c):
    return a + b + c
    # Função que retornará
    # o valor do perímetro.

def area (a, b, c):
    return ((a + b) / 2) * c
    # Função que retornará
    # o valor da área.

fnc1 ()
# Chama a função para ser executada.

# # # # # # # # # # # # # # #

# x, y, z = map (float, input().split())
#
# if abs(y - z) < x < (y + z) and (x - z) < y < (x + z) and (x - y) < z < (x + y):
#     per = x + y + z
#     print (f'Perimetro = {per:.1f}')
#
# else:
#     area = (((x + y) / 2) * z)
#     print (f'Area = {area:.1f}')

# EXEMPLO 1045:
# def calculo (a, b, c, d, e, f):
#     if a >= b and a >= c:
#         d = a
#         if b >= c:
#             e = b
#             f = c
#         else:
#             e = c
#             f = b
#     if b >= a and b >= c:
#         d = b
#         if a >= c:
#             e = a
#             f = c
#         else:
#             e = c
#             f = a
#
#     if c >= a and c >= b:
#         d = c
#         if a >= b:
#             e = a
#             f = b
#         else:
#             e = b
#             f = a
#
#     if a == b and b == c:
#         d = a
#         e = b
#         f = c
#     # Casos que detectarão que tipo
#     # de triângulo é formado de acordo
#     # com os valores inseridos,
#
#     a = d
#     b = e
#     c = f
#
#     if a >= (b + c):
#         print ('NAO FORMA TRIANGULO')
#         # Caso onde o 'a' é maior ou igual
#         # que a soma de 'b' e 'c'.
#     else:
#         if (a ** 2) == (b ** 2 + c ** 2):
#             print ('TRIANGULO RETANGULO')
#
#         if (a ** 2) > (b ** 2 + c ** 2):
#             print ('TRIANGULO OBTUSANGULO')
#
#         if (a ** 2) < (b ** 2 + c ** 2):
#             print ('TRIANGULO ACUTANGULO')
#
#         if (a == b == c):
#             print ('TRIANGULO EQUILATERO')
#
#         if a == b != c or b == c != a or a == c != b:
#             print ('TRIANGULO ISOSCELES')
#     # Casos onde será informado
#     # que tipo de triângulo os
#     # valores formam.
#
# def fnc1 ():
#     a, b, c = map (float, input().split())
#     d = float (1)
#     e = float (1)
#     f = float (1)
#     # Atribuição de valores
#
#     calculo (a, b, c, d, e, f)
#     # Chama a função para ser executada.
#
# fnc1 ()
# # Chama a função para ser executada.