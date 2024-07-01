class Persiano:
    def miagola(self):
        print("Il mio persiano miagola")
    
    def graffia(self):
        print("Il mio persiano NON graffia")

class Siamese:
    def miagola(self):
        print("Il mio siamese NON miagola")
    
    def graffia(self):
        print("Il mio siamese graffia")

# interfaccia comune, funzione che fa uso del polimorfismo
def evento(gatto):
    gatto.miagola()

# istanza oggetto
tyson = Persiano()
foreman = Siamese()

# passaggio degli oggetto all'interfaccia comune
evento(tyson)
evento(foreman)

"""
Vantaggi del Polimorfismo:

    Flessibilità: Consente di scrivere codice più generico e riutilizzabile, in quanto le funzioni possono trattare oggetti diversi allo stesso modo.
    Estensibilità: Facilita l'estensione del software aggiungendo nuove classi che implementano lo stesso interfaccia (metodi), senza dover modificare il codice esistente.
"""