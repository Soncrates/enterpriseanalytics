import requests
import re
from bs4 import BeautifulSoup

def _content(url,regex) :
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    regex = re.compile(regex, re.IGNORECASE)
    soup.find_all(string=regex)

def _spider(url) :
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for link in soup.findAll('a') :
        href = link.get('href')
        title = link.string
        yield href, title

def _spider_list(*url_list) :
    ret = {}
    for url in url_list :
        for href, title in _spider(url) :
            ret[href] = title
    return ret

def _spider_main(depth, *url_list) :
    ret = _spider_list(*url_list)
    iter_list = range(0,4)
    for iter in iter_list :
        _ret = _spider_list(*ret.keys())
        ret.update(_ret)
    return ret

if __name__ == "__main__" :
   url_list = [""]
   ret = _spider_main(5,*url_list)
