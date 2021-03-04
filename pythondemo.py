print ('hello')
import pyautogui
import time

import timeit
import getpass
# -*- coding: UTF-8 -*-
import math
def pytest():
    lst = []

    for i in range(100):
        lst.append(i)

    print(lst)

# 遍历1-4.输出三位数组合（三位数没有重复数字）
def demo1():
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                if (i != j) and (i != k) and (j != k):
                    print(i, j, k)

# 利润计算
def demowhile():
    while True:
        # I = input("please input the lirun：")
        # age = int (I)
        I = int(input("please input the lirun："))
        print(I)

        if I <= 10:
            a = I * 0.01
            print('领取的金额为：%a' % a)
            # print (a)
        elif I <= 20 and I > 10:
            J = I - 10
            b = 10 * 0.01 + J * 0.075
            print(b)

#登录脚本
def demologin():
    user = 'xes'
    passwd = 'w123456'
    username = input('请输入姓名：')
    password = input('请输入密码：')

    for i in range(3):
        if username == user and password == passwd:
            print('恭喜你登录成功')
            break
        elif i < 2:
            username = input('请输入姓名：')
            password = input("请输入密码：")
        elif i == 2:
            print("账号已锁定")
            break





# 购物车实例脚本
def demoshop():
    shop_car = []  # 用来存放购买的商品
    goods = {
        1: ['手机', 6000],
        2: ['电脑', 18000],
        3: ['自行车', 800],
        4: ['宝马', 400000]
    }  # 商品列表

    while True:
        salary = input("你有多少钱：")
        salary = int(salary)
        print("是否要买东西：")
        flag1 = input('Y   N:')
        if flag1.upper() == 'N':
            exit("欢迎下次光临")
        elif flag1.upper() == 'Y':
            break
        elif flag1.upper() == 'Q':
            exit('欢迎下次光临')

    while True:
        print("淘宝".center(30, '-'))  #输出以 -------淘宝---------

        for i in goods:
            print(i, goods[i])

        print("淘宝".center(30, '-'))
        choice_good = int(input("请输入商品编码："))

        if choice_good >= 1 and choice_good <= 4:
            if salary >= goods[choice_good][1]: #判断你的钱是否大于等于商品的价格
                shop_car.append(goods[choice_good][0]) #给字典中添加元素.将你选择的商品的价格添加到数组中。
                salary = salary - goods[choice_good][1]
                print('您购买的商品为：', goods[choice_good][0])
                print("您购买的商品价格为：", goods[choice_good][1])
                print("您当前的余额为：", salary)
                print("是否继续：")
                contin = input('Y N:')
                if contin.upper() == 'Q':
                    break
                elif contin.upper() == 'N':
                    # exit('欢迎下次光临')
                    break
            else:
                print("余额不足")
                print("是否继续：")
                contin = input('Y N:')
                if contin.upper() == 'N':
                    # exit('欢迎下次光临')
                    break
        else:
            print("没有该商品编号")
            continue
    print("本次购物".center(30, '-'))
    print("你买了：", end=' ')
    for i in shop_car:
        print(i, end=' ')
    print("余额为：", salary)
    print("欢迎下次光临")




def demofile():
    user = 'xes'
    passwd = 'w123456'

    userfile = 'fuser' #定义存放用户的文件
    passwdfile = 'fpwd' #定义存放密码的文件

    creatfile1 = open(userfile, 'a+')  # 创建文件
    creatfile2 = open(passwdfile, 'a+')

    username = input('请输入姓名：')
    password = input("请输入密码：")
    # password = getpass.getpass("请输入密码：")

    if username == user and passwd == password:
        print("恭喜您登录成功")
    else:
        # print(username)
        creatfile1.write(username + '\n')  #把用户名写进文件
        creatfile1.close()
        # print(password)
        creatfile2.write(password + '\n')
        creatfile2.close()

    f = open(userfile, 'r')
    if f.mode == 'r':
        contents = f.read()
        print(contents)


def democount():
    for i in range(1, 10):
        for j in range(1, 10):
            x = i * j
            print("%d * %d = %d" % (i, j, x))


def demomath():
    print(math.sin(10))
    name="hahaha"
    print(name.capitalize())

if __name__ == '__main__':
    print('利润核算')
    # democount()
    # demofile()
    # demoshop()
    # demologin()
    # demo1()
    # pytest()
    demomath()
