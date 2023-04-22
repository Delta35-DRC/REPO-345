import requests
from bs4 import BeautifulSoup
import sqlite3

connection = sqlite3.connect('table410w.sl3', 5)
cur = connection.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS data (times TEXT, value REAL);')


def search():
    quote = input()
    html = requests.get(f'https://www.bing.com/search?q={quote}')
    soup = BeautifulSoup(html.content, 'lxml')
    url = soup.find('.b_algo, cite')
