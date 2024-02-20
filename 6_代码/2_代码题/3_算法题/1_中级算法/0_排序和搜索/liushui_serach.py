# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。


def serach(a,list):
    res = []
    for k in list:
        for i in range(0, len(a)):
            if a[i] in k:
                if i == len(a)-1:
                    res.append(k)
                continue
            if a[i] not in k:
                break
    return res

a = "12"
list = ["12","13","134","124","142"]
print(serach(a,list))

