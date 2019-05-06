'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados
de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
a)Quantas pessoas cadastradas
b)A média de idade.
c)Uma lista com mulheres
d)uma lista com idade acima da média
'''

cadastro = dict()
listcad = list()
mediaidade = 0
valcont = 's'
while valcont == 's':

    print('='*40)
    print('{:^40}' .format('EX094 - Dicionários em Listas'))
    print('='*40)
    print('''
    [1] - Cadastrar
    [2] - Quantas pessoas cadastradas
    [3] - Média de Idade
    [4] - Lista com mulheres
    [5] - Pessoas acima da média de idade
    [6] - Sair
    ''')

    entry = str(input('Escolha uma opção: '))
    while entry.isnumeric() == False:
        print('\033[31mOpção Inválida\033[m')
        entry = str(input('Escolha uma opção: '))
    opcao = int(entry)
    print()

    #[1] - CADASTRAR
    if opcao == 1:

        cadastro['nome'] = str(input('Nome: '))
        while cadastro['nome'].isalpha() == False:
            print('\033[31mApenas Letras\033[m')
            cadastro['nome'] = str(input('Nome: '))

        cadastro['sexo'] = str(input('Sexo [M/F]: ')).lower()
        while cadastro['sexo'] not in 'mf':
            print('\033[31mDigite \033[36mM \033[31mpara Masculino ou \033[36mF \033[31mpara Feminino\033[m')
            cadastro['sexo'] = str(input('Sexo: ')).lower()

        cadastro['idade'] = int(input('Idade: '))
        while cadastro ['idade'] <= 0:
            print('\033[31mIdade inválida\033[m')
            cadastro['idade'] = int(input('Idade: '))

        listcad.append(cadastro.copy())
        print()

    #[2] - QTDE PESSOAS CADASTRADAS
    elif opcao == 2:

        if len(listcad) == 0:
            print('\033[31mNÃO HÁ REGISTROS\033[m')
        elif len(listcad) == 1:
            print('\033[33m Apenas 1 cadastro ativo\033[m')
        else:
            print(f'\033[33m{len(listcad)} pessoas cadastradas\033[m')

        print()

    #[3] - MÉDIA DE IDADE
    elif opcao == 3:
      soma = 0
      media = 0

      if len(listcad) == 0:
          print('\033[31mNÃO HÁ REGISTROS\033[m')
      else:
          for count in range(0, len(listcad)):
              soma += listcad[count]['idade']

          media = soma/len(listcad)
          print(f'\033[33mMédia de Idade: {media:.0f}\033[m')

      print()

    #[4] - LISTA COM MULHERES
    elif opcao == 4:
      mulheres = list()

      for count in range(0, len(listcad)):
          if listcad[count]['sexo'] == 'f':
            mulheres.append(listcad[count].copy())

      if len(mulheres) == 0:
          print('\033[31mNÃO HÁ REGISTROS\033[m')
      else:
          for count in range(0, len(mulheres)):
              print(f'\033[33m{mulheres[count]["nome"]:<10}: {mulheres[count]["idade"]} anos\033[m')

      print()

    #[5] - Pessoas acima da média de idade
    elif opcao == 5:
        soma = 0
        media = 0

        if len(listcad) == 0:
            print('\033[31mNÃO HÁ REGISTROS\033[m')
        else:
            for count in range(0, len(listcad)):
                soma += listcad[count]['idade']

            media = soma / len(listcad)

            for count in range(0, len(listcad)):
                if listcad[count]['idade'] >= media:
                    print(f'\033[33m{listcad[count]["nome"]:<10}: {listcad[count]["idade"]} anos\033[m')

        print()


    elif opcao == 6:
        valcont = 'n'
        print()
        break

    else:
        print('\033[31mOpção Inválida\033[m')
        print()


print('\033[1mSaindo do Programa...\033[m')
