#  Escreva um programa que leia a velocidade de um carro.
#  Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#  A multa vai custar R$7,00 por cada Km acima do limite.

'''velocidade = float(input('Qual é a velocidade do carro? '))
print('Radar: {}Km/h.'.format(velocidade))

if velocidade > 80:
    print('Limite acima do permitido. A multa é {} reais.'.format((velocidade-80) *7))
else:
    print('Bom dia, dirija com segurança!')'''

# Usando condição simples (só um if)

velocidade = float(input('Qual é a velocidade do carro? '))
print('Radar: {}Km/h.'.format(velocidade))

if velocidade > 80:
    print('Limite acima do permitido.')
    multa = (velocidade-80) * 7
    print('Acima do permitido. A multa é de R${:.2f}.'.format(multa))
print('Bom dia, dirija com segurança!')
