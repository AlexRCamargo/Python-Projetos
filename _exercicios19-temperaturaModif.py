
cidades = []
temperaturas = []
total_negativas = 0

# Coleta de dados
while True:
    cidade = input('Digite o nome da cidade (ou "fim" para encerrar): ')
    if cidade.lower() == 'fim':
        break
    temperatura = float(input('Digite a temperatura atual: '))
    
    cidades.append(cidade)
    temperaturas.append(temperatura)

# Verificação
for cidade, temp in zip(cidades, temperaturas):
    if temp < 0:
        total_negativas += 1
        print(f'A temperatura em {cidade} é negativa, com {temp}°C.')

if total_negativas == 0:
    print('Não há temperaturas negativas na amostra.')
