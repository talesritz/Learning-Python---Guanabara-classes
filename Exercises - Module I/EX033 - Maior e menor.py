print('\n')
print('-=-'*7)
print('EX033 - Maior e menor ')
print('-=-'*7)
print('\n')

a = int(input('Digite um valor para A: '))
b = int(input('Digite um valor para B: '))
c = int(input('Digite um valor para C: '))

menor = 0
maior = 0

if a>b and b>c:
  maior = a
  menor = c
else:
  if a>c and c>b:
    maior = a
    menor = b
  else:
    if b>a and a>c:
      maior = b
      menor = c
    else:
      if b>c and c>a:
        maior = b
        menor = a
      else:
        if c>a and a>b:
          maior = c
          menor = b
        else:
          maior = c
          menor = a 


print('Maior valor: {}' .format(maior))
print('Menor valor: {}' .format(menor))
