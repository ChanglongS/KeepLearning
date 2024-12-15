import random

from PyQt5.sip import voidptr

var_1: int = 100
var_2: float = 100.34


class Student:
    data = None

    def func(self, data: int) -> None:
        print(f"1: {data}")


stu: Student = Student()
stu2 = Student()  # type: Student
stu2.func(1)  # type: None

my_list: list[int] = [1, 2, 3]

num = random.randint(1, 10)  # type: int
my_dict = {"st": 2}  # type: dict[str, int]
