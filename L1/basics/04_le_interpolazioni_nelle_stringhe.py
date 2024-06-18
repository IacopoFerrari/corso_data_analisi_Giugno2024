# FOCUS le interpolazioni nelle stringhe:

# con le f_strings:

# con tipi semplici:
numero_intero = 42
numero_float = 3.1415

print(f"Numero intero: {numero_intero}")
print(f"Numero float: {numero_float:.2f}")  # Specifica il numero di cifre decimali dopo il punto

# con i dizionari:
studente = {
    "nome": "Alice",
    "eta": 25,
    "corso": "Informatica"
}

print(f"Nome dello studente: {studente['nome']}")
print(f"Età dello studente: {studente['eta']}")
print(f"Corso dello studente: {studente['corso']}")

# oppure con il metodo format delle stringhe
name = "Alice"
age = 25

# Interpolazione di stringhe utilizzando .format()
message = "Ciao, mi chiamo {} e ho {} anni.".format(name, age)

print(message)

# mentre se ho un dizionario
person = {
    "name": "Alice",
    "age": 25,
    "occupation": "Software Engineer"
}

# Interpolazione di stringhe utilizzando .format() con un dizionario
message = "Ciao, mi chiamo {name}, ho {age} anni e sono {occupation}.".format(**person)

print(message)
