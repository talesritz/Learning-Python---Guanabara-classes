#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. se por caso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.



from datetime import datetime, date, timedelta

tmp = dict()
tdate = date.today()
oneYear = timedelta(days=365)
cadastros = list()

valcont = 's'
cont = 1
while valcont == 's':

  print('='*40)
  print('{:^40}' .format('EX092 - Cadastro de Trabalhadores'))
  print('='*40)
  print()
  
  #menu de entrada
  print('''  [1] - Cadastrar
  [2] - Mostrar Cadastros
  [3] - Sair\n''')  
  
  #Valida se a opção está correta e se estiver, converte para Integer
  optionstr = str(input('Escolha uma opção: '))
  while optionstr.isnumeric() == False:
    print('\033[31mOpção Inválida\033[m')
    optionstr = str(input('Escolha uma opção: '))
  print()
  option = int(optionstr)
  
  #[1] - CADASTRAR
  if option == 1:  

    print('{:-^40}' .format(f' cadastro {cont} '))
    print()

    tmp['name'] = str(input('Nome: '))
    bday = str(input('Data de Nascimento: '))
    tmp['bdaydate'] = datetime.strptime(bday, '%d/%m/%Y').date()
    tmp['age'] = tdate.year-tmp['bdaydate'].year
    tmp['ctps'] = int(input('CTPS: '))

    if tmp['ctps'] != 0:
      tmp['hiredate'] = int(input('Ano de contratação: '))
      tmp['wage'] = float(input('Salário: '))
      tmp['retirement'] = tmp['hiredate']+35

    cadastros.append(tmp.copy())
    tmp.clear()
    print()
    cont += 1
  
  #[2] - Mostrar
  elif option == 2:
    if cadastros == []:
      print('\033[33mNão há cadastros registrados\033[m')
      print()
    else:
      for count in range(0, len(cadastros)):

        print('{:-^40}' .format(f' Cadastro {count+1} '))
        print()
        print(f'Nome         :  {cadastros[count]["name"]}')
        print(f'Nascimento   :  {cadastros[count]["bdaydate"].strftime("%d/%m/%Y")}')
        print(f'Idade        :  {cadastros[count]["age"]}')
        
        if cadastros[count]['ctps'] != 0:
          print(f'CTPS         :  {cadastros[count]["ctps"]}')
          print(f'Contratação  :  {cadastros[count]["hiredate"]}') 
          print(f'Salário      :  R$ {cadastros[count]["wage"]:.2f}')
          print(f'Aposentadoria:  {cadastros[count]["retirement"]}')
        print(f'')


      print()

  #[3] - Sair
  elif option == 3:
    valcont = 'n'
    break

  #opção inválida
  else:
    print('\033[31mOpção Inválida\033[m')
    print()

 

print()
print('\033[1mSaindo do Programa...\033[m')
