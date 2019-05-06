 #Crie um programa onde o usuário possa digitar cinco valores númericos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
#No final, mostre a lista ordenada na tela. 

print('='*40)
print('{:^40}' .format('EX080 - Listagem ordenada sem Sort()'))
print('='*40)
print('\n')

numeros = list()


for c in range(0, 5):
  num = int(input('Digite um número: '))
 
  pos = 0
  for index, value in enumerate(numeros):
    if num > numeros[index]:
      pos = index+1
  
  if numeros == []:
    numeros.append(num)
    print(f'{num} é o primeiro item da lista')
  elif pos == 0:
    numeros.insert(pos, num)
    print(f'{num} inserido no início da lista')
    print(f'Lista: {numeros}')
  elif pos == len(numeros):
    numeros.append(num)
    print(f'{num} inserido no final da lista')
    print(f'Lista: {numeros}')
  else:
    numeros.insert(pos, num)
    print(f'{num} foi inserido na posição {pos}')
    print(f'Lista: {numeros}')

print('\n\033[1mSaindo do Programa...')