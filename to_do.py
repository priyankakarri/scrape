from bs4 import BeautifulSoup
from html.parser import HTMLParser
import requests

url = 'http://www.insightsonindia.com/2017/11/21/secure-synopsis-07-october-2017/'
r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc,'html.parser')
a = soup.find_all(class_="pf-content")[0]
answers = []
for var in a.blockquote.next_siblings:
	answers=var.get_text()
	print(answers)