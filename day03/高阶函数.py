# def sum_num(a,b,f):
#     return f(a)+f(b)-a+b
# resykt=sum_num(-1.1,2.1,abs)
# print(resykt)

# 内置高阶函数

# list1=[1,2,3,4]
# def func(x):
#     return x**2
# result =map(func,list1)
# print(list(result))


import  functools
list01=[1,2,3,4,5]
def func(a,b):
    return  a+b
result=functools.reduce(func,list01)
print(result)