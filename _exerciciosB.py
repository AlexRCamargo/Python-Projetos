# Desenvolva um programa que realize cálculos simples, como a soma, subtração, multiplicação e divisão de dois números inseridos pelo usuário.

x = y = 0

x = int(input('Digite um número inteiro: '))
y = int(input('Digite outro número inteiro: '))

z1 = x + y
z2 = x - y
z3 = x * y
z4 = x // y

print('O resultado da soma dos números digitados é igual a',z1)
print('O resultado da subtração dos números digitados é igual a',z2)
print('O resultado da multiplicação dos números digitados é igual a',z3)
print('O resultado da divisão dos números digitados é igual a',z4)
