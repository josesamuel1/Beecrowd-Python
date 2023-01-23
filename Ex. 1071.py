from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

soma = 0
# Atribuição de valor para contagem.

x = int (input ())
y = int (input ())
# Atribuição de valores.

if x > y:
    aux = y
    y = x
    x = aux
# Caso x seja maior que y, a troca de valores
# é feita para que 'x' seja sempre o menor.

for i in range (x + 1, y):
    if i % 2 != 0:
        soma += i
# Para cada valor entre os valores inseridos
# pelo usuário (x não conta), ele irá somar
# os valores ímpares existentes.

print (soma)
# Impressão de valor.