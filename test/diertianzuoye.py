# # 第一题（1、三角形）
# a = 0
# while a <= 4:
#     b = 0
#     while b <= a:
#         print('*',end=' ')
#         b += 1
#     print()
#     a += 1

# 第一题（2、99乘法表）
# a=1
# while a <= 9:
#     b=1
#     while b <= a:
#         print(f'{b}*{a}={a*b}', end='\t')
#         b += 1
#     print()
#     a += 1


# 第二题（求100以内能被3整除的数，并将作为列表输出）
# a=0
# while a <=100:
#     if a % 3 == 0:
#         print(a,end='\t')
#     a += 1


#第三题 （列表[1,2,3,4,3,4,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表）
# list1 = [1,2,3,4,3,4,2,5,5,8,9,7]
# list2 = []
# for i in list1:
#     list2.append(i)
#     if list2.count(i)> 1:
#         list2.remove(i)
# print(list2)

#第四题 （求斐波那契数列 1 1 2 3 5 8 13 ……）(有疑问)

# a1=1
# a2=1
#
# n=1
# print(a1,a2,end=',')
# while n <10:
#
#     a2= a1+a2
#     print(a2, end=',')
#     a1 = a2
#     a2 = a1 + a2
#
#     n += 1

#第五题 (求100以内的质数（只能被1和它本身整除）)

# a=1
# while a <=100:
#     b=1
#     list=[]
#     while b<=a:
#         if a%b==0:
#             list.append(b)
#         b +=1
#     if len(list) ==2:
#         print(a,end=' ')
#     a +=1


#第六题 （有一堆字符串“aabbbcddef”打印出不重复的字符串结果：cef）

# str = 'aabbbcddef'
# for i in str:
#     if str.count(i) == 1:
#         print(i,end='')
# print()

#第七题： 有一堆字符串，“welocme to super&Test”，打印出superTest，不能查字符的索引

# str='welocme to super&Test'
#
# for i in str
#     if i == &
#     print()

#第八题（有一堆字符串，“welocme to super&Test”，打印出tseT&repus ot ……全部单词原位置反转）
# str='welocme to super&Test'
# print(str[::-1])

#第九题（有一堆字符串，“abcdef”，将收尾反转，结果：fedcba，不能使用现有的函数或方法，自己写算法实现）
# str='abcdef'
# 第一种方法
# print(str[::-1])
# 第二种方法
# num = -1
# while num>= -len(str):
#     print(str[num],end='')
#     num -=1
# print()


# 第十题（有一堆字符串，“aabbbcddef”，输出abcdef）
str='aabbbcddef'
i=0
print(str[i],end='')
while i<len(str)-1:
    if str[i]!= str[i+1]:
        print(str[i+1],end='')
    i +=1
print()






