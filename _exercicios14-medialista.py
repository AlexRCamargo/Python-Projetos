# Calcule a média dos valores dessa lista.

# Nesse código, temos uma lista de números chamada numeros. 

numeros = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

soma = 0                                # Para calcular a média, primeiro inicializamos uma variável soma com o valor zero. 
for numero in numeros:                  # Percorremos cada número na lista numeros usando um for loop for e adicionamos cada número à variável soma.
    soma += numero

media = soma / len(numeros)             # Dividimos a soma pelo número total de elementos na lista numeros, que obtemos através da função len(). 
print('A média dos números é: ', media) # Com essa operação, obtemos a média. Então, ao final do código, exibimos a média usando a função print().
