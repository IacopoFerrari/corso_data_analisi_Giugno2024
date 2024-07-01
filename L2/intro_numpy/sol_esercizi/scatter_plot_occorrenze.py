from collections import Counter

# Generazione dei dati casuali
x = np.random.randint(0, 11, (10000,2))
#print(x)
# Conta le occorrenze di ciascuna coppia (x, y)
counts = Counter(coordinates)

# Prepara i dati per il grafico a dispersione
x_unique = np.array([coord[0] for coord in counts.keys()])
sizes = np.array([counts[coord] * 100 for coord in counts.keys()])  # Moltiplica per 100 per dimensioni visibili

# Crea il grafico a dispersione
plt.scatter(x_unique, y_unique, s=sizes, alpha=0.5, cmap='viridis')

# Aggiungi titoli e etichette
plt.title('Scatter Plot con Dimensioni Determinate dalle Occorrenze')
plt.xlabel('Asse X')
plt.ylabel('Asse Y')

# Mostra il grafico
plt.show()