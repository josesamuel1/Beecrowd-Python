from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

def calculo (x, y):
    return x % y
    # Função que retorna o resto da divisão
    # entre os dois valores informados.

def fnc1 ():
    a, b = map (int, input().split())
    # Atribuição de valores.
    
    if a == b:
        print ('Sao Multiplos')
        # Caso os valores informados
        # sejam iguais.

    if a > b:
        if calculo (a, b) == 0:
            print ('Sao Multiplos')
            # Caso 'a' seja maior que 'b'
            # e o resto da divisão entre eles
            # seja igual a 0.
        else:
            print ('Nao sao Multiplos')
            # Caso contrário.

    if b > a:
        if calculo (b, a) == 0:
            print ('Sao Multiplos')
            # Caso 'b' seja maior que 'a'
            # e o resto da divisão entre eles
            # seja igual a 0.
        else:
            print ('Nao sao Multiplos')
            # Caso contrário.

fnc1 ()
# Chama a função para ser executada