

class ClasseGenitore:
    def __init__(self):
        self.__numero = 10

    def metodo_genitore(self):
        print("Sono il metodo della classe genitore")

#ereditarieta:
class ClasseFiglia(ClasseGenitore):
    def metodo_figlia(self):
        super().metodo_genitore()
        print("Sono il metodo della classe figlia")

    
