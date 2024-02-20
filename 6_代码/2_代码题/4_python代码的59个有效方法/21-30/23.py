# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 第23条，简单的接口应该接受函数，而不是类的实例
# api在执行的时候，会通过这些挂钩函数，回调函数的代码。
name = ['name','age','job']
name.sort(key=lambda x:len(x))
print(name)

# 剩余  复习