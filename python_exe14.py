# DOCSTRING
def contador(i, f, p):
    """
    - Faz uma contagem e mostra na tela
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('Fim!')


help(contador)

# PARÂMETROS OPCIONAIS
"""
def somar(a=0, b=0, c=0):
    somar()

"""


def somar(a, b, c=0):
    s = a+b+c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(8, 4)

# ESCOPO DE VARIÁVEIS


def teste():
    x = 8  # x tem um escopo local, pois foi declarada apenas na função
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


n = 2  # tem escopo global
print(f'No programa principal, n vale {n}')
teste()
# aqui o x dará erro, pois tem escopo local
#print(f'No programa principal, x vale {x}')


def teste(b):
    global a  # para usar o escopo global, usa o valor 5
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5
teste(a)
print(f'A fora vale {a}')  # aqui usa o valor 8

# RETORNANDO VALORES


def somar(a=0, b=0, c=0):
    s = a+b+c
    return s


r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)

print(f'Os resultados foram {r1}, {r2} e {r3}')


# script que tenha uma função chamada voto() que
# vai receber como parâmetro o ano de nascimento de
# uma pessoa, retornando um valor literal indicando
# se uma pessoa tem voto negado, opcional ou obrigatório
# nas eleições


def voto(ano):
    import datetime
    today = datetime.date.today()
    atual = int(today.year)
    idade = atual - ano

    if idade < 16:
        return (f'Com {idade} anos: VOTO NEGADO')
    elif 16 >= idade < 18 or idade > 65:
        return (f'Com {idade} anos: VOTO OPCIONAL')
    else:
        return (f'Com {idade} anos: VOTO OBRIGATÓRIO')


ano = int(input('Em que ano você nasceu? '))
print(voto(ano))


# script que tenha uma função fatorial () que receba
# dois parâmetros: o primeiro que indique o número
# a calcular e o outro chamado show, que será um valor
# lógico (opcional) indicando se será mostrado ou não
# na tela o processo de cálculo do fatorial


def fatorial(n, show=False):
    """
    Calcula o fatorial de um número:
    :param n: O número a ser calculado.
    :param show: (opcional) mostrar ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    fat = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fat *= c
    return fat


print(fatorial(4, True))
# help(fatorial)


# script que tenha uma função chamada ficha() que receba
# dois parâmetros: o nome de um jogador e quantos gols
# ele marcou. O script deverá ser capaz de mostrar a ficha
# do jogador, mesmo que algum dado não tenha sido
# informado corretamente


def ficha(nome='<desconhecido>', gols=0):
    return (f'O jogador {nome} fez {gols} gol(s) no campeonato.')


nome = input('Nome do Jogador: ').capitalize()
gols = input('Número de gols: ')
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':  # strip remove espaços em branco
    print(ficha(gols=gols))
else:
    print(ficha(nome, gols))


# script que tenha a função leiaint() que vai funcionar
# de forma semelhante a função input, só que fazendo
# a validação para aceitar apenas um valor numérico


def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO')
        if ok:
            break
    return valor


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')


# script que tenha uma função notas() que pode receber
# várias notas de alunos e vai retornar um dicionário
# com as seguintes informações:
# quantidade de notas
# a maior nota
# a menor nota
# a média da turma
# a situação (opcional)
# adicione também os docstrings da função

notas_alunos = []
dic_notas = {}


def notas(notas_alunos, sit=False):
    """
    Informações de notas de alunos:
    :param notas_alunos: lista com a nota dos alunos.
    :param sit: (opcional) mostrar ou não a situação do aluno.
    :return: sem retorno.
    """
    while True:
        n = int(input('Digite uma nota: '))
        notas_alunos.append(n)
        dic_notas['total'] = len(notas_alunos)
        dic_notas['maior'] = max(notas_alunos)
        dic_notas['menor'] = min(notas_alunos)
        dic_notas['média'] = round(sum(notas_alunos) / len(notas_alunos), 2)
        if sit:
            if dic_notas['média'] >= 7:
                dic_notas['situação'] = 'BOA'
            elif dic_notas['média'] > 6 and dic_notas['média'] < 7:
                dic_notas['situação'] = 'RAZOÁVEL'
            elif dic_notas['média'] < 7:
                dic_notas['situação'] = 'RUIM'
        pergunta = ' '
        while pergunta not in 'SsNn':
            pergunta = input('Deseja continuar? (S/N) ').strip().upper()[0]
            continue
        if pergunta in 'Nn':
            break
    print(dic_notas)


notas(notas_alunos, sit=True)
help(notas)
