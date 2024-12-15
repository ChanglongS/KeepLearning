# 作者: 王道 龙哥
# 2022年03月22日10时01分23秒
class Foo:
    def func(self):
        print('I am func')

    # 定义property属性
    @property
    def prop(self):
        print('I am prop')

# ############### 调用 ###############
foo_obj = Foo()
foo_obj.func()  # 调用实例方法
foo_obj.prop  # 调用property属性