numero = int(input('Informe um número qualquer: '))
par = lambda numero: numero % 2 == 0 # São funções que não possuem nome e devem ser criadas e usadas no mesmo momento. 

if par(numero):
    print(f'O número {numero} é par')
else:
    print(f'O número {numero} é impar')

# Lambda – são funções que não possuem nome e devem ser criadas e usadas no mesmo momento. 
# Define uma função previa para ser utilizada depois. Podem ser utilizadas no código onde 
# não é possível utilizar uma função def comum dentro de uma lista ou chamada de outra função. 
# Funciona como um “atalho” de função. 