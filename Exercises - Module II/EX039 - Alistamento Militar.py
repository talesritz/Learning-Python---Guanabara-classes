#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#- Se ele ainda vai se alistar ao serviço militar.
#- Se é a hora de se alistar
#- Se já passou o tempo do alistamento

#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo. 

from datetime import date

print('\n')
print('\033[34m-=-\033[m'*9)
print('\033[33mEX039 - Alistamento Militar\033[m')
print('\033[34m-=-\033[m'*9)
print('\n') 

anivdia = int(input('Digite o dia do seu aniversário: '))
anivmes = int(input('Digite o mês do seu aniversário: '))
anivano = int(input('Digite o ano do seu aniversário: '))
hoje = date.today()

#print(hoje)
print('\n')

if anivano+18>hoje.year:
  print('\033[1;33mNão chegou a data de seu alistamento\033[m')

elif anivano+18==hoje.year and anivmes<hoje.month:
  print('\033[1;33mNão chegou a data de seu alistamento\033[m')

elif anivano+18==hoje.year and anivmes>hoje.month:
  print('\033[1;31mVocê está atrasado para se alistar\033[m')

elif anivano+18==hoje.year and anivmes==hoje.month and anivdia<hoje.day:
  print('\033[1;33mNão chegou a data de seu alistamento\033[m')

elif anivano+18==hoje.year and anivmes==hoje.month and anivdia==hoje.day:
  print('\033[1;32mHOJE É O DA DO SEU ALISTAMENTO!\033[m')

elif anivano+18==hoje.year and anivmes==hoje.month and anivdia>hoje.day:
  print('\033[1;31mVocê está atrasado para se alistar\033[m')
else:
  print('\033[1;31mVocê está atrasado para se alistar\033[m')
