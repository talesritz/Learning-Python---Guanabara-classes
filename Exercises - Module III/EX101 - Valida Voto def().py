#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições. 



def cabecalho(msg):
  print('='*40)
  print('{:^40}' .format(msg))
  print('='*40)
  print()
def voto(ybirth):
  from datetime import date
  
  tyear = date.today().year
  age = tyear - ybirth 

  if age < 16:
    return (f'Com {age} anos o voto é NEGADO')
  elif age < 18 or age > 65:
    return (f'Com {age} anos o voto é OPCIONAL') 
  else:
    return (f'Com {age} anos o voto é OBRIGATÓRIO')
  


  

  return str()


cabecalho('EX101 - Valida Voto def()')

num = int(input('Ano de Nascimento: '))
print(voto(num))