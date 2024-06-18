import time
import multiprocessing as mp
import threading as th


def fattoriale(n):
  f=1
  for i in range (1, n+1):
    f*=i
  return f

def main():
  numeri = 100000, 100001, 100002, 100003

  st = time.time()
  risultati = []
  for i in numeri:
    risultati.append(fattoriale(i))
  ft = time.time()
  print("tempo utilizzato per l'esecuzione sequenziale con numeri grandi: ", ft-st)

  #multiprocessing
  st = time.time()
  #with mp.Pool() as pool:
    #result = pool.map(fattoriale, numeri)
  lista_thread = []
  for i in numeri:
      lista_thread.append(th.Thread(target=fattoriale,args=(i,))) 
        #lista_processi.append(mp.Process(target=calcola,args=(lista_interna,q,i))) 


  for p in lista_thread:
      p.start()

  for p in lista_thread:
      p.join()    

  ft = time.time()
  print("tempo utilizzato per l'esecuzione con multiprocessing dei numeri grandi: ", ft-st)

#-------------------------------------------------------

  numeri = 10000, 10001, 10002, 10003
  st = time.time()
  risultati = []
  for i in numeri:
    risultati.append(fattoriale(i))
  ft = time.time()
  print("tempo utilizzato per l'esecuzione sequenziale dei numeri piccoli: ", ft-st)

  st = time.time()
  with mp.Pool() as pool:
    result = pool.map(fattoriale, numeri)
  ft = time.time()
  print("tempo utilizzato per l'esecuzione con multiprocessing dei numeri piccoli: ", ft-st)


if __name__ == "__main__":
  main()