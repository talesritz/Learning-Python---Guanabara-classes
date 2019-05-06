#Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
#No final, mostre a matriz na tela, com a formatação correta

print('='*38)
print('{:^38}' .format('EX086 - Preenchendo Matriz'))
print('='*38)
print('\n')

matriz = []


for line in range(0, 3):
  for col in range(0, 3):
    num = int(input(f'Posição {line+1} - {col+1}: '))
    matriz.append(num)

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
print('\033[1m\nSaindo do Programa...')
