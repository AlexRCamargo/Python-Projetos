# Faça um programa que receba o projeto do etanol e o preço da gasolina e escrever na tela qual o mais vantajoso abastecer. 
# Lembrando que somente é mais vantajoso abastecer com etanol quando o valor é 70 % menor que o valor da gasolina. USE FUNÇÃO.

def calculo (e,g):
    vantagem = e/g
    if(vantagem <= 0.7):
        return(f'Pode abastecer com Etanol')
    else:
        return(f'Pode abastecer com Gasolina')
    
etanol = float(input(f'Digite o preço do Etanol: '))
gasolina = float(input(f'Digite o preço da Gasolina: '))
print(calculo(etanol, gasolina))

