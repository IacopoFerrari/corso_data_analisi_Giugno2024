

class ClasseGenitore:
    def __init__(self):
        self._numero = 10 # protetto, le classi che ereditano da questa in modo pubblico avranno accesso a quell'attributo in modo protetto

    def metodo_genitore(self):
        print(self._numero)

#ereditarieta:
class ClasseFiglia(ClasseGenitore):
    def __init__(self, f):
        super().__init__()
        self._attributo_figlia = f
        #self._numero = 9
    def metodo_figlia(self):
        super().metodo_genitore()
        print("Sono il metodo della classe figlia")

    
