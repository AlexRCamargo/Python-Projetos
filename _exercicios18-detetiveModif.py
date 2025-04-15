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
    for jogador, classificacao in resultados:
        print(f'{jogador}: {classificacao}')

def main():
    resultados = []
    print('=== Questionário de Investigação Criminal ===')

    while True:
        jogador = input('\nDigite o nome do jogador (ou "fim" para encerrar): ').strip()
        if jogador.lower() == 'fim':
            break
        respostas_positivas = fazer_perguntas()
        classificacao = classificar(respostas_positivas)
        resultados.append((jogador, classificacao))
        print(f'\nO jogador {jogador} foi classificado como: {classificacao}.')

    if resultados:
        salvar_resultados('resultados_investigacao.csv', resultados)
        mostrar_ranking(resultados)
    else:
        print('\nNenhum jogador participou.')

if __name__ == '__main__':
    main()