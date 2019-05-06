#Faça um programa que leia um número qualquer e mostre o seu fatorial

print('\033[34m-=-'*6)
print('\033[33m EX060 - Fatorial')
print('\033[34m-=-\033[m'*6)
print('\n')

num = int(input('Digite um número: '))
nreal = num
fat = num

while num!=1:
  fat = fat*(num-1)
  num = num-1

print('Fatorial de {}: {}' .format(nreal, fat))