# 作者: 王道 龙哥
# 2022年03月22日11时22分16秒
from test import Person

obj = Person()
print(obj.__module__)  # 输出 test 即：输出模块
print(obj.__class__)  # 输出 test.Person 即：输出类

