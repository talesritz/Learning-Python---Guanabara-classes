#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantos já são maiores. 
print('\033[34m-=-'*9)
print('\033[33mEX054 - Grupo da Maioridade')
print('\033[34m-=-\033[m'*9)
print('\n')

from datetime import date, datetime, timedelta

today = date.today()
major = 0
minor = 0

#1 year = 6570
print('\n')
for index in range(0, 7): 
  bday = datetime.strptime(input('Digite seu aniversário: '), '%d/%m/%Y').date() 
  
  if bday>today:
    print('Digite o aniversário de alguém que já tenha nascido.')
  elif today-timedelta(days=6570)<bday:
    minor+=1
  else: 
    major+=1

print('{} pessoas possuem mais de 18 anos' .format(major))
print('{} pessoas possuem menos de 18 anos' .format(minor)) 
