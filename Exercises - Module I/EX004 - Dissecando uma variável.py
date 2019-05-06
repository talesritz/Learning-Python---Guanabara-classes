#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.  

algo = input('Digite algo: ')

print('Qual é o tipo primitivo: {} '.format(type(algo)))
print('Só tem espaços? {}' .format(algo.isspace()))
print('É um número? {}' .format(algo.isnumeric()))
print('São letras? {}' . format(algo.isalpha()))
print('É alfa-numérico? {}' .format(algo.isalnum()))
print('É maiúscula? {}' . format(algo.isupper()))
print('É minúscula? {}' .format(algo.islower()))
print('É capitalizada? {}' .format(algo.istitle()))