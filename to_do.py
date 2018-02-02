from bs4 import BeautifulSoup
from html.parser import HTMLParser
import requests

url = 'http://www.insightsonindia.com/2018/01/31/secure-synopsis-28-october-2017/'
r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc,'html.parser')
a = soup.find_all(class_="pf-content")
bqs = soup('blockquote')
kids = []
count = 0
for x in a :
	for item in x.descendants:
		kids.append(item)
for k in range(0,len(kids)):
	if kids[k] in bqs:
		print(k)
