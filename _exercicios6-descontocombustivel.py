# Um posto de combustiveis está vendendo combustiveis com a seguinte tabela de desconto
# Etanol: Até 20 litros, desconto de 3 % por litro
# Acima de 20 litros, desconto de 5 % por litro
# GAsolina: Até 20 litros, desconto de 4 % por litro
# Acima de 20 litros, desconto de 6 % por litro
# Escreva um algoritmo que leia o número de litros vendidos
# Tipo de combustivel (codificado da seguinte forma: E - Etanol/ G - Gasolina)
# Calcule e imprima o valor a ser pago pelo cliente, sabendo-se que o preço do litro da gasolina é R$ 5,80 e o preço do litro do etanol é R$ 3,80

G = 'gasolina'
E = 'etanol'
g = 'gasolina'
e = 'etanol'
preco_G = ()
preco_E = ()
preco = ()

litros = int(input(f'Digite quantos litros de combustiveis você quer abastecer: '))
combustivel = input(f'Digite E para Etanol ou G para Gasolina: ')
int(input('Digite o preço do Combustivel em R$: '))

if combustivel == G or combustivel == g:
    preco = litros * preco_G
    if litros <= 20:
        preco == preco_E * litros * 3 / 100
    else:
        preco == preco_E * litros * 5 / 100
elif combustivel == G or combustivel == g:
    preco = litros * preco_G
    if litros <= 20:
        preco == preco_G * litros * 4 / 100
    else:
        preco == preco_G * litros * 6 / 100

print(f'O preço a pagar é R${preco:.2f}')