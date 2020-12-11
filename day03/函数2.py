# 局部变量


# def testA():
#     a=100
#     print(a)
# testA()
#
# 全局变量

# a=100
# def testA():
#     print(a)
#
# def testB():
#     a=200
#     print(a)
# testA()
# testB()
# print(f'全局变量是{a}')


# 变更全局变量

# a=100
# def testA():
#     print(a)
# def testB():
#     global a
#     a=200
#     print(a)
# testA()
# testB()
# print(f'全局变量a={a}')

# 共用全局变量
# a=100
# def testA():
#     global a
#     a=200
#     print(a)
# def testB():
#     print(a)
# testA()
# testB()

# 返回值作为参数传递
def test1():
    return 50
def test2(num):
    print(num)
ooa=test1()
test2(ooa)