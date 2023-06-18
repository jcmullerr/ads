def cenario_multiplos_workers(data,numero_de_workers,num_instancias=200):
    tempo = 0
    item_index = 0
    item = data[item_index]
    tempo_buscar_proximo_item = int(item[0]) + tempo
    atividades = []
    tempos_de_espera = []
    workers = []
    for i in range(numero_de_workers):
        workers.append((True,None,None,None,None))
    
    def tem_worker_disponivel():
        for i in range(numero_de_workers):
            worker = workers[i]
            if(worker[0] == True):
                return True
        
        return False
    

    def todos_workers_disponiveis():
        for i in range(numero_de_workers):
            worker = workers[i]
            if(worker[0] == False):
                return False
        
        return True
    
    def obter_index_worker_disponivel():
        for i in range(numero_de_workers):
            worker = workers[i]
            if(worker[0] == True):
                return i
            

    while (True):
        for idx,worker in enumerate(workers):
            
            if worker[4] != tempo:
                if(len(atividades) == 0 and item_index >= num_instancias and todos_workers_disponiveis()):
                    return tempos_de_espera
                
                continue

            tempos = worker[2]
            if(len(atividades) > 0):
                item = atividades.pop(0)
                worker = (False, item[0], item[1],item[2],tempo+tempos[1])
                tempos_de_espera.append((item[0],tempo-item[2]))
                workers[idx] = worker

            elif len(atividades) == 0 and item_index <= num_instancias:
                workers[idx] = (True,None,None,None,None)


            elif item_index < num_instancias:
                tempos = data[item_index]
                worker = (False,item_index,tempos,tempo,tempo+tempos[1])
                tempos_de_espera.append((worker[1],tempo-worker[3]))
                item_index = item_index + 1
                tempo_buscar_proximo_item = tempo + (data[item_index][0] if data[item_index][0] > 0 else 1)
    
        if(tempo_buscar_proximo_item == tempo):
            if(tem_worker_disponivel()):
                tempos = data[item_index]
                index_worker_disponivel = obter_index_worker_disponivel()
                worker = (False,item_index,tempos,tempo,tempo+tempos[1])
                tempos_de_espera.append((worker[1],tempo-worker[3]))
                workers[index_worker_disponivel] = worker

                item_index = item_index + 1
                if(item_index < num_instancias):
                    tempo_buscar_proximo_item = tempo + (data[item_index][0] if data[item_index][0] > 0 else 1)
                
            else:
                if(item_index < num_instancias):
                    tempos = data[item_index]
                    atividades.append((item_index,tempos,tempo))
                    item_index = item_index + 1
                    if(item_index < num_instancias):
                        tempo_buscar_proximo_item = tempo + (data[item_index][0] if data[item_index][0] > 0 else 1) 
    
        
        # os.system('clear')
        # print("Tempo",tempo)
        # print("Em espera:",len(atividades))
        # print("workers:",workers)
        # print("______________________")
        # ts.sleep()
        tempo = tempo + 1
