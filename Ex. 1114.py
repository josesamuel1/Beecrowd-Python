from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

while 1:
    # Comando de laço infinito até que um
    # comando de parada seja executado.

    x = int (input())
    # Atribuição de valor.
    
    if x == 2002:
        print ('Acesso Permitido')
        break
        # Caso onde 'x' é exatamente igual
        # à resposta que a questão informa.

    else:
        print ('Senha Invalida')
        # Caso onde 'x' não é igual
        # à resposta que a questão informa.