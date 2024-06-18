class Studente: # definisco la classe Studente, un prototipo che utilizzero per gli studenti
    def __init__(self, n, c, classe_appartenenza): # costruttore della classe, gli do i parametri tra le parantesi, che quindi dovro valorizzare quando poi istanziero' un particolare studente
# qui di seguito definisco gli attributi della classe
        self.nome = n
        self.cognome = c
        self.classe_frequentata = classe_appartenenza
        self.eta = 17
    # metodo della classe, tra i parametri questo metodo utilizza solo self, una parola chiave che sta ad indicare l'istanza stessa, ovvero il particolare studente appartanente alla classe Studente
    def scheda_studente(self):
# la riga successiva assegna alla variabile scheda la stringa tra doppi apici, dove {0} vuol dire che nella stringa in quel punto mettero' il valore della variabile alla posizione 0 tra quelle dentro .format(...) in questo caso:
#    {0} --> self.nome, {1}--> self.cognome, {2}--> self.classe_frequentata
        scheda = "Nome: {0},\n Cognome = {1},\n Classe = {2}\n".format(self.nome, self.cognome, self.classe_frequentata)
        return scheda


if __name__ == "__main__":
    studente1 = Studente("Pinco", "Pallino","4A it") # creo l'istanza studente1 della classe Studente, con i parametri tra parentesi
    studente2 = Studente("Ciccio", "Pasticcio","4d it") # creo l'istanza studente2 della classe Studente, con i parametri tra parentesi
    print(studente1) # stampa l'oggetto studente1 indicandomi la classe e l'indirizzo di memoria in cui si trova
    print(studente2) # stampa l'oggetto studente1 indicandomi la classe e l'indirizzo di memoria in cui si trova
    print(studente1.nome) # stampa l'attributo nome dell'istanza studente1
    print(studente1.cognome) # stampa l'attributo cognome dell'istanza studente1
    print(studente2.nome) # stampa l'attributo nome dell'istanza studente2
    print(studente2.cognome) # stampa l'attributo cognome dell'istanza studente2
    scheda_studente2 = studente2.scheda_studente() # assegna alla variabile scheda_studente2 il valore di ritorno del metodo scheda_studente, un metodo esistente solo per le istanze della classe Studente
    print("\nScheda Studente:\n") # stampa una stringa
    print(scheda_studente2) #stampa la variabile scheda
