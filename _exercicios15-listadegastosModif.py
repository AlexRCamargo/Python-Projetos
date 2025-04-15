# Seu objetivo é encontrar quem gastou mais dinheiro ao longo do mês, João ou Pedro. Para isso, crie um código em Python que responda a essa pergunta.

   # Por fim, o código exibe o resultado da comparação.

# Listas de gastos mensais
gastos_joao = [300, 400, 200, 800]
gastos_pedro = [200, 400, 500, 700]

# Soma dos gastos de cada um
total_gastos_joao = sum(gastos_joao)
total_gastos_pedro = sum(gastos_pedro)

# Comparação dos totais de gastos
if total_gastos_joao > total_gastos_pedro:
    print("João gastou mais dinheiro este mês.")
elif total_gastos_pedro > total_gastos_joao:
    print("Pedro gastou mais dinheiro este mês.")
else:
    print("João e Pedro gastaram a mesma quantia este mês.")