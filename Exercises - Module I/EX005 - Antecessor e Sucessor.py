#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

num = int(input('Digite um número inteiro: '))

print('O número digitado foi {}, seu antecessor é {} e seu sucessor é {}. ' .format(num, num-1, num+1))