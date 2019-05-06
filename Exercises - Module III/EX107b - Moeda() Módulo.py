# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro(), e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções

from uteis import formata, moedab, validacao

#Versão necessária para o ex108
formata.cabecalho('EX107b - Moeda() Módulo')


tmp = validacao.leiaInt('Digite o preço: ')
print(f'A metade de R${tmp} é {moedab.metade(tmp)}')
print(f'O dobro de {tmp} é {moedab.dobro(tmp)}')
print(f'Aumentando 10%, temos {moedab.aumentar(tmp)}')
print(f'Diminuindo 15%, temos {moedab.diminuir(tmp)}')