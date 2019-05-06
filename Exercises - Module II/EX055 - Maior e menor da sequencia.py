#Faça um programa que leia o peso de cinco pessoas, no final mostre qual foi o maior e o menor peso lidos. 

print('\033[34m-=-'*12)
print('\033[33m EX055 - Maior e Menor da Sequência')
print('\033[34m-=-\033[m'*12)
print('\n')

major=-1000
minor=1000
for  index in range(0, 5):
  peso = float(input('Digite seu peso: '))
  if peso<0:
    print('Digite um valor válido')
  elif peso>major:
    major=peso
  elif peso<minor:
    minor=peso

print('\n')
print('Maior peso: {:.0f} kg' .format(major))
print('Menor peso: {:.0f} kg' .format(minor))