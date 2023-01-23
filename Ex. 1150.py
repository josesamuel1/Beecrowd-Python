from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

soma = vezes = 0
x = int (input ())
y = int (input ())
# Atribuição de valores.

while y <= x:
    y = int (input ())
    # Condição para que sempre
    # 'y' seja maior que 'x'.

while soma < y:
    soma += x
    x += 1
    vezes += 1
    # Condição que irá contar quantas
    # vezes que 'soma' teve que ser
    # somado para ultrapassar 'y'.

print (vezes)
# Impressão de valores.