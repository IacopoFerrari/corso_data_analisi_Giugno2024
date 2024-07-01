"""
Esercizio 1: Filtraggio di Numeri Pari con List Comprehension
Usa list comprehension per creare una nuova lista che contenga solo i numeri pari da una lista di numeri. 
Utilizza anche continue per saltare i numeri dispari durante la creazione della nuova lista.

Esercizio 2: Trova il Primo Numero Pari Maggiore di 5
Utilizza un ciclo for con un'istruzione break per trovare il primo numero pari maggiore di 5 
in una lista di numeri e uscire dal ciclo.

Esercizio 3: Lista delle Prime Tre Lettere Maiuscole di una Parola
Utilizza un ciclo while per creare una lista delle prime tre lettere maiuscole 
di una parola data. 
"""


if __name__ == "__main__":
    #es 1
    l1 = [1,2,432,12,142,21,0,9]
    l2 = [x for x in l1 if x%2==0]
    print("elementi pari di l1: ", l2)

    #es 2
    for num in l1:
        if num%2==0 and num>5:
            print("trovato ", num)
            break
    

    # es 3
    s = "MasBodSìl1!D"
    i = 0 
    n_maiusc = 0
    l_maiusc = []
    while n_maiusc<3 and i<len(s):
        if s[i].isupper():
            n_maiusc+=1
            l_maiusc.append(s[i])
            continue
        i+=1
    
    print(l_maiusc)