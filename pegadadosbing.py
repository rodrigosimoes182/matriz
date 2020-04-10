import urllib3
import numpy as np
from bs4 import BeautifulSoup

#pegando dados do Bing
http = urllib3.PoolManager()
r = http.request('GET', 'https://www.bing.com/covid')
data = r.data.decode('utf-8')
soup = BeautifulSoup(data,'html.parser')
#achando o Brazil no html
p = soup.find(class_='BodyText')
pais_itens = p.find_all('a')
for p in pais_itens:
    print(p.prettify())
caminho = open('bingcovid','w')
#escrevendo o arquivo como texto
caminho.write(data)
print(data)