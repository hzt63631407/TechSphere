# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。


def substring(str):
    if str == str[::-1]:
        return True
    else:
        return False

print(substring('1213'))


