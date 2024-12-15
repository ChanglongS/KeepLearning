#!/usr/bin/env python3
# -*-coding:UTF-8 -*-
# FileName  :quiz_14.py
# Time      : 11:51
# Author    :SunChanglong
# 14. 读取两个数a和b，输出a和b中较大的
# 15. 读取输入，判断是否是质数，是输出 质数两字，不是输出 非质数
# 16. 通过计算，输出[0,100]（左闭右闭区间）内的素数
def cmpLar():
    num1 = 10
    num2 = 20
    if num1 > num2:
        print(num1)
    else:
        print(num2)
    print("-" * 50)
    #     17. Python 阶乘实例，读取一个数字，输出对应数字的阶乘结果
    num = int(input("Enter a number: "))
    numC = 1
    for i in range(1, num + 1):
        numC *= i
    print(numC)
    print("-" * 50)
    #     19. 读取一个数，输出从1到该数字之间斐波那契数列
    list19 = [0, 1, 2]
    num = int(input("Enter a number: "))
    if num < 3:
        print(list19[num])
    for i in range(3, num + 1):
        list19.append(list19[i - 1] + list19[i - 2])
    print(list19[1::])
    print("-" * 50)
    # 20. 读取一个数，判断是否是阿姆斯特朗数，是输出 是，不是输出 不是
    num = int(input("Enter a number: "))
    numCopy = num
    sum = 0
    while numCopy > 0:
        sum += 1
        numCopy //= 10
    numcopy2 = num
    sum2 = 0
    while numcopy2 > 0:
        sum2 += (numcopy2 % 10) ** sum
        numcopy2 //= 10
    if sum2 == num:
        print("阿姆斯特朗数")
    else:
        print("No")
    print("-" * 50)
    #     21. 读取一个数，分别输出其二进制、八进制、十六进制
    num = int(input("Enter a number: "))
    print(bin(num))
    print(oct(num))
    print(hex(num))
    print("-" * 50)
    # 22. 读取一个字符，输出ASCII 码值，读取一个ASCII码（数字范围属于ASCII范围内的），输出
    # 对应字符
    cite = input("char : ")
    print(ord(cite))
    print(chr(65))
    print("-" * 50)


def isZhiShu(num):
    if num == 0 or num == 1 or num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


def isRange():
    for i in range(101):
        if isZhiShu(i):
            print(i)
        else:
            continue


if __name__ == "__main__":
    run_code = 0
    isRange()
    print("-" * 50)
    if isZhiShu(29):
        print("质数")
    else:
        print("非质数")
    print("-" * 50)
    cmpLar()
