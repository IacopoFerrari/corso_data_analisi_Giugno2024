import datetime

if __name__ == "__main__":
    #f = open("./basics/file_dati.txt","w") #apro file in scrittura w, a --> append, r --> read, r+ e w+
    #f.write("ok\nprova\n")
    #f.close()
    #with open("file_dati.txt","a") as f:
    #    f.write("appendo in coda")
    #chiude
    #f = open("file_dati.txt","r")
    #riga = f.readline()
    #print(riga)
    #riga = f.readline()
    #print(riga)
    #print(f.readlines())
    #print(f.read())
    oggi = datetime.date.today()
    print(str(oggi))
    nome_file = "iacopo_ferrari" + input("inserire nome file ") + str(oggi) + ".txt"
    f = open(f"./{nome_file}","w")
    #f.close()
    num_righe = int(input("quante vuoi inserire?"))
    for i in range(num_righe):
        riga_i = input(f"inserisci riga {i}: ")
        f.write(riga_i + "\n")
    
    f.close()
    f = open(nome_file, "r")
    linee = f.readlines()
    diz_righe_dispari = {}
    l_righe_pari = []
    for i in range(len(linee)):
        if i%2: #righe dispari
            diz_righe_dispari[linee[i].replace("\n","")] = linee[i]
        else:
            l_righe_pari.append(linee[i].replace("\n",""))

    f.close()
    resoconto = open("./resoconto.txt","w")
    resoconto.write(" - ".join(l_righe_pari))    
