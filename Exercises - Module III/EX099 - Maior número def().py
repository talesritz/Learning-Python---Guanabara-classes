#Faça um programa que tenha uma função chamada maior(), que receba vvários parâmetros com valores inteiros. 
#Seu programa tem que analisar todos os valores e dizer qual deles é o maior. 

def cabecalho(msg):
  '''print('='*40)
  print('{:^40}' .format(f'{msg}'))
  print('='*40)
  print()
  '''
  print('\n')
  print('\033[34m-=-\033[m'*13)
  print(f'\033[33m{msg:^40}\033[m')
  print('\033[34m-=-\033[m'*13)
def maior(num):
  if num == []:
    print('\033[33mNÃO HÁ REGISTROS\033[m')
  else:
    maior = 0
    for count in range(0, len(num)):
      if count == 0:
        maior = num[count]
      elif num[count] > maior:
        maior = num[count]
    
    print(f'O maior número é: {maior}')
    print()
def mostrar(lst):
  if len(lst) == 0:
    print('\033[33mNÃO HÁ REGISTROS\033[m')
    print()
   
  else:
    print('Lista: ', end='')
    for count in range(0, len(lst)):
      print(lst[count], end='')

      if count+1 == len(lst):
        print('.', end='')
      else:
        print(', ', end='')
    print('\n')

numeros = list()
cont = 1

while True:

  cabecalho('EX099 - Maior Número def()')
  print('''
  [1] - Cadastrar número
  [2] - maior()
  [3] - mostrar números cadastrados
  [4] - Sair''')
  
  #Entrada de opção
  strop = str(input('Escolha uma opção: '))
  while strop.isnumeric() == False:
    print('\033[31mOpção inválida\033[m')
    strop = str(input('Escolha uma opção: '))
  print()
  opcao = int(strop)
  

  #[1] - Cadastrar número
  if opcao == 1:
    
    numstr = str(input(f'Número {cont}: '))
    while numstr.isnumeric() == False:
      print('\033[31mDigite apenas números inteiros\033[m')
      numstr = str(input(f'Numero {cont}: '))
    num = int(numstr)
    
    cont += 1
    numeros.append(num)
    print()   

  #[2] - Maior()  
  elif opcao == 2:
    maior(numeros)
    print() 
  
  #[3] - Mostrar números cadastrados
  elif opcao == 3:
    mostrar(numeros)

  #[3] - Sair
  elif opcao == 4:
    break
    print()
  
  #Para entradas inválidas
  else:
    print('\033[31mOpção Inválida\033[m')
    print()

print('\n\033[1mSaindo do Programa\033[m')

