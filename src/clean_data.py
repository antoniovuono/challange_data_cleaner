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
# remvoer duplicatas
df = df.drop_duplicates()
print("Quantidade de itens duplicados:", df.duplicated().sum())

# 6. Gere estatísticas básicas
print("\n📊 Estatísticas descritivas:")
print(df.describe(include='all'))

# Verificar a quantidade de valores nulos por coluna
print("Quantidade de valores nulos")
print(df.isnull().sum())

# Forçar conversão das colunas numéricas:
df["quantidade"] = pd.to_numeric(df["quantidade"], errors="coerce")
df["preco_unitario"] = pd.to_numeric(df["preco_unitario"], errors="coerce")

# Remover linhas com NaN ou preço <= 0:
df = df.dropna(subset=["produto", "quantidade", "preco_unitario", "vendedor"])
df = df[df["preco_unitario"] > 0]

print("\n✅ Dataset após limpeza:")
print(df.info())

# Criar coluna valor total (qunatidade x preço)
df['valor_total'] = df['quantidade'] * df['preco_unitario']
total_vendas = df['valor_total'].sum()
print("O valor total de vendas:", total_vendas)

# Produto mais vendido por quantidade:
produto_mais_vendido = df.groupby("produto")["quantidade"].sum().sort_values(ascending=False)
print("\n📦 Produto mais vendido (por quantidade):")
print(produto_mais_vendido.head(1))
