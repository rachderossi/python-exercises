frase = "Curso em video"

print(frase[:12])

print("""Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it to make a type specimen book""")

# script em python que lê o nome completo de uma pessoa

nome = str(input("Qual o seu nome completo? ")).strip()

print(f"Seu nome me maiúsculo é {nome.upper()}")
print(f"Seu nome me minúsculo é {nome.lower()}")

dividido = nome.split()
print(f"Seu primeiro nome tem {len(dividido[0])} letras")
print(f"Seu nome completo tem {len(nome) - nome.count(' ')} letras")


# scriipt em python que separa os dígitos

numero = int(input("Digite um número: "))

u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print(f"unidade: {u}")
print(f"dezena: {d}")
print(f"centena: {c}")
print(f"milhar: {m}")


# script que leio o nome de uma cidade e diga se começa ou não com o nome SANTO

cidade = str(input("Nome da cidade: ")).strip()
cidade = cidade.upper()
primeiro_nome = cidade.split()

if primeiro_nome[0] == "SANTO":
    print("O nome começa com SANTO")
else:
    print("O nome não começa com SANTO")


# script que leia uma frase

frase = str(input("Digite a frase: ")).strip()
frase = frase.upper()

print(f"A letra 'A' aparece {frase.count('A')} vezes")
print(f"Posição da letra 'A' pela primeira vez: {frase.find('A')}")
print(f"Posição da letra 'A'pela última vez: {frase.rfind('A')}")


# script que leia o nome completo de uma pessoa e separe as strings

nome_completo = str(input("Nome completo: ")).strip()
nome = nome_completo.split()

print(f"Primeiro nome: {nome[0]}")
print(f"Último nome: {nome[-1]}")
