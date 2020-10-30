# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

palavra = input('Digite uma palavra: ') #palavra = variavel
print('O tipo primitivo é: ', type(palavra))
print('Só tem espaços? ', palavra.isspace()) #palavra = objeto
print('É um número? ', palavra.isnumeric())
print('É alfabético? ', palavra.isalpha())
print('É alfanumérico? ', palavra.isalnum())
print('Está em maisculas? ', palavra.isupper())
print('Está em minusculas? ', palavra.islower())
print('Está capitalizada? ', palavra.istitle())

