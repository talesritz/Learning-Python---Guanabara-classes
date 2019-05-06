#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão.
#1 para binário
#2 para octal
#3 para hexadecimal

cores = {
  'vermelho' : '\033[31m',
  'limpa' : '\033[m'
}

print('\n')
print('\033[34m-=-\033[m'*9)
print('\033[33mEX037 - Conversor Numérico\033[m')
print('\033[34m-=-\033[m'*9)
print('\n')

print('Selecione o tipo de conversão:')
print('1. Binária')
print('2. Octal')
print('3. Hexadecimal')

num = int(input('Digite a opção desejada: '))
print('\n')

if num==1:
  print('{}AGUARDE - CONVERTENDO PARA BINÁRIO...{}' .format(cores['vermelho'], cores['limpa']))
elif num==2:
  print('{}AGUARDE - CONVERTENDO PARA OCTAL...{}' .format(cores['vermelho'], cores['limpa']))
elif num==3:
  print('{}AGUARDE - CONVERTENDO PARA HEXADECIMAL...{}' .format(cores['vermelho'], cores['limpa']))
else: 
  print('{}ERRO - Digite uma opção válida{}' .format(cores['vermelho'], cores['limpa']))