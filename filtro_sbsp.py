import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv('dados_anac.csv')

# Filtrar apenas pelos outros critérios
filtered_df = df[
    (df['NR_AEROPORTO_REFERENCIA'] == 'SBSP') &
    (df['NR_MOVIMENTO_TIPO'] == 'P')
]

# Calcular o percentual para cada valor de `NR_CABECEIRA`
percent_cabeceira = (
    filtered_df['NR_CABECEIRA']
    .value_counts(normalize=True) * 100
)

# Exibir o resultado
print("Percentual de ocorrências por valor de NR_CABECEIRA:")
print(percent_cabeceira)
