# dimostrare che nel multiprocessing i processi usano un differente spazio di indirizzamento
# mentre nel multithreading i thread usano lo stesso spazio di indirizzamento
# 

import multiprocessing as mp
import threading as th
import os # getpid, getppid()
import time

def modifica(l, nome):
    #print(f"PID {nome} figlio: ", os.getpid())
    if nome == "processo":
        print("PID di mio padre: ", os.getppid())
    l.append("elemento")
    
    #qui finisce l'esecuzione di thread e processo figlio

def accesso_risorsa(n,s):
    print(f"sono {n} sono entrato nella funzione accesso_risorsa")
    with s:
    #s.acquire() # prende un lock
    # sezione critica!
        print(f"sono {n} ho acquisito il lock")
        time.sleep(2)
    #s.release() # rilascia il lock
    print(f"sono {n} ho rilasciato il lock")


if __name__ == "__main__":
    #print("PID processo padre: ", os.getpid())
    time.sleep(100)
    semaforo = mp.Lock()
    #l = [1,2,3]
    #t = th.Thread(target = modifica, args=(l,"thread"))
    lista_thread = []
    for i in range(0,4):
        lista_thread.append(th.Thread(target = accesso_risorsa, args=(i,semaforo)))
    
    for t in lista_thread:
        t.start()
        
    for t in lista_thread:        
        t.join()


    #print("elementi lista dopo modifica thread: ", l)    
    #p = mp.Process(target = modifica, args=(l,"processo",semaforo))
    #p = mp.Process(target = accesso_risorsa, args=(l,"processo",semaforo))
    #p.start()
    #p.join()
    #print("elementi lista dopo modifica processo: ", l)
