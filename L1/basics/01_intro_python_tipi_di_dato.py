# import librerie necessarie
# import numpy as np

# VARIABILI GLOBALI:
a = 10

######### FUNZIONI ##########

def modifica_lista(l: list) -> None: # type hinting
    """
    (docstring funzione) es. questa funzione modifica il primo elemento della lista passata in ingresso  
    """
    l[0] = 99
    return

def ciclista(lista):
    l_ciclista1 = lista.copy()
    #ciclare sugli indici:
    for i in range(0,len(l_ciclista1)):
        print("indice ", i)
        print("elemento ", l_ciclista1[i])
    
    #ciclare sugli elementi:
    l_ciclista2 = lista.copy()
    for el in l_ciclista2:
        print("elemento l_ciclista2: ", el)
    
    #list comprehension:
    l_ciclista_compr = [el for el in lista if el < 3]
    print("l_ciclista_compr: ", l_ciclista_compr)

def main():
    #VARIABILI LOCALI
    l_vuota = []
    print("l vuota:", l_vuota)
    print("tipo di l vuole:", type(l_vuota))
    n = "3"
    print("tipo di n: ", type(n))
    l = [1,2,3,4,5]
    diz = {"nome" : "Mario", "cognome" : "Rossi", "eta" : 90, 1:"2"}
    print("diz: ", diz)
    num = 10
    
    print("lista PRE chiamata funzione: ", l)
    modifica_lista(l)
    print("lista POST chiamata funzione: ", l) # cosa succede? perché?
    # proviamo a fare la stessa operazione con dizionari e con interi!

    # creiamo un oggetto uguale alla lista l. In che senso uguale? vediamo i due modi:
    l1 = l
    l2 = l[:] # con lo slicing
    l.append("0")
    print("lista l1 dopo append: ", l1)
    print("lista l2 dopo append: ", l2)
    #cosa stampano? ce lo aspettavamo?

    #vediamo i modi di ciclare su una lista
    ciclista(l2)

    #cerchiamo insieme modi di ciclare su un dizionario


    
print("inizio ad eseguire il main:")
if __name__ == "__main__": # perché si usa? dopo lo facciamo vedere con un esempio magari
    main() # richiamiamo la funzione