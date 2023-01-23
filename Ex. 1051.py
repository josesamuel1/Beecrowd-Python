from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

def fnc1 ():
    salario = float (input ())
    # Atribuição de valor.
    
    if salario <= 2000.00:
        print ('Isento')

    elif 2000.00 < salario <= 3000.00:
        imp = imp8 (salario)
        print (f'R$ {imp:.2f}')

    elif 3000.00 < salario <= 4500.00:
        imp = imp18 (salario)
        print (f'R$ {imp:.2f}')

    elif salario > 4500.00:
        imp = imp28 (salario)
        print (f'R$ {imp:.2f}')
    # Casos de impressão para cada valor do
    # imposto de renda que depende do salário.


def imp8 (salario):
    return (salario - 2000) * (8/100)
    # Retorna o salário com imposto.

def imp18 (salario):
    return (salario - 3000) * (18/100) + (8/100) * 1000
    # Retorna o salário com imposto.

def imp28 (salario):
    return (salario - 4500) * (28/100) + (8/100) * 1000 + (18/100) * 1500
    # Retorna o salário com imposto.

fnc1 ()
# Chama a função para ser executada.