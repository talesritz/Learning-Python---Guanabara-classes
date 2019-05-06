#Faça um programa que calcule a soma entre todos os numeros impares que são multiplos de 3 e que se encontram no intervalo de 1 até 500. 

print('\033[34m-=-'*8)
print('\033[33mEX048 - Somando Ímpares')
print('\033[34m-=-\033[m'*8)
print('\n')

sum = 0
qtde = 0
for count in range (1, 500):
  if count%2!=0 and count%3==0:
    qtde += 1
    sum += count
    #print('Count: {}' .format(count))
    #print('Soma: {}\n' .format(sum))
    

print('A soma entre todos os {} números ímpares divisíveis por 3 é: {}' .format(qtde, sum))