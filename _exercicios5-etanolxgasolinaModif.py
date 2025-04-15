# Faça um programa que receba o projeto do etanol e o preço da gasolina e escrever na tela qual o mais vantajoso abastecer. 
# Lembrando que somente é mais vantajoso abastecer com etanol quando o valor é 70 % menor que o valor da gasolina. USE FUNÇÃO.

def calculo_vantagem(preco_etanol, preco_gasolina):
    """
    Calcula a vantagem entre Etanol e Gasolina com base na regra dos 70%.
    Retorna uma recomendação de abastecimento.
    """
    if preco_gasolina == 0:
        return 'Erro: o preço da gasolina não pode ser zero.'
    
    vantagem = preco_etanol / preco_gasolina
    
    if vantagem <= 0.7:
        return 'Recomendação: Abasteça com Etanol.'
    else:
        return 'Recomendação: Abasteça com Gasolina.'

try:
    # Entrada dos preços
    etanol = float(input('Digite o preço do Etanol: R$ '))
    gasolina = float(input('Digite o preço da Gasolina: R$ '))

    # Resultado da análise
    resultado = calculo_vantagem(etanol, gasolina)
    print('\n' + resultado)

except ValueError:
    print('Erro: por favor, insira apenas números válidos.')