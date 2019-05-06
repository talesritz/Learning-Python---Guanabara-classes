#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. 
#Considere US$1.00 = 3.27

din = float(input('Diga quanto tens para saber a conversão em dólares: '))

print('Para a quantia de {:.2f} reais você poderá trocar por {:.2f} dólares.' .format(din, din/3.27))