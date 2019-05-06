#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela. 

print('='*40)
print('{:^40}' .format('EX090 - Dicionário em Python'))
print('='*40)
print()

cadastro = dict()

cadastro['Nome'] = str(input('Nome: '))
cadastro['Media'] = float(input('Média [0-10]: '))

if cadastro['Media'] >= 7:
  cadastro['Situacao'] = '\033[32mAprovado\033[m'
elif cadastro['Media'] < 7:
  cadastro['Situacao'] = '\033[31mReprovado\033[m'
else:
  cadastro['Situacao'] = 'teste'

print()

print(f'Aluno \033[31;1m{cadastro["Nome"]}\033[m cadastrado com sucesso!')
print('\n\033[1mCADASTRO \033[m ')
for k, v in cadastro.items():
  print(f'{k}: {v}')