# AS LISTAS SÃO MUTÁVEIS
"""
lanche = []  # isso é uma lista
"""

num = [2, 5, 9, 1]
num[2] = 3  # mudar valor
num.append(7)
num.sort()  # ordenar
num.sort(reverse=True)  # ordenar ao contrário
num.insert(2, 0)  # inserir o 0 na posição 2
num.pop()  # elimina o último elemento
num.remove(2)  # remove a primeira ocorrência do valor
print(num)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4.')

valores = []
# valores.append(5)
# valores.append(9)
# valores.append(4)

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):  # enumerate info chave e valor
    print(f'Na posição {c} encontrei {v}!')
print('Cheguei no final da lista.')

a = [2, 3, 4, 7]
b = a[:]  # faz uma cópia de a dentro de b
b[2] = 8
print(f'A lista A: {a}')
print(f'A lsita B: {b}')

# script que leia 5 valores numéricos e guarde em uma lista
# no final mostre qual foi o maior e o menor valor digitado
# e as suas respectivas posições na lista

lista = []
maior = menor = 0
for n in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
    if n == 0:
        maior = menor = lista[n]
    else:
        if lista[n] > maior:
            maior = lista[n]
        if lista[n] < menor:
            menor = lista[n]
print(f'Você digitou os valores: {lista}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for c, v in enumerate(lista):
    if v == maior:
        print(f'{c}...', end='')
print(f'\nO menor valor digitado foi {menor} nas posiçôes ', end='')
for c, v in enumerate(lista):
    if v == menor:
        print(f'{c}...', end='')


# script onde o usuário possa digitar vários valores numéricos
# e cadastre-os em uma lista. Caso o número já exista na lista
# ele não será adicionado. No final, serão exibidos todos os
# valores únicos digitados em ordem crescente

lista = []

while True:
    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
    else:
        print('Valor duplicado! Não será adicionado')
    pergunta = ' '
    while pergunta not in 'SsNn':
        pergunta = input('Deseja continuar (S/N)? ').strip().upper()[0]
        continue
    if pergunta in 'Nn':
        break
lista.sort()
print(f'Você digitou os valores: {lista}')


# script onde o usuário possa digitar cinco valores numéricos
# e cadastre-os em uma lista, já na posição correta da inserção
# (sem usar o sort()). No final mostre a lista ordenada

lista = []
for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print(f'Os valores digitados foram: {lista}')


# script que leia vários números e coloque em uma lista
# depois disso mostre:
# quantos números foram digitados
# lista de valores ordenado de forma decrescente
# se o valor 5 foi digitado e está ou não na lista

lista = []
count = 0
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    count += 1
    pergunta = ' '
    while pergunta not in 'SsNn':
        pergunta = input('Deseja continuar (S/N)? ').strip().upper()[0]
        continue
    if pergunta in 'Nn':
        break
print(lista)
print(f'Foram digitados {count} números.')
lista.sort(reverse=True)
print(f'Valores ordenados de forma decrescente: {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')


# script que vai ler vários números e colocar em uma lista
# depois disso crie duas listas extras que vão contar apenas
# os valores pares e os valores ímpares digitados. No final
# mostre o conteúdo das 3 listas geradas

lista = []
lista2 = []
lista3 = []

while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        lista2.append(n)
    else:
        lista3.append(n)
    pergunta = ' '
    while pergunta not in 'SsNn':
        pergunta = input('Deseja continuar (S/N)? ').strip().upper()[0]
        continue
    if pergunta in 'Nn':
        break

print(f'A lista completa: {lista}')
print(f'Os valores pares são: {lista2}')
print(f'Os valores impares são: {lista3}')


# script onde o usuário digite uma expressão qualquer que use
# parênteses. Seu script deverá analisar se a expressão
# passada está com parênteses abertos e fechados na ordem correta

expr = str(input('Digite a expressão: '))
lista = []
for simbolo in expr:
    if simbolo == '(':
        lista.append('(')
    elif simbolo == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
