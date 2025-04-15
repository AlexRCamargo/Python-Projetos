# Exibe o cabeçalho da tabuada com identação horizontal (\t)
print('\t------- Tabuada -------')

# Solicita ao usuário um número inteiro
numero = int(input('Informe um número para ver a Tabuada: '))

# Exibe o título da tabuada
print(f'\nTabuada do {numero}:\n')

# Geração da tabuada de 1 a 10 usando laço for
for i in range(1, 11):
    resultado = numero * i
    print(f'{numero} x {i:2} = {resultado}')