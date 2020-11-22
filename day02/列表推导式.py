# list=[]
# i=0
# while i<=10:
#     list.append(i)
#     i+=1
# print(list)
#
# list1=[]
# for a in range(10):
#     list1.append(a)
# print(list1)
#
#
# list2=[b for b in range(10)]
# print(list2)


# list1=[]
# for i in range(1,3):
#     for j in range(3):
#         list1.append((i,j))
# print(list1)
#
# list2=[(i,j)for i in  range(1,3)for j in  range(3)]
# print(list2)

# 创建⼀一个字典：字典key是1-5数字，value是这个数字的2次⽅方
dict1={i:i**2 for i in range(1,5)}
print(dict1)

# 将两个列列表合并为⼀一个字典
list1=['name','age','gender']
list2=['Tom',20,'man']
dict2={list1[i]:list2[i]for i in  range(len(list1))}
print(dict2)

# 提取字典中⽬目标数据
counts = {'MBP': 268,'HP': 125,'DELL': 200}
count1={key:value for key,value in counts.items() if value >=200}
print(count1)
