import requests
from bs4 import BeautifulSoup

r= requests.get("https://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo, 'html.parser')
b= soup.body
print(len(b.contents),b.children)