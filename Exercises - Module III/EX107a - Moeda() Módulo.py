# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro(), e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções

from uteis import moedaa, formata, validacao
from time import sleep

format.cabecalho('EX107 - moeda() Módulos')


coin = 0
while True:

    print('''
    [1] Aumentar
    [2] Diminuir
    [3] Dobro
    [4] Metade
    [5] Sair
    ''', end = '')

    opcao = validacao.leiaInt('Escolha uma opção: ')

    if opcao == 1:
        coin = moeda.aumentar(coin)

    elif opcao == 2:
        coin = moeda.diminuir(coin)

    elif opcao == 3:
        coin = moeda.dobro(coin)

    elif opcao == 4:
        coin = moeda.metade(coin)

    elif opcao == 5:
        formata.sair()
        sleep(1)
        break

    else:
        print(formata.cores['vermelho'], end = '')
        print('    Opção Inválida')
        print(formata.cores['limpacor'], end = '')


    print(f'AGORA TEMOS {coin:.1f} MOEDAS!')
