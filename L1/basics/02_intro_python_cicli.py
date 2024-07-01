#import librerie necessarie

# VARIABILI GLOBALI:
a = 10


######### FUNZIONI ##########
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    max_divisor = int(n**0.5) + 1

    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True


def main():
    #i for li abbiamo già accennati:, approfondiamoli:
    l = [17,31,13,11,19,5,3,10,29,12,6]
    print("CICLO for con break")
    for el in l:
        if not is_prime(el):
            print(f"trovato numero {el} non primo, esco dal ciclo")
            break

        else:
            print(f"{el} è numero primo")
            
    print("CICLO for con continue")
    for el in l:
        if not is_prime(el):
            print(f"trovato numero {el} non primo, esco dall'iterazione")
            continue

        else:
            print(f"{el} è numero primo")
        
        print("iterazione terminata")

    #CICLI INDEFINITI in python NON esiste il ciclo do ... while():
    contatore = 1
    while contatore <= 5:
        print(f"aumento il contatore da {contatore} a {contatore+1}")
        contatore += 1  # Incrementa il contatore di 1 a ogni iterazione

    print("Ciclo While terminato.")

    #ESERCIZI
    """
    Esercizio 1: Filtraggio di Numeri Pari con List Comprehension
    Usa list comprehension per creare una nuova lista che contenga solo i numeri pari da una lista di numeri. 
    Utilizza anche continue per saltare i numeri dispari durante la creazione della nuova lista.
    
    Esercizio 2: Trova il Primo Numero Pari Maggiore di 5
    Utilizza un ciclo for con un'istruzione break per trovare il primo numero pari maggiore di 5 in una lista di numeri.

    Esercizio 3: Lista delle Prime Tre Lettere Maiuscole di una Parola
    Utilizza list comprehension con un'istruzione continue per creare una lista delle prime tre lettere maiuscole 
    di una parola data. 
    """
    

if __name__ == "__main__":
    main()