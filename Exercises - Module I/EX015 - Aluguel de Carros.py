#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0.15 por Km rodado. 

print('-=-'*8)
print('    Aluguel de Carros')
print('-=-'*8)
print('\n')

km = float(input('Digite quantos Km o carro percorreu: '))
dias = int(input('Por quantos dias o carro foi alugado? '))

print('\n========== Valores ==========')
print('Distância percorrida: R$ {:.2f} ' .format(km*0.15))
print('Dias alugados: R$ {:.2f}' .format(dias*60))
print('Total a pagar: R$ {:.2f}' .format((km*0.15)   + (dias*60)))
