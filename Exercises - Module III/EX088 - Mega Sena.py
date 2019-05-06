#Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar  quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta. 

from random import randint

print('='*40)
print('{:^40}' .format('EX088 - Mega Sena'))
print('='*40)
print('\n')

qtdejogos = int(input('Quantos jogos: '))
palpite = []
jogadas = []

for count in range(0, qtdejogos):
  
  for x in range(0, 6):
    palpite.append(randint(0, 60))
   
  jogadas.append(palpite[:])
  #print(jogadas)
  palpite.clear()


print('\n')

if qtdejogos == 0:
  print('Não há palpites para a quantidade de jogos solicitada')
elif qtdejogos == 1:
  print(f'Palpite: ', end='')
  for x in range(0, 6):
    print(f'{jogadas[0][x]} ', end='')
else:
  for x in range(0, qtdejogos):
    print(f'Palpite {x+1}: ', end='')
    for y in range(0, 6):
      print(f'{jogadas[x][y]} ', end='')
    print('\n')



print('\033[1m\nSaindo do Programa...')