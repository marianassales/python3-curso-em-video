# Faça um programa que leia um número inteiro e mostre na tela o seu antecessor e sucessor

n = int(input('Digite um número: '))
a = n - 1
s = n + 1
print('Analisando seu número {}, o antecessor é {} e o sucessor é {}'.format(n, a, s))

# OU caso eu não precise guardar as variaveis:
n = int(input('Digite um número: '))
print('Analisando seu número {}, o antecessor é {} e o sucessor é {}'.format(n, (n-1), (n+1)))

