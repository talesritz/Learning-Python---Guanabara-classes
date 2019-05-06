#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

print('-=-'*10)
print('EX017 - Catetos e Hipotenusa')
print('-=-'*10)
print('\n')


catop = int(input('Cateto Oposto: '))
catad = int(input('Cateto Adjacente: '))
hip = (catop**2 + catad**2)*0.5

print('A hipotenusa mede: {}' .format(hip))