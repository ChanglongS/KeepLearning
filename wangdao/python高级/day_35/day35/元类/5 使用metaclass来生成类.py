# 作者: 王道 龙哥
# 2022年03月25日11时38分08秒
def upper_attr(class_name, class_parents, class_attr):
    print(class_name, class_parents, class_attr)
    # 遍历属性字典，把不是__开头的属性名字变为大写
    new_attr = {}
    for name, value in class_attr.items():
        if not name.startswith("__"):
            new_attr[name.upper()] = value

    # 调用type来创建一个类,这里的返回值给了Foo
    return type(class_name, class_parents, new_attr)


class Foo(object, metaclass=upper_attr):
    bar = 'bip'


print(Foo.BAR)
