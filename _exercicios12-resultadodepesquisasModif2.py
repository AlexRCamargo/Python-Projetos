# Seu objetivo é calcular qual produto foi o mais votado. A partir da lista de votos, 
# Crie um dicionário onde a chave é cada produto, 
# E o valor é o número de votos que o produto recebeu.

# Código mais moder e sofisticado usando a biblioteca Counter do módulo collections

from collections import Counter

votos = int(input('Quantos votos você deseja registrar? '))   # Pedimos ao usuário para inserir o número de votos que deseja registrar.

produtos = []                                                 # Criamos uma lista vazia chamada produtos.
for _ in range(votos):                                        # Usamos um loop for para solicitar ao usuário que insira o nome de um produto.
    produto = input('Digite o nome do produto: ')             # Para cada iteração, pedimos ao usuário para inserir o nome de um produto.
    produtos.append(produto)  
                                  
contagem_votos = Counter(produtos)                            # Usamos a função Counter para contar quantas vezes cada produto aparece na lista produtos. O resultado é armazenado no dicionário contagem_votos.

print(dict(contagem_votos))                                   # Por fim, exibimos o dicionário contagem_votos, que contém o número de votos para cada produto.
