import multiprocessing as mp
import threading as th
import os
import time

def funzione(n1,n2):
    time.sleep(1)
    return

if __name__ == "__main__":
    print("processo main: ", os.getpid())
    #time.sleep(20)
    a = 10
    b = 9
    lista_processi = []
    t_init = time.time()
    for i in range(5):
        #lista_processi.append(th.Thread(target=funzione,args=(a,b,)))
        lista_processi.append(mp.Process(target=funzione,args=(a,b,)))
    
    for p in lista_processi:
        p.start()
    
    for p in lista_processi:
        p.join()
    
    print("tempo impiegato", time.time()- t_init)