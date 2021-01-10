import requests
# 发送get请求
urlstr='https://www.wanandroid.com/user/login'
header={'user-Agent':'Mozilla/6.0'}
payload={'username':'chaoge','password':'123456'}
# 发送请求
r=requests.post(url=urlstr,data=payload,headers=header)


# 获取结果
print(r.text)
print(r.headers)