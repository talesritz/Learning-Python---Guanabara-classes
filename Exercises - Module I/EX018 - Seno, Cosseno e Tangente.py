#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. 

from math import sin, cos, tan

print('-=-'*11)
print('EX018 - Seno, Cosseno e Tangente')
print('-=-'*11)
print('\n')

ang = int(input('Digite um ângulo: '))
print('Seno: {:.2f}' .format(sin(ang)))
print('Cosseno: {:.2f}' .format(cos(ang)))
print('Tangente: {:.2f}' .format(tan(ang)))