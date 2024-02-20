# 编写一个程序，按升序对（名称，年龄，得分）元组进行排序，
# 其中name是字符串，age和height是数字。元组由控制台输入。
# 如果给出以下元组作为程序的输入：
# Tom，19，80
# John，20，90
# Johy，17，91
# Johy，17，93
# Json，21，85
# 然后，程序的输出应该是：
# [('John','20','90'),('Johy'，'17'，'91')，
# ('Johy'，'17'，'93'),('Josn'，'21'，'85'),
# ('Tom'，'19'，'80')]
class Reversinator(object):

    def __init__(self, obj):
        self.obj = obj

    def __lt__(self, other):
        return other.obj < self.obj

# https://blog.csdn.net/qq_36575363/article/details/108930409
# https://blog.csdn.net/qq_42636503/article/details/124573500
def reverse(*args):
    l1 = []
    for i in args:
        k = tuple(i)
        l1.append(k)
    print(type(l1))
    # l1.sort(key=lambda x: (x[0], x[1], x[2]))
    # l1 = sorted(l1, key=lambda x: (x[0], Reversinator(x[1]), x[2]))
    l1 = sorted(l1, key=lambda x: (x[0], -int(x[1]), x[2]))
    return l1

# 如果元祖的元素是"3"，可以用-x[1]，但是如果元素有"tom"这样的字母，就不能加负号，要写一个类。
# 或者可以把在先把类型装成int类型，然后再判断。

print(reverse(("tom", "12", "80"), ("John", "17", "80"), ("John", "21", "80"), ("Josn", "21", "80")))

# ls=[(1,2),(2,2),(5,4),(5,3),(8,4)]

# 字典排序
# >>> persons = [{'name': 'Dong', 'age': 37, 'height': 170},
#            {'name': 'Zhang', 'age': 40, 'height': 172},
#            {'name': 'Dong', 'age': 37, 'height': 171},
#            {'name': 'Zhang', 'age': 50, 'height': 173},
#            {'name': 'Dong', 'age': 43, 'height': 170},
#            {'name': 'Zhang', 'age': 40, 'height': 171}]
# >>> print(sorted(persons, key=lambda person: (person['name'], -person['age'], -person['height']))


# https://blog.csdn.net/u013193903/article/details/81096367