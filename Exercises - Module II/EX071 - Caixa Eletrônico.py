#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qul será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. 
#OBS: Considere que o vaixa possui cédulas de 50, 20, 10 e 1.
print('\033[34m-=-'*8)
print('\033[33mEX071 - Caixa Eletrônico')
print('\033[34m-=-\033[m'*8)
print('\n')

print('\033[1mCÉDULAS:\033[m [50] - [20] - [10] - [1]\n')
saque = int(input('Quanto deseja sacar: '))
print('\n')
ced50 = 0
ced20 = 0
ced10 = 0
ced1 = 0

while saque != 0:
  
  while saque/50 >= 1:
    ced50 += 1
    saque -= 50
  if ced50 >0:
    print(f'\033[32m{ced50}\033[m de [50]')
    
  while saque/20 >= 1:
    ced20 += 1
    saque -= 20
  if ced20 >0:
    print(f'\033[32m{ced20}\033[m de [20]')

  while saque/10 >= 1:
    ced10 += 1
    saque -= 10
  if ced10 >0:
    print(f'\033[32m{ced10}\033[m de [10]')

  while saque/1 >= 1:
    ced1 += 1
    saque -= 1
  if ced1 >0:
    print(f'\033[32m{ced1}\033[m de [1]')
