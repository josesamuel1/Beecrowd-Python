from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

def calculo (dinh):
    d100 = dinh // 100
    dinh = dinh - d100 * 100

    d50 = dinh // 50
    dinh = dinh - d50 * 50

    d20 = dinh // 20
    dinh = dinh - d20 * 20

    d10 = dinh // 10
    dinh = dinh - d10 * 10

    d5 = dinh // 5
    dinh = dinh - d5 * 5

    d2 = dinh // 2
    dinh = dinh - d2 * 2

    d1 = dinh // 1
    dinh = dinh - d1 * 1
    
    return d100, d50, d20, d10, d5, d2, d1
    # Função que retornará a quantidade de cédulas
    # que existem na variável indicada pelo usuário.

def fnc1 ():
    dinh = int (input ())
    d100, d50, d20, d10, d5, d2, d1 = calculo (dinh)
    # Atribuição de valores.
    
    print (dinh)
    print(f'{d100} nota(s) de R$ 100,00')
    print(f'{d50} nota(s) de R$ 50,00')
    print(f'{d20} nota(s) de R$ 20,00')
    print(f'{d10} nota(s) de R$ 10,00')
    print(f'{d5} nota(s) de R$ 5,00')
    print(f'{d2} nota(s) de R$ 2,00')
    print(f'{d1} nota(s) de R$ 1,00')
    # Impressão de valores.

fnc1 ()
# Chama a função para ser executada.