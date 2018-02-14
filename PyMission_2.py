from bs4 import BeautifulSoup
from html.parser import HTMLParser
import requests
l = []
for i in range(0,3):
	url = input('Enter any url to print the actors: ')
	r = requests.get(url)
	html_doc = r.text
	soup = BeautifulSoup(html_doc,'html.parser')
	a = []
	favs = ['\nAamir Khan,             ','\nAmitabh Bachchan,             ']
	actors = soup.find_all('span',{'itemprop': 'actors'})
	rating = soup.find_all('span',{'itemprop': 'ratingValue'})[0].get_text()
	title = soup.find_all('h1',{'itemprop': 'name'})[0].get_text()
	title = title.replace(u'\xa0',u' ')
	for actor in actors:
		a.append(actor.get_text())
	for hero in a:
		if hero in favs:
			if (float(rating))>7.5 and (float(rating))<8.5:
				l.append(title)
print(l)