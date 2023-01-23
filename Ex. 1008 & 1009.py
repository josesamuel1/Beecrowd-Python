from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

# EXEMPLO 1008:
def salario (num_horas, valor_hora):    
    return num_horas * valor_hora
# Função que retorna a diferença dos
# números inseridos pelo usuário.

def fnc1 ():
    num_func = int (input ())
    num_horas = int (input ())
    valor_hora = float (input ())
    # Atribuição de valores.

    print(f'NUMBER = {num_func}')
    # Impressão do número do funcionário.
    print(f'SALARY = U$ {salario (num_horas, valor_hora):.2f}')
    # Comando função e impressão que retorna o
    # salário ganho com base nos valores inseridos.

fnc1 ()
# Chama a função para ser executada.

# # # # # # # # # # # # # # #

# EXEMPLO 1009:
# def fnc1 ():
#     nome = str (input ())
#     sfixo = float (input ())
#     totalvendas = float (input ())
#
#     print (f'TOTAL = R$ {calculo (sfixo, totalvendas):.2f}')
#
# def calculo (sfixo, totalvendas):
#     return sfixo + (totalvendas * (15/100))
#
# fnc1 ()