from itertools import takewhile
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import requests
a = []
url = 'http://www.insightsonindia.com/2018/01/18/secure-synopsis-16-january-2018/'
r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc,'html.parser')
bqs = soup('blockquote') # find all <blockquote> elements
for bq, bqnext in zip(bqs, bqs[1:]):
  # get elements in between
  between_it = takewhile(lambda el: el is not bqnext, bq.nextSiblingGenerator())
  # extract text
  print(''.join(getattr(el, 'text', el) for el in between_it))