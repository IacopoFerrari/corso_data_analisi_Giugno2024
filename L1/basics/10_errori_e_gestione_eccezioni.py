

def converti_float(n):
    try:
        return float(n)
    
    except ValueError:
        print("errore di conversione")
        return n
    
    #except:
        #print("errore generico")

if __name__ == "__main__":
    print(converti_float("20.2"))
    print(converti_float("ciao"))
    #print(converti_float([2.1,3.2]))