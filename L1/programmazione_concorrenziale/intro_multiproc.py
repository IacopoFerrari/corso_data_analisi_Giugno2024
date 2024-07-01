import random
import multiprocessing as mp
import threading as th
import time

def calcola(l,q,num_processo):
    print("sono il processo ", num_processo , " inizio lo sleep")
    time.sleep(2)
    print("sono il processo ", num_processo , " ho finito lo sleep")
    massimo = max(l)
    minimo = min(l)
    media = sum(l)/len(l)
    q.put((massimo,minimo,media))
    #return massimo,minimo,media

if __name__ == "__main__":
    num_liste = int(input("inserisci numero di liste: "))
    num_elementi = int(input("inserisci numero di elementi: "))
    t_init = time.time()
    l = []
    for i in range(0,num_liste):
        l.append([])
        for j in range(0,num_elementi):
            l[i].append(random.randint(0,101))

    #print(l)
    lista_processi = []
    #un oggetto pipe o queue
    q = mp.Queue() # oggetto coda che serve per instaurare un metodo di comunicazione tra padre e figlio
    i=0

    for lista_interna in l:
        i+=1
        #lista_processi.append(th.Thread(target=calcola,args=(lista_interna,q,i))) 
        lista_processi.append(mp.Process(target=calcola,args=(lista_interna,q,i))) 


    for p in lista_processi:
        p.start()

    print("sono il processo Padre, aspetto i miei figli")     
    for p in lista_processi:
        p.join()
        #time.sleep(1)
        #print("un figlio ha finito")

    print("I miei figli hanno finito")     


    risultati = []
    while not q.empty():
        risultati.append(q.get())

    t_final =time.time() - t_init
    print(risultati)
    print("tempo impiegato: ", t_final) 

#in sequenza invece
"""
    for lista_interna in l:
        i+=1
        ris = calcola(lista_interna,q,i)

    t_final = time.time() - t_init
    print("tempo impiegato: ", t_final)
"""
   
