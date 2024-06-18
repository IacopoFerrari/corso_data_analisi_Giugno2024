# cosa capiamo degli attributi privati dal seguente script?
# esercizietto: proviamo invece che per gli attributi pubblici non è cosi!

class Facciata:
    def __init__(self, colore): #costruttore parametrizzato
        self.__colore = colore #attributo privato
        #self._colore = colore #attributo protetto
        self.h = 10
        

    def colora(self):
        print("La facciata è di colore {}".format(self.__colore))

    def impostaColore(self, variante):
        self.__colore = variante

if __name__ == "__main__":
    # istanza di classe
    c = input("inserisci colore inizale: ")
    x = Facciata(c)
    x.colora()

    # modifica del colore??
    x.__colore = "rosso"
    x.colora()

    # funzione setter
    x.impostaColore("rosso")
    x.colora()