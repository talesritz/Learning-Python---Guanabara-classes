#Desenvolva uma logica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
#-abaixo de 18.5: Abaixo do peso
#- ente 18.5 e 25: peso ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- acima de 40: Obesidade Mórbida

print('\033[34m-=-\033[m'*8)
print('\033[33mEX043 - Calculando IMC\033[m')
print('\033[34m-=-\033[m'*8)
print('\n')

print('Abaixo de 18.5: \033[37mAbaixo do peso\033[m')
print('Entre 18.5 e 25: \033[32mPeso ideal\033[m')
print('entre 25 até 30: \033[36mSobrepeso\033[m')
print('Entre 30 até 40: \033[33mObesidade\033[m')
print('Acima de 40: \033[31mObesidade MÓRBIDA\033[m')
print('\n')


alt = float(input('Digite sua altura (em Metros): '))
peso = float(input('Digite seu peso: '))
imc = peso/(alt**2)
print('\n')

if imc<18.5 and imc>0:
  print('IMC: {:.2f}' .format(imc))
  print('\033[37mAbaixo do peso\033[m')
elif imc >=18.5 and imc<25:
  print('IMC: {:.2f}' .format(imc))
  print('\033[32mPeso ideal\033[m')
elif imc >=25 and imc<30:
  print('IMC: {:.2f}' .format(imc))
  print('\033[36mSobrepeso\033[m')
elif imc>=30 and imc<40:
  print('IMC: {:.2f}' .format(imc))
  print('\033[33mObesidade\033[m')
elif imc>40: 
  print('IMC: {:.2f}' .format(imc))
  print('\033[1;31mObesidade MÓRBIDA\033[m')
else:
  print('Digite valores válidos')
