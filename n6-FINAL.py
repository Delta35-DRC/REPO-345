import requests
from bs4 import BeautifulSoup
import sqlite3

connection = sqlite3.connect('table250v.db', 5)
cur = connection.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, value TEXT);')

quote = input('search: ')
html = requests.get(f'https://www.bing.com/search?q={quote}')
soup = BeautifulSoup(html.content, 'lxml')
url = soup.select('cite')
for value in url:
    print(value)
    cur.execute('INSERT INTO data (value) VALUES (?);', (value,))

connection.commit()
cur.execute('SELECT value, COUNT(*) AS count FROM data GROUP BY value ORDER BY count DESC')
rows = cur.fetchall()
connection.commit()
connection.close()
