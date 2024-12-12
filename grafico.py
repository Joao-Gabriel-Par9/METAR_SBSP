import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

df = pd.read_csv('replica1.csv')
total_linhas = df.shape[0]

#Variável de análise
contagem = df['WEATHER'].value_counts()

contagem = contagem.sort_index(ascending=False)
porcentagem = (contagem / total_linhas) * 100
fig, ax = plt.subplots(figsize=(10, 6))
contagem.plot(kind='bar', color='#90EE90', ax=ax)

# Adicionando rótulos de porcentagem acima de cada barra
##for i, (termo, valor) in enumerate(contagem.items()):
    ##ax.text(i, valor + 0.05 * max(contagem), f"{porcentagem[termo]:.4f}%", ha='center', fontsize=9, color='black', fontweight='bold')

ax.set_title('Distribuição das Condições Meteorológicas com RVR igual ou abaixo do 2000m (SBSP)', fontsize=14, fontweight='bold')
ax.set_xlabel('Condições Meteorológicas', fontsize=12, fontweight='bold')
ax.set_ylabel('Frequência (em dados de Metar)', fontsize=12, fontweight='bold')
ax.grid(False)
ax.tick_params(axis='x', rotation=45, labelsize=10)
ax.tick_params(axis='y', labelsize=10)
ax.set_ylim(0, max(contagem) * 1.1)

# Configurando o eixo y para usar apenas números inteiros
ax.yaxis.set_major_locator(MaxNLocator(integer=True))

# Adicionando uma borda ao redor das barras para melhor contraste
for bar in ax.patches:
    bar.set_edgecolor('black')
    bar.set_linewidth(1)

plt.tight_layout()
plt.show()
print(contagem)
