# Seu objetivo é encontrar quem gastou mais dinheiro ao longo do mês, João ou Pedro. Para isso, crie um código em Python que responda a essa pergunta.

gastos_joao = [300, 400, 200, 800]
gastos_pedro = [200, 400, 500, 700]

total_gastos_joao = sum(gastos_joao)                            # Primeiro, somamos todos os gastos de João e Pedro usando a função sum(). 
total_gastos_pedro = sum(gastos_pedro)                          # Dessa forma, são criadas as variáveis total_gastos_joao e total_gastos_pedro.

if total_gastos_joao > total_gastos_pedro:                      # Em seguida, comparamos os totais de gastos usando uma estrutura condicional (if, elif, else) 
    print("João gastou mais dinheiro este mês.")                # para determinar quem gastou mais (ou se ambos gastaram a mesma quantidade). 
elif total_gastos_pedro > total_gastos_joao:
    print("Pedro gastou mais dinheiro este mês.")
else:
    print("João e Pedro gastaram a mesma quantia este mês.")    # Por fim, o código exibe o resultado da comparação.
