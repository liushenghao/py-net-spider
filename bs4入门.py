import requests
from bs4 import BeautifulSoup

r= requests.get("https://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo, 'html.parser')
tag = soup.a
print(tag)
print(soup.prettify())