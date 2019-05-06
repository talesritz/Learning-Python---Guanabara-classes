def cabecalho(msg):
    print(cores['anil'], end='')
    print('=' * 40)
    print(cores['laranja'], end='')
    print('{:^40}' .format(msg))
    print(cores['anil'], end='')
    print('=' * 40)
    print(cores['limpacor'])


def sair():
    print('\n\033[1mSaindo do programa...\033[m')


cores = {
    'branco': '\033[30m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'laranja': '\033[33m',
    'azul': '\033[34m',
    'roxo': '\033[35m',
    'anil': '\033[36m',
    'cinza': '\033[37m',
    'limpacor': '\033[m'
}
