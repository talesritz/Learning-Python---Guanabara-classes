#Crie um programa que leia dois números e mostre a soma entre eles

cores = {
  'vermelho':'\033[31m',
  'amarelo' : '\033[33m',
  'azul' : '\033[36m',
  'limpa': '\033[m' 
}

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))

print('A soma entre {}{}{} e {}{}{} é: {}{}{}!' .format(cores['vermelho'],a, cores['limpa'],cores['amarelo'], b, cores['limpa'],cores['azul'], a+b , cores['limpa']))
   