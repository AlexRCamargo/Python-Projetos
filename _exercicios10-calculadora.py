OPERACOES = {
    'Soma': lambda n1, n2: n1 + n2,                                     # Função Lambda são funções que não possuem nome e devem ser criadas e usadas no mesmo momento. 
    'Subtração': lambda n1, n2: n1 - n2,
    'Multiplicação': lambda n1, n2: n1 * n2,
    'Divisão': lambda n1, n2: n1 / n2,
    'potência': lambda n1, n2: n1 ** n2,
}
nome_operacao = lambda operacao: list(OPERACOES.keys())[operacao - 1]   # São funções que não possuem nome e devem ser criadas e usadas no mesmo momento. 
lista_operacoes = list(OPERACOES.keys())                                # retornar uma lista com todas as chaves do dicionário
total_operacoes = len(OPERACOES) + 1                                    # Função len indica quantos elementos tem dentro da lista


def mensagem_operacoes():
    print('Operações:')
    for i, j in enumerate(lista_operacoes):
        print(f' ({i + 1}) {j.title()}')
    print('')


def operacao_valida(operacao):
    return operacao in range(1, total_operacoes)


def efetua_operacao(operacao, numero1, numero2):
    calculo = OPERACOES.get(nome_operacao(operacao))
    return calculo(numero1, numero2)


def get_operacao_usuario():
    return int(input('Informe qual operação gostaria de realizar: '))


if __name__ == '__main__':
    mensagem_operacoes()
    operacao = get_operacao_usuario()

    while not operacao_valida(operacao):
        print('Operação inválida!!!')
        operacao = get_operacao_usuario()

    print(f'({nome_operacao(operacao).upper()})')
    numero1 = int(input('Informe o primeiro número: '))
    numero2 = int(input('Informe o segundo número: '))
    resultado = efetua_operacao(operacao, numero1, numero2)
    print(f'O resultado da {nome_operacao(operacao)} é {resultado}.')