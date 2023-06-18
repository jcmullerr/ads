def cenario_fila_unica(data,num_instancias=200):
    tempo = 0
    item_index = 0
    item = data[item_index]
    tempo_buscar_proximo_item = int(item[0]) + tempo
    tempo_inicio_trabalho = 0
    atividades = []
    tempos_de_espera = []
    item = None

    while (True):
        if(tempo_buscar_proximo_item == tempo):
            if(item == None):
                tempos = data[item_index]
                item = (item_index,tempos,tempo)
                tempos_de_espera.append((item[0],tempo-item[2]))
                item_index = item_index + 1
                tempo_inicio_trabalho = tempo
                tempo_buscar_proximo_item = tempo + (data[item_index][0] if data[item_index][0] > 0 else 1)
            else:
                if(item_index < num_instancias):
                    tempos = data[item_index]
                    atividades.append((item_index,tempos,tempo))
                    item_index = item_index + 1
                    if(item_index < num_instancias):
                        tempo_buscar_proximo_item = tempo + (data[item_index][0] if data[item_index][0] > 0 else 1)
    
        if(item != None):
            tempos = item[1]
            if(tempos[1] + tempo_inicio_trabalho == tempo):
                if(len(atividades) > 0):
                    item = atividades.pop(0)
                    tempo_inicio_trabalho =  tempo
                    tempos_de_espera.append((item[0],tempo-item[2]))
                elif(len(atividades) == 0 and item_index >= num_instancias):
                    break
                elif item_index < num_instancias:
                    item = (item_index,data[item_index],tempo)
                    tempo_inicio_trabalho = tempo
                    tempos_de_espera.append((item[0],tempo-item[2]))
                    item_index = item_index + 1
                    tempo_buscar_proximo_item = tempo+tempos[0]
        
        # tempo = tempo + 1

        # os.system('clear')
        # print("Tempo",tempo)
        # print("Em espera:",len(atividades))
        # if(item != None):
        #     print("Ultimo tempo iniciado:",tempo_inicio_trabalho)
        #     print(item)
        # else:
        #     print("Ultimo tempo iniciado: 0")
        # print("______________________")
        # ts.sleep()
        tempo = tempo + 1
    
    return tempos_de_espera