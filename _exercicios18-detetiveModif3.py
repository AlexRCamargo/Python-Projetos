# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:  
# a. "Telefonou para a vítima?"  
# b. "Esteve no local do crime?"  
# c. "Mora perto da vítima?"  
# d. "Devia para a vítima?"  
# e. "Já trabalhou com a vítima?"  
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
# Caso contrário, ele será classificado como "Inocente". 

import csv
import os
import matplotlib.pyplot as plt
from colorama import Fore, Style, init

# Inicializa o colorama
init(autoreset=True)

# Define a ordem das classificações
ordem_classificacao = {
    'Assassino': 1,
    'Cúmplice': 2,
    'Suspeito': 3,
    'Inocente': 4
}

# Define cores para as classificações
cores_classificacao = {
    'Assassino': Fore.RED,
    'Cúmplice': Fore.YELLOW,
    'Suspeito': Fore.MAGENTA,
    'Inocente': Fore.GREEN
}

def fazer_perguntas():
    perguntas = [
        'Telefonou para a vítima?',
        'Esteve no local do crime?',
        'Mora perto da vítima?',
        'Devia para a vítima?',
        'Já trabalhou com a vítima?'
    ]

    respostas_positivas = 0
    print('\nResponda às perguntas com "S" para SIM ou "N" para NÃO.')

    for pergunta in perguntas:
        while True:
            resposta = input(f'{pergunta} (S/N): ').strip().lower()
            if resposta in ['s', 'n']:
                if resposta == 's':
                    respostas_positivas += 1
                break
            else:
                print('Resposta inválida. Digite apenas "S" ou "N".')
    
    return respostas_positivas

def classificar(respostas_positivas):
    if respostas_positivas == 2:
        return 'Suspeito'
    elif 3 <= respostas_positivas <= 4:
        return 'Cúmplice'
    elif respostas_positivas == 5:
        return 'Assassino'
    else:
        return 'Inocente'

def salvar_resultados(nome_arquivo, resultados):
    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(['Jogador', 'Classificação'])
        for jogador, classificacao in resultados:
            escritor.writerow([jogador, classificacao])
    print(f'\n📄 Resultados salvos em "{nome_arquivo}".')

def mostrar_ranking(resultados):
    print('\n=== RANKING FINAL ===')
    # Ordena pela severidade da classificação
    resultados_ordenados = sorted(resultados, key=lambda x: ordem_classificacao[x[1]])

    for jogador, classificacao in resultados_ordenados:
        cor = cores_classificacao.get(classificacao, Fore.WHITE)
        print(f'{cor}{jogador}: {classificacao}')

def gerar_grafico(resultados):
    categorias = ['Assassino', 'Cúmplice', 'Suspeito', 'Inocente']
    contagem = {categoria: 0 for categoria in categorias}

    for _, classificacao in resultados:
        if classificacao in contagem:
            contagem[classificacao] += 1

    plt.bar(contagem.keys(), contagem.values(), color=['red', 'yellow', 'magenta', 'green'])
    plt.title('Classificação dos Jogadores')
    plt.xlabel('Classificação')
    plt.ylabel('Quantidade de Jogadores')
    plt.grid(axis='y')
    plt.show()

def main():
    while True:
        resultados = []
        print('\n=== Questionário de Investigação Criminal ===')

        while True:
            jogador = input('\nDigite o nome do jogador (ou "fim" para encerrar): ').strip()
            if jogador.lower() == 'fim':
                break
            respostas_positivas = fazer_perguntas()
            classificacao = classificar(respostas_positivas)
            resultados.append((jogador, classificacao))
            cor = cores_classificacao.get(classificacao, Fore.WHITE)
            print(f'\n{cor}O jogador {jogador} foi classificado como: {classificacao}.')

        if resultados:
            salvar_resultados('resultados_investigacao.csv', resultados)
            mostrar_ranking(resultados)
            gerar_grafico(resultados)
        else:
            print('\nNenhum jogador participou.')

        # Perguntar se o usuário quer repetir o jogo
        repetir = input('\nDeseja realizar outra investigação? (S/N): ').strip().lower()
        if repetir != 's':
            print('\nEncerrando o programa. Obrigado!')
            break

if __name__ == '__main__':
    main()