import requests
urlstr='http://www.kuaidi.com/index-ajaxselectcourierinfo-773058962040428-shentong-UUCAO1609062844568.html'
s=requests.session()
r=s.get(url=urlstr)
result=r.json()
data=result['data']

print('*',r.content)
print('*****',r.json())
get_result=data[0]['context']
print(get_result)