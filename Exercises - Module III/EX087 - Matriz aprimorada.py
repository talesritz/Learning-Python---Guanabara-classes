#Aprimore o desafio anterior, mostrando no final:
#a) A soma de todos os valores pares digitados.
#b) A soma dos valores da terceira coluna. 
#c) O maior valor da segunda linha. 

print('='*38)
print('{:^38}' .format('EX086 - Preenchendo Matriz'))
print('='*38)
print('\n')

matriz = []
somaP = 0
somaTC = 0
maiorSC = -100000000

for line in range(0, 3):
  for col in range(0, 3):
    num = int(input(f'Posição {line+1} - {col+1}: '))
    matriz.append(num)
    
    #
    if num%2 == 0:
      somaP += num
    
    if col == 2:
      somaTC += num
    
    if line == 1 and num > maiorSC:
      maiorSC = num


#print(matriz)
print('\n')

quebra = 0
for count in range(0, len(matriz)):
  if quebra == 3:
    print(f'\n{matriz[count]} ', end='')
    quebra = 1
  else:
    print(f'{matriz[count]} ', end='')
    quebra += 1

print('\n')

print(f'Soma dos Pares: {somaP}')
print(f'Soma da terceira coluna: {somaTC}')
print(f'Maior número da segunda linha: {maiorSC}')

print('\n')
print('\033[1m\nSaindo do Programa...')
