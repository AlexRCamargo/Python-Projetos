# Seu objetivo é calcular qual produto foi o mais votado. A partir da lista de votos, 
# Crie um dicionário onde a chave é cada produto, 
# E o valor é o número de votos que o produto recebeu.

votos = int(input('Quantos votos você deseja registrar? '))   # Pedimos ao usuário para inserir o número de votos que deseja registrar.

produtos = []                                                 # Criamos uma lista vazia chamada produtos.
for i in range(votos):                                        # Usamos um loop for para solicitar ao usuário que insira o nome de um produto.
    produto = input('Digite o nome do produto: ')             # Para cada iteração, pedimos ao usuário para inserir o nome de um produto.
    produtos.append(produto)  
                                  
contagem_votos = {}                                           # Iniciamos um dicionário vazio chamado contagem_votos.

for produto in produtos:                                      # Iteramos sobre cada voto na lista produtos e, para cada produto, verificamos se ele já está no dicionário contagem_votos.
    if produto in contagem_votos:
        contagem_votos[produto] += 1
    else:
        contagem_votos[produto] = 1

print(contagem_votos)
