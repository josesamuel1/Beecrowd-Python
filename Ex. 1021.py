from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

def resultado (dinh):
    dinh100 = dinh // 100
    dinh50 = dinh % 100 // 50
    dinh20 = dinh % 100 % 50 // 20
    dinh10 = dinh % 100 % 50 % 20 // 10
    dinh5 = dinh % 100 % 50 % 20 % 10 // 5
    dinh2 = dinh % 100 % 50 % 20 % 10 % 5 // 2
    moeda1 = dinh % 100 % 50 % 20 % 10 % 5 % 2 // 1
    moeda50 = dinh % 100 % 50 % 20 % 10 % 5 % 2 % 1 // 0.50
    moeda25 = dinh % 100 % 50 % 20 % 10 % 5 % 2 % 1 % 0.50 // 0.25
    moeda10 = dinh % 100 % 50 % 20 % 10 % 5 % 2 % 1 % 0.50 % 0.25 // 0.10
    moeda05 = dinh % 100 % 50 % 20 % 10 % 5 % 2 % 1 % 0.50 % 0.25 % 0.10 // 0.05
    moeda01 = dinh % 100 % 50 % 20 % 10 % 5 % 2 % 1 % 0.50 % 0.25 % 0.10 % 0.05 / 0.01 + 0.01
    
    print ("NOTAS:")
    print (f"{dinh100:.0f} nota(s) de R$ 100.00")
    print (f"{dinh50:.0f} nota(s) de R$ 50.00")
    print (f"{dinh20:.0f} nota(s) de R$ 20.00")
    print (f"{dinh10:.0f} nota(s) de R$ 10.00")
    print (f"{dinh5:.0f} nota(s) de R$ 5.00")
    print (f"{dinh2:.0f} nota(s) de R$ 2.00")
    print ("MOEDAS:")
    print (f"{moeda1:.0f} moeda(s) de R$ 1.00")
    print (f"{moeda50:.0f} moeda(s) de R$ 0.50")
    print (f"{moeda25:.0f} moeda(s) de R$ 0.25")
    print (f"{moeda10:.0f} moeda(s) de R$ 0.10")
    print (f"{moeda05:.0f} moeda(s) de R$ 0.05")
    print (f"{moeda01:.0f} moeda(s) de R$ 0.01")
    # Função que irá calcular quantas cédulas e
    # moedas ecistem no valor informado pelo usuário.
    
def fnc1 ():
    dinh = float(input())
    # Atribuição de valor.
    
    resultado (dinh)
    # Chamada da função.
    
fnc1 ()
# Chama a função para ser executada.