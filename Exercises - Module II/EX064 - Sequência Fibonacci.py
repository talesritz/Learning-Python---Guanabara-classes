#Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elemenos de uma sequência fibonacci.
print('\n')
print('\033[34m-=-'*9)
print('\033[33mEX063 - Sequência Fibonacci')
print('\033[34m-=-\033[m'*9)
print('\n')

n = int(input('Digite um número: '))

fibo = [0,1]
a=0
b=1

while b<=n-2:
  fibo.append(fibo[a]+fibo[b])
  a+=1
  b+=1

print(fibo)

#professor
'''n = int(input('Digite um número: ')) 

t1 = 0
t2 = 1

print(t1, t2, end=' ')

count = 0
while count-2 < n:
  t3 = t1+t2
  print(t3, end=' ')
  t1 = t2
  t2 = t3
  count+=1 '''