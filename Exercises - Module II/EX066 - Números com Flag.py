#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles. 

print('\033[34m-=-'*9)
print('\033[33mEX066 - Números com Flag')
print('\033[34m-=-\033[m'*9)
print('\n')

qtde = 0
soma =0
num = 0

while num != 999:
  num = int(input('Digite um número: '))
  if num==999:
    print('\n')
    break
  else:
    qtde+=1
    soma+=num

print('\033[1mENCERRANDO:\033[m ')
print(f'Quantidade: {qtde}')
print(f'Soma: {soma}') 
  