#This code get covid-19 information from a API and save data to plote 
import requests, json
import pandas as pd
from pandas import read_json
from pandas.io.json import json_normalize
#connect to API, authenticate and alocate as dataframe
url = "https://covid-193.p.rapidapi.com/statistics"
#pais = input('insira o Pais que deseja consultar:')
pais = 'Brazil'
querystring = {"country":pais}

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "ba4bc89c4fmsh0c24e8a4fe890c6p15c7e6jsn7d629a2821e1"
    }
response = requests.request("GET", url, headers=headers, params=querystring)
leitura = response.text.split(',')
resposta = pd.DataFrame(response)
#ETL with API data
localjson='/Users/rodsim/Documents/matrizes/BasedeDados.json'
resposta.to_json(localjson, orient='values')
'''leitura = read_json(localjson)
arrumajson = json_normalize(response)'''
#Prit information to confirm if everything is fine
for i in leitura:
   print(i)
print(resposta)
#end of code
