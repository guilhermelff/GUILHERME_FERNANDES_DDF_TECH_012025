import pandas as pd

# Caminho para o arquivo CSV original
arquivo_csv = "db\desempenho_funcionarios.csv"

# Carregar o arquivo CSV em um DataFrame
df = pd.read_csv(arquivo_csv)

# Definir as colunas que não serão desestruturadas (identificadores e dados básicos)
colunas_identificadoras = [
    "ID_Funcionario",
    "Nome",
    "Departamento",
    "Cargo",
    "Data_Contratacao"
]

# Aplicar o melt para transformar as métricas em linhas separadas
df_desestruturado = df.melt(
    id_vars=colunas_identificadoras,
    var_name="Metrica",
    value_name="Valor"
)

# Exibir as primeiras linhas do DataFrame desestruturado
print(df_desestruturado.head())

# Opcional: Salvar o DataFrame desestruturado em um novo arquivo CSV
df_desestruturado.to_csv("db/desempenho_funcionarios_desestruturado.csv", index=False)
