import requests
from proxyPool.conf import HEADERS
from bs4 import BeautifulSoup


def get_page(url):
    res = requests.get(url=url, headers=HEADERS)

    try:
        soup = BeautifulSoup(res.content.decode('utf-8'), 'lxml')

    except UnicodeDecodeError:
        soup = BeautifulSoup(res.text, 'lxml')

    return soup
