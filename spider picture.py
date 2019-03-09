import requests
import os
root = "H:/python项目/测试保存项/"
url = "http://img0.dili360.com/ga/M00/46/FC/wKgBy1iv0WmAaXa1AE7LkZQs2kI077.tub.jpg"
path = root+url.split('/')[-1]
note={'user-agent':'IE 10.0'}
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r= requests.get(url,headers = note)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print('save successfully')
except:
    print("spider error")