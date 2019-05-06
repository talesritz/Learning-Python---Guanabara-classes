#Crie um programa que leia dois valores e mostre um menu na tela:
#[1]somar
#[2]multiplicar
#[3]maior
#[4]novos números
#[5]sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso. 

print('\033[34m-=-'*8)
print('\033[33m EX059 - Menu de Opções')
print('\033[34m-=-\033[m'*8)

print('\n')
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

print('''\033[1m
  [1] Somar
  [2] Multiplicar 
  [3] Maior
  [4] Novos números
  [5] Sair do programa
  \033[m''')

opcao = str(input('\033[1m  Digite uma opção: \033[m')).strip()

while opcao!=5:
  if opcao=='1':
    print('\n')
    print('\033[1mSOMA\033[m')   
    print('A soma entre \033[33m{}\033[m e \033[33m{}\033[m é: \033[1;32m{}\033[m' .format(num1, num2, num1+num2))
    print('\n')
   
    #menu
    print('''\033[1m
  [1] Somar
  [2] Multiplicar 
  [3] Maior
  [4] Novos números
  [5] Sair do programa
  \033[m''')

    opcao = str(input('\033[1m  Digite outra opção: \033[m')).strip()

  elif opcao=='2':
    print('\n')
    print('\033[1mMULTIPLICAÇÃO\033[m')
    print('O produto entre \033[33m{}\033[m e \033[33m{}\033[m é: \033[1;32m{}\033[m' .format(num1, num2, num1*num2))

    #menu
    print('''\033[1m
  [1] Somar
  [2] Multiplicar 
  [3] Maior
  [4] Novos números
  [5] Sair do programa
  \033[m''')

    opcao = str(input('\033[1m  Digite outra opção: \033[m')).strip()

  elif opcao=='3':
    print('\n')
    print('\033[1mMAIOR NÚMERO\033[m')
  
    if num1==num2:
      print('Os números \033[33m{}\033[m e \033[33m{}\033[m \033[1;32mSÃO IGUAIS!\033[m' .format(num1, num2, num1*num2))
    elif num1>num2:
      print('O maior número entre \033[33m{}\033[m e \033[33m{}\033[m é: \033[1;32m{}\033[m' .format(num1, num2, num1))
    else:
      print('O maior número entre \033[33m{}\033[m e \033[33m{}\033[m é: \033[1;32m{}\033[m' .format(num1, num2, num2))

    #menu
    print('''\033[1m
  [1] Somar
  [2] Multiplicar 
  [3] Maior
  [4] Novos números
  [5] Sair do programa
  \033[m''')

    opcao = str(input('\033[1m  Digite outra opção: \033[m')).strip()
  
  elif opcao=='4':
    print('\n')
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))  

   #menu
    print('''\033[1m
  [1] Somar
  [2] Multiplicar 
  [3] Maior
  [4] Novos números
  [5] Sair do programa
  \033[m''')

    opcao = str(input('\033[1m  Digite outra opção: \033[m')).strip()
  
  elif opcao=='5':
    break

  else:
    print('\n  \033[1;31mOPÇÃO INVÁLIDA\033[m')
    opcao = str(input('\033[1m  Digite outra opção: \033[m')).strip()

print('\n  \033[1mSaindo...')

#SOLUÇÃO PROFESSOR
'''#Crie um programa que leia dois valores e mostre um menu na tela:
#[1]somar
#[2]multiplicar
#[3]maior
#[4]novos números
#[5]sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso. 

print('\033[34m-=-'*8)
print('\033[33m EX059 - Menu de Opções')
print('\033[34m-=-\033[m'*8)

print('\n')
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

opcao='0'
while opcao!='5':
  #menu
  print('''\033[1m
  [1] Somar
  [2] Multiplicar 
  [3] Maior
  [4] Novos números
  [5] Sair do programa
  \033[m''')

  opcao = str(input('\033[1m  Digite uma opção: \033[m')).strip()
  
  #Soma
  if opcao=='1':
    print('\n')
    print('\033[1mSOMA\033[m')   
    print('A soma entre \033[33m{}\033[m e \033[33m{}\033[m é: \033[1;32m{}\033[m' .format(num1, num2, num1+num2))
    print('\n')

  #Multiplicação 
  elif opcao=='2':
    print('\n')
    print('\033[1mMULTIPLICAÇÃO\033[m')
    print('O produto entre \033[33m{}\033[m e \033[33m{}\033[m é: \033[1;32m{}\033[m' .format(num1, num2, num1*num2))
  #Maior número
  elif opcao=='3':
    print('\n')
    print('\033[1mMAIOR NÚMERO\033[m')
  
    if num1==num2:
      print('Os números \033[33m{}\033[m e \033[33m{}\033[m \033[1;32mSÃO IGUAIS!\033[m' .format(num1, num2, num1*num2))
    elif num1>num2:
      print('O maior número entre \033[33m{}\033[m e \033[33m{}\033[m é: \033[1;32m{}\033[m' .format(num1, num2, num1))
    else:
      print('O maior número entre \033[33m{}\033[m e \033[33m{}\033[m é: \033[1;32m{}\033[m' .format(num1, num2, num2))

  #Novo número 
  elif opcao=='4':
    print('\n')
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))  
  
  elif opcao=='5':
    break

  else:
    print('\n  \033[1;31mOPÇÃO INVÁLIDA\033[m')

#FIM  
print('\n  \033[1mSaindo...')'''
