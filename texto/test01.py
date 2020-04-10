# import libraries
from bs4 import BeautifulSoup
import urllib3
# specify the url
http = urllib3.PoolManager()
r = http.request('GET', 'https://www.bing.com/covid')
# query the website and return the html to the variable 'page'
#page = urllib3.request.urlopen(urlpage)
# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')
# find product items
# at time of publication, Nov 2018:
# results = soup.find_all('div', attrs={'class': 'listing category_templates clearfix productListing'})
# updated Nov 2019:
results = soup.find_all('div', attrs={'class': 'lastUpdate'})
print('Number of results', len(results))