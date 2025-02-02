import pandas as pd
from faker import Faker
import random
from datetime import datetime

# Configurações iniciais
fake = Faker('pt_BR')  # Gerar dados em português
random.seed(42)  # Para resultados reproduzíveis

# Parâmetros
ANO_INICIO = 2015
ANO_FIM = 2023
NUM_REGISTROS = 200000
DEPARTAMENTOS = ['vendas', 'marketing', 'TI']
CARGOS = ['junior', 'pleno', 'senior']
AUMENTO_PLENO = 1.1
AUMENTO_SENIOR = 1.5

LIMITE_INF_VENDAS = 0
LIMITE_SUP_VENDAS = 10000
LIMITE_INF_SATISFACAO = 0
LIMITE_SUP_SATISFACAO = 5
LIMITE_INF_VALOR_GERADO_REAIS = 0
LIMITE_SUP_VALOR_GERADO_REAIS = 1000000
LIMITE_INF_ROI = 0
LIMITE_SUP_ROI = 7
LIMITE_INF_AUMENTO_TRAFEGO = 0
LIMITE_SUP_AUMENTO_TRAFEGO = 30
LIMITE_INF_CAC = 0
LIMITE_SUP_CAC = 25
LIMITE_INF_TICKETS = 0
LIMITE_SUP_TICKETS = 300
LIMITE_INF_TICKETS_PRAZO = 0
LIMITE_SUP_TICKETS_PRAZO = 300
LIMITE_INF_TEMPO_ATEND = 0
LIMITE_SUP_TEMPO_ATEND = 90
LIMITE_INF_RED_CUSTOS = 0
LIMITE_SUP_RED_CUSTOS = 15
LIMITE_INF_CONV_MELHORIA = 0
LIMITE_SUP_CONV_MELHORIA = 15
LIMITE_INF_CRIT_BUGS = 0
LIMITE_SUP_CRIT_BUGS = 10

METAS_VENDAS = {'vendas': 5000,
                'satisfacao_cliente': 4,
                'valor_gerado_reais': 500000}

METAS_MARKETING = {'roi_por_real_investido': 4,
                   'porcentagem_aumento_trafego': 20,
                   'porcentagem_reducao_cac': 15} # custo aquisicao cliente

METAS_TI = {'tickets_resolvidos': 200, 
            'tickets_resolvidos_no_prazo': 200, 
            'tempo_medio_atendimento_minutos': 60, 
            'porcentagem_reducao_custos': 10,
            'porcentagem_aumento_conversao_apos_melhorias': 5,
            'max_bugs_criticos': 5}

# Função para gerar datas de contratação
def data_contratacao():
    start_date = datetime(ANO_INICIO, 1, 1)
    end_date = datetime(ANO_FIM, 12, 31)
    return fake.date_between(start_date=start_date, end_date=end_date)

def aumento_cargo(valor:float, cargo:str) -> float:
     if cargo == 'junior':
         return valor
     elif cargo == 'pleno': 
        return valor * AUMENTO_PLENO
     elif cargo =='senior':
        return valor * AUMENTO_SENIOR
     else:
        raise ValueError("Cargo não existente")

# Gerar dados

# Gerando a lista com os nomes das chaves
chaves_metas_vendas = list(METAS_VENDAS.keys())
chaves_metas_marketing = list(METAS_MARKETING.keys())
chaves_metas_ti = list(METAS_TI.keys())

# Juntando todos os nomes das metas em uma única lista
coluna_nomes_metas = chaves_metas_vendas + chaves_metas_marketing + chaves_metas_ti

dados = []

for _ in range(NUM_REGISTROS):
    departamento = random.choice(DEPARTAMENTOS)
    cargo = random.choice(CARGOS)
    data_contrato = data_contratacao()

    #colunas relacionadas as metas
    coluna = {nome:0.0 for nome in coluna_nomes_metas} 
    
    # Gerar métricas de desempenho baseadas no departamento
    match departamento:
        case 'vendas':
            coluna['vendas'] = int(aumento_cargo(round(random.uniform(LIMITE_INF_VENDAS, LIMITE_SUP_VENDAS), 0), cargo))

            coluna['satisfacao_cliente'] = aumento_cargo(round(random.uniform(LIMITE_INF_SATISFACAO, LIMITE_SUP_SATISFACAO), 2), cargo)
            if coluna['satisfacao_cliente'] > LIMITE_SUP_SATISFACAO:
                coluna['satisfacao_cliente'] = LIMITE_SUP_SATISFACAO

            coluna['valor_gerado_reais'] = aumento_cargo(round(random.uniform(LIMITE_INF_VALOR_GERADO_REAIS, LIMITE_SUP_VALOR_GERADO_REAIS), 2), cargo)

        case 'marketing':
            coluna['roi_por_real_investido'] = aumento_cargo(round(random.uniform(LIMITE_INF_ROI, LIMITE_SUP_ROI), 2), cargo)
            coluna['porcentagem_aumento_trafego'] = aumento_cargo(round(random.uniform(LIMITE_INF_AUMENTO_TRAFEGO, LIMITE_SUP_AUMENTO_TRAFEGO), 2), cargo)
            coluna['porcentagem_reducao_cac'] = aumento_cargo(round(random.uniform(LIMITE_INF_CAC, LIMITE_SUP_CAC), 2), cargo)

        case 'TI':
            coluna['tickets_resolvidos'] = int(aumento_cargo(round(random.uniform(LIMITE_INF_TICKETS, LIMITE_SUP_TICKETS), 0), cargo))
            coluna['tickets_resolvidos_no_prazo'] = int(aumento_cargo(round(random.uniform(LIMITE_INF_TICKETS_PRAZO, LIMITE_SUP_TICKETS_PRAZO), 0), cargo))
            coluna['tempo_medio_atendimento_minutos'] = int(aumento_cargo(round(random.uniform(LIMITE_INF_TEMPO_ATEND, LIMITE_SUP_TEMPO_ATEND), 0), cargo))
            coluna['porcentagem_reducao_custos'] = aumento_cargo(round(random.uniform(LIMITE_INF_RED_CUSTOS, LIMITE_SUP_RED_CUSTOS), 2), cargo)
            coluna['porcentagem_aumento_conversao_apos_melhorias'] = aumento_cargo(round(random.uniform(LIMITE_INF_CONV_MELHORIA, LIMITE_SUP_CONV_MELHORIA), 2), cargo)
            coluna['max_bugs_criticos'] = int(aumento_cargo(round(random.uniform(LIMITE_INF_CRIT_BUGS, LIMITE_SUP_CRIT_BUGS), 0), cargo))


    funcionario = {
        'ID_Funcionario': fake.unique.random_number(digits=6),
        'Nome': fake.name(),
        'Departamento': departamento,
        'Cargo': cargo,
        'Data_Contratacao': data_contrato.strftime('%Y-%m-%d'),
        'Treinamentos_Completos': random.randint(1, 15),
        'Vendas': coluna['vendas'],
        'Satisfacao_Cliente': coluna['satisfacao_cliente'],
        'Valor_Gerado_Reais': coluna['valor_gerado_reais'],
        'ROI_Por_Real_Investido': coluna['roi_por_real_investido'],
        'Porcentagem_Aumento_Trafego': coluna['porcentagem_aumento_trafego'],
        'Porcentagem_Reducao_CAC': coluna['porcentagem_reducao_cac'],
        'Tickets_Resolvidos': coluna['tickets_resolvidos'],
        'Tickets_Resolvidos_No_Prazo': coluna['tickets_resolvidos_no_prazo'],
        'Tempo_Medio_Atendimento_Minutos': coluna['tempo_medio_atendimento_minutos'],
        'Porcentagem_Reducao_Custos': coluna['porcentagem_reducao_custos'],
        'Porcentagem_Aumento_Conversao_Apos_Melhorias': coluna['porcentagem_aumento_conversao_apos_melhorias'],
        'Max_Bugs_Criticos': coluna['max_bugs_criticos']
    }

    dados.append(funcionario)

    print(f"Registros inseridos: {_ + 1}/200000", end="\r")

# Criar DataFrame
df = pd.DataFrame(dados)

# Salvar em CSV
df.to_csv('db/desempenho_funcionarios.csv', index=False, encoding='utf-8-sig')

print(f"Base de dados com {NUM_REGISTROS} registros criada com sucesso!")