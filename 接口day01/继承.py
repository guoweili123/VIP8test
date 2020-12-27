# 单继承
#
# class Shifu ():
#     def __init__(self):
#         self.kongfu=['五香煎饼果子方法']
#
#     def moke_cake(self):
#         print(f'技术是{self.kongfu}')
#
#
# class Tudi(Shifu):
#     pass
#
# xiaoming=Tudi()
# print(xiaoming.kongfu)
# xiaoming.moke_cake()




# 多重继承
# class  Master():
#     def __init__(self):
#         self.kongfu='[古法煎饼果子配方]'
#     def make_cake(self):
#         print(f'运用{self.kongfu}制作煎饼果子')
# class School():
#     def __init__(self):
#         self.kongfu='[黑马煎饼果子配方]'
#     def make_cake(self):
#         print(f'运用{self.kongfu}制作煎饼果子')
# class prentice(School,Master):
#     def __init__(self):
#         self.kongfu='[独家煎饼果子方法]'
#     def make_cake(self):
#         print(f'运用{self.kongfu}制作煎饼果子')
#
# daqiu=prentice()
# print(daqiu.kongfu)
# daqiu.make_cake()
#
# print(prentice.__mro__)



# 子类调用父类的同名方法

#
# class Master():
#     def __init__(self):
#         self.kongfu='[古法煎饼果子配方]'
#     def make_cake(self):
#         print(f'运用{self.kongfu}制作煎饼果子')
# class School():
#     def __init__(self):
#         self.kongfu='[黑马煎饼果子配方]'
#     def make_cake(self):
#         print(f'运用{self.kongfu}制作煎饼果子')
# class prentice(School,Master):
#     def __init__(self):
#         self.kongfu='[独创]'
#     def make_cake(self):
#         self.__init__()
#         print(f'运用{self.kongfu}制作')
#     def make_master_cake(self):
#         Master.__init__(self)
#         Master.make_cake(self)
#
#     def make_school_cake(self):
#         School.__init__(self)
#
#         School.make_cake(self)
#
# daqiu = prentice()
# daqiu.make_cake()
# daqiu.make_master_cake()
# daqiu.make_school_cake()
# daqiu.make_cake()




# 私有方法

# class Master():
#     def __init__(self):
#         self.kongfu='[古法煎饼果子]'
#     def make_cake(self):
#         print(f'运用{self.kongfu}制作')
# class School():
#     def __init__(self):
#         self.kongfu='[香辣]'
#     def make_cake(self):
#         print(f'运用{self.kongfu}制作')
# class prentice(School,Master):
#     def __init__(self):
#         self.kongfu=['独家']
#         self.__money=20000
#     def __info_print(self):
#         print(self.kongfu)
#         print(self.__money)
#     def make_cake(self):
#         self.__init__()
#         print(f'运用{self.kongfu}')
#     def make_master_cake(self):
#         Master.__init__(self)
#         Master.make_cake(self)
#     def make_school_cake(self):
#         School.__init__(self)
#         School.make_cake(self)
# class Tusun(prentice):
#     pass
#
# daqiu = prentice()
# print(daqiu.__money)
# daqiu.__info_print()
# xiaoqiu =Tusun()
# print(xiaoqiu.__money)
# xiaoqiu.__info_print()




# 类属性

# class man():
#     sex='男'
#
# xiaoming=man()
# xiaogang=man()
#
# print(man.sex)
# print(xiaoming.sex)
# print(xiaogang.sex)
#
# man.sex='女'
#
# print(man.sex)
# print(xiaoming.sex)
# print(xiaogang.sex)
#
#
# xiaoming.sex = 66
# print(man.sex)
# print(xiaoming.sex)
# print(xiaogang.sex)
#


# 类方法
#
class Dog():
    __tooth=10

    @classmethod
    def get_tooth(cls):
        return cls.__tooth


wangcai =Dog()
result= wangcai.get_tooth()
print(result)



# 静态方法

# class Dog():
#     @staticmethod
#     def info_print():
#         print('这是个狗类')
# wangcai=Dog()
# wangcai.info_print()
# Dog.info_print()



