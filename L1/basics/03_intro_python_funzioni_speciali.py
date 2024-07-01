#import librerie necessarie
import random
# VARIABILI GLOBALI:
a = 10

######### FUNZIONI ##########
def doppio(x):
    return 2 * x


def main():
    #VARIABILI LOCALI
    l = [random.randint(0,10) for x in range(20)] #--> lunghezza 20
    l0 = [0 for x in range(20)]
    l0_new = [0]*20
    print("l0_new: ", l0_new)
    l1 = [1 for x in range(20)]
    print("lista random l: ", l)
    
    #funzioni sugli iterabili:
    #sorting (in place o in nuova lista.)
    l_ord = sorted(l) # funzione
    print("lista l_ord", l_ord)
    print("lista l dopo sorted: ", l)
    l.sort() # metodo per ordinare le liste in place
    print("lista l ordinata", l)

    #esploriamo insieme le funzioni len,max,min,sum,argmax, reversed,any e all.

    #zip
    lista1 = [1, 2, 3, 5]
    lista2 = ['a', 'b', 'c', 'd'] # se aggiungo un elemento?
    combinato = zip(lista1, lista2)
    print(list(combinato))

    #map
    numeri = [1, 2, 3, 4, 5]
    # Usiamo map() per applicare la funzione doppio a ogni elemento di numeri
    risultato = map(doppio, numeri) # cosa ritorna?
    print("risultato con map: ", list(risultato))

    #utilizzo funzione lambda (funzione anonima)
    doppio_lambda = lambda x: 2*x
    doppi = list(map(doppio_lambda, numeri))
    print(doppi)  # Output: [2, 4, 6, 8, 10]

    numeri = [1, 2, 3, 4, 5]
    pari = filter(lambda x: x % 2 == 0, numeri)
    print(list(pari))  # Output: [2, 4]



if __name__ == "__main__": # perché si usa? dopo lo facciamo vedere con un esempio magari
    #main()
    #ESERCIZIO:
    """
    Esercizio: Lista delle Prime Tre Lettere Maiuscole di una Parola
    Utilizza filter e lambda.

    Usa una funzione lambda per calcolare la lunghezza di ogni stringa in una lista di stringhe 
    e filter() per selezionare solo le stringhe di lunghezza maggiore di 3.

    """
    s = "Ghs!dUpiUA"
    maiusc = []
    ris = filter(lambda x: x.isupper(),s) # solo le prime 3
    print(list(ris)[0:3])

    ls = ["csoidjc", "cwds", "a","QQ", "qwerty"]
    ris = filter(lambda x: len(x)>3 , ls)
    print(list(ris))
