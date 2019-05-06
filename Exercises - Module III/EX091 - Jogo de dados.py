#Crie um programa onde 4 jogadores  joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado. 

print('='*40)
print('{:^40}' .format('EX091 - Jogo de Dados'))
print('='*40)
print()

from random import randint

cadastros = []
temp = dict()
maior = 0
ganhadores = []
insereord = -1
desempate = []
gandesempate = []



for c in range(0, 4):
  temp['nome'] = str(input(f'Digite o jogador {c+1}: '))
  temp['jogada'] = randint(1, 6)  
    
  #Verifica em qual posição será inserido o cadastro temp, já efetua a inserção do dicionário na lista de maneira ordenada
  if cadastros == []:
    cadastros.append(temp.copy())
  else:
    for pos in range(0, len(cadastros)):
      if temp['jogada'] < cadastros[pos]['jogada']:
        insereord = pos
        break

    if insereord == -1:
      cadastros.append(temp.copy())
    else: 
     cadastros.insert(insereord, temp.copy())
     
  #Verifica qual foi o maior valor jogado no dado
  if temp['jogada'] > maior:
    maior = temp['jogada']
  insereord = -1
  temp.clear()

print()


for count in range(0, len(cadastros)):
  for k, v in cadastros[count].items():
    print(f'{k}: {v:<12} ', end=' ')
  print()  

  if cadastros[count]['jogada'] == maior:
    ganhadores.append(cadastros[count]['nome'])

print('\nGanhador: ', end='')
for count in range(0, len(ganhadores)):
  print(f'{ganhadores[count]}', end='')
  if count == len(ganhadores)-1:
    print('.')
  else:
    print(', ', end='')
print()

#Caso ocorra empate novamente, o código abaixo sorteia novamente os dados para os jogadores ganhadores até que reste apenas 1 vencedor. 
maior = 0
temp.clear()
while len(ganhadores) > 1:
  for count in range(0, len(ganhadores)):
    temp['nome'] = ganhadores[count]
    temp['jogada'] = randint(1, 6)
    
    if temp['jogada'] > maior:
      maior = temp['jogada']
    
    desempate.append(temp.copy())
    temp.clear()
  
  ganhadores.clear()
  for count in range(0, len(desempate)):
    for k, v in desempate[count].items():
      print(f'{k}: {v:<12}', end='')
    print()
  
    if desempate[count]['jogada'] == maior:
      ganhadores.append(desempate[count]['nome'])

  print('\nGanhador: ', end='')
  for count in range(0, len(ganhadores)):
    print(f'{ganhadores[count]}', end='')
    if count == len(ganhadores)-1:
      print('.')
    else:
      print(', ', end='')
  print()
  desempate.clear() 
    