#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais. 

print('='*40)
print('{:^40}' .format('EX077 - Contagem de Vogais'))
print('='*40)
print('\n')

words = ('carro', 'homem', 'mulher', 'bicicleta', 'caminhao', 'voar', 'espaco', 'treino')

for w in words:
  print(f'\nNa palavra {w.upper()} temos: ', end='')
  for count in range(0, len(w)):
    if w[count] in 'aeiou':
      print(f'{w[count]} ', end='')  
