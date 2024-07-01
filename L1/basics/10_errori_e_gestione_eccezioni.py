

def converti_a_float(n):
    try:
        return float(n)
    
    except (ValueError, TypeError):
        print("errore di conversione")
        return n
    
    except:
        print("errore generico")

    finally:
        print("quando passo qui?")

if __name__ == "__main__":
    print(converti_a_float("20.2"))
    print(converti_a_float("ciao"))
    print(converti_a_float([2.1,3.2]))