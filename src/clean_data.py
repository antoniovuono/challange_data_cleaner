import pandas as pd

# 🔹 Etapa 1: Leitura do arquivo

data_path = "data/vendas_ficticias.csv"
df = pd.read_csv(data_path)

print(df)

# 🔹 Etapa 2: Diagnóstico e limpeza

print("\n🔍 Diagnóstico inicial:")
print(df.info())
print("\nValores nulos por coluna:")
print(df.isnull().sum())
print("\nduplicados:", df.duplicated().sum())

# 2.1 Limpeza
df = df.drop_duplicates()
df["quantidade"] = pd.to_numeric(df['quantidade'], errors="coerce")
df["preco_unitario"] = pd.to_numeric(df['preco_unitario'], errors="coerce")
df = df.dropna(subset=["produto", "quantidade", "preco_unitario","data", "vendedor"])
df = df[df["preco_unitario"] > 0]

# 🔹 Etapa 3: Análise e estatísticas

# Descubra o valor total em vendas:
df["valor_total"] = df["quantidade"] * df["preco_unitario"]
print(f"\n Valor total de vendas: {df["valor_total"].sum():,.2f}")

print("\n Produto mais vendido:")
print(df.groupby("produto")["quantidade"].sum().sort_values(ascending=False).head(1))
