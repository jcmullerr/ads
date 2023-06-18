import pandas as pd
import numpy as np

from simulador_cenario_fila_unica import cenario_fila_unica as fila_unica
from simulador_cenario_multiplos_workers import cenario_multiplos_workers as multiplos_workers
from simulador_cenario_dois_workers_e_filas import cenario_multiplos_workers as dois_workers_e_filas


qt_testes = 5
size = 200 # quantidade de valores gerados padrão=200.
mean = 4.640000 # media
std = 1.990025 # desvio padrao
min = 8
max = 14

for qt in range(qt_testes):

    # gera uma lista de dist. normal com [size] valores a partir de [mean] com desvio padrão de [std].
    tc = np.random.normal(loc=mean, scale=std, size=size)
    tc = [round(x) for x in tc]

    # gera uma lista de dist. linear com [size] valores de [min] ate [max].
    ts = np.random.uniform(low=min, high=max, size=size)
    ts = [round(x) for x in ts]

    cenario = [[tc[x],ts[x]] for x in range(size)]
    print(f"==================== TESTE ALEATORIOS {qt+1} ====================")
    print(f"TEMPOS ALEATORIOS:\n{cenario}")

    filaUnica = fila_unica(cenario,num_instancias=size)
    print(f"\n\nTEMPO MEDIO DE ESPERA FILA UNICA: \n {sum(j for i, j in filaUnica[0])/size}")
    print(f"\nTAMANHO MAXIMO FILA UNICA: \n {filaUnica[1]}")

    doisWorkersFilas = dois_workers_e_filas(cenario,num_instancias=size)
    print(f"\n\nTEMPO MEDIO DE ESPERA FILA DUPLA COM 2 WORKERS: \n {sum(j for i, j in doisWorkersFilas[0])/size}")
    print(f"\nTAMANHO MAXIMO FILA DUPLA COM 2 WORKERS: \n {doisWorkersFilas[1]}")

    multiplosWorkers = multiplos_workers(cenario,num_instancias=size,numero_de_workers=2)
    print(f"\n\nTEMPO MEDIO DE ESPERA FILA UNICA E MULTIPLOS WORKERS: \n {sum(j for i, j in multiplosWorkers[0])/size}")
    print(f"\nTAMANHO MAXIMO  FILA UNICA E MULTIPLOS WORKERS: \n {multiplosWorkers[1]}")

    print("\n")

data = pd.read_csv('../tc.txt')
data['ts'] = pd.read_csv('../ts.txt')
data.rename(columns={'x': 'tc', 'ts': 'ts'}, inplace=True)
data = data[data['ts'] < 15].head(200)
data = data.values.tolist()

print(data)

print(f"==================== TESTE DADOS REAIS {qt+1} ====================")
print(f"TESTE DADOS REAIS:\n{data}")

filaUnica = fila_unica(data,num_instancias=size)
print(f"\n\nTEMPO MEDIO DE ESPERA FILA UNICA: \n {sum(j for i, j in filaUnica[0])/size}")
print(f"\nTAMANHO MAXIMO FILA UNICA: \n {filaUnica[1]}")

doisWorkersFilas = dois_workers_e_filas(data,num_instancias=size)
print(f"\n\nTEMPO MEDIO DE ESPERA FILA DUPLA COM 2 WORKERS: \n {sum(j for i, j in doisWorkersFilas[0])/size}")
print(f"\nTAMANHO MAXIMO FILA DUPLA COM 2 WORKERS: \n {doisWorkersFilas[1]}")

multiplosWorkers = multiplos_workers(data,num_instancias=size,numero_de_workers=2)
print(f"\n\nTEMPO MEDIO DE ESPERA FILA UNICA E MULTIPLOS WORKERS: \n {sum(j for i, j in multiplosWorkers[0])/size}")
print(f"\nTAMANHO MAXIMO  FILA UNICA E MULTIPLOS WORKERS: \n {multiplosWorkers[1]}")

print("\n")