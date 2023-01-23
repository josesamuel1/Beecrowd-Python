from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

minuto_seg = 60
hora_seg = minuto_seg * 60
dia_seg = hora_seg * 24
# Atribuição de valores.

_, dia_i = input().split()
hi, mi, si = map (int, input().split(' : '))
_, dia_f = input().split()
hf, mf, sf = map (int, input().split(' : '))
# Atribuição de valores.

dia_i = int (dia_i)
dia_f = int (dia_f)
# Casting nas variáveis.

inicio = si + mi * minuto_seg + hi * hora_seg + dia_i * dia_seg
final = sf + mf * minuto_seg + hf * hora_seg + dia_f * dia_seg
# Montagem das variáveis do tempo total em segundos.

if inicio < final:
    tempo = final - inicio
    dias = int (tempo / dia_seg)
    tempo = tempo % dia_seg
    horas = int (tempo / hora_seg)
    tempo = tempo % hora_seg
    minutos = int (tempo / minuto_seg)
    tempo = tempo % minuto_seg
    segundos = tempo
    # Cálculo para a conversão de segundos
    # em dias, horas, minutos e segundos.
    
    print(f'{dias} dia(s)\n{horas} hora(s)\n{minutos} minuto(s)\n{segundos} segundo(s)')
    # Impressão dos valores.