import pandas as pd
nome_arquivo = "loja.xlsx"
df = pd.read_excel(nome_arquivo)
print(df)
novo_arquivo = "convertido.csv"
df.to_csv(novo_arquivo, index=False, encoding='utf-8')
print("Pronto!!!")