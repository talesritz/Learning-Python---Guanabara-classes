#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR

print('-=-'*4)
print('Par ou Ímpar')
print('-=-'*4)
print('\n')

num = int(input('Digite um número: '))

if num%2 == 0:
  print('O número {} é par' .format(num))
else:
  print('O número {} é ímpar' .format(num))