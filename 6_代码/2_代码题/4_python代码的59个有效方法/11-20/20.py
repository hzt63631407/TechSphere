# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 第20条，用None和文档字符串来描述具有动态默认值的参数
# 在python中，若想正确实现动态默认值，习惯上是把默认值设为None
# 如果参数的实际默认值是可变类型，那就一定要记得用None作为形式上的默认值。


# turtle.circle(r,extent=None)
# 你写了extent=None，说明调用这个函数的时候不穿参数也可以调用这个函数，里边的代码也可以被执行，但是里边的代码逻辑你要规避这个参数为空会出现的报错问题。

# def f(a, l = []):
#     l.append(a)
#     return l
#
# print(f(1)) # 1
# print(f(2)) # 1,2
# print(f(3)) # 1,2,3

# 如果参数的实际默认值是可变类型，那就一定要记得用None作为形式上的默认值。        其他——id1
# 参数设置为none不会叠加，相当于重置了
def f(a, l = None):
    if l is None:
        l = []
    l.append(a)
    return l

print(f(1)) # 1
print(f(2)) # 2
print(f(3)) # 3



# https://www.zhihu.com/question/277548837/answer/394117084