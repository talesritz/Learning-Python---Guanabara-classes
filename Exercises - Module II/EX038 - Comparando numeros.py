#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
#- O primeiro valor é maior
#- O segundo valor é maior
#- Não existe valor maior, os dois são iguais

cores = {
  'vermelho' : '\033[33m',
  'anil' : '\033[34m',
  'limpa' : '\033[m'
}

print('\n')
print('\033[34m-=-\033[m'*9)
print('\033[33mEX038 - Comparando Números\033[m')
print('\033[34m-=-\033[m'*9)
print('\n') 

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))

if a>b:
  print('O {}primeiro valor{} é {}maior{}' .format(cores['vermelho'], cores['limpa'], cores['anil'], cores['limpa']))
elif b>a:
  print('O {}segundo valor{} é {}maior{}' .format(cores['vermelho'], cores['limpa'], cores['anil'], cores['limpa']))
else:
  print('{}Não existe{} valor maior, os dois são {}iguais{}' .format(cores['vermelho'], cores['limpa'], cores['anil'], cores['limpa']))
