def quad_gen(n=10): #generatore
    print(f"Genero quadrati da 1 a {n**2}")
    for i in range(1,n+1):
        print("passo nel generatore")
        yield i**2

def quad_func(n=10): #funzione
    print(f"Genero quadrati da 1 a {n**2}")
    res = []
    for i in range(1,n+1):
        print("passo nella funzione")
        res.append(i**2)
    return res

if __name__ =="__main__":
    gen = quad_gen()
    print(gen)
    for x in gen:
        print(x, end=" ")
        # altre operazioni
    
    print("\n")
    print(quad_func())

"""
Utiliziamo un generatore per leggere, una alla volta le line di un file
"""

"""
Vantaggi principale dei Generatori --> Efficienza in Memoria: Utilizzando yield, i generatori producono valori su richiesta, riducendo il consumo di memoria.
Ciò può essere utile quando dobbiamo eseguire operazioni in sequenza su una grande quantità di dati
"""
























"""
def leggi_linee(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line

# Utilizzo del generatore per leggere un file
for linea in leggi_linee('testo.txt'):
    print(linea.strip())
"""