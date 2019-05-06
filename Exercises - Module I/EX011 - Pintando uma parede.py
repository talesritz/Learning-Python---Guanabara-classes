#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²

print('-=-'*7)
print('Simulador de pintura')
print('-=-'*7)

largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))
area = largura*altura
print('\n')
print('A parede possui {:.2f} m² e será necessário {:.2f}L de tinta' .format(area, area/2))