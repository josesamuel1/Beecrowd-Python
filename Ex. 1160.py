from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

rep = int (input ())
# Atribuição de valor para contagem.

for _ in range (rep):
    anos = 0
    PopA, PopB, CPopA, CPopB = input().split()
    # Atribuição de valores.
    
    PopA = int(PopA)
    PopB = int(PopB)
    CPopA = float(CPopA)
    CPopB = float(CPopB)
    # Casting das variáveis.
    
    while PopA <= PopB:
        PopA += PopA * CPopA // 100
        PopB += PopB * CPopB // 100
        anos += 1
        # Cálculo para descobrir em quantos
        # anos que a população da cidade A
        # ultrapassará a da cidade B.

        if anos > 100:
            print ('Mais de 1 seculo.')
            break
            # Caso a quantidade de anos exceda 100.
    
    if anos <= 100:
        print (f'{anos} anos.')
        # Impressão de valor.