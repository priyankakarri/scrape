from bs4 import BeautifulSoup
from html.parser import HTMLParser
import requests
a=[]
url = input("Please enter the required url: ")
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