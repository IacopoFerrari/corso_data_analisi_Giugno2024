"""
SUGGERIMENTO ESERCIZIO:
Scrivi un programma che: chieda all'utente di inserire il nome di un file, poi crei questo file con estensione txt e davanti al nome inserito dall'utente 
metta pincopallino e la data. (Esempio se l'utente scrive ciao il file si chiamerà pincopallino14_06_2023_ciao.txt). 
(Puoi usare una libreria python per ottenere la data odierna)
Chiedi quante parole vuole inserire, apri il file in modalità append e permettigli di inserire dentro una parola ogni riga, e poi chiudi il file.
Poi, attraverso una funzione che scrivi tu, apri il file in lettura e salva in una lista solo le righe pari. 
Le righe dispari invece le salvi in un dizionario che abbia come chiave la parola della riga e come valore il numero della riga.
Togli i caratteri '\n' dai dati che hai prodotto e poi apri un file in scrittura che si chiami resoconto.txt, 
fai in modo che lo crei se non esiste e scrivici dentro gli elementi della lista creata
tutti uniti tra di loro e separati da " - " (cioè spazio trattino spazio)
"""
import datetime

def apri_e_salva(path,nome):
    f = open(f"{path}{nome}","r")
    list_return = []
    diz_return = {}
    for index, line in enumerate(f):
        if index%2==0:
            list_return.append(line.replace("\n",""))
        
        else:
            diz_return[line.replace("\n","")] = index

    f.close()
    return list_return,diz_return


if __name__ == "__main__":
    path = ".\\dati\\"
    nome_file = input("inserisci nome file: ")
    data = datetime.date.today().strftime("%d_%m_%Y")
    nome_completo = "pincopallino_" + data + "_" + nome_file + ".txt"
    f = open(f"{path}{nome_completo}","w+")
    f.close()
    num_parole = -1
    while num_parole < 0:
        num_parole = int(input("inserisci numero parole:"))
    
    with open(f"{path}{nome_completo}","a") as mio_file:
        for i in range(0,num_parole):
            mio_file.write(input(f"inserisci parola {i} :"))
            mio_file.write("\n")
    #tabulando chiudo
    lista_1, diz_1 = apri_e_salva(path, nome_completo)
    #print(lista_1)
    #print(diz_1)
    f = open(f"{path}resoconto.txt","w+")
    f.write(" - ".join(lista_1))
    f.close()