# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 第6条 在单次切片操作内，不要同时指定start、end和stride
# 如果要进行切割，可以考虑先转换成python的str
# *查看数据结构list