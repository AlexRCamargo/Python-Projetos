# Seu objetivo é calcular qual produto foi o mais votado. A partir da lista de votos, 
# Crie um dicionário onde a chave é cada produto, 
# E o valor é o número de votos que o produto recebeu.

votos = ['A', 'A', 'B', 'A', 'B', 'C', 'C', 'A', 'A', 'C', 'B', 'A', 'D', 'D']

contagem_votos = {}                     # Iniciamos um dicionário vazio chamado contagem_votos. 

for produtos in votos:                  # Iteramos sobre cada voto na lista votos e, para cada produto, verificamos se ele já está no dicionário contagem_votos. 
    if produtos in contagem_votos:
        contagem_votos[produtos] += 1   # Se sim, incrementamos o valor associado a essa chave em 1
    else:                               
        contagem_votos[produtos] = 1    # Caso contrário, criamos uma associação nova no dicionário, associando o produto e o valor de contagem 1 (já que ele está 
                                        # sendo contado pela primeira vez).
print(contagem_votos)                   # No final, o dicionário contagem_votos possuirá o número de votos para cada produto, e exibimos com a função print()

# Para criar um dicionário com o número de votos para cada produto, podemos iterar pela lista de votos e contar quantas vezes cada produto aparece. 
