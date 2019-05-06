#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem.
#Seu programa tem que realizar três contagens através da função criada.
#a) de 1 até 10, de 1 em 1
#b) de 10 até 0, de 2 em 2
#c) uma contagem personalizada

from time import sleep
from sys import stdout

def cabecalho(msg):
  print('='*40)
  print('{:^40}' .format(f'{msg}'))
  print('='*40)
  print()
def lin():
  print('-'*40)
def contador(inicio, fim, passo):
  
  #VALIDADOR PASSO
  #Se passo = 0, passo será padrão 1, se for digitado -1 o sistema entenderá que ele quer contar de traz para frente 
  if passo == 0:
    passo = 1
  elif passo < 0:
    passo *= -1
    if inicio < fim:
      temp = inicio
      inicio = fim
      fim = temp
  
  
  lin()
  #PADRÃO (inicio<fim)
  if inicio < fim:
    
    print(f'Contagem de {inicio} até {fim}, de {passo} em {passo}: ')
    for count in range(inicio, fim+1, passo):
      print(f'{count} ', end='')
      stdout.flush()
      sleep(0.5)

    print()
  
  #Se o fim for maior, o programa consira que será uma contagem inversa
  elif inicio > fim:
    print(f'Contagem de {inicio} até {fim}, de {passo} em {passo}: ')
    passo *= -1
    for count in range(inicio, fim-1, passo):
      print(f'{count} ', end='')
      stdout.flush()
      sleep(0.5)
      
    print()

  lin()


cabecalho('EX098 - Contador Passos def()')

contador(1, 10, 1)
print()

contador(10, 0, 2)
print()

print('Agora é sua vez, digite início, fim e o passo da contagem')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)