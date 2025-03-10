# Funções Lambda (anônimas)
# Sintaxe:
# lambda argumentos: expressão

# quadrado = lambda x: x**2

# for i in range(1,11):
#     print(quadrado(i))

# par = lambda x: x %2 == 0
# print(par(10))

# f_c = lambda f: (f - 32) * 5/9
# print(f_c(100))

#Funções Map
# Sintaxe:
# map(função, iteravel)

# num = [1,2,3,4,5,6,7,8]
# dobro = list(map(lambda x: x*2, num))
# print(dobro)

# palavras = ['Pythoon', 'é', 'uma', 'linguagem', 'de', 'programação']
# maiúsculas = list(map(str.upper, palavras))
# print(maiúsculas)

#Funções Filter()
# Sintaxe:
# filter(função, sequencia)

# def numeros_pares(n):
#     return n % 2 == 0

# numeros = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]

# num_par = list(filter(numeros_pares, numeros))
# print(num_par)

# numeros = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
# num_impar = list(filter(lambda x: x % 2 != 0, numeros))
# print(num_impar)

#Funções Reduce()
# Sintaxe:
# reduce(função, sequencia, valor_inicial)

# from functools import reduce

# def mult(x, y):
#     return x * y

# numeros = [1,2,3,4,5,6]

# total = reduce(mult, numeros)
# print(total)

# Soma cumulativa dos quadrados de valores, utilizando expressão lambda

numeros = [1,2,3,4]
# ((1² + 2²)² +3²)² + 4²

total = reduce(lambda x, y: x**2 + y**2, numeros)
print(total)

