def aumentar(n=0, taxa=0, formato=False):
    """
    -  Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param n: o preço que se quer reajustar
    :param taxa: qual é a porcentagem de aumento
    :param formato: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem formato
    """
    preco = n + (n * (taxa/100))
    return preco if formato is False else moeda(preco)


def diminuir(n=0, taxa=0, formato=False):
    preco = n - (n * (taxa/100))
    return preco if formato is False else moeda(preco)


def dobro(n=0,  formato=False):
    preco = n * 2
    return preco if formato is False else moeda(preco)


def metade(n=0,  formato=False):
    preco = n / 2
    return preco if formato is False else moeda(preco)


def moeda(n=0, moeda='R$'):
    # :.2f coloca duas casas decimais
    return f'{moeda}{n:.2f}'.replace('.', ',')


def resumo(n, taxaA=10, taxaR=5):
    print('-' * 30)
    print('RESUMO DO VALOR'. center(30))
    print('-' * 30)
    print(f'Preço analisado: {moeda(n)}')
    print(f'Dobro do preço: {dobro(n, True)}')
    print(f'{taxaA}% de aumento: {aumentar(n, taxaA, True)}')
    print(f'{taxaR}% de redução: {diminuir(n, taxaR, True)}')
    print('-' * 30)
