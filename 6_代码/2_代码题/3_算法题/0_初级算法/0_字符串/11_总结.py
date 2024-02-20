
# 1.替换
# s = s.replace(" ", "%20")         # 空格替换成%20

# https://blog.csdn.net/qq_45664055/article/details/118111074
# 2.切割
# a = s.split()                       # 如果没有参数，函数默认以空格，tab空格符，回车符等作为分割条件
# a = s.split(":")                    # 逗号切割
# a = s.split(".")                    # 句号切割
# print str.split(' ', 1 );           # 以空格为分隔符，分隔成两个

# "".join(s)            以空格形式将列表s转换成字符串     如：[1,2,3],123
# "/"+"/".join(s)       以/形式将列表s转换成字符串       如：[1,2,3],/1/2/3


# 使用正则表达式的re.split()方法，一次性拆分字符串
# 可以填入多个参数，而split只有一个
# import re
# s = "ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz"
# print re.split(r'[;|,\t]+',s)


# 3.大小写
# s.lower()                            # 变成小写
#  upper() -- 小写转大写：全部变成大写


# 4.判断相关
# s.isalnum                            # 如果字符传里面都是字母或者数字 返回Ture
# 数字用str.isdigit, 字母用 str.isalpha


# 5.filter函数    过滤
# s = filter(lambda n: n % 2 == 0, list(range(20)))
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


# filter(function, iterable)
# 参数
# function -- 判断函数。
# iterable -- 可迭代对象。
# 该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，
# 然后返回 True 或 False，最后将返回 True 的元素放到新列表中


# https://blog.csdn.net/suoluo_2020/article/details/118306146
# 6.join()          拼接
#  join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
# # list1=["1","2","3","4"]
# # result="".join(list1)
# # print(result) #1234

# 7.查找
# info = 'abca'
# print info.find('a')##从下标0开始，查找在字符串里第一个出现的子串，返回结果：0
# info = 'abca'
# print info.find('a',1)##从下标1开始，查找在字符串里第一个出现的子串：返回结果3
# index()方法：
# python 的index方法是在字符串里查找子串第一次出现的位置，
# 类似字符串的find方法，不过比find方法更好的是，如果查找不到子串，会抛出异常，而不是返回-1

# 其他
# https://blog.csdn.net/Zzzzzz_m/article/details/122588062

# 用正则表达式切分字符串比用固定的字符更灵活，请看正常的切分代码：
#
# >>> 'a b   c'.split(' ')
# ['a', 'b', '', '', 'c']
# 嗯，无法识别连续的空格，用正则表达式试试：
#
# >>> re.split(r'\s+', 'a b   c')
# ['a', 'b', 'c']
# 无论多少个空格都可以正常分割。加入,试试：
#
# >>> re.split(r'[\s\,]+', 'a,b, c  d')
# ['a', 'b', 'c', 'd']
# 再加入;试试：
#
# >>> re.split(r'[\s\,\;]+', 'a,b;; c  d')
# ['a', 'b', 'c', 'd']

