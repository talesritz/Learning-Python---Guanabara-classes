#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiusculas e minusculas
#Quantas letras ao todo(sem considerar espaços)
#Quantas letras tem o primeiro nome

print('-=-'*8)
print('EX022- Analisador de textos')
print('-=-'*8)
print('\n')

name = input('Type your name here: ')

upper = name.upper()
lower = name.lower()
splited = name.split()
count = len((''.join(splited)))

print('a) All characters uppered: {}' .format(upper))
print('b) All characters lowered: {}' .format(lower))
print('c) Your name has {} characters ' .format(count))
print('d) The first name has {} characters' .format(len(splited[0])))