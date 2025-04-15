while True:
    try:
        numero = int(input('Informe um número qualquer: '))
        break  # Sai do loop se a conversão for bem-sucedida
    except ValueError:
        print('Entrada inválida. Por favor, digite um número inteiro.')

par = lambda numero: numero % 2 == 0 # A função lambda é apropriada nesse contexto, já que a verificação é simples e de uso pontual

if par(numero):
    print(f'O número {numero} é par')
else:
    print(f'O número {numero} é ímpar')