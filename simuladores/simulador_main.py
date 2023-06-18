import pandas as pd

from simulador_cenario_fila_unica import cenario_fila_unica
from simulador_cenario_multiplos_workers import cenario_multiplos_workers
from simulador_cenario_dois_workers_e_filas import cenario_multiplos_workers

data = pd.read_csv('./tc.txt')
data['ts'] = pd.read_csv('./ts.txt')
data.rename(columns={'x': 'tc', 'ts': 'ts'}, inplace=True)
data = data[data['ts'] < 15].head(200)
data = data.values.tolist()

# cenario_multiplos_workers(data,2)
# cenario_fila_unica(data)
cenario_multiplos_workers(data)