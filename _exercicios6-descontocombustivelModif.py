# Um posto de combustiveis está vendendo combustiveis com a seguinte tabela de desconto
# Etanol: Até 20 litros, desconto de 3 % por litro
# Acima de 20 litros, desconto de 5 % por litro
# GAsolina: Até 20 litros, desconto de 4 % por litro
# Acima de 20 litros, desconto de 6 % por litro
# Escreva um algoritmo que leia o número de litros vendidos
# Tipo de combustivel (codificado da seguinte forma: E - Etanol/ G - Gasolina)
# Calcule e imprima o valor a ser pago pelo cliente, sabendo-se que o preço do litro da gasolina é R$ 5,80 e o preço do litro do etanol é R$ 3,80

# Definindo constantes para facilitar a leitura
G = 'G'
E = 'E'

# Solicita as informações ao usuário
litros = int(input('Digite quantos litros de combustível você quer abastecer: '))
combustivel = input('Digite E para Etanol ou G para Gasolina: ').strip().upper()  # Limpa espaços e transforma a letra em maiúscula para não ter erro de digitação.
preco_combustivel = float(input('Digite o preço do combustível em R$: '))

# Calcula o valor total sem desconto
preco_total = litros * preco_combustivel

# Aplica desconto de acordo com o combustível e quantidade
if combustivel == E:
    if litros <= 20:
        desconto = 3  # 3% de desconto
    else:
        desconto = 5  # 5% de desconto
elif combustivel == G:
    if litros <= 20:
        desconto = 4  # 4% de desconto
    else:
        desconto = 6  # 6% de desconto
else:
    print('Tipo de combustível inválido.')
    desconto = 0

# Aplica o desconto
preco_final = preco_total - (preco_total * desconto / 100)

# Exibe o preço final
print(f'O preço a pagar é R$ {preco_final:.2f}')