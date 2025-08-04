import pandas as pd
import datetime

# 1. Carregar os dados limpos
df = pd.read_csv('../data/vendas_limpo.csv')

# Certifique-se de que a coluna de data está no formato correto
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# 2. Calcular a Recência (Recency)
# Para a Recência, precisamos de uma data de referência (hoje ou a última data no dataset)
snapshot_date = df['InvoiceDate'].max() + datetime.timedelta(days=1)

# Agrupar por CustomerID para calcular RFM
rfm = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (snapshot_date - x.max()).days, # Recência
    'InvoiceNo': 'count',                                   # Frequência
    'TotalPrice': 'sum'                                     # Monetário
})

# Renomear as colunas para RFM
rfm.rename(columns={'InvoiceDate': 'Recency',
                    'InvoiceNo': 'Frequency',
                    'TotalPrice': 'Monetary'}, inplace=True)

# 3. Exibir os resultados
print("Tabela RFM (os 5 primeiros clientes):")
print(rfm.head())
print("-" * 50)
print("Resumo estatístico da tabela RFM:")
print(rfm.describe())

# Opcional: Salvar a tabela RFM para futuras análises
rfm.to_csv('../data/tabela_rfm.csv')
print("\nTabela RFM salva com sucesso em 'data/tabela_rfm.csv'.")