# Projeto: Análise da Relação entre Orçamento e Qualidade em Filmes de Ação

Este projeto teve como objetivo analisar a relação entre orçamento, popularidade e qualidade em filmes de ação, utilizando dados do TMDB (The Movie Database). A análise foi conduzida em 5 sprints, cada uma com etapas específicas de ingestão, processamento e visualização de dados.

## Principais Perguntas Respondidas

- Filmes de alto orçamento são realmente melhores avaliados?

- Como filmes de baixo orçamento conseguem boas avaliações?

- Existe correlação entre orçamento, popularidade e qualidade?

- Como a evolução do orçamento impactou a receita e a popularidade ao longo das décadas?

## Sprints

### 📌 Sprint 1: Ingestão de Dados CSV no S3
Objetivo: Carregar arquivos movies.csv e series.csv em um bucket S3 usando um script Python em um contêiner Docker.

Principais etapas:

✅ Criação do bucket S3

✅ Desenvolvimento do script Python (boto3) para upload dos arquivos

✅ Configuração do Dockerfile para execução do script

✅ Upload dos dados no formato raw/YYYY/MM/DD/

### 📌 Sprint 2: Coleta de Dados via API TMDB (AWS Lambda)
Objetivo: Coletar dados adicionais do TMDB via AWS Lambda e armazená-los no S3 como JSON.

Principais etapas:

✅ Criação de uma função Lambda para chamar a API TMDB

✅ Extração de dados de filmes populares, mais bem avaliados e em cartaz

✅ Armazenamento dos JSONs no bucket (raw/tmdb/YYYY/MM/DD/)

✅ Tratamento de credenciais e permissões (IAM)

### 📌 Sprint 3: Processamento com AWS Glue e Modelagem em Parquet
Objetivo: Transformar os dados da camada Raw para Trusted usando AWS Glue (Spark).

Principais etapas:

✅ Criação de jobs no Glue para processar CSV e JSON

✅ Conversão dos dados para Parquet (otimizado para consultas)

✅ Particionamento por data (trusted/YYYY/MM/DD/)

✅ Criação de tabelas no Athena via Crawlers

### 📌 Sprint 4: Modelagem Dimensional (Staging → Refined)
Objetivo: Criar um modelo dimensional (Star Schema) na camada Refined.

Principais etapas:

✅ Unificação dos dados CSV + JSON em uma tabela staging

✅ Criação de dimensões (dim_filme, dim_tempo, dim_popularidade)

✅ Construção da tabela fato (fato_filmes) com métricas-chave

✅ Ajustes de tipos de dados e tratamento de nulos

### 📌 Sprint 05: Dashboard no Amazon QuickSight

Objetivo: Criar visualizações para análise dos dados refinados.

Principais insights:

- Filmes de baixo orçamento podem ter avaliações melhores que os de alto orçamento

- Popularidade não está diretamente ligada à qualidade

- Orçamentos aumentaram após os anos 2000, mas avaliações não acompanharam

- Franquias dominam o mercado, mas filmes independentes também se destacam

## Visualizações criadas:


![imagem_dashboard](https://github.com/heitorkobayashi/action-movies-tmdb-analysis/blob/main/Sprint%2005/evidencias/14_dashboard.png)


## Tecnologias Utilizadas

- AWS (S3, Lambda, Glue, Athena, QuickSight)

- Python (boto3, PySpark)

- Docker

- TMDB API