# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 菜鸟教程：https://www.runoob.com/python3/python3-string-split.html


# 参数
# str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
# num -- 分割次数。默认为 -1, 即分隔所有。


str = "this is string example....wow!!!"
print (str.split( ))       # 以空格为分隔符
print (str.split('i',1))   # 以 i 为分隔符           # 分割成2端
print (str.split('w'))     # 以 w 为分隔符



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


