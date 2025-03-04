# Seu objetivo é calcular qual produto foi o mais votado. A partir da lista de votos, 
# Crie um dicionário onde a chave é cada produto, 
# E o valor é o número de votos que o produto recebeu.

votos = ['A', 'A', 'B', 'A', 'B', 'C', 'C', 'A', 'A', 'C', 'B', 'A']

contagem_votos = {}

for produtos in votos:
    if produtos in contagem_votos:
        contagem_votos[produtos] += 1
    else:
        contagem_votos[produtos] = 1

print(contagem_votos)

# Para criar um dicionário com o número de votos para cada produto, podemos iterar pela lista de votos e contar quantas vezes cada produto aparece.
# No código acima, iniciamos um dicionário vazio chamado contagem_votos. 
# Em seguida, iteramos sobre cada voto na lista votos e, para cada produto, verificamos se ele já está no dicionário contagem_votos. 
# Se sim, incrementamos o valor associado a essa chave em 1. Caso contrário, criamos uma associação nova no dicionário, associando o produto e o valor 
# de contagem 1 (já que ele está sendo contado pela primeira vez).
# No final, o dicionário contagem_votos possuirá o número de votos para cada produto, o qual exibimos com a função print().