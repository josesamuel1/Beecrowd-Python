from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

cond = 1
alc = gas = dis = 0
# Atribuição de valores.

while cond == 1:
    # Comando de laço infinito até que um
    # comando de parada seja executado.
    
    x = int (input ())
    # Atribuição de valor.

    if x < 1 or x > 4:
        x = int (input ())
    # Caso de repetição onde o valor inserido
    # deve estar sempre entre 1 e 4.

    if x == 1:
        alc += 1

    if x == 2:
        gas += 1

    if x == 3:
        dis += 1
    # Casos onde irá ser somado as preferências dos
    # clientes do posto de gasolina, tendo cada tipo
    # de combustível seu valor a ser inserido.

    if x == 4:
        cond = 0
    # Condição de parada do código.

print ('MUITO OBRIGADO')
print (f'Alcool: {alc}')
print (f'Gasolina: {gas}')
print (f'Diesel: {dis}')
# Impressão dos valores finais.