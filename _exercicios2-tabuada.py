print('\t ---- Tabuada ----') # \t = escape para tubulação

numero = int(input('Informe um número para ver a Tabuada: '))

print('\nTabuada do', numero,':')

for i in range(1, 11):
    print(numero, 'x', i, '=', (numero * i))
