#Deselvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o número 9
#b) Em que posição foi digitado o primeiro valor 3
#C) Quais foram os números pares

print('='*40)
print('{:^40}' .format('EX075 - Análise de Dados Tuplas'))
print('='*40)
print('\n')

num9 = 0
pos3 = 0
qtdepares = 0

print('Digite 4 números: ')
numbers = (int(input('a: ')), int(input('b: ')), int(input('c: ')), int(input('d: ')))

#print(numbers)

#a) Quantas vezes apareceu o número 9
for count in numbers:
  if count == 9:
    num9+=1
if num9 == 0:
  print('A) Número 9 apareceu: Não há registros')
else:
  print(f'A) Número 9 apareceu: {num9} vezes')

#b)Em que posição foi digitado o primeiro número 3
for count in range(0, len(numbers)):
  if numbers[count] == 3:
    pos3 = count
    break
if pos3 == 0:
  print('B) Primeira aparição do 3: Não há registros')
else:
  print(f'B) Primeira aparição do 3: posição {pos3+1}')

#c)Mostre os números pares
print('C) Números pares: ', end='')
for count in numbers:
  if count%2 == 0:
    print(f'{count} ', end='')
    qtdepares+=1
if qtdepares == 0:
  print('Não há registros')

print('\n\033[1mSaindo do programa...')

#Professor
'''

print('a) Número 9 apareceu {numbers.count(9)} vezes')

if 3 in numbers:
  print('b) Número 3 aparece pela primeira vez na posição {numbers.index(3)+1}')
else:
  print('b) Número 3 não foi digitado)

print('c) Números Pares: ', end='')
for count in numbers:
  if count%2 == 0:
    print(count, end=' ')
    '''