import urllib.request


try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero.')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados.')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre!')

# reescreva a função leiaInt() que tenha a possibilidade da digitação
# de um número do tipo inválido. Crie também a funçâo leiaFloat()


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número inteiro válido.')
        except (KeyboardInterrupt):
            print('O usuário preferiu não informar os dados.')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número inteiro válido.')
        except (KeyboardInterrupt):
            print('O usuário preferiu não informar os dados.')
            return 0
        else:
            return n


num = leiaInt('Digite um Inteiro: ')
num2 = leiaFloat('Digite um Float: ')
print(f'O valor inteiro digitado foi {num} e o Floar foi {num2}.')


# script que testa se o site Pudim está acessível pelo computador

try:
    site = urllib.request.urlopen('https://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim não está acessível no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso.')
