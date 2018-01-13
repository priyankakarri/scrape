from bs4 import BeautifulSoup
import requests
url = 'https://www.biographyonline.net/people/successful.html'
r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc)
pics = soup.find_all('img')
for link in pics:
	print(link.get('src'))