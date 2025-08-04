# Projeto: Análise de Dados de Vendas Online

### Introdução

Este projeto consiste na análise de um conjunto de dados de transações de uma loja de varejo online. O objetivo é extrair insights sobre o desempenho de vendas, identificar produtos mais populares e segmentar clientes usando a análise RFM, que é fundamental para estratégias de marketing.

### Tecnologias Utilizadas

O projeto foi desenvolvido em Python, utilizando as seguintes bibliotecas e ferramentas:

* **Pandas:** Para manipulação e limpeza dos dados.
* **Openpyxl:** Para ler arquivos no formato `.xlsx`.
* **Matplotlib e Seaborn:** Para a criação de visualizações estatísticas.
* **Jupyter Notebook:** Para a documentação e execução interativa da análise.
* **Git & GitHub:** Para controle de versão e hospedagem do projeto.

### Estrutura do Projeto

A estrutura de pastas foi organizada para manter o projeto limpo e organizado:

.

├── data/
│   ├── Online Retail.xlsx
│   └── vendas_limpo.csv

├── notebooks/
│   └── analise_vendas.ipynb

├── reports/
│   ├── top_paises.png
│   ├── top_produtos.png
│   └── vendas_por_mes.png

└── scripts/
├── analise_rfm.py
├── limpeza_vendas.py
└── visualizacao_vendas.py

### Análise e Resultados

#### 1. Limpeza de Dados

A etapa de limpeza de dados incluiu:
-   Remoção de linhas com `CustomerID` ausente.
-   Conversão da coluna de data para o formato `datetime`.
-   Filtro de transações com quantidade positiva, focando apenas em vendas.

#### 2. Visualização de Dados

Os gráficos gerados revelaram insights importantes:
-   **Tendência de Vendas:** As vendas mostraram um crescimento consistente ao longo do ano, com um pico significativo nos meses finais, indicando um possível impacto de feriados.
-   **Produtos Mais Vendidos:** Foi possível identificar os produtos mais populares em termos de quantidade vendida, o que pode ajudar na gestão de estoque.
-   **Faturamento por País:** A análise de faturamento por país mostrou que o Reino Unido é o principal mercado, seguido de outros países europeus.

#### 3. Análise de Clientes (RFM)

A análise RFM permitiu segmentar a base de clientes. Com as métricas de Recência, Frequência e Valor Monetário, é possível identificar:
-   **Melhores Clientes:** Aqueles que compraram recentemente, com frequência e gastaram mais.
-   **Clientes em Risco:** Clientes que compraram há muito tempo, mas que compravam com frequência e gastavam muito.

### Como Executar o Projeto

1.  **Clone o repositório:**
    `git clone https://github.com/dencode7/analise-vendas-online.git`
2.  **Navegue para a pasta do projeto:**
    `cd analise-vendas-online`
3.  **Inicie o Jupyter Notebook:**
    `jupyter notebook`
4.  Abra o arquivo `notebooks/analise_vendas.ipynb` para ver a análise completa.
