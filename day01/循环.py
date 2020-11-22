#循环遍历
# n=0
# #循环条件
# while n<5:
#     #循环体
#     print('媳妇，我错了,第%d次打印 '%(n+1))
#     #循环变化
#     n +=1
#

#1-100累加

# n=1
# sum=0
# while n<=100:
#     sum=sum+n
#     n+=1
# print('sum',sum)

#1-100之间偶数的和
n=1
sum=0
while n<=100:
    if n%2==0:
        sum=sum+n
    n+=1
print('1-100减偶数加是',sum)