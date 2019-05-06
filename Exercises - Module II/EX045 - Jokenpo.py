#Crie um programa que faça o computador jogar Jokenpô com você

from random import choice
from time import sleep

print('\033[34m-=-\033[m'*6)
print(' \033[33mEX045 - Jokenpô\033[m')
print('\033[34m-=-\033[m'*6)
print('\n')

opcoes = ['1', '2', '3']
pc = int((choice(opcoes)))

print('\033[1mTENTE GANHAR DE MIM!\n\033[m')
print(pc)
print('Escolha uma opção: ')
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')
player = int(input('Digite sua opção: '))
print('\n')

print('JO!')
sleep(0.5)
print('KEN!')
sleep(0.5)
print('POOO!\n')
sleep(0.5)

if player==pc:
  print('\033[33mEMPATAMOS!!!\033[m')
elif player==1 and pc==2:
  print('\033[1;31mGANHEI! Eu escolhi \033[36mPAPEL\033[m\033[1;31m.\033[m' . format(pc))
elif player==1 and pc==3:
  print('\033[32mVOCÊ GANHOU!\033[m') 
elif player==2 and pc==1: 
  print('\033[32mVOCÊ GANHOU!\033[m')
elif player==2 and pc==3:
  print('\033[1;31mGANHEI! Eu escolhi \033[36mTESOURA\033[m\033[1;31m.\033[m' . format(pc))
elif player==3 and pc==1:
  print('\033[1;31mGANHEI! Eu escolhi \033[36mPEDRA\033[m\033[1;31m.\033[m' . format(pc))
elif player==3 and pc==2:
  print('\033[32mVOCÊ GANHOU!\033[m')
else:
  print('Digite uma opção válida')
  
''' #Crie um programa que faça o computador jogar Jokenpô com você
from random import randint
from time import sleep

itens = ['pedra', 'papel', 'tesoura']
pc = int(randint(0, 2))
#print(itens[pc])

print('\033[34m-=-\033[m'*5)
print('\033[33mEX045 - Jokenpo\033[m')
print('\033[34m-=-\033[m'*5)
print('\n')

print('''Escolha uma opção:
1 - Pedra
2 - Papel
3 - Tesoura''')
player = int(input('Digite sua opção: '))

print('\n')
print('{}{:=^19}' .format('\033[1;31m',' JO! '))
sleep(0.5)
print('{}{:=^19}' .format('\033[1;31m',' KEN! '))
sleep(0.5)
print('{}{:=^19}' .format('\033[1;31m',' POO! '))
sleep(0.5)

print('\n')
if pc==0: #PEDRA
  if player==1:
    print('\033[1;33mEMPATAMOS!\033[m')
  elif player==2:
    print('\033[1;032mVOCÊ GANHOU!\033[m')
  elif player==3:
    print('\033[1;31mVOCÊ PERDEU!\033[m')
  else:
    print('Opção inválida')
elif pc==1: #PAPEL
  if player==1:
    print('\033[1;31mVOCÊ PERDEU!\033[m')
  elif player==2:
    print('\033[1;33mEMPATAMOS!\033[m')
  elif player==3:
    print('\033[1;032mVOCÊ GANHOU!\033[m')
  else:
   print('Opção inválida')
else: #TESOURA
  if player==1:
    print('\033[1;032mVOCÊ GANHOU!\033[m')
  elif player==2:
    print('\033[1;31mVOCÊ PERDEU!\033[m')
  elif player==3:
    print('\033[1;33mEMPATAMOS!\033[m')
  else:
    print('Opção inválida')
'''

