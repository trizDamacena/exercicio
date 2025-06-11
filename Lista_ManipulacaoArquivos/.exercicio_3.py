import pandas as pd 

arquivo = './arquivo_pedido.csv'
df = pd.read_csv(arquivo)

print(df.head())

df.to_json('arquivo_Historico.json', orient='records', lines=True)