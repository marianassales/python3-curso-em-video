# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

aluno = str(input('Aluno: '))
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
media = (n1 + n2) / 2
print('A média de {} é {}.'.format(aluno, media))

