#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada. 

from random import sample, choice, shuffle

print('-=-'*12)
print('EX020 - Sorteando ordem de alunos')
print('-=-'*12)
print('\n')

a = str(input('Digite o primeiro aluno: '))
b = str(input('Digite o segundo aluno: '))
c = str(input('Digite o terceiro aluno: '))
d = str(input('Digite o quarto aluno: '))
alunos = [a, b, c, d]
shuffle(alunos)

print('A ordem de apresentação de trabalhos será: {}' .format(alunos))