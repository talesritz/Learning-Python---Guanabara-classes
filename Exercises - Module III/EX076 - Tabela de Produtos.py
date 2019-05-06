#Crie um programa que tenha uma tupla única com nomes de produtos e seus respecivos preços na sequência.
#No final, mostre uma listagem de preços, organizando os dados em forma tabular
print('='*40)
print('{:^40}' .format('EX076 - Listagem de Preços'))
print('='*40)
print('\n')

tabprodutos = ('Ovo da Páscoa', 2.99,
               'Costela Ripa', 119.89,
               'Cerveja Stela Artois 250ml', 2.79, 'Maionese Hellmanns', 6.79, 
               'Nescau 1Kg', 9.89, 
               'Caixa de Bombom Nestlé', 7.99, 'Salsicha Seara', 5.90, 
               'Guaraná Antártica 2L', 4.99, 
               'ovo', 4.00)

#professor

print('-'*40)
print('{:^40}' .format('TABELA DE PREÇOS'))
print('-'*40)
print('\n')

for count in range(0, len(tabprodutos)):
  if count%2 == 0:
    print(f'{tabprodutos[count]:.<30}', end='')
  else:
    print(f'R$ {tabprodutos[count]:>7.2f}')

print('-'*40)





#minha maneira
'''
lenprod = 0
rightalign = 0

print('='*48)
print('{:^48}' .format('LISTAGEM DE PREÇOS'))
print('='*48)

for count in range(0, len(tabprodutos)):
  if count%2 == 0:
    print(tabprodutos[count], end=' ')
    
    #efetua o distanciamento automatico 
    lenprod = len(tabprodutos[count])
    rightalign = 40-lenprod
    for count in range(0, rightalign):
      print('.', end='')

  else:
    print(f'R$ {tabprodutos[count]:.2f}')

print('='*48) '''