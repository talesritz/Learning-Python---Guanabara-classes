from uteis import validacao

def aumentar(num):
    tmp = validacao.leiaInt('Quanto iremos aumentar? ')
    return num + tmp

def diminuir(num):
    tmp = validacao.leiaInt('Quanto iremos diminuir? ')
    return num - tmp

def dobro(num):
    return num*2

def metade(num):
    return num/2