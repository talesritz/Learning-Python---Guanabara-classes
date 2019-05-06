#Refaça o Desafio 51, lendo o primeiro termo e a razao de uma PA. Mostrando os 10 primeiros termos a progressão utilizando a estrutura while. 
colors = {
  'red' : '\033[31m',
  'orange' : '\033[33m',
  'navy' : '\033[34m'
}

print('\033[34m-=-'*12)
print('\033[33mEX061 - Progressão Aritmética While')
print('\033[34m-=-\033[m'*12)

primt = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
enesimo = 1

while enesimo<=10:
  print(primt+(enesimo-1)*razao, end=' ')
  enesimo+=1