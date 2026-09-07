import requests
from bs4 import BeautifulSoup

url = "https://time.com/archive/6597365/are-hyperlocal-news-sites-replacing-newspapers/"
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')
test = soup.find_all('p')
for p in test:
    print(p.text)