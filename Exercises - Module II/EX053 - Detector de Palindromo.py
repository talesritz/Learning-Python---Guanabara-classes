#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços

print('\033[34m-=-'*10)
print('\033[33mEX053 - Detector de Palíndromo')
print('\033[34m-=-\033[m'*10)
print('\n')

#Metodo String (simples)
frase = str(input('Digite uma frase: '))
frasejoin = ''.join(frase.split())
#fraseinvsimples = frasejoin[::-1]
fraseinvcomp = ''

for index in range(len(frasejoin)-1, -1, -1):
  fraseinvcomp+=frasejoin[index]
 
print('\n')
if frasejoin.lower()==fraseinvcomp.lower():
   print('O inverso de {} é {}.\n A frase digitada é um palíndromo' .format(frasejoin.upper(), fraseinv.upper()))
else:
  print('O inverso de {} é {}.\n A frase digitada \033[1;31mNÃO\033[m é um palíndromo' .format(frasejoin.upper(), fraseinvcomp.upper()))

'''if frasejoin.lower()==fraseinvsimples.lower():
   print('O inverso de {} é {}.\n A frase digitada é um palíndromo' .format(frasejoin.upper(), fraseinv.upper()))
else:
  print('O inverso de {} é {}.\n A frase digitada \033[1;31mNÃO\033[m é um palíndromo' .format(frasejoin.upper(), fraseinvsimples.upper()))'''