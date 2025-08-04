import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurações do estilo dos gráficos
sns.set_style('whitegrid')

# 1. Carregar os dados limpos
df = pd.read_csv('../data/vendas_limpo.csv')

# Exibir as primeiras linhas do dataframe limpo para confirmar
print("Visualizando os dados limpos:")
print(df.head())
print("-" * 50)


# 2. Gráfico de Série Temporal - Vendas por Mês
# Extrair o mês e ano da coluna 'InvoiceDate'
df['InvoiceMonth'] = df['InvoiceDate'].apply(lambda x: x[:7])

plt.figure(figsize=(12, 6))
vendas_por_mes = df.groupby('InvoiceMonth')['TotalPrice'].sum().reset_index()
sns.lineplot(x='InvoiceMonth', y='TotalPrice', data=vendas_por_mes)
plt.title('Vendas Totais por Mês')
plt.xlabel('Mês')
plt.ylabel('Vendas Totais')
plt.xticks(rotation=45)
plt.savefig('../reports/vendas_por_mes.png')
plt.show() # Para ver o gráfico na tela


# 3. Gráfico de Barras - Produtos Mais Vendidos (Top 10)
plt.figure(figsize=(12, 6))
top_produtos = df.groupby('Description')['Quantity'].sum().nlargest(10).sort_values(ascending=False).index
sns.barplot(x='Description', y='Quantity', data=df[df['Description'].isin(top_produtos)], estimator=sum, errorbar=None)
plt.title('Top 10 Produtos Mais Vendidos')
plt.xlabel('Produto')
plt.ylabel('Quantidade Vendida')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('../reports/top_produtos.png')
plt.show() # Para ver o gráfico na tela


# 4. Gráfico de Barras - Países com Mais Vendas (Top 5)
plt.figure(figsize=(10, 6))
top_paises = df.groupby('Country')['TotalPrice'].sum().nlargest(5).sort_values(ascending=False)
sns.barplot(x=top_paises.index, y=top_paises.values)
plt.title('Top 5 Países com Maior Faturamento')
plt.xlabel('País')
plt.ylabel('Faturamento Total')
plt.tight_layout()
plt.savefig('../reports/top_paises.png')
plt.show() # Para ver o gráfico na tela


print("Gráficos gerados e salvos na pasta 'reports/'.")