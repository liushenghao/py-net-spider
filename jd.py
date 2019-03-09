import requests
url="https://item.taobao.com/item.htm?id=541685684057&ali_trackid=2:mm_26632614_0_0:1552044043_239_402472960&spm=a21bo.7925826.192013.3.3de84c0dtmvLfH"
try:
    j=requests.get(url)
    j.raise_for_status()
    #返回200时候不产生异常
    j.encoding= j.apparent_encoding
    print(j.text[:2000])
except:
    print("error")
