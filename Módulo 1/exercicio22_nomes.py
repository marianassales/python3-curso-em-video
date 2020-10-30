# Crie um programa que leia o nome completo de uma pessoa e mostre o nome com todas as letras maiúsculas e minúsculas
# e quantas letras aotodo (sem considerar espaços).

nome = str(input('Digite seu nome: ')).strip()
print('Analisando seu nome...')
print('Seu nome em MAIÚSCULAS é: {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem {} caracteres.'.format(len(nome) - nome.count(' ')))
# print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} tem {} letras'.format(separa[0], len(separa[0])))


