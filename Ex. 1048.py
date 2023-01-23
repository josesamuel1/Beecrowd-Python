from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

salarios = {
    400.00: 15,
    800.00: 12,
    1200.00: 10,
    2000.00: 7,
    2000.01: 4
} # Dicionário contendo as
  # informações da questão.

def reajuste_salarial (salarios):
    salary = float (input())
    # Atribuição de valor.
    
    for key, percent in salarios.items():
        if salary <= key:
            new_s = salary + (salary * (percent/100))
            reajuste = new_s - salary
            break
        elif salary >= key:
            new_s = salary + (salary * (percent/100))
            reajuste = new_s - salary
    # Condição que irá reajustar
    # o salário do funcionário.
            
    print (f'Novo salario: {new_s:.2f}')
    print (f'Reajuste ganho: {reajuste:.2f}')
    print (f'Em percentual: {percent} %')
    # Impressão de valores.

reajuste_salarial (salarios)
# Chama a função para ser executada
# passando o dicinário como argumento.

# # # # # # # # # # # # # # #

# def novosalario (salario):
#     if 0 < salario <= 400.00:
#         novosalario = salario + (salario * (15/100))
#         reajuste = novosalario - salario
#         percentual = 15
#
#     if 400.01 <= salario <= 800.00:
#         novosalario = salario + (salario * (12/100))
#         reajuste = novosalario - salario
#         percentual = 12
#
#     if 800.01 <= salario <= 1200.00:
#         novosalario = salario + (salario * (10/100))
#         reajuste = novosalario - salario
#         percentual = 10
#
#     if 1200.01 <= salario <= 2000.00:
#         novosalario = salario + (salario * (7/100))
#         reajuste = novosalario - salario
#         percentual = 7
#
#     if salario > 2000.00:
#         novosalario = salario + (salario * (4/100))
#         reajuste = novosalario - salario
#         percentual = 4
#
#     return novosalario, reajuste, percentual
#
# def fnc1 ():
#     salario = float (input())
#     ns, reaj, percent = novosalario (salario)
#
#     print (f'Novo salario: {ns:.2f}')
#     print (f'Reajuste ganho: {reaj:.2f}')
#     print (f'Em percentual: {percent} %')
#
# fnc1 ()