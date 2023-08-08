import world

print(world.num)


def all_the_args(a,*args, **kwargs):
    print(a)
    print(args)
    print(kwargs)


all_the_args( 2,3,c=3, b=4)
import requests

# import math
#
# print(math.log(2,3))
#
# b = int('33')
# print(type(b),b)
#
# if b > 2:
#     print('hel')
# else:
#     print('oo')
#
# if b > 2 and b <30:
#     print('22')
#
# tuple1 = ('aa','ccc')
# print(tuple1)
#
# m1 = {'a':1,'b':1,'b2':2,'b3':3,'b4':4}
#
# for m in m1:
#     if 3 > m1[m] >= 2:
#         print(m)
#
# print(len(m1))
#
# ls = ['aaa']
# ls.append('bbb')
# ls.append('ccc')
# ls.remove('bbb')
# print(ls)
#
# print("""
# 你好啊
# 我是
# """)
#
#
# def calc():
#     return 1
#
#
# class Animal:
#     def __init__(self):
#         self.name = 'a'
#

with open('./hello1.py', 'r+') as f:
    print(f.readline())
    f.write(''"""print(2)\n"""'')
