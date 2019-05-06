#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

numeros = list()

for count in range(0, 5):
  numeros.append(int(input('Digite um número: ')))

maior = -10000000000000
posmaior = list() 
menor = 1000000000000
posmenor = list()

for valor in numeros:
  if valor > maior:
    maior = valor
    
  elif valor < menor:
    menor = valor

for pos in range(0, len(numeros)):
  if maior == numeros[pos]:
    posmaior.append(pos)
  elif menor == numeros[pos]:
    posmenor.append(pos)



if posmaior == [] or posmenor == []:
  print(f'\nTodos os números são iguais')
else:
  print(f'\nMaior valor: {maior}, nas posições: {posmaior}')
  print(f'Menor valor: {menor}, nas posições: {posmenor}')

#Sem dizer em quais posições aparece o maior e menor
'''
for pos, valor in enumerate(numeros):
print(f'\nMaior valor: {maior} na posição {posmaior+1}')
print(f'Menor valor: {menor} na posição {posmenor+1}') 
'''