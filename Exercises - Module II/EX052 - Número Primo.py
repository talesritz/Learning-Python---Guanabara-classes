#Faça um programa que leia um numero inteiro e diga se ele é ou não um número primo.

print('\033[34m-=-'*8)
print('\033[33m EX052 - Números Primos')
print('\033[34m-=-\033[m'*8)
print('\n')

prime = int(input('Digite um número: '))

count = 0
for index in range(1, prime+1):
  #print('index: {}' .format(index))
  #print('R: {}' .format(prime%index))
  #print('\n')
  if prime%index==0:
    count = count+1
  #print('count: {}' .format(count))


if count==2:
  print('O número {} é primo' .format(prime))
else:
  print('O número {} NÃO é primo' .format(prime))