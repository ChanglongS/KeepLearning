# 作者: 王道 龙哥
# 2022年03月22日11时25分42秒
class Foo:
    def __init__(self,*args):
        print(args)

    def __call__(self, *args, **kwargs):
        print(args)
        print('__call__')


obj = Foo('init参数')  # 执行 __init__
obj('haha')

print(Foo.__dict__)