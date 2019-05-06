def leiaInt(msg):
    tmp = str(input(msg))
    while tmp.isnumeric() == False:
        print('\033[31mOpção inválida\033[m')
        tmp = str(input(msg))

    return int(tmp)


