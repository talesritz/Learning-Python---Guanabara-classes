#Escreva um programa que leia um valor em metros e o exiba convertido em centímeros e milímetros. 

from time import sleep

medida = float(input('Digite a medida em metros: '))

print('--- AGUARDE - Convertendo valores ---')
sleep(1)
print('centímetros: {:.0f}' .format(medida*100))
print('milímetros: {:.0f}' .format(medida*1000))