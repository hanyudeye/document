#!/usr/bin/env python3

import os
import time
# import time
# from math import sqrt
# import operator
# for var in range(1,30):
#    print(var) 
#    time.sleep(1)
# import subprocess
# subprocess.call([ "ls","-l","."]) 

# print("!你是笨蛋 ")

# home=["xiezi","yanijng","aa"]
# yourhome=["xiezi","yanijng","bb"]
# r=home==yourhome

# if not r :
#     print("不相等")


# print('he')
# print(hex(41))
# print(r)
# def exit():
#     print("程序结束")

# exit()

t=("xiao","xhang")
# print(t)

s={"name":"xiaoli","age":32}
# del s['age']
l=['2','3','1','nihao','a']
r=list.sort(l)

# print(s.__len__())

yizi=4
# print(yizi)

name="wuming"
# print(name)

SRC_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

SRC_PATH = os.path.dirname(os.path.realpath(__file__))


def task1(dummy=None):
    if True:
        sentence = "Helel world"
    return True

R=task1()

computer={
    "hostname":"aming",
    "buydate":"2014-3-4",
    "nettype":"wifi",
    "buymoney":5000
}


# print(computer["buymoney"])
# time.sleep(3)
# print(computer["buymoney"]+1)
# time.sleep(3)
# print(computer["buymoney"]+2)

l=[1,3,4,3]
list.sort(l)
# print(l)
t=(  1,3,4 ) 
# l= tuple.count(t)
l=type(t)

# print(l.count())
t=tuple("hello")
# print(t)

# 将华氏温度转换为摄氏温度

# f=float(input("请输入华氏温度"))
# c=(f-32)/1.8
# print('%.1f s华氏温度 = %.1f 摄氏度 ' % (f,c))

class Student():
    def __init__(self,id,name):
        self.id=id
        self.name=name

    def __repr__(self):
        return 'id =' + self.id + ', name =' + self.name

xiaoming=Student(id='1',name='xiaoming')
# print(ascii(xiaoming))


tigerMonther="伊莎贝拉"
tigerChildren=["拉里","鸿都","李笛"]

