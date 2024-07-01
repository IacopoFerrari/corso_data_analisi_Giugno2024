import requests
from bs4 import BeautifulSoup as bs
r = requests.get("http://web-13.challs.olicyber.it/")
soup = bs(r.text, 'html.parser')
print(r.text)
flag = ""
for word in soup.find_all('span'):
   flag += str(word.getText())
print("flag{"+flag+"}")