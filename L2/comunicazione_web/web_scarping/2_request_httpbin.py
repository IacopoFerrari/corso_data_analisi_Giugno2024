import requests

#GET passo i dati con querystring
#response = requests.get('https://httpbin.org/get', headers = {"Accept":"text/html"}, params={'id': 1, 'name': 'Jessa&'})
#print("url: ", response.url)
#print("Status code: ", response.status_code)
#print("Printing Entire Post Request")
#print(response.content)


##POST passo i dati con json
response = requests.post('https://httpbin.org/post', headers = {"Accept":"application/json"},)
print(response.url)
#print(response.content) # cosi da bytes
#print(response.json()) # da un dizionario

#stampo l'header della richiesta: dove posso vedere lo user-agent python-requests/2.28.1
#print(response.request.headers)