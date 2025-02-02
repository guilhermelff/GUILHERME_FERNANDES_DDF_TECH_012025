import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import openai
import base64

def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512",
        response_format='b64_json'
    )
    return response['data'][0]['b64_json']

def plot_image(b64_image_data):
    image_data = base64.b64encode(b64_image_data)

    image = Image.open(io.BytesIO(image_data))
    plt.imshow(image)
    plt.axis('off')
    plt.show()

# Título do aplicativo
st.title("Meu Data App com Streamlit")

# Seção para upload do arquivo CSV
st.header("Carregar arquivo CSV")
uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")

if uploaded_file is not None:
    # Leitura do CSV
    df = pd.read_csv(uploaded_file)
    
    # Exibir as primeiras linhas do DataFrame
    st.subheader("Visualização dos Dados")
    st.write(df.head())
    
    # Exibir informações estatísticas
    st.subheader("Estatísticas Descritivas")
    st.write(df.describe())
    
    # Listar colunas disponíveis
    st.subheader("Colunas Disponíveis")
    st.write(df.columns.tolist())

    # Gerar prompts para carrossel de imagens (se colunas existirem)
    if 'Product Name' in df.columns and 'Features' in df.columns:
        st.subheader("🧩 Apresentações dos produtos")
        
        # Gerar um prompt para cada produto
        for index, row in df.iterrows():
            product_name = str(row['Product Name'])
            features = str(row['Features'])
            
            # Construir o prompt combinando as informações
            prompt = (
                f"Crie um carrossel de imagens para o produto '{product_name}' que destaque: "
                f"{features}. Use elementos visuais atraentes e cores vibrantes que representem "
                "as características principais do produto."
            )

            b64 = generate_image(prompt)
            
            # Exibir o prompt em um container estilizado
            with st.container():
                st.markdown(f"**{product_name}:**")

                plot_image(b64)

                st.markdown("---")
    else:
        st.warning("⚠️ Colunas 'Product Name' ou 'Features' não encontradas para geração de prompts")

    # Verificar colunas numéricas para plotar um histograma
    numeric_columns = df.select_dtypes(include=['float', 'int']).columns.tolist()
    
    if numeric_columns:
        # Seleção da coluna numérica
        coluna = st.selectbox("Selecione uma coluna numérica para plotar um histograma", numeric_columns)
        
        # Criação do histograma
        fig, ax = plt.subplots()
        ax.hist(df[coluna].dropna(), bins=20, color="blue", alpha=0.7)
        ax.set_title(f"Histograma da coluna {coluna}")
        ax.set_xlabel(coluna)
        ax.set_ylabel("Frequência")
        
        # Exibir o gráfico no Streamlit
        st.pyplot(fig)
    else:
        st.write("Não há colunas numéricas disponíveis para plotar o histograma.")