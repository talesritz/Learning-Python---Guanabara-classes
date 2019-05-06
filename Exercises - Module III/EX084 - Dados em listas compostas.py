#Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#a) Quantas pessoas foram cadastradas
#b) Uma listagem com as pessoas mais pesadas.
#c) Uma listagem com as pessoas mais leves. 

print('='*40)
print('{:^40}' .format('EX084 - Dados Lista Composta'))
print('='*40)
print('\n')

pessoas = list()
cadastro = list()
cadqtde = 0
pes = list()
lev = list()


valcont = 's'
while valcont == 's':
  #registra as entradas de dados
  cadastro.append(str(input('Digite seu nome: ').strip()))
  cadastro.append(int(input('Digite seu peso: ')))
  
  #adiciona as entradas a lista permanente e efetua a contagem
  pessoas.append(cadastro[:])
  cadastro.clear()
  cadqtde += 1 
  
  #Valida se o usuário deseja continuar
  while valcont == 's':
    cont = str(input('Deseja continuar [S/N]: '))

    if cont.lower() == 's':
      break
    elif cont.lower() == 'n':
      valcont = 'n'
    else:
      print('\033[31mOpção Inválida\033[m')
  print('\n')    

#registra as pessoas leves e pesadas
for count in range(0, len(pessoas)):
  
  if pessoas[count][1] < 65:
    lev.append(pessoas[count])
  elif pessoas[count][1] > 90:
    pes.append(pessoas[count])

#a)
print(f'a) {cadqtde} cadastro(s) registrados \n')

#b)
if pes == []:
  print('b) Não há pessoas acima do peso')
else:
  print('b)Pesados da turma: ')
  for count in range(0, len(pes)):
    print(f'  {pes[count][0]} com {pes[count][1]} Kg')
print('\n')

#c)
if lev == []:
  print('c) Não há pessoas abaixo do peso')
else:
  print('c)Leves da turma: ')
  for count in range(0, len(lev)):
    print(f'  {lev[count][0]} com {lev[count][1]} Kg')


#sai do programa
print('\n\033[1mSaindo do Programa...\033[m')