s1={10,20,30,40}
# print(s1)
# s2={10,10,20,20,30,40}
# print(s2)
#
# s3=set('abcdef')
# print(s3)
#
# s4=set()
# print(type(s4))
#
# s5={}
# print(type(s5))



s1={10,20}
s1.add(100)
s1.add(10)
print(s1)


s1.update([100,200])
s1.update('abc')
print(s1)

# s1.remove(10)
# print(s1)
# s1.remove(10)
# print(s1)

# s1.discard(10)
# print(s1)
#
# s1.discard(10)
# print(s1)
#
del_num=s1.pop()
print(del_num)
print(s1)

print('a' in s1)

print(10 not in s1)

