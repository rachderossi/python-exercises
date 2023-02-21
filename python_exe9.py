# AS TUPLAS SÃO IMUTÁVEIS
"""
lanche = ()  # isso é uma tupla
"""

from random import randint
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print(lanche[1])
print(lanche[-1])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-3:])

"""
# TypeError: 'tuple' object does not support item assignment
lanche[1] = 'Refrigerante' 
"""
for comida in lanche:
    print(f'Eu vou comer {comida}.')
print('Comi pra caramba!')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}.')
print('Comi pra caramba!')

print(sorted(lanche))  # em ordem alfabética (print uma lista)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(len(c))
print(c.count(5))  # num 5 aparece 2 vezes
print(c.index(8))  # posição do número
print(c.index(2, 1))  # onde esta o num 2 a partir da posição 1

# podemos ter dados de tipos diferentes em tuplas
pessoa = ('Gustavo', 39, 'M', 89.2)
"""
# NameError: name 'pessoa' is not defined
del (pessoa)
print(pessoa) # não é possível fazer print de algo que foi deletado
"""

# script que tenha uma tupla totalmente preenchida com uma
# contagem por extenso de zero até dez.
# o script deverá ler um número pelo teclado entre 0 e 10 e
# mostrá-lo por extenso

num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
       'seis', 'sete', 'oito', 'nove', 'dez')

while True:
    n = int(input('Digite um número entre 0 e 10: '))
    if 0 <= n <= 10:
        break
    print('Tente novamente... ', end='')
print(f'Você digitou o número {num[n]}.')


# crie uma tupla preenchida com os 20 primeiros colocados da
# tabela do brasileirão na ordem de colocaçâo. Depois mostre:
# apenas os 5 primeiros colocados
# os últimos 4 colocados na tabela
# uma lista com os times em ordem alfabética
# em que posição na tabela está o time da Corinthians

times = ('Palmeiras', 'Internacional', 'Flamengo', 'Fluminense', 'Corinthians', 'Athletico-PR', 'Atlético-MG',
         'América-MG', 'Fortaleza', 'Botafogo', 'Santos', 'São Paulo', 'Bragantino', 'Goiás', 'Coritiba', 'Ceará',
         'Cuiabá', 'Atlético-GO', 'Avaí', 'Juventude')

print(f'Os cinco primeiros colocados são: {times[0:5]}')
print('>-' * 40)
print(f'Os últimos quatro colocados na tabela são {times[-4:]}')
print('>-' * 40)
print(f'Lista em ordem alfabética: {sorted(times)}')
print('>-' * 40)
print(
    f'Em que posição da tabela está o time do Corinthians: {times.index("Corinthians")+1} posição.')


# script que vai gerar 5 números aleatórios e colocar em uma tupla
# depois disso, mostre a listagem de números gerados e também
# indique o menor e o maior valor que estão na tupla


tupla = ((randint(1, 10)), (randint(1, 10)),
         (randint(1, 10)), (randint(1, 10)), (randint(1, 10)))

print('Os valores sorteados foram: ', end='')
for n in tupla:
    print(f'{n} ', end='')
print(f'\nO maior valor da lista é: {max(tupla)}.')
print(f'O menor valor da lista é: {min(tupla)}.')


# script que leia 4 valores pelo teclado e guarde-os em uma tupla
# No final, mostre:
# quantas vezes apareceu o valor 9
# em que posição foi digitado o primeiro valor 3
# quais foram os números pares

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
n4 = int(input('Digite um número: '))

nums = (n1, n2, n3, n4)

print(f'O número 9 apareceu: {nums.count(9)} vezes.')
if 3 in nums:
    print(f'O valor 3 apareceu: {nums.index(3)+1} posição.')
else:
    print('O valor 3 não foi digitado.')
print('Os valores pares digitados foram: ', end='')
for n in nums:
    if n % 2 == 0:
        print(n, end=' ')


# script que tenha uma tupla única com nomes de produtos e seus
# respectivos preços na sequência. No final, mostre uma listagem
# de preços organizando os dados em forma tabular

escola = ('Lápis', 1.75,
          'Borracha', 2.00,
          'Caderno', 15.90,
          'Estojo', 25.00,
          'Compasso', 9.99,
          'Mochila', 120.45,
          'Canetas', 22.30,
          'Livro', 34.90)

print('-' * 40)
print('\tLISTAGEM DE PREÇOS')
print('-' * 40)
for pos in range(0, len(escola)):
    if pos % 2 == 0:
        print(f'{escola[pos]:.<30}', end='')
    else:
        # 2f são para mostrar duas casas decimais
        print(f'R${escola[pos]:>7.2f}')
print('-' * 40)


# script que tenha uma tupla com várias palavras (não usar acentos)
# depois disso mostrar para cada palavra quais são as suas vogais

palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
            'mercado', 'programador', 'futuro')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
