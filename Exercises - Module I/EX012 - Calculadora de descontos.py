#Faça um algoritmo que leia o preço de um produo e mostre seu novo preço com 5% de desconto

print('-=-'*7)
print('Simulador de Descontos')
print('-=-'*7)

preco = float(input('Digite o preço do produto: '))
desc = float(input('Quantos % de desconto: '))

print('\n')
print('Preço atual: {:.2f}' .format(preco))
print('Preço com {}% de desconto: {:.2f}' .format(desc, preco-(preco*(desc/100)))) 