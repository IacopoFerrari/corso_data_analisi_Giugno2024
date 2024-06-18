import argparse

# Creazione del parser
parser = argparse.ArgumentParser(description='Esempio di utilizzo di argparse') # con --help o -h vediamo la descrizione

# Aggiunta degli argomenti
parser.add_argument('input_file', help='Nome del file di input')
parser.add_argument('-o', '--output', help='Nome del file di output (opzionale)')
parser.add_argument('numero', type=int, help='Numero intero')

# Analisi degli argomenti
args = parser.parse_args()

# Accesso ai valori degli argomenti
input_file = args.input_file
output_file = args.output

# Utilizzo degli argomenti
print(f"File di input: {input_file}")
if output_file:
    print(f"File di output: {output_file}")
else:
    print("Nessun file di output specificato")


"""
ESERCIZIO:
Scrivi uno script Python che accetti due argomenti da linea di comando:
    Il nome di un file di testo.
    Il numero di riga da leggere (opzionale).

Lo script stampi il contenuto della riga richiesta. Se non indica la riga stampa tutto il contenuto!
Gestisci il caso in cui la linea NON esiste o il file NON è stato trovato. 
"""