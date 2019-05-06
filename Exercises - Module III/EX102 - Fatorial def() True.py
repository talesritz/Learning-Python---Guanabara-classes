#Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial. 

def cabecalho(msg):
  print('='*40)
  print('{:^40}' .format(msg))
  print('='*40)
  print()
def fatorial(num, show=False):
  """
  Função Fatorial

  :param num: recebe um número inteiro para efetuar o cálculo de fatorial do mesmo

  :param show: (True) Mostra a conta do fatorial, (False) Apenas mostra o resultado

  :return: retorna o valor int() do cálculo fatorial se for diferente de 0 e 1 (números que não possuem cálculo por si próprios)
  """


  if num == 0:
    return 'Fatorial: 0'
  
  elif num == 1:
    return 'Fatorial: 1'

  else: 

    if show == False:
      fat = 1
      for count in range(num, 1, -1):
        fat *= count
      return (f'Fatorial: {fat}')
    
    else:
      fat = 1
      for count in range(num, 1, -1):
        print(f'{count} x ', end='')
        if count-1 == 1:
          print(f'{count-1}: ', end='')
        fat*= count
      return fat


cabecalho('EX102 - Fatorial def() Opcional')
num = int(input('Digite um número: '))
print(fatorial(num))