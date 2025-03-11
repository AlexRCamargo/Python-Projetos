# Lista representa uma sequencia de valores armazenadas na memoria.

# Sintaxe: nome_lista = [valores] - separados por virgula

# notas = [5, 7, 8, 6, 9]
# print(notas)

n1 = [4, 6, 7, 8, 0, 3]
n2 = [1, 6, 3, 0, 12, 4]
valores = n1 + n2
# valores[0] = 8
# print(valores)
# print(type(valores)) - indica a classe dos valores
# print(valores[0:2])
# print(len(valores))
# print(sorted(valores))
# print(sorted(valores, reverse=True)) - exibe os valores na ordem inversa
# print(sum(valores))
# print(min(valores))  
# print(max(valores)) 

# valores.append(13)
# print(valores)
# valores.pop()
# print(valores)
# valores.pop(3)
# print(valores)
# valores.insert (3, 21)
# print(valores)
# print(12 in valores)
# print(17 in valores)

# planetas = ['Mercúrio', 'Vênus', 'Marte', 'Saturno', 'Urano', 'Netuno']
# for planeta in planetas:
#     print(planeta)

# Resolução Exercicio

bebidas = []

for i in range(5):
    print(f'Digite o nome de uma bebida favorita:')
    bebida = input()
    bebidas.append(bebida)

    bebidas.sort()

    print(f'\nBebidas escolhidas:')
    for bebida in bebidas:
        print(bebida)

print(f'\nÓtimas escolhas!!!')