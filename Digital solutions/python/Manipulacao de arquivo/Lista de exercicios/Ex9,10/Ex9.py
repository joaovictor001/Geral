import pandas as pd
Conteudo = {'Nome': ['João', 'Mariana'],'Matematica':[10,7],'Portugues':[10,8],}

df = pd.DataFrame(Conteudo)

nome_arquivo = "notas.xlsx"

df.to_excel(nome_arquivo, index=False)
print("arquivos adicionados")