import pandas as pd

# Definisci gli elementi della matrice di Vandermonde
elements = [2.3, 12, -7, 9, 4.3]

# Numero di colonne della matrice di Vandermonde
n = len(elements)

# Crea un dizionario per contenere le colonne della matrice di Vandermonde
vandermonde_dict = {f'col_{i}': pd.Series([x ** (i) for x in elements]) for i in range(n)}

# Converte il dizionario in un DataFrame di pandas
df = pd.DataFrame(vandermonde_dict)

print(df)

# Aggiungi una nuova colonna `sum` che contenga la somma di tutte le colonne per ciascuna riga
df['sum'] = df.sum(axis=1)
print(df)

# Sostituisci tutti i valori negativi del DataFrame con `NaN`
df[df < 0] = float('NaN')
print(df)

# Filtra il DataFrame per mostrare solo le righe in cui `col_0` è maggiore di 1000
filtered_df = df[df['col_0'] > 1000]
print(filtered_df)

# Ordina il DataFrame in base ai valori della colonna `col_1` in ordine decrescente
sorted_df = df.sort_values(by='col_1', ascending=False)
print(sorted_df)

# Calcola la media, il minimo e il massimo dei valori di ciascuna colonna
mean_values = df.mean()
min_values = df.min()
max_values = df.max()
print('Mean Values:\n', mean_values)
print('Min Values:\n', min_values)
print('Max Values:\n', max_values)

# Visualizza il numero di valori non `NaN` per ciascuna colonna
non_nan_counts = df.count()
print('Non-NaN Counts:\n', non_nan_counts)

# Salva il DataFrame in un file CSV chiamato `vandermonde.csv`
df.to_csv('vandermonde.csv', index=False)

# Carica il DataFrame dal file `vandermonde.csv`
loaded_df = pd.read_csv('vandermonde.csv')
print(loaded_df)


# Seleziona 5 valori casuali nel DataFrame (considerando tutte le celle)
indices = list(df.stack().index)
print(indices)
random_indices = np.random.choice(len(indices), size=5, replace=False)

for idx in random_indices:
    row, col = indices[idx]
    df.at[row, col] = np.nan

df