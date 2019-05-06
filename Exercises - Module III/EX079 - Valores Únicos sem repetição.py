#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
#No final, serão exibidos todo os valores únicos digitados em ordem crescente. 
print('='*40)
print('{:^40}' .format('EX079 - Números Únicos'))
print('='*40)
print('\n')


numeros = list()

while True:
  num = int(input('Digite um número: '))
  
  if num not in numeros:
    numeros.append(num)

  valcont = 'n'
  while valcont == 'n':
    continuar = str(input('Deseja continuar [S/N]: '))

    if continuar in 'Ss':
      valcont = continuar.lower()[0]
    elif continuar in 'nN':
      break
    else:
      print('\033[31mOpção Inválida\033[m')
    
  if continuar in 'nN':
    break    

numeros.sort()
print(f'\nNúmeros digitados: {numeros}')    

print('\n\033[1mSaindo do Programa...')