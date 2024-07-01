
def modifica_lista(l, num=10): # type hinting
    """
    (docstring funzione) es. questa funzione modifica il primo elemento della lista passata in ingresso  
    """
    l[0] = 99
    #print("valore parametro di default: ", num)
    return

def ritorna_cose(): #posso ritornare piu di una cosa? sì 
    a = 10
    b = 9
    c = 8
    return a,b,c


def main():
    #DIZIONARI#
    # ai dizionari si accede tramite chiave 
    diz = {"nome" : "Iacopo", "eta" : 31, 'cognome': 'Marani'}
    #print("valore chiave 'nome': ", diz.get("nome"))
    #print(diz.get("cognome")) # ritorna None se la chiave non esiste, altrimenti ritorna il valore della chiave
    diz.setdefault("cognome","Ferrari") # assegna alla chiave (primo parametro) un valore (secondo parametro)
    diz["professione"] = "notaio"
    # se la chiave NON esiste. Altrimenti NON fa nulla
    diz2 = {"codice fiscale" : "jvhsdvsdvjlksd", "cognome": "rossi"}
    diz.update(diz2) # aggiorna diz con diz2
    #print(diz)
    # cosa succede se ho delle chiavi in diz2 che sono già presenti in diz? con valori diveresi? lo aggiorna!
    #print(diz.keys())
    #Liste: strutture dati che possono contenere dati eterogenei
    l = [1,2.3,"ciao", True, False,"ciao"]
    #print(l[-3]) #indici negativi partono dall'ultimo a ritroso
    #print(l[1:3]) # slicing
    #l.append("elemento appeso")
    #l.insert(1,"inserito")
    #print(l)
    #print(l.count("ciao"))
    #print("lunghezza: ", len(l))
    """
    definite una lista a con degli elementi dentro, poi ugualiate una nuova lista b ad a. Istruzione b = a
    poi aggiungete un elemento alla lista b e stampate la lista a. Cosa è successo? cosa deduciamo?
    """
    a = [1,2,3,4]
    b = a # facendo così io NON creo una lista b che è la copia di a, ma creo un collegamento b che punta alle stesse celle di memoria a cui punta a 
    b.append(99) # aggiungo un elemento a b
    #print(a) # cosa succede?? Cambia anche a! ho modificato a modificando b.
    #Scelta dovuta al fatto che python vuole essere usato per analizzare una grande quantità di dati, quindi per essere più efficiente.
    c = a[:] # a.copy()
    c.append(88)
    #print(a)
    # se lo faccio con due interi o con due stringhe, l'ugualianza è per copia di default.
    n1 = "10"
    n2 = n1
    n2+="1"
    #print("valore di n1 dopo modifica n2", n2)
    l = [4321,90,13,24] 
    modifica_lista(l, 0) # le liste vengono passate per riferimento. Il secondo è un parametro
    #print(l)
    t = (1,2,3,4) # tupla, è una lista immutabile!
    res1, res2, res3 = ritorna_cose()
    #print(res1)

    #cicli: si fanno sugli iterabili
    #ciclo definito FOR:
    #ciclo su indici
    #for i in range(4,30,3): #range(10) --> [0,1,2,3,4,5,6,7,8,9] 
        #print("i") #dentro il for
    l = [4321,90,13,24] 
    #for i in range(0, len(l)):
    #    print("indice: ", i)
    #    print(l[i])
    
    #ciclo su elementi
    #for el in l:
    #    print(el)

    #LIST COMPREHENSION:
    #se volessi creare una lista dei primi 10 numeri pari:
    l_pari = [ 2*x for x in range(10) ]
    l_pari = [x for x in range(0,20) if x%2==0]
    #print(l_pari)

    #ciclare su un dizionario
#    for k in diz:
#        print(f"chiave {k}, valore {diz[k]}.")

    #for v in diz.values():
    #    print(v)
    
    #for k,v in diz.items():
    #    print(f"chiave {k} valore: {v}")

    contatore = 1
    while contatore <= 5: # while True:
        print(f"aumento il contatore da {contatore} a {contatore+1}")
        contatore += 1  # Incrementa il contatore di 1 a ogni iterazione

    print("Ciclo While terminato.")
  
    return 

if __name__=="__main__":
    print("Hello World")
    main()