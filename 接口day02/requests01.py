import  requests

urlstr='https://www.baidu.com'

r =requests.get(url=urlstr)

print(r.text)
print (r.url)
print (r.encoding)
print (r.content)
print(r.headers)
print (r.cookies)
print (r.status_code)
# print (r.json())
print (r.url)
print (r.encoding)
print (r.raw)
print (r.raise_for_status())
