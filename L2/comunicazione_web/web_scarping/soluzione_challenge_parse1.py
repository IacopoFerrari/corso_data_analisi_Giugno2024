import requests
from bs4 import BeautifulSoup
r = requests.get("http://web-12.challs.olicyber.it/")
#print(r.text)
soup = BeautifulSoup(r.text, "html.parser")
for elem in soup.find_all("pre"):
    print(elem.getText())
