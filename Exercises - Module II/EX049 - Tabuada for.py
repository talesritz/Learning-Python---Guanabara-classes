#Refaça o DESAFIO 009 mostrando a tabuada de um numer que o usuario escolher, só que agora utilizando um laço FOR

print('\033[34m-=-'*6)
print('\033[33m EX049 - Tabuada')
print('\033[34m-=-\033[m'*6)
print('\n')

num = int(input('Digite um número de 1 a 10: '))


print('\n')
print('\033[1;32mTabuada do {}\033[m' .format(num))
for count in range (0, 11):
  print(' {} x {} = {}' .format(num, count, num*count))