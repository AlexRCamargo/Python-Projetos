# Trocar valores entre duas variaveis

var1 = 12
var2 = 31

# var2, var1 = var1, var2

# print(f'var1: {var1}, var2: {var2}')

# Operador Condicional Ternario

# menor = var1 if var1 < var2 else var2

# print(f'Menor valor: {menor}')
# print(f'Menor valor: {(var2, var1)[var1 < var2]}') # Tupla

# Generators - Tipo especial de objeto que é parecido com Compreensões de Listas, mas não retorna uma Lista e sim um objeto especial interável.
# Consome menos recursos em memória

# valores = [1,3,5,7,9,11,13,15]
# quadrados =(item**2 for item  in valores)
# print(quadrados)
# for valor in quadrados:
#     print(valor)

# Função enumerate()

# bebidas = ['Café', 'Água', 'Chá', 'Suco', 'Refrigerante']
# for i, item in enumerate(bebidas):
#     print(f'Indice: {i}, Item: {item}')

temperaturas = [-1, 10, 5, -3, 8, 4, -2, -5, 7]
total = 0

# for i, t in enumerate(temperaturas):
#     if t < 0:
#         total +=1
# print(f'Há {total} temperaturas negativas na amostra.')

# temperaturas = [-1, 10, 5, -3, 8, 4, -2, -5, 7]
# total = 0

# for i, t in enumerate(temperaturas):
#     if t < 0:
#         print(f'A temperatura em {i} é negativa, com {t}°C.')

# Gerenciamento de Contexto com with

# try:
#     a = open('frutas.txt',  'r', encoding='utf-8')
#     print(a.read())
# except IOError:
#     print(f'Não foi possível abrir o arquivo')
# else:
#     a.close()

with open ('frutas.txt',  'r', encoding='utf-8') as a:
    for linha in a:
        print(linha, end='')
