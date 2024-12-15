# 作者: 王道 龙哥
# 2022年03月22日10时14分32秒
class Goods:

    @property
    def price1(self):
        print('@property')

    @price1.setter
    def price1(self, value):
        print(value)
        print('@price.setter')

    @price1.deleter
    def price1(self):
        print('@price.deleter')

# ############### 调用 ###############


obj = Goods()
obj.price1          # 自动执行 @property 修饰的 price 方法，并获取方法的返回值
obj.price1 = 123    # 自动执行 @price.setter 修饰的 price 方法，并将  123 赋值给方法的参数
del obj.price1      # 自动执行 @price.deleter 修饰的 price 方法