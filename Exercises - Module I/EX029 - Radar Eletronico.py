#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7.00 por cada km acima do limite. 


print('-=-'*8)
print('EX029 - Radar Eletrônico')
print('-=-'*8)
print('\n')

vel = float(input('Digite a velocidade que você estava: '))

if vel>80:
  print('VOCÊ FOI MULTADO! Terá que pagar uma multa de {:.2f}' .format((vel-80)*7))
print('Boa viagem! Viaje com segurança!')
