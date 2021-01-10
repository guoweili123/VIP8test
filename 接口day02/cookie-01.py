# 第一种方法

import requests
urlstr='https://www.wanandroid.com/user/login'
data={'username':'liangchao','password':'123456'}

# r=requests.post(url=urlstr,data=data)
# # print("***",r.text)
# # print("*",r.cookies)
# # print("**",r.headers)
#
# cookie=r.cookies
# r2=requests.get('https://www.wanandroid.com/lg/tpdp/list/0',cookies=cookie)
# print("******",r2.text,r2.status_code)



# 第二种
# s=requests.session()
# r=s.post(url=urlstr,data=data)
# r2=s.get('https://www.wanandroid.com/lg/tpdp/list/0')
# print("*",r2.text)
# print("**",r.text)



# 第三种
# r=requests.post(url=urlstr,data=data)
# print("**",r.text)
# print("***",r.cookies)
#
# cookie={'JSESSIONID':r.cookies['JSESSIONID']}
# r2=requests.get('https://www.wanandroid.com/lg/tpdp/list/0',cookies=cookie)
#
# print("****",r.text)
# print("*****",r.headers)



# 第四种

r=requests.post(url=urlstr,data=data)
# print("*",r.text)
# print("**",r.cookies)
# print("***",r.headers)
# print(r.cookies['JSESSIONID'])

header={'cookie':'JSESSIONID'+r.cookies['JSESSIONID']}

r2=requests.get('https://www.wanandroid.com/lg/tpdp/list/0',headers=header)
# print("*",r2.text)
# print("**",r2.headers)

result=r2.text.find('已完成清单')
# print(result)
# if result !=-1:
#     print('查询成功')
# else:
#     print('查询失败')


# 通过正则来查找

pattern=re.compile(r';\">(.*?)<\/h2>')
result = pattern.findall(r2.text)
print(result)

