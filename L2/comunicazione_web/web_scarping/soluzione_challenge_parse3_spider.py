import requests
from bs4 import BeautifulSoup

url = "http://web-16.challs.olicyber.it/"
global lista_link_visitati

def visita(links):
    for link in links:
        if link not in lista_link_visitati:
            lista_link_visitati.append(link)
            response = requests.get(url+link)
            s = BeautifulSoup(response.text, "html.parser")
            title = s.find("h1").get_text()
            if "flag" in title:
                #print(title)
                #print(link)
                #print(len(lista_link_visitati))
                return
                
            else:
                for link in s.find_all("a"):
                    lista_url.append(link["href"])

                visita(lista_url)


if __name__ == "__main__":
    lista_link_visitati = []
    res = requests.get(url)
    s = BeautifulSoup(res.text, "html.parser")
    lista_url = []
    for link in s.find_all("a"):
        lista_url.append(link["href"])
        
    visita(lista_url)
    print(len(lista_link_visitati))