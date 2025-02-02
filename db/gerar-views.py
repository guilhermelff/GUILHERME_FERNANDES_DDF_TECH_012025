import pandas as pd

CAMINHO_DB = "db/view_vendas_desempenho_funcionarios.csv"

df_db = pd.read_csv(CAMINHO_DB)

def gerar_view(dataframe, coluna_filtro, valor_filtro):
    df_filtrado = dataframe[dataframe[coluna_filtro] == valor_filtro]

    colunas_para_remover = (df_filtrado == 0).all()

    # Filtra as colunas para remover
    colunas_para_remover = colunas_para_remover[colunas_para_remover].index

    # Remove as colunas identificadas do DataFrame
    df_filtrado = df_filtrado.drop(columns=colunas_para_remover)

    df_filtrado.to_csv(f"db/{valor_filtro}_{CAMINHO_DB.replace('db/', '')}", index=False)
    return df_filtrado

for i in ["junior", "pleno", "senior"]:

    df_filtrado = gerar_view(df_db, "Cargo", i)


