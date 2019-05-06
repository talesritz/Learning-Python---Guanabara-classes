#Faça um programa que tenha uma lista chamada numeros e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro dda lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior. 

from random import randint
from sys import stdout
from time import sleep

def cabecalho(msg):
  print('='*40)
  print('{:^40}' .format(f'{msg}'))
  print('='*40)
  print()
def sorteia():
  numeros = list()

  print('Números sorteados: ', end='') 
  for count in range(0, 5):
    num = randint(0, 10)
    
    #printa o numero sorteado na posição count do laço e efetua a pausa SLEEP.
    print(num, end='')
    stdout.flush()
    sleep(0.5)
    
    #inserção de vírgula e ponto final
    if count+1 == 5:
      print('. ')
    else:
      print(', ', end='')
    
    #Joga os numeros para dentro da lista
    numeros.append(num)  
  

  return(numeros)      
def somaPar(lst):
  soma = 0
  for count in range(0, len(lst)):
    if lst[count]%2 == 0:
      soma += lst[count]
  
  if soma == 0:
    print('Não há Números pares na lista sorteada.')
  else:
    print(f'Soma: {soma}')

cabecalho('EX100 - Sorteio e somaPar def()')

somaPar(sorteia())

print('\n\033[1mSaindo do Programa\033[m')