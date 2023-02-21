nome = str(input("qual o seu nome? "))
idade = int(input('qual a sua idade? '))
peso = float(input('qual o seu peso? '))

print(nome, idade, peso)

# script em python que leia o nome de uma pessoa e
# mostre uma mensagem de boas vindas

nome = str(input('qual o seu nome? '))

print('Olá' + ' ' + nome + '!' + ' ' + 'Prazer em te conhecer.')
print('Olá, {}' .format(nome) + '!' + ' ' + 'Prazer em te conhecer.')


# script que leia o dia, mês e ano de nascimento de uma pessoa
# e mostre a mensagem na data formatada

dia = str(input('dia:'))
mes = str(input('mes:'))
ano = str(input('ano:'))

print('Você nasceu no dia' + ' ' + dia + ' ' + 'de' + ' ' +
      mes + ' ' + 'de' + ' ' + ano + '.' + ' ' + 'Correto?')


# script que leia dois numeros e mostre a soma entre eles

primeiro_numero = int(input('Primeiro número: '))
segundo_numero = int(input('Segundo número: '))
soma = primeiro_numero + segundo_numero

print('Soma:' + ' ' + str(soma))
print('A soma entre {} e {} vale {}'.format(
    primeiro_numero, segundo_numero, soma))
