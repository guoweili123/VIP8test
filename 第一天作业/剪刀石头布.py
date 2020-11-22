# 剪刀1
# 石头2
# 布3

# computer=电脑   player=玩家


import random
computer =random.randint(1, 3)
print('电脑出的是%d'% computer)
player=int(input('请出拳：1剪刀，2石头，3布'))
if((player ==1)and(computer ==2))or((player ==2)and (computer ==3))or((player == 3)and(computer ==1)):
    print('玩家胜利')
elif player == computer:
    print('平局')
else:
    print('电脑胜利')
