
# 1.sort()
# list或者str进行调用
# 可以不传，也传key key是方法，
# 没有返回
def rule(m):
    if m % 2 == 0:
        return 1
    else:
        return 0

l = [1,2,3,4,5]
l.sort(key=rule)            # 不返回  l = l.sort(key=rule) 写法错误
print(l)                    # 0在前面，1在后面，如果有2，2在1后面

# 2 sorted()
# sorted(iterable, key=None, reverse=False)
# 输入是可以可迭代的对象，list，str，dir.item()(二维元祖)，元祖，字典，集合也可以，
# 可以不传key
# 有返回 需要定义变量返回
# 注意返回的是一个list
# def reverse(*args):
#     l1 = []
#     for i in args:
#         l1.append(i)
#     l1 = sorted(l1, key=lambda x: (x[0], -int(x[1]), x[2]))
#     return l1


