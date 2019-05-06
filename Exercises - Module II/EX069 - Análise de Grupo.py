#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#a) quantas pessoas tem mais de 18 anos.
#b) Quantos homens foram cadastrados
#c) Quantas mulheres tem menos de 20 anos
print('\033[34m-=-'*9)
print('\033[33m EX069 - Análise de Grupo')
print('\033[34m-=-\033[m'*9)
print('\n')

idade = 0
sexo = ''
maisdz = 0
homens = 0
mulheresnv = 0

continuar ='s'
while continuar == 's':

  #input idade 
  validade = 'n'
  while validade == 'n':
    idade = int(input('Digite a idade: '))
    
    if idade <= 0:
      print('\033[1;31mValor Inválido\033[m')
    else:
      validade = 's'
  
  #input sexo
  valsexo = 'n'
  while valsexo == 'n':
    sexo = str(input('Digite o sexo [M/F]: '))

    if sexo not in 'mMfF':
      print('\033[1;31mValor Inválido\033[m')
    else:
      valsexo = 's'
  
  #Pessoas com mais de 18 anos
  if idade >=18:
    maisdz+=1
  #Quantidade de homens
  if sexo in 'Mm':
    homens+=1
  #Mulheres com menos de 20 anos
  if sexo in 'Ff' and idade < 20:
    mulheresnv+=1
  
  #input continuar
  valcontinuar = 'n'
  while valcontinuar == 'n':
    continuar = str(input('Deseja continuar [S/N?]: ')).strip().lower()

    if continuar not in 'SsNn':
      print('\033[1;31mValor Inválido\033[m')
    else:
      valcontinuar = 's'

if maisdz == 0:
    print(f'\033[33mPessoas com mais de 18 anos:\033[m 0')
else: 
  print(f'\033[33mPessoas com mais de 18 anos:\033[m {maisdz}')

if homens == 0: 
  print(f'\033[33mQuantidade de homens:\033[m 0')
else:
  print(f'\033[33mQuantidade de homens:\033[m {homens}')

if mulheresnv == 0: 
  print(f'\033[33mMulheres com menos de 20 anos:\033[m 0')
else:
  print(f'\033[33mMulheres com menos de 20 anos:\033[m {mulheresnv}')