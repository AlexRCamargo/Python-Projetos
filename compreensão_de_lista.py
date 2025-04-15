numeros = [1,4,7,9,10,12,21]

quadrados = list(map(lambda num: num**2, numeros))
print(quadrados)

quadrados = [num**2 for num in numeros] # Compreensão de Lista
print(quadrados)

# Criar uma lista de números pares de 0 a 10
pares = [num for num in range(11) if num % 2 == 0]
print(pares)

# Distributiva entre valores de duas listas
distributiva = [k * m for k in [2,3,5] for m in [10,20,30]]
print(distributiva)
