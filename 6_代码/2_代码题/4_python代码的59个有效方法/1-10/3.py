# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# https://www.cnblogs.com/xiaobingqianrui/p/9870480.html
# https://blog.csdn.net/csdnnews/article/details/83052809


# 一个字节8个位 ASCII码，一种8位即1个字节的编码规范
# UNICODE的万国码，它规定任何一个字符（不管哪国的）至少以2个字节表示，可以更多。
# UTF-8很快就得到了广泛的应用。 它规定英文字母系列用1个字节表示，汉字用3个字节表示等等

# 第三条 了解bytes、str、unicode的区别
# 一个unicode可能是一个字节或者两个字节
# bytes表示二进制流 str表示一个或者多个unicode
# 在编写python程序，一定要把编码和解码操作放在界面最外围来做，encode或者decode
# 在python3中，bytes是一种包含8位值的序列，str是一种包含unicode字符的序列，不能进行+
# 从文件中读取二进制数据，或向其中写入二进制数据时，总应该以'rb'或'wb'等二进制来开启文件
# 如果有前缀u，表示u编码，如果有前缀b，表示二进制流


