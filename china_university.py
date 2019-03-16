import requests
import bs4
from bs4 import BeautifulSoup
# r = requests.get("http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html")
# print(r.status_code)

#1获取内容
def getHTML(url):
    try:
        r= requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return " "
#2提取有用信息，并存储到合适结构
def findInfo(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds= tr('td')
            ulist.append([tds[0].strting],tds[1].string,tds[2].string)
#3利用数据结构输出
def printData(ulist,num):
    print("{:^10}\t{:^6}\t{:^10}".format('rank','name','score'))
    for i in range(num):
        l=ulist[i]
        print(print("{:^10}\t{:^6}\t{:^10}".format(l[0],l[1],l[2])))
    
#主函数
def main():
    info=[]
    url="http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html"
    html=getHTML(url)
    findInfo(info,html)
    printData(info,20)

if __name__ =="__main__":
    main()