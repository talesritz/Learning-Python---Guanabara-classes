#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo. 

a = float(input('Digite o lado A: '))
b = float(input('Digite o lado B: '))
c = float(input('Digite o lado C: '))

if a<=0 or b<=0 or c<=0:
  print('Não é possível construir um triângulo com essas medidas')
else:
 if a<b+c and b<a+c and c<a+b and a>abs(b-c) and b>abs(a-c) and c>abs(a-b):
   print('Este triângulo pode existir')
 else:
   print('Não é possível construir um triângulo com essas medidas')
