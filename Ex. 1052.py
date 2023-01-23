from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

meses = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
} # Dicionário contendo as
  # informações da questão.

def mes_escolhido (meses):
    mes = int (input ())
    # Atribuição de valor.

    for code, month in meses.items():
        if mes == code:
            print (month)
        # Casos onde irá imprimir o respectivo
        # mês informado pelo usuário.

mes_escolhido (meses)
# Chama a função para ser executada.

# # # # # # # # # # # # # # #

# def fnc1 ():
#     mes = int (input ())
#
#     mes_escolhido (mes)
#
# def mes_escolhido (mes):
#     meses = {
#         1: "January",
#         2: "February",
#         3: "March",
#         4: "April",
#         5: "May",
#         6: "June",
#         7: "July",
#         8: "August",
#         9: "September",
#         10: "October",
#         11: "November",
#         12: "December"
#     }
#
#     if 1 <= mes <= 12:
#         for i in range (1, mes + 1):
#             if i % mes == 0:
#                 print (meses[i])
#
# fnc1 ()