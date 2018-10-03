import requests
from bs4 import BeautifulSoup

def trade_spider(url) :
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for link in soup.findAll('a', {'class' : 'item-name'}) :
        href = link.get('href')
        title = link.string
