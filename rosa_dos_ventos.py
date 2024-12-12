import pandas as pd
import matplotlib.pyplot as plt
from windrose import WindroseAxes
df = pd.read_csv('SBSP_unique.csv')

# Remover entradas com valores nulos nas colunas 'D' e 'F'
df.dropna(subset=['D', 'F'], inplace=True)

# Encontrar o valor máximo de 'F'
max_F = df['F'].max()

# Definir os intervalos de velocidade do vento para a legenda
bins = [0, 5, 10, 15, 20, 25,30, max_F]

ax = WindroseAxes.from_ax()
ax.bar(df['D'], df['F'], bins=bins, normed=True, opening=0.8, edgecolor='white')
ax.set_legend(title="Velocidade do Vento (KT)", loc='best', fontsize=8)
plt.title('Rosa dos Ventos de SBSP')
plt.show()
