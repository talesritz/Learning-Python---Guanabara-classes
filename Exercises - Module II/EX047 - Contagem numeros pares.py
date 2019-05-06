#Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50. 
print('\033[34m-=-'*11)
print('\033[31mEX047 - Contagem de Números Pares')
print('\033[34m-=-\033[m'*11)
print('\n')

sum = 0
for count in range(1, 50, 1):
  if count%2==0:
    print(count)
