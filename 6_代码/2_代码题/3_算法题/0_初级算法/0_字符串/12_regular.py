# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

import re

# 比较实用
# 常用的字符串匹配 可以使用其找出自己想要的字符传
# pattern = re.compile(r'\d+')  # 查找数字

pattern = re.compile(r':" \d+ google')              # 查找数字  查找:" 123 google

result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob:" 123 google:" 456 google456')

print(result1)
print(result2)


# https://www.runoob.com/python3/python3-reg-expressions.html

# 匹配成功 re.match 方法返回一个匹配的对象，否则返回 None。
# 我们可以使用 group(num) 或 groups() 匹配对象函数来获取匹配表达式。

# group(num=0)	匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。

line = "Cats are smarter than dogs"

# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
# (.*?) 表示"非贪婪"模式，只保存第一个匹配到的子串
# matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)    # re.I 不区分大小写


matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)    # re.I 不区分大小写


if matchObj:
    print(matchObj)
    print ("matchObj.group() : ", matchObj.group())                         #   匹配成功
    print ("matchObj.group(0) : ", matchObj.group(0))                       #   匹配成功    返回全部
    print ("matchObj.group(1) : ", matchObj.group(1))                       #   匹配成功    返回第一个数组，Cats
    print ("matchObj.group(2) : ", matchObj.group(2))                       #   匹配成功    返回smarter？          因为？(.*?) 表示"非贪婪"模式，只保存第一个匹配到的子串
    # print ("matchObj.group(2) : ", matchObj.group(3))                     # 报错 IndexError: no such group
else:
    print ("No match!!")

# matchObj.group() :  Cats are smarter than dogs
# matchObj.group(1) :  Cats
# matchObj.group(2) :  smarter






# python的正则表达式默认是贪心的 它们会尽可能匹配最长的字符串
# 非贪心，匹配最短的字符串

#提取邮件地址、url
text = "Please contact us at contact@qq.com for further information."+\
        " You can also give feedbacl at feedback@yiibai.com"

emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
print(emails)


line ="Now a days you can learn almost anything by just visiting http://www.google.com. " \
      "But if you are completely new to computers or internet then first you need to leanr those"

urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', line)
print(urls)

