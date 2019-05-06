from uteis import validacao

#EX107
def aumentar(num):
    tmp = 1.1
    return num * tmp

def diminuir(num):
    tmp = 0.85
    return num * tmp

def dobro(num):
    return num*2

def metade(num):
    return num/2

#EX108 Formatando moeda()
def moeda(num):
  tmp = f'R${num:.2f}'
  return tmp  


  