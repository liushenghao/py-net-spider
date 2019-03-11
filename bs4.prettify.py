import requests
from bs4 import BeautifulSoup
r = requests.get("https://python123.io/ws/demo.html")
webcode = r.text
soup= BeautifulSoup(webcode,"html.parser")
print(soup.prettify())