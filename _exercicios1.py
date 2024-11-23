bebidas = []

for i in range(6):
    bebida = input(f'Digite o nome de uma bebida favorita:')
    bebidas.append(bebida) # Manipular dados da lista, alterando seus valores, inserindo novos elementos no final da lista 

    bebidas.sort() # Retorna versão ordenada da lista sem modificar a lista em si. Coloca em ordem alfabetica ou numerica

    print(f'\nBebidas Escolhidas:')
    for bebida in bebidas:
        print(bebida)

print(f'\nÓtimas Escolhas!!!')
