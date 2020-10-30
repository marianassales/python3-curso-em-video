# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
computador = randint(0,5)
print('~~~~' *15)
print('Vou pensar em um número de 1 a 5. Tente adivinhar')
print('~~~~' *15)
usuario = int(input('Qual número o PC pensou? '))

if usuario == computador:
    print('ACERTOU')
else:
    print('ERROU. Eu pensei no número {}.'.format(computador))

