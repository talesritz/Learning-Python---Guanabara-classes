#Faça um programa que tenha um função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável. 

def cabecalho(x):
  print('='*40)
  print('{:^40}' .format(f'{x}'))
  print('='*40)
  print()

def escreva(msg):
  tamlin = len(msg)
  
  print()
  print('='*tamlin)
  print(msg)
  print('='*tamlin)
  print()
 

cabecalho('EX096 - Ajustando Texto def()')


escreva(str(input('Digite algo: ')))