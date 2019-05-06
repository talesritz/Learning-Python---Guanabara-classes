#Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogresult = list()
cadastro = dict()
gols = list()
totgols = 0 

valcont = 's'
while valcont == 's':

  print('='*40)
  print('{:^40}' .format('EX093 - Cadastro Jogador Futebol'))
  print('='*40)
  print('''
  [1] - Cadastrar
  [2] - Resumo Geral
  [3] - Detalhamento Individual
  [4] - Detalhamento Geral
  [5] - Sair
  ''')
  
  opstr = str(input('Escolha uma opção: ')).strip()
  while opstr.isnumeric() == False:
      print('\033[31mOpção Inválida\033[m')
      opstr = str(input('Escolha uma opção: ')).strip()
  print()
  
  opcao = int(opstr)
  
  #[1] - Cadastrar
  if opcao == 1:

    #Valida se o nome contém apenas letras 
    cadastro['nome'] = str(input('Nome: ')).strip()
    while cadastro['nome'].isalpha() == False:
      print('\033[31mNome deve conter apenas letras\033[m')
      cadastro['nome'] = str(input('Nome: ')).strip()
  
    #Valida se a quantidade de jogos é positiva
    cadastro['qtdejogos'] = int(input('Quantidade de Jogos: '))
    while cadastro['qtdejogos'] <= 0:
      print('\033[31minformação Inválida\033[m')
      cadastro['qtdejogos'] = int(input('Quantidade de Jogos: '))
    
    #Se não houver jogos, a quantidade de gols é imediatamente 0.
    if cadastro['qtdejogos'] == 0:
      cadastro['totgols'] = 0
    
    #Se houver jogos, pergunta quantos gols ocorreram em cada partida e efetua a soma total dos gols para cada jogador.
    else:
      for count in range(0, cadastro['qtdejogos']):
        golpartida = int(input(f'Gols partida {count+1}: '))
        gols.append(golpartida)
        totgols += golpartida

      cadastro['totgols'] = totgols
      cadastro['golspartida'] = gols.copy()  

    #Adiciona o cadastro atual na lista de jogadores
    jogresult.append(cadastro.copy())
    totgols = 0
    gols.clear()
    
    print()
  
  #[2] - Resumo Geral
  elif opcao == 2:

    if len(jogresult) == 0:
      print('\033[33mNÃO HÁ REGISTROS\033[m')
      print()
    else:
      for k, v in enumerate(jogresult):
        print('\033[31m{:-^25}\033[m' .format(f' Jogador {k+1} '))
        print(f'\033[37mJogador:\033[m {v["nome"]}')
        print(f'\033[37mTotal de Gols:\033[m {v["totgols"]}')
        print()

  #[3] - Detalhamento individual      
  elif opcao == 3:  
    
    if len(jogresult) == 0:
      print('033[33mNÃO HÁ REGISTROS')
      print()
    else:
      for k, v in enumerate(jogresult):
        print(f'\033[32m[{k+1}]\033[m {v["nome"]}')
      print()
      
      option = str(input('Escolha o jogador: ')).strip()
      while option.isnumeric() == False:
        print('\033[31mEscolha utilizando os números de referência')
        option = str(input('Escolha o jogador: ')).strip() 
      opnum = int(option) 
      print()
              
      print(f'\033[37mJogador:\033[m {jogresult[opnum-1]["nome"]}')
      print(f'\033[37mTotal de Gols:\033[m {jogresult[opnum-1]["totgols"]}')
      print('\033[31m{:-^25}' .format('\033[31m Jogos '))
      print('\033[m', end='')
      for count in range(0, len(jogresult[opnum-1]["golspartida"])):
        print(f'\033[37mJogo {count+1}:\033[m {jogresult[opnum-1]["golspartida"][count]}')
    
      print()
     
  #[4] - Detalhamento Geral
  elif opcao == 4:
    
    if len(jogresult) == 0:
      print('\033[33mNÃO HÁ REGISTROS\033[m')
      print()
    else:
      #Cabeçalho
      print('\033[33m{:-^40}' .format(' Detalhamento Geral '))
      print('\033[m', end='')
      print('-'*40)
      print('{:<10}' .format('NOME'), end='')
      print('{:^20}' .format('GOLS PARTIDA'), end='')
      print('{:>10}' .format('TOTAL'))
      print('-'*40)

      for k, v in enumerate(jogresult):
        print('{:<10}' .format(f'{jogresult[k]["nome"]}'), end='')
        print('{:^20}' .format(f'{jogresult[k]["golspartida"]}'), end='')
        print('{:>8}' .format(f'{jogresult[k]["totgols"]}'))

      print('\n\n')

  #[5] - Sair 
  elif opcao == 5:
    valcont = 'n'
    print()
  
  else:
    print('\033[31mEscolha uma opção de 1 a 4\033[m')
    print()

print()
print('\033[1mSaindo do Programa...\033[m')