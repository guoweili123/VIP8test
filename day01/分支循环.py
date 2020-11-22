
#if语句
# age = int(input('请输入您的年龄'))
# if age >= 18:
#     print(f'年龄是{age},可以上网')
# print('系统关闭')

# if……else

# age1 = int(input('请输入您的年龄'))
# if age1>18:
#     print(f'年龄是{age1}，可以上网')
# else:
#     print(f'您还未成年，不可上网')
# print('系统关闭')


#多重判断
# age = int(input('请输入您的年龄'))
# if age<=18:
#     print(f'你的年龄是{age},是童工，不合法')
# elif age>18 and age<=60:
#     print(f'您的年龄是{age}，可以工作')
# elif age >60:
#     print(f'您的年龄是{age},您可以退休啦')



# if嵌套



money = int(input('有多少钱'))
if money >=1:
    print(f'您的钱是{money}，可以上车，但不找零')
    seat = int(input('有几个空座'))
    if seat>=1:
        print(f'您已经上车，有{seat}个空座位，可以坐下')
    else:print('没有空座')
else:
    print(f'您有{money}元，不可以上车')