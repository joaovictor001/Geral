import pandas as pd
import json
nome_arquivo = "convertido.csv"
df = pd.read_csv(nome_arquivo)
dados_json = df.to_dict(orient='records')
novo_arquivo = "arquivo_em_json.json"
with open("arquivo_em_json.json", "w", encoding="utf-8") as myfile:
    json.dump(dados_json, myfile, ensure_ascii=False, indent=4)