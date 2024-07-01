import requests
from bs4 import BeautifulSoup

search = input('Ricerca: ')
response = requests.get('http://google.it/search', headers={'Accept':'text/html'}, params={'q':search})
soup = BeautifulSoup(response.content, 'html.parser')
result = soup.find_all("a")
for link in result:
    print(link["href"])
    

