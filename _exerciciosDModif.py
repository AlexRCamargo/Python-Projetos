# Estruturas de decisões e iteração

# Implemente um programa que utilize estruturas de decisões (if, else, elif) para determinar se um número inserido pelo usuário é positivo, negativo ou zero. 
# Utilize também loops para pedir novos números até que o usuário insira X.

while True:
    entrada = input('Digite um número qualquer (ou "X" para sair): ').strip() # .strip() remove espaços em branco extras.

    if entrada.upper() == 'X': # .upper() garante que tanto "x" quanto "X" funcionem para sair.
        print('Encerrando o programa...')
        break

    try: # Tenta converter a entrada para inteiro. Se falhar, entra no except.
         # O try-except é uma boa prática para evitar que o programa quebre com entradas inválidas.
         # O uso de try-except é uma boa prática para evitar que o programa quebre com entradas inválidas.
        numero = int(entrada)

        if numero < 0:
            print(f'O número digitado {numero} é NEGATIVO.')
        elif numero > 0:
            print(f'O número digitado {numero} é POSITIVO.')
        else:
            print(f'O número digitado {numero} é NEUTRO.')

    except ValueError: # try-except garante robustez contra entradas não numéricas.
        print('Entrada inválida. Digite um número inteiro ou "X" para sair.')