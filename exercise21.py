import requests
from bs4 import BeautifulSoup

txt_name = input("Enter file name: ")

url = "https://www.nytimes.com/"
headers = {'User-Agent': 'Mozilla/5.0'}
r = requests.get(url, headers=headers)
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')
titles = soup.find_all('p', 'indicate-hover')


with open(txt_name, 'w') as open_file:
    for t in titles:
        open_file.write(t.string)

