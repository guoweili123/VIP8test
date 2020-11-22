# 输出
# age=18
# name='TOM'
# weight=75.5
# student_id=1
#
# print('我的名字是%s'%name)
#
# print('我的年龄是%d'%age)
#
# print('我的学号是%04d'%student_id)
# print('我的体重是%.2f'%weight)
# print('我的名字是%s，今年%d岁了'%(name,age))
#
# print('我的名字是%s,明年我%d岁了'%(name,age+1))
# print(f'我的名字是{name}，明年{age+1}s岁了')

# 输出

# password=input('请输入您的密码')
# print(f'您输入的密码是{password}')
# print(type(password))

# 转换类型

# 1. float()  转换成浮点型
num1 = 1
print(float(num1))
print(type(float(num1)))

# 2. str() 转换成字符串串类型
num2 = 10
print(str(num2))
print(type(str(num2)))

# 3. tuple() 转换成元组
list1 = [10, 20, 30]
print(tuple(list1))
print(type(tuple(list1)))

# 4. list()   转换成列表
t1 = (100, 200, 300)
print(list(t1))
print(type(list(t1)))
# 5. eval()  将字符串串中的数据转换成Python表达式原本类型
str1 = '10'
str2 = '[1, 2, 3]'
str3 = '(1000, 2000, 3000)'
print(type(eval(str1)))
print(type(eval(str2)))
print(type(eval(str3)))


