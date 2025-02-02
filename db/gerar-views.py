import pandas as pd

CAMINHO_DB = "db/desempenho_funcionarios.csv"

df_db = pd.read_csv(CAMINHO_DB)

def gerar_view(dataframe, coluna_filtro, valor_filtro):
    df_filtrado = dataframe[dataframe[coluna_filtro] == valor_filtro]
    df_filtrado.to_csv(f"db/view_{valor_filtro}_{CAMINHO_DB.replace('db/', '')}", index=False)
    return df_filtrado

df_filtrado = gerar_view(df_db, "Departamento", "marketing")


