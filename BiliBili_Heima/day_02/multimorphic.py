# 多态：多种状态，即完成某个行为时，使用不同的对象会得到不同的状态
class Animals:
    # 含有抽象方法的类叫做抽象类
    # 抽象方法：含有pass实现的抽象方法
    def speak(self):
        pass


class Dog(Animals):
    def speak(self):
        print("wangwangwang")


class Cat(Animals):
    def speak(self):
        print("miaomiaomiao")


def main_func(animals: Animals):
    animals.speak()


dog = Dog()
cat = Cat()

main_func(dog)
main_func(cat)
