#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido. 

from random import sample, choice

print('-=-'*12)
print('EX019 - Sorteando um nome na lista')
print('-=-'*12)
print('\n')

a = str(input('Digite o primeiro aluno: '))
b = str(input('Digite o segundo aluno: '))
c = str(input('Digite o terceiro aluno: '))
d = str(input('Digite o quarto aluno: '))
alunos = [a, b, c, d]
rand = choice(alunos)
#rand = sample(alunos, k=1)

print('\n')
print('O aluno escolhido para apagar o quadro é o(a): {}' .format(rand))