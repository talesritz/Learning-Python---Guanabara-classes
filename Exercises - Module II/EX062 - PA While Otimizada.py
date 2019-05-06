#Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos. 

print('\033[34m-=-'*9)
print('\033[33mEX061 - PA While Otimizada')
print('\033[34m-=-\033[m'*9)
print('\n')

primt = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
print('\n')
enesimo = 1

termos = 10
vezes=-1
while vezes!=0:
  while enesimo <= termos:
    print(primt+(enesimo-1)*razao, end=' ')
    enesimo+=1
  
  print('\n')
  vezes= int(input('Quer continuar? Quantos termos? :  '))
  print('\n') 
  termos = termos+vezes

print('\nSaindo...')
