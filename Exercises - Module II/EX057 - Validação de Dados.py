#Faça um programa que leio o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto. 

print('\033[34m-=-'*9)
print('\033[33mEX057 - Validação de dados')
print('\033[34m-=-\033[m'*9)
print('\n')

sexo = 'error'
while sexo=='error':
  sexo = str(input('Sexo [F/M]: ')).strip()
  if sexo in 'mMfF':
    print('Programa encerrado')
  else:
    sexo = 'error'

#simplificado
'''
sexo = str(input('Sexo [F/M]: ')).strip()
while not in 'mMfF':
  sexo = str(input('Sexo [F/M]: ')).strip()
print('Programa encerrado') '''