# Importar o módulo math completo
import math

# Importar uma função especifica do módulo math
from math import sqrt, sin

import math as m
print(m.sqrt(144))

# Ponto de inicio do programa
import mod_func as mf

if __name__ == '__main__':

    mf.mensagem()

    num = int(input('Digite um número inteiro: '))

    print(f'\nCalcular o fatorial do número {num}:')
    fat = mf.fatorial(num)
    print(f'O fatorial é {fat}')

    print(f'\nCalcular sequencia de Fibonacci do número {num}:')
    fib = mf.fibo(num)
    print(f'A sequencia é {fib}')
