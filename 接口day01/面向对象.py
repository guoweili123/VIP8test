# class digua():
#     def __init__(self):
#         self.cook_time=0
#         self.cook_static='生的'
#         self.tiaoliao=[]
#
#     def cook(self,time):
#         self.cook_time += time
#         if 0<=elf.cook_time<3:
#             self.cook_static='生的'
#         elif <=self.cook_time<5:
#             self.cook_static='半生不熟'
#         elif 5<=self.cook_time<8:
#             self.cook_static='熟了'
#         else self.cook_time>=8:
#             self.cook_static='糊了'
#     def __str__(self):


# 类： 房子
# 、家具
# 属性：面积、剩余面积，地址，哪些家具
#      名称、面积



# class Jiajv():
#     def __init__(self,name,area):
#         self.name=name
#         self.area=area
# class Hose():
#     def __init__(self,addres,area):
#         self.addres=addres
#         self.area=area
#         self.free_area=area
#         self.jiajv=[]
#     def __str__(self):
#         return  f'您的房子在{self.addres},有{self.area}平，还剩{self.free_area}平,家具有{self.jiajv}；加油会实现的'
#
#     def add_jiajv(self,item):
#         if self.free_area >= item.area:
#             self.jiajv.append(item.name)
#             self.free_area -= item.area
#         else:
#             print('没地方了')
#
# bed=Jiajv('双人床',4)
# jia1=Hose('北京',110)
# print(jia1)
#
# jia1.add_jiajv(bed)
# print(jia1)
#
# safa = Jiajv ('高档沙发',10)
# jia1.add_jiajv(safa)
# print(jia1)
#
# fbx = Jiajv('fbx',200)
# jia1.add_jiajv(fbx)
# print(jia1)



'''
类：房子
    属性：总面积，剩余面积，家具列表
    方法：添加家具
        参数item
        比较面积
类：家具
    属性：名称和面积
    方法：无
'''
class Giaju():
    #家具属性
    def __init__(self,name,cover_area):
        self.name=name
        self.cover_area=cover_area

class House():
    #房子属性
    def __init__(self,area):
        self.area=area
        self.free_area=area
        self.jj=[]
    #添加家具
    def add_jiaju(self,item):
        if self.free_area>=item.cover_area:
            self.jj.append(item.name)
            self.free_area-=item.cover_area
        else:
            print('家具太大，搬不进去')
    def __str__(self):
        return f'房子的总面积{self.area}，剩余面积{self.free_area}，家具列表{self.jj}'

bed=Giaju('床',10)
house1=House(100)
house1.add_jiaju(bed)
print(house1)
