#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores  e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
print('\033[34m-=-'*9)
print('\033[33mEX065 - Maior e Menor Valor')
print('\033[34m-=-\033[m'*9)
print('\n')


total = 0
maior = -1000
menor = 1000
cont = 0
manter = 'S'

while manter in 'Ss':
  manter = str(input('Quer digitar um número? [S/N] ')).strip()
  if manter not in 'SsNn':
    print('\033[1;31mOpção Inválida\033[m\n')
    manter = 's'
  elif manter in 'nN':
    print('\n')
    break
  else:
    num = int(input('Digite um número: '))
    print('\n')
    cont+=1
    total+=num

    if num > maior:
      maior = num
    if num < menor:
      menor = num

print('\033[1mEncerrando programa: ')

if cont == 0:
  print('\033[33mMédia:\033[m Informações insuficientes')
  print('\033[33mMaior:\033[m Nenhum valor foi digitado')
  print('\033[33mMenor:\033[m Nenhum valor foi digitado')

elif cont == 1:
  maior = num
  menor = num
  print('\033[33mMédia:\033[m {:.2f}' .format(total/cont))
  print('\033[33mMaior:\033[m {}' .format(maior))
  print('\033[33mMenor:\033[m {}' .format(menor))

else:
  print('\033[33mMédia:\033[m {:.2f}' .format(total/cont))
  print('\033[33mMaior:\033[m {}' .format(maior))
  print('\033[33mMenor:\033[m {}' .format(menor))