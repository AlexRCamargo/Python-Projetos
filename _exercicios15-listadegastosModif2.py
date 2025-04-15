# Listas de gastos mensais por categoria/semana (por exemplo)
gastos_joao = [300, 400, 200, 800]
gastos_pedro = [200, 400, 500, 700]

# Função para gerar resumo dos gastos
def resumo_gastos(nome, gastos):
    print(f"\nResumo de gastos - {nome}")
    print(f"Total gasto: R${sum(gastos):.2f}")
    print(f"Média de gastos: R${sum(gastos)/len(gastos):.2f}")
    print(f"Maior gasto: R${max(gastos):.2f}")
    print(f"Menor gasto: R${min(gastos):.2f}")

# Exibe resumo individual
resumo_gastos("João", gastos_joao)
resumo_gastos("Pedro", gastos_pedro)

# Comparação de total
print("\nComparação de totais:")
total_joao = sum(gastos_joao)
total_pedro = sum(gastos_pedro)

if total_joao > total_pedro:
    print("João gastou mais dinheiro este mês.")
elif total_pedro > total_joao:
    print("Pedro gastou mais dinheiro este mês.")
else:
    print("João e Pedro gastaram a mesma quantia este mês.")

# Comparação por categoria (índice)
print("\nComparação por categoria:")
for i in range(len(gastos_joao)):
    if gastos_joao[i] > gastos_pedro[i]:
        vencedor = "João"
    elif gastos_pedro[i] > gastos_joao[i]:
        vencedor = "Pedro"
    else:
        vencedor = "Empate"
    
    print(f"Categoria {i+1}: João = R${gastos_joao[i]}, Pedro = R${gastos_pedro[i]} → {vencedor}")