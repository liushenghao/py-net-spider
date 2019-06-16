import requests
import bs4
from bs4 import BeautifulSoup
headers={
	'User-Agent':'Chrome/67.0.3396.99'
}
data={
    'cate':'realtimehot'
}
url = 'https://s.weibo.com/top/summary'
try:
    r= requests.get(url,params=data,headers=headers)
    r.raise_for_status()
    r.encoding=r.apparent_encoding 
except:
    r.text=' '

soup = BeautifulSoup(r.text,"html.parser")
tag = soup.select('tbody')
for t in tag:
    rank = t.find("td",class_="td-01 ranktop").string
    # keyword = t.find("td",calss_="td-02").a.string
    # href = t.find("td",class_="td-02").a.get('herf')
    # click = t.find("td",class_="td-02").span.string
    # print(rank,keyword,href,click)
    print(rank)
    print('===========')