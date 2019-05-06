#Melhore o jogo do Desafio 028 onde o computador vai 'pensar' em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer. 

from random import randint

print('\033[34m-=-'*10)
print('\033[33mEX058 - Jogo de Advinhação 2.0')
print('\033[34m-=-\033[m'*10)
print('\n')

pc = randint(0,10)
player = int(input('Digite um número: '))
count =0

while player!=pc:
  if player<pc:
    print('\033[31mMAIS! Tente outra vez\033[m\n')
  else:
    print('\033[31mMENOS! Tente outra vez\033[m\n')
  player = int(input('Digite um número: '))
  count+=1

print('\033[1;32mACERTOU!\033[m Você tentou {} vez(es)' .format(count))
