#Crie um programa que leia o nome de uma pessoa e diga se ela tem SILVA no nome. 

print('-=-'*8)
print('EX025 - Procurando uma String dentro de outra')
print('-=-'*8)
print('\n')

name = input('Type your name here: ')

print('Is SILVA part of your name?', 'SILVA' in name.upper())
