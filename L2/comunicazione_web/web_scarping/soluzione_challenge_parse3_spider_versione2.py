import requests
from bs4 import BeautifulSoup


BASE_URL = "http://web-16.challs.olicyber.it/"


visited = []
found = False


def follow_link(url: str):
   global found
   if found:
       return
   r = requests.get(url)
   parsed = BeautifulSoup(r.content, 'html.parser')
   titles = parsed.find_all("h1")
   for title in titles:
       titleContent = title.contents[0]
       #print(titleContent)
       index = titleContent.find("flag{")
       if index != -1:
           found = True
           substr = titleContent[index:-1]
           flag_end = substr.find("}")
           flag = substr[0:flag_end + 1]
           print(flag)
           break
   visited.append(url)
   links = parsed.find_all("a")
   for link in links:
       next_url = BASE_URL + link["href"]
       if not next_url in visited:
           follow_link(next_url)
  


if __name__ == "__main__":
   follow_link(BASE_URL)