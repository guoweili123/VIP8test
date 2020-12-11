# 3+2+1
# def sum_number(num):
#     if num ==1:
#         return 1
#     return num+sum_number(num-1)
#
# sum_result = sum_number(3)
# print(sum_result)


# def fn1():
#     return 200
# print(fn1)
# print(fn1())
#
# # 匿名函数
# fn2=lambda:100
# print(fn2)
# print(fn2())


# add01=lambda a,b:a+b
# print(add01(1,2))



students=[{'name':'TOM','age':20},
          {'name':'ROSE','age':19},
          {'name':'Jack','age':22}]

# students.sort(key=lambda x:x['name'])
# print(students)
students.sort(key=lambda x:x['name'],reverse=True)
print(students)
# students.sort(key=lambda x:x['age'])
# print(students)
