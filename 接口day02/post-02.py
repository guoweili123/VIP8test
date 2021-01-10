import requests
# 发送post请求
urlstr='https://www.wanandroid.com/user/login'
payload={'username':'chaoge','password':'123456'}
# 发送请求
r=requests.post(url=urlstr,data=payload)
# 获取结果
print(r.text)
# 查看类型后为字典类型，r.json将resquests中的返回的json处理成了dict
print(type(r.json()))
# 通过dict-key来访问对应的值
print(r.json())


