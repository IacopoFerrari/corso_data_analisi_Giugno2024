class Veicolo:
    def __init__(self, modello, anno):
        self._modello = modello
        self._anno = anno

    def descrizione(self):
        return f"Modello: {self._modello}, Anno: {self._anno}"

class Automobile(Veicolo):
    def __init__(self, modello, anno, porte):
        super().__init__(modello, anno)
        self._porte = porte

    def descrizione(self):
        return f"Automobile - {super().descrizione()}, Porte: {self._porte}"

class Moto(Veicolo):
    def __init__(self, modello, anno, tipo_guida):
        super().__init__(modello, anno)
        self._tipo_guida = tipo_guida

    def descrizione(self):
        return f"Moto - {super().descrizione()}, Tipo guida: {self._tipo_guida}"

def mostra_descrizione(veicolo):
    print(veicolo.descrizione())

# Utilizzo delle classi
auto = Automobile("Toyota Corolla", 2022, 4)
moto = Moto("Honda CB500", 2021, "Manubrio")

mostra_descrizione(auto)   # Output: Automobile - Modello: Toyota Corolla, Anno: 2022, Porte: 4
mostra_descrizione(moto)   # Output: Moto - Modello: Honda CB500, Anno: 2021, Tipo guida: Manubrio
