from bs4 import BeautifulSoup
from html.parser import HTMLParser
import requests
links = []
main_url = input("Enter the main url to get the other urls from: ")
r1 = requests.get(main_url)
html_doc = r1.text
soup1 = BeautifulSoup(html_doc,'html.parser')
urls = soup1.find_all('td',{'class':'titleColumn'})
ratings = soup1.find_all('td',{'class':'ratingColumn imdbRating'})
for url,rating in zip(urls,ratings):
	for rating in ratings:
		if (float(rating.get_text()))>7.5 and (float(rating.get_text()))<8.5:
			links.append('http://www.imdb.com'+str(url.a['href']))
l=[]
for link in links:
	r2 = requests.get(link)
	html_docu = r2.text
	soup2 = BeautifulSoup(html_docu,'html.parser')
	a = []
	favs = ['\nAamir Khan,             ','\nAmitabh Bachchan,             ']
	actors = soup2.find_all('span',{'itemprop': 'actors'})
	title = soup2.find_all('h1',{'itemprop': 'name'})[0].get_text()
	title = title.replace(u'\xa0',u' ')
	for actor in actors:
		a.append(actor.get_text())
	for fav in a:
		if fav in favs:
				l.append(title)
print(l)