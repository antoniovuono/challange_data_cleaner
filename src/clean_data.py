from itertools import groupby
import pandas as pd

# 🔹 Etapa 1: Leitura do arquivo

def load_data(path):
    print("Lê o arquivo CSV e retorna um dataframe")
    df = pd.read_csv(path)
    return df


# 🔹 Etapa 2: Diagnóstico e limpeza

# 2.1 Limpeza
def clean_data(df):
    df = df.drop_duplicates()
    df["quantidade"] = pd.to_numeric(df['quantidade'], errors="coerce")
    df["preco_unitario"] = pd.to_numeric(df['preco_unitario'], errors="coerce")
    df = df.dropna(subset=["produto", "quantidade", "preco_unitario","data", "vendedor"])
    df = df[df["preco_unitario"] > 0]
    df["valor_total"] = df["quantidade"] * df["preco_unitario"]
    return df

# 🔹 Etapa 3: Análise e estatísticas: Relatório

def generate_report(df):
        """Imprime estatísticas úteis sobre os dados"""
        total = df["valor_total"].sum()
        print(f"\n💰 Valor total de vendas: R$ {total:,.2f}")

        print("\n Produto mais vendido:")
        # Agrupa por produtos, pega a coluna quantidade e traz a soma, ordena do maior para o menor e pega o primeiro.
        print(df.groupby("produto")["quantidade"].sum().sort_values(ascending=False).head(1))

        print("\n Vendedor que mais vendeu: ")
        best_seller = df.groupby("vendedor")["valor_total"].sum().sort_values(ascending=False).head(1)
        print(best_seller)

        print("\n Média de preço por produto vendido:")
        # tirar dúvida do mean:
        average_price = df.groupby('produto')['preco_unitario'].mean().sort_values(ascending=False)
        print(average_price)

def export_data_cleaned(df, path):
    df.to_csv(path, index=False)
    print(f"\n📁 Arquivo exportado para: {path}")


# Pipeline principal:

if __name__ == "__main__":
    path = "data/vendas_ficticias.csv"
    export_path = "data/vendas_limpo.csv"

    df = load_data(path)
    df_cleaned = clean_data(df)
    generate_report(df_cleaned)
    export_data_cleaned(df_cleaned, export_path)
