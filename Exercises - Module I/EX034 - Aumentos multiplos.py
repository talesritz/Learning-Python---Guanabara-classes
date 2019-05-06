#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para saários superiores a 1250, calcule um aumento de 10%, para os inferiores ou iguais a 1250, o aumento é de 15%. 

print('-=-'*9)
print('EX034 - Aumentos Múltiplos')
print('-=-'*9)
print('\n')

sal = float(input('Digite seu salário para saber quanto será seu aumento: '))

if sal<=1250 and sal>0:
  print('Seu aumento será de {:.2f} reais, totalizando um salário final de {:.2f} reais no fim do mês. ' .format(sal*0.15, sal*1.15))
else:
  if sal>1250:
    print('Seu aumento será de {:.2f} reais, totalizando um salário final de {:.2f} reais no fim do mês.' .format(sal*0.1, sal*1.1))
  else:
    print('Digite um salário válido!')