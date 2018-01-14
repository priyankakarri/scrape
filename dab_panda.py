from bs4 import BeautifulSoup
import requests
url = 'https://www.biographyonline.net/people/successful.html'
req = requests.get(url)
html_doc = req.text
soup = BeautifulSoup(html_doc)
pics = soup.find_all('img')
for link in pics:
	print(link.get('src'))