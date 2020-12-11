# 关键字参数
# def user_info(name,age,gender):
#     print(f'您的名字是{name},年龄是{age},性别是{gender}')
#
# user_info(name='小明',gender='man',age=20)


# 缺省参数
# def user_info01(name,age=18,gender='man'):
#     print(f'您的名字是{name},您的年龄是{age},性别是{gender}')
#
# user_info01('gwl')
#
# user_info01('大侠',20)
#
# user_info01('天天',22,'women')

# 不定长参数
#
# def user_info(*args):
#     print(args)
#
# user_info('TOM')
# user_info('TOM',18)
# user_info()
# list1=[1,2,3]
# user_info(*list1)
#
# 包裹关键字传递

# def user_info(**kwargs):
#     print(kwargs)
# user_info(name='TOM',age=18,gender='男')
#
# dict1={'name':'TOM','age':18}
# user_info(**dict1)



# 拆包
dict1={'name':'TOM','age':18}
a,b=dict1
print(a)
print(b)
print(dict1[a])
print(dict1[b])

