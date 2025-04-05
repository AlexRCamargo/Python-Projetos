# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:  
# a. "Telefonou para a vítima?"  
# b. "Esteve no local do crime?"  
# c. "Mora perto da vítima?"  
# d. "Devia para a vítima?"  
# e. "Já trabalhou com a vítima?"  
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
# Caso contrário, ele será classificado como "Inocente". 

respostas = [ 'a', 'b', 'c', 'd', 'e']
classificado = ['Suspeito', 'Cúmplice', 'Assassino', 'Inocente']

contagem_votos = {}

N = 'nao' 
n = 'nao' 
S = 'sim' 
s = 'sim'

jogador = input('Digite o nome do Jogador: ')
resposta = input('Responda as perguntas abaixo digitando S para SIM e N para NÃO:')

a = input('a. Telefonou para a vítima? ')
for resposta in respostas:
    if resposta in contagem_votos:
        contagem_votos[resposta] += 1
    else:
        contagem_votos[resposta] = 1

b = input('b. Esteve no local do crime? ')


c = input('c. Mora perto da vítima? ')


d = input('d. Devia para a vítima? ')


e = input('e. Já trabalhou com a vítima? ')

print(contagem_votos)
print(f'O jogador {jogador} não é suspeito de participação no crime!')
print(f'O jogador {jogador} é {classificado} de participação nesse crime!')


