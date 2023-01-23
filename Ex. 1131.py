from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

cond = 1
itr = grm = emp = gren = 0
# Atribuição de valores.

while cond == 1:
    # Comando de laço infinito até que um
    # comando de parada seja executado.
    
    x, y = map (int, input().split())
    # Atribuição de valores.

    if x == y:
        emp += 1
        gren += 1
    if x > y:
        itr += 1
        gren += 1
    if x < y:
        grm += 1
        gren += 1
    # Casos onde o código analisará se o Inter
    # ganhou, o Grêmio ganhou ou se deu empate.
    
    print ('Novo grenal (1-sim 2-nao)')
    repet = int (input ())
    if repet == 1:
        cond = 1
    elif repet == 2:
        cond = 0
    else:
        print ('Novo grenal (1-sim 2-nao)')
        repet = int (input ())
    # Casos onde o código deve ser repetido, se não
    # deve ou se nenhuma das opções foram escolhidas.
    
if itr == grm:
    maior = 'Nao houve vencedor'
if itr > grm:
    maior = 'Inter venceu mais'
if itr < grm:
    maior = 'Gremio venceu mais'
# Casos para identificar qual time ganhou
# mais ou se foi empate ao final do código.    

print (f'{gren} grenais')
print (f'Inter:{itr}')
print (f'Gremio:{grm}')
print (f'Empates:{emp}')
print (maior)
# Impressão dos resultados finais.