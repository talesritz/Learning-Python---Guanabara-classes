#Faça um programa que leia um ano qualquer e mostre se ele é Bissexto. 

print('-=-'*7)
print('EX032 - Ano Bissexto')
print('-=-'*7)
print('\n')

ano = int(input('Digite um ano: '))

# --- Validação ---
#quatro = ano%4
#qtcentos = ano%400
#cem = ano%100
#print(quatro, qtcentos, cem)


if ano%4==0 and ano%100!=0 or ano%400==0:
  print('O ano {} é bissexto' .format(ano))
else:
  print('O ano {} não é bissexto' .format(ano))
