import pandas as pd
Conteudo = {'Notas':[10,9,8,7,6,5,4,4,2,1]}

df = pd.DataFrame(Conteudo)

nome_arquivo = "notas.xlsx"


df.to_excel(nome_arquivo, index=False)
print("arquivos adicionados")