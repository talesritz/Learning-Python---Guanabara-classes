#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados. 

print('-=-'*9)
print('EX023 - Separando números')
print('-=-'*9)
print('\n')

num = int(input('Digite um número: '))

print('Milhar: {}' .format(num//1000%10))
print('Centena: {}' .format(num//100%10))
print('Dezena: {}' .format(num//10%10))
print('Unidade: {}' .format(num//1%10))