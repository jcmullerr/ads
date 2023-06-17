import pandas as pd
import time as ts
import os
import numpy as np


#         tc          ts
# count  200.000000  200.000000
# mean     4.640000   11.105000
# std      1.990025    2.018501
# min      0.000000    8.000000
# 25%      3.000000    9.000000
# 50%      5.000000   11.000000
# 75%      6.000000   13.000000
# max     10.000000   14.000000

# altera a semente do random
# np.random.seed(1)

qt_testes = 5
size = 10 # quantidade de valores gerados padrão=200.
mean = 11.105000 # media
std = 2.018501 # desvio padrao
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
    print(f"cenario {qt+1}: {cenario}")


data = pd.read_csv('./tc.txt')
data['ts'] = pd.read_csv('./ts.txt')
data.rename(columns={'x': 'tc', 'ts': 'ts'}, inplace=True)
data = data[data['ts'] < 15].head(200)
data = data.values.tolist()

tempo = 0
item_index = 0
item = data[item_index]
tempo_buscar_proximo_item = int(item[0]) + tempo
tempo_inicio_trabalho = 0
atividades = []
item = None


while (True):
        
    if(tempo_buscar_proximo_item == tempo):
        if(item == None):
            item = data[item_index]
            item_index = item_index + 1
            tempo_inicio_trabalho = tempo
            tempo_buscar_proximo_item = tempo + (item[0] if item[0] > 0 else 1)
        else:
            if(item_index < 200):
                atividades.append(data[item_index])
                item_index = item_index + 1
                tempo_buscar_proximo_item = tempo + (item[0] if item[0] > 0 else 1)
    
    if(item != None):
        if(item[1] + tempo_inicio_trabalho == tempo):
            if(len(atividades) > 0):
                item = atividades.pop(0)
                tempo_inicio_trabalho = tempo
            elif(len(atividades) == 0 and item_index > 199):
                break
            else:
                item = data[item_index]
                item_index = item_index + 1
                tempo_inicio_trabalho = tempo
                tempo_buscar_proximo_item = tempo+item[0]
        
    tempo = tempo + 1

    os.system('cls')
    print("Tempo",tempo)
    print("Em espera:",len(atividades))
    print("Ultimo tempo iniciado:",tempo_inicio_trabalho)
    ts.sleep(0.05)