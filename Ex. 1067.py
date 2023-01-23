from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

x = int (input ())
impares = 1
# Atribuição de valores.

while x > 0:
    if impares % 2 == 1:
        print (impares)
        
    x -= 1
    impares += 1
    # Sendo 'x' o limitador da
    # questão, os números ímpares
    # de 1 até 'x' serão imprimidos.