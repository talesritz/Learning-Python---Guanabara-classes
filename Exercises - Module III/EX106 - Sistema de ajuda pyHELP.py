#Faça um mini-sistema que utilize o interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerarrá.
#OBS: use cores

from time import sleep
cores = {
  'branco': '\033[30;7m',
  'vermelho': '\033[1;31;40;7m',
  'verde': '\033[1;32;40;7m',
  'laranja': '\033[33;7m',
  'azul': '\033[30;44m',
  'roxo': '\033[35;7m',
  'anil': '\033[1;36;40;7m',
  'cinza': '\033[37;7m',
  'limpacor': '\033[m'
}

def cabecalho(msg):
    print('='*40)
    print('{:^40}' .format(msg))
    print('='*40)
    print()
def sair():
  bye = 'Até Logo!!!'

  titulo(bye, cores['vermelho'])
def titulo(msg, cor=0):

  print(cor, end='')
  print('-'*len(msg))
  print(msg)
  print('-'*len(msg))
  print(cores['limpacor'], end='')
def ajuda(msg):
    titulo(f'Analisando o comando "{msg}"', cores['anil'])
    sleep(1)
    print(cores['branco'], end='')
    help(msg)
    print(cores['limpacor'], end='')
    sleep(1)

cabecalho('EX106 - Sistema de Ajuda pyHelp')

while True:

    titulo('Sistema de Ajuda pyHELP', cores['verde'])
    func = str(input('Função ou módulo: '))

    if func.lower() == 'fim':
        sair()
        break
    else:
        ajuda(func)

