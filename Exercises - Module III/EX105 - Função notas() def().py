#Faça um programa que tenha uma função chamada notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#- Quantidade de notas
#- A maior nota
#- A menor nota
#- A média da turma
#- A situação (opcional)
#Adicione também as docstrings da função. 

#Solução próxima do professor

def cabecalho(msg):
  print('='*40)
  print('{:^40}' .format(msg))
  print('='*40)
  print()
def sair():
  print('\n\033[1mSaindo do programa...\033[m')
def notas(*num, situacao=False):
  
  resumo = dict()
  maior = 0
  menor = 0
  soma = 0
  media = 0
  qtde = len(num)

  for count in range (0, len(num)):
    soma += num[count]
    if count == 0:
      maior = num[count]
      menor = num[count]
    else:
      if num[count] > maior:
        maior = num[count]
      if num[count] < menor:
        menor = num[count]
  
  resumo['maior'] = maior
  resumo['menor'] = menor
  resumo['media'] = (f'{soma/qtde:.2f}')
  if situacao == True:
    msg = ''
    if media < 6:
      msg = 'RUIM'
    elif media < 7:
      msg = 'RAZOÁVEL'
    elif media < 9:
      msg = 'BOA'
    else:
      msg = 'EXCELENTE'
    
    resumo['situacao'] = msg
    
  return resumo

     
cabecalho('EX105 - função notas() dict()')

print(notas(4, 5, 7, situacao=True))  

sair()


#Minha solução
'''
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
def situacao(msg):
  estados = ['aprovado', 'reprovado', 'recuperação']
  sit = input(msg)
  
  if sit in estados:
    return sit
  else:
    return 'Não há registro'
def continuar():

  valcont = input('Deseja continuar [S/N]: ').lower().strip()[0]
  while valcont not in 'sn':
    valcont = input('Deseja continuar [S/N]: ').lower().strip()[0]

  if valcont == 'n':
    return True
def preenchedict():
  global qtde
  print('{:-^40}' .format(f' Aluno {qtde} '))
  
  notaluno['nome'] = (f'Aluno {qtde}')
  notaluno['nota'] = leiaInt('Nota: ')
  notaluno['situacao'] = situacao('Situação: ')

  alunos.append(notaluno.copy())
  notaluno.clear()
  
  resumo['maior'] = maior(alunos)
  resumo['menor'] = menor(alunos)
  resumo['media'] = media(alunos)
  resumo['situacao'] = sitdict(resumo['media'])
    
  qtde += 1
def maior(lista):
  maior = 0
  
  if len(lista) == 0:
    return maior
  else: 
    for count in range(0, len(lista)):
      if count == 0:
        maior = lista[count]['nota']
        
      elif lista[count]['nota'] > maior:
        maior = lista[count]['nota']
    return maior 
def menor(lista):
  
  menor = 0

  if len(lista) == 0:
    return menor
  else:
    for count in range(0, len(lista)):
      if count == 0:
        menor = lista[count]['nota']
      elif lista[count]['nota'] < menor:
        menor = lista[count]['nota']
    return menor     
  
  print(menor)
def media(lista):
  
  soma = 0
  media = 0
  
  if len(lista) == 0:
    return media
  else:
    for count in range(0, len(lista)):
      soma += lista[count]['nota']
    
  media = soma/qtde
  return media
def sitdict(num):
  msg = ''
  if num < 6:
    msg = 'RUIM'
  elif num < 7:
    msg = 'MÉDIA'
  elif num < 9: 
    msg = 'BOA'
  else:
    msg = 'EXCELENTE'
  return msg
def notas(resumonotas, situacao=False):
  print()
  print('{:-^40}' . format(' Resumo '))
  print(f'Maior nota: {resumonotas["maior"]}')
  print(f'Menor nota: {resumonotas["menor"]}')
  print(f'Média: {resumonotas["media"]:.2f}')
  if situacao == True:
    print(f'Situação: {resumonotas["situacao"]}')
  


notaluno = dict()
resumo = dict()
alunos = list()
qtde = 1

cabecalho('EX105 - Função notas() dict()')

while True:
   
  preenchedict()

  if continuar():
    break
  print()

notas(resumo, situacao=True)

sair()
'''