#Faça um programa que leia uma frase pelo teclado e mostre:
#- quantas vezes aparece a letra 'A'
#- Em que posição ela aparece a primeira vez
#- Em que posição ela aparece a última vez
print('-=-'*12)
print('EX026 - Primeira e última ocorrência')
print('-=-'*12)
print('\n')


phrase = input('Type something in here: ')
print('\n')

print('a) the character A appers {} time(s)' .format(phrase.lower().count('a')))
print('b) it appears for the first time on the position {}' .format((phrase.lower().find('a')+1)))
print('c) it appears for the last time on the position {}' .format((phrase.lower().rfind('a')+1)))
