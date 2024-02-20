# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 第31条 用描述符来改写需要复用的@propert方法
# 简单地说： 某个类，只要是内部定义了方法 __get__, __set__, __delete__ 中的一个或多个，就可以称为描述符
# class Grade(object):
#     def __get__(self, instance, owner):
#         # ...
#     def __set__(self, instance, value):
#         # ...
#
# class Exam(object):
#     math_grade = Grade()
#     writing = Grade()
#     sciencen_grade = Grade()


# 使用set和get的属性 让外部可以定义也可以调用 设置为私有是因为不让外部随意定义属性

# 其他
# class Animal(object):
#     @property
#     def height(self):
#         return self._height
#     @height.setter
#     def height(self, value):
#         if not isinstance(value, float):
#             raise ValueError("高度应该是小数")
#         if value < 0 or value > 300:
#             raise ValueError("高度范围是0到300cm")
#         self._height = value
#
# d = Animal()
# d.height = 250.9
# print(d.height) --------------> 250.9
