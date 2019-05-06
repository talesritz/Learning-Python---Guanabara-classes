#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta. 
print('='*38)
print('{:^38}' .format('EX083 - Validando Exp. Matemáticas'))
print('='*38)
print('\n')

abre = list()
fecha = list()
valexp = 'n'

exp = str(input('Digite uma expressão matemática:\n '))

for count in range(0, len(exp)):
  if exp[count] == '(':
    abre.append(count)
  elif exp[count] == ')':
    fecha.append(count)

if len(abre) != len(fecha):
  valexp = 'n'
else:
  for count in range(0, len(abre)):
    if abre[count] > fecha[count]:
      valexp = 'n'
      break
    else:
      valexp = 's'

if valexp == 's':
  print('\n\033[32;1mExpressão válida\033[m')
else:
  print('\n\033[31;1mExpressão Inválida\033[m')