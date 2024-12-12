import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

df_5anos = pd.read_csv('SBSP_base_de_dados_corrigida.csv')  # Dados de 5 anos
df_1ano = pd.read_csv('1_ano_SBSP.csv')   # Dados de 1 ano

contagem_5anos = df_5anos['WEATHER'].value_counts().sort_index(ascending=False)
contagem_1ano = df_1ano['WEATHER'].value_counts().sort_index(ascending=False)

total_5anos = df_5anos.shape[0]
total_1ano = df_1ano.shape[0]

# Calculando porcentagens para cada período
porcentagem_5anos = (contagem_5anos / total_5anos) * 100
porcentagem_1ano = (contagem_1ano / total_1ano) * 100

# Unindo os índices para garantir que ambos os períodos tenham os mesmos valores para comparação
indices = porcentagem_5anos.index.union(porcentagem_1ano.index)
porcentagem_5anos = porcentagem_5anos.reindex(indices, fill_value=0)
porcentagem_1ano = porcentagem_1ano.reindex(indices, fill_value=0)
diferenca_percentual = porcentagem_1ano - porcentagem_5anos
media_diferenca_percentual = abs(diferenca_percentual).mean()


fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.35
x = range(len(indices))
ax.bar(x, porcentagem_5anos, width=bar_width, label='5 anos', color='#FFA85B', edgecolor='black', linewidth=1)
ax.bar([i + bar_width for i in x], porcentagem_1ano, width=bar_width, label='1 ano', color='#87CEFA', edgecolor='black', linewidth=1)
ax.set_title('Comparação da Distribuição da Direção do Vento (SBSP)', fontsize=14, fontweight='bold')
ax.set_xlabel('Direção do Vento', fontsize=12, fontweight='bold')
ax.set_ylabel('Porcentagem (%)', fontsize=12, fontweight='bold')
ax.set_xticks([i + bar_width / 2 for i in x])
ax.set_xticklabels(indices, rotation=45, fontsize=10)
ax.legend()

# Adicionando valores de diferença percentual acima das barras
for i, index in enumerate(indices):
    diff = diferenca_percentual[index]
    ax.text(i + bar_width / 2, max(porcentagem_5anos[index], porcentagem_1ano[index]) + 1,
            f"{diff:.2f}%", ha='center', fontsize=9, color='black', fontweight='bold')

# Ajustando os limites do eixo y
ax.set_ylim(0, max(max(porcentagem_5anos), max(porcentagem_1ano)) * 1.2)

# Configurando o eixo y para usar apenas números inteiros
ax.yaxis.set_major_locator(MaxNLocator(integer=True))


plt.tight_layout()
plt.show()

# Exibindo as diferenças percentuais
diferencas = pd.DataFrame({
    '5 anos (%)': porcentagem_5anos,
    '1 ano (%)': porcentagem_1ano,
    'Diferença (%)': diferenca_percentual
})

print(diferencas)
print(f"\nMédia geral da diferença percentual (em módulo): {media_diferenca_percentual:.4f}%")
