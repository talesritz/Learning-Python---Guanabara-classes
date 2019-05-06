#Crie um programa que leia um número Real qualuer pelo teclado e mostre na tela a sua porção inteira.
#Ex: Digite um número: 6.127
#O número 6.127 tem a parte inteira 6.
print('\n')
print('-=-'*9)
print('EX016 - Quebrando um número')
print('-=-'*9)
print('\n')

num = float(input('Digite um número: '))
print('O número {} tem a parte inteira {:.0f}' .format(num, num//1))