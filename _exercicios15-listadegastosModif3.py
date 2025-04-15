import pandas as pd
import matplotlib.pyplot as plt

# Dados dos gastos
gastos_joao = [300, 400, 200, 800]
gastos_pedro = [200, 400, 500, 700]
categorias = ['Categoria 1', 'Categoria 2', 'Categoria 3', 'Categoria 4']

# Criação de DataFrame
df = pd.DataFrame({
    'Categoria': categorias,
    'João': gastos_joao,
    'Pedro': gastos_pedro
})

# Cálculo de totais e médias
df.loc['Total'] = ['Total', df['João'].sum(), df['Pedro'].sum()]
df.loc['Média'] = ['Média', df['João'][:-1].mean(), df['Pedro'][:-1].mean()]  # Ignora a linha 'Total' ao calcular a média

# Exibir a tabela
print("\nTabela de Gastos:\n")
print(df)

# Gráfico de barras comparando os gastos por categoria
plt.figure(figsize=(8, 5))
bar_width = 0.35
index = range(len(categorias))

plt.bar(index, gastos_joao, bar_width, label='João', color='skyblue')
plt.bar([i + bar_width for i in index], gastos_pedro, bar_width, label='Pedro', color='orange')

plt.xlabel('Categorias')
plt.ylabel('Valor gasto (R$)')
plt.title('Comparativo de Gastos - João vs Pedro')
plt.xticks([i + bar_width / 2 for i in index], categorias)
plt.legend()
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Mostrar gráfico
plt.show()