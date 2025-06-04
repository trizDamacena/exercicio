import pandas as pd

dataframe = pd.read_excel("C:/Users/beatr/PycharmProjects/Lista_ManipulacaoArquivos/historico_pedidos.xlsx", engine='openpyxl')

dataframe.to_csv("arquivo_pedido.csv", index=False)