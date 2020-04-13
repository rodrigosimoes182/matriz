### import libraries
#from bs4 import BeautifulSoup
#import urllib3
#specify the url
#http = urllib3.PoolManager()
#r = http.request('GET', 'https://bing.com/covid/data/brazil')
#print(r)
import requests, json
import pandas as pd
url = "https://covid-193.p.rapidapi.com/statistics"
pais = input('insira o Pais que deseja consultar:')
querystring = {"country":pais}

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "ba4bc89c4fmsh0c24e8a4fe890c6p15c7e6jsn7d629a2821e1"
    }
response = requests.request("GET", url, headers=headers, params=querystring)
resposta = pd.DataFrame (response)
resposta.to_json((r'/Users/rodsim/Documents/matrizes/BasedeDados.json'))
print(response)
print(resposta)
#print(type(resposta))
