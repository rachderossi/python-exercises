# SE EU SEI O LIMITE: FOR OU WHILE
# SE EU NÃO SEI O LIMITE: WHILE
from time import sleep
from random import randint

c = 1
while c < 10:
    print(c)
    c = c + 1
print('Fim')

n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')

# script que leia o sexo de uma pessoa, mas só aceita os valores 'M' ou 'F'
# caso esteja errado peça a digitação novamente até ter um valor correto

sexo = input('Insira seu sexo (M ou F): ').strip().upper()[0]

while sexo not in 'MF':
    sexo = input(
        'Dados inválidos! Insira seu sexo (M ou F): ').strip().upper()[0]
print(f'Seu sexo é {sexo}')


# melhorar o script de adivinhar número
# o computador vai pensar num número de 0 a 10
# o jogador vai tentar adivinhar até acertar, mostrando no final quantos
# palpites foram necessários para vencer

computador = randint(0, 10)

print('Olá! Eu sou o computador e estou pensando num número de 0 a 10, tente adivinhar!')
sleep(3)

acertou = False
count = 0
while not acertou:
    jogador = int(input('Qual foi o número que o computador escolheu? '))
    count += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente novamente.')
        else:
            print('Menos... Tente novamente.')
print(f'Acertou! o computador escolheu o número {computador}.')
print(f'Foram necessários {count} palpites até o acerto.')


# script que leia dois valores e mostre um menu na tela:
# script deverá realizar a operação indicada em cada caso
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa

num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))

option = 0
while option != 5:
    print('Menu de operações: \n'
          '1.' + '' + 'somar \n'
          '2.' + '' + 'multiplicar \n'
          '3.' + '' + 'maior \n'
          '4.' + '' + 'novos números \n'
          '5.' + '' + 'sair do programa \n')
    option = int(input('Qual a sua escolha? '))

    if option == 1:
        soma = num1 + num2
        print(f'A soma dos dois valores é {soma}.')
    elif option == 2:
        mult = num1 * num2
        print(f'A multiplicação dos dois núneros é igual a {mult}.')
    elif option == 3:
        maior = num1
        if num1 > num2:
            print(f'O maior número é {maior}.')
        else:
            print(f'O maior número é o {num2}.')
    elif option == 4:
        print('Insira os números novamente.')
        num1 = int(input('Digite um valor: '))
        num2 = int(input('Digite outro valor: '))
    elif option == 5:
        print(f'Você saiu do programa.')
    else:
        print('Opção inválida!')
print('Fim!')


# script que leia um número e mostre o seu fatorial (com while e for)

n = int(input('Digite um número para calcular o fatorial: '))

c = n
fat = 1
print(f'Calculando {n}! = ', end='')  # esse end deixa tudo na mesma linha

while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    fat *= c
    c -= 1
print(f'{fat}')


# script que leia um número n inteiro e mostre na tela os n primeiros
# elementos de uma sequencia de fibonacci

print('-' * 10)
print('Fibonacci')
print('-' * 10)

n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('-' * 10)

print(f'{t1} → {t2}', end='')
cont = 3  # já temos o primeiro termo e o segundo por isso começamos a contar no 3
while cont <= n:
    t3 = t1 + t2
    print(f' → {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' → FIM!')


# script que leia vários números inteiros. O script irá parar quando o
# usuário digitar o valor 999. No final, mostre quantos números foram
# digitados e qual foi a soma entre eles
# desconsiderando o flag

num = count = soma = 0
num = int(input('Digite um número (999 para sair): '))

while num != 999:
    count += 1
    soma = soma + num
    num = int(input('Digite um número (999 para sair): '))

print(f'Foram digitados no total {count} números.')
print(f'A soma entre os números foi de {soma}.')


# script que leia vários números inteiros pelo teclado. No final da
# execução mostre a média entre todos os valores e qual foi o maior e
# o menor valor lido. O script deve perguntar ao usuário se ele quer ou
# não continuar a digitar valores

soma = count = media = maior = menor = 0
user = 'S'

while user in 'S':
    num = int(input('Digite um número: '))
    soma += num
    count += 1
    if count == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < maior:
            menor = num
    user = input('Deseja continuar (Sim ou Não)? ').strip().upper()[0]
media = round((soma / count), 2)

print(f'A média de todos os números foi de {media}.')
print(f'O maior número é o {maior} e o menor é o {menor}.')
