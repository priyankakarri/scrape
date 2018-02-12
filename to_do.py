from bs4 import BeautifulSoup
from html.parser import HTMLParser
import requests
def func_name(url):
	r = requests.get(url)
	html_doc = r.text
	soup = BeautifulSoup(html_doc,'html.parser')
	a = soup.find_all(class_="pf-content")[0]
	answers = []
	for var in a.blockquote.next_siblings:
		answers=var.get_text()
		print(answers)
	return answers
