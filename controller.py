import csv
import requests
from requests import HTTPError
import pandas as pd
from bs4 import BeautifulSoup

URL = "https://coinmarketcap.com/pt-br/trending-cryptocurrencies/"

def web_crawl(URL):
    try:
        response = requests.get(URL)
        response.raise_for_status()
    except HTTPError as exc:
        print(exc)
    else:
        content = response.text
        return content

def save_page(page_file):
    with open('./data/page.html',mode='w',encoding='utf8') as f:
        f.write(page_file)

def extraction():
    page = BeautifulSoup(open('./data/page.html',mode='r',encoding='utf8'),'html.parser')
    extract_content = []
    table = page.find('table', {'class':'sc-66133f36-3 hLiUvb cmc-table  '}) #Table extraction
    header = table.find_all('p')
