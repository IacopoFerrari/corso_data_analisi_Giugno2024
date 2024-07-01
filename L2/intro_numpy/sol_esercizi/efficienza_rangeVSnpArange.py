import time # libreria da installare
start = time.time()
# *: argument-unpacking operator
Y = [*range(10000000)] # diieci milioni
end = time.time()
times = end - start
print("tempo impiegato da range: ", times)

start = time.time()
X = np.arange(100000000) # diieci milioni
end = time.time()
times = end - start
print("tempo impiegato da np.arange: ", times)