def cenario_multiplos_workers(data,num_instancias=200):
    tempo = 0
    item_index = 0
    item = data[item_index]
    tempo_buscar_proximo_item = int(item[0]) + tempo
    atividades = [[],[]]
    tempos_de_espera = []
    workers = []
    for i in range(2):
        workers.append((True,None,None,None,None))
    
    def tem_worker_disponivel():
        for i in range(2):
            worker = workers[i]
            if(worker[0] == True):
                return True
        
        return False
    
    def obter_index_worker_disponivel():
        for i in range(2):
            worker = workers[i]
            if(worker[0] == True):
                return i
    
    def filas_estao_vazias():
        return len(atividades[0]) + len(atividades[1]) == 0
    
    def obter_fila_preferencial(numero_do_worker):
        if(numero_do_worker == 1):
            if(len(atividades[1]) > 0):
                return 1
            
            return 0
        return 0
    
    while (True):
        if(tempo_buscar_proximo_item == tempo):
            if(tem_worker_disponivel()):
                tempos = data[item_index]
                index_worker_disponivel = obter_index_worker_disponivel()
                worker = (False,item_index,tempos,tempo,tempo)
                tempos_de_espera.append((worker[1],tempo-worker[3]))
                item_index = item_index + 1
                if(item_index < num_instancias and not filas_estao_vazias()):
                    tempo_buscar_proximo_item = tempo + (data[item_index][0] if data[item_index][0] > 0 else 1)
                    workers[index_worker_disponivel] = worker
            else:
                if(item_index < num_instancias):
                    tempos = data[item_index]
                    if(tempos[0] > 18):
                        atividades[0].append((item_index,tempos,tempo))
                    else:
                        atividades[1].append((item_index,tempos,tempo))
                    item_index = item_index + 1
                    if(item_index < num_instancias):
                        tempo_buscar_proximo_item = tempo + (data[item_index][0] if data[item_index][0] > 0 else 1) 
    
        for idx,worker in enumerate(workers):
            if worker[0]:
                continue

            tempos = worker[2]
            if(tempos[1] + worker[4] <= tempo):
                if(not filas_estao_vazias()):
                    index_fila = obter_fila_preferencial(idx)
                    if(len(atividades[index_fila]) == 0):
                        continue
                    item = atividades[index_fila].pop(0)
                    worker = (False, item[0], item[1],item[2],tempo)
                    tempos_de_espera.append((item[0],tempo-item[2]))
                    workers[idx] = worker
                
                elif(filas_estao_vazias() and item_index > num_instancias):
                    return
                elif (item_index < num_instancias):
                    tempos = data[item_index]
                    worker = (False,item_index,tempos,tempo,tempo)
                    tempos_de_espera.append((worker[1],tempo-worker[3]))
                    item_index = item_index + 1
                    tempo_buscar_proximo_item = tempo+tempos[0]
        
        # os.system('clear')
        print("Tempo",tempo)
        print("Em espera:",len(atividades))
        print("workers:",workers)
        print("______________________")
        tempo = tempo + 1
        # ts.sleep()
