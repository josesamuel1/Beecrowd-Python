from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

rep = int (input())
# Atribuição de valor para contagem.

for _ in range (rep):
    x, y = map (int, input().split())
    # Atribuição de valores.

    if y == 0:
        print ('divisao impossivel')
        # Caso onde 'y' é igual a 0, onde
        # a divisão não é possível.

    else:
        divs = x / y
        print (divs)
        # Caso contrário.