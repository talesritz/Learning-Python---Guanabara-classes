#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles.
print('\033[34m-=-'*8)
print('\033[33mEX064 - Tratando Valores')
print('\033[34m-=-\033[m'*8)
print('\n')

num = 0
soma = 0
qtde = 0

while num != 999:
  num = int(input('Digite um valor: '))
   
  if num!=999:
    soma+=num
    qtde+=1
  
print('\nFinalizando: ')
print('Quantidade: {} ' .format(qtde))
print('Soma: {}' .format(soma))
