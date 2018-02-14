from bs4 import BeautifulSoup
from html.parser import HTMLParser
import requests
url = input('Enter any url to print the actors: ')
r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc,'html.parser')
actors = soup.find_all('span',{'itemprop': 'actors'})
rating = soup.find_all('span',{'itemprop':'ratingValue'})[0]
for actor in actors:
	print(actor.get_text())
print('Movie rating: ',rating.get_text())