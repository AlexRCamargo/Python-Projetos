# Calcule a média dos valores dessa lista.

numeros = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

soma = 0
for numero in numeros:
    soma += numero

media = soma / len(numeros)
print("A média dos números é: ", media)

# Nesse código, temos uma lista de números chamada numeros. Para calcular a média, primeiro inicializamos uma variável soma com o valor zero. 
# Em seguida, percorremos cada número na lista numeros usando um for loop for e adicionamos cada número à variável soma.

# Depois de percorrer todos os números, dividimos a soma pelo número total de elementos na lista numeros, que obtemos através da função len(). 
# Com essa operação, obtemos a média. Então, ao final do código, exibimos a média usando a função print().