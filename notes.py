import requests
from bs4 import BeautifulSoup

url = 'http://192.168.3.45:8080/api/v2/event/log'
data = {"eventType": "AAS_PORTAL_START", "data": {"uid": "hfe3hf45huf33545", "aid": "1", "vid": "1"}}
params = {'sessionKey': '9ebbd0b25760557393a43064a92bae539d962103', 'format': 'xml', 'platformId': 1}
r = requests.post(url, params=params, json=data)

url = "http://bugs.python.org"
data={'number': 12524, 'type': 'issue', 'action': 'show'}
r = requests.post(url, data=data)

URL = 'https://www.yourlibrary.ca/account/index.cfm'
payload = {'barcode': 'your user name/login', 'telephone_primary': 'your password', 'persistent': '1' }

session = requests.session()
r = requests.post(URL, data=payload)

'''
    FORM
'''
