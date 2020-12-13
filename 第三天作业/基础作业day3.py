# 1.把上次课的作业重新编程（不能看着答案，把分析过程写出来再敲代码）

#  99乘法表；
# a=1
# while a<10:
#     b=1
#     while b<=a:
#         print(f'{b}*{a}={a*b}',end= '    ')
#         b += 1
#     print()
#     a+=1
# #
#  质数判断；
# num = int(input('请输入一个数'))
# n=2
# while n < num:
#     if num % n ==0:
#         print('不是质数')
#         break
#     n +=1
# else:
#     print(f'{num}是质数')

#
#  三角形打印；
## i = 1
# while i <= 5:
#     j = 1
#     while j <= i:
#         print('*',end='')
#         j += 1
#     print()
#     i += 1

#
#  斐波那契数列
# 第一种：
# l = [1,1]
# i = 0
# j = int(input('请输入数列长度：'))
# while i <= j:
#     c = l[i] + l[i+1]
#     l.append(c)
#     i += 1
# print(l)

# 第二种：

i = int(input('输入第几位数：'))
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)
fib_result = fib(i)
print(fib_result)


# 2.打印由*组成的菱形，该菱形一共7行，已在群里发了，大家自己找图
def lx(n):
    j=1
    while j<=n:
        if j<n:
            s1='*'*j
            print(s1.center(n))
        else:
            m=n
            while m>0:
                s2='*'* m
                print(s2.center(n))
                m-=2
        j+=2
lx(7)

# def lingxing(n):
#     j = 1
#     while j <= n:
#         if j < n:
#             s1 = '*' * j
#             print(s1.center(n))
#         else:
#             m = n
#             while m > 0:
#                 s2 = '*' * m
#                 print(s2.center(n))
#                 m -= 2
#         j += 2
# lingxing(7)



# 3.使用列表推导式生成能被5整除的数（100以内）

# list1 = [i for i in range(101) if i % 5 == 0]
# print(list1)


# 4.有两个列表，一个是学生姓名，一个是学生的年龄，生成一个字典，key为姓名，value为年龄

a=['郭魏利']
b=[18]
c={a[i]:b[i] for  i in range (len(a))}
print(c)



# 5.开发一个注册系统，
# 页面：
# ----------------
# *   1-新增用户
# *   2-查询用户
# *   3-删除用户
# ----------------
# 功能1：新增学生信息（姓名和年龄）通过键盘，如果学生已经存在提示用户已存在
# 功能2：查询学生信息
# 功能3：删除学生信息