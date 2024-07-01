# Genera 1000 campioni da una distribuzione uniforme tra 0 e 3
data = np.random.uniform(0, 3, 1000)

# Crea l'istogramma
plt.hist(data, bins=30, density=True, color='red', edgecolor='black')

# Aggiungi titolo e etichette degli assi
plt.title('Distribuzione Uniforme tra 0 e 3')
plt.xlabel('Valore')
plt.ylabel('Frequenza')

# Rimuovi la griglia dal grafico
plt.grid(False)

# Mostra il grafico
plt.show()