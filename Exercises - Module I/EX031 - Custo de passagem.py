#Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrança 0.50 por Km para viagens de até 200km e 0.45 para viagens mais longas.

print('-=-'*8)
print('EX031 - Custo da Viagem')
print('-=-'*8)
print('\n')

dist = float(input('Qual a distância percorrida: '))

if dist > 200:
  print('A passagem custará {:.2f} reais' .format(dist*0.45))
else:
  if dist > 0:
    print('A passagem custará {:.2f} reais' .format(dist*0.5))
  else:
    print('Digite uma distânca válida, por favor.')