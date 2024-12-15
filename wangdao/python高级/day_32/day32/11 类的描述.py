# 作者: 王道 龙哥
# 2022年03月22日11时17分15秒
class Foo:
    """ 描述类信息，这是用于看片的神奇 """
    def func(self)->int:
        """
        I am func
        :return:
        """
        pass

print(Foo.__doc__)
print(Foo.func.__doc__)
#输出：类的描述信息