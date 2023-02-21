# A IDEIA É SEPARAR AS FUNCIONALIDADES DO SCRIPT
# EM UM OUTRO ARQUIVO, NESSE EXEMPLO: 'uteis.py'
from moeda import resumo
import moeda
from moeda import aumentar, diminuir, dobro, metade, moeda
from uteis import fatorial, dobro
import uteis

num = int(input('Digite um valor: '))
fat = uteis.fatorial(num)
print(f'O fatorial de {num} é {fat}.')

"""
OUTRA OPÇÃO
"""
num = int(input('Digite um valor: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat} e o dobro é {dobro(num)}.')


# crie um módulo chamado moeda.py que tenhas as funções
# incorporadas aumentar(), diminuir(), dobra() e metade()
# faça também um script que importe esse módulo e use
# algumas funções

n = float(input('Digite o preço: R$ '))
aumentar = aumentar(n)
diminuir = diminuir(n)
dobro = dobro(n)
metade = metade(n)
print(f'Aumentando 10%, temos R$ {aumentar}')
print(f'Diminuindo 10%, temos R$ {diminuir}')
print(f'O dobro de {n} é R$ {dobro}')
print(f'A metade de {n} é R$ {metade}')


# adapte o script do desafio anterior e crie uma função
# adicional chamada moeda() que consiga mostrar os valores
# como um valor monetário formatado


n = float(input('Digite o preço: R$ '))
print(
    f'Aumentando {moeda.aumentar(50)}%, temos {moeda.moeda(moeda.aumentar(n,50))}')
print(
    f'Diminuindo {moeda.diminuir(20)}%, temos {moeda.moeda(moeda.diminuir(n,20))}')
print(f'O dobro de {moeda.moeda(n)} é {moeda.moeda(moeda.dobro(n))}')
print(f'A metade de {moeda.moeda(n)} é {moeda.moeda(moeda.metade(n))}')


# adicione ao módulo moeda.py uma função resumo() que mostre
# na tela algumas informações geradas pelas funções que já
# temos no módulo criado até aqui

n = float(input('Digite o preço: R$ '))
resumo(n, 80, 35)
