#Crie um programa que gerencie o aproveitamento de um jogador de futubol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato. 

print('='*40)
print('{:^40}' .format('EX093 - Cadastro Jogador Futebol'))
print('='*40)
print()


cadastro = dict()
gols = list()
totgols = 0

cadastro['nome'] = str(input('Nome: '))
cadastro['qtdejogos'] = int(input('Quantidade de Jogos: '))

if cadastro['qtdejogos'] == 0:
  cadastro['totgols'] = 0

elif cadastro['qtdejogos'] > 0:
  for  count in range(0, cadastro['qtdejogos']):
    golpartida = int(input(f'Gols partida {count+1}: '))
    gols.append(golpartida)
    totgols += golpartida

  cadastro['totgols'] = totgols
  cadastro['golspartida'] = gols.copy()  

else:
  cadastro['totgols'] = 0


print()
for k, v in cadastro.items():
  if k != 'golspartida':
    print(f'{k}  :  {v}')
  else:
    for count in range(0, len(cadastro['golspartida'])):
      print(f'Gols partida {count+1}: {cadastro["golspartida"][count]}')
