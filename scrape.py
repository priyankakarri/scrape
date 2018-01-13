from bs4 import BeautifulSoup
from html.parser import HTMLParser
import requests
a=[]
url = 'http://www.insightsonindia.com/category/secure-synopsis/'
r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc,"html.parser")
heads = soup.find_all('h2',{"class":"post-title entry-title"})
for head in heads:
	final = head.find_all('a',{'rel':'bookmark'})
	a.append(final)
for link in a:
	for address in link:
		print(address.get('href'))
for num in range(2,4):
	b = []
	urlx = 'http://www.insightsonindia.com/category/secure-synopsis/page/'+ str(num) +'/'
	r = requests.get(urlx)
	html_doc = r.text
	soup = BeautifulSoup(html_doc,"html.parser")
	heads = soup.find_all('h2',{"class":"post-title entry-title"})
	for head in heads:
		final = head.find_all('a',{'rel':'bookmark'})
		b.append(final)
	for link in b:
		for address in link:
			print(address.get('href'))