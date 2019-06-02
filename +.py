#coding=utf-8
# print("hello,world")
# print(range(10))
# a,b,c=1,2,"jhon"
# print(a,b,c)
# 100+200
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('{}x{}={}\t'.format(j, i, i*j))
#     print()
# print("*****")
# print ("hello")
# age=input ("age:")
# print (age)




# a,b,c=1,2,3
# str1 = "hello"
# str2 = "world"
# list = ['runoob', 786, 2.23, 'john', 70.2]
# print (str1 and str2)
# print (list[1])
# print (-9//2,2**2,7894%3)


#if 1 <> 0:

#    print (1)
#else:
#    print (0)

# a,b=-7,2
# print a or b
#
# c=1
# list=[0,1,2,3]
# print (c not in list)
#
# if  0==1:
#     print 1
# else:
#     print 0
#
#
#
# print ("pleas input num")
# num = input()
# while num > 0:
#     print num
#     num = num - 1
# print ("while is out")
#
#
#
# for abc in "1256":
#     print abc
#
# fruits = {'banana',1,'mango'}
# for fruit in fruits:
#     print  fruit
#
# print "Good bye!"
#

# names = ['Michael', 'Bob', 'Tracy']
# words = ['cat', 'window', 'defenestrate']
# for name in names:
#     print(names)
#     for b in words:
#         print(b, len(b))
#
# num1=10
# while  num1>=0 :
#     print(num1)
#     break
# print type (num1),dir(num1)
# print help(dir)
#
#
# s1 = '123'
# s2 = int(s1)
# print (s2)

# import calendar
# cal = calendar.month(2019, 4)
# print cal

# num = "a"
# v = int(num,base=16)
# v.bit_length()
# print (v)

# import string
# test = "Aello\t {0} World {1}"
# # v1 = test.capitalize()
# # v2 = test.lower()
# print (v1)
# print (v2)
# print(v1.endswith("o"))
# v1.isalnum()
# print 1
# print test.capitalize(),string.digits
# print test.center(20)
# print test.count("el")
# # print test.title()
# print (test.format("jean","jack"))
# v = test.islower()
# v1=test.isnumeric()
# print v

# for z in test:
#     v = type(z)
#     print z,v

# v = range(100000)
# for item in v:
#     print v

#
# tu=("alex",[11,22,{"k1":'v1',"k2":["age","name"],"k3":(11,22,33)},44])
# dic={'k1':"v1","k2":"v2","k3":[11,22,33]}
# for i in dic.keys():
#     print(i)


# i = 0
# while i<=10 :
#     i+=1
#     if i==7:
#         continue
#     else:
#         print i



# i = range(100+1)
# print sum(i)
#
# i = 0
# sum =0
# while i<100:
#     i+=1
#     sum=sum+i
# print sum

# -*- coding:utf-8-*
# i = 0
# sum1=0
# sum2=0
# while i<100:
#     i+=1
#     if i%2==1:
#         sum1=sum1+i
#     else:
#         sum2=sum2+i
# print sum1-sum2-100

# -*- coding:utf-8 -*-
# i = 0
# while i<3:
#     i += 1
#     username = input("please input username:")
#     password = input("please input password:")
#     if username=="oldboy"and password =="123":
#         break
#     else:
#         continue

# l = [455,6894,55,74,5,478,45,745,4,544,5,862,54,54475454]
# for l in l:
#     v = int(l)
#     print l%2

# v = "heldiegjghfitg"
# for zyz in v :
#     print zyz

# li = [1,2,"hello",["word",55],-1]
# # for zyz in li[2]:
# #     print li
# # li[1]=5
# # print li
# # del li[1]
# # print li
# # print li[1]
# # li[1:3]=[454,5]
#
# # s="hello,woeet"
# # li=list(s)
# # print li
# #
# # v=str(li)
# # print v
#
# # li.append(5)
# li.extend("world")
# print li.index("hello")
# li.reverse()
# print li
# li.pop(2)
# print li

# tu = ("hello","world",[1,2,3])
# # v = " ".join(tu)
# # y = list(tu)
# # print v,type(y)
# #
# # for item in tu :
# #     print item
# tu[2][0] = 2
# print tu.count(1)


# info = {"key1":"hello","key2":"world","key3":"haha"}
# # print info["key3"][3]
# # del(info["key1"])
# # print info
# for item in info.values():
#     print item
# info.update(k1=46,k8=895)
# print info

# dict1 = ['orange','pear','orange','banana']
# dict2 = ['aplle','orange','orange','banana']
# dict3 = ['orange','pear','orange','banana']
# dict4 = ['orange','pear','orange']
# # d = []
# # for item in dict1 :
# #     if item in dict2 :
# #         d.append(item)
# # print d
# d1 = set(dict1)
# d2 = set(dict2)
# d3 = set(dict3)
# d4 = set(dict4)
#
# v ="orange" not in d1
# print d1&d2,d1==d2,d1.union(d2)
# print v,d1 and d4,d1.intersection(d4),d1.difference(d4),d1.issubset(d4),d1^d2

# print dict1
# print dict2
# print dict1-dict2,dict1.difference(dict2),dict1|dict2,dict1&dict2,dict1^dict2

# s = set('hello')
# s.add(5)
# print s
# z=s.pop()
# y=s.copy()
# y.clear()
# y.add(5698)
# s.discard("o")
# print s,y,z

# print "i am %s.2f my body is alex %s" %(18.236,"world")
# print "i am +30.2f my%(name)s  body is alex " %({"name":18})

# def y(x,type="mysql"):
#     """
#
#     :param x:
#     :return:
#     """
#     print x
#     print type
#
# y(5,895)


# name = "hello"
# def changename1():
#     name = "world1"
#     def changename2():
#         name = "world2"
#         def changename3():
#             name = "world3"
#             print name
# changename1()
# print name


# name  = "gangniang"
# def weihou():
#     name = "chenzhuo"
#     def weiweihou():
#         name = "lengjing"
#     weiweihou()
#     print name
# print name
# weihou()
# print name


#
# def foo():
#     print "hello"
#     bar ()
#
# def bar():
#     print "world"
#
# foo()


# import  time
# def calc(n):
#     print n
#     time.sleep(1)
#     calc (n)
# calc(10)


# def calc(n):
#     print(n)
#     if int(n / 2) == 0:
#         return n
#     return calc(int(n / 2))
# calc(10)



# __author__ = 'Linhaifeng'
# import time
#
# person_list=['alex','wupeiqi','yuanhao','linhaifeng']
# def ask_way(person_list):
#     print('-'*60)
#     if len(person_list) == 0:
#         return '没人知道'
#     person=person_list.pop(0)
#     if person == 'linhaifeng':
#         return '%s说:我知道,老男孩就在沙河汇德商厦,下地铁就是' %person
#     print('hi 美男[%s],敢问路在何方' %person)
#     print('%s回答道:我不知道,但念你慧眼识猪,你等着,我帮你问问%s...' %(person,person_list))
#     time.sleep(0)
#     res=ask_way(person_list)
#     # print('%s问的结果是: %res' %(person,res))
#     return res
#
# res=ask_way(person_list)
#
# print(res)
#
import time
# def f(n):
#     if n==1:
#         return 1
#     return n*f(n-1)
#
# print f(5)

# def sumtree(L):
#     tot = 0
#     for x in L:
#         if not isinstance(x, list):
#             tot += x
#         else:
#             tot += sumtree(x)
#     return tot
# print sumtree([1,5,8,65])


# def fib(n):
#
#     if n <2:
#
#          return n
#
#     else:
#
#          return fib(n-1)+ fib(n -2)
#
# print fib(3)


# list1 = ["life","is","short"]
# list2 = ["you","need","python"]
# list3 = [1,2,3,4,5,6,7,8,9]
#
# list1_set = set(list1)
# list12_set = set(list2)
# list3_set = set(list3)

# list1_set.update(list12_set)
# print list1_set


# print list2[2],list2.index("python")
# # list1.append(",")
# list2.append("!")
# print list1,list2, len(list1)
#
# list1.extend(list2)
# print list1,len(list1),list1.sort()

# list2[list2.index("python")]="python3"
# print list2
# list1.remove(list1[list1.index(",")])
# print list1
#
# list2.remove(list2[list2.index("!")])
# print list2


# list_set1 = set(list1+list2)
# # print list_set1
# # list_set1.remove("python")
# # print list_set1


# def itemnum(x):
#     """
#     计算传入字符串中的数字、字母、空格和其他的个数
#     :param x:
#     :return:
#     """
#     digit_num = 0
#     space_num = 0
#     alpha_num = 0
#     else_num = 0
#     for item in x :
#         if item.isdigit():
#             digit_num+=1
#         elif item.isspace():
#             space_num+=1
#         elif item.isalpha():
#             alpha_num+=1
#         else:else_num+=1
#     return digit_num,space_num,alpha_num,else_num
# v = itemnum("hel543558lo   _/*-656+")
# print v

# v = "45455545"
# x = [1,2,3,4,9,6,]
# z = (1,6,8,7)
# # print len(v),len(x),len(z)
#
# def ismore5 (x):
#     """
#     判断用户传入字符串、列表、元组长度是否大于5
#     :return:
#     """
#     if len(x)>5 :
#         return 1
#     else:
#         return 0
#
# print ismore5(x)

#
# def fn (n):
#     v = fn
#     print v
#     if n==1:
#         return 1
#     return fn(n-1)+n
# v = fn(5)
# print v

# name = lambda x:x+1
# print name(10)

# def foo(n):
# #     print n
# # def bar(name):
# #     print "my name is %s" %name
# #     return 1
# # foo(bar)
# # foo(bar("lili"))


# def test1():
#     print "test1"
#     return test1
# test1()
# v=test1()
# print v

# def test()
#     print "form test"
#     test()
# test()

# num = [1,2,50,8,7]
#
# def fn(x):
#     """
#     表达式操作
#     :param x:
#     :return:
#     """
#     return x**10
# def map_list(func,arrary):
#     """
#     遍历表操作
#     :return:
#     """
#     li = []
#     for i in arrary:
#         v = func(i)
#         li.append(v)
#     return li
#
# print  map_list(fn,num)
# print  map(lambda x:x**10,num)
#
# str1 = "jieigngghdhg"
# print  map(lambda x:x.upper(),str1)
# print map

# word = ["hellolife","worldlife","python","life"]
#
#
# def fliter_test():
#     ret = []
#     for w in word:
#         if not w.endswith("life"):
#             ret.append(w)
#     return ret
# print fliter_test()
# print filter(lambda n:n.endswith("life"),word)
#
# print filter(lambda n:n%2,[1,2,3,4,5,6,7,8,9])
#
# print reduce(lambda x,y:x-y,range(100))

# print abs(-50),all([1,2,369,0]),any([0,0,0,1]),bin(79),format(-79,"b"),bytes("11")
# print chr(83),ord("a"),complex(59),hash("a"),hash("b")


# name = '你好'
# print  bytes(name,encoding='utf-8')

# print  divmod(20,3)
#
# print help(dir(all))

# print  isinstance("abc",int)

# fo = open("hello","wb")
# b1 = bytes("pythos is not good")
# print "file name:",fo.name,fo.closed,fo.mode,fo.read(10)
# print v
# print type(b1)
# fo.tell()


# f = open("a.txt","a+")
# f.write("abcdef \nefghell\n")
# # f.flush()
# f.seek(3)
# print f.tell()
# date = f.read()
# print date
# print f.tell()
#



# def add(x,y,f):
#     return f(x),f(y)
# v = add(1,2,str)
# print  type(list(v)),type(v)
#


# li =["adma","LISA","barT"]
# def func1():
#     res = map(lambda x:x.lower().title(),li)
#     return res
# print func1()

# l = range(10)
#
#
# def func(x,y):
#     return x+y
#
# def prod(l):
#     return reduce(func,l)
#
# print prod(l)


#利用map和reduce编写一个str2float函数，把字符串’123.456’转换成浮点数123.456


# from functools import reduce
# #
# # def str2float(s):
# #     def number_int(s):
# #         numbers = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
# #     '9': 9}
# #         return numbers[s]
# #     def flt(x, y):
# #         return x * 10 + y
# #
# #     return reduce(flt, map(number_int, s.replace('.', ''))) / (10 ** (len(s) -
# #     s.index('.') - 1))
# # print  str2float("458.586")

# def f_w():
#     f = open("test1","w")
#     f.write("hello,world ! \nthis is python\ntest\n")
#
#
# def f_r():
#     f = open("test1","r")
#     f.write("this is r+\n")WWW.5V5.COM
#     print f.read()
#
# def f_a():
#     f = open("test1", "a")
#     f.write("this is a+\n")
#
#
#
# f_w()
# f_r()



# test = [ "test1\n", "test2\n", "test3\n" ]
# # f = open("test.txt", "w+")
# # try:
# #  # f.seek(0)
# #  for l in test:
# #   f.write(l)
# # finally:
# #  f.close()

# l = [2,4,5,8,90,3,5,7,3]
# #
# # def func (x):
# #     return x.__iter__()
# # print list(func(li)),type(func)
# # x=xrange(10)
# # print range(10),x
# # print x
#
# def func1():
#     x = range(10)
#     for i in x:
#         print i
#         print x
# def func2():
#     x = xrange(10)
#     for i in x:
#         print i
#         print x
#
# func1()
# func2()

# print  list.__iter__(li)
#
# print  list.__iter__(li).next()
# print  li.__iter__().next()



# def lay_eggs(num):
#     egg_list=[]
#     for egg in range(num):
#         egg_list.append('蛋%s' %egg)
#     return egg_list
#
# yikuangdan=lay_eggs(10)
# print(yikuangdan)


# def lay_eggs(num):
#     for egg in range(num):
#         res='蛋%s' %egg
#         yield res
#         print('下完一个蛋')
#
#
# laomuji=lay_eggs(10)#我们拿到的是一只母鸡
# print(laomuji)
# print(laomuji.__next__())
# print(laomuji.__next__())
# print(laomuji.__next__())
# egg_l=list(laomuji)
# print(egg_l)
# #演示只能往后不能往前
# #演示蛋下完了，母鸡就死了


# name = "jesson"
# name = "tim"
# res =("sb" if name=="jesson" else "tim")
# fat = 1
# res = ("sb","tim") [fat]
# print res


# egg_list=[i for i in range(10)] #列表推导式
# print egg_list

# li = (1,5,9,7,9)
#
#
# res=(i for i in range(10))
# egg_list=res#列表推导式
# print egg_list,type(egg_list)
# print (next(egg_list))
# print (next(egg_list))
# print (next(egg_list))
# print (next(egg_list))
# print (next(egg_list))
# print (next(egg_list))
# print (next(egg_list))
# print (next(egg_list))
# print (next(egg_list))
# print egg_list.next()
#
#
# print sum(x**2 for x in range(10))
# print sum([1,2,5,8])


# def index_words(text):
#     result = []
#     if text:
#         result.append(0)
#     for index, letter in enumerate(text, 1):
#         if letter == ' ':
#              result.append(index)
#     return result
#
# print(index_words('hello alex da sb'))


# def index_words(text):
#     if text:
#         yield 0
#     for index,letter in enumerate(text,1):
#         if letter == " ":
#             yield index
#             print index_words().next()
#
#
# g=index_words("hello world hello python hello life")

# print g.next()
# print g.next()
# print g.next()
# print g.next()
# print g.next()
# print g.next()


# print  type(enumerate)
#
#

#
# s = "abc"
# print  iter(s).next()
# print  (i for i in "abc")

# import time
# def cal(l):
#     res = 0
#     for i in l:
#         time.sleep(0.1)
#         res+=1
#     return res
#
#
# def timer(func):
#     def wa
#
# res = cal(range(20))
# print res

# import time
# def func1():
#     time.sleep(3)
#     print "hello"
#
#
# def func2(func):
#     def func3():
#         startime = time.time()
#         res = func()
#         stoptime = time.time()
#         print "run time is:%s " % (stoptime - startime)
#         return res
#     return func3()
#
# func1 = func2(func1)
# func1()

# import time
#
# def timer (fucn):
#     def wrapper (*args,**kwargs):
#         startime = time.time()
#         res = fucn(*args,**kwargs)
#         stoptime = time.time()
#         print "run tiem is:%s" %(stoptime-startime)
#         return res
#     return wrapper
#
#
# @timer # foo=timer(foo)
# def foo (x):
#     time.sleep(1)
#     print "hello,world"
#     v = x+1
#     print v
#
#
#
# foo(2)
# print foo

# str1 = "#  ....... Section 3.2.1 Issue #32 .......  "
# print str1.strip(" .!#!. ")


# a,b,c=1,2,3
# print a,b,c
# a,b,c=c,b,a
# print a,b,c



#
# import logging
#
# logger = logging.getLogger()
# # 创建一个handler，用于写入日志文件
#
# print logger
# fh = logging.FileHandler('test.log')
#
# # 再创建一个handler，用于输出到控制台
# ch = logging.StreamHandler()
#
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#
# fh.setFormatter(formatter)
# ch.setFormatter(formatter)
#
# # logger.addHandler(fh) #logger对象可以添加多个fh和ch对象
# # logger.addHandler(ch)
#
#
# logger1 = logging.getLogger('mylogger')
# logger1.setLevel(logging.DEBUG)
#
# logger2 = logging.getLogger('mylogger')
# logger2.setLevel(logging.INFO)
#
# logger1.addHandler(fh)
# logger1.addHandler(ch)
#
# logger2.addHandler(fh)
# logger2.addHandler(ch)
#
# logger.debug('logger debug message')
# logger.info('logger info message')
# logger.warning('logger warning message')
# logger.error('logger error message')
# logger.critical('logger critical message')
#
# logger1.debug('logger1 debug message')
# logger1.info('logger1 info message')
# logger1.warning('logger1 warning message')
# logger1.error('logger1 error message')
# logger1.critical('logger1 critical message')
#
# logger2.debug('logger2 debug message')
# logger2.info('logger2 info message')
# logger2.warning('logger2 warning message')
# logger2.error('logger2 error message')
# logger2.critical('logger2 critical message')

#
# # coding:utf-8
# import logging
#
# # 创建一个logger
# logger = logging.getLogger()
#
# logger1 = logging.getLogger('mylogger')
# logger1.setLevel(logging.DEBUG)
#
# logger2 = logging.getLogger('mylogger')
# logger2.setLevel(logging.INFO)
#
# logger3 = logging.getLogger('mylogger.child1')
# logger3.setLevel(logging.WARNING)
#
# logger4 = logging.getLogger('mylogger.child1.child2')
# logger4.setLevel(logging.DEBUG)
#
# logger5 = logging.getLogger('mylogger.child1.child2.child3')
# logger5.setLevel(logging.DEBUG)
#
# # 创建一个handler，用于写入日志文件
# fh = logging.FileHandler('test3.log')
#
# # 再创建一个handler，用于输出到控制台
# ch = logging.StreamHandler()
#
# # 定义handler的输出格式formatter
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# fh.setFormatter(formatter)
# ch.setFormatter(formatter)
#
# # 定义一个filter
# # filter = logging.Filter('mylogger.child1.child2')
# # fh.addFilter(filter)
#
# # 给logger添加handler
# # logger.addFilter(filter)
# logger.addHandler(fh)
# logger.addHandler(ch)
#
# # logger1.addFilter(filter)
# logger1.addHandler(fh)
# logger1.addHandler(ch)
#
# logger2.addHandler(fh)
# logger2.addHandler(ch)
#
# # logger3.addFilter(filter)
# logger3.addHandler(fh)
# logger3.addHandler(ch)
#
# # logger4.addFilter(filter)
# logger4.addHandler(fh)
# logger4.addHandler(ch)
#
# logger5.addHandler(fh)
# logger5.addHandler(ch)
#
# # 记录一条日志
# logger.debug('logger debug message')
# logger.info('logger info message')
# logger.warning('logger warning message')
# logger.error('logger error message')
# logger.critical('logger critical message')
#
# logger1.debug('logger1 debug message')
# logger1.info('logger1 info message')
# logger1.warning('logger1 warning message')
# logger1.error('logger1 error message')
# logger1.critical('logger1 critical message')
#
# logger2.debug('logger2 debug message')
# logger2.info('logger2 info message')
# logger2.warning('logger2 warning message')
# logger2.error('logger2 error message')
# logger2.critical('logger2 critical message')
#
# logger3.debug('logger3 debug message')
# logger3.info('logger3 info message')
# logger3.warning('logger3 warning message')
# logger3.error('logger3 error message')
# logger3.critical('logger3 critical message')
#
# logger4.debug('logger4 debug message')
# logger4.info('logger4 info message')
# logger4.warning('logger4 warning message')
# logger4.error('logger4 error message')
# logger4.critical('logger4 critical message')
#
# logger5.debug('logger5 debug message')
# logger5.info('logger5 info message')
# logger5.warning('logger5 warning message')
# logger5.error('logger5 error message')
# logger5.critical('logger5 critical message')
#
# import os
# import time
# import logging
# from config import settings
#
#7
# def get_logger(card_num, struct_time):
#
#     if struct_time.tm_mday < 23:
#         file_name = "%s_%s_%d" %(struct_time.tm_year, struct_time.tm_mon, 22)
#     else:
#         file_name = "%s_%s_%d" %(struct_time.tm_year, struct_time.tm_mon+1, 22)
#
#     file_handler = logging.FileHandler(
#         os.path.join(settings.USER_DIR_FOLDER, card_num, 'record', file_name),
#         encoding='utf-8'
#     )
#     fmt = logging.Formatter(fmt="%(asctime)s :  %(message)s")
#     file_handler.setFormatter(fmt)
#
#     logger1 = logging.Logger('user_logger', level=logging.INFO)
#     logger1.addHandler(file_handler)
#     return logger1



# !/usr/bin/python
# -*- coding: UTF-8 -*-

#
# class Fuzhou:
#     # print "hello"
#     date = "30,0000"
#
#     def _init_ (self,name,age,sex):
#         print ("star")
#         self.name=name
#         self.age=age
#         self.sex=sex
#         print ("over")
#
#     def test(test):
#         print ("test")
#
#     def test1(test):
#         print("test1")
#
# # print (Fuzhou.date)
# # print (Fuzhou.test)
# # print (Fuzhou)
# # print (dir(Fuzhou))
# # Fuzhou.__dict__["test"](1)
# #
# #
# #
# # Fuzhou.test1("45")
#
# p1 = Fuzhou(1,2,3)





# !/usr/bin/python
# -*- coding: UTF-8 -*-

# class Employee:
#     '所有员工的基类'
#     empCount = 0
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.empCount += 1
#
#     def displayCount(self):
#         print ("Total Employee %d" % Employee.empCount)
#
#     def displayEmployee(self):
#         print ("Name : ", self.name, ", Salary: ", self.salary)
#
#
# p1 = Employee("alex","hello")
# # print(p1)
# # p1.displayCount()
# # p1.displayEmployee()
#
# def eat_food(self):
#     print(self)
# Employee.eat=eat_food
# p1.eat(p1,"apple")


#
# !/usr/bin/python
# -*- coding: UTF-8 -*-
#
# from math import pi
#
# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
#
#     def area(self):
#         return self.radius**2*pi
#
#     def perimeter(self):
#         return self.radius*2*pi
#
#
#
# class Ring:
#     def __init__(self,radius_outside,radius_inside,Circle):
#
#         self.radius_outside=Circle(radius_outside)
#         self.radius_inside=Circle(radius_inside)
#         self.s1=Circle
#
#     def  rin_area(self):
#
#         return self.radius_outside.area()-self.radius_inside.area()
#
#     def  rin_perimeter(self):
#
#         return self.radius_outside.perimeter()+self.radius_inside.perimeter()
#
#
#
# r1=Ring(9,3,Circle)
# print(Circle.__dict__)
# print(Ring.__dict__)
# print(r1.__dict__)



# ring = Ring(9, 3)
# rinArea = ring.rin_area()   # 计算圆环的面积
# rinPer = ring.rin_perimeter()   # 计算圆环的周长
# print(rinArea, rinPer)  # 打印圆环的面积和周长


#
# class Animal(object):
#     def __init__(self, name, sex, age):
#         self.name = name
#         self.sex = sex
#         self.age = age
#
#     def eat(self):
#         print("%s 在吃东西" % self.name)
#
#     def drink(self):
#         print("%s 在喝东西" % self.name)
#
#     def pull(self):
#         print("%s 在拉粑粑" % self.name)
#
#     def sow(self):
#         print("%s 在嘘嘘" % self.name)
#
#
# class Bird(Animal):
#     def flight(self):
#         print("%s 在自由的飞翔" % self.name)
#
#
# class Horse(Animal):
#     def running(self):
#         print("%s 在飞驰的奔跑" % self.name)
#
#
# bird1 = Bird("麻雀", 1.2, "公")   # 实例化一只鸟
# print (Animal.__dict__)
# print(bird1.__dict__)
# bird1.flight()  # 调用自身独有的方法
# bird1.eat()     # 调用父类公共的方法
# horse1 = Horse("草原马", 3, "公")   # 实例化一匹马
# horse1.running()    # 调用自身独有的方法
# horse1.pull()       # 调用父类公共的方法

# import abc
# class baba(metaclass=abc.ABCMeta):
#     def __init__(self,name):
#         self.name=name
#
#     @abc.abstractmethod
#     def hit_son(self):
#         print ("hit son")
#
#
# class son(baba):
#     def hit_son(self):
#         print ("hit baba")
#
# s1=son(baba)
# s1.hit_son()



# import math
# print (math.tau)


# matplotlib inline

# import numpy as np
# import matplotlib.pyplot as plt
# alpha =1
# theta = np.linspace(0,2*np.pi,num=1000)
# x=alpha * np.sqrt(2)*np.cos(theta)/(np.sin(theta)**2+1)
# y= alpha *np.sqrt(2)*np.cos(theta)* np.sin(theta)/(np.sin(theta)**2+1)
# plt.plot(x,y)
# plt.grid()
# plt.show()

#
# class A(object):
#     def func1(self):
#         print(" In A ")
#
#     def func2(self):
#         self.func1()
#
#
# class B(A):
#     def func1(self):
#         print(" In B ")
#
#
# c1 = B()
# print c1
# c1.func2()
# print c1.func2
# c1.func1()
# print c1.func1
#
#
# class A(object):
#     def __func1(self):
#         print(" In A ")
#
#     def func2(self):
#         self.__func1()
#
#
# class B(A):
#     def __func1(self):
#         print(" In B ")
#
# c2 = B()
# print c2
# c2.func2()

#
# class Bmi(object):
#     def __init__(self, name, weight, height):
#         self.name = name
#         self.weight = weight
#         self.height = height
#
#     @property
#     def calculation_bmi(self):
#         return "%s 的bmi 值%s" % (self.name, self.weight / self.height ** 2)
#
#
# p1 = Bmi("小白", 54, 1.65)
# # print(p1.calculation_bmi())
# print(p1.calculation_bmi)


# import django
# print ("hello")
#
# import time,datetime
# print (datetime.datetime.new())



#获取100以内的质数


# def fn(a):
#     li=len(a)
#     print li
#     if li>5:
#         print 1
#     else:
#         print 0
#
# fn([54,68,7])



# import numpy
# print ("hello,world")




# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if( i != k ) and (i != j) and (j != k):
#                 print i,j,k

# num=90
# li=[0,10,20,40,60,100]
# pi=[0.1,0.075,0.05,0.03,0.015,0.01]
# i=4
#
#
# for i in range(0,4):
#
#     if num-li[i]>0:
#         res=(num-li[i])*pi[i]+li[i-1]*pi[i-1]
#         print(res)
#     else:
#         i-=1
#         if i<0:
#             break
#         else:
#             continue


# li = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 150, 160, 180, 1000]
# arr = [100, 60, 40, 20, 10, 0]
# rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
# r = 0
# n=0
# for n in range(0,len(li)):
#     i = li[n]
#     print(n, li[n])
#     n+=1
#     for idx in range(0, len(arr)):
#         if i > arr[idx]:
#             r += (i - arr[idx]) * rat[idx]
#             print((i - arr[idx]) * rat[idx])
#             i = arr[idx]
#     print(r, "*******")


import math
# res = math.sqrt(3)
# res=isinstance(math.sqrt(3),int)
# print(res)



# import math
# li = []
# for i in range(1,85):
#     if 168 % i == 0:
#         j = 168 / i;
#         if  i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0 :
#             m = (i + j) / 2
#             # n = (i - j) / 2
#             # x = n * n - 100
#             x = m * m-100-168
#             li.append(x)
# print(li)


# year = int(raw_input('year:\n'))
# month = int(raw_input('month:\n'))
# day = int(raw_input('day:\n'))
#
# months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
# if 0 < month <= 12:
#     sum = months[month - 1]
# else:
#     print
#     'data error'
# sum += day
# leap = 0
# if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
#     leap = 1
# if (leap == 1) and (month > 2):
#     sum += 1
# print sum


# x=input()
# y=input()
# z=input()
# li = []
# li.append(x)
# li.append(y)
# li.append(z)
# li.sort()
# print(li)


# def f(n):
#     if n==1:
#         return 1
#     elif n==2:
#         return 1
#     return f(n-1)+f(n-2)
#
#
# print(f(50))

# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     return fib(n - 1) + fib(n - 2)
#
#
# # 输出了第10个斐波那契数列
# print fib(40)




#
# def fib(n):
#     a, b = 1, 1
#     for i in range(n - 1):
#         a, b = b, a + b
#     return a
#
# print fib(57)



# li=[1,2,5,7,8,9,4]
# li1=li[:]
# print(li1)


# for i in range(10):
#     j = 1
#     print
#     while i >= j:
#         print "%d*%d=%d" % (j, i, i * j)
#         j += 1


# for i in range(1, 10):
#     print
#     for j in range(1, i + 1):
#          print "%d*%d=%d" % (i, j, i * j)

# import time
# for i in range(10):
#     print time.asctime()
#     time.sleep(1)


# for n in range(100, 1000):
#     i = n / 100
#     j = n / 100 % 10
#     k = n % 10
#     if n == i ** 3 + j ** 3 + k ** 3:
#         print(n)


# n = 153
# i = n / 100
# j = n / 10 % 10
# k = n % 10
# print i, j, k

# print(dir(int))
# print(int.__dict__)
# print(hasattr(int,"__ror__"))
# print(getattr(int,"__ror__"))


# class c1(object):
#     n1 = "name1"
#     n2 = "mane2"
#
#     def f1(self):
#         print(1)
#
#     def f2(self):
#         print(2)
#
#
# print(c1.__dict__)
# print(hasattr(c1, "n1"))
# n3 = getattr(c1, "n1")
# print(n3)
# print(setattr(c1, "n2", "name3"))
# delattr(c1, "n1")
# print(c1.n1)


# class foo:
#     def func1(self):
#         print("hello")
#     def __del__(self):
#         print("world")
#     pass
#
#


# l=list("hello")
# print(l)

# li="hello"
# print(li)



# class Open :
#     def __init__(self):
#         pass
#     def __enter__(self):
#         print("exe")
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("exit")
#
# with Open() as f:
#     print("-->")
#     print("-->")
#     print("-->")
#     print("-->")


# class cls:
#     name=1
#     def func(self):
#         a=1
#         li=[1,2,3]
#         print("this is class func")
#
#
# class cls1(cls):
#     pass
#
# def func():
#     a = 1
#     print("this is func")
#     name="funcname"







# c=func()
# # print(c.__dict__)
# # delattr(c,"name")
# print(getattr(c,"a"))
# setattr(c,"a",2)
# print(getattr(c,"a"))








# c=cls()
# print(c.__dict__)
# # delattr(c,"name")
# print(getattr(c,"name"))
# setattr(c,"name",2)
# print(getattr(c,"name"))



# def func1():
#     class cls2:
#         a = 1
#         print("this is func")
#         name="funcname"

# print(hasattr(func,"name"))

# print(cls.__dict__)
# print(hasattr(cls,"func"))




# obj=cls()
# obj1=func()
# print(isinstance(obj,cls))
# print(isinstance(obj1,func))

#
# print(issubclass(cls1,cls))



#
# #
# # print(cls)
# # print(cls())
#
# cls.__dict__["name"]=2
# print(cls.name)





# #查看类、类中的函数、函数的名称的含义
# print(cls)#就是个地址
# print("*"*200)
#
# print(cls.name)
# print("*"*200)
#
# print(cls.func)
# print("*"*200)
# print(func)
# print("*"*200)


# #查看类、类中的函数、函数的名称的含义
# print(cls())#就是个地址
# print("*"*200)
#
# print(cls.name)
# print("*"*200)
#
# print(cls.func(5))
# print("*"*200)
# print(func())
# print("*"*200)




# #查看类、类中的函数、函数的type
# print(type(cls))
# print("*"*200)
#
# print(type(cls.name))
# print("*"*200)
#
# print(type(cls.func))
# print("*"*200)
# print(type(func))
# print("*"*200)



# #查看类、类中的函数、函数的所有的属性
# print("*"*200)
#
# print(dir(cls))
# print("*"*200)
#
# print(dir(cls.name))
# print("*"*200)
#
# print(dir(cls.func))
# print("*"*200)
# print(dir(func))
# print("*"*200)


# #查看类、类中的函数、函数的所有的属性字典
# print("*"*200)
#
# print(cls.__dict__)
# print("*"*200)
#
# # print(cls.name.__dict__)
# # print("*"*200)
#
# print(cls.func.__dict__)
# print("*"*200)
# print(func.__dict__)
# print("*"*200)


# #查看类、类中的函数、函数的所有的类型
# print("*"*200)
#
#
#
# print(cls().name)
# print("*"*200)
#
# print(cls.name)
# print("*"*200)
#
# print(cls.func(788))
# print("*"*200)
# print(func())
# print("*"*200)




#
# #描述符挂起
#
#
# class str:
#
#     def __get__(self, instance, owner):
#         print("this is get")
#         print(instance)
#         print(owner)
#
#
#     def __set__(self, instance, value):
#         print("this is set")
#         print(instance)
#         print(value)
#
#     def __del__(self):
#         print("this is del")
#
#
#
# class people:
#
#     name = str()
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def say(self):
#         print("this is %s ,%s" % (self.name, self.age))
#
#
#
#
# p = people("alex", 8)
# p.name=1
# print(p.name)
# print(p.__dict__)


# class cls:
#
#     """
#     this is doc
#     """
#     format_spec={
#
#     }
#     # __slots__ ={"helo":1}
#     def __init__(self, a):
#         self.a = a
#
#     def __iter__(self):
#         pass
#     def __next__(self):
#         self.a += 1
#
#         return self.a

#
# c=cls(0)
# print(c.__next__())
# print(c.__next__())
# print(c.__next__())
# print(c.__next__())
# print("*"*10)
# for i in range(100):
#     print(c.__next__())

    # def __str__(self):
    #     return "this is str "
    #
    #
    # def __format__(self, format_spec):
    #
    #     return



# print(c)





    # def __getattr__(self, item):
    #     print("this is getatter")
    #     return self.__dict__.items
    #     pass
    #
    # def __setattr__(self, key, value):
    #     print("this is setattr")
    #     self.__dict__[key]=value
    #     pass
    # def __delattr__(self, item):
    #     print("this is delattr")
    #     self.__dict__.pop(item)
    #     pass


# c=cls("alex")
# print(c.__dict__)
# c.name="egon"
# print(c.__dict__)
# del c.name
# print(c.__dict__)


    # def __enter__(self):
    #     print("this is enter")
    #     pass
    #
    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     print("this is exit")
    #     pass
    #
    # def __call__(self, *args, **kwargs):
    #     print("this is call method")


# with cls("alex") as c:
#     print('hell')

# print(cls("alex").__doc__)

# print(cls("alex").__dict__)

    # def __getitem__(self, item):
    #     print(self.__dict__[item])
    #
    # def __setitem__(self, key, value):
    #     self.__dict__[key]=value
    #
    # def __delitem__(self, key):
    #     print("this is delling...")
    #     self.__dict__.pop(key)
    #

# f1=cls("ab")
# print(f1.__dict__)
# f1['age']=18
# print(f1.__dict__)
# f1["age1"]=19
# print(f1.__dict__)
# f1.__setitem__("age2",17)
# print(f1.__dict__)
# del f1.name
# print(f1.__dict__)
# del f1["age"]
# print(f1.__dict__)



# class Foo:
#     __slots__=['name','age']
#
# f1=Foo()
# f1.name='alex'
# f1.age=18
# print(f1.__slots__)
#
# f2=Foo()
# f2.name='egon'
# f2.age=19
# print(f2.__slots__)
#
# print(Foo.__dict__)
# #f1与f2都没有属性字典__dict__了,统一归__slots__管,节省内存





# def tpyey(a):
#
#     def deco(attr):
#         print("this is deco")
#         setattr(attr,"name",5)
#         return attr
#
#     return deco
#
#
# @tpyey(5)
# class cls:
#     print("this is class")
#
# print(cls.__dict__)


# def func1(x):
#     num=1
#     for i in range(1,x+1):
#         num*=i
#     return num
#
# res=0
# for i in range(1,21):
#     res+=func1(i)
# print(res)




# str1="55e5lofjr4i4kg67"
# m=len(str1) - 1
# for n in str1:
#     print(str1[m])
#     m-=1

