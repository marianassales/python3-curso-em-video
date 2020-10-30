# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

num = float(input('Digite um número: '))
print('O número inteiro é {}'.format(int(num)))

from math import trunc
num = float(input('Digite um número: '))
print('O número inteiro é {}'.format(trunc(num)))