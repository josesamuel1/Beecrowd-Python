from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

lin = int (input ())
# Atribuição de valor.

xlin = lin * 4
# Multiplicação de 'lin' em 4 e armazenando
# seu valor na variável 'xlin'.

for x in range (1, xlin + 1):
    if x % 4 == 0:
        print ('PUM')
        # Caso onde a divisão de
        # 'x' por 4 seja igual a 0.

    else:
        print (x, end=' ')
        # Caso onde a divisão de 'x'
        # por 4 não seja igual a 0.