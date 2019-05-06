#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
import emoji

print('\033[34m-=-\033[m'*9)
print('\033[33mEX046 - Contagem Regressiva\033[m')
print('\033[34m-=-\033[m'*9)

print('\n{}{:^30}{}\n' .format('\033[1;31m', ' PREPARE-SE ', '\033[m'))

for c in range(10, -1, -1):
  print('{:>20} {} ' .format('Estouro em: ', c))
  sleep(1)

print(emoji.emojize('\n{:>20}{}{}' .format('\033[1;32m', 'AEEEE!',':grinning_face:')))
