#Refaça o desafio 35 dos triangulos, acrescentando o recurso fr mostrar que tipo de triangulo sera formado.
#- equilatero: todos os lados iguais
#isosceles: dois lados iguais
#escaleno: todos os lados diferentes

a = float(input('Digite o lado A: '))
b = float(input('Digite o lado B: '))
c = float(input('Digite o lado C: '))

if a<=0 or b<=0 or c<=0:
  print('Não é possível construir um triângulo com essas medidas')
elif a<b+c and b<a+c and c<a+b and a>abs(b-c) and b>abs(a-c) and c>abs(a-b) and a==b and a==c and b==c:
   print('Este triângulo pode existir e é EQUILÁTERO')
elif a<b+c and b<a+c and c<a+b and a>abs(b-c) and b>abs(a-c) and c>abs(a-b) and a==b and a!=c or a==c and a!=b:
   print('Este triângulo pode existir e é ISÓSCELES.')
elif a<b+c and b<a+c and c<a+b and a>abs(b-c) and b>abs(a-c) and c>abs(a-b) and a!=b and a!=c and a!=b:
   print('Este triângulo pode existir e é ESCALENO.')
else:
   print('Não é possível construir um triângulo com essas medidas')
