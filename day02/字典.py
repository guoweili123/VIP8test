# 有数据字典
# dict1={'name':'Tom','age':20,'gender':'男'}
#  空字典
# dict2 ={}
# dict3 = dict()


# 增加
dict1={'name':'Tom','age':20,'gender':'男'}
# dict1['name']='Rose'
# print(dict)
# dict1['id'] = 110
# print(dict1)

# 删除
# del  dict1['gender']
# print(dict1)
# dict1.clear()
# print()

# 查找
# print(dict1['name'])
# print(dict1[id])
#
# get
# print(dict1.get('name'))
# print(dict1.get('id',110))
# print(dict1.get(id()))


# print(dict1.keys())
#
# print(dict1.values())
#

# print(dict1.items())

# print(dict1.keys(),type(dict1.keys()))
#
# print(list(dict1.keys()))



for item in  dict1.items():
    print(item)


for key,value in dict1.items():
    print(f'{key}={value}')