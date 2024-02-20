# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 第13条，合理利用try/except/else/finally结构中的每个代码块
#  1 try:
#  2     Nomal execution block
#  3 except A:
#  4     Exception A handle
#  5 except B:
#  6     Exception B handle
#  7 except:
#  8     Other Exception handle
#  9 else:
# 10     if no exception, get here
# 11 finally:
# 12     print('finally')

# try：正常执行的程序，如果执行过程中出现异常，则中断当前的程序执行，跳转到对应的异常处理模块中；
# except：（可选）如果异常与A/B相匹配，则跳转到对应的except A/B中执行；如果A、B中没有相对应的异常，则跳转到except中执行。
#          （这个except块是可选的，如果没有提供，则执行python默认的异常处理程序，即：中断执行，打印提示信息）
# else：（可选）如果try中的程序执行过程中没有发生错误，则会继续执行else中的程序；   （try成功else也执行，如果执行except，则不执行）
# finally：无论是否发生异常，只要提供了finally程序，就在执行所有步骤之后执行finally中的程序。
# 总的来说：
#
# 正常执行的程序在try下面执行，在执行中如果发生了异常，则中断当前执行然后执行except中的部分，如果没有异常即不执行except的情况下，则会执行else中的语句，finally语句是最后无论是否有异常都要执行的代码。
