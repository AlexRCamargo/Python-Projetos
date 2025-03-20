# Operadores e cálculos

# Desenvolva um programa que realize cálculos simples, como a soma, subtração, multiplicação e divisão de dois números inseridos pelo usuário.

x = y = 0

x = int(input('Digite um número inteiro: '))
y = int(input('Digite outro número inteiro: '))

z1 = x + y
z2 = x - y
z3 = x * y
z4 = x // y
z5 = x ** y

print(f'O resultado da soma de {x} + {y} é igual a',z1)
print(f'O resultado da subtração de {x} - {y} é igual a',z2)
print(f'O resultado da multiplicação de {x} x {y} é igual a',z3)
print(f'O resultado da divisão de {x} / {y} é igual a',z4)
print(f'O resultado da potência de {x} elevado a {y} é igual a', z5)
