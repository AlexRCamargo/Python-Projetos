numero = int(input(f'Informe um numero inteiro entre 0 e 99: '))

if numero % 2 == 0:
    print(f'O numero informado {numero} é PAR')
elif(numero >=99):
    print(f'Numero invalido. Digite outra vez: ')
else:
    print(f'O numero informado {numero} é IMPAR')