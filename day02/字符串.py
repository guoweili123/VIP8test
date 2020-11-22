# join():用一个字符或子串合并字符串

# list1=['a','b','c']
# t1=('aa','bb','cc')
# print(''.join(list1))
# print('_'.join(list1))
#
# print(''.join(t1))
# print('_'.join(t1))

# capitalize()首字母大写

# mystr='hello world and supertest and chaoge and Python'
# print(mystr.capitalize())
#
# # title():将每个单词的首字母都转换成大写
# print(mystr.title())
#
# # lower():将大写转小写
#
# print(mystr.lower())
#
# #upper():小写转大写
# print(mystr.upper())
#
#
#
# # lstrip():删除左侧空白字符
#
# mystr1='  hello world and supertest and chaoge and Python     '
# print(mystr1.lstrip())


# mystr1='hello'
# mystr2='hello12345'
# print(mystr1.isalpha())
# print(mystr2.isalpha())
#
# mystr3='12345'
# print(mystr1.isdigit())
# print(mystr2.isdigit())
# print(mystr3.isdigit())
# mystr4='12345_'
# print(mystr4.isalnum())
# print(mystr1.isalnum())
# print(mystr2.isalnum())
# print(mystr3.isalnum())
#
# mystr5='1 2 3 4 5'
# mystr6='     '
# print(mystr5.isspace())
# print(mystr6.isspace())


# 练习：从键盘输入一个姓名，判断是否在班级内，
# 如果在，则判断这个人在该班级内是否有重名的同学，
#     如果有重名则输出重名的个数
#     否则提示无重名
# 如果不在，则提示不在


student='guoweili limei liangchao guoweili tom'
name=input('请输入一个名字')
res=name.find(student)
if (student.find(name)!=-1):
    if(student.count(name)>1):
        print('有重名')
        print(f'重复次数{student.count(name)-1}')
    else:

        print('无重名')

else:
    print('不在这个班级')

