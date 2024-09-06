# ETL Olist

Este projeto realiza a extração, transformação e carregamento (ETL) dos dados da Olist, uma plataforma de e-commerce brasileira. O objetivo é preparar os dados para análises e visualizações, facilitando a tomada de decisões estratégicas.

## Descrição

O notebook `ETL_Olist.ipynb` contém o processo completo de ETL, desde a leitura dos dados brutos até a criação de um dataset limpo e estruturado. As etapas principais incluem:

1. **Extração**: Leitura dos dados das diferentes tabelas fornecidas pela Olist.
2. **Transformação**: Limpeza e transformação dos dados, incluindo tratamento de valores ausentes, conversão de tipos de dados e criação de novas colunas.
3. **Carregamento**: Armazenamento dos dados transformados em um formato adequado para análises posteriores.

## Estrutura do Projeto

- `ETL_Olist.ipynb`: Notebook Jupyter contendo todo o processo de ETL.
- `data/`: Diretório contendo os arquivos de dados brutos (não incluídos no repositório).
- `output/`: Diretório onde os dados transformados são salvos.

### Datasets utilizados nesta análise:
```
olist_sellers_dataset.csv
olist_order_payments_dataset.csv
olist_order_items_dataset.csv
olist_products_dataset.csv
```

## Dependências

Para executar este projeto, você precisará das seguintes bibliotecas Python:

- pandas
- numpy
- matplotlib
- seaborn

## Como Usar

1. Clone este repositório para sua máquina local:
2. Navegue até o diretório do projeto:
3. Coloque os arquivos de dados brutos no diretório `data/`.
4. Abra o notebook `ETL_Olist.ipynb` e execute todas as células para realizar o processo de ETL.

### Lidando com Erros

Para correções de erros apontadas pelos códigos, aperfeiçoamento da execução e melhor estilo dos gráficos foram feitas consultas às IAs Copilot, GhatGPT, Gemini e Perplexity.

## Contribuições

Contribuições e sugestões são bem-vindas!