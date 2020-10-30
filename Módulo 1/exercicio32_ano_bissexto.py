# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input('Qual ano você quer analisar? '))
# Quando o ano é divisivel por 4 é bissexto, exceto anos múltiplos de 100 que não são multiplos de 400, logo:
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano é bissexto.')
else:
    print('NÂO é bissexto.')
