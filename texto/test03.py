### import libraries
#from bs4 import BeautifulSoup
#import urllib3
#specify the url
#http = urllib3.PoolManager()
#r = http.request('GET', 'https://bing.com/covid/data/brazil')
#print(r)

import subprocess, string

processo = subprocess.Popen("docker ps -a", shell=True, stdout=subprocess.PIPE)
processo_return = str(processo.stdout.read())
pedaco_string =  processo_return.split(" ")
ultima_parte =pedaco_string[-1]
final_str=ultima_parte[0:-3]
print(final_str)