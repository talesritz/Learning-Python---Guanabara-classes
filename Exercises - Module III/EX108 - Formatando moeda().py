# Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado.

from uteis import formata, moedab, validacao

#Versão necessária para o ex108
formata.cabecalho('EX108 - Formatando Moeda()')


tmp = validacao.leiaInt('Digite o preço: ')
print(f'A metade de {moedab.moeda(tmp)} é {moedab.moeda(moedab.metade(tmp))}')
print(f'O dobro de {moedab.moeda(tmp)} é {moedab.moeda(moedab.dobro(tmp))}')
print(f'Aumentando 10%, temos {moedab.moeda(moedab.aumentar(tmp))}')
print(f'Diminuindo 15%, temos {moedab.moeda(moedab.diminuir(tmp))}')
