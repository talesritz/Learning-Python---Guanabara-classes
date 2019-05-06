#Escreva um programa que faça o computador 'pensar' entre 0 e 5 e peça para o usuário tentar descobrir qual foi o numero escolhido pelo computador.
#O programa deverá escrever na tela se o usuario venceu ou perdeu
from random import randint
from time import sleep

cores = {
  'amarelo' : '\033[33m',
  'anil' : '\033[34m',
  'roxo' : '\033[35m', 
  'vermelho' : '\033[31m',
  'verde' : '\033[32m',
  'limpa' : '\033[m'
}

print('\n')
print('\033[33m-=-\033[m'*9)
print('\033[34mEX028 - Jogo de Adivinhação\033[m')
print('\033[33m-=-\033[m'*9)
print('\n')

computador = randint(0,5)
user = int(input('Digite um número entre 0 e 5: '))

print('\n')
print('\033[35mPROCESSANDO ...\033[m')
print('\n')
sleep(1)

if user == computador:
  print('\033[32mPARABÉNS! Você acertou!\033[m')
else:
  print('\033[31mGANHEI! Eu escolhi o número {} e não o {}!\033[m' .format(computador, user))
