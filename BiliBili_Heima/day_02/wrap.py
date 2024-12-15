class Phone:
    __is_5G_enable = None

    def __check_5G_enable(self):
        self.__is_5G_enable = False
        if self.__is_5G_enable:
            print("5G enabled")
        else:
            print("5G disabled")

    def call_by_5G(self):
        self.__check_5G_enable()
        print("通话中")


phone = Phone()
phone.call_by_5G()
