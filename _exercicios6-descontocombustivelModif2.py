# Um posto de combustiveis está vendendo combustiveis com a seguinte tabela de desconto
# Etanol: Até 20 litros, desconto de 3 % por litro
# Acima de 20 litros, desconto de 5 % por litro
# GAsolina: Até 20 litros, desconto de 4 % por litro
# Acima de 20 litros, desconto de 6 % por litro
# Escreva um algoritmo que leia o número de litros vendidos
# Tipo de combustivel (codificado da seguinte forma: E - Etanol/ G - Gasolina)
# Calcule e imprima o valor a ser pago pelo cliente, sabendo-se que o preço do litro da gasolina é R$ 5,80 e o preço do litro do etanol é R$ 3,80

def calcular_desconto(combustivel: str, litros: float) -> float: 
    """Retorna o percentual de desconto conforme o tipo de combustível e litros abastecidos."""
    if combustivel == 'E':  # Etanol
        return 3 if litros <= 20 else 5
    elif combustivel == 'G':  # Gasolina
        return 4 if litros <= 20 else 6
    else:
        return 0  # Combustível inválido

def calcular_preco_final(litros: float, preco_unitario: float, desconto_percentual: float) -> float:
    """Calcula o preço final com desconto aplicado."""
    preco_bruto = litros * preco_unitario
    desconto = preco_bruto * (desconto_percentual / 100)
    return preco_bruto - desconto

def main(): 
    """Organiza o fluxo do programa. Aqui o usuário interage e os cálculos são feitos chamando as funções."""
    litros = float(input('Digite quantos litros de combustível você quer abastecer: '))
    combustivel = input('Digite E para Etanol ou G para Gasolina: ').strip().upper()
    preco_unitario = float(input('Digite o preço do combustível em R$: '))

    desconto_percentual = calcular_desconto(combustivel, litros)
    
    if desconto_percentual == 0:
        print('Tipo de combustível inválido. Operação cancelada.')
        return

    preco_final = calcular_preco_final(litros, preco_unitario, desconto_percentual)

    print(f'O preço a pagar é R$ {preco_final:.2f}')

if __name__ == "__main__": # Garante que o script rode diretamente e seja reutilizável em outros projetos se quiser.
    main()