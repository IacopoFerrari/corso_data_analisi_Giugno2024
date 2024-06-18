

def main():
    #creazione di un file:
    # l'istruzione sotto apre il file myfile nel path C:/Users/desktop, se non esiste lo crea.
    # w+ indica che apre il file in modalità di scrittura (w=write) e se non esiste lo crea
    f = open("./file_dati.txt","w+")
    #se si vuole aprire un file per "appendere" quindi in modalità scrittura in coda (a=append), metto a al posto di w+

    print(f) # cosa vi stampa??
    f.write("Sto scrivendo")
    #for i in range(10):
    #    f.write("This is line {}\r\n".format(i+1))

    #chiudo il file
    f.close()

    # c'è anche la modalità read con cui posso leggere il contenuto del file.
    # un altro metodo fondamentale dei file è readlines, possiamo immaginare cosa faccia

    """
    SUGGERIMENTO ESERCIZIO:
    Scrivi un programma che: chieda all'utente di inserire il nome di un file, poi crei questo file con estensione txt e davanti al nome inserito dall'utente 
    mettI il tuo nome e la data. (Esempio se l'utente scrive ciao il file si chiamerà iacopo_ferrari19_06_2024_ciao.txt). 
    (Puoi usare una libreria python per ottenere la data odierna)
    Chiedi quante parole vuole inserire, apri il file in modalità append e permettigli di inserire dentro una parola ogni riga, e poi chiudi il file.
    Poi, attraverso una funzione che scrivi tu, apri il file in lettura e salva in una lista solo le righe pari. 
    Le righe dispari invece le salvi in un dizionario che abbia come chiave la parola della riga e come valore il numero della riga.
    Togli i caratteri '\n' dai dati che hai prodotto e poi apri un file in scrittura che si chiami resoconto.txt, 
    fai in modo che lo crei se non esiste e scrivici dentro gli elementi della lista creata
    tutti uniti tra di loro e separati da " - " (cioè spazio trattino spazio)
    """


if __name__ == "__main__":
    main()