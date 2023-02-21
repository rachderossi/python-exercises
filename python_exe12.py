# DICIONÁRIOS
"""
lanche = {}  # isso é um dicionário
"""

import datetime
from operator import itemgetter
from time import sleep
from random import randint

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 23}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas.keys():
    print(k)

for k, v in pessoas.items():
    print(f'{k} = {v}')

"""
del(pessoas['sexo'])
pessoas['nome'] = 'Joca'
"""
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(brasil[0])
print(brasil[0]['uf'])

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do estado: ')
    brasil.append(estado.copy())  # copy() no lugar de [:]
# print(brasil)
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')

for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()

# script que leia um nome e média de um aluno, guardando também
# a situação em um dicionário. No final, mostre o conteúdo na tela
# media > 7 aprovado

aluno = {}

aluno['nome'] = input('Nome: ').capitalize()
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'

print('-' * 10)
for k, v in aluno.items():
    print(f'- {k} é igual a {v}.')


# script onde 4 jogadores joguem um dado e tenham resultados aleatórios
# guarde esses resultados em um dicionário. No final, coloque esse
# dicionário em ordem, sabendo que o vencedor tirou o maior
# número no dado

print('Valores sorteados:')
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = dict()
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
# print(ranking)
print('=-' * 15)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'  {i+1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)


# script que leia nome, ano de nascimento e carteira de trabalho
# e cadastre-os com a idade em um dicionário se por acaso a CTPS
# for diferente de zero o dicionário receberá também o ano de
# contratação e o salário. Calcule e acrescente além da idade com
# quantos anos a pessoa vai se aposentar

funcionario = {}
today = datetime.date.today()
ano = int(today.year)

funcionario['nome'] = input('Nome: ').capitalize()
nascimento = int(input('Ano de Nascimento: '))
funcionario['idade'] = ano - nascimento
funcionario['ctps'] = input('Carteira de trabalho (0 não tem): ')
if funcionario['ctps'] != '0':
    funcionario['contrato'] = int(input('Ano de contratação: '))
    funcionario['salario'] = float(input('Salário: '))
    funcionario['aposentadoria'] = (
        funcionario['idade'] + funcionario['contrato'] + 35 - ano)
for k, v in funcionario.items():
    print(f'- {k} tem o valor {v}')


# script que gerencie o aproveitamento de um jogador de futebol.
# o script vai ler o nome do jogador e quantas partidas ele jogou
# depois vai ler a quantidade de gols feitos em cada partida.
# No final tudo isso será guardado em um dicionário, incluindo
# o total de gols feitos durante o campeonato

jogador = {}
gols = []

jogador['nome'] = input('Nome do jogador: ').capitalize()
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for j in range(0, partidas):
    num = int(input(f'Quantos gols na partida {j+1}? '))
    gols.append(num)
    jogador['gols'] = gols
jogador['total'] = sum(jogador['gols'])
print('=-' * 30)
print(jogador)
print('=-' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=-' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'  - Na partida {i+1}, fez {v} gols.')
print(F'Foi um total de {jogador["total"]} gols.')


# script que leia nome, sexo e idade de várias pessoas guardando
# os dados de cada pessoa em um dicionário e todos os dicionários
# em uma lista. No final mostre:
# quantas pessoas foram cadastradas
# a média da idade do grupo
# uma lista com todas as mulheres
# uma lista com todas as pessoas com idade acima da média

pessoa = {}
galera = []
soma = 0

while True:
    pessoa.clear()  # apaga a pessoa antiga
    pessoa['nome'] = input('Nome: ')
    sexo = input('Sexo [M/F]: ').strip().upper()[0]
    while sexo not in 'MF':
        print('ERRO!')
        sexo = input('Sexo [M/F]: ').strip().upper()[0]
    pessoa['sexo'] = sexo
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())  # adicona a pessoa
    continuar = input('Deseja continuar [S/N]? ').strip().upper()[0]
    if continuar not in 'SN':
        print('Erro!')
        continuar = input('Deseja continuar [S/N]? ').strip().upper()[0]
        continue
    if continuar in 'Nn':
        break
print(galera)
print('-=' * 15)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'A média de idade é de {media:5.2f} anos.')
print(f'As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'F':
        print(f'{p["nome"]} ', end='')
print(f'\nA lista das pessoas com idade acima da média:', end='')
for p in galera:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'{k} = {v}: ', end='')
        print()
print('Fim!')
