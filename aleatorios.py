import random

# valor = random.randint(1,20)
# print(valor)

# print('Gerar seis números aleatórios entre 1 e 60: \n')
# for i in range(6):
#     n = random. randint(1,60)
#     print(f'Número gerado: {n}')

# valor = random.random()
# print(f'Número gerado: {round(valor * 10, 2)}')

# valor = random.uniform(1,100)
# print(f'Número: {round(valor, 4)} ')

L = [3,5,9,11,12,15,17,19,21,27]
# n = random.choice(L)
# print(f'Número escolhido: {n}')

# n = random.sample(L,3)
# print(f'Número escolhido: {n}')

# Embaralhar
print(f'Exibir a lista original: {L}')
print(f'Embaralhar a lista e exibi-la:')
n = random.shuffle(L)
print(L)