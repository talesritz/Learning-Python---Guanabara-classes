#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#- Média abaixo de 5.0
#REPROVADo
#- Média entre 5.0 e 6.9
#RECUPERACAO
#-Média 7.0 ou superior
#APROVADO

print('\033[1;34m-=-\033[m' *10)
print('\033[33mEX040 - Média entre duas notas\033[m')
print('\033[1;34m-=-\033[m' *10)

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1+nota2)/2

print('\n')
if media<5 and media>=0:
  print('\033[31mREPROVADO\033[m')
elif media >=5 and media<7:
  print('\033[33mRECUPERAÇÃO\033[m')
elif media>=7 and media<=10:
  print('\033[32mAPROVADO\033[m')
else:
  print('\033[1mDigite uma nota válida')
