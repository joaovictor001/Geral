import pandas as pd
historico_pedidos = {
    'ID': [1, 2, 3, 4],
    'Nome': ['João', 'Mariana', 'Carlos', 'Fernanda'],
    'Endereço': ['Rua das Flores, 123', 'Avenida Central, 456', 'Praça da Estação, 789', 'Alameda dos Anjos, 101'],
    'Produto': ['Camiseta', 'Tênis', 'Mochila', 'Relógio'],
    'Quantidade': [2, 1, 1, 1],
    'Preço': [50, 120, 80, 150],
    'Data': ['01/01/2023', '02/01/2023', '03/01/2023', '04/01/2023']
}

df = pd.DataFrame(historico_pedidos)
nome_do_arquivo = "loja.xlsx"
df.to_excel(nome_do_arquivo, index=False)

