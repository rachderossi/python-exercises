import math
from time import sleep
from random import randint

nome = str(input("Qual o seu nome? ")).strip().capitalize()
if nome == 'Raquel':
    print("Que nome lindo você tem!")
else:
    print("Seu nome é bem comum.")
print(f"Bom dia, {nome}!")

# script de um número entre 0 e 5 e tentar descobrir qual foi o número escolhido.
# escrever na tela se o usuário venceu ou perdeu

computador = randint(0, 5)
print("-=-" * 20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-=-" * 20)

jogador = int(input("Em que número eu pensei? "))
print("PROCESSANDO...")
sleep(3)

if jogador == computador:
    print("Parabéns! Você conseguiu me vencer!")
else:
    print(f"Você perdeu! Eu pensei no número {computador} e não no {jogador}.")


# script que leia a velocidade de um carro, se estiver a mais de 80 km/h foi multado.
# a multa custa 7 reias por cada km acima do limite

velocidade = float(input("Velocidade do carro (km/h): "))
multa = (velocidade - 80) * 7

if velocidade > 80:
    print("Você foi multado!")
    print(f"Você tem que pagar um total de {multa} reais.")
else:
    print("Pode seguir viagem!")
print("Tenha um bom dia! Dirija com segurança!")


# script que leia um número inteiro e diga se ele é par ou ímpar

num = int(input("Digite um número: "))

if num % 2 == 0:  # num % 2 == 1 é impar
    print(f"O número {num} é par.")
else:
    print(f"O número {num} é ímpar.")


# script que pergunte a distância de uma viagem em km
# calcule o preço da passagem cobrando 0,50 cents por km por viagens de até 200 km
# e 0,45 cents por km para viagens mais longas

distancia = float(input("Qual a distância da sua viagem? "))
curta = distancia * 0.50
longa = distancia * 0.45

if distancia <= 200:
    print(f"A sua viagem é curta, o preço da passagem será {curta} reais.")
else:
    print(f"A sua viagem é longa, o preço da passagem será {longa} reais.")


# script que leia um ano qualquer e mostre se ele é bissexto

ano = int(input("Diga um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print("Esse ano é bissexto!")
else:
    print("Esse ano não é bissexto!")


# script que leia três números e mostre qual é o maior e qual é o menor

a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))
c = int(input("Terceiro número: "))

# Verificando quem é o menor
menor = a

if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print(f"O menor número é {menor}")

# Verificando quem é o maior
maior = a

if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f"O maior número é {maior}")


# script que pergunte o salário de um funcionário e calcule seu aumento
# se salário for maior que 1250 reais o aumento é de 10%
# para inferiores ou iguais o aumento é de 15%

salario = float(input("Qual seu salário? "))

if salario > 1250:
    novo = salario + (salario * 10 / 100)
else:
    novo = salario + (salario * 15 / 100)
print(f"Quem ganhava R${salario} passará a ganhar R${novo}.")


# script que leia o comprimento de trÊs retas e diga se elas formam ou não um triângulo

print('-=' * 20)
print("Analisador de triângulos")
print('-=' * 20)

reta1 = float(input("Comprimento da reta 1: "))
reta2 = float(input("Comprimento da reta 2: "))
reta3 = float(input("Comprimento da reta 3: "))

triangulo = math.fmod(reta2, reta3)  # módulo

if triangulo < reta1 < reta2 + reta3:
    print("As retas formam um triângulo!")
else:
    print("Desculpe, as retas não formam um triângulo!")
