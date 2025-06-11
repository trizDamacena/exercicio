import pandas as pd

historico_pedidos = [
    {
        'ID': 1, 
        'Nome': 'João',
        'Endereço': 'Rua Flores, 123',
        'Produto': 'Camiseta',
        'Quantidade': 2,
        'Preço': 50,
        'Data': '01/01/2023'
    },

    {
        'ID': 2, 
        'Nome': 'Maria',
        'Endereço': 'Avenida Central, 456',
        'Produto': 'Tênis',
        'Quantidade': 1,
        'Preço': 120,
        'Data': '02/01/2023'
    },

    {
        'ID': 3, 
        'Nome': 'Carlos',
        'Endereço': 'Praça Estação, 789',
        'Produto': 'Mochila',
        'Quantidade': 1,
        'Preço': 80,
        'Data': '03/01/2023'
    },

    {
        'ID': 4, 
        'Nome': 'Fernanda',
        'Endereço': 'Alameda dos Anjos, 101',
        'Produto': 'Relógio',
        'Quantidade': 1,
        'Preço': 150,
        'Data': '04/01/2023'
    },

]

df = pd.DataFrame.from_dict(historico_pedidos)
df.to_excel("historico_pedidos.xlsx", index=False)