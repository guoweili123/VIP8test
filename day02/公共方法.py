# range()

# 1 2 3 4 5 6 7 8
# for i in range(1,20,1):
#     print(i)

list1=['a','b','c','d']
for i in enumerate(list1):
    print(i)
for index,char in enumerate(list1,start=0):
    print(f'下标是{index},对应的字符是{char}')