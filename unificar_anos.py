import os
import pandas as pd

# Caminho do diretório contendo os arquivos txt
diretorio = r'C:/Diretorio/...'
dados = []


for arquivo in sorted(os.listdir(diretorio)):
    if arquivo.endswith('.txt'):
        caminho_arquivo = os.path.join(diretorio, arquivo)
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read()
            dados.append(conteudo)

conteudo_unificado = '\n'.join(dados)

with open('temp_unificado.txt', 'w', encoding='utf-8') as f:
    f.write(conteudo_unificado)

df = pd.read_csv('temp_unificado.txt', delimiter='\t') 
df.to_csv('dados_unificados.csv', index=False, encoding='utf-8')