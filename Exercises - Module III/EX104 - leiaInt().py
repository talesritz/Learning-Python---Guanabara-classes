#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.

def cabecalho(msg):
  print('='*40)
  print('{:^40}' .format(msg))
  print('='*40)
  print()
def sair():
  print('\n\033[1mSaindo do programa...\033[m')
def leiaInt(msg):
  """
  param msg: recebe a mensagem de input 
  return: retorna o valor já validade como int()
  """

  num = str(input(msg))
  while num.isnumeric() == False:
    print('\033[31mDigite apenas números\033[m')
    num = str(input(msg))
  
  return int(num)


cabecalho('EX104 - Leiaint()')

n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')

sair()