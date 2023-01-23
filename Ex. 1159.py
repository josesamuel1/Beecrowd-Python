from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

while 1:
    soma = 0
    # Atribuição de valor para contagem.

    x = int (input ())
    # Atribuição de valor.
    
    if x == 0:
        break
        # Caso 'x' seja igual a
        # 0, o código irá parar.

    else:
        for _ in range (10):
            if x % 2 == 0:
                soma += x
                # Caso contrário, irá somar todos os
                # próximos 5 pares a partir de 'x'.
            x += 1
            # Atribuição de valor para contagem.

    print (soma)
    # Impressão de valor.