#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas, no final do programa mostre: 
#- A média de idade do grupo
#- Qual é o homem mais velho
#- Quantas mulheres tem menos de 20 anos 

print('\033[34m-=-'*9)
print('\033[33mEX056 - Analisador Completo')
print('\033[34m-=-\033[m'*9)
print('\n')

majorh =-1000
majornome = ''
somaid = 0
countf = 0
cadastrados =0

for index in range(0, 4):
  print('Cadastro {}' .format(index+1))
  name = str(input('Digite seu nome: '))
  idade = int(input('Digite sua idade: '))
  sexo = str(input('Digite seu sexo (F/M): '))
  print('\n')

  #Se idade menor que zero, não considera o cadastro
  if idade<=0:
    print('\033[31mDigite valores válidos\033[m\n')
  else: 
    #conta quantas pessoas possuem cadastros válidos(média)
    cadastrados+=1
    #soma as idades para efetuar média no final
    somaid+=idade
    
    #valida qual o homem mais velho
    if sexo.lower()=='m' and idade>0 and idade>majorh:
      majorh=idade
      majornome = name
    
    #verificar quantas mulheres com menos de 20 anos
    if sexo.lower()=='f' and idade<20:
      countf+=1

print('\n')
#valida quantas pessoas se cadastraram e mostra a média 
if somaid<=0:
  print('\033[33mMédia de idade do grupo:\033[m Não há cadastros suficientes')
else:
  print('\033[33mMédia de idade do grupo:\033[m {} anos' .format(somaid/cadastrados))

#mostra o homem mais velho: idade e nome
if majorh<=0:
  print('\033[33mHomem mais velho:\033[m Não há cadastros suficientes')
else:
  print('\033[33mHomem mais velho:\033[m {} com {} anos' .format(majornome, majorh))  

#mostra quantas mulheres com menos de 20 anos
if countf<=0:
  print('\033[33mMulheres com menos de 20 anos:\033[m Não há cadastros suficientes')
else:
  print('\033[33mMulheres com menos de 20 anos:\033[m {}' .format(countf))
