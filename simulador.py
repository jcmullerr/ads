import pandas as pd

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