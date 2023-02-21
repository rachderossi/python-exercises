from random import randint
from time import sleep


def soma(a, b):
    s = a+b
    print(s)


soma(4, 5)
soma(2, 3)
soma(7, 9)


def contador(*num):  # *num parâmetros empacotados
    print(num)


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 8, 2)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

# script que tenha uma função chamada área()
# que receba as dimennsões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno


def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {a}m2.')


# Programa Principal
print('Controle de Terrenos')
print('-' * 20)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)


# script que tenha uma função chamada escreva(), que
# receba um texto qualquer como parâmetro e mostre uma
# mensagem com tamanho adaptável

def escreva(texto):
    tam = len(texto) + 4
    print('-' * tam)
    print(f'  {texto}')
    print('-' * tam)


# Programa Principal
escreva('Raquel Rossi')
escreva('Curso em Python')
escreva('Oi')


# script que tenha uma função chamada contador() que
# receba três parâmetros: início, fim e passo e
# realize a contagem.
# A) de 1 até 10, de 1 em 1
# B) de 10 até 0, de 2 em 2
# c) Uma contagem personalizada

def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1  # deixa o passo positivo
    if passo == 0:
        passo = 1

    print('-=' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            # flush mostra o número pausadamente
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += passo
        print('FIM!')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= passo
        print('FIM!')
        print('-=' * 20)


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem! ')
inicio = int(input('Ínicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)


# script que tenha uma função chamada maior(), que
# receba vários parâmetros com valores inteiros.
# script tem que analisar todos os valores e dizer
# qual é o maior

def maior(* num):
    cont = maior = 0
    print('-=' * 25)
    print('Analisando os valores passados... ')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


maior(2, 9, 4, 5, 6)
maior(4, 7, 0)
maior(1, 3)
maior(0)
maior()


# scrpt que tenha uma lista chamada números e duas
# funções chamadas sorteia() e somaPar(). A primeira
# função vai sortear 5 números e vai colocá-los
# dentro da lista e a segunda função vai mostrar a
# soma entre todos os valores PARES sorteados pela
# função anterior.


numeros = []


def sorteia(numeros):
    print('Sorteando 5 valores da lista: ', end='')
    for n in range(0, 5):
        n = randint(1, 10)
        numeros.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.5)
    print('PRONTO!')


def somaPar(numeros):
    soma = 0
    for valor in numeros:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {numeros}, temos {soma}.')


sorteia(numeros)
somaPar(numeros)
