#Crie um programa que tenha uma tupla totalente preenchida por extenso, de zero até vinte. 
#Seu programa deverá ler um número pelo teclado (entre 0 e 20 e mostrá-lo por extenso.

numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze' , 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')



while True:
  num = int(input('Digite um número: '))
  if num <0 or num>20:
    print('\033[31mValor Inválido\033[m')
  else:
    print(f"O número {num} se escreve '{numeros[num]}'")
    break