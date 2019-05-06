#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá pergntar se o usuário vai continuar. No final mostre:
#a) Qual é o total gasto na compra.
#b) Quantos produtos custam mais de R$1000
#c) Qual é o nome do produto mais barato. 

print('\033[34m-=-'*11)
print('\033[33m EX070 - Estatística em Produtos')
print('\033[34m-=-\033[m'*11)
print('\n')

menor = float(100000000000000)
nomemenor = ''
total = float(0)
qtdemil = int(0)
continuar ='s'

while continuar == 's':

  nomeprod = str(input('Nome do produto: ')).strip()
  
  #valida se o preco é maior que 0
  valpreco = 'n'
  while valpreco == 'n':
    preco = float(input('Preço: '))
    if preco < 0:
      print('\033[1;31mValor inválido\033[m')
    else:
      total+=preco
      valpreco = 's'
    
    #mostra a quantidade de precos acima de 1000
    if preco > 1000:
      qtdemil+=1
    
    #mostra qual o menor valor
    if preco < menor:
      menor = preco
      nomemenor = nomeprod

  #valida se o usuário deseja continuar 
  valcontinuar = 'n' 
  while valcontinuar == 'n':
    continuar = input('Deseja continuar [S/N]? ').lower()

    if continuar not in 'nNsS':
      print('\033[31mValor Inválido\033[m')
    else:
      valcontinuar = 's'
      print('\n')
  

print(f'\033[33mTotal gasto:\033[m {total:.2f}')
print(f'\033[33mProdutos acima de R$1000:\033[m {qtdemil}')

if nomemenor ==  '':
  print(f'\033[33mProduto mais barato:\033[m Nenhum nome digitado')
else:
  print(f'\033[33mProduto mais barato:\033[m {nomemenor}')