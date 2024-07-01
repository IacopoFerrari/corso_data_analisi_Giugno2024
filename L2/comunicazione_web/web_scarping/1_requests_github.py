import requests
re = requests.get('https://api.github.com')
#print(re.status_code)
#print(re.content)
#print(re.encoding)
#print(re.text)
#print(type(re.text))
#print(re.json())
#print(type(re.json()))
#print(re.headers)

response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
        #headers={'Accept': 'text/html'},
)

#print(response.content)
#print(response.status_code)
json_response = response.json()
repository = json_response['items'][0]
#print(f'Repository name: {repository["name"]}')  # Python 3.6+
#print(f'Repository description: {repository["description"]}')  # Python 3.6+
#print(json_response['items'][0])

""" 
nel caso avessi un proxy tra me e la rete:


proxies = {
    'http': 'http://{}:{}@ip_proxy:porta'.format('<user_proxy>', '<password_proxy>'),
    'https': 'http://{}:{}@ip_proxy:porta'.format('<user_proxy>', '<password_proxy>'),
}

"""

s = requests.Session()
res = s.get("https://api.github.com/user", auth=("iacopoferrari92@gmail.com","..."))
res = s.get("https://api.github.com/user")
print(res.status_code)
print(res.content)
#print(res.text)