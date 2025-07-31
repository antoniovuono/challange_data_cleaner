import pandas as pd

# 1. Defina um caminho para o arquivo csv que vamos trabalhar
data_path = "data/vendas_ficticias.csv"

# 2. Faça a leitura do arquivo
df = pd.read_csv(data_path)

# 3. Exiba as 5 primeiras linhas para aprender
print("Primeiras linhas do dataset:")
print(df.head())

# 4. Capture informações básicas sobre tipos de dados e nulos
print("Informações do dataframe:")
print(df.info())

# 5. Verifique a quantidade de duplicatas na nossa base de dados
print("Quantidade de itens duplicados:", df.duplicated().sum())

# 6. Gere estatísticas básicas
print("\n📊 Estatísticas descritivas:")
print(df.describe(include='all'))
