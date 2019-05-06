#A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade.
#até 9 anos: MIRIM
#até 14 anos: INFANTIL
#até 19 anos : JUNIOR
#até 20 anos SÊNIOR
#Acima: MASTER

from datetime import datetime, date, timedelta

print('\n')
print('\033[34m-=-\033[m'*10)
print('\033[33mEX041 - Classificando Atletas\033[m')
print('\033[34m-=-\033[m'*10)
print('\n')

bday = str(input('Digite sua data de nascimento: '))

bdaydate = datetime.strptime(bday, '%d/%m/%Y').date()
today =date.today()

print(bdaydate)
print(today)
print('Hoje menos 1 ano: {}' .format(today-timedelta(days=365)))
print('\n')

#timedelta(days=365)))
novey = today-timedelta(days=3285)
#print(novey)

#implantar reconhecimento de ano bissexto***
if novey<bdaydate :
  print('Classificação: MIRIM')
elif  today-timedelta(days=5110)<bdaydate:
  print('Classificação: INFANTIL')
elif today-timedelta(days=6935)<bdaydate:
  print('Classificação: JUNIOR')
elif today-timedelta(days=7300)<bdaydate:
  print('Classificação: SÊNIOR')  
else: 
  print('Classificação: MASTER')

