import pandas as pd
import glob
import os

directory_path = "r/diretorio_x/2021_a_2023_movimentacoes"
csv_pattern = os.path.join(directory_path, "*.csv")
csv_files = glob.glob(csv_pattern)
dataframes = [pd.read_csv(file) for file in csv_files]
combined_df = pd.concat(dataframes, ignore_index=True)
print(combined_df)

# Salvar df combinado 
output_file = "dados_anac.csv"
combined_df.to_csv(output_file, index=False)
