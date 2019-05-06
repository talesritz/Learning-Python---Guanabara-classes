#Elabore um programa que calcule o valor a ser pago por um produto, considerando o oseu preço normal e condição de pagamento:

#- a vista dinheiro/cheque: 10% de desconto
#- a vista no cartao: 5% de desconto
#- em ate 2x no cartao: preço normal
#- 3x ou mais no cartao: 20% de juros


print('\033[34m-=-\033[m'*11)
print('\033[33mEX044 - Gerenciador de Pagamentos\033[m')
print('\033[34m-=-\033[m'*11)
print('\n')

print('1 - À Vista (dinheiro ou cheque)')
print('2 - À Vista (débito)')
print('3 - Crédito (até 2x)')
print('4 - Crédito (3x ou mais')
print('\n')

pgto = int(input('Digite a forma de pagamento: '))
preco = float(input('Digite o preço do produto: '))

if pgto==1:
  print('Valor a pagar: {:.2f} reais' .format(preco*0.9))
elif pgto==2:
  print('Valor a pagar: {:.2f} reais' .format(preco*0.95))
elif pgto==3:
  parc = int(input('Quantas vezes? '))
  if parc>2:
    print('Máximo de 2 parcelas para esta opção')
  else:
    print('Valor a pagar: {} parcela(s) de {:.2f} reais' .format(parc, preco/parc))
elif pgto==4:
  parc = int(input('Quantas vezes? '))
  print('Valor a pagar: {} parcela(s) de {:.2f} reais' .format(parc, (preco*1.2)/parc))
else: 
  print('Digite uma opção válida.')