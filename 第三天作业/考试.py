# list1=[1,2,3,4,5,5,2,3,2,4]
# list2=[]
# for i in list1:
#     list2.append(i)
#     if list2.count(i) >1:
#         list2.remove(i)
# print(list2)




#
# list01=[i for i in  range(101) if i % 3 == 0]
# print(list01)


# list01=[]
# for i in range(101):
#     if i %3 == 0:
#         list01.append(i)
# print(list01)

# str01='welocme to super&Test'
# str02=str01.split(' ')[0]
# print(str02[::-1],end='   ')
# str03=str01.split(' ')[1]
# print(str03[::-1],end='   ')
# str04=str01.split(' ')[-1]
# print(str04[::-1],end='')
#
# print(str02)

list001=[]
i = int(input('请输入一个数'))
def f01(n):
    if n==1 or n==2:
        return  1
    return  f01(n-1)+f01(n-2)
a =f01(i)
list001.append(a)
print(list001)


