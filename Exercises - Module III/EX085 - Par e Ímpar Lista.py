#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os pares e ímpares em ordem crescente. 

 

#Utilizando For in range
'''print('='*40)
print('{:^40}' .format('EX085 - Par e Ímpar Lista'))
print('='*40)
print('\n')

numeros = []

for count in range(0, 7):
  num = int(input('Digite um número: ')) 

  if numeros == []:
    numeros.append(num)
  elif num%2 == 0:
    numeros.insert(0, num)
  else:
    numeros.append(num)

  print(numeros)

print('\n')
print(f'Números digitados: {numeros}')
numeros.sort()
print(f'Números ordenados: {numeros}')

print('\033[1m\nSaindo do Programa...\033[m')
'''

#Utilizando while com lista infinita
print('='*40)
print('{:^40}' .format('EX085 - Par e Ímpar Lista'))
print('='*40)
print('\n')

numeros = list()
pares = list()
impares = list()

valcont = 's'
while valcont == 's':
  num = int(input('Digite um número: '))
  
  #Valida se o usuário deseja continuar
  while valcont == 's':
    cont = str(input('Deseja continuar[S/N]: '))
    
    if cont.lower() == 's':
      print('\n')
      break
    elif cont.lower() == 'n':
      valcont = 'n'
    else:
      print('\033[31mOpção Inválida\033[m')

  #Separa os números pares dos ímpares
  if num%2 == 0:
    pares.append(num)
  else:
    impares.append(num)


for count in range(0, len(pares)):
  numeros.append(pares[count])

for count in range(0, len(impares)):
  numeros.append(impares[count])

print(f'\nNúmeros digitados: {numeros}')
numeros.sort()
print(f'Números ordenados: {numeros}')


print('\033[1m\nSaindo do Programa...\033[m')