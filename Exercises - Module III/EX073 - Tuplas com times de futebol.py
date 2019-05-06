#Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) APenas os 5 primeiros colocados.
#b) Os últimos 4 colocados
#c) Uma lista com os times em ordem alfebetica
#D) em que posição na tabela está o time chapecoense.

print('\033[34m-=-'*9)
print('\033[33m EX073 - Tuplas com Times')
print('\033[34m-=-\033[m'*9)
print('\n')

tabfut = ('Flamengo', 'São Paulo', 'Palmeiras', 'Corinthians', 'Ceará', 'Internacional', 'Grêmio', 'Bahia', 'Atlético-MG', 'Vasco', 'Fluminense', 'Cruzeiro', 'Botafogo', 'Sport', 'Santos', 'Atlético-PR', 'Chapecoense', 'Vitória', 'Paraná', 'América-MG')
#newtabfut = ''

while True:

  print('''BRASILEIRÃO
  [1] - 5 primeiros colocados
  [2] - 4 últimos colocados
  [3] - Times no campeonato
  [4] - Posição do seu time
  [5] - Sair   
 ''' )
  opcao = int(input('Digite uma opção: '))
  a =''
  if opcao == 1:
    for count in range(0, 5):
      print(f'{count+1}º - {tabfut[count]}')
    print('\n')

  elif opcao == 2:
    for count in range (-1, -5, -1):
      print(f'{len(tabfut)+1+count}º - {tabfut[count]}')
    print('\n')
    
  elif opcao == 3:
    newtabfut = sorted(tabfut)
    for count in range(0, len(newtabfut)):
      print(f'- {newtabfut[count]}')
    print('\n')

  elif opcao == 4:
    
    valtime = 'n'
    while valtime == 'n':
      seutime = str(input('Seu time: ')).strip()
      if seutime in tabfut:
        for count in range(0, len(tabfut)):
          if seutime.lower() == tabfut[count].lower():
            print(f'{seutime} está na {count+1}ª posição.')
            print('\n')
            valtime = 's'
      else:
        print('\033[31mTime não está na lista\033[m')

  elif opcao == 5:
    break
  else:
    print('\033[31mOpção inválida\033[m')
    print('\n')


print('\033[1mSaindo do programa...\033[m')