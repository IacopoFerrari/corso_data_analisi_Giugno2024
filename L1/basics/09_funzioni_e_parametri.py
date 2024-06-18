def somma_due_o_qualcosa_di_tuo(num1 : int, num2 : int =2) -> int:
#def somma_due_o_qualcosa_di_tuo(num1, num2=2):
    return num1+num2

if __name__=="__main__":
    print("risultato prima volta: ", somma_due_o_qualcosa_di_tuo(15))
    print("risultato seconda volta: ", somma_due_o_qualcosa_di_tuo(15,11))



"""
A cosa servono le annotazioni dei tipi?

    Documentazione: Le annotazioni dei tipi forniscono informazioni sul tipo di dato atteso per i parametri della funzione. Possono aiutare a rendere il codice più leggibile e comprensibile per altri sviluppatori che leggono il codice.

    Chiarezza nell'interfaccia: Le annotazioni dei tipi nei default arguments possono fornire una descrizione chiara dell'interfaccia di una funzione, indicando quali parametri sono obbligatori e quali sono opzionali.

    Strumenti di analisi statica: Gli strumenti di analisi statica del codice e gli IDE possono utilizzare le annotazioni dei tipi per fornire suggerimenti e controlli di tipo durante lo sviluppo. Possono segnalare eventuali inconsistenze o errori di tipo nelle chiamate alla funzione.

    Documentazione automatica: Le annotazioni dei tipi possono essere utilizzate da strumenti di generazione della documentazione per creare automaticamente documentazione dettagliata sulla funzione, inclusi i tipi dei parametri e dei valori di ritorno.

    Debugging: Le annotazioni dei tipi possono aiutare nel processo di debugging, poiché forniscono informazioni sul tipo dei parametri che possono essere utili per identificare eventuali problemi nel codice.

Tuttavia, è importante sottolineare che le annotazioni dei tipi nei default arguments non influiscono direttamente sul comportamento della funzione o sulla validità dei valori passati. Sono opzionali e non vengono eseguiti controlli di tipo automatici da parte di Python durante l'esecuzione del codice.

"""