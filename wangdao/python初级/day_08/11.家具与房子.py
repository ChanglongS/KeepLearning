#!/usr/bin/python
# author luke
# 2022年02月22日

class HouseItem:

    def __init__(self, name, area):

        self.name = name
        self.area = area

    def __str__(self):

        return "[%s] 占地 %.2f" % (self.name, self.area)


class House:

    def __init__(self, house_type, area):

        self.house_type = house_type
        self.area = area

        # 剩余面积
        self.free_area = area

        # 家具名称列表
        self.item_list = []

    def __str__(self):

        # Python 能够自动的将一对括号内部的代码连接在一起
        return ("户型：%s\n总面积：%.2f[剩余：%.2f]\n家具：%s"
                % (self.house_type, self.area,
                   self.free_area, self.item_list))

    def add_item(self, item:HouseItem): #加注解是为了告知集成开发环境变量类型

        print("要添加 %s" % item)
        # 判断剩余面积要够放家具，否则不能添加
        if self.free_area>=item.area:
            self.item_list.append(item)  #添加家具到列表中
            self.free_area-=item.area  #减少房间剩余面积
        else:
            print('没地方放了')

if __name__ == '__main__':
    # 1. 创建家具
    bed = HouseItem("席梦思", 4)
    chest = HouseItem("衣柜", 2)
    table = HouseItem("餐桌", 1.5)

    house=House('小三房',60)
    house.add_item(bed)
    house.add_item(chest)
    print(house)