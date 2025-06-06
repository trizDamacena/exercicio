import pandas as pd

dataframe = pd.read_excel("./historico_pedidos.xlsx", engine='openpyxl')

dataframe.to_csv("arquivo_pedido.csv", index=False)