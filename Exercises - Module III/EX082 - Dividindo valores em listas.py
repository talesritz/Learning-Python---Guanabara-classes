#Crie um programa que vai ler vários numeros e colocar em uma lista.
#Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente.
#Ao final, mostre o conteúdo das tres listas geradas. 

print('='*38)
print('{:^38}' .format('EX082 - Dividindo valores entre Listas'))
print('='*38)
print('\n')

lista = list()
pares = list()
impares = list()

valcont = 's'
while valcont == 's':
  lista.append(int(input('\nDigite um número: ')))
  
  while valcont != 'n':
    cont = str(input('Deseja continuar [S/N]: '))
    if cont.lower()[0] == 's':
      break
    elif cont.lower()[0] == 'n':
      valcont = 'n'
    else:
      print('\033[31mOpção Inválida\033[m')


for count in range(0, len(lista)):
  if lista[count]%2 == 0:
    pares.append(lista[count])
  else:
    impares.append(lista[count])


print(f'\nLista completa: {lista}')
print(f'Lista Pares: {pares}')
print(f'Lista Ímpares: {impares}')


print('\n\033[1mSaindo do Programa...')