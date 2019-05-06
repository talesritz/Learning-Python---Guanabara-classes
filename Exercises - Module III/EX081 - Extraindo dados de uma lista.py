#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, mostre:
#a) Quantos números foram digitados
#b) A lista de valores ordenada de forma decrescente
#c) Se o valor 5 foi digitado e está ou não na lista. 
print('='*40)
print('{:^40}' .format('EX081 - Extraindo Dados de uma Lista'))
print('='*40)
print('\n')

numeros = list()
valcont = 's'

while valcont == 's':
  num = int(input('Digite um número: '))
  numeros.append(num)  

  while valcont != 'n':
    cont = str(input('Deseja continuar [S/N]: '))
    if cont.lower() == 'n':
      valcont = 'n'
    elif cont.lower() == 's':
      valcont = 's'
      break
    else:
      print('\033[31mOpção Inválida\033[m')

#a) números digitados
print(f'\na) {len(numeros)} números digitados')

#b)lita decrescente
numeros.sort(reverse=True)
print(f'b) Lista decrescente: {numeros}')

#c) Se o 5 foi digitado e se está na lista
if 5 in numeros:
  pos5 = list()
  for count in range(0, len(numeros)):
    if numeros[count] == 5:
      pos5.append(count+1)
  print(f'c) 5 está presente na lista nas posições: {pos5}')
else:
  print('c) 5 não está na lista')


print('\n\033[1mSaindo do Programa...')