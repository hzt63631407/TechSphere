# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 第21条，用只能以关键字形式指定的参数来确保代码明晰
# def save(number,*,ignore=false) 有* 所以必须指定ignore是否为false

def save(number,*,ignore=False):
        print(number)
        print(ignore)


# save(1,2,3)     TypeError: save() takes 1 positional argument but 3 were given
save(1,ignore=False)            # 有* 所以必须设置ignore是否为false