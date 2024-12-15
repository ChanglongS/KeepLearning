# 面向对象三大特性
# 继承，封装，多态
# 封装：把现实世界的属性封装成成员变量
#      把现实世界的行为封装成成员方法

class Phone:
    # __开头表示私有成员变量
    __current_volt = None

    # 私有成员方法
    def __keep_solo_kernal(self):
        print("单核运行")

    def call_by_5G(self):
        self.__current_volt = 4.9
        if self.__current_volt < 5:
            self.__keep_solo_kernal()
            print("solo kernal running")
        else:
            print("5G is starting")


phone = Phone()
phone.call_by_5G()
