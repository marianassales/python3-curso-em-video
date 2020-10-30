# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Seu nome complleto: ')).strip()
print('Seu nome tem silva? {}'.format('Silva' in nome.lower()))
