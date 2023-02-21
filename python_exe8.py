from random import randint

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}.')

# script que leia vários números inteiros pelo teclado
# O scrpt só irá ºarar quando o usuário digitar o valor 999
# No final mostre quantos números foram digitados e qual foi
# a soma entre eles

n = soma = count = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    soma += n
    count += 1
print(f'A soma dos {count} números é {soma}.')


# script que mostre a tabuada de vários
# números. O script será interrompido quando
# o número solicitado for negativo

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
print('Tabuada encerrada!')


# script que jogue par ou ímpar com o computador.
# O jogo será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele
# conquistou no final do jogo

print('-' * 20)
print('Jogo de par ou ímpar')
print('-' * 20)

soma = count = 0

while True:
    computador = (randint(0, 10))
    jogador = int(input('Digite um número de 0 a 10: '))
    soma = computador + jogador
    escolha = ' '
    while escolha not in 'PI':
        escolha = input('Par ou ímpar (P/I)? ').strip().upper()[0]
    print(
        f'Jogador jogou {jogador} e o computador {computador}. Total foi {soma}.', end='')
    print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
    if soma % 2 == 0:
        if escolha == 'P':
            print('Jogador VENCEU!')
            count += 1
        else:
            print('Jogador PERDEU!')
            break
    elif soma % 2 == 1:
        if escolha == 'I':
            print('Jogador VENCEU!')
            count += 1
        else:
            print('Jogador PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {count} vezes.')


# script que leia a idade e o sexo de várias pessoas
# A cada pessoa cadastrada o script deverá perguntar se
# o usuário quer ou não continuar. No final, mostre:
# quantas pessoas tem mais de 18 anos
# quantos homens foram cadastrados
# quntas mulheres tem menos de 20 anos

count = masc = fem = 0

while True:
    print('-' * 20)
    print('Cadastre uma pessoa:')
    print('-' * 20)
    idade = int(input('Qual a sua idade? '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Qual seu sexo (M/F)? ').strip().upper()[0]

    if idade >= 18:
        count += 1
    if sexo == 'M':
        masc += 1
    if sexo == 'F' and idade < 20:
        fem += 1

    escolha = ' '
    while escolha not in 'SN':
        escolha = input('Deseja continuar (S/N)? ').strip().upper()[0]
    if escolha == 'N':
        print('-' * 10)
        print('Fim do programa!')
        print('-' * 10)
        break
print(f'Temos cadastradas {count} pessoas com mais de 18 anos.')
print(f'Temos cadastrados {masc} homens.')
print(f'Temos cadastradas {fem} mulheres com menos de 20 anos.')


# script que leia o nome e o preço de
# vários produtos. O script deverá perguntar
# se o usuário vai continuar. No final, mostre:
# Qual o total gasto na compra
# Quantos produtos custam mais de 1000 reais
# Qual o nome do produto mais barato

soma = count = prod = menor = 0
barato = ' '
print('-' * 20)
print('SACOLÃO DA RACHEL')
print('-' * 20)

while True:
    nome = input('Nome do produto: ')
    valor = float(input('Valor do produto: R$ '))
    soma += valor
    prod = valor

    if valor > 1000:
        count += 1
    if prod == 1 or valor < menor:
        menor = valor
        barato = nome

    escolha = ' '
    while escolha not in 'SN':
        escolha = input('Deseja continuar (S/N)? ').strip().upper()[0]
    if escolha == 'N':
        print('Fim!')
        break
print(f'O valor gasto na compra foi de {soma} reais.')
print(f'Temos no total {count} produtos que custam mais de  R$ 1000.')
print(f'O nome do produto mais barato é {barato} e custa {menor}.')
