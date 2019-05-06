#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado. 
print('\n')
print('\033[34m-=-\033[m'*9)
print('\033[33m EX036 - Aprovando crédito\033[m')
print('\033[34m-=-\033[m'*9)
print('\n')

vcasa = float(input('\033[36mValor da casa:\033[m '))
sal = float(input('\033[36mRenda mensal: \033[m'))
anos = int(input('\033[36mEm quantos anos pretende pagar? \033[m'))
prest = vcasa /(anos*12)

print('\n')
if prest>sal*0.3 and prest>0:
  print('\033[1;31mNEGADO\033[m - a prestação seria de {:.2f} reais.\n Não pode ser maior que 30% do seu salário ({:.2f}).\n Selecione um tempo maior de parcelamento.' .format(prest, sal*0.3))
else:
  if sal<=0 or vcasa<=0 or anos<=0:
    print('Digite um valor válido')
  else: 
    print('\033[1;32mAPROVADO\033[m - {} vezes de {:.2f} reais.' .format(anos*12, prest))
