from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

def fnc1 ():
    nums = list (map (int, input().split()))
    # Atribuição de valores.
    
    soma_ints (nums)
    # Chama a função para ser executada.

def soma_ints (nums):
    num1 = "X"
    num2 = soma = 0
    # Atribuição de valores.
    
    for i in nums:
        if num1 == "X":
            num1 = i
        else:
            if i > 0:
                num2 = i
                break
                # Condição que irá identificar os 2 primeiros
                # números positivos e arquivá-las em variáveis.
    
    for _ in range (num2):
        soma += num1
        num1 += 1
        # Condição que irá aumentar 'soma' durante
        # 'num2' vezes, cada vez mais com 'num1' + 1.
    
    print (soma)
    # Chama a função para ser executada.

fnc1 ()
# Chama a função para ser executada.