#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de jogador e quantos gols ele marcou.
#O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente. 

#Solução próxima ao do professor
def cabecalho(msg):
  print('='*40)
  print('{:^40}' .format(msg))
  print('='*40)
  print()
def ficha(a = '', b = ''):
  """
  param a: Corresponde ao nome do jogador
  param b: Corresponde a quantidade de jogos 
  return: retorna a frase com nome e qtde de jogos
  """   
  if a == '':
    a = '<desconhecido>'
  if b == '':
    b = '0'
  return (f'O jogador {a} fez {b} gol(s)')


cabecalho('EX103 - Ficha def() Opcional')

nome = str(input('Nome: '))
qtdegols = str(input('Quantidade de gols: '))
print(ficha(nome, qtdegols))




#Minha Solução
'''vago = 'Não há dados registrados'

def cabecalho(msg):
  print('='*40)
  print('{:^40}' .format(msg))
  print('='*40)
  print()
def ficha(a= vago, b = vago):
  """
  param a: recebe o nome para dict()
  param b: recebe a qtde de gols para dict()
  return: retorna o cadastro mesmo que vago como dict()
  """    
  cadastro = dict()
  
  cadastro['nome'] = a
  cadastro['qtdegols'] = b
  
  return cadastro



cabecalho('EX103 - Ficha def() Opcional')

nome = str(input('Nome: '))
qtdegols = str(input('Quantidade de Gols: '))

cadastro = ficha(nome, qtdegols)

print('\n{:-^40}' . format(' Cadastro '))
print(f'Nome: {cadastro["nome"]}')
print(f'Quantidade de gols: {cadastro["qtdegols"]}')
'''