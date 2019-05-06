#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente. 


nome = ''
notaA = 0
notaB = 0
cadastro = list() #armazena os dados do cadastro
alunos = list() #arquiva todos os cadastro em uma única lista composta

opcao = 0
valmenu = 's'
while valmenu == 's':
  print('\n')
  print('='*40)
  print('{:^40}' .format('EX089 - Boletim Alunos')) 
  print('='*40)
  print('''
  [1] - Cadastrar aluno
  [2] - Mostrar média dos alunos
  [3] - Ver notas de um aluno específico
  [4] - Sair
  ''')

  opcaostr = input('Digite uma opção: ')
  while opcaostr.isnumeric()==False:
    print('\033[31mOpção inválida\033[m')
    opcaostr = input('Digite uma opção: ')
  print('\n')

  opcao = int(opcaostr)

  #[1] - Cadastrar aluno
  if opcao == 1:
    print('\033[34m='*40)
    print('{:^40}' .format('\033[33m[1] - Cadastro de Alunos'))
    print('\033[34m=\033[m'*40)
    #contador para o cabeçalho
    cont = 0
    #validador while
    valcont = 's'
    while valcont == 's':
      print('{:-^40}' .format(f' Aluno {cont+1} '))
      
      #leitor NOME, validação
      valnome = 's'
      while valnome == 's':
        nome = str(input('Nome: '))
        
        if nome.isalpha():
          cadastro.append(nome)
          valnome = 'n'
        else:
          print('\033[31mNome deve conter apenas letras\033[m')
      
      #leitor NOTA A, validação
      valnota = 's'
      while valnota == 's':
        notaA = input('Nota A: ')
        
        if notaA.isnumeric():
          cadastro.append(float(notaA))
          valnota = 'n'
        else:
          print('\033[31mNota deve conter apenas números\033[m')

      #leitor NOTA B, validação
      valnota = 's'
      while valnota == 's':
        notaB = input('Nota B: ')
        
        if notaB.isnumeric():
          cadastro.append(float(notaB))
          valnota = 'n'
        else:
          print('\033[31mNota deve conter apenas números\033[m')  

      alunos.append(cadastro[:])
      cadastro.clear()
      #teste
      #print(alunos)

      while valcont == 's':
        continuar = input('Deseja continuar [S/N]? ')
        
        if continuar.lower()[0] == 'n':
          valcont = 'n'
          break

        elif continuar.lower()[0] == 's':
          break
        else:
          print('\033[31mOpção Inválida\033[m')

      
      cont += 1
      print('\n')
  
  #[2] - Mostrar média dos alunos
  elif opcao == 2:
    print('\033[34m='*40)
    print('{:^40}' .format('\033[33m[2] - Mostrar média dos alunos'))
    print('\033[34m=\033[m'*40)

    if alunos == []:
      print('\033[31;1m\nNão há dados a serem exibidos\n\033[m')
    else:    
      for count in range(0, len(alunos)):
        print('{:<10} ' .format(f'{alunos[count][0]}: '), end='' )
        print(f'{(alunos[count][1]+alunos[count][2])/2}')
  
  #[3] - nota de Aluno específico
  elif opcao == 3: 
    print('\033[34m='*40)
    print('{:^40}' .format('\033[33m[3] - Nota de aluno específico'))
    print('\033[34m=\033[m'*40)

    if alunos == []:
      print('\033[31;1m\nNão há dados a serem exibidos\n\033[m')
    else:
      for count in range(0, len(alunos)):
        print(f'[ {count+1} ] - {alunos[count][0]}')
      
      alEscolhido = input('Selecione o aluno: ')
      print('\n')
      print(f'{alunos[int(alEscolhido)-1][0]}')
      print(f'Nota A: {alunos[int(alEscolhido)-1][1]}')
      print(f'Nota B: {alunos[int(alEscolhido)-1][2]}')

  #[4] - Sair
  elif opcao == 4:
    valmenu = 'n'
    print('\n')
    break    
  
  #Qualquer outra opção
  else:
    print('\033[31;1m\nOpção Inválida\033[m')

print('\033[1mSaindo do Programa\033[m...')