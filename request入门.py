import requests
def req():  
    try:
        b = requests.get('https://www.baidu.com')
        b.raise_for_status()
        b.encoding = b.apparent_encoding
        return b.txt
    except:
        return 'error'
if __name__ == "__main__":
    print(req())