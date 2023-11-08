import pandas as pd 
nome_arquivo  = "notas.xlsx"
ver = pd.read_excel(nome_arquivo)
print(ver)