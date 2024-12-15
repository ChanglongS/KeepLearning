#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :quiz.py
# Time      : 09:04
# Author    :SunChanglong


def vector():
    my_list = [1, 2, 3]
    my_tuple = (1, 2, 3)
    my_str = ""
    my_dic = {}
    my_set = set()

    # 3、求两个有序数字列表的公共元素
    my_list2 = [2, 3, 4]
    i = j = 0
    count_list = []
    while i < len(my_list) and j < len(my_list2):
        if my_list[i] == my_list2[j]:
            count_list.append(my_list[i])
            i += 1
            j += 1
        elif my_list[i] < my_list2[j]:
            i += 1
        elif my_list[i] > my_list2[j]:
            j += 1
    print(count_list)
    print("-" * 50)
    #     4、给定一个n个整型元素的列表a，
    #     其中有一个元素出现次数超过n / 2，求这个元素
    my_list3 = [1, 1, 1, 1, 1, 1, 2, 3, 3, 3]
    len3 = len(my_list3)
    for i in my_list3:
        if my_list3.count(i) > len3 / 2:
            print(i)
            break
    print("-" * 50)
    #     6、将元组 (1,2,3) 和集合 {4,5,6} 合并成一个列表。
    my_list4 = list(my_tuple)
    print(my_list4)
    my_list5 = list({4, 5, 6})
    my_list4.extend(my_list5)
    print(my_list4)
    print("-" * 50)

    #   7、在列表 [1,2,3,4,5,6] 首尾分别添加整型元素 7 和 0。
    my_list6 = [1, 2, 3, 4, 5, 6]
    my_list6.append(0)
    my_list6.insert(0, 7)
    print(my_list6)
    print("-" * 50)

    # 8、反转列表 [0,1,2,3,4,5,6,7] 。
    # 9、反转列表 [0,1,2,3,4,5,6,7] 后给出中元素 5 的索引号。
    my_list7 = [0, 1, 2, 3, 4, 5, 6, 7]
    my_list7.reverse()
    print(my_list7)
    print(my_list7.index(5))
    print("-" * 50)

    #     10、分别统计列表
    #     [True,False,0,1,2] 中 True,False,0,1,2的元素个数，发现了什么？
    my_list8 = [True, False, 0, 1, 2]
    print("count: ", my_list8.count(True))
    print("count: ", my_list8.count(False))
    print("count: ", my_list8.count(0))
    print("count: ", my_list8.count(1))
    print("count: ", my_list8.count(2))
    # True == 1, False == 0
    print("-" * 50)

    # 11.从列表 [True,1,0,‘x’,None,‘x’,False,2,True] 中删除元素‘x’
    # 12、从列表[True, 1, 0,‘x’, None,‘x’, False, 2, True] 中删除索引号为4的元素。
    # 13、删除列表中索引号为奇数（或偶数）的元素。
    # 14、清空列表中的所有元素。
    my_list9 = [True, 1, 0, "x", None, "x", False, 2, True]
    my_list10 = my_list9
    while my_list9.count("x") != 0:
        my_list9.remove("x")
    print(my_list9)
    my_list10.pop(4)
    print(my_list10)
    # 不要在for循环里使用pop
    # for i in range(len(my_list10)):
    #     if i % 2 == 0:
    #         my_list10.pop(i)
    my_list11 = []
    for i in range(len(my_list10)):
        if i % 2 == 0:
            my_list11.append(my_list10[i])
    print(my_list11)
    my_list10.clear()
    print(my_list10)
    print("-" * 50)

    # 15、对列表 [3,0,8,5,7] 分别做升序和降序排列。
    # 16、将列表 [3,0,8,5,7] 中大于 5 元素置为1，其余元素置为0。
    my_list12 = [3, 0, 8, 5, 7]
    my_list12.sort()
    print(my_list12)
    my_list12.sort(reverse=True)
    print(my_list12)
    print("-" * 50)
    for i in range(len(my_list12)):
        if my_list12[i] > 5:
            my_list12[i] = 1
        else:
            my_list12[i] = 0
    print(my_list12)
    print("-" * 50)

    # 17、遍历列表[‘x’, ‘y’, ‘z’]，打印每一个元素及其对应的索引号。
    my_list13 = ["x", "y", "z"]
    for i in my_list13:
        print(i, my_list13.index(i))
    print("-" * 50)

    # 18、将列表[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # 拆分为奇数组和偶数组两个列表。
    my_list14 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    my_list15 = []
    my_list16 = []
    for i in range(len(my_list14)):
        if i % 2 == 0:
            my_list15.append(my_list14[i])
        else:
            my_list16.append(my_list14[i])
    print(my_list15)
    print(my_list16)
    print("-" * 50)

    #     19.分别根据每一行的首元素和尾元素大小对二维列表
    #     [[6, 5], [3, 7], [2, 8]] 排序。
    my_list17 = [[6, 5], [3, 7], [2, 8]]
    my_list17_1 = sorted(my_list17, key=lambda x: x[0])
    print(my_list17_1)
    my_list17_2 = sorted(my_list17, key=lambda x: x[1])
    print(my_list17_2)
    print("-" * 50)

    # 20、从列表 [1,4,7,2,5,8] 索引为3的位置开始，
    # 依次插入列表 [‘x’,‘y’,‘z’] 的所有元素。
    my_list18 = [1, 4, 7, 2, 5, 8]
    my_list18_1 = ["x", "y", "z"]
    for i in range(len(my_list18_1)):
        my_list18.insert(3 + i, my_list18_1[i])
    print(my_list18)
    print("-" * 50)

    # 21、快速生成由 [5,50) 区间内的整数组成的列表。
    my_list19 = [x for x in range(5, 51)]
    print(my_list19)
    print("-" * 50)

    #     23.将列表 [‘x’,‘y’,‘z’] 和 [1,2,3]
    #     转成 [(‘x’,1),(‘y’,2),(‘z’,3)] 的形式
    list23 = ["x", "y", "z"]
    list23_2 = [1, 2, 3]
    list23_3 = []
    for i in range(3):
        list23_3.append((list23[i], list23_2[i]))
    print(list23_3)
    print("-" * 50)

    #     24、以列表形式返回字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中所有的键。
    dict24 = {"Alice": 20, "Beth": 18, "Cecil": 21}
    print(list(dict24.keys()))
    print(type(dict24.keys()))
    print("-" * 50)

    #     25、以列表形式返回字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中所有的值。
    dict25 = dict24.copy()
    print(list(dict25.values()))
    print("-" * 50)

    #     26、以列表形式返回字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中所有键值对组成的元组。
    dict26 = dict25.copy()
    print(tuple(dict26.items()))
    print("-" * 50)

    #     27、向字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21}
    #     中追加 ‘David’:19 键值对，更新Cecil的值为17。
    dict27 = dict26.copy()
    dict27["David"] = 19
    dict27["Cecil"] = 17
    print(dict27)
    print("-" * 50)

    #     28、删除字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中的Beth键后，清空该字典。
    dict28 = dict26.copy()
    print(dict26)
    dict28.pop("Beth")
    print(dict28)
    dict28.clear()
    print(dict28)
    print("-" * 50)

    # 29、判断 David 和 Alice 是否在字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中。
    dict29 = dict24.copy()
    print(dict29)
    if dict29.get("David") and dict29.get("Alice"):
        print("Yes")
    else:
        print("No")
    print("-" * 50)

    # 30、遍历字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21}，打印键值对。
    dict30 = dict24.copy()
    print(dict30)
    for key in dict30.keys():
        print(key, dict30[key])
    print("-" * 50)

    # 32、以列表[‘A’, ‘B’, ‘C’, ‘D’, ‘E’, ‘F’, ‘G’, ‘H’]
    # 中的每一个元素为键，默认值都是0，创建一部字典。
    dict32 = {}
    list32 = ["A", "B", "C", "D", "E", "F", "G", "H"]
    for i in list32:
        # dict32[i] = 0
        # dict32.update({i: 0})
        dict32.setdefault(i, 0)
    print(dict32)
    print("-" * 50)

    # 33、将二维结构 [[‘a’,1],[‘b’,2]] 和 ((‘x’,3),(‘y’,4)) 转成字典。
    list33 = [["a", 1], ["b", 2]]
    tuple33 = (('x', 3), ('y', 4))
    dict33 = {}
    for i in list33:
        dict33.setdefault(i[0], i[1])
    for i in tuple33:
        dict33.setdefault(i[0], i[1])
    print(dict33)
    print("-" * 50)

    #     34、将元组 (1,2) 和 (3,4) 合并成一个元组。
    tuple34 = (1, 2)
    tuple35 = (3, 4)
    tuple36 = tuple34 + tuple35
    print(tuple36)
    print("-" * 50)

    #     35、将空间坐标元组 (1,2,3) 的三个元素解包对应到变量 x,y,z。
    tuple35 = (1, 2, 3)
    x, y, z = tuple35
    print(x, y, z)
    print("-" * 50)

    #     36、返回元组 (‘Alice’,‘Beth’,‘Cecil’) 中 ‘Cecil’ 元素的索引号。
    tuple36 = ("Alice", "Beth", "Cecil")
    print(tuple36.index("Cecil"))
    print("-" * 50)

    #     37、返回元组 (2,5,3,2,4) 中元素 2 的个数。
    # 38、判断 ‘Cecil’ 是否在元组 (‘Alice’,‘Beth’,‘Cecil’) 中。
    tuple37 = (2, 5, 3, 2, 4)
    print(tuple37.count(2))
    tuple38 = ("Alice", "Beth", "Cecil")
    if tuple38.count("Cecil") != 0:
        print("Yes")
    else:
        print("No")
    print("-" * 50)

    #     39、返回在元组 (2,5,3,7) 索引号为2的位置插入元素 9 之后的新元组。
    tuple39 = (2, 5, 3, 7)
    tuple39_2 = (9,)
    tuple13_3 = tuple39[:2:] + tuple39_2 + tuple39[2::]
    print(tuple13_3)
    print("-" * 50)

    #     40、创建一个空集合，增加 {‘x’,‘y’,‘z’} 三个元素。
    set40 = set()
    set40.add("x")
    set40.add("y")
    set40.add("z")
    set40.update("a", "b", "c")
    print(set40)
    print("-" * 50)

    #     41、删除集合 {‘x’,‘y’,‘z’} 中的 ‘z’ 元素，
    #     增j加元素 ‘w’，然后清空整个集合。
    set41 = {"x", "y", "z"}
    set41.remove("z")
    print(set41)
    set41.add("w")
    print(set41)
    set41.clear()
    print(set41)
    print("-" * 50)

    #     42、返回集合 {‘A’,‘D’,‘B’}
    #     中未出现在集合 {‘D’,‘E’,‘C’} 中的元素（差集）。
    # 43、返回两个集合 {‘A’,‘D’,‘B’} 和 {‘D’,‘E’,‘C’} 的并集。
    # 44、返回两个集合 {‘A’,‘D’,‘B’} 和 {‘D’,‘E’,‘C’} 的交集。
    # 45、返回两个集合 {‘A’,‘D’,‘B’} 和 {‘D’,‘E’,‘C’} 未重复的元素的集合。
    # 46、判断两个集合 {‘A’,‘D’,‘B’} 和 {‘D’,‘E’,‘C’} 是否有重复元素。
    # 47、判断集合 {‘A’,‘C’} 是否是集合 {‘D’,‘C’,‘E’,‘A’} 的子集。
    set42 = {"a", "d", "b"}
    set42_2 = {"d", "e", "f"}
    print(set42.difference(set42_2))
    set42_3 = set42.union(set42_2)
    print(set42_3)
    set42_4 = set42.intersection(set42_2)
    print(set42_4)
    set42_5 = set42.symmetric_difference(set42_2)
    print(set42_5)
    print(set42.isdisjoint(set42_2))
    set47 = {"A", "C"}
    set47_2 = {"D", "C", "E", "A"}
    print(set47.issubset(set47_2))
    print("-" * 50)

    # 48、去除数组 [1,2,5,2,3,4,5,‘x’,4,‘x’] 中的重复元素。
    list48 = [1, 2, 5, 2, 3, 4, 5, "x", 4, "x"]
    set48 = set(list48)
    print(set48)
    print("-" * 50)

    #     49、返回字符串 ‘abCdEfg’ 的全部大写、全部小写和大下写互换形式。
    str1 = "abCdEfg"
    str2 = str1.upper()
    print(str2)
    str3 = str1.lower()
    print(str3)
    str4 = str1.swapcase()
    print(str4)
    print("-" * 50)

    #     50、判断字符串 ‘abCdEfg’ 是否首字母大写，字母是否全部小写，字母是否全部大写。
    str50 = "abCdEfg"
    if str50[0].isupper():
        print("Yes")
    if str50.islower():
        print("Yes")
    if str50.isupper():
        print("Yes")
    else:
        print("No")
    print("-" * 50)

    #     51、返回字符串 ‘this is python’ 首字母大写以及字符串内每个单词首字母大写形式。
    # str51.title()------>每个单词首字母大写
    str51 = "this is python"
    list51 = str51.split(" ")
    print(list51)
    list51_2 = []
    for item in list51:
        list51_2.append(item[:1:].upper() + item[1::] + " ")
    print(list51_2)
    print("".join(list51_2))
    print("-" * 50)

    #     52、判断字符串 ‘this is python’ 是否以 ‘this’ 开头，又是否以 ‘python’ 结尾。
    # 53、返回字符串 ‘this is python’ 中 ‘is’ 的出现次数。
    # 54、返回字符串 ‘this is python’ 中 ‘is’ 首次出现和最后一次出现的位置。
    # 55、将字符串 ‘this is python’ 切片成3个单词。
    # 56、返回字符串 ‘blog.csdn.net / xufive / article / details / 102946961’ 按路径分隔符切片的结果。
    str52 = str51
    # str52 = ""
    # print(str51)
    print(str52)
    list52 = str52.split(" ")
    if list52[0] == "this":
        print("Yes")
    if list52[-1] == "python":
        print("Yes")
    print(str52.count("is"))
    print(str52.find("is"))
    print(str52.rfind("is"))

    str56 = "blog.csdn.net/xufive/article/details/102946961"
    list56 = str56.split("/")
    print(list56)
    print("-" * 50)

    #     57、将字符串 ‘2.72, 5, 7, 3.14’ 以半角逗号切片后，再将各个元素转成浮点型或整形。
    str57 = "2.72, 5, 7, 3.14"
    list57 = str57.split(", ")
    print(list57)
    list57_2 = []
    for item in list57:
        if item.count(".") == 0:
            list57_2.append(int(item))
        else:
            list57_2.append(float(item))
    print(list57_2)
    print("-" * 50)

    #  58.判断字符串 ‘adS12K56’ 是否完全为字母数字，是否全为数字，是否全为字母？
    str58 = 'adS12K56'
    print(str58.isalnum())
    print(str58.isalpha())
    print(str58.isdecimal())
    print("-" * 50)

    # 59、将字符串 ‘there is python’ 中的 ‘is’ 替换为 ‘are’。
    str59 = "there is python"
    print(str59.replace("is", "are"))
    print("-" * 50)

    #     60、清除字符串 ‘\t python \n’ 左侧、右侧，以及左右两侧的空白字符。
    str60 = "\t python \n"
    print(str60.strip())
    print("-" * 50)

    #     61、将三个全英文字符串（比如，‘ok’, ‘hello’, ‘thank you’）分行打印，实现左对齐、右对齐和居中对齐效果。
    # 62、将三个字符串（比如，‘Hello, 我是David’, ‘OK, 好’, ‘很高兴认识你’）分行打印，实现左对齐、右对齐和居中效果。
    # 63、将三个字符串 ‘15’, ‘127’, ‘65535’ 左侧补0成同样长度。
    str61 = "ok"
    str61_2 = "hello"
    str61_3 = "thank you"
    print(str61.ljust(10, "-"))
    print(str61_2.rjust(10, "-"))
    print(str61_3.center(10, "-"))
    print("-" * 50)

    #    64、将列表 [‘a’,‘b’,‘c’] 中各个元素用’|'连接成一个字符串。
    list64 = ["a", "b", "c"]
    list64_2 = []
    for item in list64:
        list64_2.append(item + "|")
    print(list64_2)
    print("".join(list64_2)[:-1:])
    print("-" * 50)

    # 65、字符串 ‘abc’ 相邻的两个字母之间加上半角逗号，生成新的字符串。
    str65 = "abc"
    str65_2 = ",".join(str65)
    print(str65_2)
    print("-" * 50)

    #   66、从键盘输入手机号码，输出形如 ‘Mobile: 186 6677 7788’ 的字符串。
    str66 = input()
    print(str66)
    print("-" * 50)


if __name__ == "__main__":
    run_code = 0
    vector()
