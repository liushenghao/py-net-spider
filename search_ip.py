import requests
url1="http://ip.tool.chinaz.com/"
url2="http://www.ip138.com/"
net = 'www.baidu.com'#input('输入网站')
try:
    r=requests.get(url1+net)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    #提取其中的IP地址net2（使用bs4）
    net2='123'
    p=requests.get(url2+net2)
    p.raise_for_status()
    p.encoding=r.apparent_encoding
    """找到里面的位置/信息等然后
    print输出或者存到某个文件"""
except:
    print("error")