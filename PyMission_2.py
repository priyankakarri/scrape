from bs4 import BeautifulSoup
from html.parser import HTMLParser
import requests
url = input('Enter any url to print the actors: ')
r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc,'html.parser')
actors = soup.find_all('span',{'itemprop': 'actors'})
for actor in actors:
	print(actor.get_text())