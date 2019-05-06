#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final mostre os 10 primeiros termos dessa progressão. 

print('\033[34m-=-'*10)
print('\033[33mEX051 - Progressão Aritmética')
print('\033[34m-=-\033[m'*10)
print('\n')

termos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
termos[0] = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))

print('\n')


for index in range (1, 11):
  termos[index-1] = termos[0] + (index-1)*razao
  print(termos[index-1], end=' ')