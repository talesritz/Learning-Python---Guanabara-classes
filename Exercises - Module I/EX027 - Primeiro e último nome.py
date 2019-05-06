#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
print('\n')
print('-=-'*10)
print("EX028 - Primeiro e último nome")
print('-=-'*10)
print('\n')

name = input('Type your name here: ')

splited = name.split()
firstname =  splited[0]
lastname = splited[name.count(' ')]

print("The first name is {} and the last one is {}" .format(firstname, lastname))