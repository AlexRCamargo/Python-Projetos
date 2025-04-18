# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:  
# a. "Telefonou para a vítima?"  
# b. "Esteve no local do crime?"  
# c. "Mora perto da vítima?"  
# d. "Devia para a vítima?"  
# e. "Já trabalhou com a vítima?"  
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
# Caso contrário, ele será classificado como "Inocente". 

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
                print('Resposta inválida. Digite apenas "S" para SIM ou "N" para NÃO.')
    
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

def main():
    print('=== Questionário de Investigação Criminal ===')
    jogador = input('Digite o nome do jogador: ').strip()

    respostas_positivas = fazer_perguntas()
    resultado = classificar(respostas_positivas)

    print(f'\nO jogador {jogador} foi classificado como: {resultado}.')

if __name__ == '__main__':
    main()