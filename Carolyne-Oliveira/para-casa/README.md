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

## 🟦 Análise exploratória

 ### - Coleta:

            #Importando a base de dados diretamente do Github
            url_pedidos = "https://raw.githubusercontent.com/CarolyneS14/on33-python-s14-analise-de-dados/main/material/dados/olist_orders_dataset.csv"

            #Transformando a base em um DataFrame
            df_pedidos = pd.read_csv(url_pedidos)

            #Visualizando o DataFrame(df)
            df_pedidos

            #Visualizando o DataFrame(df)
            df_itens_pedido

            #Visualizando o DataFrame(df)
            df_consumidor

            #Visualizando o DataFrame(df)
            df_vendedor

            #Visualizando o DataFrame(df)
            df_produtos


 ### - Limpeza:

            #Estatísticas descritivas sobre o DataFrame
            df_pedidos.describe(include='all')

## 👩🏻‍🏫 Professora Patrícia Bongiovanni Catandi.
[GitHub](https://github.com/patriciacatandi "Patricia Catandi")
/n
[Linkedin](https://www.linkedin.com/in/patr%C3%ADcia-bongiovanni-catandi-13650ba1)
