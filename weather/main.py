import requests
from bs4 import BeautifulSoup

data = requests.get('https://darksky.net/forecast/28.6741,77.438/us12/en')

soup = BeautifulSoup(data.text, 'html.parser')
soup.prettify()

print(soup.body.div.attrs)
