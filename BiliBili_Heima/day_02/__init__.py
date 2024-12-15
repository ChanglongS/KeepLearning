# # 构造方法
# # __init__
# class Student:
#     name = None
#     age = None
#     tl = None
#
#     def __init__(self, name, age, tl):
#         self.name = name
#         self.age = age
#         self.tl = tl
#         print("create class")
#
#
# stu = Student("周杰伦", 30, "13600006666")
# print(stu.name)
# print(stu.age)
# print(stu.tl)
class Student:
    name = None
    age = None
    address = None

    def __init__(self):
        self.name = input("Enter your name: ")
        self.age = input("Enter your age: ")
        self.address = input("Enter your address: ")

for i in range(1, 11):
    print(f"当前录入第{i}位学生信息")
    student = Student()
    print(f"{i}位学生的信息{student.age},{student.address},{student.name}")