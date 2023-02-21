import datetime
from time import sleep

for c in range(0, 6):
    print('Oi')
print('Fim')

for c in range(6, 0, -1):
    print(c)
print('Fim')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print(f'O somatório de todos os valores foi {s}.')

# script que mostre na tela uma contagem regressiva
# para o estouro de fogos de artificio indo de 10 até
# 0, com uma pausa de 1 segundo entre eles

print('<-' * 10)
print('Contagem regressiva para o Ano Novo')
print('<-' * 10)

for c in range(1, 11):
    print(c)
    sleep(1)
print('Feliz Ano Novo!!')


# script que mostre na tela todos os números pares
# que estão no intervalo entre 1 e 50

for c in range(1, 51):
    if c % 2 == 0:
        print(c, end=' ')


for c in range(2, 51, 2):  # ocupa menos memória
    print(c, end=' ')


# script que calcula a soma entre todos os números
# impares que são múltiplos de três e que se
# encontram no intervalo de 1 até 500

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print(f'A soma dos {cont} números é: {soma}')


# script que faça uma tabuada de um número que
# # o usuário escolher

print('<-' * 10)
print('Tabuada Multiplicação')
print('<-' * 10)
num = int(input('Digite um número: '))
for c in range(1, 11):
    print(f'{num} * {c} = {num * c}')


# script que leia seis números inteiros e mostre a
# soma apenas daqueles que foram pares. Se o valor
# digitado for ímpar desconsidere-o

soma = 0

for c in range(1, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0 and not (num % 2 != 0):
        soma += num
print(f'A soma desses valores é de: {soma}')


# script que leia o primeiro termo e a razão de
# uma PA. No final mostre os 10 primeiros termos
# dessa progresssão

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao

for c in range(primeiro, decimo + razao, razao):
    print(c, end=' > ')
print('Fim')


# script que leia um núemero inteiro e diga se ele
# é ou não um número primo

num = int(input('Digite um número: '))
for c in range(1, num+1):
    if num % c == 0:
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')
    print(c, end=' ')


# script que leia uma frase qualquer e diga se ela
# é um palindromo. Desconsiderando os espaços

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()  # separa numa lista
junto = ''.join(palavras)  # elimina espaços internos
inverso = ''

# ultima letra, letra antes da primeira (primeira é zero), e volta uma letra
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palíndromo.')
else:
    print('Não é um palíndromo.')


# script que leia o ano de nascimento de sete pessoas
# No fnal mostre quantas pessoas ainda não atingiram
# a maioridade e quantas já são maiores

today = datetime.date.today()
year = today.year

maior = 0
menor = 0

for c in range(1, 8):
    num = int(input('Digite o ano do seu nascimento: '))
    idade = year - num
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('Maior de idade:', maior)
print('Menor de idade:', menor)


# script que leia o peso de cinco pessoas e no final
# mostre qual foi o maior e o menor peso lidos

maior = 0
menor = 0

for c in range(1, 6):
    peso = float(input('Digite seu peso: '))
    if peso > maior:
        maior = peso
    else:
        menor = peso
print(f'Maior peso: {maior} Kg')
print(f'Menor peso: {menor} Kg')


# script que leia o nome, idade e sexo de 4 pessoas
# No final mostre:
# a média da idade do grupo
# qual o nome do homem mais velho
# quantas mulheres tem menos de 20 anos

soma_idade = 0
maior = 0
nome_velho = 0
mulher20 = 0

for p in range(1, 5):
    nome = str(input('Qual seu nome? ')).capitalize()
    idade = int(input('Qual a sua idade? '))
    sexo = int(input('Qual o seu sexo: \n'
                     '1' + ' ' + 'feminino \n'
                     '2' + ' ' + 'masculino \n '))

    soma_idade += idade
    media_idade = round(soma_idade / p, 2)

    if p == 1 and sexo == 2:
        maior = idade
        nome_velho = nome
    if sexo == 2 and idade > maior:
        maior = idade
        nome_velho = nome
    if sexo == 1 and idade < 20:
        mulher20 += 1

print(f'A média da idade do grupo é de: {media_idade}')
print(f'O nome do homem mais velho é: {nome_velho}')
print(f'No total temos {mulher20} mulheres com menos de 20 anos.')
