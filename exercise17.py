import requests
from bs4 import BeautifulSoup

url = "https://www.nytimes.com/"
headers = {'User-Agent': 'Mozilla/5.0'}
r = requests.get(url, headers=headers)
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')
titles = soup.find_all('p', 'indicate-hover')
for t in titles:
    print(t.string)