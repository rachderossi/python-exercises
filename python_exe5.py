import math
import datetime

nome = str(input('Qual o seu nome? ')).capitalize()

if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'João':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claudia Raquel Bruna':
    print('Belo nome feminino.')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia, {nome}!')

# script para aprovar empréstimo bancário na compra de uma casa
# valor da casa, salário, quantos anos vai pagar
# calcular valor da prestação mensal (não pode exceder 30% do salário)
# caso contrátrio o empréstimo será negado

print('-<' * 20)
print('Calculadora de empréstimo bancário')
print('-<' * 20)

casa = float(input('Qual o valor do imóvel? '))
salario = float(input('Qual o seu salário? '))
anos = int(input('Pretende pagar em quantos anos? '))

prest = salario * (30/100)
mensal = round(casa / (anos*12), 2)

if mensal < prest:
    print(
        f'O valor da prestação mensal será de {mensal} reais a ser pago em {anos} anos.')
else:
    print('Seu empréstimo foi negado.')


# script que leia um número inteiro e peça para o usuário escolher a base de conversão
# 1 para binário
# 2 para octal
# 3 para hexadecimal

num = int(input('Escreva um número: '))
escolha = int(input(('Escolha a base de conversão: \n'
                     '1' + ' ' + 'binário \n'
                     '2' + ' ' + 'octal \n'
                     '3' + ' ' + 'hexadecimal \n')))

if escolha == 1:
    print(f'{num} convertido para binário é igual a {bin(num)[2:]}.')
elif escolha == 2:
    print(f'{num} convertido para octal é igual a {oct(num)[2:]}.')
elif escolha == 3:
    print(f'{num} convertido para hexadecimal é igual a {hex(num)[2:]}.')
else:
    print('Você não escolheu nenhuma opção.')
print('Até logo!')


# script que leia dois números inteiros e compare-os mostrando:
# o primeiro valor e maior ou o segundo valor é maior
# ou não existe valor maior, os dois são iguais

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

if num1 > num2:
    print('O primeiro valor é maior.')
elif num1 < num2:
    print('O segundo valor é maior.')
else:
    print('Não existe valor maior, os dois são iguais.')


# script qie leia o ano de nascimento de um jovem e informa de acordo com a idade:
# se ele ainda vai se alistar ao serviço militar
# se é a hora de se alistar
# se já passou do tempo de alistamento
# mostrar o tempo que falta ou que já passou do prazo

today = datetime.date.today()
year = int(today.year)
ano = int(input('Qual seu ano de nascimento? '))

idade = year - ano

if idade == 18:
    print('É hora de se alistar!')
elif idade < 18:
    falta = 18 - idade
    print('Você ainda irá se alistar.')
    print(f'Faltam exatamente {falta} anos para o seu alistamento.')
else:
    passou = idade - 18
    print('Já passou do tempo de alistamento!')
    print(f'Se passaram {passou} anos do seu alistamento.')


# script que leia duas notas de um aluno e calcule a sua média
# mostrando uma mensagem no final de acordo com a média atingida
# média abaixo de 5.0: reprovado
# média entre 5.0 e 6.9: recuperação
# média 7 ou superio: aprovado

nota1 = float(input('Digite uma nota: '))
nota2 = float(input('Digite outra nota: '))

media = (nota1+nota2) / 2

if media >= 7.0:
    print(f'Aprovado! A sua média foi {media}.')
elif media >= 5.0 and media <= 6.9:
    print(f'Recuperação! A sua média foi {media}.')
else:
    print(F'Reprovado! A sua média foi {media}.')


# script que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade:
# até 9 anos: mirim
# até 14 anos: infantil
# até 19 anos: junior
# até 20 nos: sênior
# acima: master

today = datetime.date.today()
year = int(today.year)
ano = int(input('Qual seu ano de nascimento? '))

idade = year - ano

if idade <= 9:
    print(f'Categoria: Mirim, sua idade é {idade}.')
elif idade > 9 and idade <= 14:
    print(f'Categoria: Infantil, sua idade é {idade}.')
elif idade > 14 and idade <= 19:
    print(f'Categoria: Junior, sua idade é {idade}.')
elif idade > 19 and idade <= 20:
    print(f'Categoria: Senior, sua idade é {idade}.')
else:
    print(f'Categoria: Master, sua idade é {idade}.')


# refaça o desafio dos triângulos acrescentando o tipo de triângulo
# equilátero : todos os lados iguais
# escaleno: todos os lados diferentes
# isósceles: dois lados iguais

print('-=' * 20)
print("Analisador de triângulos")
print('-=' * 20)

reta1 = float(input("Comprimento da reta 1: "))
reta2 = float(input("Comprimento da reta 2: "))
reta3 = float(input("Comprimento da reta 3: "))

triangulo = math.fmod(reta2, reta3)  # módulo

if triangulo < reta1 < reta2 + reta3 and reta1 == reta2 == reta3:
    print("As retas formam um triângulo!")
    print('O triângulo é do tipo Equilátero, tem todos os lados iguais.')
elif triangulo < reta1 < reta2 + reta3 and reta1 != reta2 != reta3:
    print("As retas formam um triângulo!")
    print('O triângulo é do tipo Escaleno, tem todos os lados diferentes.')
elif triangulo < reta1 < reta2 + reta3 and reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
    print("As retas formam um triângulo!")
    print('O triângulo é do tipo Isósceles, tem dois lados iguais.')
else:
    print("Desculpe, as retas não formam um triângulo!")


# script que calcule o imc (peso e altura)
# e mostre o status de acordo com a tabela abaixo:
# abaixo de 18.5: abaixo do peso
# entre 18.5 e 25: peso ideal
# 25 até 30: sobrepeso
# acima de 40: obesidade mórbida

print('-<' * 20)
print('Calculadora de IMC')
print('-<' * 20)

peso = float(input('Qual o seu peso (kg)? '))
altura = float(input('Qual a sua altura (m)? '))

imc = round(peso / (altura*2), 2)

if imc < 18.5:
    print(f'Abaixo do peso, seu imc é de {imc}.')
elif imc >= 18.5 and imc < 25:
    print(f'Peso ideal, seu imc é de {imc}.')
elif imc >= 25 and imc < 30:
    print(f'Sobrepeso, seu imc é de {imc}.')
else:
    print(f'Obesidade mórbida, seu imc é de {imc}.')


# script que calcula o valor a ser pago por um produto
# considerando o seu preço normal e a condição de pagamento
# a vista dinheiro ou cheque: 10% de desconto
# a vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

valor = float(input('Insira o valor do produto: '))
pagamento = int(input('Opções de pagamento: \n'
                      '1.' + ' ' + 'À vista no dinheiro ou cheque:' +
                      ' ' + '10%' + ' ' 'de desconto. \n'
                      '2.' + ' ' + 'À vista no cartão:' + ' ' + '5%' + ' ' 'de desconto. \n'
                      '3.' + ' ' + 'Em até 2x no cartão:' + ' ' + 'preço normal. \n'
                      '4.' + ' ' + '3x ou mais no cartão:' + ' ' + '20%' + ' ' 'de juros. \n'))

if pagamento == 1:
    desc = valor * (10/100)
    calc = valor - desc
    print(f'O valor a ser pago será de {calc} reais.')
elif pagamento == 2:
    desc = valor * (5/100)
    calc = valor - desc
    print(f'O valor a ser pago será de {calc} reais.')
elif pagamento == 3:
    print(f'O valor a ser pago será de {valor} reais.')
else:
    juros = valor * (20/100)
    calc = valor + juros
    print(f'O valor a ser pago será de {calc} reais.')
