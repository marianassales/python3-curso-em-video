# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random
n1 = str(input('Aluno 1: '))
n2 = str(input('Aluno 2: '))
n3 = str(input('Aluno 3: '))
lista = [n1, n2, n3]
escolhido = random.choice(lista) #choice é 1 chance
print('O aluno escolhido é {}'.format(escolhido))
random.shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)

