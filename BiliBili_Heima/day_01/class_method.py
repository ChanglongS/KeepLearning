# 类是图纸，需要基于图纸生产实体（对象），才能正常工作，这种套路，称为：面向对象编程
class Student:
    # 属性--成员变量
    name = None
    age = None

    # 行为--成员方法，self必须存在
    def hi_name(self):
        # 传参可以省略self，但是类内调用属性必须带上self
        print(f"{self.name}, {self.age}")

    def hi_name_2(self, msg):
        print(f"大家好，我是{self.name}，{msg}")


stu_1 = Student()
stu_1.name = "周杰伦"
stu_1.age = 18
stu_1.hi_name()
stu_1.hi_name_2("很高兴认识你")
