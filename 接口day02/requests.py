import requests

urlstr='https://www.baidu.com'

r= requests.get(url=urlstr)

print(r.text)

