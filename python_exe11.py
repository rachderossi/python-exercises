from random import randint

teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])  # [:] faz uma cópia
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

galera = [['João', 19], ['Ana', 33], ['Maria', 45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')

pessoas = list()
dado = list()
for c in range(0, 3):
    dado.append(input('Nome: '))
    dado.append(int(input('Idade:')))
    pessoas.append(dado[:])
    dado.clear()
print(pessoas)

# script que leia o nome e o peso de várias pessoas
# guardando tudo em uma lista. No final, mostre:
# quantas pessoas foram cadastradas
# uma listagem com as pessoas mais pesadas
# uma listagem com as pessoas mais leves

pessoas = list()
dados = list()
maior = menor = 0
while True:
    dados.append(input('Qual o seu nome? '))
    dados.append(float(input('Qual o seu peso? ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    pergunta = ' '
    while pergunta not in 'SsNn':
        pergunta = input('Deseja continuar (S/N)? ').strip().upper()[0]
        continue
    if pergunta in 'Nn':
        break
print('-' * 30)
print(f'Você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior} Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print(f'\nO menor peso foi de {menor} Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')


# script onde o usuário possa digitar sete valores numéricos
# e cadastre-os em uma lista única que mantenha separados os
# valores pares e ímpares. No final, mostre os valores pares
# e ímpares em ordem crescente

lista = [[], []]
for i in range(0, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()
print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores ímpares digitados foram: {lista[1]}')


# script que crie uma matriz 3x3 e preencha com valores lidos
# pelo teclado, no final mostre a matriz na tela com a formatação
# correta

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        # :^5 fica 5 espaços centralizados
        print(f'[{matriz[l][c]:^5}]', end='')
    print()  # quebra a linha


# com o desafio anterior faça:
# a soma de todos os valores pares digitados
# a soma dos valores da terceira coluna
# o maior valor da segunda linha

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = maior = soma_col = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        # :^5 fica 5 espaços centralizados
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            soma_par += matriz[l][c]
    print()  # quebra a linha
print(f'A soma de de todos os valores pares: {soma_par}')
for l in range(0, 3):
    soma_col += matriz[l][2]
print(f'A soma dos valores da terceira coluna: {soma_col}')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha: {maior}')


# script que ajude um jogador da mega sena a criar palpites.
# O script vai perguntar quantos jogos serão gerados e vai sortear
# 6 números entre 1 e 60 para cada jogo. Cadastrando tudo em
# uma lista composta

lista = list()
sorteio = list()

print('-' * 40)
print('\tNÚMEROS PARA A MEGA SENA')
print('-' * 40)
jogo = int(input('Quantos jogos você quer que eu sorteie? '))

total = 1
while total <= jogo:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    sorteio.append(lista[:])
    lista.clear()
    total += 1

print('-=' * 5 + ' ' + f'SORTEANDO {jogo} JOGOS' + ' ' + '-=' * 5)

for i, l in enumerate(sorteio):
    print(f'Jogo {i+1}: {l}')

print('-=' * 6 + ' ' + '< BOA SORTE! >' + ' ' + '-=' * 6)


# script que leia nome e duas notas de vários alunos e guarde tudo
# em uma lista composta. No final mostre um boletim contendo a
# média de cada um e permita que o usuário possa mostrar as notas
# de cada aluno individualmente

pessoas = list()

while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    pessoas.append([nome, [nota1, nota2], media])

    pergunta = ' '
    while pergunta not in 'SsNn':
        pergunta = input('Quer continuar (S/N)? ').strip().upper()[0]
        continue
    if pergunta in 'Nn':
        break
print('-' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA:":>8}')
print('-' * 30)
for i, a in enumerate(pessoas):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 encerrar) '))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(pessoas) - 1:
        print(f'Notas de {pessoas[opc][0]} são {pessoas[opc][1]}')
print('Até logo!')
