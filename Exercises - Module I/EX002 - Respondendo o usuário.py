#Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas. 

cores = {
  'branco': '\033[m',
  'vermelho': '\033[31m',
  'verde': '\033[32m',
  'amarelho': '\033[33m',
  'anil': '\033[34m',
  'roxo': '\033[35m',
  'azul': '\033[36m',
  'cinza':'\033[37m',
  'limpa': '\033[m'
}

nome = str(input('Digite seu nome: '))
print('Selecione uma cor para seu nome: ')
print('1. branco')
print('2. vermelho')
print('3. verde')
print('4. amarelo')
print('5. anil')
print('6. roxo')
print('7. azul')
print('8. cinza')
cor = str(input('Qual cor: '))

#print('Seja bem vindo {}{}{}!!!' .format(cores['vermelho'],nome, cores['limpa']))

if cor.lower()=='1':
  print('Seja bem vindo, {}{}{}!!!' .format(cores['branco'], nome, cores['limpa']))
else:
  if cor.lower()=='2':
    print('Seja bem vindo, {}{}{}!!!' .format(cores['vermelho'], nome, cores['limpa']))
  else:
    if cor.lower()=='3':
      print('Seja bem vindo, {}{}{}!!!' .format(cores['verde'], nome, cores['limpa']))
    else:
      if cor.lower()=='4':
        print('Seja bem vindo, {}{}{}!!!' .format(cores['amarelo'], nome, cores['limpa']))
      else:
        if cor.lower()=='5':
          print('Seja bem vindo, {}{}{}!!!' .format(cores['anil'], nome, cores['limpa'])) 
        else:
          if cor.lower()=='6':
            print('Seja bem vindo, {}{}{}!!!' .format(cores['roxo'], nome, cores['limpa']))
          else:
            if cor.lower()=='7':
              print('Seja bem vindo, {}{}{}!!!' .format(cores['azul'], nome, cores['limpa']))
            else:
              if cor.lower()=='8':
                print('Seja bem vindo, {}{}{}!!!' .format(cores['cinza'], nome, cores['limpa']))
              else:
                print('Digite uma cor válida!')