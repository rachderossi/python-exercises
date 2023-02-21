# script para jogar pedra, papel ou tesoura

from random import randint
from time import sleep

itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)

print('Suas opções: \n'
      '0' + ' ' + 'pedra \n'
      '1' + ' ' + 'papel \n'
      '2' + ' ' + 'tesoura \n')

jogador = int(input("Qual sua jogada? "))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
print('<-' * 11)
print(f"Computador jogou {itens[computador]}")
print(f"Jogador jogou {itens[jogador]}")
print('<-' * 11)

if computador == 0:  # computador joga pedra
    if jogador == 0:
        print('Empate!')
    elif jogador == 1:
        print('Jogador vence!')
    elif jogador == 2:
        print('Computador vence!')
    else:
        print('Jogada Inválida!')
if computador == 1:  # computador joga papel
    if jogador == 0:
        print('Computador vence!')
    elif jogador == 1:
        print('Empate!')
    elif jogador == 2:
        print('Jogador vence!')
    else:
        print('Jogada Inválida!')
if computador == 2:  # computador joga tesoura
    if jogador == 0:
        print('Jogador vence!')
    elif jogador == 1:
        print('Computador vence!')
    elif jogador == 2:
        print('Empate!')
    else:
        print('Jogada Inválida!')
