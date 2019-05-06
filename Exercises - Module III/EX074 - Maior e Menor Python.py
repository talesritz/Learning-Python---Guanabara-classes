#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

print('='*40)
print('{:^40}' .format('EX074 - Maior e Menor Tuplas'))
print('='*40)
print('\n')

numbers = ( randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
maior = -10000000
menor = 10000000

print('Números gerados: ', end='')
for count in numbers:
   print(f'{count} ', end='')
   
for count in range(0, len(numbers)):
  if numbers[count]< menor:
    menor = numbers[count]
  elif numbers[count]> maior:
    maior = numbers[count]

print(f'\nMaior: {maior}')
print(f'Menor: {menor}')

