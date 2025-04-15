def coletar_dados():
    cidades = []
    temperaturas = []

    print('=== Cadastro de Cidades e Temperaturas ===')
    while True:
        cidade = input('\nDigite o nome da cidade (ou "fim" para encerrar): ').strip()
        if cidade.lower() == 'fim':
            break
        if not cidade:
            print('Nome da cidade não pode ser vazio. Tente novamente.')
            continue
        
        try:
            temperatura = float(input(f'Digite a temperatura atual em {cidade}: '))
        except ValueError:
            print('Temperatura inválida. Digite um número válido.')
            continue
        
        cidades.append(cidade)
        temperaturas.append(temperatura)
    
    return cidades, temperaturas

def analisar_temperaturas(cidades, temperaturas):
    total_negativas = 0

    print('\n=== Análise de Temperaturas ===')
    for cidade, temp in zip(cidades, temperaturas):
        if temp < 0:
            total_negativas += 1
            print(f'⚠️  Temperatura negativa em {cidade}: {temp:.1f}°C')
    
    if total_negativas == 0:
        print('✅ Não há temperaturas negativas na amostra.')

def main():
    cidades, temperaturas = coletar_dados()
    
    if cidades:
        analisar_temperaturas(cidades, temperaturas)
    else:
        print('Nenhuma cidade foi cadastrada.')

if __name__ == '__main__':
    main()