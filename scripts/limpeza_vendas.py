import pandas as pd

# 1. Carregar os dados
# O arquivo está na pasta 'data/' e o script está em 'scripts/',
# então o caminho relativo é '../data/Online Retail.xlsx'.
df = pd.read_excel('../data/Online Retail.xlsx')

# Exibir as primeiras 5 linhas e informações para inspeção inicial
print("Dados originais:")
print(df.head())
print("-" * 50)
print("Informações sobre os dados (valores ausentes e tipos):")
print(df.info())
print("-" * 50)

# 2. Lidando com valores ausentes
# A coluna 'CustomerID' tem valores ausentes, que podem ser importantes.
# Vamos remover as linhas onde o CustomerID está ausente.
df.dropna(subset=['CustomerID'], inplace=True)

# 3. Tratando tipos de dados incorretos
# A coluna 'InvoiceDate' está como string, mas deveria ser datetime.
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# 4. Corrigindo dados inconsistentes
# Existem valores negativos na coluna 'Quantity', que representam devoluções.
# Para a nossa análise inicial, vamos focar apenas nas vendas.
# Vamos filtrar o DataFrame para manter apenas as quantidades positivas.
df = df[df['Quantity'] > 0]

# 5. Criando novas colunas úteis
# Vamos calcular o preço total por transação.
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

# 6. Salvar o conjunto de dados limpo
# Salvaremos o novo arquivo na pasta 'data/' com um nome diferente.
df.to_csv('../data/vendas_limpo.csv', index=False)

# Exibir informações do novo DataFrame limpo
print("Informações sobre os dados após a limpeza:")
print(df.info())
print("-" * 50)
print("Dados limpos e processados salvos com sucesso em 'data/vendas_limpo.csv'.")