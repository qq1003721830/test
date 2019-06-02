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


import os
# print os.getcwd()
# os.chdir("..")
# print os.getcwd()
# # os.makedirs("子目录3/子目录4")
# os.chdir(os.pardir)
# os.chdir(os.curdir)
# print os.getcwd()
# print os.curdir
# print  os.pardir

# os.rmdir("子目录4") ???
print os.listdir()
# os.renames("+.py","-.py")

print os.getcwd()
print os.getcwd()
print os.getcwd()
print os.getcwd()
print os.getcwd()
print os.getcwd()
print os.getcwd()
print os.getcwd()

