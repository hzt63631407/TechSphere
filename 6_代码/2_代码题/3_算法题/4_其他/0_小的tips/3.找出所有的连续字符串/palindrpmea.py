# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。



def palindromea(a):
    l1 = []
    for i in range(0, len(a)):
        for j in range(i,len(a)+1):
            if i < j :
                l = a[i:j]
                l1.append(l)
    return l1


print(palindromea([1,2,3]))
