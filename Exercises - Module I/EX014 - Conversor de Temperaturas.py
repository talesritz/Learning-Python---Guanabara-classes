#Escreva um programa que converta uma temperatura digitada em °C e converta para °F

print('-=-'*8)
print('Conversor de Temperaturas')
print('-=-'*8)
print('\n')

tempc = float(input('Digite a temperatura em °C: '))
print('{:.1f}°C equivalem a {:.1f}°F' .format(tempc, (tempc*9/5)+32 ))