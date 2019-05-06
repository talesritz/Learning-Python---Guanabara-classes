#Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivasd que ele conquistou no final do jogo. 
from random import randint

print('\n')
print('\033[34m-=-'*8)
print('\033[33mEX - Par ou Ímpar While')
print('\033[34m-=-\033[m'*8)
print('\n')

parimpar = ['par', 'impar']
ganhou ='s'
ganhouqtde = 0
#valida se o player ganhou
while ganhou == 's':
  pc = randint(0, 1)
  #valida se a opção escolhida está correta
  validaopcao ='n'
  while validaopcao == 'n':
    print(pc)
    print('''PAR OU ÍMPAR: 
    [1] Par
    [2] Ímpar''')
    opcao = int(input('Digite sua opção: '))
    
    #valida se a opção é válida
    if opcao == 1 or opcao == 2:
      player = parimpar[opcao-1]
      validaopcao ='s'
    else:
      print('\033[1;31mOpção inválida\033[m')
      print('\n')
    
  validanum = 'n'
  while validanum =='n':
    num = int(input('Quantos dedos [1 a 5]: '))
    if 1 <= num <=5:
      validanum ='s'
    else:
      print('\033[1;31mOpção inválida\033[m')
      print('\n')
      
  if player == 'par':
    if (num+pc)%2 == 0:
      ganhouqtde+=1
      print('\n')
      print('\033[1;32mGANHOU!\033[m Vamos de novo...\n')
      
    else:
      print('\n')
      print('\033[1;31mPERDEU!\033[m\n')
      ganhou ='n'
  else:
    if (num+pc)%2 == 0:
      print('\n')
      print('\033[1;31mPERDEU!\033[m\n')
      ganhou ='n'
    else:
      ganhouqtde+=1
      print('\n')
      print('\033[1;32mGANHOU!\033[m Vamos de novo...\n')
      
 
print(f'Você ganhou {ganhouqtde} vez(es)!')