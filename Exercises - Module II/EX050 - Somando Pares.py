#Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o. 

print('\033[34m-=-'*8)
print('\033[33m  EX050 - Somando Pares')
print('\033[34m-=-\033[m'*8)
print('\n')

listnum = [0, 0, 0, 0, 0, 0]
sum = 0
for count in range(0, 6):
  listnum[count] = int(input('Digite um numero para a posição {}: ' .format(count+1)))
  if listnum[count]%2==0:
    sum+=listnum[count]

print('\033[1m\nA soma dos números pares é:\033[m {}' .format(sum))
