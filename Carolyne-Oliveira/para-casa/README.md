# 📈📉📊🎲 Análise de Dados do Mundo Real 

## 📚 Descrição da Atividade

Exercicio para casa semana 14.
**Objetivo:** Por em prática os conhecimentos de Análise de Dados que aprendemos em aula.

**Desafio:** Criar um notebook de análise exploratória (como fizemos na nossa aula de hoje) com todas as etapas de coleta, limpeza, análise e visualização com base de dados da [Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce).

* Formular no mínimo 4 perguntas para responder com suas análises;

* Utilizar pelo menos 3 bases de dados da Olist (caso você deseje criar sua base do zero). Caso deseje continuar utilizando a que criamos em aula, é necessário incluir pelo menos mais 1 tabela para enriquecer sua análise.

Para responder as perguntas elaboradas usar:

  * Criar pelo menos 3 gráficos.
  * Exporte sua base final em csv.
  * Submeta uma pasta que contenha:
  * o arquivo .ipynb com sua análise exploratória rodada, ou seja, com as respostas aparecendo no notebook;
  * interpretações observadas a partir dos gráficos dentro do notebook;
  * a base final criada por você no formato .csv;
  * especificar quais bases da olist foram usadas;

## 📈 Introdução

A base de dados da Olist é composta por 9 tabelas diferentes, nelas temos informações de:
- pedidos (olist_orders_dataset)
- itens dos pedidos (olist_order_items_dataset)
- review dos usuários sobre os pedidos (olist_order_reviews_dataset)
- detalhes de pagamento dos pedidos (olist_order_payments_dataset)
- detalhes do consumidor que fez os pedidos (olist_customers_dataset)
- detalhes de geolocalização do consumidor (olist_geolocation_dataset)
- detalhes dos produtos (olist_products_dataset)
- detalhes dos vendedores (olist_sellers_dataset)

Optei por trabalhar apenas com estes datasets, o de pedidos (olist_orders_dataset), itens do pedido (olist_order_items_dataset), o de consumidor (olist_customers_dataset), a de produtos (olist_products_dataset) e a de vendedores (olist_sellers_dataset).

## 📋 Passo a Passo

## 🟦 Instalação de Bibliotecas:

 ### - Bibliotecas Utilizadas:

            import pandas as pd
            import seaborn as sns
            import matplotlib.pyplot as plt

## 🟦 Análise exploratória

 ### - Coleta:

            #Importando a base de dados diretamente do Github
            url_pedidos = "https://raw.githubusercontent.com/CarolyneS14/on33-python-s14-analise-de-dados/main/material/dados/olist_orders_dataset.csv"

            #Transformando a base em um DataFrame
            df_pedidos = pd.read_csv(url_pedidos)
            (...)
            #Visualizando o DataFrame(df)
            df_pedidos
            (...)
            #Visualizando o DataFrame(df)
            df_itens_pedido
            (...)
            #Visualizando o DataFrame(df)
            df_consumidor
            (...)
            #Visualizando o DataFrame(df)
            df_vendedor
            (...)
            #Visualizando o DataFrame(df)
            df_produtos


 ### - Limpeza:

            #Estatísticas descritivas sobre o DataFrame:

            df_pedidos.describe(include='all')
            (...)
            #Estatísticas descritivas sobre o DataFrame:

            df_vendedor.describe(include='all')

            #Merge para unir o df_pedidos e o df_itens_pedido:

            df_olist_pedidos = pd.merge(df_pedidos, df_itens_pedido, on=['order_id'], how='inner')
            df_olist_pedidos
            (...)
            #Merge para unir o novo df_olist_pedidos_uf_prod e o df_produtos:

            df_vendas_olist = pd.merge(df_olist_pedidos_uf_prod, df_vendedor, on=['seller_id'], how='inner')
            df_vendas_olist

            #Excluir colunas que nao vamos utilizar:

            columns_drop = ['order_approved_at', 
            'order_delivered_carrier_date', 
            'product_name_lenght', 
            'product_description_lenght', 
            'product_photos_qty',
            'product_weight_g',               
            'product_length_cm',             
            'product_height_cm',
            'product_width_cm',
            'seller_zip_code_prefix',
            'customer_zip_code_prefix',
            'customer_unique_id']
            df_vendas_olist = df_vendas_olist.drop(columns_drop, axis=1)
            df_vendas_olist  

            #Contando o total de valores nulos em cada coluna:

            print(df_vendas_olist.isnull().sum())

            #Substituindo valores nulos pela string 'diversos' na coluna 'product_category_name':

            df_vendas_olist.loc[df_vendas_olist['product_category_name'].isnull(), 'product_category_name'] = 'diversos'

            #Verificando o DataFrame após a substituição:

            print(df_vendas_olist['product_category_name'].isnull().sum())

            #Substituindo os valores nulos na coluna 'order_delivered_customer_date':

            df_vendas_olist.loc[df_vendas_olist['order_delivered_customer_date'].isnull(), 'order_delivered_customer_date'] = df_vendas_olist['order_estimated_delivery_date']

            #Verificando o DataFrame após a substituição:

            print(df_vendas_olist['order_delivered_customer_date'].isnull().sum())

            #Exportando a base final:

            df_vendas_olist.to_csv('base_vendas_s14_olist.csv', index=False)

 ### - Análises:

- 4. Indique quais os três estados possuem a maioria dos clientes na base de dados e quais três estados abrigam a maior quantidade de vendedores? 

            #Contar quantos estados únicos existem na coluna 'customer_state':

            num_estados_clientes = df_vendas_olist['customer_state'].nunique()
            print(f"Quantidade de estados (clientes): {num_estados_clientes}")

            #Contar quantos estados únicos existem na coluna 'seller_state':

            num_estados_vendedores = df_vendas_olist['seller_state'].nunique()
            print(f"Quantidade de estados (vendedores): {num_estados_vendedores}")

            #Quantidade de clientes por estado:

            df_vendas_olist['customer_state'].value_counts()

            #Quantidade de vendedores por estado:

            df_vendas_olist['seller_state'].value_counts()

- 5. Quais são as 10 categorias mais vendidas? E as 10 menos vendidas?

            #Quandidade de categorias presentes na base:

            num_categorias = df_vendas_olist['product_category_name'].nunique()

            #Exibindo o resultado:

            print(f"Quantidade de categorias presentes na base: {num_categorias}")

            #Agrupando os produtos por categoria e contando o número de itens vendidos:

            produtos_por_categoria = df_vendas_olist.groupby('product_category_name')['order_item_id'].count().reset_index()
            produtos_por_categoria.columns = ['Categoria', 'Quantidade Vendida']

            #Ordenando os produtos pela quantidade vendida:

            produtos_por_categoria = produtos_por_categoria.sort_values(by='Quantidade Vendida', ascending=False)

            #Exibindo as 10 principais categorias:

            print(produtos_por_categoria.head(10))

            #Agrupando os produtos por categoria e contando o número de itens vendidos:

            produtos_por_categoria = df_vendas_olist.groupby('product_category_name')['order_item_id'].count().reset_index()
            produtos_por_categoria.columns = ['Categoria', 'Quantidade Vendida']

            #Ordenando os produtos pela quantidade vendida:

            produtos_por_categoria = produtos_por_categoria.sort_values(by='Quantidade Vendida', ascending=True)

            #Exibindo as 10 principais categorias:

            print(produtos_por_categoria.head(10))

- 6. Qual a média de valor gasto pelos clientes por estado? Qual o estado que possue a média mais alta?

            #Verificar a média:

            media_por_estado = df_vendas_olist.groupby('customer_state')['price'].mean().reset_index()
            media_por_estado.columns = ['Estado', 'Média de Valor Gasto']

            #Ordenando os produtos pelo maior valor:

            media_por_estado = media_por_estado.sort_values(by='Média de Valor Gasto', ascending=False)

            #Exibir os estados:

            print('Média de Valor Gasto por Cliente em cada Estado')
            print(media_por_estado)

- 7. Quais categorias de produtos têm um valor mais elevado de vendas? Ou seja, qual categoria vende mais?

            #Configurando a opção de visualização para não resumir a saída:

            pd.set_option('display.max_rows', None)  # Isso exibe todas as linhas sem truncamento/sem resumir (...)

            #Agrupando os produtos por categoria e contando o preço total por categoria:

            preco_por_categoria = df_vendas_olist.groupby('product_category_name')['price'].sum().reset_index()
            preco_por_categoria.columns = ['Categoria', 'Preço Total']

            #Ordenando os produtos pelo preço total (decrescente):

            preco_por_categoria = preco_por_categoria.sort_values(by='Preço Total', ascending=False)

            #Exibindo o total de vendas por categoria:

            print('Total de Vendas por Categoria:')
            print(preco_por_categoria)

- 8. Qual a média de venda por estado? Qual o estado possui a média mais alta?

            #Verificar a média:

            media_por_estado = df_vendas_olist.groupby('seller_state')['price'].mean().reset_index()
            media_por_estado.columns = ['Estado', 'Média de Venda']

           #Ordenando os produtos pelo maior valor:

            media_por_estado = media_por_estado.sort_values(by='Média de Venda', ascending=False)

           #Exibir os estados:

            print('Média de Venda por Estado')
            print(media_por_estado)

 ### - Visualizações:

4 - Clientes e Vendedores por Estado

      #Contando a quantidade de clientes por estado:
      
            clientes_por_estado = df_vendas_olist['customer_state'].value_counts()

      #Selecionando os três estados com maior quantidade de clientes:
      
            top3_estados = clientes_por_estado.head(3)

      #Plotando o gráfico de barras:
      
            plt.figure(figsize=(10, 6))
            ax = sns.barplot(x=top3_estados.index, y=top3_estados.values, hue=top3_estados.index, palette='pastel', legend=False)

      #Adicionando rótulos às barras:
      
            for p in ax.patches:
                ax.annotate(f'{p.get_height():,}', 
                            (p.get_x() + p.get_width() / 2, p.get_height()), 
                            ha='center', va='bottom', 
                            fontsize=10, color='black', 
                            xytext=(0, 5), 
                            textcoords='offset points')

            plt.title('Top 3 Estados com Maior Quantidade de Clientes', fontsize=16)
            plt.xlabel('Estado', fontsize=12)
            plt.ylabel('Quantidade de Clientes', fontsize=12)
            plt.show()

![Grafico1](https://github.com/CarolyneS14/on33-python-s14-analise-de-dados/blob/main/Carolyne-Oliveira/para-casa/Graficos/Grafico1.png)

      #Contando a quantidade de vendedores por estado:

            clientes_por_estado = df_vendas_olist['seller_state'].value_counts()

      #Selecionando os três estados com maior quantidade de vendedores:

            top3_estados = clientes_por_estado.head(3)

      #Plotando o gráfico de barras:

            plt.figure(figsize=(10, 6))
            ax = sns.barplot(x=top3_estados.index, y=top3_estados.values, hue=top3_estados.index, palette='pastel', legend=False)

      #Adicionando rótulos às barras:

            for p in ax.patches:
                ax.annotate(f'{p.get_height():,}', 
                            (p.get_x() + p.get_width() / 2, p.get_height()), 
                            ha='center', va='bottom', 
                            fontsize=10, color='black', 
                            xytext=(0, 5), 
                            textcoords='offset points')

            plt.title('Top 3 Estados com Maior Quantidade de Vendedores', fontsize=16)
            plt.xlabel('Estado', fontsize=12)
            plt.ylabel('Quantidade de Vendedores', fontsize=12)
            plt.show()

![Grafico2](https://github.com/CarolyneS14/on33-python-s14-analise-de-dados/blob/main/Carolyne-Oliveira/para-casa/Graficos/Grafico2.png)

5 - Categorias Mais Vendidas

      #Ordenando os dados de produtos_por_categoria de forma decrescente:

            produtos_por_categoria = produtos_por_categoria.sort_values(by='Quantidade Vendida', ascending=False)

      #Plotando a distribuição por categoria (gráfico de barras):

            plt.figure(figsize=(15, 6))
            ax = sns.barplot(x='Quantidade Vendida', y='Categoria', data=produtos_por_categoria.head(10), hue='Categoria', palette='pastel')

      #Adicionando rótulos às barras:

            for p in ax.patches:
                ax.annotate(f'{p.get_width():,.0f}', 
                            (p.get_width() + 500, p.get_y() + p.get_height() / 2), 
                            ha='left', va='center', 
                            fontsize=10, color='black', 
                            xytext=(10, 0), 
                            textcoords='offset points')

            plt.title('Top 10 Categorias Mais Vendidas', fontsize=16)
            plt.xlabel('Quantidade Vendida', fontsize=12)
            plt.ylabel('Categoria', fontsize=12)
            plt.show()

![Grafico3](https://github.com/CarolyneS14/on33-python-s14-analise-de-dados/blob/main/Carolyne-Oliveira/para-casa/Graficos/Grafico3.png)

6 - Média Estadual de Valor Gasto por Clientes

      #Verificar a média:

            media_por_estado = df_vendas_olist.groupby('customer_state')['price'].mean().reset_index()
            media_por_estado.columns = ['Estado', 'Média de Valor Gasto']

      #Ordenando os estados pela maior média de valor gasto:

            media_por_estado = media_por_estado.sort_values(by='Média de Valor Gasto', ascending=False)

      #Selecionando os cinco estados com a maior média de valor gasto:

            top5_estados = media_por_estado.head(5)

      #Plotando o gráfico de barras:

            plt.figure(figsize=(12, 6))
            ax = sns.barplot(x='Estado', y='Média de Valor Gasto', data=top5_estados, hue='Média de Valor Gasto', palette='pastel', legend=False)

      #Adicionando rótulos às barras:

            for p in ax.patches:
                ax.annotate(f'{p.get_height():,.2f}', 
                            (p.get_x() + p.get_width() / 2, p.get_height()), 
                            ha='center', va='bottom', 
                            fontsize=10, color='black', 
                            xytext=(0, 5), 
                            textcoords='offset points')

            plt.title('Top 5 Estados com Maior Média de Valor Gasto por Cliente', fontsize=16)
            plt.xlabel('Estado', fontsize=12)
            plt.ylabel('Média de Valor Gasto (R$)', fontsize=12)
            plt.show()

![grafico4](https://github.com/CarolyneS14/on33-python-s14-analise-de-dados/blob/main/Carolyne-Oliveira/para-casa/Graficos/Grafico4.png)

7 - Categoria mais Lucrativa

      #Agrupando os produtos por categoria e somando o preço total por categoria:

            preco_por_categoria = df_vendas_olist.groupby('product_category_name')['price'].sum().reset_index()
            preco_por_categoria.columns = ['Categoria', 'Preço Total']

      #Ordenando as categorias pelo preço total (decrescente) e selecionando as 10 principais:

            preco_por_categoria = preco_por_categoria.sort_values(by='Preço Total', ascending=False).head(10)

      #Plotando o gráfico de barras horizontais:

            plt.figure(figsize=(12, 6))
            ax = sns.barplot(x='Preço Total', y='Categoria', data=preco_por_categoria, hue='Preço Total', palette='pastel', legend=False)

      #Adicionando rótulos às barras:

            for p in ax.patches:
                ax.annotate(f'R$ {p.get_width():,.2f}', 
                            (p.get_width(), p.get_y() + p.get_height() / 2), 
                            ha='left', va='center', 
                            fontsize=10, color='black', 
                            xytext=(5, 0), 
                            textcoords='offset points')

      #Título e rótulos dos eixos:

            plt.title('Top 10 Categorias com Maior Lucro', fontsize=16)
            plt.xlabel('Preço Total (R$)', fontsize=12)
            plt.ylabel('Categoria', fontsize=12)

            #Exibindo o gráfico:

            plt.show()

![grafico5](https://github.com/CarolyneS14/on33-python-s14-analise-de-dados/blob/main/Carolyne-Oliveira/para-casa/Graficos/grafico5.png)

8 - Media de Vendas por Estado

      #Verificar a média:

            media_por_estado = df_vendas_olist.groupby('seller_state')['price'].mean().reset_index()
            media_por_estado.columns = ['Estado', 'Média de Venda']

      #Ordenando os produtos pelo maior valor:

            media_por_estado = media_por_estado.sort_values(by='Média de Venda', ascending=False)

      #Selecionando os cinco estados com a maior média de valor gasto:

            top5_estados = media_por_estado.head(5)

      #Plotando o gráfico de barras:

            plt.figure(figsize=(12, 6))
            ax = sns.barplot(x='Estado', y='Média de Venda', data=top5_estados, hue='Média de Venda', palette='pastel', legend=False)

      #Adicionando rótulos às barras:

            for p in ax.patches:
                ax.annotate(f'{p.get_height():,.2f}', 
                            (p.get_x() + p.get_width() / 2, p.get_height()), 
                            ha='center', va='bottom', 
                            fontsize=10, color='black', 
                            xytext=(0, 5), 
                            textcoords='offset points')

            plt.title('Top 5 Estados com Maior Média de Vendas', fontsize=16)
            plt.xlabel('Estado', fontsize=12)
            plt.ylabel('Média de Venda (R$)', fontsize=12)
            plt.show()

![grafico6](https://github.com/CarolyneS14/on33-python-s14-analise-de-dados/blob/main/Carolyne-Oliveira/para-casa/Graficos/Grafico6.png)

 ### - Conclusão:

🌟 Com base nas análises realizadas, podemos concluir o seguinte:

1. **Valor das Compras e Frete**:
   A média do valor das compras (R$ 119,98) e do frete (R$ 19,95) revela que o frete representa cerca de 17% do total pago pelos clientes. Essa informação é relevante, especialmente em regiões sensíveis ao preço final.

2. **Sazonalidade de Vendas**:
   Embora não possamos identificar um padrão sazonal claro devido à falta de dados completos, é crucial coletar informações mais consistentes para análises precisas.

3. **Prazo de Entrega**:
   A alta taxa de entregas atrasadas é preocupante. Melhorias na logística são essenciais para a satisfação dos clientes.

4. **Distribuição por Estado**:
   São Paulo, Rio de Janeiro e Minas Gerais concentram clientes e vendedores. Esses estados são os principais centros de comércio no Brasil.

5. **Categorias Mais Vendidas**:
   Produtos para lar, cuidados pessoais e lazer são os mais demandados.

6. **Média de Gasto por Estado**:
   Paraíba, Alagoas e Acre têm maiores valores médios de gasto por cliente.

7. **Categorias Lucrativas**:
   "Beleza e Saúde" e "Relógios e Presentes" são áreas rentáveis.

8. **Desempenho por Estado**:
   Bahia e Paraíba têm as maiores médias de vendas, indicando força de mercado.

Esses insights combinados podem orientar estratégias de crescimento, abrangendo otimização logística, foco em regiões estratégicas e categorias de maior retorno financeiro. 🚀📊           

## 👩🏻‍🏫 Professora Patrícia Bongiovanni Catandi.
[GitHub](https://github.com/patriciacatandi "Patricia Catandi")
<br/>
[Linkedin](https://www.linkedin.com/in/patr%C3%ADcia-bongiovanni-catandi-13650ba1)
