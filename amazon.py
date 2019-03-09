import requests
#模拟
note = {'user-agent':'IE 10.0'}
url= "https://www.douban.com/"
a=requests.get(url,headers=note)
print(a.status_code)
print(a.encoding)
a.encoding = a.apparent_encoding
print(a.request.headers) 