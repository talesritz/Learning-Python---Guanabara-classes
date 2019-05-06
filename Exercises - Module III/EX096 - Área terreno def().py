#Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular(largura e comprimento) e mostre a área do terreno. 

def cabecalho(x):
  print('='*40)
  print('{:^40}' .format(f'{x}'))
  print('='*40)
  print()

def area(x, y):
  area = x*y 
  return area

cabecalho('EX096 - Área terreno def()')

largura = float(input('Largura: '))
comprimento = float(input('Comprimento: '))

print(f'Área: {area(largura, comprimento):.2f} m²')
