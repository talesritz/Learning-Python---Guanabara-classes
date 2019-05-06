#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'

print('-=-'*13)
print('EX024 - Verificando as Primeiras Letras')
print('-=-'*13)
print('\n')

name = input('type your citys name here: ').strip()

splited = name.split()

print('Does the name of the city starts with Santo?: ', 'SANTO' in splited.upper())