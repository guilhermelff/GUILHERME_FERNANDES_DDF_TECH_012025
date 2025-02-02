import pandas as pd
from faker import Faker
import random
from datetime import datetime

# Configurações iniciais
fake = Faker('pt_BR')  # Gerar dados em português
random.seed(42)  # Para resultados reproduzíveis

# Definir parâmetros
NUM_REGISTROS = 200000
DEPARTAMENTOS = ['vendas', 'marketing', 'TI']
CARGOS = ['junior', 'pleno', 'senior']

METAS_VENDAS = {'vendas': 5000,
                'satisfacao_cliente': 4,
                'valor_gerado_reais': 500000}

METAS_MARKETING = {'roi_por_real_investido': 4,
                   'porcentagem_aumento_trafego': 20,
                   'porcentagem_reducao_cac': 15}

METAS_TI = {'tickets_resolvidos': 200, 
            'tickets_resolvidos_no_prazo': 200, 
            'tempo_medio_atendimento_minutos': 60, 
            'porcentagem_reducao_custos': 10,
            'porcentagem_aumento_conversao_apos_melhorias': 5,
            'max_bugs_criticos': 5}

# Gerar dados

# Gerando a lista com os nomes das chaves
chaves_metas_vendas = list(METAS_VENDAS.keys())
chaves_metas_marketing = list(METAS_MARKETING.keys())
chaves_metas_ti = list(METAS_TI.keys())

# Juntando todas as listas em uma única lista
coluna_nomes = chaves_metas_vendas + chaves_metas_marketing + chaves_metas_ti

coluna = {nome:0 for nome in coluna_nomes}

print(coluna['tickets_resolvidos'])