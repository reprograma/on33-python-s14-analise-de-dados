import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns



df_avaliacao = pd.read_csv(r'C:\Users\55119\OneDrive\Área de Trabalho\REPROGRAMA (On33)\Semana14\on33-python-s14-analise-de-dados\material\dados\olist_order_reviews_dataset.csv')
df_avaliacao.head()

df_pedidos = pd.read_csv(r'C:\Users\55119\OneDrive\Área de Trabalho\REPROGRAMA (On33)\Semana14\on33-python-s14-analise-de-dados\material\dados\olist_orders_dataset.csv')
df_pedidos.head()

df_produtos = pd.read_csv(r'C:\Users\55119\OneDrive\Área de Trabalho\REPROGRAMA (On33)\Semana14\on33-python-s14-analise-de-dados\material\dados\olist_products_dataset.csv')
df_produtos.head()

df_vendas = pd.read_csv(r'C:\Users\55119\OneDrive\Área de Trabalho\REPROGRAMA (On33)\Semana14\on33-python-s14-analise-de-dados\material\dados\olist_order_items_dataset.csv')
df_vendas.head()

df_avaliacao.describe(include='all')

# Verificar colunas
df_avaliacao.columns

# Combinar as bases de dados
dados_juntos = df_avaliacao.merge(df_pedidos, on='order_id')
dados_juntos = dados_juntos.merge(df_vendas, on='order_id')
dados_juntos = dados_juntos.merge(df_produtos, on='product_id')

# Criar uma coluna para identificar avaliações negativas (nota menor que 3)
dados_juntos['avaliacao_negativa'] = dados_juntos['review_score'] < 3

# Converter a coluna de data para datetime
dados_juntos['review_creation_date'] = pd.to_datetime(dados_juntos['review_creation_date'])
dados_juntos['order_purchase_timestamp'] = pd.to_datetime(dados_juntos['order_purchase_timestamp'])

# Período de tempo para comparar as vendas antes e depois das avaliações negativas
periodo_comparacao = pd.Timedelta(days=120)

# Garantir que 'price' esteja no tipo correto (float)
dados_juntos['price'] = dados_juntos['price'].astype(float)

# Calcular as vendas antes das avaliações    
dados_juntos['vendas_antes'] = 0
dados_juntos.loc[dados_juntos['order_purchase_timestamp'] < dados_juntos['review_creation_date'] - periodo_comparacao, 'vendas_antes'] = dados_juntos['price']

# Calcular as vendas depois das avaliações
dados_juntos['vendas_depois'] = 0
dados_juntos.loc[dados_juntos['order_purchase_timestamp'] > dados_juntos['review_creation_date'] + periodo_comparacao, 'vendas_depois'] = dados_juntos['price']

# Agrupar por produto e calcular a média de vendas antes e depois das avaliações negativas
analise_vendas = dados_juntos.groupby('product_id').agg({
    'avaliacao_negativa': 'sum',
    'vendas_antes': 'sum',
    'vendas_depois': 'sum'
}).reset_index()

# Calcular a diferença nas vendas
analise_vendas['diferenca_vendas'] = analise_vendas['vendas_depois'] - analise_vendas['vendas_antes']

# Exibe o resultado
print('\nA diferença nas vendas é:')
(analise_vendas.head(20))

#Configurar o tamanho da figura
plt.figure(figsize=(14, 7))

# Criar o gráfico de barras
plt.bar(analise_vendas['product_id'], analise_vendas['diferenca_vendas'], color='skyblue')

# Adicionar título e rótulos aos eixos
plt.title('Diferença nas Vendas Antes e Depois das Avaliações Negativas por Produto', fontsize=16)
plt.xlabel('ID do Produto', fontsize=14)
plt.ylabel('Diferença nas Vendas', fontsize=14)

# Rotacionar os rótulos do eixo x para melhor visualização
plt.xticks(rotation=90)

# Ajustar o layout para evitar sobreposição
plt.tight_layout()

# Exibir o gráfico
plt.show()